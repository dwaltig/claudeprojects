#!/usr/bin/env python3
"""
Add proper breaks (double line breaks) for ElevenLabs audiobook production.
Each chapter and subsection will have distinct pause points for narration.
"""

INPUT_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/lotus_sutra_for_elevenreader.txt"
OUTPUT_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/lotus_sutra_for_elevenreader_FORMATTED.txt"

# Read the file
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Process lines and add breaks
result_lines = []
for i, line in enumerate(lines):
    current_line = line.rstrip('\n')

    # Check if this line should have a break BEFORE it
    should_add_break = False

    # Check for chapter markers
    if current_line.startswith('--- CHAPTER'):
        should_add_break = True
    elif current_line.startswith('CHAPTER ') and ':' in current_line:
        should_add_break = True
    # Check for subsection headers (all caps, starting with THE, etc.)
    elif current_line.startswith('THE ') and current_line.isupper():
        # But only if previous line isn't blank and isn't a chapter header
        if result_lines and result_lines[-1].strip():
            should_add_break = True
    # Check for other subsection patterns
    elif current_line in ['INTERPRETATION NOTES:'] and result_lines and result_lines[-1].strip():
        should_add_break = True
    elif current_line.startswith('CHAPTER ') and current_line.isupper():
        should_add_break = True

    # Add break before line if needed
    if should_add_break and result_lines and result_lines[-1].strip():
        result_lines.append('\n')

    # Add the current line
    result_lines.append(current_line + '\n')

# Join all lines
content = ''.join(result_lines)

# Clean up excessive blank lines (more than 2 in a row)
import re
content = re.sub(r'\n\n\n+', r'\n\n', content)

# Write output
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ File formatted successfully!")
print(f"Output: {OUTPUT_FILE}")
print(f"\nFormatting applied:")
print("✓ Double line breaks before each chapter header (--- CHAPTER)")
print("✓ Double line breaks before each chapter title (CHAPTER [NUMBER]:)")
print("✓ Double line breaks before each subsection header (THE ...)")
print("✓ Double line breaks before INTERPRETATION NOTES sections")
print("✓ Excessive blank lines removed (max 2 consecutive)")
print(f"\n📚 Ready for ElevenLabs upload!")
print(f"Each chapter and subsection will now be a distinct narration pause point.")
