#!/usr/bin/env python3
"""
Extract verse content from the Blues translation.
Simpler approach: Keep lines that start with * (italic) or ( (parenthetical)
and filter out specific commentary patterns.
"""

import re
from pathlib import Path

def extract_verses(content: str) -> str:
    """Extract verse content with chapter/song structure."""
    lines = content.split('\n')
    output = []
    in_frontmatter = False
    
    # Commentary patterns to skip
    skip_patterns = [
        r'^The Teaching:',
        r'^What It Means:',
        r'^\*\*The Teaching:\*\*',
        r'^\*\*What It Means:\*\*',
        r'^\*\*Translator\*\*',
        r'^\*\*Interpreter\*\*',
        r'^\*\*Status\*\*',
        r'^Translator:',
        r'^Interpreter:',
        r'^Status:',
        r'^\*End of Chapter',
        r'^\*Ready for QA',
        r'^For those who want the deep doctrine',
        r'^The Blues Insight:',
        r'^The Two Truths',
        r'^No Soloist',
        r'^Karma Without',
        r'^\d+\.\s+\*\*',  # Numbered lists
        r'^Nāgārjuna',
        r'^The opponent',
        r'^Buddhist teaching says',
        r'^First, let\'s',
        r'^Fine\. Let\'s',
        r'^Same problem:',
        r'^Same with',
        r'^Think about it:',
        r'^Fair enough',
        r'^Try to find',
        r'^They\'re stuck',
        r'^They\'re all leaning',
        r'^They\'re leaning',
        r'^You can run this',
        r'^Either way,',
        r'^No effect,',
        r'^Causation slips',
        r'^If the foundation',
        r'^If seeing falls',
        r'^If duration',
        r'^Now here\'s where',
        r'^Now here\'s the Blues',
        r'^Now we get',
        r'^Now flip',
        r'^After all this',
        r'^We\'re almost',
        r'^One last try:',
        r'^Feeling arises',
        r'^Perception arises',
        r'^Formations arise',
        r'^Consciousness arises',
        r'^Walking ain\'t got',
        r'^There ain\'t nowhere',
        r'^As the Buddha said:',
        r'^The Buddha said:',
        r'^"Seeing, hearing',
        r'^"Therefore,',
        r'^"A separate entity',
        r'^"And if a separate',
        r'^"Someone has',
        r'^"The entity implies',
        r'^"In this very way',
        r'^All goings are prevented',
        r'^\*\s*\*Tasmād\*',
        r'^\* \* \*$',  # Horizontal rules
    ]
    
    for line in lines:
        stripped = line.strip()
        
        # Handle YAML frontmatter
        if stripped == '---' and (len(output) == 0 or in_frontmatter):
            if not in_frontmatter:
                in_frontmatter = True
            else:
                in_frontmatter = False
            output.append(line)
            if not in_frontmatter:
                output.append('')
            continue
        
        if in_frontmatter:
            output.append(line)
            continue
        
        # Keep chapter headings
        if stripped.startswith('# Chapter') or stripped.startswith('# Madhyamakashāstra'):
            output.append('')
            output.append(stripped)
            output.append('')
            continue
        
        # Keep subheadings (## *When You Search...*)
        if stripped.startswith('## ') or re.match(r'^#+\s*#+', stripped):
            cleaned = re.sub(r'^#+\s*#+\s*', '## ', stripped)
            output.append(cleaned)
            output.append('')
            continue
        
        # Keep song titles
        if stripped.startswith('### "') or stripped.startswith("### '"):
            output.append('')
            output.append(stripped)
            output.append('')
            continue
        
        # Keep verse markers
        if re.match(r'^\*\*\(Verse', stripped):
            output.append('')
            output.append(stripped)
            continue
        
        # Skip specific commentary patterns
        skip = False
        for pattern in skip_patterns:
            if re.match(pattern, stripped, re.IGNORECASE):
                skip = True
                break
        if skip:
            continue
        
        # Keep verse lines starting with | and *
        if stripped.startswith('|'):
            verse_text = stripped[1:].strip()
            # Remove footnotes
            verse_text = re.sub(r'[¹²³⁴⁵⁶⁷⁸⁹⁰]+', '', verse_text)
            if verse_text:
                output.append(verse_text)
            continue
        
        # Keep italic verse blocks
        if stripped.startswith('*') and not stripped.startswith('**'):
            # Remove footnotes
            cleaned = re.sub(r'[¹²³⁴⁵⁶⁷⁸⁹⁰]+', '', stripped)
            output.append(cleaned)
            continue
        
        # Keep parenthetical response lines
        if stripped.startswith('(') and ')' in stripped:
            output.append(stripped)
            continue
        
        # Keep blank lines (but not too many)
        if not stripped:
            if output and output[-1].strip():
                output.append('')
            continue
    
    # Clean up
    result = '\n'.join(output)
    result = re.sub(r'\n{4,}', '\n\n\n', result)
    
    return result

def main():
    base = Path('/Users/williamaltig/claudeprojects/madhyama-kasha-shastra/01_TRANSLATIONS')
    md_path = base / 'Mūlamadhyamakakārikā_Blues_Lyrics_Only.md'
    verses_path = base / 'Mūlamadhyamakakārikā_Blues_VERSES.md'
    
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    verses = extract_verses(content)
    
    with open(verses_path, 'w', encoding='utf-8') as f:
        f.write(verses)
    
    print(f"Created: {verses_path}")
    print(f"Original: {len(content)} bytes")
    print(f"Verses only: {len(verses)} bytes")
    
    # Also create DOCX
    import subprocess
    docx_path = base / 'Mūlamadhyamakakārikā_Blues_VERSES.docx'
    subprocess.run(['pandoc', str(verses_path), '-o', str(docx_path), '--from=markdown', '--to=docx'])
    print(f"Created DOCX: {docx_path}")

if __name__ == '__main__':
    main()
