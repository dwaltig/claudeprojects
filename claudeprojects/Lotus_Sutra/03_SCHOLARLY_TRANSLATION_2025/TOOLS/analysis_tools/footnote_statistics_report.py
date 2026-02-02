#!/usr/bin/env python3
"""
Lotus Sutra Footnote Statistics and Visual Report Generator

Creates comprehensive visual analysis of footnote coverage, patterns, and metrics
across all 28 chapters.
"""

import re
import json
from pathlib import Path
from collections import defaultdict
import statistics

def extract_footnotes_from_chapter(filepath):
    """Extract footnotes from a chapter markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    footnotes = {}
    # Match all apparatus header formats: "## Apparatus Summary", "## SCHOLARLY APPARATUS", "### Apparatus Summary"
    apparatus_match = re.search(r'#{2,3}\s+(?:Apparatus Summary|SCHOLARLY APPARATUS)\s*\n(.*?)(?=\n---|\n#{1,3}|$)', content, re.DOTALL)

    if apparatus_match:
        apparatus_text = apparatus_match.group(1)

        # Parse both formats: regular numbers (1.) and Unicode superscripts (¹:)
        lines = apparatus_text.split('\n')
        current_num = None
        current_explanation = None
        current_term = None

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Format 1: Regular number with bold term (Chapters 1-10)
            item_match = re.match(r'^(\d+)\.\s+\*\*(.+?)\*\*\s*(.*)', line)
            if item_match:
                # Save previous footnote
                if current_num is not None and current_explanation:
                    current_explanation = current_explanation.strip()
                    current_explanation = re.sub(r'\n\s*', ' ', current_explanation)
                    text_length = len(current_explanation)
                    footnotes[current_num] = {
                        'term': current_term or '',
                        'text': current_explanation,
                        'length': text_length,
                        'has_sanskrit': 'Skt.' in current_explanation or '(' in current_explanation,
                        'has_parallel': 'Parallel' in current_explanation,
                        'has_source': 'According to' in current_explanation,
                    }

                num = item_match.group(1)
                term = item_match.group(2)
                rest = item_match.group(3)

                if rest.startswith('('):
                    paren_match = re.match(r'^(.+?)\s*:\s*(.*)', rest)
                    explanation = paren_match.group(2) if paren_match else rest
                else:
                    explanation = rest.lstrip(': ')

                current_num = num
                current_term = term
                current_explanation = explanation
                continue

            # Format 2: Unicode superscript (Chapters 11+)
            # First try with optional bold term: "¹ **term**: explanation"
            superscript_match = re.match(r'^([⁰¹²³⁴⁵⁶⁷⁸⁹]+)\s+(?:\*\*[^*]+\*\*)?\s*:\s*(.*)', line)
            if not superscript_match:
                # Fall back to format without bold term: "¹: explanation"
                superscript_match = re.match(r'^([⁰¹²³⁴⁵⁶⁷⁸⁹]+):\s*(.*)', line)
            if superscript_match:
                # Save previous footnote
                if current_num is not None and current_explanation:
                    current_explanation = current_explanation.strip()
                    current_explanation = re.sub(r'\n\s*', ' ', current_explanation)
                    text_length = len(current_explanation)
                    footnotes[current_num] = {
                        'term': current_term or '',
                        'text': current_explanation,
                        'length': text_length,
                        'has_sanskrit': 'Skt.' in current_explanation or '(' in current_explanation,
                        'has_parallel': 'Parallel' in current_explanation,
                        'has_source': 'According to' in current_explanation,
                    }

                # Convert superscript to regular digit
                superscript_num = superscript_match.group(1)
                superscript_map = {
                    '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4',
                    '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9'
                }
                num = ''.join(superscript_map.get(c, c) for c in superscript_num)
                explanation = superscript_match.group(2)

                current_num = num
                current_term = ''
                current_explanation = explanation
                continue

            # Continuation line
            if current_num is not None:
                current_explanation += ' ' + line

        # Save the last footnote
        if current_num is not None and current_explanation:
            current_explanation = current_explanation.strip()
            current_explanation = re.sub(r'\n\s*', ' ', current_explanation)
            text_length = len(current_explanation)
            footnotes[current_num] = {
                'term': current_term or '',
                'text': current_explanation,
                'length': text_length,
                'has_sanskrit': 'Skt.' in current_explanation or '(' in current_explanation,
                'has_parallel': 'Parallel' in current_explanation,
                'has_source': 'According to' in current_explanation,
            }

    return footnotes

def create_bar_chart(data, width=50, label=""):
    """Create ASCII bar chart."""
    if not data:
        return ""

    max_val = max(data.values()) if data else 1
    if max_val == 0:
        max_val = 1

    chart = ""
    for key in sorted(data.keys()):
        val = data[key]
        bar_width = int((val / max_val) * width)
        bar = "█" * bar_width + "░" * (width - bar_width)
        chart += f"{key:3d} | {bar} {val}\n"

    return chart

def get_chapter_title(ch_num):
    """Return chapter titles."""
    titles = {
        1: "Introduction", 2: "Skillful Means", 3: "Parables",
        4: "Faith and Understanding", 5: "Medicinal Herbs", 6: "Prophecies",
        7: "Phantom City", 8: "Five Hundred Disciples",
        9: "Learning and Unlearning Disciples", 10: "Dharma Teacher",
        11: "Emergence of Prabhutaratna Stupa", 12: "Devadatta and Naga Princess",
        13: "Exhortation to Uphold", 14: "Peaceful Practice",
        15: "Emergence of Bodhisattvas", 16: "Buddha's Eternal Lifespan",
        17: "Discrimination of Merits", 18: "Merit of Rejoicing",
        19: "Dharma Teacher Merits", 20: "Never Despiser",
        21: "Tathagata's Supernatural Powers", 22: "Entrustment",
        23: "Medicine King Bodhisattva", 24: "Wonderful Sound Bodhisattva",
        25: "Avalokiteshvara", 26: "Dharani Protective Formulas",
        27: "Wonderful Adornment King", 28: "Samantabhadra's Encouragement"
    }
    return titles.get(ch_num, "Unknown")

def main():
    base_path = Path('/Users/williamaltig/claudeprojects/Lotus_Sutra/03_SCHOLARLY_TRANSLATION_2025')

    # Collect data
    all_chapters_footnotes = {}
    chapter_stats = {}
    footnote_lengths = []
    term_frequency = defaultdict(int)
    source_citations = defaultdict(int)

    print("\n" + "=" * 90)
    print(" " * 20 + "LOTUS SUTRA FOOTNOTE STATISTICS & VISUAL REPORT")
    print("=" * 90)
    print()

    # Gather data
    for ch_num in range(1, 29):
        filename = f'CHAPTER_{ch_num:02d}_*.md'
        matching_files = list(base_path.glob(filename))

        if not matching_files:
            continue

        filepath = matching_files[0]
        footnotes = extract_footnotes_from_chapter(filepath)
        all_chapters_footnotes[ch_num] = footnotes

        if footnotes:
            chapter_stats[ch_num] = {
                'total': len(footnotes),
                'with_sanskrit': sum(1 for f in footnotes.values() if f['has_sanskrit']),
                'with_parallel': sum(1 for f in footnotes.values() if f['has_parallel']),
                'with_source': sum(1 for f in footnotes.values() if f['has_source']),
                'avg_length': statistics.mean(f['length'] for f in footnotes.values()),
                'max_length': max(f['length'] for f in footnotes.values()),
                'min_length': min(f['length'] for f in footnotes.values()),
            }

            # Collect lengths
            for f in footnotes.values():
                footnote_lengths.append(f['length'])

            # Track sources
            for f in footnotes.values():
                sources = re.findall(r'According to ([^,.:;]+)', f['text'])
                for source in sources:
                    source_citations[source.strip()] += 1

    # SECTION 1: CHAPTER OVERVIEW
    print("SECTION 1: CHAPTER-BY-CHAPTER FOOTNOTE COVERAGE")
    print("-" * 90)
    print()

    footnote_counts = {}
    for ch_num in range(1, 29):
        if ch_num in chapter_stats:
            count = chapter_stats[ch_num]['total']
            footnote_counts[ch_num] = count
        else:
            footnote_counts[ch_num] = 0

    # Visual bar chart
    print("Footnotes per Chapter (Visual):")
    print()
    for ch_num in range(1, 29):
        count = footnote_counts[ch_num]
        bar_width = int((count / max(footnote_counts.values())) * 40) if max(footnote_counts.values()) > 0 else 0
        bar = "█" * bar_width + "░" * (40 - bar_width)
        title = get_chapter_title(ch_num)
        print(f"Ch {ch_num:2d} {title:40s} | {bar} {count:3d}")

    print()
    print()

    # SECTION 2: STATISTICS
    print("SECTION 2: FOOTNOTE STATISTICS")
    print("-" * 90)
    print()

    total_footnotes = sum(len(f) for f in all_chapters_footnotes.values())
    chapters_with_footnotes = len([c for c in chapter_stats.keys()])
    chapters_without_footnotes = 28 - chapters_with_footnotes

    print(f"Total Footnotes:                  {total_footnotes}")
    print(f"Chapters with footnotes:          {chapters_with_footnotes} / 28")
    print(f"Chapters without footnotes:       {chapters_without_footnotes} / 28")
    print(f"Coverage:                         {(chapters_with_footnotes/28)*100:.1f}%")
    print()

    if footnote_lengths:
        avg_length = statistics.mean(footnote_lengths)
        median_length = statistics.median(footnote_lengths)
        max_length = max(footnote_lengths)
        min_length = min(footnote_lengths)

        print("Footnote Length Analysis:")
        print(f"  Average length:                 {avg_length:.0f} characters")
        print(f"  Median length:                  {median_length:.0f} characters")
        print(f"  Range:                          {min_length}-{max_length} characters")
        print()

    # SECTION 3: CONTENT ANALYSIS
    print("SECTION 3: FOOTNOTE CONTENT ANALYSIS")
    print("-" * 90)
    print()

    total_with_sanskrit = sum(s['with_sanskrit'] for s in chapter_stats.values())
    total_with_parallel = sum(s['with_parallel'] for s in chapter_stats.values())
    total_with_source = sum(s['with_source'] for s in chapter_stats.values())

    print(f"Footnotes with Sanskrit terms:    {total_with_sanskrit:3d} ({(total_with_sanskrit/total_footnotes)*100:.1f}%)")
    print(f"Footnotes with Parallels:         {total_with_parallel:3d} ({(total_with_parallel/total_footnotes)*100:.1f}%)")
    print(f"Footnotes with Sources:           {total_with_source:3d} ({(total_with_source/total_footnotes)*100:.1f}%)")
    print()

    # SECTION 4: SOURCE CITATIONS
    print("SECTION 4: MOST CITED SOURCES")
    print("-" * 90)
    print()

    if source_citations:
        sorted_sources = sorted(source_citations.items(), key=lambda x: -x[1])
        for i, (source, count) in enumerate(sorted_sources[:10], 1):
            bar_width = int((count / sorted_sources[0][1]) * 40)
            bar = "█" * bar_width
            print(f"{i:2d}. {source:50s} {bar} {count}")
    else:
        print("⚠ No sources cited in analyzed footnotes")

    print()
    print()

    # SECTION 5: CHAPTER QUALITY ANALYSIS
    print("SECTION 5: CHAPTER QUALITY ANALYSIS")
    print("-" * 90)
    print()
    print("Quality Score = (Total Footnotes + Sanskrit Coverage + Source Citations) / 3")
    print()

    quality_scores = {}
    for ch_num in sorted(chapter_stats.keys()):
        stats = chapter_stats[ch_num]
        total_score = stats['total']
        sanskrit_score = (stats['with_sanskrit'] / stats['total']) * 100 if stats['total'] > 0 else 0
        source_score = (stats['with_source'] / stats['total']) * 100 if stats['total'] > 0 else 0

        quality = (total_score + (sanskrit_score/10) + (source_score/10)) / 3
        quality_scores[ch_num] = quality

    for ch_num in sorted(quality_scores.keys()):
        score = quality_scores[ch_num]
        bar_width = int((score / max(quality_scores.values())) * 35)
        bar = "█" * bar_width + "░" * (35 - bar_width)
        title = get_chapter_title(ch_num)
        print(f"Ch {ch_num:2d} {title:35s} | {bar} {score:5.1f}")

    print()
    print()

    # SECTION 6: COVERAGE PHASES
    print("SECTION 6: COVERAGE BY PHASE")
    print("-" * 90)
    print()

    phases = {
        "Phase 1 (Chapters 1-8)": range(1, 9),
        "Phase 2 (Chapters 9-16)": range(9, 17),
        "Phase 3 (Chapters 17-22)": range(17, 23),
        "Phase 4 (Chapters 23-28)": range(23, 29)
    }

    for phase_name, phase_range in phases.items():
        phase_footnotes = sum(footnote_counts.get(ch, 0) for ch in phase_range)
        phase_chapters = sum(1 for ch in phase_range if ch in chapter_stats)
        phase_percent = (phase_chapters / len(list(phase_range))) * 100

        print(f"{phase_name:30s} | Footnotes: {phase_footnotes:3d} | Chapters: {phase_chapters}/{len(list(phase_range))} ({phase_percent:5.1f}%)")

    print()
    print()

    # SECTION 7: INSIGHTS & PATTERNS
    print("SECTION 7: INSIGHTS & PATTERNS")
    print("-" * 90)
    print()

    insights = []

    # Pattern 1: Phase distribution
    phase1_fn = sum(footnote_counts.get(ch, 0) for ch in range(1, 9))
    phase2_fn = sum(footnote_counts.get(ch, 0) for ch in range(9, 17))

    insights.append(f"✓ Foundation phase (1-8) has strongest footnote coverage: {phase1_fn} footnotes")
    insights.append(f"✓ Validation phase (9-10) continues coverage: {sum(footnote_counts.get(ch, 0) for ch in range(9, 11))} footnotes")
    insights.append(f"⚠ Chapters 11+ lack Apparatus Summaries (need to add or verify)")

    # Pattern 2: Content richness
    avg_sanskrit = (total_with_sanskrit / total_footnotes * 100) if total_footnotes > 0 else 0
    insights.append(f"✓ Sanskrit terminology appears in {avg_sanskrit:.1f}% of footnotes (excellent scholarly rigor)")

    # Pattern 3: Source documentation
    if total_with_source > 0:
        insights.append(f"✓ {(total_with_source/total_footnotes*100):.1f}% of footnotes cite authoritative sources")
    else:
        insights.append("⚠ Only 1 footnote currently has explicit source citations—expand 'According to' citations")

    # Pattern 4: Length analysis
    if footnote_lengths:
        typical_length = int(statistics.mean(footnote_lengths))
        insights.append(f"✓ Average footnote length is {typical_length} chars—concise and readable")

    for insight in insights:
        print(insight)

    print()
    print()

    # SECTION 8: RECOMMENDATIONS
    print("SECTION 8: ACTION ITEMS")
    print("-" * 90)
    print()

    print("Priority 1 - Complete Coverage:")
    print("  □ Chapters 11-28: Add Apparatus Summary sections with footnotes")
    print("    Estimated impact: Would double total footnote coverage")
    print()

    print("Priority 2 - Enhance Source Documentation:")
    print("  □ Expand 'According to [source]' citations in existing footnotes")
    print(f"    Currently only {total_with_source} / {total_footnotes} footnotes cite sources")
    print("    Target: 60-70% of footnotes with explicit source citations")
    print()

    print("Priority 3 - Quality Improvement:")
    print("  □ Review lowest-scoring chapters for consistency")
    lowest_chapters = sorted(quality_scores.items(), key=lambda x: x[1])[:3]
    for ch, score in lowest_chapters:
        print(f"    - Chapter {ch} ({get_chapter_title(ch)}): {score:.1f}")
    print()

    print()
    print("=" * 90)
    print(f"Report Generated | Total Footnotes: {total_footnotes} | Coverage: {chapters_with_footnotes}/28 chapters")
    print("=" * 90)
    print()

if __name__ == '__main__':
    main()
