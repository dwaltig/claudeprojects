#!/usr/bin/env python3
"""
Add proper breaks (double line breaks) for ElevenLabs audiobook production.
Each chapter and subsection will have distinct pause points for narration.
"""

import re

INPUT_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/lotus_sutra_for_elevenreader.txt"
OUTPUT_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/lotus_sutra_for_elevenreader_FORMATTED.txt"

# Read the file
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# List of patterns that should have breaks added BEFORE them
# These are subsection headers that don't start with --- or CHAPTER
subsection_patterns = [
    r'(?<!^)\n(THE [A-Z][A-Z\s\-\']*)\n',  # Subsections like "THE GATHERING"
    r'(?<!^)\n(INTERPRETATION NOTES:)\n',  # Interpretation notes
]

# Add double line breaks before CHAPTER headers
content = re.sub(r'\n(--- CHAPTER)', r'\n\n\1', content)

# Add double line breaks before CHAPTER titles
content = re.sub(r'\n(CHAPTER [A-Z]+:)', r'\n\n\1', content)

# Add double line breaks before subsection headers (THE ...)
# This regex finds lines that start with "THE " and are uppercase
lines = content.split('\n')
result_lines = []

for i, line in enumerate(lines):
    # Check if this is a subsection header (starts with THE and is all caps/title case)
    if line.strip() and line.startswith('THE ') and line.isupper():
        # Add extra line break before subsection if not already present
        if i > 0 and result_lines and result_lines[-1].strip():
            result_lines.append('')  # Add blank line

    result_lines.append(line)

content = '\n'.join(result_lines)

# Add proper spacing around INTERPRETATION NOTES sections
content = re.sub(r'\n(INTERPRETATION NOTES:)\n', r'\n\n\1\n', content)

# Clean up any triple or more line breaks (keep max 2)
content = re.sub(r'\n\n\n+', r'\n\n', content)

# Write output
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ File formatted successfully!")
print(f"Output: {OUTPUT_FILE}")
print(f"\nFormatting applied:")
print("- Double line breaks before each CHAPTER header")
print("- Double line breaks before each subsection (THE ...)")
print("- Double line breaks around INTERPRETATION NOTES sections")
print("- Triple+ breaks cleaned to prevent excessive pauses")
print(f"\nReady for ElevenLabs upload!")
