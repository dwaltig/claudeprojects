import re
import os
import glob
import subprocess

# 1. Define the 27-Day Lunar Cycle Schedule (plus Day 28 Gap)
# Format: (Day, Title, Chapter_Num, Start_Verse, End_Verse)
SCHEDULE = [
    (1, "Ignition", 1, 1, 36),
    (2, "The Burden", 2, 1, 33),
    (3, "Refuge", 2, 34, 65),
    (4, "The Vow", 3, 1, 33),
    (5, "Care", 4, 1, 24),
    (6, "Vigilance", 4, 25, 48),
    (7, "Mindfulness", 5, 1, 36),
    (8, "Discipline", 5, 37, 72),
    (9, "Conduct", 5, 73, 109),
    (10, "Anger", 6, 1, 33),
    (11, "Suffering", 6, 34, 66),
    (12, "Compassion", 6, 67, 100),
    (13, "Benefit", 6, 101, 134),
    (14, "Laziness", 7, 1, 38),
    (15, "Power", 7, 39, 76),
    (16, "Stillness", 8, 1, 31),
    (17, "Attachment", 8, 32, 62),
    (18, "The Body", 8, 63, 93),
    (19, "Equality", 8, 94, 124),
    (20, "Exchange", 8, 125, 155),
    (21, "Mastery", 8, 156, 186),
    (22, "Two Truths", 9, 1, 33),
    (23, "Emptiness", 9, 34, 66),
    (24, "Selflessness", 9, 67, 100),
    (25, "Critique", 9, 101, 133),
    (26, "Presence", 9, 134, 167),
    (27, "Giving Back", 10, 1, 58),
]

SOURCE_DIR = "/Users/williamaltig/claudeprojects/Sutra_Projects/Bodhicaryavatara/01_TRANSLATIONS/Scholarly"
OUTPUT_MD = "/Users/williamaltig/claudeprojects/Sutra_Projects/Bodhicaryavatara/01_TRANSLATIONS/Bodhicaryavatara_LUNAR_PATH_ELEVENREADER.md"
OUTPUT_DOCX = "/Users/williamaltig/claudeprojects/Sutra_Projects/Bodhicaryavatara/01_TRANSLATIONS/Bodhicaryavatara_LUNAR_PATH_ELEVENREADER.docx"

def clean_text_for_tts(text):
    """
    Cleans text for audio reading:
    - Removes blockquotes (>)
    - Removes footnote markers [^1] or 1, 2
    - Removes Sanskrit diacritics? No, keep them but maybe simplify if needed. User wants "scholarly practice", so keep.
    - Removes Markdown headers (#, ##, ###) captured within text
    - Collapses whitespace.
    """
    # Remove blockquote markers
    text = text.replace(">", "")
    
    # Remove footnote markers like ¹, ², ³, or [1]
    # The text uses superscript chars ¹ ² ³
    text = re.sub(r'[¹²³⁴⁵⁶⁷⁸⁹⁰]', '', text)
    text = re.sub(r'\[\^?\d+\]', '', text)
    
    # Remove bolding/italics markers
    text = text.replace("**", "").replace("*", "")

    # Remove any lines that look like Headers within the verse capture
    # e.g. "## II. The Precious Human Life" or "### Verses 4-6"
    text = re.sub(r'(?m)^#+.*$', '', text)
    
    # Remove lines that are just "---"
    text = re.sub(r'(?m)^---+$', '', text)

    # Collapse multiple newlines
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    return text.strip()

def parse_chapter(file_path):
    """
    Parses a chapter file and returns a dict {verse_int: verse_text}
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    verses = {}
    
    # Split by "Verse X"
    # Pattern: **Verse (\d+)** ... (content) ... until next **Verse or ---
    
    # We'll use a regex iterator
    pattern = re.compile(r'\*\*Verse (\d+)\*\*(.*?)(?=\*\*Verse|\n---)', re.DOTALL)
    
    matches = pattern.finditer(content)
    for m in matches:
        v_num = int(m.group(1))
        v_text = m.group(2).strip()
        verses[v_num] = clean_text_for_tts(v_text)
        
    return verses

def main():
    # 1. Load all chapters
    chapter_data = {}
    files = sorted(glob.glob(os.path.join(SOURCE_DIR, "Chapter_*_Scholarly.md")))
    
    # Map file index to chapter number (assuming sorted order 01..10)
    for i, fpath in enumerate(files):
        chap_num = i + 1
        print(f"Parsing Chapter {chap_num}: {os.path.basename(fpath)}")
        chapter_data[chap_num] = parse_chapter(fpath)
        
    # 2. Build the Document
    doc_content = []
    doc_content.append("# The Lunar Path: Bodhicaryāvatāra\n")
    doc_content.append("## A 28-Day Liturgical Cycle\n\n")
    doc_content.append("This text is arranged for daily recitation over the course of one sidereal lunar month (27 days), with a final day of silence.\n\n")
    
    for day, title, chap, start, end in SCHEDULE:
        header = f"## Day {day}: {title} (Chapter {chap}, Verses {start}-{end})"
        doc_content.append(header + "\n")
        
        verses_dict = chapter_data.get(chap, {})
        
        # Iterate verses
        for v in range(start, end + 1):
            if v not in verses_dict:
                # print(f"  WARNING: Missing Verse {v} in Ch {chap}")
                text = ""
            else:
                text = verses_dict[v]
            
            if text:
                doc_content.append(f"{text}\n")
            
        doc_content.append("\n---\n") # Section break
        
    # Day 28
    doc_content.append("## Day 28: The Silence (Abhijit)\n")
    doc_content.append("Rest in the echo of the dedication. No verses are recited today.\n")
    
    full_text = "\n".join(doc_content)
    
    # 3. Write Output
    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write(full_text)
    print(f"Generated Markdown: {OUTPUT_MD}")
    
    # 4. Convert to DOCX
    try:
        subprocess.run(["pandoc", OUTPUT_MD, "-o", OUTPUT_DOCX], check=True)
        print(f"Generated DOCX: {OUTPUT_DOCX}")
    except Exception as e:
        print(f"Pandoc failed: {e}")

if __name__ == "__main__":
    main()
