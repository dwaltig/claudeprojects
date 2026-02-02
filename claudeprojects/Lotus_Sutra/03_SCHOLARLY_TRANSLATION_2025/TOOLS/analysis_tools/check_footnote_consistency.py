#!/usr/bin/env python3
"""
Footnote Consistency Checker for Lotus Sutra Translation

Analyzes all chapter footnotes to identify inconsistencies in:
- Terminology definitions
- Sanskrit spelling and transliteration
- Cross-references and citations
- Tone and style
- Repeated concepts
"""

import re
import json
from pathlib import Path
from collections import defaultdict

def extract_footnotes_from_chapter(filepath):
    """Extract footnotes from a chapter markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    footnotes = {}
    apparatus_match = re.search(r'## Apparatus Summary\s*\n(.*?)(?=\n---|\n##|$)', content, re.DOTALL)

    if apparatus_match:
        apparatus_text = apparatus_match.group(1)
        blocks = re.split(r'\n\s*\n', apparatus_text)

        for block in blocks:
            block = block.strip()
            if not block:
                continue

            lines = block.split('\n')
            for i, line in enumerate(lines):
                item_match = re.match(r'^(\d+)\.\s+\*\*(.+?)\*\*\s*(.*)', line)
                if item_match:
                    num = item_match.group(1)
                    term = item_match.group(2)
                    rest = item_match.group(3)

                    if rest.startswith('('):
                        paren_match = re.match(r'^(.+?)\s*:\s*(.*)', rest)
                        explanation = paren_match.group(2) if paren_match else rest
                    else:
                        explanation = rest.lstrip(': ')

                    for j in range(i + 1, len(lines)):
                        next_line = lines[j]
                        if re.match(r'^\d+\.', next_line):
                            break
                        if next_line.strip():
                            explanation += ' ' + next_line.strip()

                    explanation = explanation.strip()
                    footnotes[num] = {'term': term, 'full_text': explanation[:200]}

    return footnotes

def extract_sanskrit_terms(text):
    """Extract Sanskrit terms in format: word (Skt. term)"""
    pattern = r'\(Skt\.\s+\*?([^)]+)\*?\)'
    return re.findall(pattern, text)

def main():
    base_path = Path('/Users/williamaltig/claudeprojects/Lotus_Sutra/03_SCHOLARLY_TRANSLATION_2025')

    # Collect all footnotes
    all_chapters_footnotes = {}
    term_definitions = defaultdict(list)  # Track same terms across chapters
    sanskrit_variations = defaultdict(set)  # Track Sanskrit spelling variations

    print("=" * 80)
    print("LOTUS SUTRA FOOTNOTE CONSISTENCY CHECKER")
    print("=" * 80)
    print()

    for ch_num in range(1, 29):
        filename = f'CHAPTER_{ch_num:02d}_*.md'
        matching_files = list(base_path.glob(filename))

        if not matching_files:
            continue

        filepath = matching_files[0]
        footnotes = extract_footnotes_from_chapter(filepath)

        if footnotes:
            all_chapters_footnotes[ch_num] = footnotes

            for num, data in footnotes.items():
                term = data['term']
                full_text = data['full_text']

                # Track term definitions
                term_definitions[term].append({
                    'chapter': ch_num,
                    'footnote': num,
                    'preview': full_text[:100]
                })

                # Extract Sanskrit terms
                sanskrit_terms = extract_sanskrit_terms(full_text)
                for sanskrit in sanskrit_terms:
                    sanskrit_variations[sanskrit].add(ch_num)

    # REPORT 1: Repeated terms with different definitions
    print("REPORT 1: REPEATED TERMS (Check for consistency)")
    print("-" * 80)

    repeated_terms = {k: v for k, v in term_definitions.items() if len(v) > 1}

    if repeated_terms:
        for term, occurrences in sorted(repeated_terms.items()):
            print(f"\n✓ Term: {term}")
            print(f"  Appears in {len(occurrences)} chapters:")
            for occ in occurrences:
                print(f"    - Ch {occ['chapter']}, Fn {occ['footnote']}: {occ['preview']}...")
    else:
        print("✓ No repeated terms found (each term appears only once)")

    print()
    print()

    # REPORT 2: Sanskrit transliteration consistency
    print("REPORT 2: SANSKRIT TRANSLITERATION")
    print("-" * 80)

    # Check for potential spelling variations (e.g., samadhi vs samādhi)
    potential_variations = defaultdict(list)

    for sanskrit in sanskrit_variations.keys():
        # Check if there's a variant with/without diacritics
        base = re.sub(r'[āēīōūṃṇ]', lambda m: {
            'ā': 'a', 'ē': 'e', 'ī': 'i', 'ō': 'o', 'ū': 'u',
            'ṃ': 'm', 'ṇ': 'n'
        }.get(m.group(0), m.group(0)), sanskrit)

        if base != sanskrit:
            potential_variations[base].append(sanskrit)

    if potential_variations:
        print("⚠ Potential transliteration variations (with/without diacritics):")
        for base, variants in sorted(potential_variations.items()):
            if len(variants) > 1:
                print(f"  {base}: {', '.join(sorted(set(variants)))}")
    else:
        print("✓ No transliteration variations detected")

    print()
    print()

    # REPORT 3: Chapters missing footnotes
    print("REPORT 3: FOOTNOTE COVERAGE BY CHAPTER")
    print("-" * 80)

    for ch_num in range(1, 29):
        if ch_num in all_chapters_footnotes:
            count = len(all_chapters_footnotes[ch_num])
            print(f"Chapter {ch_num:2d}: {count:2d} footnotes")
        else:
            print(f"Chapter {ch_num:2d}: ⚠ NO FOOTNOTES")

    print()
    print()

    # REPORT 4: Cross-reference verification
    print("REPORT 4: CROSS-REFERENCES (cf. Chapter X)")
    print("-" * 80)

    cross_refs = defaultdict(list)

    for ch_num, footnotes in all_chapters_footnotes.items():
        for num, data in footnotes.items():
            matches = re.findall(r'cf\. Chapter (\d+)', data['full_text'])
            for ref_ch in matches:
                cross_refs[f"Ch{ch_num}_Fn{num}"].append(int(ref_ch))

    if cross_refs:
        print("Cross-references found:")
        for source, targets in sorted(cross_refs.items()):
            print(f"  {source} → Chapter(s) {', '.join(str(t) for t in targets)}")
    else:
        print("✓ No cross-references (cf.) found in footnotes")

    print()
    print()

    # REPORT 5: Source citations consistency
    print("REPORT 5: SOURCE CITATIONS")
    print("-" * 80)

    source_patterns = [
        (r'\*([^*]+)\*\s+(?:\(|tradition)', 'italicized source'),
        (r'According to ([^,.:]+)', 'according to'),
        (r'\(Sanskrit|Skt\.', 'Sanskrit terms'),
    ]

    sources_found = defaultdict(int)

    for ch_num, footnotes in all_chapters_footnotes.items():
        for num, data in footnotes.items():
            text = data['full_text']

            # Look for sources
            if 'According to' in text:
                sources = re.findall(r'According to ([^,.:]+)', text)
                for source in sources:
                    sources_found[source.strip()] += 1

    if sources_found:
        print("Source citations used:")
        for source, count in sorted(sources_found.items(), key=lambda x: -x[1]):
            print(f"  '{source}': {count} times")
    else:
        print("⚠ No 'According to' citations found")

    print()
    print()

    # REPORT 6: Suggested actions
    print("REPORT 6: RECOMMENDATIONS")
    print("-" * 80)

    recommendations = []

    if len([c for c in all_chapters_footnotes.keys() if c < 11]) < 10:
        recommendations.append("- Chapters 1-10 have incomplete footnote coverage")

    if potential_variations:
        recommendations.append("- Review Sanskrit diacritical consistency (macrons, tildes, dots)")

    if len(repeated_terms) > 5:
        recommendations.append("- Many repeated terms—verify definitions are consistent")

    if not sources_found:
        recommendations.append("- Add source citations (e.g., 'According to...') to more footnotes")

    if recommendations:
        for rec in recommendations:
            print(rec)
    else:
        print("✓ No major consistency issues detected!")

    print()
    print("=" * 80)
    print(f"SUMMARY: {sum(len(f) for f in all_chapters_footnotes.values())} total footnotes analyzed")
    print("=" * 80)

if __name__ == '__main__':
    main()
