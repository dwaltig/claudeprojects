#!/usr/bin/env python3
"""
Convert inline footnotes to chapter endnotes for Dhammapada Scholarly Book.
Restructures each chapter so footnotes appear at chapter end.
"""

import re

def convert_footnotes_to_endnotes(content):
    """
    Convert inline footnotes to chapter endnotes.
    
    Current structure:
    ### Verse X
    [verse text with [N] reference]
    #### Footnotes
    [N] footnote text
    
    New structure:
    ### Verse X
    [verse text with [N] reference]
    
    (At chapter end)
    ---
    ## Endnotes
    [N] footnote text
    """
    
    # Split content into lines for processing
    lines = content.split('\n')
    
    result_lines = []
    current_chapter = None
    chapter_endnotes = []
    in_footnote_section = False
    footnote_buffer = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Detect chapter start (# Chapter N: ...)
        chapter_match = re.match(r'^# Chapter \d+:', line)
        if chapter_match:
            # If we have accumulated endnotes from previous chapter, append them
            if current_chapter and chapter_endnotes:
                result_lines.append('')
                result_lines.append('---')
                result_lines.append('')
                result_lines.append('## Endnotes')
                result_lines.append('')
                result_lines.extend(chapter_endnotes)
            
            # Reset for new chapter
            current_chapter = line
            chapter_endnotes = []
            in_footnote_section = False
            result_lines.append(line)
            i += 1
            continue
        
        # Detect "End of [Chapter]" which signals chapter end
        if re.match(r'^\*\*End of .+vagga', line, re.IGNORECASE):
            # Append accumulated endnotes before the "End of" line
            if chapter_endnotes:
                result_lines.append('')
                result_lines.append('---')
                result_lines.append('')
                result_lines.append('## Endnotes')
                result_lines.append('')
                result_lines.extend(chapter_endnotes)
                chapter_endnotes = []  # Reset after adding
            result_lines.append('')
            result_lines.append(line)
            i += 1
            continue
        
        # Detect footnote section header
        if line.strip() == '#### Footnotes':
            in_footnote_section = True
            i += 1
            continue
        
        # If in footnote section, collect footnotes
        if in_footnote_section:
            # Check if we've hit the end of footnotes (next section starting with --- or ### or ##)
            if line.strip() == '---' or line.startswith('### ') or line.startswith('## '):
                in_footnote_section = False
                # Add collected footnotes to chapter endnotes
                if footnote_buffer:
                    chapter_endnotes.extend(footnote_buffer)
                    footnote_buffer = []
                # Don't skip this line - process it normally
                result_lines.append(line)
                i += 1
                continue
            
            # Collect footnote content
            if line.strip():
                footnote_buffer.append(line)
            elif footnote_buffer:
                # Empty line - might be between footnotes
                footnote_buffer.append('')
            i += 1
            continue
        
        # Regular line - just append
        result_lines.append(line)
        i += 1
    
    # Handle any remaining endnotes at the very end
    if chapter_endnotes:
        result_lines.append('')
        result_lines.append('---')
        result_lines.append('')
        result_lines.append('## Endnotes')
        result_lines.append('')
        result_lines.extend(chapter_endnotes)
    
    return '\n'.join(result_lines)


def process_file(input_path, output_path):
    """Read input file, convert footnotes, write output."""
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    converted = convert_footnotes_to_endnotes(content)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(converted)
    
    print(f"Converted: {input_path} -> {output_path}")


if __name__ == '__main__':
    input_file = '/Users/williamaltig/claudeprojects/Dhammapada/DHAMMAPADA_SCHOLARLY_BOOK.md'
    output_file = '/Users/williamaltig/claudeprojects/Dhammapada/DHAMMAPADA_SCHOLARLY_BOOK_ENDNOTES.md'
    process_file(input_file, output_file)
    print("Done! Footnotes converted to chapter endnotes.")
