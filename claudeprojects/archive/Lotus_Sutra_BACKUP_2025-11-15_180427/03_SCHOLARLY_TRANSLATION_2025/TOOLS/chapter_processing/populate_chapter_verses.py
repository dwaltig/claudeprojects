#!/usr/bin/env python3
"""
Extract verses from chapter markdown files and populate chapter HTML files
with proper verse-line formatting (each line in <p class="verse-line">)
"""

import os
import re
from pathlib import Path

def extract_verses_from_markdown(md_file):
    """Extract all verse blocks from a markdown file"""
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
            # Remove the '>' marker and leading/trailing spaces
            verse_line = line.strip()[1:].strip()

            # If this is an empty line within a verse (blank verse separator)
            if not verse_line:
                # Don't add empty lines - they'll naturally separate verse blocks
                in_blank_lines = True
            else:
                # Regular verse line
                if in_blank_lines and current_verse:
                    # We had a blank line, so treat this as a new verse block
                    verses.append(current_verse)
                    current_verse = []
                    in_blank_lines = False
                current_verse.append(verse_line)
        else:
            # End of verse block (non-verse line)
            if current_verse:
                verses.append(current_verse)
                current_verse = []
            in_blank_lines = False

    # Don't forget the last verse if file ends with one
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

def update_chapter_html(chapter_num, verses):
    """Update chapter HTML file with verses"""

    html_file = Path(f"chapters/chapter_{chapter_num:02d}.html")

    if not html_file.exists():
        print(f"⚠️  {html_file} not found")
        return False

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    if not verses:
        print(f"⚠️  Chapter {chapter_num}: No verses found")
        return False

    # First, try to replace verse placeholders <p>> </p>
    updated_content = content
    replacements_made = 0

    for verse_lines in verses:
        verse_html = format_verse_to_html(verse_lines)

        # Replace the first occurrence of <p>> </p> with the formatted verse
        if '<p>> </p>' in updated_content:
            updated_content = updated_content.replace('<p>> </p>', verse_html, 1)
            replacements_made += 1

    # If no placeholders found, the verses might already be in old <br> format
    # In that case, we don't replace (they're already there, just in old format)
    # This preserves verses that are already populated

    if replacements_made == 0 and '<p>> </p>' not in content:
        # Verses might already be in HTML (old <br> format)
        # Don't overwrite - verses are already there
        return False

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    return replacements_made > 0

def find_markdown_file(chapter_num):
    """Find the markdown source file for a chapter"""

    # List all files in current directory and find matching chapter file
    for file in Path('.').glob('CHAPTER_*.md'):
        # Check if filename contains the chapter number (e.g., CHAPTER_01, CHAPTER_02)
        if f"CHAPTER_{chapter_num:02d}" in file.name:
            return file

    return None

def main():
    """Populate all chapter HTML files with verses"""

    updated_count = 0

    for chapter_num in range(1, 29):
        # Find markdown source
        md_file = find_markdown_file(chapter_num)

        if not md_file:
            print(f"⚠️  Chapter {chapter_num}: Markdown source not found")
            continue

        # Extract verses
        verses = extract_verses_from_markdown(md_file)

        if not verses:
            print(f"⊘ Chapter {chapter_num}: No verses to extract")
            continue

        # Update HTML file
        if update_chapter_html(chapter_num, verses):
            print(f"✅ Chapter {chapter_num}: {len(verses)} verse section(s) populated with verse-line formatting")
            updated_count += 1
        else:
            print(f"❌ Chapter {chapter_num}: Failed to update")

    print(f"\n✨ Updated {updated_count} chapter files with verse-line formatted verses!")
    print(f"📁 Verses now in: chapters/chapter_XX.html")

if __name__ == "__main__":
    main()
