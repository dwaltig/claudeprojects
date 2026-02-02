#!/usr/bin/env python3
"""
Detailed Proofreading Analysis - Focus on User's Priority Issues
Especially capitalization inconsistencies (The/the, To/to)
"""

import re
from collections import defaultdict

def analyze_capitalization_detailed(lines):
    """Detailed analysis of capitalization patterns."""
    issues = []

    # Track "The" vs "the" patterns
    the_patterns = {
        'sentence_start_lowercase': [],  # ". the" or "! the" or "? the"
        'clause_start_lowercase': [],    # ", the" in mid-sentence
        'line_start_lowercase': [],      # Line starts with "the"
        'line_start_uppercase': [],      # Line starts with "The"
        'inconsistent_parallels': []     # Similar contexts with different capitalization
    }

    # Track "To" vs "to" patterns
    to_patterns = {
        'sentence_start_lowercase': [],
        'line_start_lowercase': [],
        'line_start_uppercase': [],
        'inconsistent_infinitives': []
    }

    for i, line in enumerate(lines, 1):
        text = line.rstrip('\n')
        if not text.strip():
            continue

        # Pattern 1: "the" after sentence-ending punctuation
        for match in re.finditer(r'([.!?])\s+(the)\s+', text):
            the_patterns['sentence_start_lowercase'].append({
                'line': i,
                'context': text[max(0, match.start()-20):min(len(text), match.end()+30)],
                'full_line': text
            })

        # Pattern 2: Line starts with lowercase "the"
        if re.match(r'^\s*the\s+[A-Z]', text):
            the_patterns['line_start_lowercase'].append({
                'line': i,
                'text': text[:80]
            })

        # Pattern 3: Line starts with uppercase "The"
        if re.match(r'^\s*The\s+', text):
            the_patterns['line_start_uppercase'].append({
                'line': i,
                'text': text[:80]
            })

        # Pattern 4: "to" after sentence-ending punctuation
        for match in re.finditer(r'([.!?])\s+(to)\s+', text):
            to_patterns['sentence_start_lowercase'].append({
                'line': i,
                'context': text[max(0, match.start()-20):min(len(text), match.end()+30)],
                'full_line': text
            })

        # Pattern 5: Line starts with lowercase "to"
        if re.match(r'^\s*to\s+[A-Z]', text):
            to_patterns['line_start_lowercase'].append({
                'line': i,
                'text': text[:80]
            })

        # Pattern 6: Line starts with uppercase "To"
        if re.match(r'^\s*To\s+', text):
            to_patterns['line_start_uppercase'].append({
                'line': i,
                'text': text[:80]
            })

    return the_patterns, to_patterns

def analyze_punctuation_detailed(lines):
    """Detailed punctuation analysis."""
    issues = {
        'missing_space_after': [],
        'extra_space_before': [],
        'double_punctuation': [],
        'quote_issues': [],
        'dash_inconsistency': []
    }

    for i, line in enumerate(lines, 1):
        text = line.rstrip('\n')
        if not text.strip():
            continue

        # Missing space after punctuation
        for match in re.finditer(r'([.!?,;:])[A-Za-z]', text):
            if match.group(0) not in ['Dr.', 'Mr.', 'Mrs.', 'Ms.', 'U.S.', 'U.K.']:
                issues['missing_space_after'].append({
                    'line': i,
                    'position': match.start(),
                    'context': text[max(0, match.start()-10):min(len(text), match.end()+20)]
                })

        # Extra space before punctuation
        for match in re.finditer(r'\s+([.!?,;:])(?:\s|$)', text):
            issues['extra_space_before'].append({
                'line': i,
                'position': match.start(),
                'context': text[max(0, match.start()-20):min(len(text), match.end()+10)],
                'punctuation': match.group(1)
            })

        # Mixed dash styles in same line
        if '--' in text and '—' in text:
            issues['dash_inconsistency'].append({
                'line': i,
                'text': text[:100]
            })

        # Count dash types for overall consistency
        if '--' in text:
            issues.setdefault('double_dash_lines', []).append(i)
        if '—' in text:
            issues.setdefault('em_dash_lines', []).append(i)

    return issues

def analyze_spacing(lines):
    """Detailed spacing analysis."""
    issues = {
        'double_space': [],
        'triple_space': [],
        'tab_space_mix': []
    }

    for i, line in enumerate(lines, 1):
        text = line.rstrip('\n')

        # Double spaces
        if '  ' in text:
            count = len(re.findall(r'  +', text))
            issues['double_space'].append({
                'line': i,
                'count': count,
                'text': text[:100]
            })

        # Triple or more spaces
        if '   ' in text:
            issues['triple_space'].append({
                'line': i,
                'text': text[:100]
            })

    return issues

def analyze_typos(lines):
    """Common typo patterns."""
    issues = {
        'repeated_words': [],
        'common_misspellings': [],
        'missing_apostrophes': []
    }

    # Common contractions that should have apostrophes
    contractions = {
        r"\baint\b": "ain't",
        r"\bdont\b": "don't",
        r"\bcant\b": "can't",
        r"\bwont\b": "won't",
        r"\bwasnt\b": "wasn't",
        r"\bwerent\b": "weren't",
        r"\bhasnt\b": "hasn't",
        r"\bhadnt\b": "hadn't",
        r"\bshouldnt\b": "shouldn't",
        r"\bcouldnt\b": "couldn't",
        r"\bwouldnt\b": "wouldn't",
        r"\bisnt\b": "isn't",
        r"\barent\b": "aren't",
        r"\bdidnt\b": "didn't",
        r"\bdoesnt\b": "doesn't",
        r"\bgonna\b": "gonna",  # This one's okay in blues
        r"\bwanna\b": "wanna",  # This one's okay in blues
        r"\bImma\b": "I'mma",
        r"\byall\b": "y'all"
    }

    for i, line in enumerate(lines, 1):
        text = line.rstrip('\n')
        if not text.strip():
            continue

        # Repeated words (but exclude intentional repetitions in dharani mantras)
        words = text.split()
        for j in range(len(words) - 1):
            word1 = words[j].strip('.,!?;:"\'')
            word2 = words[j+1].strip('.,!?;:"\'')

            if word1.lower() == word2.lower() and len(word1) > 2:
                # Skip if it looks like a mantra (all caps repetition)
                if not (word1.isupper() and word2.isupper()):
                    # Skip intentional emphatic repetitions
                    if word1.lower() not in ['stop', 'yes', 'excellent', 'listen', 'look']:
                        issues['repeated_words'].append({
                            'line': i,
                            'word': word1,
                            'context': text[:100]
                        })

        # Missing apostrophes
        for pattern, correct in contractions.items():
            if re.search(pattern, text, re.IGNORECASE):
                # Skip if the correct form is already there
                if correct not in text.lower():
                    issues['missing_apostrophes'].append({
                        'line': i,
                        'found': re.search(pattern, text, re.IGNORECASE).group(0),
                        'should_be': correct,
                        'context': text[:100]
                    })

    return issues

def generate_detailed_report(the_patterns, to_patterns, punct_issues, spacing_issues, typo_issues):
    """Generate user-focused report."""
    lines = []

    lines.append("=" * 100)
    lines.append("COMPREHENSIVE PROOFREADING REPORT")
    lines.append("The Lotus Sutra: A Blues Interpretation - DETAILED ANALYSIS")
    lines.append("=" * 100)
    lines.append("")

    # PRIORITY 1: CAPITALIZATION
    lines.append("\n" + "=" * 100)
    lines.append("PRIORITY 1: CAPITALIZATION INCONSISTENCIES")
    lines.append("=" * 100)

    # The/the analysis
    lines.append("\n" + "-" * 100)
    lines.append("'THE' CAPITALIZATION PATTERNS")
    lines.append("-" * 100)

    if the_patterns['sentence_start_lowercase']:
        lines.append(f"\n⚠ FOUND: Lowercase 'the' after sentence-ending punctuation ({len(the_patterns['sentence_start_lowercase'])} occurrences)")
        lines.append("These should likely be capitalized as 'The':")
        for idx, item in enumerate(the_patterns['sentence_start_lowercase'][:20], 1):
            lines.append(f"  Line {item['line']}: ...{item['context']}...")
    else:
        lines.append("\n✓ No lowercase 'the' after sentence-ending punctuation found")

    if the_patterns['line_start_lowercase']:
        lines.append(f"\n⚠ FOUND: Lines starting with lowercase 'the' ({len(the_patterns['line_start_lowercase'])} occurrences)")
        lines.append("These may need capitalization review:")
        for idx, item in enumerate(the_patterns['line_start_lowercase'][:20], 1):
            lines.append(f"  Line {item['line']}: {item['text']}")
    else:
        lines.append("\n✓ No lines starting with lowercase 'the' found")

    # To/to analysis
    lines.append("\n" + "-" * 100)
    lines.append("'TO' CAPITALIZATION PATTERNS")
    lines.append("-" * 100)

    if to_patterns['sentence_start_lowercase']:
        lines.append(f"\n⚠ FOUND: Lowercase 'to' after sentence-ending punctuation ({len(to_patterns['sentence_start_lowercase'])} occurrences)")
        lines.append("These should likely be capitalized as 'To':")
        for idx, item in enumerate(to_patterns['sentence_start_lowercase'][:20], 1):
            lines.append(f"  Line {item['line']}: ...{item['context']}...")
    else:
        lines.append("\n✓ No lowercase 'to' after sentence-ending punctuation found")

    if to_patterns['line_start_lowercase']:
        lines.append(f"\n⚠ FOUND: Lines starting with lowercase 'to' ({len(to_patterns['line_start_lowercase'])} occurrences)")
        lines.append("These may need capitalization review:")
        for idx, item in enumerate(to_patterns['line_start_lowercase'][:20], 1):
            lines.append(f"  Line {item['line']}: {item['text']}")
        if len(to_patterns['line_start_lowercase']) > 20:
            lines.append(f"  ... and {len(to_patterns['line_start_lowercase']) - 20} more")
    else:
        lines.append("\n✓ No lines starting with lowercase 'to' found")

    # PRIORITY 2: PUNCTUATION
    lines.append("\n\n" + "=" * 100)
    lines.append("PRIORITY 2: PUNCTUATION & GRAMMAR")
    lines.append("=" * 100)

    if punct_issues['extra_space_before']:
        lines.append(f"\n⚠ FOUND: Extra space before punctuation ({len(punct_issues['extra_space_before'])} occurrences)")
        for idx, item in enumerate(punct_issues['extra_space_before'][:15], 1):
            lines.append(f"  Line {item['line']}: ...{item['context']}...")
    else:
        lines.append("\n✓ No extra spaces before punctuation found")

    if punct_issues['missing_space_after']:
        lines.append(f"\n⚠ FOUND: Missing space after punctuation ({len(punct_issues['missing_space_after'])} occurrences)")
        for idx, item in enumerate(punct_issues['missing_space_after'][:15], 1):
            lines.append(f"  Line {item['line']}: ...{item['context']}...")
    else:
        lines.append("\n✓ No missing spaces after punctuation found")

    # Dash consistency
    double_dash_count = len(punct_issues.get('double_dash_lines', []))
    em_dash_count = len(punct_issues.get('em_dash_lines', []))

    if double_dash_count > 0 and em_dash_count > 0:
        lines.append(f"\n⚠ DASH INCONSISTENCY DETECTED:")
        lines.append(f"  Lines with '--' (double dash): {double_dash_count}")
        lines.append(f"  Lines with '—' (em dash): {em_dash_count}")
        lines.append("  RECOMMENDATION: Choose one style and apply consistently throughout")

    # PRIORITY 3: SPACING
    lines.append("\n\n" + "=" * 100)
    lines.append("PRIORITY 3: SPACING ISSUES")
    lines.append("=" * 100)

    if spacing_issues['double_space']:
        lines.append(f"\n⚠ FOUND: Double spaces ({len(spacing_issues['double_space'])} occurrences)")
        for idx, item in enumerate(spacing_issues['double_space'][:15], 1):
            lines.append(f"  Line {item['line']} ({item['count']} instance(s)): {item['text']}")
    else:
        lines.append("\n✓ No double spacing issues found")

    # PRIORITY 4: TYPOS
    lines.append("\n\n" + "=" * 100)
    lines.append("PRIORITY 4: COMMON TYPOS & SPELLING")
    lines.append("=" * 100)

    if typo_issues['repeated_words']:
        lines.append(f"\n⚠ FOUND: Repeated words ({len(typo_issues['repeated_words'])} occurrences)")
        lines.append("NOTE: Mantras and intentional repetitions are expected. Review these:")
        for idx, item in enumerate(typo_issues['repeated_words'][:15], 1):
            lines.append(f"  Line {item['line']} - '{item['word']}': {item['context']}")
    else:
        lines.append("\n✓ No repeated words found (excluding mantras)")

    if typo_issues['missing_apostrophes']:
        lines.append(f"\n⚠ FOUND: Possible missing apostrophes in contractions ({len(typo_issues['missing_apostrophes'])} occurrences)")
        for idx, item in enumerate(typo_issues['missing_apostrophes'][:15], 1):
            lines.append(f"  Line {item['line']}: '{item['found']}' → should be '{item['should_be']}'")
    else:
        lines.append("\n✓ No missing apostrophes detected")

    # SUMMARY
    lines.append("\n\n" + "=" * 100)
    lines.append("SUMMARY OF ISSUES FOUND")
    lines.append("=" * 100)

    total = 0
    summary_items = [
        (len(the_patterns['sentence_start_lowercase']), "Lowercase 'the' after sentence punctuation"),
        (len(the_patterns['line_start_lowercase']), "Lines starting with lowercase 'the'"),
        (len(to_patterns['sentence_start_lowercase']), "Lowercase 'to' after sentence punctuation"),
        (len(to_patterns['line_start_lowercase']), "Lines starting with lowercase 'to'"),
        (len(punct_issues.get('extra_space_before', [])), "Extra space before punctuation"),
        (len(punct_issues.get('missing_space_after', [])), "Missing space after punctuation"),
        (len(spacing_issues.get('double_space', [])), "Double spacing"),
        (len(typo_issues.get('repeated_words', [])), "Repeated words (non-mantra)"),
        (len(typo_issues.get('missing_apostrophes', [])), "Missing apostrophes"),
    ]

    for count, description in summary_items:
        if count > 0:
            lines.append(f"  {count:4d} - {description}")
            total += count

    lines.append(f"\n  TOTAL ISSUES REQUIRING REVIEW: {total}")

    if double_dash_count > 0 and em_dash_count > 0:
        lines.append(f"\n  NOTE: Dash style inconsistency detected (-- vs —)")

    lines.append("\n" + "=" * 100)

    return "\n".join(lines)

def main():
    input_file = '/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/temp_converted.txt'
    output_file = '/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/DETAILED_PROOFREAD_REPORT.txt'

    print("Loading document...")
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    print(f"Analyzing {len(lines)} lines...")

    print("  - Analyzing capitalization patterns...")
    the_patterns, to_patterns = analyze_capitalization_detailed(lines)

    print("  - Analyzing punctuation...")
    punct_issues = analyze_punctuation_detailed(lines)

    print("  - Analyzing spacing...")
    spacing_issues = analyze_spacing(lines)

    print("  - Analyzing typos...")
    typo_issues = analyze_typos(lines)

    print("Generating detailed report...")
    report = generate_detailed_report(the_patterns, to_patterns, punct_issues, spacing_issues, typo_issues)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\nDetailed report saved to:")
    print(f"  {output_file}")

    # Print quick summary
    total = (len(the_patterns['sentence_start_lowercase']) +
             len(the_patterns['line_start_lowercase']) +
             len(to_patterns['sentence_start_lowercase']) +
             len(to_patterns['line_start_lowercase']) +
             len(punct_issues.get('extra_space_before', [])) +
             len(punct_issues.get('missing_space_after', [])) +
             len(spacing_issues.get('double_space', [])) +
             len(typo_issues.get('repeated_words', [])) +
             len(typo_issues.get('missing_apostrophes', [])))

    print(f"\nQUICK SUMMARY:")
    print(f"  Capitalization issues (the/The, to/To): {len(the_patterns['sentence_start_lowercase']) + len(the_patterns['line_start_lowercase']) + len(to_patterns['sentence_start_lowercase']) + len(to_patterns['line_start_lowercase'])}")
    print(f"  Punctuation issues: {len(punct_issues.get('extra_space_before', [])) + len(punct_issues.get('missing_space_after', []))}")
    print(f"  Spacing issues: {len(spacing_issues.get('double_space', []))}")
    print(f"  Typo issues: {len(typo_issues.get('repeated_words', [])) + len(typo_issues.get('missing_apostrophes', []))}")
    print(f"  TOTAL: {total} issues requiring review")

if __name__ == '__main__':
    main()
