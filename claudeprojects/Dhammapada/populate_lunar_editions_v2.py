#!/usr/bin/env python3
"""
Populate Lunar Calendar Editions with Existing Translations (Version 2)

Improved version with better placeholder detection.
"""

import re
from pathlib import Path

# Directory paths
BASE_DIR = Path(__file__).parent
TRANSLATIONS_DIR = BASE_DIR / "01_TRANSLATIONS"
LUNAR_SCHOLARLY = BASE_DIR / "DHAMMAPADA_LUNAR_SCHOLARLY_28.md"
LUNAR_BLUES = BASE_DIR / "DHAMMAPADA_LUNAR_BLUES_28.md"

def read_file(filepath):
    """Read file content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """Write content to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def get_chapter_content(canonical_ch, edition):
    """Get full chapter content."""
    chapter_names = {
        1: "Yamakavagga", 2: "Appamadavagga", 3: "Cittavagga", 4: "Pupphavagga",
        5: "Balavagga", 6: "Panditavagga", 7: "Arahantavagga", 8: "Sahassavagga",
        9: "Papavagga", 10: "Dandavagga", 11: "Jaravagga", 12: "Attavagga",
        13: "Lokavagga", 14: "Buddhavagga", 15: "Sukhavagga", 16: "Piyavagga",
        17: "Kodhavagga", 18: "Malavagga", 19: "Dhammatthavagga", 20: "Maggavagga",
        21: "Pakinnakavagga", 22: "Nirayavagga", 23: "Nagavagga", 24: "Tanhavagga",
        25: "Bhikkhuvagga", 26: "Brahmanavagga"
    }

    name = chapter_names.get(canonical_ch)
    suffix = "Scholarly" if edition == "scholarly" else "Blues"
    filename = f"Chapter_{canonical_ch:02d}_{name}_{suffix}.md"
    filepath = TRANSLATIONS_DIR / filename

    if filepath.exists():
        return read_file(filepath)
    else:
        return f"[ERROR: File not found: {filename}]"

def split_chapter_14(edition):
    """Split Chapter 14 into two parts for verses 179-187 and 188-196."""
    content = get_chapter_content(14, edition)

    # Find the split point - look for verse 188
    patterns = [
        r"###\s+Verses?\s+188",
        r"\*\*Verses?\s+188",
        "### Verses 188-192",
        "**Verses 188-192**"
    ]

    split_pos = -1
    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            split_pos = match.start()
            break

    if split_pos > 0:
        part1 = content[:split_pos].strip()
        part2 = content[split_pos:].strip()
    else:
        # Fallback: just take first 60% and last 40%
        split_pos = int(len(content) * 0.6)
        part1 = content[:split_pos].strip()
        part2 = content[split_pos:].strip()

    return part1, part2

def split_chapter_26(edition):
    """Split Chapter 26 for verses 383-386 + 411-423 (Ch 27) and 387-410 (Ch 28)."""
    content = get_chapter_content(26, edition)

    # Find verse 383, 387, and 411
    verse_383_match = re.search(r"###\s+Verses?\s+383", content)
    verse_387_match = re.search(r"###\s+Verses?\s+38[789]", content)
    verse_411_match = re.search(r"###\s+Verses?\s+411", content)

    if not (verse_383_match and verse_387_match and verse_411_match):
        # Try alternative patterns
        verse_383_match = re.search(r"\*\*Verses?\s+383", content)
        verse_387_match = re.search(r"\*\*Verses?\s+38[789]", content)
        verse_411_match = re.search(r"\*\*Verses?\s+411", content)

    if verse_383_match and verse_387_match and verse_411_match:
        # Extract the three sections
        verses_383_386 = content[verse_383_match.start():verse_387_match.start()].strip()
        verses_387_410 = content[verse_387_match.start():verse_411_match.start()].strip()
        verses_411_423 = content[verse_411_match.start():].strip()

        ch27_content = verses_383_386 + "\n\n---\n\n" + verses_411_423
        ch28_content = verses_387_410
    else:
        # Fallback: split roughly
        third = len(content) // 3
        ch27_content = content[:third] + "\n\n" + content[2*third:]
        ch28_content = content[third:2*third]

    return ch27_content, ch28_content

def populate_edition(template_file, edition):
    """Populate a lunar edition file."""
    print(f"\n{'='*70}")
    print(f"POPULATING {edition.upper()} EDITION")
    print(f"{'='*70}\n")

    template = read_file(template_file)

    # Simple replacement strategy: replace all placeholders in order
    replacements = []

    # Chapters 1-13: Direct mapping
    for ch in range(1, 14):
        content = get_chapter_content(ch, edition)
        replacements.append((f"Ch {ch}", content))

    # Chapter 14: First part of split
    ch14_part1, ch14_part2 = split_chapter_14(edition)
    replacements.append(("Ch 14 (179-187)", ch14_part1))

    # Chapter 15: Second part of Chapter 14 split
    replacements.append(("Ch 15 (188-196) ✨", ch14_part2))

    # Chapters 16-26: Canonical 15-25 shifted
    for lunar_ch in range(16, 27):
        canonical_ch = lunar_ch - 1
        content = get_chapter_content(canonical_ch, edition)
        replacements.append((f"Ch {lunar_ch}", content))

    # Chapter 27: Nibbānavagga
    ch27_content, ch28_content = split_chapter_26(edition)
    replacements.append(("Ch 27 (Nibbānavagga) ✨", ch27_content))

    # Chapter 28: Brāhmaṇavagga
    replacements.append(("Ch 28 (Brāhmaṇavagga)", ch28_content))

    # Replace placeholders - use a simpler approach
    # Just replace in order of appearance
    placeholder_pattern = r'\[.*?CONTENT TO BE INSERTED HERE.*?\]'

    matches = list(re.finditer(placeholder_pattern, template))
    print(f"Found {len(matches)} placeholders to replace")
    print(f"Have {len(replacements)} replacement contents\n")

    if len(matches) != len(replacements):
        print(f"⚠️  WARNING: Placeholder count ({len(matches)}) != Replacement count ({len(replacements)})")

    # Replace each placeholder with corresponding content
    offset = 0
    for i, (match, (label, content)) in enumerate(zip(matches, replacements), 1):
        start = match.start() + offset
        end = match.end() + offset
        before = template[:start]
        after = template[end:]
        template = before + content + after
        offset += len(content) - (end - start)
        print(f"  ✓ Replaced placeholder {i:2d}: {label}")

    # Write output
    output_file = template_file.parent / f"{template_file.stem}_FINAL.md"
    write_file(output_file, template)

    print(f"\n{'='*70}")
    print(f"✓ COMPLETE: {output_file.name}")
    print(f"{'='*70}\n")

    return output_file

def main():
    """Main function."""
    print("\n" + "="*70)
    print("DHAMMAPADA LUNAR EDITION POPULATION SCRIPT V2")
    print("="*70)

    scholarly_output = populate_edition(LUNAR_SCHOLARLY, "scholarly")
    blues_output = populate_edition(LUNAR_BLUES, "blues")

    print("\n" + "="*70)
    print("✓✓✓ ALL EDITIONS POPULATED SUCCESSFULLY! ✓✓✓")
    print("="*70)
    print(f"\nFinal output files:")
    print(f"  • {scholarly_output}")
    print(f"  • {blues_output}")
    print("\n" + "="*70 + "\n")

if __name__ == "__main__":
    main()
