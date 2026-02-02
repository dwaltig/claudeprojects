#!/usr/bin/env python3
"""
Comprehensive formatting audit for Chapter 7: The Phantom City
Compares against established standards from Chapters 1-6
"""

from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import sys

# ESTABLISHED STANDARDS (from Chapters 1-6)
STANDARDS = {
    'font': 'Garamond',
    'normal_size': 152400,  # ~12pt in twips
    'heading1_size': 177800,  # ~14pt in twips
    'heading2_size': 165100,  # ~13pt in twips
    'interpretation_space_after': 127000,  # twips for blank line before INTERPRETATION NOTES
}

def twips_to_pt(twips):
    """Convert twips to points"""
    if twips is None:
        return None
    return twips / 1440.0

def analyze_paragraph(para, index):
    """Analyze a single paragraph for formatting details"""
    result = {
        'index': index,
        'text': para.text[:80] + ('...' if len(para.text) > 80 else ''),
        'style': para.style.name if para.style else 'None',
        'alignment': para.alignment,
        'font_name': None,
        'font_size': None,
        'bold': False,
        'italic': False,
        'space_after': para.paragraph_format.space_after,
        'issues': []
    }

    # Check run-level formatting
    if para.runs:
        # Get formatting from first run (typically indicative)
        first_run = para.runs[0]
        result['font_name'] = first_run.font.name
        result['font_size'] = first_run.font.size
        result['bold'] = first_run.font.bold
        result['italic'] = first_run.font.italic

        # Check if formatting is consistent across runs
        for run in para.runs[1:]:
            if run.font.name != result['font_name']:
                result['issues'].append(f"Inconsistent font: {run.font.name}")
            if run.font.size != result['font_size']:
                result['issues'].append(f"Inconsistent size: {run.font.size}")

    return result

def audit_document(doc_path):
    """Perform comprehensive formatting audit"""
    doc = Document(doc_path)

    print("=" * 80)
    print("COMPREHENSIVE FORMATTING AUDIT: CHAPTER 7 - THE PHANTOM CITY")
    print("=" * 80)
    print()

    # Collect all paragraph data
    para_data = []
    for i, para in enumerate(doc.paragraphs):
        para_data.append(analyze_paragraph(para, i))

    # SECTION 1: DOCUMENT STRUCTURE VERIFICATION
    print("1. DOCUMENT STRUCTURE VERIFICATION")
    print("-" * 80)

    # Expected structure
    if len(para_data) > 0:
        print(f"Para 0 (Title): {para_data[0]['text']}")
        print(f"  Style: {para_data[0]['style']}")
        print(f"  Alignment: {para_data[0]['alignment']}")
        print(f"  Expected: Heading 1, CENTER")
        if para_data[0]['style'] != 'Heading 1':
            print(f"  ❌ ISSUE: Style is '{para_data[0]['style']}', should be 'Heading 1'")
        if para_data[0]['alignment'] != WD_ALIGN_PARAGRAPH.CENTER:
            print(f"  ❌ ISSUE: Alignment is {para_data[0]['alignment']}, should be CENTER")
        print()

    if len(para_data) > 1:
        print(f"Para 1 (Byline): {para_data[1]['text']}")
        print(f"  Style: {para_data[1]['style']}")
        print(f"  Alignment: {para_data[1]['alignment']}")
        print(f"  Italic: {para_data[1]['italic']}")
        print(f"  Expected: Normal, CENTER, ITALIC")
        if para_data[1]['style'] != 'Normal':
            print(f"  ❌ ISSUE: Style is '{para_data[1]['style']}', should be 'Normal'")
        if para_data[1]['alignment'] != WD_ALIGN_PARAGRAPH.CENTER:
            print(f"  ❌ ISSUE: Alignment is {para_data[1]['alignment']}, should be CENTER")
        if not para_data[1]['italic']:
            print(f"  ❌ ISSUE: Should be italic")
        print()

    # Find END OF CHAPTER marker
    end_marker = None
    for i, p in enumerate(para_data):
        if 'END OF CHAPTER' in p['text']:
            end_marker = i
            print(f"Para {i} (END OF CHAPTER): {p['text']}")
            print(f"  Style: {p['style']}")
            print(f"  Expected: Normal")
            if p['style'] != 'Normal':
                print(f"  ❌ ISSUE: Style is '{p['style']}', should be 'Normal'")
            break
    print()

    # Find INTERPRETATION NOTES
    interp_notes_idx = None
    blank_before_interp = None
    for i, p in enumerate(para_data):
        if p['text'] == 'INTERPRETATION NOTES':
            interp_notes_idx = i
            print(f"Para {i} (INTERPRETATION NOTES header): {p['text']}")
            print(f"  Style: {p['style']}")
            print(f"  Expected: Heading 2")
            if p['style'] != 'Heading 2':
                print(f"  ❌ ISSUE: Style is '{p['style']}', should be 'Heading 2'")

            # Check blank line before it
            if i > 0 and para_data[i-1]['text'].strip() == '':
                blank_before_interp = i - 1
                print(f"  Blank line before INTERPRETATION NOTES: Para {blank_before_interp}")
                print(f"    space_after: {para_data[blank_before_interp]['space_after']}")
                print(f"    Expected: 127000 twips")
                if para_data[blank_before_interp]['space_after'] != 127000:
                    print(f"    ❌ ISSUE: space_after is {para_data[blank_before_interp]['space_after']}, should be 127000")
            break
    print()

    # SECTION 2: FONT CONSISTENCY CHECK
    print("\n2. FONT CONSISTENCY CHECK")
    print("-" * 80)

    non_garamond = []
    for p in para_data:
        if p['font_name'] and p['font_name'] != STANDARDS['font'] and p['text'].strip():
            non_garamond.append((p['index'], p['text'], p['font_name']))

    if non_garamond:
        print(f"❌ FOUND {len(non_garamond)} paragraphs with non-Garamond fonts:")
        for idx, text, font in non_garamond[:10]:  # Show first 10
            print(f"  Para {idx}: '{text[:50]}...' - Font: {font}")
        if len(non_garamond) > 10:
            print(f"  ... and {len(non_garamond) - 10} more")
    else:
        print("✓ All paragraphs use Garamond font")
    print()

    # SECTION 3: HEADING STYLE VERIFICATION
    print("\n3. HEADING STYLE VERIFICATION")
    print("-" * 80)

    heading1_paras = [p for p in para_data if p['style'] == 'Heading 1']
    heading2_paras = [p for p in para_data if p['style'] == 'Heading 2']

    print(f"Heading 1 paragraphs: {len(heading1_paras)}")
    for p in heading1_paras:
        print(f"  Para {p['index']}: {p['text']}")
        size_str = f"{p['font_size']} ({twips_to_pt(p['font_size']):.1f}pt)" if p['font_size'] else "None"
        print(f"    Font: {p['font_name']}, Size: {size_str}")
        print(f"    Alignment: {p['alignment']}")
        expected_str = f"{STANDARDS['heading1_size']} ({twips_to_pt(STANDARDS['heading1_size']):.1f}pt)"
        print(f"    Expected size: {expected_str}")
        if p['font_size'] and p['font_size'] != STANDARDS['heading1_size']:
            print(f"    ❌ ISSUE: Size mismatch")
        if p['alignment'] != WD_ALIGN_PARAGRAPH.CENTER:
            print(f"    ❌ ISSUE: Should be CENTER aligned")
    print()

    print(f"Heading 2 paragraphs: {len(heading2_paras)}")
    for p in heading2_paras[:5]:  # Show first 5
        print(f"  Para {p['index']}: {p['text']}")
        size_str = f"{p['font_size']} ({twips_to_pt(p['font_size']):.1f}pt)" if p['font_size'] else "None"
        print(f"    Font: {p['font_name']}, Size: {size_str}")
        print(f"    Alignment: {p['alignment']}")
        expected_str = f"{STANDARDS['heading2_size']} ({twips_to_pt(STANDARDS['heading2_size']):.1f}pt)"
        print(f"    Expected size: {expected_str}")
        if p['font_size'] and p['font_size'] != STANDARDS['heading2_size']:
            print(f"    ❌ ISSUE: Size mismatch")
        if p['alignment'] not in [WD_ALIGN_PARAGRAPH.LEFT, None]:
            print(f"    ❌ ISSUE: Should be LEFT aligned")
    if len(heading2_paras) > 5:
        print(f"  ... and {len(heading2_paras) - 5} more Heading 2 paragraphs")
    print()

    # SECTION 4: ALIGNMENT VERIFICATION
    print("\n4. ALIGNMENT VERIFICATION")
    print("-" * 80)

    centered_paras = [p for p in para_data if p['alignment'] == WD_ALIGN_PARAGRAPH.CENTER and p['text'].strip()]
    print(f"CENTER aligned paragraphs: {len(centered_paras)}")
    print("Expected: Title (H1), Byline, *** separators")

    non_separator_centered = []
    for p in centered_paras:
        if p['style'] not in ['Heading 1'] and p['text'].strip() != '***' and 'Translated by' not in p['text']:
            non_separator_centered.append(p)

    if non_separator_centered:
        print(f"❌ Found {len(non_separator_centered)} unexpected CENTER aligned paragraphs:")
        for p in non_separator_centered[:5]:
            print(f"  Para {p['index']}: {p['text']}")
    else:
        print("✓ CENTER alignment used appropriately")
    print()

    # Count *** separators
    separators = [p for p in para_data if p['text'].strip() == '***']
    print(f"*** separators found: {len(separators)}")
    print("Positions:", [p['index'] for p in separators])
    for sep in separators:
        if sep['alignment'] != WD_ALIGN_PARAGRAPH.CENTER:
            print(f"  ❌ Para {sep['index']}: Separator not CENTER aligned")
    print()

    # SECTION 5: SPACING VERIFICATION
    print("\n5. SPACING VERIFICATION")
    print("-" * 80)

    paras_with_spacing = [p for p in para_data if p['space_after'] and p['space_after'] > 0]
    print(f"Paragraphs with explicit space_after: {len(paras_with_spacing)}")

    # Check the critical blank line before INTERPRETATION NOTES
    if blank_before_interp is not None:
        p = para_data[blank_before_interp]
        print(f"\nCRITICAL: Blank line before INTERPRETATION NOTES (Para {blank_before_interp}):")
        print(f"  space_after: {p['space_after']}")
        print(f"  Expected: {STANDARDS['interpretation_space_after']}")
        if p['space_after'] == STANDARDS['interpretation_space_after']:
            print("  ✓ CORRECT")
        else:
            print(f"  ❌ ISSUE: Should be {STANDARDS['interpretation_space_after']}")
    else:
        print("❌ Could not find blank line before INTERPRETATION NOTES")
    print()

    # SECTION 6: INTERPRETATION NOTES FORMAT CHECK
    print("\n6. INTERPRETATION NOTES FORMAT CHECK")
    print("-" * 80)

    if interp_notes_idx:
        print(f"Interpretation notes start at Para {interp_notes_idx}")

        # Check for bold text in interpretation notes
        bold_in_notes = []
        markdown_in_notes = []

        for i in range(interp_notes_idx + 1, len(para_data)):
            p = para_data[i]
            if p['bold']:
                bold_in_notes.append(i)
            if '**' in p['text'] or '##' in p['text']:
                markdown_in_notes.append((i, p['text']))

        if bold_in_notes:
            print(f"❌ Found {len(bold_in_notes)} paragraphs with bold text in interpretation notes:")
            for idx in bold_in_notes[:5]:
                print(f"  Para {idx}: {para_data[idx]['text'][:60]}...")
        else:
            print("✓ No bold text in interpretation notes")

        if markdown_in_notes:
            print(f"❌ Found {len(markdown_in_notes)} paragraphs with markdown in interpretation notes:")
            for idx, text in markdown_in_notes[:5]:
                print(f"  Para {idx}: {text[:60]}...")
        else:
            print("✓ No markdown formatting in interpretation notes")
    print()

    # SECTION 7: FONT SIZE VERIFICATION
    print("\n7. FONT SIZE VERIFICATION")
    print("-" * 80)

    size_issues = []
    for p in para_data:
        if not p['text'].strip():
            continue

        expected_size = None
        if p['style'] == 'Heading 1':
            expected_size = STANDARDS['heading1_size']
        elif p['style'] == 'Heading 2':
            expected_size = STANDARDS['heading2_size']
        elif p['style'] == 'Normal':
            expected_size = STANDARDS['normal_size']

        if expected_size and p['font_size'] and p['font_size'] != expected_size:
            size_issues.append((p['index'], p['text'][:60], p['style'], p['font_size'], expected_size))

    if size_issues:
        print(f"❌ Found {len(size_issues)} paragraphs with incorrect font sizes:")
        for idx, text, style, actual, expected in size_issues[:10]:
            actual_str = f"{actual} ({twips_to_pt(actual):.1f}pt)" if actual else "None"
            expected_str = f"{expected} ({twips_to_pt(expected):.1f}pt)" if expected else "None"
            print(f"  Para {idx} ({style}): {text}...")
            print(f"    Actual: {actual_str}, Expected: {expected_str}")
    else:
        print("✓ All font sizes correct for their styles")
    print()

    # SECTION 8: OVERALL SUMMARY
    print("\n" + "=" * 80)
    print("8. OVERALL ASSESSMENT")
    print("=" * 80)

    total_issues = 0
    issue_categories = []

    if non_garamond:
        total_issues += len(non_garamond)
        issue_categories.append(f"Font inconsistencies: {len(non_garamond)}")

    if size_issues:
        total_issues += len(size_issues)
        issue_categories.append(f"Font size issues: {len(size_issues)}")

    if non_separator_centered:
        total_issues += len(non_separator_centered)
        issue_categories.append(f"Alignment issues: {len(non_separator_centered)}")

    if bold_in_notes:
        total_issues += len(bold_in_notes)
        issue_categories.append(f"Bold text in interpretation notes: {len(bold_in_notes)}")

    if markdown_in_notes:
        total_issues += len(markdown_in_notes)
        issue_categories.append(f"Markdown in interpretation notes: {len(markdown_in_notes)}")

    # Check blank line spacing
    if blank_before_interp is not None:
        if para_data[blank_before_interp]['space_after'] != STANDARDS['interpretation_space_after']:
            total_issues += 1
            issue_categories.append("Incorrect spacing before INTERPRETATION NOTES")

    print(f"\nTotal issues found: {total_issues}")
    if issue_categories:
        print("\nIssue breakdown:")
        for cat in issue_categories:
            print(f"  - {cat}")

    print("\n" + "-" * 80)
    if total_issues == 0:
        print("PUBLICATION READINESS: A (Perfect - matches Chapters 1-6 standards)")
    elif total_issues <= 5:
        print("PUBLICATION READINESS: A- (Excellent - minor fixes needed)")
    elif total_issues <= 15:
        print("PUBLICATION READINESS: B+ (Very good - some fixes needed)")
    elif total_issues <= 30:
        print("PUBLICATION READINESS: B (Good - multiple fixes needed)")
    elif total_issues <= 50:
        print("PUBLICATION READINESS: B- (Acceptable - significant fixes needed)")
    else:
        print("PUBLICATION READINESS: C (Needs substantial revision)")
    print("-" * 80)

if __name__ == '__main__':
    doc_path = '/Users/williamaltig/claudeprojects/Lotus_Sutra/Chapters_DOCX/Chapter_07_The_Phantom_City.docx'
    audit_document(doc_path)
