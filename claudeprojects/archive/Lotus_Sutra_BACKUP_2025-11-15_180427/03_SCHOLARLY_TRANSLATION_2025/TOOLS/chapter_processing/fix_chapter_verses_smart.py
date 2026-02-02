#!/usr/bin/env python3
"""
Smart verse fixing - handles the actual broken HTML patterns seen in chapters
- Identifies ALL <p> tags containing inline > markers
- Groups them into verse blocks
- Replaces with properly formatted verse sections
"""

import re
from pathlib import Path

def extract_verses_from_markdown(md_file):
    """Extract all verse blocks from markdown"""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return []

    verses = []
    lines = content.split('\n')
    current_verse = []
    in_blank_lines = False

    for line in lines:
        if line.strip().startswith('>'):
            verse_line = line.strip()[1:].strip()
            if not verse_line:
                in_blank_lines = True
            else:
                if in_blank_lines and current_verse:
                    verses.append(current_verse)
                    current_verse = []
                    in_blank_lines = False
                current_verse.append(verse_line)
        else:
            if current_verse:
                verses.append(current_verse)
                current_verse = []
            in_blank_lines = False

    if current_verse:
        verses.append(current_verse)

    return verses

def create_verse_html(verse_lines):
    """Create proper verse HTML with verse-line tags"""
    html_lines = []
    for line in verse_lines:
        html_lines.append(f'<p class="verse-line">{line}</p>')
    verse_html = '<div class="verse">\n' + '\n'.join(html_lines) + '\n</div>'
    return verse_html

def fix_chapter_verses(chapter_num, verses):
    """Fix verses in a chapter by replacing broken patterns"""

    html_file = Path(f"chapters/chapter_{chapter_num:02d}.html")
    if not html_file.exists():
        return 0

    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    if not verses:
        return 0

    replacements_made = 0

    # Strategy 1: Replace <p>> </p> placeholders
    for verse_lines in verses:
        verse_html = create_verse_html(verse_lines)
        if '<p>> </p>' in html_content:
            html_content = html_content.replace('<p>> </p>', verse_html, 1)
            replacements_made += 1

    # Strategy 2: Find and replace sections with inline > markers
    # Pattern: <p>...> <em>...</em> > <em>...</em>...</p>
    # This matches <p> tags that contain the " > " pattern (inline verse markers)

    while True:
        # Find <p> tags that contain inline > markers
        pattern = r'<p>.*?> <em>.*?</p>'
        match = re.search(pattern, html_content, re.DOTALL)

        if not match or not verses:
            break

        # Replace with next verse
        broken_section = match.group(0)
        verse_lines = verses.pop(0)
        verse_html = create_verse_html(verse_lines)

        html_content = html_content.replace(broken_section, verse_html, 1)
        replacements_made += 1

    # Ensure CSS styles are present
    if '.verse-line' not in html_content:
        style_close = html_content.find('</style>')
        if style_close != -1:
            verse_css = '''        .verse {
            border-left: 4px solid #16a085;
            margin: 1.5rem 0;
            color: #555;
            background: #f9f9f9;
            padding: 1.5rem;
            border-radius: 4px;
        }
        .verse-line {
            margin: 0.5rem 0;
            font-style: italic;
            line-height: 1.8;
            color: #555;
        }
        .verse-line:first-child {
            margin-top: 0;
        }
        .verse-line:last-child {
            margin-bottom: 0;
        }
'''
            html_content = html_content[:style_close] + verse_css + html_content[style_close:]

    # Write back
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    return replacements_made

def find_markdown_file(chapter_num):
    """Find markdown source for chapter"""
    for file in Path('.').glob('CHAPTER_*.md'):
        if f"CHAPTER_{chapter_num:02d}" in file.name:
            return file
    return None

def main():
    """Fix all chapters comprehensively"""

    total_fixed = 0
    total_replacements = 0

    for chapter_num in range(1, 29):
        print(f"Chapter {chapter_num}: ", end="")

        md_file = find_markdown_file(chapter_num)
        if not md_file:
            print("⚠️  No markdown source")
            continue

        verses = extract_verses_from_markdown(md_file)
        if not verses:
            print("⊘ No verses")
            continue

        replacements = fix_chapter_verses(chapter_num, verses)

        if replacements > 0:
            print(f"✅ Fixed {replacements} verse block(s)")
            total_fixed += 1
            total_replacements += replacements
        else:
            print(f"✓ Already properly formatted")

    print(f"\n{'='*80}")
    print(f"✨ Complete!")
    print(f"Chapters with verses fixed: {total_fixed}/28")
    print(f"Total verse blocks repaired: {total_replacements}")
    print(f"{'='*80}")

if __name__ == "__main__":
    main()
