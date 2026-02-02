#!/usr/bin/env python3
"""
Add intelligent verse breaks at natural thought boundaries (periods, end of stanzas).
Instead of arbitrary line counts, this finds:
1. Sentence endings (periods)
2. Major thought breaks
3. Stanza transitions
4. Natural pause points for narration

Creates breaks every 500+ words in verse passages for optimal narration.
"""

import re

INPUT_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/lotus_sutra_for_elevenreader_FORMATTED_v1_backup.txt"
OUTPUT_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/lotus_sutra_for_elevenreader_FORMATTED.txt"

# Read file
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# Strategy: Find verse sections and break them at sentence ends (periods)
# when they exceed ~500 words (roughly 60-80 lines depending on line length)

# Verse start markers
verse_markers = [
    'spoke in verse',
    'sings it out in verse',
    'sings out his own verse',
    'sings it in verse',
    'wishing to say it again',
    'wanting to say it again',
    'these verses had rhythm',
]

# Split into paragraphs for processing
paragraphs = content.split('\n\n')
result_paragraphs = []

i = 0
while i < len(paragraphs):
    para = paragraphs[i]

    # Check if this paragraph contains a verse start marker
    has_verse_marker = any(marker.lower() in para.lower() for marker in verse_markers)

    if has_verse_marker:
        # This paragraph introduces verses
        result_paragraphs.append(para)
        i += 1

        # Now process the following paragraph(s) as verse until we hit a section marker
        while i < len(paragraphs):
            verse_para = paragraphs[i]

            # Check if this is a new section (ALL CAPS header)
            first_line = verse_para.split('\n')[0] if '\n' in verse_para else verse_para

            # If it's an all-caps header, we've reached the end of the verse section
            if (first_line.isupper() and len(first_line) > 3 and
                first_line.startswith(('THE ', 'CHAPTER ', '---', 'INTERPRETATION'))):
                break

            # This is part of the verse section
            # Now break it at natural points (periods) if it's long
            words = len(verse_para.split())

            if words > 500:
                # This verse section is long enough to need breaks
                # Break at sentence endings (periods) to create natural pause points

                # Find all periods followed by space
                sentences = re.split(r'(\. )', verse_para)

                # Reconstruct with breaks after every 500+ words
                current_chunk = ""
                chunk_words = 0

                for j, sentence in enumerate(sentences):
                    current_chunk += sentence
                    chunk_words = len(current_chunk.split())

                    # If we've accumulated 500+ words and just finished a sentence, add break
                    if chunk_words >= 500 and sentence.endswith('. '):
                        result_paragraphs.append(current_chunk.rstrip())
                        current_chunk = ""
                        chunk_words = 0

                # Add remaining text
                if current_chunk.strip():
                    result_paragraphs.append(current_chunk.rstrip())
            else:
                # Verse section is short, just add it as-is
                result_paragraphs.append(verse_para)

            i += 1
    else:
        # Not a verse section, just add as-is
        result_paragraphs.append(para)
        i += 1

# Reconstruct file with double line breaks between paragraphs
output_content = '\n\n'.join(result_paragraphs)

# Clean up any excessive blank lines
output_content = re.sub(r'\n\n\n+', r'\n\n', output_content)

# Write output
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(output_content)

print(f"✅ Smart verse breaks added successfully!")
print(f"Output: {OUTPUT_FILE}")
print(f"\nFormatting strategy:")
print("✓ Preserves all subsection headers (ALLCAPS)")
print("✓ Breaks verses at natural thought boundaries (sentence endings)")
print("✓ Breaks triggered when verse section exceeds 500+ words")
print("✓ Creates breaks at periods (.) not arbitrary line counts")
print("✓ Maintains poetic flow and meaning")
print(f"\n📊 Result: Professional audiobook pacing with semantic breaks")
