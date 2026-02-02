#!/usr/bin/env python3
"""
Comprehensive Formatting Audit for Lotus Sutra Chapters
Analyzes font consistency, heading styles, spacing, structure, and formatting issues
"""

from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

def twips_to_pt(twips):
    """Convert twips to points (1 point = 20 twips)"""
    return twips / 20 if twips else None

def pt_to_twips(pt):
    """Convert points to twips"""
    return pt * 20

def analyze_run_formatting(run):
    """Extract detailed formatting from a run"""
    info = {
        'text': run.text,
        'font_name': run.font.name,
        'font_size_twips': run.font.size.twips if run.font.size else None,
        'font_size_pt': twips_to_pt(run.font.size.twips) if run.font.size else None,
        'bold': run.font.bold,
        'italic': run.font.italic,
        'underline': run.font.underline,
    }
    return info

def analyze_paragraph(para, para_num):
    """Extract detailed formatting from a paragraph"""
    style_name = para.style.name if para.style else 'None'

    # Get alignment
    alignment = 'LEFT'
    if para.alignment == WD_ALIGN_PARAGRAPH.CENTER:
        alignment = 'CENTER'
    elif para.alignment == WD_ALIGN_PARAGRAPH.RIGHT:
        alignment = 'RIGHT'
    elif para.alignment == WD_ALIGN_PARAGRAPH.JUSTIFY:
        alignment = 'JUSTIFY'

    # Get spacing
    space_before = para.paragraph_format.space_before.twips if para.paragraph_format.space_before else None
    space_after = para.paragraph_format.space_after.twips if para.paragraph_format.space_after else None

    # Get text and run formatting
    text = para.text
    runs_info = []
    for run in para.runs:
        if run.text:  # Only include runs with text
            runs_info.append(analyze_run_formatting(run))

    # Detect if this is a blank line
    is_blank = len(text.strip()) == 0

    return {
        'para_num': para_num,
        'style': style_name,
        'alignment': alignment,
        'text': text,
        'is_blank': is_blank,
        'space_before': space_before,
        'space_after': space_after,
        'runs': runs_info,
        'run_count': len(para.runs)
    }

def audit_chapter(filepath):
    """Perform comprehensive audit of a single chapter"""
    doc = Document(filepath)
    chapter_name = os.path.basename(filepath)

    print(f"\n{'='*80}")
    print(f"CHAPTER: {chapter_name}")
    print(f"{'='*80}\n")

    # Analyze all paragraphs
    paragraphs = []
    for i, para in enumerate(doc.paragraphs, 1):
        para_info = analyze_paragraph(para, i)
        paragraphs.append(para_info)

    # SECTION 1: FONT CONSISTENCY CHECK
    print("1. FONT CONSISTENCY ANALYSIS")
    print("-" * 80)

    font_issues = []
    expected_font = "Garamond"

    for para in paragraphs:
        for run in para['runs']:
            if run['font_name'] != expected_font and run['font_name'] is not None:
                font_issues.append({
                    'para_num': para['para_num'],
                    'found_font': run['font_name'],
                    'text_preview': run['text'][:50]
                })

    if font_issues:
        print(f"ISSUES FOUND: {len(font_issues)} instances of non-Garamond font")
        for issue in font_issues[:10]:  # Show first 10
            print(f"  Para {issue['para_num']}: Font '{issue['found_font']}' in: {issue['text_preview']!r}")
        if len(font_issues) > 10:
            print(f"  ... and {len(font_issues) - 10} more issues")
    else:
        print("✓ All fonts are Garamond (or null)")

    # SECTION 2: HEADING STYLE VERIFICATION
    print("\n2. HEADING STYLE VERIFICATION")
    print("-" * 80)

    h1_expected_twips = 177800  # ~14pt
    h2_expected_twips = 165100  # ~13pt
    normal_expected_twips = 152400  # ~12pt

    heading_issues = []

    h1_paras = [p for p in paragraphs if p['style'] == 'Heading 1']
    h2_paras = [p for p in paragraphs if p['style'] == 'Heading 2']

    print(f"Heading 1 paragraphs: {len(h1_paras)}")
    for para in h1_paras:
        print(f"  Para {para['para_num']}: {para['alignment']} | {para['text'][:60]!r}")
        for run in para['runs']:
            size_twips = run['font_size_twips']
            if size_twips and size_twips != h1_expected_twips:
                heading_issues.append(f"Para {para['para_num']} H1: Expected {h1_expected_twips} twips, found {size_twips}")
        if para['alignment'] != 'CENTER':
            heading_issues.append(f"Para {para['para_num']} H1: Expected CENTER, found {para['alignment']}")

    print(f"\nHeading 2 paragraphs: {len(h2_paras)}")
    for para in h2_paras:
        print(f"  Para {para['para_num']}: {para['alignment']} | {para['text'][:60]!r}")
        for run in para['runs']:
            size_twips = run['font_size_twips']
            if size_twips and size_twips != h2_expected_twips:
                heading_issues.append(f"Para {para['para_num']} H2: Expected {h2_expected_twips} twips, found {size_twips}")

    if heading_issues:
        print("\nISSUES FOUND:")
        for issue in heading_issues:
            print(f"  {issue}")
    else:
        print("\n✓ All heading styles are correct")

    # SECTION 3: PARAGRAPH SPACING VALIDATION
    print("\n3. PARAGRAPH SPACING VALIDATION")
    print("-" * 80)

    expected_space_after = 127000
    blank_lines_before_interpretation = []

    for i, para in enumerate(paragraphs):
        if para['is_blank']:
            # Check if next paragraph contains "INTERPRETATION NOTES"
            if i + 1 < len(paragraphs):
                next_para = paragraphs[i + 1]
                if 'INTERPRETATION NOTES' in next_para['text']:
                    blank_lines_before_interpretation.append({
                        'para_num': para['para_num'],
                        'space_after': para['space_after']
                    })

    print(f"Blank lines before 'INTERPRETATION NOTES': {len(blank_lines_before_interpretation)}")
    spacing_issues = []

    for blank in blank_lines_before_interpretation:
        status = "✓" if blank['space_after'] == expected_space_after else "✗"
        print(f"  {status} Para {blank['para_num']}: space_after = {blank['space_after']} (expected {expected_space_after})")
        if blank['space_after'] != expected_space_after:
            spacing_issues.append(f"Para {blank['para_num']}: space_after should be {expected_space_after}, found {blank['space_after']}")

    if spacing_issues:
        print("\nISSUES FOUND:")
        for issue in spacing_issues:
            print(f"  {issue}")
    else:
        print("\n✓ All blank lines before INTERPRETATION NOTES have correct spacing")

    # SECTION 4: STRUCTURE CONFIRMATION
    print("\n4. STRUCTURE CONFIRMATION")
    print("-" * 80)

    structure_elements = {
        'title_h1': None,
        'byline': None,
        'blank_after_byline': None,
        'end_of_chapter': None,
        'blank_before_interpretation': None,
        'interpretation_notes': None
    }

    for i, para in enumerate(paragraphs):
        text = para['text'].strip()

        if para['style'] == 'Heading 1' and not structure_elements['title_h1']:
            structure_elements['title_h1'] = para['para_num']

        if para['style'] == 'Normal' and para['alignment'] == 'CENTER' and not structure_elements['byline']:
            # Check if italic
            has_italic = any(run['italic'] for run in para['runs'])
            if has_italic:
                structure_elements['byline'] = para['para_num']

        if 'END OF CHAPTER' in text.upper():
            structure_elements['end_of_chapter'] = para['para_num']

        if 'INTERPRETATION NOTES' in text:
            structure_elements['interpretation_notes'] = para['para_num']
            # Check for blank line before it
            if i > 0 and paragraphs[i-1]['is_blank']:
                structure_elements['blank_before_interpretation'] = paragraphs[i-1]['para_num']

    print("Expected structure elements:")
    for element, para_num in structure_elements.items():
        status = "✓" if para_num else "✗ MISSING"
        print(f"  {status} {element}: Para {para_num if para_num else 'N/A'}")

    # SECTION 5: INTERPRETATION NOTES FORMAT
    print("\n5. INTERPRETATION NOTES FORMAT VALIDATION")
    print("-" * 80)

    if structure_elements['interpretation_notes']:
        start_para = structure_elements['interpretation_notes']
        interpretation_section = paragraphs[start_para:]

        h2_headers = [p for p in interpretation_section if p['style'] == 'Heading 2']
        print(f"Heading 2 subsections in Interpretation Notes: {len(h2_headers)}")
        for h2 in h2_headers:
            print(f"  Para {h2['para_num']}: {h2['text'][:60]!r}")

        # Check for markdown or bold in body text (not in H2)
        markdown_issues = []
        for para in interpretation_section:
            if para['style'] != 'Heading 2':
                text = para['text']
                if '**' in text or '__' in text or '##' in text:
                    markdown_issues.append(f"Para {para['para_num']}: Contains markdown: {text[:50]!r}")

                # Check for bold in body text
                for run in para['runs']:
                    if run['bold'] and run['text'].strip():
                        markdown_issues.append(f"Para {para['para_num']}: Contains bold text: {run['text'][:50]!r}")

        if markdown_issues:
            print("\nISSUES FOUND:")
            for issue in markdown_issues[:20]:
                print(f"  {issue}")
            if len(markdown_issues) > 20:
                print(f"  ... and {len(markdown_issues) - 20} more issues")
        else:
            print("\n✓ No markdown or bold formatting in body text")
    else:
        print("✗ INTERPRETATION NOTES section not found")

    # SECTION 6: *** SEPARATOR COUNT AND PLACEMENT
    print("\n6. *** SEPARATOR VERIFICATION")
    print("-" * 80)

    separators = []
    for para in paragraphs:
        if para['text'].strip() == '***':
            separators.append(para['para_num'])

    print(f"Found {len(separators)} *** separators at paragraphs: {separators}")

    # SECTION 7: EXTRA BLANK LINES CHECK
    print("\n7. EXTRA BLANK LINES CHECK (BETWEEN CONTENT PARAGRAPHS)")
    print("-" * 80)

    # Find blank lines that are NOT before INTERPRETATION NOTES or END OF CHAPTER
    extra_blanks = []
    for i, para in enumerate(paragraphs):
        if para['is_blank']:
            # Check context
            if i + 1 < len(paragraphs):
                next_para = paragraphs[i + 1]
                prev_para = paragraphs[i - 1] if i > 0 else None

                # Skip if it's before INTERPRETATION NOTES
                if 'INTERPRETATION NOTES' in next_para['text']:
                    continue

                # Skip if it's after END OF CHAPTER
                if prev_para and 'END OF CHAPTER' in prev_para['text']:
                    continue

                # Skip if it's after byline
                if prev_para and prev_para['alignment'] == 'CENTER' and any(run['italic'] for run in prev_para['runs']):
                    continue

                # This might be an extra blank line
                extra_blanks.append({
                    'para_num': para['para_num'],
                    'context_before': prev_para['text'][:50] if prev_para else 'START',
                    'context_after': next_para['text'][:50]
                })

    if extra_blanks:
        print(f"POTENTIAL ISSUES: {len(extra_blanks)} extra blank lines found")
        for blank in extra_blanks[:10]:
            print(f"  Para {blank['para_num']}: Between '{blank['context_before']}' and '{blank['context_after']}'")
        if len(extra_blanks) > 10:
            print(f"  ... and {len(extra_blanks) - 10} more blank lines")
    else:
        print("✓ No unnecessary blank lines found")

    # SECTION 8: SUMMARY
    print("\n8. OVERALL ASSESSMENT")
    print("-" * 80)

    total_issues = len(font_issues) + len(heading_issues) + len(spacing_issues) + len(markdown_issues) + len(extra_blanks)
    missing_structure = sum(1 for v in structure_elements.values() if v is None)

    if total_issues == 0 and missing_structure == 0:
        print("✓ EXCELLENT: No formatting issues detected")
        print("✓ Chapter is publication-ready")
    elif total_issues < 5 and missing_structure == 0:
        print("✓ GOOD: Minor formatting issues detected")
        print(f"  {total_issues} issues found - quick fixes recommended")
    else:
        print("✗ NEEDS ATTENTION: Multiple formatting issues detected")
        print(f"  {total_issues} issues found")
        print(f"  {missing_structure} missing structure elements")
        print("  Review and correction recommended before publication")

    return {
        'chapter': chapter_name,
        'total_paragraphs': len(paragraphs),
        'font_issues': len(font_issues),
        'heading_issues': len(heading_issues),
        'spacing_issues': len(spacing_issues),
        'markdown_issues': len(markdown_issues),
        'extra_blanks': len(extra_blanks),
        'missing_structure': missing_structure,
        'total_issues': total_issues
    }

def main():
    """Run audit on all chapters"""
    base_path = "/Users/williamaltig/claudeprojects/Lotus_Sutra/Chapters_DOCX"

    chapters = [
        "Chapter_01_The_Opening.docx",
        "Chapter_02_The_Loving_Tricks.docx",
        "Chapter_04_Faith_and_Understanding.docx",
        "Chapter_05_The_Parable_of_the_Medicinal_Herbs.docx",
        "Chapter_06_The_Naming.docx"
    ]

    results = []

    for chapter in chapters:
        filepath = os.path.join(base_path, chapter)
        if os.path.exists(filepath):
            result = audit_chapter(filepath)
            results.append(result)
        else:
            print(f"\n✗ ERROR: File not found: {filepath}\n")

    # FINAL SUMMARY
    print("\n" + "="*80)
    print("COMPREHENSIVE AUDIT SUMMARY")
    print("="*80 + "\n")

    print(f"{'Chapter':<45} {'Issues':<10} {'Status':<20}")
    print("-" * 80)

    for result in results:
        status = "✓ Ready" if result['total_issues'] == 0 else f"✗ {result['total_issues']} issues"
        print(f"{result['chapter']:<45} {result['total_issues']:<10} {status:<20}")

    total_issues_all = sum(r['total_issues'] for r in results)

    print("\n" + "-" * 80)
    print(f"TOTAL ISSUES ACROSS ALL CHAPTERS: {total_issues_all}")

    if total_issues_all == 0:
        print("\n✓✓✓ ALL CHAPTERS ARE PUBLICATION-READY ✓✓✓")
    else:
        print(f"\n⚠ {total_issues_all} issues require attention before publication")

    print("\n" + "="*80)

if __name__ == "__main__":
    main()
