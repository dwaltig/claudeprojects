#!/usr/bin/env python3
"""
Extract ONLY the lyrics from the Blues translation.
Aggressively removes ALL notation, commentary, markers, and metadata.
"""

import re
from pathlib import Path

def is_lyric_line(line: str) -> bool:
    """Determine if a line is pure lyric content."""
    stripped = line.strip()
    
    # Skip empty lines
    if not stripped:
        return False
    
    # Skip all bold markers like **The Teaching:**
    if stripped.startswith('**') and stripped.endswith('**'):
        return False
    if stripped.startswith('**') and ':**' in stripped:
        return False
    
    # Skip metadata lines
    skip_patterns = [
        r'^\*\*Translator\*\*',
        r'^\*\*Interpreter\*\*',
        r'^\*\*Status\*\*',
        r'^Translator:',
        r'^Interpreter:',
        r'^Status:',
        r'^\*End of Chapter',
        r'^\*Ready for QA',
        r'^For those who want the deep doctrine',
        r'^---$',
        r'^\* \* \*$',
        r'^\*\*The Teaching:\*\*',
        r'^\*\*What It Means:\*\*',
        r'^\*\*The Blues Insight',
        r'^\*\*The Two Truths',
        r'^\*\*No Soloist',
        r'^\*\*Karma Without',
        r'\*Tasmād\*',
        r'Conclusion \(\*nigamana\*\)',
    ]
    
    for pattern in skip_patterns:
        if re.search(pattern, stripped, re.IGNORECASE):
            return False
    
    return True

def clean_lyric_line(line: str) -> str:
    """Clean a lyric line of footnotes and extra formatting."""
    cleaned = line.strip()
    
    # Remove footnote superscripts
    cleaned = re.sub(r'[¹²³⁴⁵⁶⁷⁸⁹⁰]+', '', cleaned)
    
    # Remove pipe prefix
    if cleaned.startswith('|'):
        cleaned = cleaned[1:].strip()
    
    # Remove bold markers around entire line
    if cleaned.startswith('**') and cleaned.endswith('**'):
        cleaned = cleaned[2:-2]
    
    return cleaned

def extract_pure_lyrics(content: str) -> str:
    """Extract only the pure lyric content."""
    lines = content.split('\n')
    output = []
    in_frontmatter = False
    
    for line in lines:
        stripped = line.strip()
        
        # Handle YAML frontmatter
        if stripped == '---':
            if not in_frontmatter and len(output) == 0:
                in_frontmatter = True
                output.append(line)
                continue
            elif in_frontmatter:
                in_frontmatter = False
                output.append(line)
                output.append('')
                continue
        
        if in_frontmatter:
            output.append(line)
            continue
        
        # Keep chapter headings
        if stripped.startswith('# Chapter') or stripped.startswith('# Madhyamakashāstra'):
            output.append('')
            output.append('')
            output.append(line)
            output.append('')
            continue
        
        # Keep section subheadings (but clean them)
        if stripped.startswith('## ') or stripped.startswith('### ##'):
            cleaned = re.sub(r'^#+\s*#+\s*', '## ', stripped)
            output.append(cleaned)
            output.append('')
            continue
        
        # Keep song section markers like ### "Nobody Before the Blues"
        if stripped.startswith('### "') or stripped.startswith("### '"):
            output.append('')
            output.append(stripped)
            output.append('')
            continue
        
        # Keep verse markers like **(Verse 1)**
        if re.match(r'^\*\*\(Verse \d+', stripped):
            output.append('')
            output.append(stripped)
            continue
        
        # Check if this is a lyric line
        if is_lyric_line(stripped):
            cleaned = clean_lyric_line(stripped)
            if cleaned:
                output.append(cleaned)
    
    # Clean up excessive blank lines
    result = '\n'.join(output)
    result = re.sub(r'\n{4,}', '\n\n\n', result)
    
    return result

def main():
    base = Path('/Users/williamaltig/claudeprojects/madhyama-kasha-shastra/01_TRANSLATIONS')
    md_path = base / 'Mūlamadhyamakakārikā_Blues_Lyrics_Only.md'
    lyrics_path = base / 'Mūlamadhyamakakārikā_Blues_PURE_LYRICS.md'
    
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lyrics = extract_pure_lyrics(content)
    
    with open(lyrics_path, 'w', encoding='utf-8') as f:
        f.write(lyrics)
    
    print(f"Created: {lyrics_path}")
    print(f"Original: {len(content)} bytes")
    print(f"Pure lyrics: {len(lyrics)} bytes")

if __name__ == '__main__':
    main()
