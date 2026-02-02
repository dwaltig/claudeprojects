#!/usr/bin/env python3
"""
Add breaks for long verse sections (50+ lines = ~500+ words when set to single line format).
This creates narration breaks within extended verse passages in ElevenReader.
"""

import re

INPUT_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/lotus_sutra_for_elevenreader_FORMATTED.txt"
OUTPUT_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/lotus_sutra_for_elevenreader_FORMATTED_v2.txt"

# Read file
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Verse markers - when these appear, the next section is verse
verse_start_markers = [
    'spoke in verse',
    'sings it out in verse',
    'sings out his own verse',
    'sings it in verse',
    'spoke in verse, saying',
    'spoke in verse, wishing',
    'wishing to say it again',
    'wanting to say it again in another way',
    'these verses had rhythm',
]

# Section end markers - when these appear, the verse is over
section_end_markers = [
    r'^THE ',
    r'^CHAPTER ',
    r'--- CHAPTER',
    r'^INTERPRETATION NOTES:',
]

# Track position
result_lines = []
i = 0

while i < len(lines):
    current_line = lines[i].rstrip('\n')
    result_lines.append(lines[i])

    # Check if this line contains a verse start marker
    has_verse_marker = any(marker.lower() in current_line.lower() for marker in verse_start_markers)

    if has_verse_marker:
        # Start of verse section found
        # Now count lines until we hit the end marker
        verse_start_idx = i + 1
        verse_line_count = 0

        j = verse_start_idx
        while j < len(lines):
            check_line = lines[j].rstrip('\n')

            # Check if this is a section end marker
            is_end = any(re.match(pattern, check_line) for pattern in section_end_markers)

            if is_end:
                # We've found the end of the verse section
                break

            verse_line_count += 1
            j += 1

        # Now process the verse section with line breaks every 50 lines
        # (roughly 500+ words when converted to single-line format)
        lines_processed = 0

        while i + 1 < len(lines):
            next_line = lines[i + 1].rstrip('\n')

            # Check if we've hit the end marker
            is_section_end = any(re.match(pattern, next_line) for pattern in section_end_markers)
            if is_section_end:
                break

            i += 1
            lines_processed += 1

            # Add break every 50 lines within verse section
            if lines_processed > 0 and lines_processed % 50 == 0:
                # Add blank line before next verse line to create narration break
                if next_line.strip():  # Only if next line isn't blank
                    result_lines.append('\n')

            result_lines.append(lines[i])

    i += 1

# Join and clean up
content = ''.join(result_lines)
content = re.sub(r'\n\n\n+', r'\n\n', content)

# Write output
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Long verse breaks added successfully!")
print(f"Output: {OUTPUT_FILE}")
print(f"\nFormatting applied:")
print("- Detected all verse sections (marked by 'spoke in verse', etc.)")
print("- Added breaks every 50 lines within long verse passages")
print("- This creates natural narration pauses every ~500 words in extended verses")
print("- Optimized for ElevenReader audiobook narration")
print(f"\n📊 Processing complete:")
print(f"- Original: {len(open(INPUT_FILE).readlines())} lines")
print(f"- With breaks: {len(open(OUTPUT_FILE).readlines())} lines")
