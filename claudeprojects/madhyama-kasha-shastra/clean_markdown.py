#!/usr/bin/env python3
"""
Clean the Blues Lyrics markdown to proper markdown syntax.
Fixes: pipe-prefixed lines, malformed headings, verse blocks.
"""

import re
from pathlib import Path

def clean_blues_markdown(content: str) -> str:
    """Convert non-standard markdown to clean markdown."""
    lines = content.split('\n')
    cleaned = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Fix malformed headings like "### ## *When..."
        if re.match(r'^#+\s*#+', line):
            # Extract the actual heading text
            text = re.sub(r'^#+\s*#+\s*', '', line)
            # Remove surrounding asterisks if present
            text = text.strip()
            if text.startswith('*') and text.endswith('*'):
                text = text[1:-1]
            cleaned.append(f'## *{text}*')
            cleaned.append('')
            i += 1
            continue
        
        # Convert "* * *" to proper horizontal rule
        if line.strip() == '* * *':
            cleaned.append('---')
            cleaned.append('')
            i += 1
            continue
        
        # Handle pipe-prefixed lines (verse blocks)
        if line.startswith('|'):
            verse_text = line[1:].strip()
            
            # Skip empty pipe lines
            if not verse_text:
                i += 1
                continue
            
            # Check if this is a numbered list item
            if re.match(r'^\d+\.', verse_text):
                cleaned.append(verse_text)
            else:
                # Regular verse line - add two spaces at end for hard line break
                cleaned.append(verse_text + '  ')
            
            i += 1
            continue
        
        # Regular lines pass through
        cleaned.append(line)
        i += 1
    
    # Post-process: Join consecutive verse lines properly
    result = '\n'.join(cleaned)
    
    # Clean up excessive blank lines
    result = re.sub(r'\n{4,}', '\n\n\n', result)
    
    return result

def main():
    base = Path('/Users/williamaltig/claudeprojects/madhyama-kasha-shastra/01_TRANSLATIONS')
    md_path = base / 'Mūlamadhyamakakārikā_Blues_Lyrics_Only.md'
    clean_path = base / 'Mūlamadhyamakakārikā_Blues_Lyrics_Only_CLEAN.md'
    
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cleaned = clean_blues_markdown(content)
    
    with open(clean_path, 'w', encoding='utf-8') as f:
        f.write(cleaned)
    
    print(f"Created: {clean_path}")
    print(f"Original: {len(content)} bytes")
    print(f"Cleaned: {len(cleaned)} bytes")

if __name__ == '__main__':
    main()
