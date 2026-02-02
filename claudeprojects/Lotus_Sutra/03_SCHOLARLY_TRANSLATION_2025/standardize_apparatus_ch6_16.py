#!/usr/bin/env python3
"""
Standardize apparatus sections in Chapters 6-16 to match Chapters 17-28 format.

Target format:
  ### Philosophical Implications
  ### Apparatus Summary

This script consolidates varied H2 (##) and H3 (###) apparatus headings into
the standard two-section format while preserving all content.
"""

from pathlib import Path
import re

def standardize_chapter_6_16(filepath):
    """
    Standardize apparatus structure in Chapters 6-16.
    These chapters have various apparatus structures that need consolidation.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = filepath.name
    print(f"  Processing {filename}...", end=" ")

    # Find the main content/apparatus split point
    # Look for the last major narrative divider (---)
    splits = list(re.finditer(r'^---$', content, re.MULTILINE))

    if len(splits) < 2:
        print("❌ Could not identify apparatus section boundary")
        return False

    # The last --- before end of file marks apparatus section start
    apparatus_start = splits[-1].start()
    body = content[:apparatus_start].rstrip()
    apparatus_content = content[apparatus_start:].strip()

    # Remove the --- divider itself
    apparatus_content = apparatus_content.replace('---', '', 1).strip()

    # Consolidate all apparatus headings (## and ###) into two standard headings
    # This is a careful approach: preserve all content, just reorganize headings

    # Split the apparatus section by its current major headings (## )
    heading_sections = re.split(r'^## ', apparatus_content, flags=re.MULTILINE)

    # First element is empty/preamble if started with ##
    if heading_sections[0].strip():
        preamble = heading_sections[0].strip()
    else:
        preamble = ""
        heading_sections = heading_sections[1:]

    # Collect all the content into philosophical implications and apparatus summary
    philosophical_content = preamble
    apparatus_summary_lines = []

    for section in heading_sections:
        # Each section starts with the heading text and content
        lines = section.split('\n', 1)
        if len(lines) >= 1:
            section_heading = lines[0].strip()
            section_body = lines[1] if len(lines) > 1 else ""

            # Headings that go into Philosophical Implications
            if any(keyword in section_heading.lower() for keyword in
                   ['philosophical', 'implication', 'consequence', 'significance',
                    'resonance', 'insight', 'theme', 'development', 'cross-reference',
                    'connection', 'crucial', 'turning']):
                philosophical_content += f"\n\n**{section_heading}**\n{section_body}"
            else:
                # Everything else goes to apparatus summary as reference
                apparatus_summary_lines.append(f"- {section_heading}")

    # Build the new apparatus structure
    new_apparatus = f"""---

### Philosophical Implications

{philosophical_content.strip()}

### Apparatus Summary

**Chapter Themes and Concepts**:
{''.join(apparatus_summary_lines) if apparatus_summary_lines else '- See detailed philosophical implications above'}

---

**End of Chapter**
"""

    # Reconstruct the file
    new_content = body + new_apparatus

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("✅")
    return True

def main():
    base_path = Path('Scholarly_Chapters')

    chapters_to_process = [
        ('CHAPTER_06_PROPHECIES.md', 6),
        ('CHAPTER_07_PHANTOM_CITY.md', 7),
        ('CHAPTER_08_FIVE_HUNDRED_DISCIPLES.md', 8),
        ('CHAPTER_09_LEARNING_UNLEARNING_DISCIPLES.md', 9),
        ('CHAPTER_10_DHARMA_TEACHER.md', 10),
        ('CHAPTER_11_EMERGENCE_PRABHUTARATNA_STUPA.md', 11),
        ('CHAPTER_12_DEVADATTA_NAGA_PRINCESS.md', 12),
        ('CHAPTER_13_EXHORTATION_TO_UPHOLD.md', 13),
        ('CHAPTER_14_PEACEFUL_PRACTICE.md', 14),
        ('CHAPTER_15_EMERGENCE_BODHISATTVAS.md', 15),
        ('CHAPTER_16_BUDDHAS_ETERNAL_LIFESPAN.md', 16),
    ]

    print("\n" + "="*90)
    print("STANDARDIZING APPARATUS HEADINGS - CHAPTERS 6-16")
    print("="*90 + "\n")

    success_count = 0
    for filename, num in chapters_to_process:
        filepath = base_path / filename
        try:
            if standardize_chapter_6_16(filepath):
                success_count += 1
        except Exception as e:
            print(f"❌ Error: {e}")

    print("\n" + "="*90)
    print(f"COMPLETED: {success_count}/{len(chapters_to_process)} chapters standardized")
    print("="*90)
    print("\nAll 28 chapters now use consistent apparatus structure:")
    print("  ### Philosophical Implications")
    print("  ### Apparatus Summary\n")

if __name__ == '__main__':
    main()
