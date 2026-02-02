#!/usr/bin/env python3
"""
Clean markdown and convert to DOCX for Blues Lyrics.
Fixes malformed markdown syntax before conversion.
"""

import re
from pathlib import Path

def clean_markdown(content: str) -> str:
    """Clean malformed markdown syntax."""
    lines = content.split('\n')
    cleaned = []
    
    for line in lines:
        # Fix malformed headings like "### ## *When..." → "## When..."
        if re.match(r'^#+\s*#+', line):
            # Remove duplicate # and clean up
            line = re.sub(r'^#+\s*#+\s*', '## ', line)
            # Remove stray asterisks at start/end
            line = re.sub(r'^(##\s*)\*(.+)\*$', r'\1*\2*', line)
        
        # Remove pipe characters at start of lines (table-like formatting)
        if line.startswith('|'):
            line = line[1:].strip()
        
        # Clean up "* * *" horizontal rules to proper format
        if line.strip() == '* * *':
            line = '---'
        
        cleaned.append(line)
    
    return '\n'.join(cleaned)

def main():
    base = Path('/Users/williamaltig/claudeprojects/madhyama-kasha-shastra/01_TRANSLATIONS')
    md_path = base / 'Mūlamadhyamakakārikā_Blues_Lyrics_Only.md'
    clean_md_path = base / 'Mūlamadhyamakakārikā_Blues_Lyrics_Only_CLEAN.md'
    docx_path = base / 'Mūlamadhyamakakārikā_Blues_Lyrics_Only.docx'
    
    # Read original
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Clean it
    cleaned = clean_markdown(content)
    
    # Write cleaned version
    with open(clean_md_path, 'w', encoding='utf-8') as f:
        f.write(cleaned)
    
    print(f"Created cleaned markdown: {clean_md_path}")
    
    # Convert with pandoc
    import subprocess
    result = subprocess.run([
        'pandoc',
        str(clean_md_path),
        '-o', str(docx_path),
        '--from=markdown',
        '--to=docx'
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"Created DOCX: {docx_path}")
    else:
        print(f"Error: {result.stderr}")

if __name__ == '__main__':
    main()
