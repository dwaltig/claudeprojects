#!/usr/bin/env python3
"""Extract chapters with footnotes - handles actual markdown structure."""

import re
import json
from pathlib import Path

def extract_all_footnotes(content):
    """Extract all footnote definitions from file.

    Handles two formats:
    1. Markdown format: [^1]: text
    2. Apparatus Summary format: 1. **term** (...): explanation
    """
    footnotes = {}

    # First, try to extract from Apparatus Summary section
    # Matches:
    # - "## Apparatus Summary" (Chapters 1-10)
    # - "## SCHOLARLY APPARATUS" (Chapters 11-16)
    # - "### Apparatus Summary" (Chapters 17-28)
    apparatus_match = re.search(r'#{2,3}\s+(?:Apparatus Summary|SCHOLARLY APPARATUS)\s*\n(.*?)(?=\n---|\n#{1,3}|$)', content, re.DOTALL)
    if apparatus_match:
        apparatus_text = apparatus_match.group(1)
        # Split by blank-line-separated blocks to avoid lookahead confusion
        # Each item is: N. **term** (...): explanation
        # We'll split on blank lines, then parse each block

        # Match both formats:
        # 1. Regular numbers: "1. **term**: explanation"  (Chapters 1-10)
        # 2. Unicode superscripts: "¹: explanation" or "¹: **term**: explanation"  (Chapters 11+)

        # Split on lines and parse sequentially
        lines = apparatus_text.split('\n')

        current_num = None
        current_explanation = None

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Try format 1: regular number with bold term (Chapters 1-10)
            # e.g., "1. **term**: explanation"
            item_match = re.match(r'^(\d+)\.\s+\*\*(.+?)\*\*\s*(.*)', line)
            if item_match:
                # Save previous footnote if exists
                if current_num is not None and current_explanation:
                    current_explanation = current_explanation.strip()
                    current_explanation = re.sub(r'\n\s*', ' ', current_explanation)
                    footnotes[current_num] = current_explanation

                num = item_match.group(1)
                term = item_match.group(2)
                rest = item_match.group(3)

                if rest.startswith('('):
                    paren_match = re.match(r'^(.+?)\s*:\s*(.*)', rest)
                    explanation = paren_match.group(2) if paren_match else rest
                else:
                    explanation = rest.lstrip(': ')

                current_num = num
                current_explanation = explanation
                continue

            # Try format 2: Unicode superscript (Chapters 11+)
            # e.g., "¹: explanation" (Chapters 11-14) or "¹ **term**: explanation" (Chapters 17-28)
            # Superscripts: ⁰¹²³⁴⁵⁶⁷⁸⁹ (U+2070-U+2079)
            # First try with optional bold term: "¹ **term**: explanation"
            superscript_match = re.match(r'^([⁰¹²³⁴⁵⁶⁷⁸⁹]+)\s+(?:\*\*[^*]+\*\*)?\s*:\s*(.*)', line)
            if not superscript_match:
                # Fall back to format without bold term: "¹: explanation"
                superscript_match = re.match(r'^([⁰¹²³⁴⁵⁶⁷⁸⁹]+):\s*(.*)', line)
            if superscript_match:
                # Save previous footnote if exists
                if current_num is not None and current_explanation:
                    current_explanation = current_explanation.strip()
                    current_explanation = re.sub(r'\n\s*', ' ', current_explanation)
                    footnotes[current_num] = current_explanation

                # Convert superscript to regular digit
                superscript_num = superscript_match.group(1)
                superscript_map = {
                    '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4',
                    '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9'
                }
                num = ''.join(superscript_map.get(c, c) for c in superscript_num)
                explanation = superscript_match.group(2)

                current_num = num
                current_explanation = explanation
                continue

            # This is a continuation line of the previous footnote
            if current_num is not None:
                current_explanation += ' ' + line

        # Save the last footnote
        if current_num is not None and current_explanation:
            current_explanation = current_explanation.strip()
            current_explanation = re.sub(r'\n\s*', ' ', current_explanation)
            footnotes[current_num] = current_explanation

    # Also check for markdown format footnotes as fallback
    lines = content.split('\n')
    for i, line in enumerate(lines):
        match = re.match(r'\[\^(\d+)\]:\s*(.*)', line)
        if match:
            num = match.group(1)
            text = match.group(2).strip()

            # Collect continuation lines (continue until next [^ or end)
            j = i + 1
            while j < len(lines):
                next_line = lines[j]
                if next_line.startswith('[^'):
                    break
                if next_line.strip():
                    text += ' ' + next_line.strip()
                j += 1

            text = text.replace('\n', ' ').strip()
            footnotes[num] = text

    return footnotes

def extract_chapter_with_footnotes(filepath):
    """Extract chapter with footnotes."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract all footnotes from entire file
    footnotes = extract_all_footnotes(content)

    # Extract main content: everything from first ### until Apparatus Summary
    main_start = content.find('\n### ')
    if main_start == -1:
        main_start = 0

    # Find where Apparatus Summary starts (this marks end of prose)
    # Check for "## Apparatus Summary", "## SCHOLARLY APPARATUS", and "### Apparatus Summary"
    apparatus_start = content.find('\n## Apparatus Summary')
    if apparatus_start == -1:
        apparatus_start = content.find('\n## SCHOLARLY APPARATUS')
    if apparatus_start == -1:
        apparatus_start = content.find('\n### Apparatus Summary')
    if apparatus_start == -1:
        # No Apparatus Summary, check for markdown footnotes
        footnote_start = content.find('\n[^1]:')
        if footnote_start == -1:
            # No footnotes either, take everything after heading
            main_content = content[main_start:]
        else:
            main_content = content[main_start:footnote_start]
    else:
        # Take everything from main_start to Apparatus Summary
        main_content = content[main_start:apparatus_start]

    # Convert markdown to HTML with footnote tooltips
    html = markdown_to_html_with_footnotes(main_content, footnotes)

    return html, footnotes

def markdown_to_html_with_footnotes(text, footnotes):
    """Convert markdown to HTML with interactive footnote references.

    Handles both markdown format [^N] and Unicode superscript format (¹²³ etc).
    """

    # Mapping of Unicode superscript characters to numbers
    # Includes both basic superscripts and Latin Extended superscripts
    superscript_map = {
        # Basic Latin Superscripts
        '\u00b9': '1', '\u00b2': '2', '\u00b3': '3',
        # Latin Extended Superscripts (U+2070-U+2079)
        '\u2070': '0', '\u00b9': '1', '\u00b2': '2', '\u00b3': '3',
        '\u2074': '4', '\u2075': '5', '\u2076': '6', '\u2077': '7',
        '\u2078': '8', '\u2079': '9'
    }

    # Convert ### headers to h4 (keep them for accordion structure)
    text = re.sub(r'^### (.+)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)

    # Convert **bold** to <strong>
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)

    # Convert *italic* to <em>
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)

    # Convert > blockquotes
    text = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', text, flags=re.MULTILINE)

    # Convert Unicode superscripts to interactive footnote spans
    # Build a regex pattern that matches any Unicode superscript character
    superscript_pattern = '[' + ''.join(superscript_map.keys()) + ']+'

    def replace_unicode_superscript(match):
        # Convert Unicode superscript(s) to number string
        unicode_super = match.group(0)
        num = ''.join(superscript_map.get(c, c) for c in unicode_super)

        if num in footnotes:
            # Escape for HTML attributes
            note_text = footnotes[num].replace('"', '&quot;').replace("'", "&#39;")
            # Use data attributes to pass tooltip text
            return f'<span class="footnote-ref" data-note="{num}" data-text="{note_text}" onclick="showFootnoteTooltip(event)" onmouseover="showFootnoteTooltip(event)"><sup>{num}</sup></span>'
        else:
            return f'<sup>{num}</sup>'

    text = re.sub(superscript_pattern, replace_unicode_superscript, text)

    # Also convert markdown format footnote references [^N] to interactive spans
    def replace_markdown_footnote(match):
        num = match.group(1)
        if num in footnotes:
            # Escape for HTML attributes
            note_text = footnotes[num].replace('"', '&quot;').replace("'", "&#39;")
            # Use data attributes to pass tooltip text
            return f'<span class="footnote-ref" data-note="{num}" data-text="{note_text}" onclick="showFootnoteTooltip(event)" onmouseover="showFootnoteTooltip(event)"><sup>{num}</sup></span>'
        else:
            return f'<sup>{num}</sup>'

    text = re.sub(r'\[\^(\d+)\]', replace_markdown_footnote, text)

    # Split paragraphs and wrap in <p>
    paragraphs = text.split('\n\n')
    html_parts = []
    for p in paragraphs:
        p = p.strip()
        if p:
            if p.startswith('<'):
                html_parts.append(p)
            else:
                # Wrap in paragraph
                html_parts.append(f'<p>{p}</p>')

    return '\n'.join(html_parts)

def get_chapter_titles():
    """Chapter titles."""
    return {
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

def main():
    base_path = Path('/Users/williamaltig/claudeprojects/Lotus_Sutra/03_SCHOLARLY_TRANSLATION_2025')
    chapters_data = {}
    titles = get_chapter_titles()

    print("Extracting chapters with working footnotes...")

    for ch_num in range(1, 29):
        filename = f'CHAPTER_{ch_num:02d}_*.md'
        matching_files = list(base_path.glob(filename))

        if not matching_files:
            continue

        filepath = matching_files[0]
        print(f"  Ch {ch_num:2d}: ", end="", flush=True)

        try:
            prose_html, footnotes = extract_chapter_with_footnotes(filepath)

            # Build full chapter content
            content = f'<div class="chapter-title">Chapter {ch_num}: {titles[ch_num]}</div>'
            content += prose_html

            chapters_data[str(ch_num)] = {
                'title': f'Chapter {ch_num}: {titles[ch_num]}',
                'prose_html': prose_html,
                'footnotes': footnotes,
                'full_html': content
            }

            print(f"✓ ({len(footnotes)} footnotes)")

        except Exception as e:
            print(f"Error: {e}")

    # Save as JavaScript
    js = "const CHAPTERS_DATA = "
    js += json.dumps(chapters_data, ensure_ascii=False, separators=(',', ':'))
    js += ";"

    output_path = base_path / 'chapters_data.js'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(js)

    print(f"\n✓ Generated chapters_data.js")
    print(f"  Size: {len(js) / 1024:.1f} KB")

if __name__ == '__main__':
    main()
