#!/usr/bin/env python3
"""Build a properly polished lotus.html with readable text and complete content."""

import re
import json
from pathlib import Path

def extract_prose_and_verses(filepath):
    """Extract complete prose and verse sections from markdown."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into sections
    prose_content = []
    verse_content = []

    in_prose = False
    in_verse = False
    current_section = []

    for line in content.split('\n'):
        # Skip metadata and headers up to prose
        if line.startswith('## Prose Section'):
            in_prose = True
            in_verse = False
            continue
        elif line.startswith('## Verse Section'):
            if current_section:
                prose_content.append('\n'.join(current_section))
                current_section = []
            in_prose = False
            in_verse = True
            continue
        elif line.startswith('## Philosophical Implications') or line.startswith('## Apparatus Summary'):
            if current_section:
                if in_verse:
                    verse_content.append('\n'.join(current_section))
                else:
                    prose_content.append('\n'.join(current_section))
            break

        # Skip footnote definitions
        if line.startswith('[^'):
            continue

        # Collect content
        if in_prose or in_verse:
            current_section.append(line)

    # Get remaining content
    if current_section:
        if in_verse:
            verse_content.append('\n'.join(current_section))
        else:
            prose_content.append('\n'.join(current_section))

    prose_text = '\n'.join(prose_content).strip()
    verse_text = '\n'.join(verse_content).strip()

    return prose_text, verse_text

def markdown_to_html(text):
    """Convert markdown to HTML, handle footnote refs."""
    # Remove footnote references but keep text
    text = re.sub(r'\[\^[\d]+\]', '', text)

    # Convert **bold** to <strong>
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)

    # Convert *italic* to <em>
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)

    # Convert ### headers to h4
    text = re.sub(r'^### (.+)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)

    # Convert > quotes to blockquote
    text = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', text, flags=re.MULTILINE)

    # Split paragraphs by double newline and wrap in <p>
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
    """Extract individual verses from verse section."""
    verses = []

    # Split by double newlines or verse markers
    blocks = text.split('\n\n')

    for block in blocks:
        block = block.strip()
        if block and len(block) > 20:  # Skip tiny fragments
            # Clean up markdown
            block = re.sub(r'\[\^[\d]+\]', '', block)
            block = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', block)
            block = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', block)
            verses.append(block)

    return verses[:10]  # Limit to first 10 verses

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

    print("Extracting and processing chapters...")

    for ch_num in range(1, 29):
        filename = f'CHAPTER_{ch_num:02d}_*.md'
        matching_files = list(base_path.glob(filename))

        if not matching_files:
            continue

        filepath = matching_files[0]
        print(f"  Ch {ch_num:2d}: ", end="", flush=True)

        try:
            prose, verse = extract_prose_and_verses(filepath)

            # Convert to HTML
            prose_html = markdown_to_html(prose)
            verse_list = extract_verses(verse)

            # Wrap in proper structure
            content = f'<div class="chapter-title">Chapter {ch_num}: {titles[ch_num]}</div>'
            content += f'<div class="chapter-prose">{prose_html}</div>'

            if verse_list:
                content += '<div class="chapter-verses">'
                for i, v in enumerate(verse_list):
                    content += f'<div class="verse-block">{v}</div>'
                content += '</div>'

            # Store verses separately for verses panel
            chapters_data[str(ch_num)] = {
                'title': f'Chapter {ch_num}: {titles[ch_num]}',
                'prose_html': prose_html,
                'verses': verse_list,
                'full_html': content
            }

            print("✓")

        except Exception as e:
            print(f"Error: {e}")

    # Save chapters data
    with open(base_path / 'chapters_polished.json', 'w', encoding='utf-8') as f:
        json.dump(chapters_data, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Processed {len(chapters_data)} chapters")
    print(f"✓ Saved to chapters_polished.json")

if __name__ == '__main__':
    main()
