#!/usr/bin/env python3
"""
Populate Lunar Calendar Editions with Existing Translations

This script populates the 28-chapter lunar calendar editions (scholarly and blues)
with content from the existing chapter translation files.

Handles:
1. Standard chapters (1-13): Direct insertion
2. Chapter 14 split: Verses 179-187 → Ch 14; Verses 188-196 → Ch 15
3. Canonical chapters 15-25 → Lunar chapters 16-26 (renumbered)
4. Chapter 26 split: Verses 383-386 + 411-423 → Ch 27; Verses 387-410 → Ch 28

Usage:
    python3 populate_lunar_editions.py
"""

import re
from pathlib import Path

# Directory paths
BASE_DIR = Path(__file__).parent
TRANSLATIONS_DIR = BASE_DIR / "01_TRANSLATIONS"
LUNAR_SCHOLARLY = BASE_DIR / "DHAMMAPADA_LUNAR_SCHOLARLY_28.md"
LUNAR_BLUES = BASE_DIR / "DHAMMAPADA_LUNAR_BLUES_28.md"

# Chapter mapping: canonical number → lunar number
CHAPTER_MAPPING = {
    1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10,
    11: 11, 12: 12, 13: 13,
    14: 14,  # Split: 179-187 stays in 14, 188-196 goes to 15
    15: 16, 16: 17, 17: 18, 18: 19, 19: 20, 20: 21,  # Shifted by +1
    21: 22, 22: 23, 23: 24, 24: 25, 25: 26,
    26: 27   # Split: 383-386 + 411-423 → 27; 387-410 → 28
}

def read_file(filepath):
    """Read file content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """Write content to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def extract_verses_by_range(content, verse_ranges):
    """
    Extract specific verses from chapter content.

    Args:
        content: Full chapter content
        verse_ranges: List of tuples like [(179, 187), (188, 196)]

    Returns:
        Extracted content containing only specified verses
    """
    extracted_parts = []

    for start, end in verse_ranges:
        # Pattern to match verse sections (various formats)
        patterns = [
            # Pattern 1: "### Verse(s) X" or "### Verses X-Y"
            rf"###\s+Verses?\s+{start}[^#]*?(?=###\s+Verses?\s+{end+1}|###\s+Verse\s+{end+1}|$)",
            # Pattern 2: "**Verse X**" format
            rf"\*\*Verses?\s+{start}[^*]*?\*\*.*?(?=\*\*Verses?\s+{end+1}|\*\*Verse\s+{end+1}|$)",
        ]

        for pattern in patterns:
            matches = re.findall(pattern, content, re.DOTALL | re.MULTILINE)
            if matches:
                extracted_parts.extend(matches)
                break

    return '\n\n'.join(extracted_parts) if extracted_parts else content

def split_chapter_14_scholarly():
    """Split Chapter 14 scholarly: 179-187 and 188-196."""
    ch14_file = TRANSLATIONS_DIR / "Chapter_14_Buddhavagga_Scholarly.md"
    content = read_file(ch14_file)

    # Split based on verse ranges
    part1 = extract_verses_by_range(content, [(179, 187)])
    part2 = extract_verses_by_range(content, [(188, 196)])

    # If extraction failed, do manual split by finding "### Verses 188"
    if not part1 or not part2:
        split_marker = "### Verses 188-192: The Three Refuges"
        if split_marker in content:
            parts = content.split(split_marker)
            part1 = parts[0]
            part2 = split_marker + parts[1]
        else:
            # Fallback: just use the whole content for part 1
            part1 = content
            part2 = ""

    return part1, part2

def split_chapter_14_blues():
    """Split Chapter 14 blues: 179-187 and 188-196."""
    ch14_file = TRANSLATIONS_DIR / "Chapter_14_Buddhavagga_Blues.md"
    content = read_file(ch14_file)

    # Find the split point (around verse 188 - The Three Refuges)
    split_marker = "### Verses 188-192: The Three Refuges"
    if split_marker in content:
        parts = content.split(split_marker)
        part1 = parts[0]
        part2 = split_marker + parts[1]
    else:
        # Fallback
        part1 = content
        part2 = ""

    return part1, part2

def split_chapter_26_scholarly():
    """Split Chapter 26 scholarly: verses for Ch 27 and Ch 28."""
    ch26_file = TRANSLATIONS_DIR / "Chapter_26_Brahmanavagga_Scholarly.md"
    content = read_file(ch26_file)

    # Chapter 27 (Nibbānavagga): verses 383-386 + 411-423
    # Chapter 28 (Brāhmaṇavagga): verses 387-410

    # Extract verses 383-386
    verses_383_386 = extract_verse_section(content, 383, 386)

    # Extract verses 387-410
    verses_387_410 = extract_verse_section(content, 387, 410)

    # Extract verses 411-423
    verses_411_423 = extract_verse_section(content, 411, 423)

    ch27_content = verses_383_386 + "\n\n" + verses_411_423
    ch28_content = verses_387_410

    return ch27_content, ch28_content

def split_chapter_26_blues():
    """Split Chapter 26 blues: verses for Ch 27 and Ch 28."""
    ch26_file = TRANSLATIONS_DIR / "Chapter_26_Brahmanavagga_Blues.md"
    content = read_file(ch26_file)

    # Similar split as scholarly
    verses_383_386 = extract_verse_section(content, 383, 386)
    verses_387_410 = extract_verse_section(content, 387, 410)
    verses_411_423 = extract_verse_section(content, 411, 423)

    ch27_content = verses_383_386 + "\n\n" + verses_411_423
    ch28_content = verses_387_410

    return ch27_content, ch28_content

def extract_verse_section(content, start_verse, end_verse):
    """Extract a section of verses from content."""
    # Try to find verse markers
    lines = content.split('\n')
    in_section = False
    section_lines = []

    for line in lines:
        # Check if we're entering the section
        if re.search(rf'###\s+Verses?\s+{start_verse}', line) or \
           re.search(rf'\*\*Verses?\s+{start_verse}', line):
            in_section = True

        # Check if we're exiting the section
        if in_section and (re.search(rf'###\s+Verses?\s+{end_verse + 1}', line) or \
                          re.search(rf'\*\*Verses?\s+{end_verse + 1}', line)):
            in_section = False
            break

        if in_section:
            section_lines.append(line)

    return '\n'.join(section_lines)

def get_chapter_filename(chapter_num, edition):
    """Get the filename for a canonical chapter."""
    chapter_names = {
        1: "Yamakavagga", 2: "Appamadavagga", 3: "Cittavagga", 4: "Pupphavagga",
        5: "Balavagga", 6: "Panditavagga", 7: "Arahantavagga", 8: "Sahassavagga",
        9: "Papavagga", 10: "Dandavagga", 11: "Jaravagga", 12: "Attavagga",
        13: "Lokavagga", 14: "Buddhavagga", 15: "Sukhavagga", 16: "Piyavagga",
        17: "Kodhavagga", 18: "Malavagga", 19: "Dhammatthavagga", 20: "Maggavagga",
        21: "Pakinnakavagga", 22: "Nirayavagga", 23: "Nagavagga", 24: "Tanhavagga",
        25: "Bhikkhuvagga", 26: "Brahmanavagga"
    }

    name = chapter_names.get(chapter_num, "Unknown")
    suffix = "Scholarly" if edition == "scholarly" else "Blues"

    return f"Chapter_{chapter_num:02d}_{name}_{suffix}.md"

def populate_lunar_edition(template_file, edition):
    """
    Populate a lunar edition file with chapter content.

    Args:
        template_file: Path to the template file
        edition: 'scholarly' or 'blues'
    """
    print(f"\n{'='*60}")
    print(f"Populating {edition.upper()} edition: {template_file.name}")
    print(f"{'='*60}\n")

    # Read template
    template = read_file(template_file)

    # Track chapters processed
    chapters_processed = []

    # Process each lunar chapter 1-28
    for lunar_ch in range(1, 29):
        print(f"Processing Lunar Chapter {lunar_ch}...", end=" ")

        # Determine source content
        if lunar_ch in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
            # Direct mapping for chapters 1-13
            canonical_ch = lunar_ch
            filename = get_chapter_filename(canonical_ch, edition)
            filepath = TRANSLATIONS_DIR / filename

            if filepath.exists():
                chapter_content = read_file(filepath)
                chapters_processed.append(f"Ch {lunar_ch}: {filename}")
            else:
                chapter_content = f"[Chapter {canonical_ch} file not found: {filename}]"
                print(f"⚠️  FILE NOT FOUND: {filename}")

        elif lunar_ch == 14:
            # Chapter 14: Verses 179-187 from canonical Chapter 14
            if edition == "scholarly":
                part1, _ = split_chapter_14_scholarly()
                chapter_content = part1
            else:
                part1, _ = split_chapter_14_blues()
                chapter_content = part1
            chapters_processed.append(f"Ch 14: Buddhavagga (179-187)")

        elif lunar_ch == 15:
            # Chapter 15 (NEW): Verses 188-196 from canonical Chapter 14
            if edition == "scholarly":
                _, part2 = split_chapter_14_scholarly()
                chapter_content = part2
            else:
                _, part2 = split_chapter_14_blues()
                chapter_content = part2
            chapters_processed.append(f"Ch 15: Tathāgatavagga (188-196) ✨")

        elif lunar_ch in range(16, 27):
            # Chapters 16-26: Shifted from canonical 15-25
            canonical_ch = lunar_ch - 1  # Shift back by 1
            filename = get_chapter_filename(canonical_ch, edition)
            filepath = TRANSLATIONS_DIR / filename

            if filepath.exists():
                chapter_content = read_file(filepath)
                chapters_processed.append(f"Ch {lunar_ch}: {filename}")
            else:
                chapter_content = f"[Chapter {canonical_ch} file not found: {filename}]"
                print(f"⚠️  FILE NOT FOUND: {filename}")

        elif lunar_ch == 27:
            # Chapter 27 (NEW): Nibbānavagga - verses 383-386 + 411-423
            if edition == "scholarly":
                ch27_content, _ = split_chapter_26_scholarly()
                chapter_content = ch27_content
            else:
                ch27_content, _ = split_chapter_26_blues()
                chapter_content = ch27_content
            chapters_processed.append(f"Ch 27: Nibbānavagga (383-386, 411-423) ✨")

        elif lunar_ch == 28:
            # Chapter 28: Brāhmaṇavagga - verses 387-410
            if edition == "scholarly":
                _, ch28_content = split_chapter_26_scholarly()
                chapter_content = ch28_content
            else:
                _, ch28_content = split_chapter_26_blues()
                chapter_content = ch28_content
            chapters_processed.append(f"Ch 28: Brāhmaṇavagga (387-410)")

        # Find and replace placeholder in template
        # Placeholder patterns to search for
        placeholders = [
            f"[FULL CHAPTER CONTENT TO BE INSERTED HERE]",
            f"[VERSES 179-187 CONTENT TO BE INSERTED HERE]",
            f"[VERSES 188-196 CONTENT TO BE INSERTED HERE - THE THREE REFUGES]",
            f"[VERSES 383-386 AND 411-423 CONTENT TO BE INSERTED HERE - THE GOAL]",
            f"[VERSES 387-410 CONTENT TO BE INSERTED HERE - THE BRAHMIN]",
        ]

        # Try to replace the first occurrence after the chapter marker
        chapter_marker = f"## {'🌑🌒🌓🌔🌕🌖🌗🌘'[lunar_ch % 8]} DAY {lunar_ch}"

        if chapter_marker in template:
            # Find the section for this chapter
            chapter_start = template.find(chapter_marker)
            next_chapter_marker = f"## {'🌑🌒🌓🌔🌕🌖🌗🌘'[(lunar_ch + 1) % 8]} DAY {lunar_ch + 1}" if lunar_ch < 28 else "# CLOSING REFLECTION"
            chapter_end = template.find(next_chapter_marker, chapter_start) if lunar_ch < 28 else len(template)

            chapter_section = template[chapter_start:chapter_end]

            # Replace first placeholder found
            for placeholder in placeholders:
                if placeholder in chapter_section:
                    chapter_section = chapter_section.replace(placeholder, chapter_content, 1)
                    template = template[:chapter_start] + chapter_section + template[chapter_end:]
                    print("✓")
                    break
            else:
                print("⚠️  No placeholder found")
        else:
            print(f"⚠️  Chapter marker not found")

    # Write populated file
    output_file = template_file.parent / f"{template_file.stem}_POPULATED.md"
    write_file(output_file, template)

    print(f"\n{'='*60}")
    print(f"✓ Populated file saved: {output_file.name}")
    print(f"{'='*60}\n")

    # Print summary
    print("Chapters processed:")
    for ch in chapters_processed:
        print(f"  • {ch}")

    return output_file

def main():
    """Main function."""
    print("\n" + "="*60)
    print("DHAMMAPADA LUNAR EDITION POPULATION SCRIPT")
    print("="*60)

    # Check if template files exist
    if not LUNAR_SCHOLARLY.exists():
        print(f"❌ Error: Scholarly template not found: {LUNAR_SCHOLARLY}")
        return

    if not LUNAR_BLUES.exists():
        print(f"❌ Error: Blues template not found: {LUNAR_BLUES}")
        return

    # Populate scholarly edition
    scholarly_output = populate_lunar_edition(LUNAR_SCHOLARLY, "scholarly")

    # Populate blues edition
    blues_output = populate_lunar_edition(LUNAR_BLUES, "blues")

    print("\n" + "="*60)
    print("✓ POPULATION COMPLETE!")
    print("="*60)
    print(f"\nOutput files:")
    print(f"  • {scholarly_output.name}")
    print(f"  • {blues_output.name}")
    print("\nReview the populated files and rename them if satisfied.")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
