#!/usr/bin/env python3
"""
Reorganize notes in the Shikshasamucchaya audiobook:
- Move all Endnotes sections to the end of the book
- Keep Theological Notes and Bluesman's Notes at the end of their chapters
"""

import re

def reorganize_notes(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split content into sections by chapter markers
    # Chapter pattern: "# Chapter N: Title"
    chapter_pattern = r'^# Chapter \d+:.*?$'

    # Find all chapters
    chapters = re.split(f'({chapter_pattern})', content, flags=re.MULTILINE)

    # chapters[0] is the front matter before first chapter
    # Then alternating: chapter_title, chapter_content, chapter_title, chapter_content...

    front_matter = chapters[0]
    chapter_list = []
    collected_endnotes = []

    # Process chapters (pairs of title + content)
    i = 1
    while i < len(chapters):
        if i + 1 < len(chapters):
            chapter_title = chapters[i]
            chapter_content = chapters[i + 1]

            # Extract chapter number for endnotes heading
            chapter_num_match = re.search(r'Chapter (\d+)', chapter_title)
            chapter_num = chapter_num_match.group(1) if chapter_num_match else "?"

            # Find and extract Endnotes sections
            # Pattern 1: ## Endnotes (level 2 heading) - used in most chapters
            endnotes_pattern_h2 = r'^## Endnotes\n(.*?)(?=^## |\Z)'
            endnotes_match_h2 = re.search(endnotes_pattern_h2, chapter_content, flags=re.MULTILINE | re.DOTALL)

            # Pattern 2: # Endnotes (level 1 heading) - used in Chapter 1
            endnotes_pattern_h1 = r'^# Endnotes\n(.*?)(?=^# Chapter |\Z)'
            endnotes_match_h1 = re.search(endnotes_pattern_h1, chapter_content, flags=re.MULTILINE | re.DOTALL)

            if endnotes_match_h2:
                endnotes_text = endnotes_match_h2.group(1).strip()
                # Remove endnotes from chapter content
                chapter_content = re.sub(endnotes_pattern_h2, '', chapter_content, flags=re.MULTILINE | re.DOTALL)
                # Collect endnotes with chapter heading
                collected_endnotes.append(f"### Chapter {chapter_num}\n\n{endnotes_text}")
            elif endnotes_match_h1:
                endnotes_text = endnotes_match_h1.group(1).strip()
                # Remove endnotes from chapter content
                chapter_content = re.sub(endnotes_pattern_h1, '', chapter_content, flags=re.MULTILINE | re.DOTALL)
                # Collect endnotes with chapter heading
                collected_endnotes.append(f"### Chapter {chapter_num}\n\n{endnotes_text}")

            # Clean up extra blank lines
            chapter_content = re.sub(r'\n{3,}', '\n\n', chapter_content)

            chapter_list.append((chapter_title, chapter_content))
            i += 2
        else:
            i += 1

    # Reconstruct the book
    reconstructed = front_matter

    for title, content in chapter_list:
        reconstructed += title + content

    # Add all endnotes at the end
    if collected_endnotes:
        reconstructed += "\n\n---\n\n# Endnotes\n\n"
        reconstructed += "\n\n---\n\n".join(collected_endnotes)
        reconstructed += "\n"

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(reconstructed)

    print(f"✓ Reorganized notes")
    print(f"✓ Moved {len(collected_endnotes)} chapter endnote sections to end of book")
    print(f"✓ Output written to: {output_file}")

if __name__ == "__main__":
    input_file = "/Users/williamaltig/claudeprojects/Sutra_Projects/Shikshasamucchaya/SHIKSHASAMUCCHAYA_COMPLETE_BLUES_AUDIOBOOK.md"
    output_file = "/Users/williamaltig/claudeprojects/Sutra_Projects/Shikshasamucchaya/SHIKSHASAMUCCHAYA_COMPLETE_BLUES_AUDIOBOOK.md"

    reorganize_notes(input_file, output_file)
