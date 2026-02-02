#!/usr/bin/env python3
"""
Comprehensive Proofreading Analysis Script
For The Lotus Sutra - Blues Interpretation
"""

import re
from collections import defaultdict

def analyze_file(filepath):
    """Perform comprehensive proofreading analysis."""

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    issues = {
        'capitalization': [],
        'punctuation': [],
        'typos': [],
        'spacing': [],
        'consistency': [],
        'diacriticals': []
    }

    # Patterns to check
    proper_names = [
        'Śāriputra', 'Śākyamuni', 'Mañjuśrī', 'Avalokiteśvara',
        'Mahākāśyapa', 'Maitreya', 'Ānanda', 'Mahāprajāpatī',
        'Yaśodharā', 'Kumārajīva', 'Dharmarakṣa'
    ]

    # Track chapter numbers
    chapter_pattern = re.compile(r'Chapter\s+(\w+):\s*(.+)')
    chapters_found = []

    for i, line in enumerate(lines, 1):
        original_line = line.rstrip('\n')

        # Skip empty lines
        if not original_line.strip():
            continue

        # Check for capitalization inconsistencies
        # Pattern 1: "The" vs "the" at start of sentences/clauses
        if re.search(r'[.!?]\s+the\s+', original_line):
            issues['capitalization'].append({
                'line': i,
                'text': original_line[:100],
                'issue': 'Lowercase "the" after sentence-ending punctuation',
                'pattern': 'sentence_the'
            })

        # Pattern 2: "To" vs "to" inconsistencies
        if re.search(r'^\s*to\s+[A-Z]', original_line):
            issues['capitalization'].append({
                'line': i,
                'text': original_line[:100],
                'issue': 'Lowercase "to" at start of line before capitalized word',
                'pattern': 'line_start_to'
            })

        # Check for double spaces
        if '  ' in original_line:
            issues['spacing'].append({
                'line': i,
                'text': original_line[:100],
                'issue': 'Double space found',
                'count': original_line.count('  ')
            })

        # Check for missing space after punctuation
        if re.search(r'[.!?,;:][A-Za-z]', original_line):
            issues['punctuation'].append({
                'line': i,
                'text': original_line[:100],
                'issue': 'Missing space after punctuation'
            })

        # Check for space before punctuation (common error)
        if re.search(r'\s+[.,!?;:](?:\s|$)', original_line):
            issues['punctuation'].append({
                'line': i,
                'text': original_line[:100],
                'issue': 'Space before punctuation mark'
            })

        # Check for repeated words
        words = original_line.split()
        for j in range(len(words) - 1):
            if words[j].lower() == words[j+1].lower():
                issues['typos'].append({
                    'line': i,
                    'text': original_line[:100],
                    'issue': f'Repeated word: "{words[j]}"'
                })

        # Check for missing apostrophes in common contractions
        contractions = ['dont', 'cant', 'wont', 'aint', 'wasnt', 'werent',
                       'hasnt', 'hadnt', 'shouldnt', 'couldnt', 'wouldnt',
                       'isnt', 'arent', 'didnt', 'doesnt']
        for contraction in contractions:
            if re.search(rf'\b{contraction}\b', original_line, re.IGNORECASE):
                issues['typos'].append({
                    'line': i,
                    'text': original_line[:100],
                    'issue': f'Missing apostrophe in contraction: "{contraction}"'
                })

        # Check chapter numbering
        chapter_match = chapter_pattern.search(original_line)
        if chapter_match:
            chapters_found.append({
                'line': i,
                'number': chapter_match.group(1),
                'title': chapter_match.group(2).strip()
            })

        # Check for proper name consistency (case-sensitive)
        for name in proper_names:
            # Look for variations without diacriticals
            base_name = name.replace('ś', 's').replace('ṇ', 'n').replace('ā', 'a').replace('ṃ', 'm').replace('ū', 'u')
            if base_name.lower() != name.lower():
                # Check if base name appears without proper diacriticals
                pattern = re.compile(rf'\b{re.escape(base_name)}\b', re.IGNORECASE)
                if pattern.search(original_line) and name not in original_line:
                    issues['diacriticals'].append({
                        'line': i,
                        'text': original_line[:100],
                        'issue': f'Missing diacriticals: found "{base_name}", should be "{name}"'
                    })

        # Check for inconsistent dash usage
        if '--' in original_line and '—' in original_line:
            issues['punctuation'].append({
                'line': i,
                'text': original_line[:100],
                'issue': 'Mixed dash styles (-- and —) in same line'
            })

        # Check for sentences ending without punctuation
        stripped = original_line.strip()
        if stripped and len(stripped) > 20:
            if stripped[-1] not in '.!?"\'':
                # Check if it's not a heading or chapter marker
                if not chapter_match and not stripped.isupper():
                    issues['punctuation'].append({
                        'line': i,
                        'text': original_line[:100],
                        'issue': 'Line may be missing ending punctuation'
                    })

    return issues, chapters_found, len(lines)

def generate_report(issues, chapters, total_lines):
    """Generate comprehensive report."""

    report = []
    report.append("=" * 80)
    report.append("COMPREHENSIVE PROOFREADING REPORT")
    report.append("The Lotus Sutra: A Blues Interpretation")
    report.append("=" * 80)
    report.append(f"\nDocument Statistics:")
    report.append(f"  Total lines: {total_lines}")
    report.append(f"  Chapters found: {len(chapters)}")
    report.append("")

    # Summary counts
    report.append("\nISSUE SUMMARY BY CATEGORY:")
    report.append("-" * 80)
    total_issues = 0
    for category, items in sorted(issues.items()):
        count = len(items)
        total_issues += count
        report.append(f"  {category.capitalize()}: {count} issue(s)")
    report.append(f"\n  TOTAL ISSUES FOUND: {total_issues}")
    report.append("")

    # Detailed findings by category
    for category in ['capitalization', 'punctuation', 'spacing', 'typos', 'diacriticals', 'consistency']:
        items = issues[category]
        if items:
            report.append("\n" + "=" * 80)
            report.append(f"{category.upper()} ISSUES ({len(items)} found)")
            report.append("=" * 80)

            # Group similar issues
            grouped = defaultdict(list)
            for item in items:
                issue_type = item.get('issue', 'Unknown')
                grouped[issue_type].append(item)

            for issue_type, occurrences in sorted(grouped.items()):
                report.append(f"\n{issue_type} ({len(occurrences)} occurrence(s)):")
                report.append("-" * 80)

                # Show first 10 occurrences, then summary
                for idx, item in enumerate(occurrences[:10], 1):
                    report.append(f"  [{idx}] Line {item['line']}: {item['text']}")

                if len(occurrences) > 10:
                    report.append(f"  ... and {len(occurrences) - 10} more occurrence(s)")
                report.append("")
        else:
            report.append(f"\n{category.upper()}: No issues found ✓")

    # Chapter structure analysis
    if chapters:
        report.append("\n" + "=" * 80)
        report.append(f"CHAPTER STRUCTURE ({len(chapters)} chapters)")
        report.append("=" * 80)
        for idx, ch in enumerate(chapters[:10], 1):
            report.append(f"  Line {ch['line']}: Chapter {ch['number']}: {ch['title']}")
        if len(chapters) > 10:
            report.append(f"  ... and {len(chapters) - 10} more chapters")

    return "\n".join(report)

if __name__ == '__main__':
    input_file = '/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/temp_converted.txt'
    output_file = '/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/PROOFREADING_REPORT.txt'

    print("Analyzing document...")
    issues, chapters, total_lines = analyze_file(input_file)

    print("Generating report...")
    report = generate_report(issues, chapters, total_lines)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\nReport saved to: {output_file}")
    print(f"Total issues found: {sum(len(items) for items in issues.values())}")
