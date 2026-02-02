#!/usr/bin/env python3
"""
Create ElevenReader-optimized version of Gracián's Art of Prudence (Blues Edition)
"""
import re

def create_elevenreader_version():
    # Read source file
    with open('Oraculo_Manual_COMPLETE_EDITION_BLUES.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Build output with clean chapter structure
    output_lines = []
    
    # Add title and introduction
    output_lines.append("# The Art of Prudence: Practical Blues Edition")
    output_lines.append("")
    output_lines.append("*300 Aphorisms of Wisdom by Baltasar Gracián*")
    output_lines.append("*Translated into the Blues Vernacular*")
    output_lines.append("")
    output_lines.append("---")
    output_lines.append("")
    output_lines.append("## Introduction")
    output_lines.append("")
    output_lines.append("Baltasar Gracián was a 17th-century Spanish Jesuit priest who wrote the sharpest survival manual ever created. His \"Oráculo Manual y Arte de Prudencia\" contains 300 aphorisms—each one a condensed lesson in how to navigate a world full of sharks, fools, and power players.")
    output_lines.append("")
    output_lines.append("This is the Blues version. No academic fluff. Just the real talk.")
    output_lines.append("")
    output_lines.append("---")
    output_lines.append("")
    
    # Process each group header and convert to chapter
    # Pattern: "# Oráculo Manual: Aphorisms X-Y (Practical Blues)"
    chapter_pattern = r'^# Oráculo Manual: Aphorisms (\d+)-(\d+) \(Practical Blues\)$'
    
    lines = content.split('\n')
    chapter_num = 0
    
    for line in lines:
        chapter_match = re.match(chapter_pattern, line)
        if chapter_match:
            chapter_num += 1
            start = chapter_match.group(1)
            end = chapter_match.group(2)
            output_lines.append(f"# Chapter {chapter_num}: Aphorisms {start} through {end}")
            output_lines.append("")
        elif line.startswith('## '):
            # Keep individual aphorism headers as-is
            output_lines.append(line)
            output_lines.append("")
        elif line.strip():
            # Regular content
            output_lines.append(line)
            output_lines.append("")
    
    # Write output
    output_content = '\n'.join(output_lines)
    
    with open('Oraculo_Manual_ELEVENREADER.md', 'w', encoding='utf-8') as f:
        f.write(output_content)
    
    print(f"Created ElevenReader version with {chapter_num} chapters")
    print(f"Output: Oraculo_Manual_ELEVENREADER.md")

if __name__ == '__main__':
    create_elevenreader_version()
