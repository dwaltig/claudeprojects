#!/usr/bin/env python3
"""
Convert all Practice Layer markdown files to beautifully formatted HTML
"""

import os
import re
from pathlib import Path

def markdown_to_html(md_text):
    """Convert markdown to HTML with verse/blockquote handling"""
    html = md_text

    # FIRST: Handle blockquotes/verses (lines starting with >)
    lines = html.split('\n')
    processed_lines = []
    in_blockquote = False
    blockquote_lines = []

    for line in lines:
        if line.strip().startswith('>'):
            verse_line = line.strip()[1:].strip()
            blockquote_lines.append(verse_line)
            in_blockquote = True
        else:
            if in_blockquote and blockquote_lines:
                verse_html = '<div class="verse">' + '<br>\n'.join(blockquote_lines) + '</div>'
                processed_lines.append(verse_html)
                blockquote_lines = []
                in_blockquote = False
            processed_lines.append(line)

    if in_blockquote and blockquote_lines:
        verse_html = '<div class="verse">' + '<br>\n'.join(blockquote_lines) + '</div>'
        processed_lines.append(verse_html)

    html = '\n'.join(processed_lines)

    # Convert headers
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.*?)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)

    # Convert bold and italic
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    html = re.sub(r'_(.*?)_', r'<em>\1</em>', html)

    # Convert code blocks
    html = re.sub(r'`(.*?)`', r'<code>\1</code>', html)

    # Convert lists (handle both - and * markers)
    html = re.sub(r'^\- (.*?)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'^\* (.*?)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.*?</li>)', r'<ul>\1</ul>', html, flags=re.DOTALL)
    html = html.replace('</ul>\n<ul>', '\n')

    # Convert numbered lists
    html = re.sub(r'^\d+\. (.*?)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.*?</li>)', r'<ol>\1</ol>', html, flags=re.DOTALL)
    html = html.replace('</ol>\n<ol>', '\n')

    # Convert line breaks to paragraphs
    paragraphs = html.split('\n\n')
    html_paras = []
    for para in paragraphs:
        para = para.strip()
        if para and not para.startswith('<'):
            para = f'<p>{para}</p>'
        html_paras.append(para)
    html = '\n'.join(html_paras)

    return html

def get_title_from_md(md_content):
    """Extract title from markdown"""
    match = re.search(r'^#\s+(.+?)(?:\n|$)', md_content)
    if match:
        return match.group(1).strip()
    return "Practice Material"

def generate_html_page(material_name, title, content, back_link="index.html"):
    """Generate an HTML page for practice material"""

    html_content = markdown_to_html(content)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Lotus Sutra Practice</title>
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
            padding: 2.5rem;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }}

        h1 {{
            color: #16a085;
            margin: 1.5rem 0 1rem 0;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #16a085;
            font-size: 2em;
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

        .verse {{
            border-left: 4px solid #16a085;
            padding-left: 1.5rem;
            margin: 1.5rem 0;
            color: #555;
            font-style: italic;
            line-height: 1.8;
            white-space: pre-wrap;
            word-wrap: break-word;
            background: #f9f9f9;
            padding: 1rem 1.5rem;
            border-radius: 4px;
        }}

        .section {{
            margin-bottom: 2rem;
            padding: 1.5rem;
            background: #f9f9f9;
            border-radius: 6px;
            border-left: 4px solid #16a085;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.5rem 0;
        }}

        th {{
            background: #16a085;
            color: white;
            padding: 0.8rem;
            text-align: left;
        }}

        td {{
            padding: 0.8rem;
            border-bottom: 1px solid #ddd;
        }}

        tr:hover {{
            background: #f9f9f9;
        }}

        footer {{
            background: #2c3e50;
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
        }}

        footer a {{
            color: #16a085;
            text-decoration: none;
        }}

        footer a:hover {{
            text-decoration: underline;
        }}

        @media (max-width: 768px) {{
            header h1 {{
                font-size: 1.6em;
            }}

            .container {{
                padding: 1rem;
            }}

            .content {{
                padding: 1.5rem;
            }}

            h2 {{
                font-size: 1.3em;
            }}

            h3 {{
                font-size: 1.1em;
            }}
        }}
    </style>
</head>
<body>
    <header>
        <h1>🌸 {title}</h1>
        <p>Lotus Sutra Practice Layer</p>
    </header>

    <div class="container">
        <a href="{back_link}" class="back-link">← Back to Practice Layer</a>

        <div class="content">
            {html_content}
        </div>
    </div>

    <footer>
        <p>&copy; 2025 Lotus Sutra Scholarly Translation Project</p>
        <p><a href="{back_link}">Practice Layer Hub</a> | <a href="../../index.html">Back to Main Site</a></p>
    </footer>
</body>
</html>
"""
    return html

def convert_file(md_path, output_dir, back_link="index.html"):
    """Convert a single markdown file to HTML"""

    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        title = get_title_from_md(md_content)
        html_content = generate_html_page(md_path.stem, title, md_content, back_link)

        # Generate output filename
        output_name = md_path.stem.lower().replace(' ', '_').replace('_guide', '') + '.html'
        output_path = output_dir / output_name

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        return True, output_name
    except Exception as e:
        return False, str(e)

def main():
    """Convert all practice layer materials to HTML"""

    base_dir = Path("_PRACTICE_LAYER")

    # Define conversions: (source_dir, output_dir, back_link)
    conversions = [
        ("00_START_HERE", "00_START_HERE", "../index.html"),
        ("01_Study_Programs", "01_Study_Programs", "../index.html"),
        ("03_Daily_Practice", "03_Daily_Practice", "../index.html"),
        ("04_Meditation_Practice", "04_Meditation_Practice", "../index.html"),
        ("05_Group_Practice", "05_Group_Practice", "../index.html"),
        ("06_Advanced_Practice", "06_Advanced_Practice", "../index.html"),
    ]

    total_converted = 0

    for source_dir, output_dir, back_link in conversions:
        source_path = base_dir / source_dir
        output_path = base_dir / output_dir

        if not source_path.exists():
            print(f"⚠️  Directory not found: {source_dir}")
            continue

        output_path.mkdir(exist_ok=True, parents=True)

        # Find all markdown files
        md_files = list(source_path.glob("*.md"))

        for md_file in md_files:
            success, result = convert_file(md_file, output_path, back_link)
            if success:
                print(f"✅ {source_dir}: {result}")
                total_converted += 1
            else:
                print(f"❌ {source_dir}/{md_file.name}: {result}")

    print(f"\n✨ Converted {total_converted} practice layer materials to HTML!")
    print(f"📁 Access at: _PRACTICE_LAYER/index.html")

if __name__ == "__main__":
    main()
