#!/usr/bin/env python3
"""Extract chapters with footnotes preserved."""

import re
import json
from pathlib import Path

def extract_chapter_with_footnotes(filepath):
    """Extract chapter content and footnotes."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract footnote definitions [^1]: text
    footnotes = {}
    footnote_pattern = r'\[\^(\d+)\]:\s*(.*?)(?=\n\[\^|\n## |\Z)'
    for match in re.finditer(footnote_pattern, content, re.DOTALL):
        num = match.group(1)
        text = match.group(2).strip()
        # Clean up the text
        text = text.replace('\n', ' ').strip()
        footnotes[num] = text

    # Extract prose section
    prose_content = []
    in_prose = False

    for line in content.split('\n'):
        if line.startswith('## Prose Section'):
            in_prose = True
            continue
        elif line.startswith('## Verse Section') or line.startswith('## Philosophical'):
            break

        if in_prose:
            prose_content.append(line)

    prose_text = '\n'.join(prose_content).strip()

    # Remove footnote definitions but keep references
    prose_text = re.sub(r'\[\^(\d+)\]:\s*.*', '', prose_text)

    # Extract verse section
    verse_lines = []
    in_verse = False

    for line in content.split('\n'):
        if line.startswith('## Verse Section'):
            in_verse = True
            continue
        elif line.startswith('## Philosophical') or line.startswith('## Apparatus'):
            break
        if in_verse:
            verse_lines.append(line)

    verse_text = '\n'.join(verse_lines).strip()

    # Convert to HTML with footnote tooltips
    prose_html = markdown_to_html_with_footnotes(prose_text, footnotes)
    verses = extract_verses(verse_text)

    return prose_html, verses, footnotes

def markdown_to_html_with_footnotes(text, footnotes):
    """Convert markdown to HTML, preserving footnote references as interactive elements."""

    # Convert **bold** to <strong>
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)

    # Convert *italic* to <em>
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)

    # Convert ### headers to h4
    text = re.sub(r'^### (.+)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)

    # Convert > quotes to blockquote
    text = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', text, flags=re.MULTILINE)

    # Convert footnote references [^1] to superscript numbers
    # If footnote definitions exist, make them interactive
    def replace_footnote(match):
        num = match.group(1)
        if num in footnotes:
            footnote_text = footnotes[num].replace('"', '&quot;')
            return f'<span class="footnote-ref" data-footnote="{num}" title="{footnote_text}" onclick="showFootnoteTooltip(event)"><sup>{num}</sup></span>'
        else:
            # No definition available, just show the superscript number
            return f'<sup class="footnote-num">{num}</sup>'

    text = re.sub(r'\[\^(\d+)\]', replace_footnote, text)

    # Split paragraphs and wrap in <p>
    paragraphs = text.split('\n\n')
    html_paragraphs = []
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('<'):
            html_paragraphs.append(f'<p>{p}</p>')
        elif p:
            html_paragraphs.append(p)

    return '\n'.join(html_paragraphs)

def extract_verses(text):
    """Extract verses from verse section."""
    verses = []
    blocks = text.split('\n\n')

    for block in blocks:
        block = block.strip()
        if block and len(block) > 20:
            # Clean up markdown
            block = re.sub(r'\[\^[\d]+\]', '', block)
            block = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', block)
            block = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', block)
            verses.append(block)

    return verses[:10]

def get_chapter_titles():
    """Get chapter titles."""
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

    print("Extracting chapters with footnotes...")

    for ch_num in range(1, 29):
        filename = f'CHAPTER_{ch_num:02d}_*.md'
        matching_files = list(base_path.glob(filename))

        if not matching_files:
            continue

        filepath = matching_files[0]
        print(f"  Ch {ch_num:2d}: ", end="", flush=True)

        try:
            prose_html, verses, footnotes = extract_chapter_with_footnotes(filepath)

            # Wrap in proper structure
            content = f'<div class="chapter-title">Chapter {ch_num}: {titles[ch_num]}</div>'
            content += f'<div class="chapter-prose">{prose_html}</div>'

            if verses:
                content += '<div class="chapter-verses">'
                for v in verses:
                    content += f'<div class="verse-block">{v}</div>'
                content += '</div>'

            chapters_data[str(ch_num)] = {
                'title': f'Chapter {ch_num}: {titles[ch_num]}',
                'prose_html': prose_html,
                'verses': verses,
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

    print(f"\n✓ Generated chapters_data.js ({len(chapters_data)} chapters)")
    print(f"  Size: {len(js) / 1024:.1f} KB")

if __name__ == '__main__':
    main()
