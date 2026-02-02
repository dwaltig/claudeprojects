#!/usr/bin/env python3
"""
Comprehensive rebuild of all chapter HTML verses:
- Extracts verses from markdown source files
- Identifies broken verse sections in HTML (containing > markers)
- Replaces with properly formatted verse-line tags
- Ensures all chapters have verse CSS styling
"""

import os
import re
from pathlib import Path

def extract_verses_from_markdown(md_file):
    """Extract all verse blocks from markdown, properly handling blank lines"""
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

def format_verse_lines(verse_lines):
    """Format verse lines as HTML with verse-line class"""
    html_lines = []
    for line in verse_lines:
        html_lines.append(f'<p class="verse-line">{line}</p>')
    return html_lines

def create_verse_html(verse_lines):
    """Create a complete verse block HTML"""
    html_lines = format_verse_lines(verse_lines)
    verse_html = '<div class="verse">\n' + '\n'.join(html_lines) + '\n</div>'
    return verse_html

def find_and_replace_broken_verses(html_content, verses):
    """
    Find broken verse sections in HTML and replace with properly formatted ones.
    Broken sections include:
    - Lines with inline > markers
    - Massive <p> tags with multiple > marks
    """

    if not verses:
        return html_content

    updated_html = html_content
    replacements_made = 0

    # Strategy: Replace <p>> </p> placeholders first (empty verses)
    for verse_lines in verses:
        if not verse_lines:
            continue

        verse_html = create_verse_html(verse_lines)

        # Pattern 1: <p>> </p> placeholders
        if '<p>> </p>' in updated_html:
            updated_html = updated_html.replace('<p>> </p>', verse_html, 1)
            replacements_made += 1
            continue

    # Strategy 2: Find and replace massive broken verse blocks
    # Pattern: <p>...> <em>...> <em>...> > <em>...</p>
    # This pattern indicates merged verse lines with inline > markers

    # Find all <p> tags that contain the " > " pattern (inline verse markers)
    pattern = r'<p>.*?> <em>.*?(?:> <em>.*?)*</p>'
    matches = re.finditer(pattern, updated_html, re.DOTALL)

    for match in matches:
        broken_block = match.group(0)

        # Check if this looks like a verse block (has multiple > markers)
        if broken_block.count('>') >= 2 and verses:
            # This is likely a broken verse block
            verse_html = create_verse_html(verses[0])
            updated_html = updated_html.replace(broken_block, verse_html, 1)
            verses.pop(0)
            replacements_made += 1

    return updated_html, replacements_made

def ensure_verse_css(html_content):
    """Ensure HTML file has verse and verse-line CSS styling"""

    # Check if .verse class already exists
    if '.verse' in html_content:
        # Check if .verse-line also exists
        if '.verse-line' in html_content:
            return html_content  # Already has both styles

    # Find the closing </style> tag
    style_close = html_content.find('</style>')
    if style_close == -1:
        return html_content  # No style section found

    # CSS to add
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

    # Insert CSS before </style>
    updated_html = html_content[:style_close] + verse_css + html_content[style_close:]
    return updated_html

def rebuild_chapter_html(chapter_num, verses):
    """Rebuild chapter HTML with properly formatted verses"""

    html_file = Path(f"chapters/chapter_{chapter_num:02d}.html")

    if not html_file.exists():
        return False, 0

    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    if not verses:
        return False, 0

    # Make a copy of verses list for this chapter
    chapter_verses = [v[:] for v in verses]  # Deep copy

    # Find and replace broken verses
    updated_html, replacements = find_and_replace_broken_verses(html_content, chapter_verses)

    # Ensure CSS styles are present
    updated_html = ensure_verse_css(updated_html)

    # Write back to file
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(updated_html)

    return replacements > 0, replacements

def find_markdown_file(chapter_num):
    """Find the markdown source file for a chapter"""
    for file in Path('.').glob('CHAPTER_*.md'):
        if f"CHAPTER_{chapter_num:02d}" in file.name:
            return file
    return None

def main():
    """Rebuild all chapter verses comprehensively"""

    total_chapters_fixed = 0
    total_replacements = 0

    for chapter_num in range(1, 29):
        print(f"Processing Chapter {chapter_num}...", end=" ")

        # Find markdown source
        md_file = find_markdown_file(chapter_num)

        if not md_file:
            print("⚠️  Markdown source not found")
            continue

        # Extract verses
        verses = extract_verses_from_markdown(md_file)

        if not verses:
            print("⊘ No verses found")
            continue

        # Rebuild chapter HTML with formatted verses
        was_fixed, replacements = rebuild_chapter_html(chapter_num, verses)

        if was_fixed:
            print(f"✅ Fixed {replacements} verse section(s)")
            total_chapters_fixed += 1
            total_replacements += replacements
        else:
            print(f"⊘ No broken verses found (already formatted or no replacements possible)")

    print(f"\n{'='*80}")
    print(f"✨ Comprehensive verse rebuild complete!")
    print(f"📊 Chapters fixed: {total_chapters_fixed}/28")
    print(f"📊 Verse sections repaired: {total_replacements}")
    print(f"📁 All chapter files updated: chapters/chapter_XX.html")
    print(f"{'='*80}")

if __name__ == "__main__":
    main()
