#!/usr/bin/env python3
"""
Convert Chapter 16 from markdown footnotes [^1] to superscript numerals ¹
"""

import re
from pathlib import Path

# Superscript mapping
SUPERSCRIPT = {
    '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
    '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'
}

def num_to_superscript(num):
    """Convert number to superscript"""
    return ''.join(SUPERSCRIPT[d] for d in str(num))

def convert_chapter_16():
    filepath = Path('Scholarly_Chapters/CHAPTER_16_BUDDHAS_ETERNAL_LIFESPAN.md')

    if not filepath.exists():
        print(f"Error: {filepath} not found")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace markdown footnote REFERENCES with superscript
    # Pattern: [^1], [^2], ... [^38]
    # But NOT the definitions [^1]: ... which come after ## FOOTNOTES

    # Split on ## FOOTNOTES to separate body from footnote definitions
    if '## FOOTNOTES' in content:
        body, footnotes_section = content.split('## FOOTNOTES', 1)
    else:
        body = content
        footnotes_section = ''

    # Convert markdown references in body to superscript
    for i in range(1, 39):
        markdown_ref = f'[^{i}]'
        superscript_ref = num_to_superscript(i)
        body = body.replace(markdown_ref, superscript_ref)

    # Reconstruct: keep footnotes section as-is for now
    if footnotes_section:
        content = body + '## FOOTNOTES' + footnotes_section
    else:
        content = body

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Converted Chapter 16 markdown footnotes to superscript numerals")
    print(f"   - Converted 38 footnote references [^n] → ⁿ")
    print(f"   - Preserved FOOTNOTES section with definitions")
    print(f"   - File saved: {filepath}")

if __name__ == '__main__':
    convert_chapter_16()
