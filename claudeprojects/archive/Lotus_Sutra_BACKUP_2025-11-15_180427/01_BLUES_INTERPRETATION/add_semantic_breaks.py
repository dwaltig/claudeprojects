#!/usr/bin/env python3
"""
Add semantic verse breaks at natural thought boundaries.
Breaks verses at:
1. Sentence endings (periods followed by capital letter or new speaker)
2. Stanza breaks (natural line groupings)
3. End of concepts (when word count exceeds 500+ words)

Works with the continuous verse format in the file.
"""

import re

INPUT_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/lotus_sutra_for_elevenreader_FORMATTED_v1_backup.txt"
OUTPUT_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/lotus_sutra_for_elevenreader_FORMATTED.txt"

# Read file
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Verse markers
verse_start_markers = [
    'spoke in verse',
    'sings it out',
    'sings out',
    'wishing to say it again',
    'wanting to say it again',
    'these verses had rhythm',
]

result_lines = []
i = 0
in_verse = False
verse_word_count = 0
last_period_line = -1

while i < len(lines):
    current_line = lines[i].rstrip('\n')

    # Check if this line starts a verse section
    has_verse_marker = any(marker.lower() in current_line.lower() for marker in verse_start_markers)

    if has_verse_marker:
        in_verse = True
        verse_word_count = 0
        result_lines.append(current_line + '\n')
        i += 1
        continue

    # If we're in a verse, check for end condition
    if in_verse:
        # Check if this line is a section header (ends verse)
        if (current_line and current_line.isupper() and
            current_line.startswith(('THE ', 'CHAPTER ', '---', 'INTERPRETATION'))):
            in_verse = False
            result_lines.append(current_line + '\n')
            i += 1
            continue

        # We're still in verse - add the line and track word count
        result_lines.append(current_line + '\n')
        verse_word_count += len(current_line.split())

        # Check if this line ends a sentence (period at end)
        # and we've accumulated 500+ words
        if current_line.rstrip().endswith('.') and verse_word_count >= 500:
            # Add a blank line for break
            result_lines.append('\n')
            verse_word_count = 0  # Reset counter

        i += 1
    else:
        # Not in verse, just add the line
        result_lines.append(current_line + '\n')
        i += 1

# Join all lines
content = ''.join(result_lines)

# Clean up excessive blank lines (more than 2 in a row)
content = re.sub(r'\n\n\n+', r'\n\n', content)

# Write output
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Semantic verse breaks added!")
print(f"Output: {OUTPUT_FILE}")
print(f"\nBreaking strategy:")
print("✓ Detects verse sections (spoke in verse, etc.)")
print("✓ Tracks word count within verses")
print("✓ Breaks ONLY at sentence endings (periods)")
print("✓ Break trigger: 500+ words + period at end of line")
print("✓ Preserves all subsection headers (ALLCAPS)")
print("✓ Natural, semantic break points for narration")

# Count breaks added
original_lines = len(open(INPUT_FILE).readlines())
new_lines = len(open(OUTPUT_FILE).readlines())
breaks_added = new_lines - original_lines

print(f"\n📊 Results:")
print(f"Original lines: {original_lines}")
print(f"New lines: {new_lines}")
print(f"Breaks added: {breaks_added}")
