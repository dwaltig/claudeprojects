#!/usr/bin/env python3
"""
Convert markdown study guides into formatted HTML pages with navigation
"""

import os
import re
from pathlib import Path

# Define the chapters
CHAPTERS = {
    1: "Introduction", 2: "Skillful Means", 3: "Parables", 4: "Faith & Understanding",
    5: "Medicinal Herbs", 6: "Prophecies", 7: "Phantom City", 8: "Five Hundred Disciples",
    9: "Learning & Unlearning Disciples", 10: "Dharma-Teacher", 11: "Emergence of Prabhūtaratna's Stupa",
    12: "Devadatta and the Nāga Princess", 13: "Exhortation to Uphold", 14: "Peaceful Practice",
    15: "Emergence of Bodhisattvas from the Earth", 16: "Buddha's Eternal Lifespan",
    17: "Discrimination of Merits", 18: "Merit of Rejoicing", 19: "Dharma-Teacher's Merits",
    20: "Never-Despiser Bodhisattva", 21: "Tathāgata's Supernatural Powers", 22: "Entrustment",
    23: "Medicine King's Original Practice", 24: "Wonderful-Sound Bodhisattva", 25: "Avalokiteśvara",
    26: "Dharani of Protective Formulas", 27: "Wonderful-Adornment King's Original Practice",
    28: "Samantabhadra's Vows"
}

def get_previous_chapter(chapter_num):
    """Get the previous chapter number"""
    if chapter_num > 1:
        return chapter_num - 1
    return None

def get_next_chapter(chapter_num):
    """Get the next chapter number"""
    if chapter_num < 28:
        return chapter_num + 1
    return None

def markdown_to_html(md_text):
    """Convert basic markdown to HTML with proper verse/blockquote handling"""
    html = md_text

    # FIRST: Handle blockquotes/verses (lines starting with >)
    # This must be done before paragraph processing to preserve line breaks
    lines = html.split('\n')
    processed_lines = []
    in_blockquote = False
    blockquote_lines = []

    for line in lines:
        if line.strip().startswith('>'):
            # Remove the '>' and leading/trailing spaces
            verse_line = line.strip()[1:].strip()
            blockquote_lines.append(verse_line)
            in_blockquote = True
        else:
            # If we were in a blockquote and now we're not, close it
            if in_blockquote and blockquote_lines:
                # Convert each blockquote line to its own <p class="verse-line"> tag
                verse_lines_html = []
                for v_line in blockquote_lines:
                    verse_lines_html.append(f'<p class="verse-line">{v_line}</p>')
                verse_html = '<div class="verse">\n' + '\n'.join(verse_lines_html) + '\n</div>'
                processed_lines.append(verse_html)
                blockquote_lines = []
                in_blockquote = False
            processed_lines.append(line)

    # Don't forget to close any remaining blockquote
    if in_blockquote and blockquote_lines:
        verse_lines_html = []
        for v_line in blockquote_lines:
            verse_lines_html.append(f'<p class="verse-line">{v_line}</p>')
        verse_html = '<div class="verse">\n' + '\n'.join(verse_lines_html) + '\n</div>'
        processed_lines.append(verse_html)

    html = '\n'.join(processed_lines)

    # Convert headers
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.*?)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)

    # Convert bold and italic
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    html = re.sub(r'_(.*?)_', r'<em>\1</em>', html)

    # Convert code blocks
    html = re.sub(r'`(.*?)`', r'<code>\1</code>', html)

    # Convert lists
    html = re.sub(r'^\- (.*?)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.*?</li>)', r'<ul>\1</ul>', html, flags=re.DOTALL)
    html = html.replace('</ul>\n<ul>', '\n')

    # Convert line breaks to paragraphs (but not for <div class="verse"> blocks)
    paragraphs = html.split('\n\n')
    html_paras = []
    for para in paragraphs:
        para = para.strip()
        if para and not para.startswith('<'):
            para = f'<p>{para}</p>'
        html_paras.append(para)
    html = '\n'.join(html_paras)

    return html

def extract_sections(md_content):
    """Extract the main sections from markdown"""
    sections = {}

    # Extract chapter number and title from first heading
    match = re.search(r'# Chapter (\d+).*?: (.*?)(?:\n|$)', md_content)
    if match:
        sections['chapter_num'] = int(match.group(1))
        sections['chapter_title'] = match.group(2).strip()

    # Split by main ## headers to identify sections
    # Pattern: any ## heading that starts a new section
    main_sections = re.split(r'^## ', md_content, flags=re.MULTILINE)

    # Skip the first empty match (before the first ##)
    main_sections = main_sections[1:]

    # Build a dict of section name -> content
    section_map = {}
    for section in main_sections:
        lines = section.split('\n', 1)
        if len(lines) == 2:
            section_name = lines[0].strip().lower()
            section_content = lines[1].strip()
            section_map[section_name] = section_content

    # Map the actual markdown sections to our 12-section display structure

    # 1. Overview
    if 'chapter overview' in section_map:
        sections['overview'] = section_map['chapter overview']

    # 2. Introduction - usually the section after overview explaining the topic
    # Look for sections with topic names (like "Understanding...", "The Teaching...", etc)
    intro_keys = [k for k in section_map.keys() if 'understanding' in k or 'the ' in k or 'what is' in k]
    if intro_keys:
        # Combine all intro-like sections
        intro_content = []
        for key in sorted(intro_keys):
            intro_content.append(section_map[key])
        sections['introduction'] = '\n\n---\n\n'.join(intro_content)

    # 3. Learning objectives
    if 'learning objectives' in section_map:
        sections['objectives'] = section_map['learning objectives']

    # 4. Key passages
    if 'key passages' in section_map or 'key passages to return to' in section_map:
        key = next((k for k in section_map.keys() if 'passages' in k), None)
        if key:
            sections['passages'] = section_map[key]

    # 5. Reflection questions
    if 'reflection questions' in section_map:
        sections['reflections'] = section_map['reflection questions']

    # 6. Practice applications
    if 'practice applications' in section_map:
        sections['practices'] = section_map['practice applications']

    # 7. Meditation
    meditation_keys = [k for k in section_map.keys() if 'meditation' in k]
    if meditation_keys:
        sections['meditation'] = '\n\n---\n\n'.join(section_map[k] for k in meditation_keys)

    # 8. Discussion questions
    if 'discussion questions' in section_map or 'discussion questions (for groups)' in section_map:
        key = next((k for k in section_map.keys() if 'discussion' in k), None)
        if key:
            sections['discussion'] = section_map[key]

    # 9. Cross-references
    if 'cross-references' in section_map or 'cross-references' in section_map:
        key = next((k for k in section_map.keys() if 'cross' in k), None)
        if key:
            sections['cross_references'] = section_map[key]

    # 10. Pacing options
    if 'pacing options' in section_map:
        sections['pacing'] = section_map['pacing options']

    # 11. Integration section
    integration_keys = [k for k in section_map.keys() if 'integration' in k or 'how this teaching' in k]
    if integration_keys:
        sections['integration'] = section_map[integration_keys[0]]

    # 12. Key takeaway - look for closing sections
    takeaway_keys = [k for k in section_map.keys() if 'takeaway' in k or 'closing' in k or 'key insight' in k]
    if takeaway_keys:
        sections['takeaway'] = section_map[takeaway_keys[0]]
    elif 'key takeaway' in section_map:
        sections['takeaway'] = section_map['key takeaway']

    return sections

def generate_html_page(chapter_num, sections):
    """Generate an HTML page for a study guide"""

    prev_ch = get_previous_chapter(chapter_num)
    next_ch = get_next_chapter(chapter_num)

    nav_html = '<div class="chapter-nav">'
    if prev_ch:
        nav_html += f'<a href="chapter_{prev_ch:02d}.html" class="nav-button">← Chapter {prev_ch}</a>'
    nav_html += f'<span class="chapter-indicator">Chapter {chapter_num} of 28</span>'
    if next_ch:
        nav_html += f'<a href="chapter_{next_ch:02d}.html" class="nav-button">Chapter {next_ch} →</a>'
    nav_html += '</div>'

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter {chapter_num}: {sections.get('chapter_title', 'Lotus Sutra')} - Study Guide</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.8;
            color: #333;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }}

        header {{
            background: linear-gradient(135deg, #16a085 0%, #128070 100%);
            color: white;
            padding: 2rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}

        header h1 {{
            font-size: 2.2em;
            margin-bottom: 0.5rem;
        }}

        header p {{
            font-size: 1em;
            opacity: 0.95;
        }}

        .container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
        }}

        .chapter-nav {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
            padding: 1rem;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}

        .nav-button {{
            padding: 0.75rem 1.5rem;
            background: linear-gradient(135deg, #16a085 0%, #128070 100%);
            color: white;
            text-decoration: none;
            border-radius: 4px;
            transition: all 0.3s ease;
            font-weight: 500;
        }}

        .nav-button:hover {{
            transform: translateX(3px);
            box-shadow: 0 4px 8px rgba(22, 160, 133, 0.3);
        }}

        .chapter-indicator {{
            color: #666;
            font-weight: 500;
        }}

        .back-link {{
            display: inline-block;
            margin-bottom: 1.5rem;
            padding: 0.75rem 1.5rem;
            background: white;
            color: #16a085;
            text-decoration: none;
            border-radius: 4px;
            transition: all 0.3s ease;
            font-weight: 500;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}

        .back-link:hover {{
            background: #16a085;
            color: white;
        }}

        .content {{
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }}

        h2 {{
            color: #16a085;
            margin-top: 2rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #16a085;
            font-size: 1.6em;
        }}

        h2:first-child {{
            margin-top: 0;
        }}

        h3 {{
            color: #128070;
            margin-top: 1.5rem;
            margin-bottom: 0.8rem;
            font-size: 1.2em;
        }}

        h4 {{
            color: #333;
            margin-top: 1rem;
            margin-bottom: 0.6rem;
            font-size: 1.05em;
        }}

        p {{
            margin-bottom: 1rem;
        }}

        ul, ol {{
            margin-left: 2rem;
            margin-bottom: 1rem;
        }}

        li {{
            margin-bottom: 0.5rem;
        }}

        strong {{
            color: #128070;
            font-weight: 600;
        }}

        em {{
            color: #666;
            font-style: italic;
        }}

        code {{
            background: #f5f5f5;
            padding: 0.2rem 0.4rem;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            color: #d63384;
        }}

        blockquote {{
            border-left: 4px solid #16a085;
            padding-left: 1rem;
            margin: 1.5rem 0;
            color: #666;
            font-style: italic;
        }}

        .verse {{
            border-left: 4px solid #16a085;
            margin: 1.5rem 0;
            color: #555;
            background: #f9f9f9;
            padding: 1.5rem;
            border-radius: 4px;
        }}

        .verse-line {{
            margin: 0.5rem 0;
            font-style: italic;
            line-height: 1.8;
            color: #555;
        }}

        .verse-line:first-child {{
            margin-top: 0;
        }}

        .verse-line:last-child {{
            margin-bottom: 0;
        }}

        .section {{
            margin-bottom: 2rem;
            padding: 1.5rem;
            background: #f9f9f9;
            border-radius: 6px;
            border-left: 4px solid #16a085;
        }}

        footer {{
            background: #2c3e50;
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
        }}

        .toc {{
            background: #ecf0f1;
            padding: 1.5rem;
            border-radius: 6px;
            margin-bottom: 2rem;
        }}

        .toc h3 {{
            margin-top: 0;
        }}

        .toc ul {{
            list-style: none;
            margin-left: 0;
        }}

        .toc li {{
            margin-bottom: 0.5rem;
        }}

        .toc a {{
            color: #16a085;
            text-decoration: none;
            font-weight: 500;
        }}

        .toc a:hover {{
            text-decoration: underline;
        }}

        @media (max-width: 768px) {{
            header h1 {{
                font-size: 1.6em;
            }}

            .container {{
                padding: 1rem;
            }}

            .chapter-nav {{
                flex-direction: column;
                gap: 1rem;
            }}

            .nav-button {{
                width: 100%;
                text-align: center;
            }}
        }}
    </style>
</head>
<body>
    <header>
        <h1>🌸 Chapter {chapter_num}: {sections.get('chapter_title', 'Study Guide')}</h1>
        <p>Comprehensive Study Guide for the Lotus Sutra</p>
    </header>

    <div class="container">
        <a href="index.html" class="back-link">← Back to All Study Guides</a>

        {nav_html}

        <div class="content">
            <div class="toc">
                <h3>📑 Guide Contents</h3>
                <ul>
                    <li><a href="#overview">Chapter Overview</a></li>
                    <li><a href="#introduction">Key Teaching Introduction</a></li>
                    <li><a href="#objectives">Learning Objectives</a></li>
                    <li><a href="#passages">Key Passages</a></li>
                    <li><a href="#reflections">Reflection Questions</a></li>
                    <li><a href="#practices">Practice Applications</a></li>
                    <li><a href="#meditation">Meditation Guide</a></li>
                    <li><a href="#discussion">Discussion Questions</a></li>
                    <li><a href="#cross">Cross-References</a></li>
                    <li><a href="#pacing">Pacing Options</a></li>
                    <li><a href="#integration">Integration Section</a></li>
                    <li><a href="#takeaway">Key Takeaway</a></li>
                </ul>
            </div>

            <div id="overview" class="section">
                <h2>📖 Chapter Overview</h2>
                {markdown_to_html(sections.get('overview', ''))}
            </div>

            <div id="introduction" class="section">
                <h2>🔑 Key Teaching Introduction</h2>
                {markdown_to_html(sections.get('introduction', ''))}
            </div>

            <div id="objectives" class="section">
                <h2>🎯 Learning Objectives</h2>
                {markdown_to_html(sections.get('objectives', ''))}
            </div>

            <div id="passages" class="section">
                <h2>💎 Key Passages with Commentary</h2>
                {markdown_to_html(sections.get('passages', ''))}
            </div>

            <div id="reflections" class="section">
                <h2>💭 Reflection Questions</h2>
                {markdown_to_html(sections.get('reflections', ''))}
            </div>

            <div id="practices" class="section">
                <h2>🧘 Practice Applications</h2>
                {markdown_to_html(sections.get('practices', ''))}
            </div>

            <div id="meditation" class="section">
                <h2>🧘‍♀️ Meditation Guide</h2>
                {markdown_to_html(sections.get('meditation', ''))}
            </div>

            <div id="discussion" class="section">
                <h2>💬 Discussion Questions</h2>
                {markdown_to_html(sections.get('discussion', ''))}
            </div>

            <div id="cross" class="section">
                <h2>🔗 Cross-References</h2>
                {markdown_to_html(sections.get('cross_references', ''))}
            </div>

            <div id="pacing" class="section">
                <h2>⏱️ Pacing Options</h2>
                {markdown_to_html(sections.get('pacing', ''))}
            </div>

            <div id="integration" class="section">
                <h2>🌱 Integration Section</h2>
                {markdown_to_html(sections.get('integration', ''))}
            </div>

            <div id="takeaway" class="section">
                <h2>✨ Key Takeaway</h2>
                {markdown_to_html(sections.get('takeaway', ''))}
            </div>
        </div>

        {nav_html}
    </div>

    <footer>
        <p>&copy; 2025 Lotus Sutra Scholarly Translation Project</p>
        <p><a href="index.html" style="color: white; text-decoration: none;">View All Study Guides</a></p>
    </footer>
</body>
</html>
"""
    return html

def main():
    """Generate HTML pages for all study guides"""

    guide_dir = Path("_PRACTICE_LAYER/02_Chapter_Study_Guides")
    output_dir = Path("_PRACTICE_LAYER/02_Chapter_Study_Guides/html")
    output_dir.mkdir(exist_ok=True)

    generated = 0

    for chapter_num in range(1, 29):
        md_file = guide_dir / f"CHAPTER_{chapter_num:02d}_STUDY_GUIDE.md"

        if md_file.exists():
            print(f"Processing Chapter {chapter_num}...", end=" ")

            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    md_content = f.read()

                sections = extract_sections(md_content)
                html_content = generate_html_page(chapter_num, sections)

                output_file = output_dir / f"chapter_{chapter_num:02d}.html"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(html_content)

                print("✅")
                generated += 1

            except Exception as e:
                print(f"❌ Error: {e}")
        else:
            print(f"Chapter {chapter_num}: Guide not found")

    print(f"\n✨ Generated {generated} HTML study guide pages!")
    print(f"📁 Output directory: {output_dir}")

if __name__ == "__main__":
    main()
