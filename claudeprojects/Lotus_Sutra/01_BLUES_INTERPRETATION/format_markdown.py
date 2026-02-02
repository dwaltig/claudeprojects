#!/usr/bin/env python3
"""
Convert Blues Lotus Sutra to proper Markdown formatting.
Adds headers, italics, bolding systematically.
"""

import re

def convert_to_markdown(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    new_lines = []
    
    for i, line in enumerate(lines):
        original = line
        
        # Skip already-formatted markdown lines
        if line.startswith('#') or line.startswith('>') or line.startswith('|'):
            new_lines.append(line)
            continue
        
        # Convert decorative separators to horizontal rules
        if re.match(r'^[═]{5,}$', line) or re.match(r'^[=]{50,}$', line):
            new_lines.append('---')
            continue
        
        # Convert "CHAPTER ONE:" patterns to # headers
        if re.match(r'^CHAPTER (ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|ELEVEN|TWELVE|THIRTEEN|FOURTEEN|FIFTEEN|SIXTEEN|SEVENTEEN|EIGHTEEN|NINETEEN|TWENTY|TWENTY-ONE|TWENTY-TWO|TWENTY-THREE|TWENTY-FOUR|TWENTY-FIVE|TWENTY-SIX|TWENTY-SEVEN|TWENTY-EIGHT):', line):
            new_lines.append(f'# {line}')
            continue
        
        # Convert "END OF CHAPTER" to ### headers
        if line.startswith('END OF CHAPTER'):
            new_lines.append(f'### {line}')
            continue
        
        # Convert all-caps section headers to ## headers
        # These are typically 3-10 word headers in all caps
        if (line.isupper() and 
            len(line) > 5 and 
            len(line) < 100 and 
            not line.startswith('---') and
            not re.match(r'^[A-Z]{1,3}\.$', line) and
            'Blues Interpretation' not in line and
            line.strip()):
            new_lines.append(f'## {line}')
            continue
        
        # Convert specific section patterns to ### headers
        section_patterns = [
            r'^Interpretation Notes?:?$',
            r'^INTERPRETATION NOTES?:?$',
            r'^Reader\'s Introduction',
            r'^Scholarly Introduction',
            r'^Interpreter\'s Note',
            r'^THE \d+ CHAPTERS',
            r"^CHAPTER SUMMARIES",
            r'^TABLE OF CONTENTS',
            r'^INTRODUCTORY MATERIAL',
            r'^SCHOLARLY APPARATUS',
        ]
        for pattern in section_patterns:
            if re.match(pattern, line, re.IGNORECASE):
                new_lines.append(f'### {line}')
                continue
        
        # Convert "Blues Interpretation from Classical Chinese by Kumārajīva" to italic
        if 'Blues Interpretation from Classical Chinese' in line:
            new_lines.append(f'*{line}*')
            continue
        
        # Convert quoted speech patterns - make them blockquotes when long
        # Skip this for now - too complex
        
        # Keep other lines as-is
        new_lines.append(line)
    
    # Join and do some global replacements
    content = '\n'.join(new_lines)
    
    # Ensure proper spacing around headers
    content = re.sub(r'\n(#{1,3} [^\n]+)\n([^\n])', r'\n\1\n\n\2', content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Converted {input_file} to {output_file}")
    print(f"Total lines: {len(new_lines)}")

if __name__ == '__main__':
    input_file = '/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/Blues_Lotus_Sutra_MASTER_CLEAN.md'
    output_file = '/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/Blues_Lotus_Sutra_FORMATTED.md'
    convert_to_markdown(input_file, output_file)
