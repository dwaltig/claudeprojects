#!/usr/bin/env python3
"""
Complete audit of apparatus section structure across all 28 chapters
"""

from pathlib import Path
import re

def extract_apparatus_headings(filepath):
    """Extract apparatus section headings from a chapter file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all section headings (# through ######)
        headings = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)

        # Extract headings that appear to be apparatus-related
        apparatus_headings = []
        found_main_content = False

        for level, text in headings:
            # Look for headings after the main translation content
            if 'philosophical' in text.lower() or 'apparatus' in text.lower() or \
               'implications' in text.lower() or 'key concepts' in text.lower() or \
               'cross-references' in text.lower() or 'significance' in text.lower():
                apparatus_headings.append((level, text))

        return apparatus_headings
    except Exception as e:
        return [("ERROR", str(e))]

def main():
    base_path = Path('Scholarly_Chapters')
    chapters = sorted(base_path.glob('CHAPTER_*.md'))

    print("\n" + "="*90)
    print("APPARATUS STRUCTURE AUDIT - ALL 28 CHAPTERS")
    print("="*90 + "\n")

    results = {}

    for i, chapter_file in enumerate(chapters, 1):
        headings = extract_apparatus_headings(chapter_file)
        results[chapter_file.name] = headings

        print(f"Chapter {i:2d}: {chapter_file.name}")
        if headings:
            for level, text in headings:
                indent = "  " * (len(level) - 1)
                print(f"  {level} {text}")
        else:
            print("  [NO APPARATUS HEADINGS FOUND]")
        print()

    # Analysis - group by structure
    print("\n" + "="*90)
    print("STRUCTURE PATTERNS FOUND")
    print("="*90 + "\n")

    structures = {}
    for filename, headings in results.items():
        # Create a pattern signature
        if headings:
            pattern = " | ".join([text for _, text in headings])
        else:
            pattern = "NO_APPARATUS"

        if pattern not in structures:
            structures[pattern] = []
        structures[pattern].append(filename)

    for i, (pattern, files) in enumerate(sorted(structures.items(), key=lambda x: -len(x[1])), 1):
        print(f"PATTERN {i}: ({len(files)} chapters)")
        print(f"  {pattern[:80]}...")
        print(f"  Chapters: {', '.join([f.replace('CHAPTER_', '').replace('.md', '') for f in files[:5]])}")
        if len(files) > 5:
            print(f"           ... and {len(files)-5} more")
        print()

    # Verdict
    print("="*90)
    print("VERDICT")
    print("="*90)
    if len(structures) == 1:
        print("✅ ALL CHAPTERS HAVE CONSISTENT APPARATUS STRUCTURE")
    else:
        print(f"❌ INCONSISTENCY FOUND: {len(structures)} DIFFERENT PATTERNS")
        print("\nDifferent apparatus structures being used:")
        for pattern in structures.keys():
            print(f"  - {pattern[:100]}")

if __name__ == '__main__':
    main()
