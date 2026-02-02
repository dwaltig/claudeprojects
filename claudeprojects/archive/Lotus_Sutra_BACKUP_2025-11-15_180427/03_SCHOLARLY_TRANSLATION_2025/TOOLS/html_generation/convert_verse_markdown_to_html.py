#!/usr/bin/env python3
"""
Convert markdown formatting in verse lines to HTML
- *text* → <em>text</em>
- **text** → <strong>text</strong>
- Apply to all chapters
"""

import re
from pathlib import Path

def convert_markdown_to_html(text):
    """Convert markdown formatting to HTML"""

    # Convert **bold** to <strong> (must be before *italic*)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)

    # Convert *italic* to <em>
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)

    # Convert _italic_ to <em>
    text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)

    return text

def fix_verse_markdown_in_chapter(chapter_num):
    """Fix markdown formatting in verse lines for a chapter"""

    html_file = Path(f"chapters/chapter_{chapter_num:02d}.html")

    if not html_file.exists():
        return 0

    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    if '<p class="verse-line">' not in html_content:
        return 0

    original_content = html_content
    replacements_made = 0

    # Find all verse-line paragraphs
    pattern = r'<p class="verse-line">(.*?)</p>'

    def replace_verse_line(match):
        nonlocal replacements_made
        line_content = match.group(1)

        # Skip if already has HTML tags (like <em> or <strong>)
        if '<' in line_content and '>' in line_content:
            return match.group(0)

        # Check if it has markdown formatting
        if '*' in line_content or '_' in line_content:
            converted = convert_markdown_to_html(line_content)
            if converted != line_content:
                replacements_made += 1
                return f'<p class="verse-line">{converted}</p>'

        return match.group(0)

    html_content = re.sub(pattern, replace_verse_line, html_content, flags=re.DOTALL)

    # Write back only if changes were made
    if html_content != original_content:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

    return replacements_made

def main():
    """Fix markdown formatting in all chapter verses"""

    print(f"\n{'='*80}")
    print("CONVERTING VERSE MARKDOWN FORMATTING TO HTML")
    print(f"{'='*80}\n")

    total_converted = 0

    for chapter_num in range(1, 29):
        print(f"Chapter {chapter_num:2d}: ", end="", flush=True)

        conversions = fix_verse_markdown_in_chapter(chapter_num)

        if conversions > 0:
            print(f"✅ Converted {conversions} verse line(s)")
            total_converted += conversions
        else:
            print(f"✓ No markdown formatting found")

    print(f"\n{'='*80}")
    print(f"✨ MARKDOWN CONVERSION COMPLETE!")
    print(f"{'='*80}")
    print(f"Total verse lines converted: {total_converted}")
    print(f"All verses now have HTML formatting instead of markdown")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    main()
