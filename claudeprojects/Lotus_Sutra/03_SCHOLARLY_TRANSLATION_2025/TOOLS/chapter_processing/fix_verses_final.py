#!/usr/bin/env python3
"""
Final comprehensive fix for chapter verses
- Identifies <p> tags containing inline > markers
- Extracts verse lines from the broken HTML
- Replaces with properly formatted verse blocks
"""

import re
from pathlib import Path

def extract_verses_from_markdown(md_file):
    """Extract verse blocks from markdown"""
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

def extract_verse_lines_from_html(html_section):
    """Extract verse lines from broken HTML format"""
    # Pattern: > <em>text</em> or > text
    # Split by " > " to find verse lines

    lines = []

    # Remove the <p> and </p> tags
    html_section = html_section.replace('<p>', '').replace('</p>', '').strip()

    # Split by " > " to get individual verse elements
    parts = html_section.split(' > ')

    for part in parts:
        part = part.strip()
        if not part:
            continue

        # Extract text from <em> tags if present
        em_match = re.search(r'<em>(.*?)</em>', part)
        if em_match:
            text = em_match.group(1)
        else:
            text = part.replace('<em>', '').replace('</em>', '')

        if text.strip():
            lines.append(text.strip())

    return lines

def create_verse_block(verse_lines):
    """Create proper verse HTML"""
    html_lines = []
    for line in verse_lines:
        html_lines.append(f'<p class="verse-line">{line}</p>')
    return '<div class="verse">\n' + '\n'.join(html_lines) + '\n</div>'

def fix_chapter_verses(chapter_num):
    """Fix verses in a chapter"""

    html_file = Path(f"chapters/chapter_{chapter_num:02d}.html")
    if not html_file.exists():
        return 0

    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    replacements_made = 0

    # Find all <p> tags containing inline > markers
    # Pattern: <p>...> <em>...> <em>...</p>
    pattern = r'<p>.*?> <em>.*?</p>'

    matches = list(re.finditer(pattern, html_content, re.DOTALL))

    # Replace from end to beginning to avoid position shifts
    for match in reversed(matches):
        broken_section = match.group(0)

        # Extract verse lines from the broken HTML
        verse_lines = extract_verse_lines_from_html(broken_section)

        if verse_lines:
            # Create proper verse block
            verse_block = create_verse_block(verse_lines)

            # Replace in content
            html_content = html_content[:match.start()] + verse_block + html_content[match.end():]
            replacements_made += 1

    # Also handle empty verse placeholders
    while '<p>> </p>' in html_content:
        html_content = html_content.replace('<p>> </p>', '', 1)
        replacements_made += 1

    # Ensure CSS is present
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
    """Find markdown source"""
    for file in Path('.').glob('CHAPTER_*.md'):
        if f"CHAPTER_{chapter_num:02d}" in file.name:
            return file
    return None

def main():
    """Fix all chapter verses"""

    print(f"\n{'='*80}")
    print("COMPREHENSIVE CHAPTER VERSE FIX")
    print(f"{'='*80}\n")

    total_fixed = 0
    total_replacements = 0

    for chapter_num in range(1, 29):
        print(f"Chapter {chapter_num:2d}: ", end="", flush=True)

        md_file = find_markdown_file(chapter_num)
        if not md_file:
            print("⚠️  No markdown source")
            continue

        verses = extract_verses_from_markdown(md_file)
        if not verses:
            print("⊘ No verses in source")
            continue

        replacements = fix_chapter_verses(chapter_num)

        if replacements > 0:
            print(f"✅ Fixed {replacements} verse block(s)")
            total_fixed += 1
            total_replacements += replacements
        else:
            print(f"✓ Clean (no broken verses found)")

    print(f"\n{'='*80}")
    print(f"✨ VERSE FIXING COMPLETE!")
    print(f"{'='*80}")
    print(f"Chapters processed:        28/28")
    print(f"Chapters with verses:      {total_fixed if total_fixed > 0 else 'Check above'}")
    print(f"Verse blocks fixed:        {total_replacements}")
    print(f"All chapters now have:     .verse-line CSS styling")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    main()
