#!/usr/bin/env python3
"""
Add breaks for long verse sections (500+ lines) in the ElevenReader file.
Verses are identified as sections that start after verse announcement markers.
"""

import re

INPUT_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/lotus_sutra_for_elevenreader_FORMATTED.txt"
OUTPUT_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/lotus_sutra_for_elevenreader_FORMATTED_v2.txt"

# Read file
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# Patterns that indicate start of a verse section
verse_start_patterns = [
    r'(?:spoke in verse|sings|spoke|sings it out)',
    r'(?:And then .+ wanting .+ spoke in verse)',
    r'(?:verses had rhythm)',
    r'(?:That Brahma-voice)',
]

# Split into paragraphs for analysis
lines = content.split('\n')

# Track position and add breaks
result_lines = []
current_section_start = 0
in_verse_section = False
verse_section_start_line = 0

for i, line in enumerate(lines):
    # Check if this line contains a verse start marker
    is_verse_marker = any(re.search(pattern, line, re.IGNORECASE) for pattern in verse_start_patterns)

    if is_verse_marker:
        in_verse_section = True
        verse_section_start_line = i
        result_lines.append(line)
        continue

    # If we were in a verse section, check if we've reached the end
    if in_verse_section:
        # Verse ends when we hit:
        # 1. A section header (THE ... or INTERPRETATION NOTES:)
        # 2. A new chapter marker
        # 3. A new CHAPTER title

        is_section_end = (
            (line.startswith('THE ') and line.isupper()) or
            line.startswith('--- CHAPTER') or
            (line.startswith('CHAPTER ') and ':' in line) or
            line == 'INTERPRETATION NOTES:'
        )

        if is_section_end:
            # We've reached the end of the verse section
            verse_length = i - verse_section_start_line

            # If verse section was over 500 lines, it likely needs breaks
            if verse_length > 50:  # More conservative threshold for practical breaks
                # Add break before this new section
                if result_lines and result_lines[-1].strip():
                    result_lines.append('')

            in_verse_section = False

        result_lines.append(line)
    else:
        result_lines.append(line)

# Join and clean up excessive blank lines
content = '\n'.join(result_lines)
content = re.sub(r'\n\n\n+', r'\n\n', content)

# Write output
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Long verse breaks added!")
print(f"Output: {OUTPUT_FILE}")
print(f"\nFormatting applied:")
print("- Identified verse sections (marked by 'spoke in verse', etc.)")
print("- Added breaks before sections following long verses (50+ lines)")
print("- Ready for ElevenReader with natural pause points between verse and prose")
