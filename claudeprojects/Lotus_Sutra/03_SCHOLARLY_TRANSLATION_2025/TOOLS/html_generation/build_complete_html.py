#!/usr/bin/env python3
"""Build complete lotus.html with all 28 chapters embedded."""

import json
from pathlib import Path

def escape_js_string(s):
    """Escape string for JavaScript."""
    s = s.replace('\\', '\\\\')
    s = s.replace('`', '\\`')
    s = s.replace('$', '\\$')
    return s

def main():
    base_path = Path('/Users/williamaltig/claudeprojects/Lotus_Sutra/03_SCHOLARLY_TRANSLATION_2025')

    # Load chapter data
    with open(base_path / 'chapters_data.json', 'r', encoding='utf-8') as f:
        chapters_data = json.load(f)

    # Generate chapter options HTML
    chapter_options = '<option value="">Select Chapter</option>\n'
    for ch_num in sorted([int(k) for k in chapters_data.keys()]):
        title = chapters_data[str(ch_num)]['title']
        chapter_options += f'                    <option value="{ch_num}">{title}</option>\n'

    # Generate chapters JavaScript object
    chapters_js = 'const CHAPTERS = {\n'
    for ch_num in sorted([int(k) for k in chapters_data.keys()]):
        ch_data = chapters_data[str(ch_num)]
        title = ch_data['title']
        content = escape_js_string(ch_data['content'])
        chapters_js += f'"{ch_num}": {{title:"{title}",content:`{content}`}},\n'
    chapters_js += '};\n'

    # Read the current lotus.html to get the template
    with open(base_path / 'lotus.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Find and replace chapter options
    start_opt = html_content.find('<select class="chapter-select" id="ch"')
    if start_opt != -1:
        end_opt = html_content.find('</select>', start_opt) + 9
        old_options_section = html_content[start_opt:end_opt]

        # Extract the select tag opening
        select_opening = old_options_section.split('\n')[0]
        new_options_section = select_opening + '\n' + chapter_options + '                </select>'

        html_content = html_content[:start_opt] + new_options_section + html_content[end_opt:]

    # Find and replace CHAPTERS object
    start_chapters = html_content.find('// CHAPTER DATA\nconst CHAPTERS')
    if start_chapters != -1:
        end_chapters = html_content.find('};', start_chapters) + 2
        old_chapters_section = html_content[start_chapters:end_chapters]

        new_chapters_section = '// CHAPTER DATA (All 28 Chapters)\n' + chapters_js

        html_content = html_content[:start_chapters] + new_chapters_section + html_content[end_chapters:]

    # Also update the sidebar header count
    html_content = html_content.replace('<h3>Concepts (75)</h3>', '<h3>Concepts (65)</h3>')

    # Save the updated HTML
    output_path = base_path / 'lotus_complete.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✓ Created {output_path.name}")
    print(f"  - 28 chapters embedded")
    print(f"  - Chapter selector with all 28 options")
    print(f"  - File size: {len(html_content) / 1024:.1f} KB")
    print(f"\nOpen in browser: {output_path}")

if __name__ == '__main__':
    main()
