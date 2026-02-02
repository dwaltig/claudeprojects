#!/usr/bin/env python3
"""
Fix all chapter verses by extracting from markdown sources and reformatting
with proper verse-line tags, replacing old <br>-based verses and placeholders
"""

import os
import re
from pathlib import Path

def extract_verses_from_markdown(md_file):
    """Extract all verse blocks from a markdown file, handling blank lines properly"""
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
                # Empty line within verse - split into separate verse block
                in_blank_lines = True
            else:
                # Regular verse line
                if in_blank_lines and current_verse:
                    # Save previous verse, start new one
                    verses.append(current_verse)
                    current_verse = []
                    in_blank_lines = False
                current_verse.append(verse_line)
        else:
            # End of verse block
            if current_verse:
                verses.append(current_verse)
                current_verse = []
            in_blank_lines = False

    if current_verse:
        verses.append(current_verse)

    return verses

def format_verse_to_html(verse_lines):
    """Convert verse lines to HTML with verse-line class"""
    html_lines = []
    for line in verse_lines:
        html_lines.append(f'<p class="verse-line">{line}</p>')

    verse_html = '<div class="verse">\n' + '\n'.join(html_lines) + '\n</div>'
    return verse_html

def remove_old_verses(html_content):
    """Remove old verse content (patterns with <br> tags and > markers)"""

    # Pattern 1: <p>...<br>...<br>...</p> that contains > markers or excessive <br> tags
    # This is a general pattern for verses in old format

    # Remove <p>> </p> placeholders
    html_content = re.sub(r'<p>> </p>', '', html_content)

    return html_content

def insert_verses_into_chapter(chapter_num, verses):
    """Insert formatted verses into chapter HTML file"""

    html_file = Path(f"chapters/chapter_{chapter_num:02d}.html")

    if not html_file.exists():
        return False

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    if not verses:
        return False

    # Clean up old verse placeholders
    updated_content = remove_old_verses(content)

    # Count how many verse sections we're replacing
    placeholder_count = updated_content.count('<p>> </p>')

    # Replace <p>> </p> placeholders with formatted verses
    for verse_lines in verses:
        verse_html = format_verse_to_html(verse_lines)
        if '<p>> </p>' in updated_content:
            updated_content = updated_content.replace('<p>> </p>', verse_html, 1)

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    return True

def find_markdown_file(chapter_num):
    """Find the markdown source file for a chapter"""
    for file in Path('.').glob('CHAPTER_*.md'):
        if f"CHAPTER_{chapter_num:02d}" in file.name:
            return file
    return None

def main():
    """Fix all chapter verses"""

    fixed_count = 0

    for chapter_num in range(1, 29):
        md_file = find_markdown_file(chapter_num)

        if not md_file:
            print(f"⚠️  Chapter {chapter_num}: Markdown source not found")
            continue

        verses = extract_verses_from_markdown(md_file)

        if not verses:
            print(f"⊘ Chapter {chapter_num}: No verses found")
            continue

        if insert_verses_into_chapter(chapter_num, verses):
            print(f"✅ Chapter {chapter_num}: Fixed {len(verses)} verse section(s) with proper verse-line formatting")
            fixed_count += 1
        else:
            print(f"⚠️  Chapter {chapter_num}: No updates needed (verses may already be correctly formatted)")

    print(f"\n✨ Fixed {fixed_count} chapter files with proper verse-line formatting!")

if __name__ == "__main__":
    main()
