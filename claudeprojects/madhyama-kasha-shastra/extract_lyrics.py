#!/usr/bin/env python3
"""
Extract just the lyrics from the Blues translation.
Removes: footnotes, commentary, "The Teaching"/"What It Means" markers, numbered lists.
"""

import re
from pathlib import Path

def extract_lyrics(content: str) -> str:
    """Extract only the lyrics, removing all notation."""
    lines = content.split('\n')
    output = []
    skip_next_blank = False
    
    for line in lines:
        stripped = line.strip()
        
        # Keep YAML frontmatter
        if stripped == '---' and len(output) < 10:
            output.append(line)
            continue
        if stripped.startswith('title:') or stripped.startswith('subtitle:') or stripped.startswith('author:'):
            output.append(line)
            continue
        
        # Keep chapter headings
        if stripped.startswith('# Chapter') or stripped.startswith('# Madhyamakashāstra'):
            output.append('')
            output.append(line)
            output.append('')
            continue
        
        # Keep subheadings (## *When You Search...*)
        if stripped.startswith('## ') or stripped.startswith('### ##'):
            # Clean it up
            cleaned = re.sub(r'^#+\s*#+\s*', '## ', stripped)
            output.append(cleaned)
            output.append('')
            continue
        
        # Skip "The Teaching:" and "What It Means:" markers
        if stripped.startswith('**The Teaching:**') or stripped.startswith('**What It Means:**'):
            continue
        
        # Skip "For those who want the deep doctrine:"
        if 'deep doctrine' in stripped.lower():
            continue
        
        # Skip "End of Chapter" notes
        if stripped.startswith('*End of Chapter') or stripped.startswith('*Ready for QA'):
            continue
        
        # Skip numbered lists (1. **The Cause**...)
        if re.match(r'^\|?\s*\d+\.', stripped):
            continue
        
        # Skip "The Blues Insight:" type markers
        if stripped.startswith('**The Blues Insight:**') or stripped.startswith('**The Two Truths'):
            continue
        if stripped.startswith('**No Soloist') or stripped.startswith('**Karma Without'):
            continue
        
        # Skip horizontal rules
        if stripped == '* * *' or stripped == '---':
            output.append('')
            continue
        
        # Process verse lines (starting with |)
        if stripped.startswith('|'):
            verse_text = stripped[1:].strip()
            if verse_text:
                # Remove footnote numbers
                verse_text = re.sub(r'[¹²³⁴⁵⁶⁷⁸⁹⁰]+', '', verse_text)
                # Remove trailing asterisks used for footnotes
                verse_text = re.sub(r'\*\d+$', '', verse_text)
                output.append(verse_text)
            continue
        
        # Process regular text (commentary vs lyrics)
        if stripped:
            # Remove footnote numbers
            cleaned = re.sub(r'[¹²³⁴⁵⁶⁷⁸⁹⁰]+', '', stripped)
            
            # Skip short commentary lines
            if any(x in cleaned.lower() for x in ['nāgārjuna says', 'the opponent', 'fair enough', 'think about it', 'try to find', 'same problem', 'same with', "let's try", "let's look", 'fine.', 'this is the blues truth', 'now here', 'after all this', "we're almost", 'one last try', 'now flip', 'buddhist teaching says', 'first,', 'now we get', 'now the opponent', 'walking ain\'t got', 'no effect', 'causation slips', 'if the foundation', 'they\'re all leaning', 'they\'re stuck', 'you can run', 'either way', 'there ain\'t nowhere']):
                continue
            
            # Keep lines that look like lyrics (italic blocks, verse-like content)
            if cleaned.startswith('*') or cleaned.endswith('*'):
                output.append(cleaned)
            # Keep lines that are part of verse blocks (short poetic lines)
            elif len(cleaned) < 80 and not any(x in cleaned.lower() for x in ['translator', 'status', 'revised']):
                output.append(cleaned)
        else:
            # Preserve blank lines but not too many consecutive
            if output and output[-1] != '':
                output.append('')
    
    # Clean up excessive blank lines
    result = '\n'.join(output)
    result = re.sub(r'\n{4,}', '\n\n\n', result)
    
    return result

def main():
    base = Path('/Users/williamaltig/claudeprojects/madhyama-kasha-shastra/01_TRANSLATIONS')
    md_path = base / 'Mūlamadhyamakakārikā_Blues_Lyrics_Only.md'
    lyrics_path = base / 'Mūlamadhyamakakārikā_Blues_LYRICS.md'
    
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lyrics = extract_lyrics(content)
    
    with open(lyrics_path, 'w', encoding='utf-8') as f:
        f.write(lyrics)
    
    print(f"Created: {lyrics_path}")
    print(f"Original: {len(content)} bytes")
    print(f"Lyrics only: {len(lyrics)} bytes")

if __name__ == '__main__':
    main()
