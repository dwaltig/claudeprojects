#!/usr/bin/env python3
"""
Remove duplicate chapter headers from Dhammapada ElevenReader version for clean TTS narration.
Keeps lunar calendar headers, removes embedded original chapter headers.
"""

import re

INPUT_FILE = "/Users/williamaltig/claudeprojects/Dhammapada/DHAMMAPADA_LUNAR_BLUES_28_ELEVENREADER.md"
OUTPUT_FILE = "/Users/williamaltig/claudeprojects/Dhammapada/DHAMMAPADA_LUNAR_BLUES_28_ELEVENREADER.md"

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    lines = f.readlines()

output_lines = []
i = 0

while i < len(lines):
    line = lines[i]
    
    # Check if this is a "# Chapter X: ... - Blues Edition" header
    if re.match(r'^# Chapter \d+:.*Blues Edition', line.strip()):
        # Skip this line
        i += 1
        
        # Skip the next line if it's a subtitle (## ...)
        if i < len(lines) and lines[i].strip().startswith('## '):
            i += 1
        
        # Skip blank lines
        while i < len(lines) and lines[i].strip() == '':
            i += 1
            
        # Skip "### Blues Interpretation by William Altig"
        if i < len(lines) and 'Blues Interpretation by William Altig' in lines[i]:
            i += 1
            
        # Skip following separator lines and blank lines
        while i < len(lines) and (lines[i].strip() == '---' or lines[i].strip() == ''):
            i += 1
            
        # Skip redundant section headers like "## The Twin Verses: Blues Style"
        if i < len(lines) and lines[i].strip().startswith('##'):
            i += 1
            # Skip blank line after
            if i < len(lines) and lines[i].strip() == '':
                i += 1
                
        continue
    
    output_lines.append(line)
    i += 1

# Write cleaned output
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.writelines(output_lines)

print(f"✓ Removed duplicate chapter headers from {len(lines)} lines")
print(f"✓ Output has {len(output_lines)} lines")
print(f"✓ Removed {len(lines) - len(output_lines)} lines")
