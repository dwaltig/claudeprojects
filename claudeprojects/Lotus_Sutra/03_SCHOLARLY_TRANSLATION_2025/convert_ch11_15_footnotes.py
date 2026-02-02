#!/usr/bin/env python3
"""
Convert markdown footnotes [^n] to superscript numerals in Chapters 11-15
Chapter 16 was already converted separately.
"""

from pathlib import Path

# Superscript mapping
SUPERSCRIPT = {
    '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
    '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'
}

def num_to_superscript(num):
    """Convert number to superscript"""
    return ''.join(SUPERSCRIPT[d] for d in str(num))

def convert_chapter(filepath):
    """Convert a chapter from markdown footnotes to superscript"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split on FOOTNOTES section to separate body from definitions
    if '## FOOTNOTES' in content:
        body, footnotes_section = content.split('## FOOTNOTES', 1)
    else:
        body = content
        footnotes_section = ''

    # Convert all markdown references to superscript (up to 99)
    for i in range(1, 100):
        markdown_ref = f'[^{i}]'
        superscript_ref = num_to_superscript(i)
        body = body.replace(markdown_ref, superscript_ref)

    # Reconstruct
    if footnotes_section:
        new_content = body + '## FOOTNOTES' + footnotes_section
    else:
        new_content = body

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    base_path = Path('Scholarly_Chapters')

    chapters = [
        ('CHAPTER_11_EMERGENCE_PRABHUTARATNA_STUPA.md', 11),
        ('CHAPTER_12_DEVADATTA_NAGA_PRINCESS.md', 12),
        ('CHAPTER_13_EXHORTATION_TO_UPHOLD.md', 13),
        ('CHAPTER_14_PEACEFUL_PRACTICE.md', 14),
        ('CHAPTER_15_EMERGENCE_BODHISATTVAS.md', 15),
    ]

    print("\n" + "="*90)
    print("CONVERTING MARKDOWN FOOTNOTES TO SUPERSCRIPT - CHAPTERS 11-15")
    print("="*90 + "\n")

    for filename, num in chapters:
        filepath = base_path / filename
        try:
            convert_chapter(filepath)
            print(f"  ✅ Chapter {num:2d}: Converted markdown footnotes [^n] → ⁿ")
        except Exception as e:
            print(f"  ❌ Chapter {num:2d}: Error - {e}")

    print("\n" + "="*90)
    print("✅ CONVERSION COMPLETE")
    print("="*90)
    print("\nChapters 11-16 now use consistent superscript footnote style")
    print("Chapter 16 was already converted separately\n")

if __name__ == '__main__':
    main()
