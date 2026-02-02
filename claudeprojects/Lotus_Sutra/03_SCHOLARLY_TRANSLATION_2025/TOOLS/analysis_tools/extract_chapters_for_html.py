#!/usr/bin/env python3
"""Extract chapter content from markdown files and generate JavaScript code for embedding."""

import os
import re
import json
from pathlib import Path

def extract_chapter_content(filepath):
    """Extract main content from a chapter markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the main content section (skip metadata/header)
    # Split by '## Prose Section' or look for main content after title
    lines = content.split('\n')

    # Find chapter title from first h1
    title = ""
    content_start = 0
    for i, line in enumerate(lines):
        if line.startswith('# '):
            title = line.replace('# ', '').strip()
            content_start = i + 1
            break

    # Extract prose and verse sections
    prose_section = []
    verse_section = []
    in_verse = False

    for i in range(content_start, len(lines)):
        line = lines[i]

        # Skip metadata sections
        if line.startswith('## Apparatus Summary') or line.startswith('## Philosophical Implications'):
            break

        # Skip section headers but process content
        if line.startswith('##'):
            if 'Verse' in line:
                in_verse = True
            elif 'Prose' in line:
                in_verse = False
            continue

        # Skip footnote definitions
        if line.startswith('[^'):
            continue

        # Add content
        if line.strip() and not line.startswith('['):
            if in_verse:
                verse_section.append(line)
            else:
                prose_section.append(line)

    # Clean up content
    prose_text = '\n'.join(prose_section).strip()
    verse_text = '\n'.join(verse_section).strip()

    # Remove markdown formatting but keep basic structure
    prose_text = re.sub(r'\[\^[\d]+\]', '', prose_text)  # Remove footnote references
    verse_text = re.sub(r'\[\^[\d]+\]', '', verse_text)

    # Truncate if very long (keep first ~1500 chars for demo)
    if len(prose_text) > 2000:
        prose_text = prose_text[:2000] + "..."

    return title, prose_text, verse_text

def get_chapter_titles():
    """Get chapter titles in order."""
    titles = {
        1: "Introduction",
        2: "Skillful Means",
        3: "Parables",
        4: "Faith and Understanding",
        5: "Medicinal Herbs",
        6: "Prophecies",
        7: "Phantom City",
        8: "Five Hundred Disciples",
        9: "Learning and Unlearning Disciples",
        10: "Dharma Teacher",
        11: "Emergence of Prabhutaratna Stupa",
        12: "Devadatta and Naga Princess",
        13: "Exhortation to Uphold",
        14: "Peaceful Practice",
        15: "Emergence of Bodhisattvas",
        16: "Buddha's Eternal Lifespan",
        17: "Discrimination of Merits",
        18: "Merit of Rejoicing",
        19: "Dharma Teacher Merits",
        20: "Never Despiser",
        21: "Tathagata's Supernatural Powers",
        22: "Entrustment",
        23: "Medicine King Bodhisattva",
        24: "Wonderful Sound Bodhisattva",
        25: "Avalokiteshvara",
        26: "Dharani Protective Formulas",
        27: "Wonderful Adornment King",
        28: "Samantabhadra's Encouragement"
    }
    return titles

def main():
    base_path = Path('/Users/williamaltig/claudeprojects/Lotus_Sutra/03_SCHOLARLY_TRANSLATION_2025')

    chapters_data = {}
    titles = get_chapter_titles()

    # Process each chapter
    for ch_num in range(1, 29):
        filename = f'CHAPTER_{ch_num:02d}_*.md'

        # Find matching file
        matching_files = list(base_path.glob(filename))
        if not matching_files:
            print(f"Warning: No file found for chapter {ch_num}")
            continue

        filepath = matching_files[0]
        print(f"Processing {filepath.name}...")

        try:
            title, prose, verse = extract_chapter_content(filepath)

            # Create HTML content
            html_content = f'<div class="chapter-title">Chapter {ch_num}: {titles[ch_num]}</div>'
            html_content += '<div>'

            if prose:
                # Add prose with some basic paragraph breaks
                paras = [p.strip() for p in prose.split('\n\n') if p.strip()]
                for para in paras[:3]:  # Limit to first 3 paragraphs
                    html_content += f'<p>{para}</p>'

            if verse:
                # Add verse section
                html_content += '<div class="verse">'
                verse_lines = [l.strip() for l in verse.split('\n') if l.strip()]
                html_content += '<br>'.join(verse_lines[:8])  # Limit to 8 lines
                html_content += '</div>'

            html_content += '</div>'

            chapters_data[str(ch_num)] = {
                "title": f"Chapter {ch_num}: {titles[ch_num]}",
                "content": html_content
            }

        except Exception as e:
            print(f"Error processing chapter {ch_num}: {e}")

    # Generate JavaScript output
    print("\n" + "="*60)
    print("JAVASCRIPT CODE FOR CHAPTERS OBJECT:")
    print("="*60 + "\n")

    print("const CHAPTERS = {")
    for ch_num in sorted([int(k) for k in chapters_data.keys()]):
        ch_key = str(ch_num)
        data = chapters_data[ch_key]
        # Escape backticks and quotes in content
        content = data['content'].replace('\\', '\\\\').replace('`', '\\`')
        print(f'"{ch_num}": {{title:"{data["title"]}",content:`{content}`}},')
    print("};")

    print(f"\n✓ Generated data for {len(chapters_data)} chapters")

if __name__ == '__main__':
    main()
