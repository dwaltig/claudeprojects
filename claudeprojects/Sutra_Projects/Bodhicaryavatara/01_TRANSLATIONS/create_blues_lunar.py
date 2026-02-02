import re
import os
import glob
import subprocess

SOURCE_DIR = "/Users/williamaltig/claudeprojects/Sutra_Projects/Bodhicaryavatara/01_TRANSLATIONS/Blues"
OUTPUT_MD = "/Users/williamaltig/claudeprojects/Sutra_Projects/Bodhicaryavatara/01_TRANSLATIONS/Bodhicaryavatara_LUNAR_PATH_BLUES_ELEVENREADER.md"
OUTPUT_DOCX = "/Users/williamaltig/claudeprojects/Sutra_Projects/Bodhicaryavatara/01_TRANSLATIONS/Bodhicaryavatara_LUNAR_PATH_BLUES_ELEVENREADER.docx"

# Mapping: Day -> (ChapterNum, [List of Headers to Include])
# Note: "All" means take the whole chapter body.
# For partials, we extract text belonging to those headers.
MAPPING = {
    1: (1, ["Opening: A Humble Man's Prayer", "The Moment You Got", "The Jewel That Transforms", "Two Ways to Wake Up", "Greater Than You Know", "The Tragedy of Running the Wrong Way", "The Great Feast", "Going Home"]),
    2: (2, ["Bringing Everything I Got", "I Give Myself", "Washing Their Feet", "Following in Their Steps"]),
    3: (2, ["I Go for Refuge", "My Confession", "Death Is Coming", "Going Back to the Refuge", "The Final Words"]),
    4: (3, "All"), 
    5: (4, ["You Made a Promise", "The Weight of What You Carry", "Today Is All You Got"]),
    6: (4, ["The Fire That's Coming", "Know Your Enemy", "Time to Fight", "The Final Vow"]),
    7: (5, ["It's All About the Mind", "The Sandal Wisdom", "Mindfulness and Clear Seeing"]),
    8: (5, ["Like a Log", "The Good Mind", "What's the Body Anyway?"]),
    9: (5, ["How to Live Every Day", "Study the Teachings", "The Definition"]),
    10: (6, ["Anger Burns It All Down", "Starve the Beast"]),
    11: (6, ["The Logic of Letting Go", "Nobody's Really in Charge", "They Can't Help Themselves"]),
    12: (6, ["I Brought This On Myself", "What Can Words Really Do?", "Rejoice in Others' Good Fortune"]),
    13: (6, ["Fame Isn't Worth Anything", "The Treasure of an Enemy", "Beings Are Equal to Buddhas", "My Vow"]),
    14: (7, ["No Effort, No Merit", "The Sleep Before the Slaughterhouse", "Don't Give Up on Yourself"]),
    15: (7, ["The Four Powers", "What Comes Around", "The Three Kinds of Pride", "Love Your Work"]),
    16: (8, ["Why You Need to Get Away", "The Joy of Getting Away"]),
    17: (8, ["The Problem with People", "The Forest Hermit's Delight"]),
    18: (8, ["The Body Is Not Your Friend"]),
    19: (8, ["You and Me Are the Same"]),
    20: (8, ["The Supreme Secret"]),
    21: (8, ["Taming the Beast"]),
    22: (9, ["Everything Before Was for This"]),
    23: (9, ["You're Not What You Think"]),
    24: (9, ["The Body Is Empty", "Nothing Has True Existence"]),
    25: (9, ["Against the Makers and Causes"]),
    26: (9, ["The Compassionate Question"]),
    27: (10, "All")
}

TITLES = {
    1: "Ignition", 2: "The Burden", 3: "Refuge", 4: "The Vow", 5: "Care", 6: "Vigilance",
    7: "Mindfulness", 8: "Discipline", 9: "Conduct", 10: "Anger", 11: "Suffering",
    12: "Compassion", 13: "Benefit", 14: "Laziness", 15: "Power", 16: "Stillness",
    17: "Attachment", 18: "The Body", 19: "Equality", 20: "Exchange", 21: "Mastery",
    22: "Two Truths", 23: "Emptiness", 24: "Selflessness", 25: "Critique", 26: "Presence",
    27: "Giving Back"
}

# ... (imports remain)

# ... (SOURCE_DIR, OUTPUT_MD, OUTPUT_DOCX, MAPPING, TITLES remain same)

# Helper to find last day for each chapter
LAST_DAY_FOR_CHAP = {}
for d, (c, _) in MAPPING.items():
    if c not in LAST_DAY_FOR_CHAP:
        LAST_DAY_FOR_CHAP[c] = d
    else:
        if d > LAST_DAY_FOR_CHAP[c]:
            LAST_DAY_FOR_CHAP[c] = d

def clean_sup_for_display(text):
    # Keep superscripts for the note text itself?
    # Or replace unicode superscript with [1] style?
    # User might prefer keeping original formatting for the notes.
    return text.strip()

def clean_blues_text(text):
    """
    Cleans Blues text for audio:
    - Removes superscript notes (¹)
    - Removes formatting bold/italic
    - Removes headers (#) so they don't get read
    """
    # Remove superscripts
    text = re.sub(r'[¹²³⁴⁵⁶⁷⁸⁹⁰]', '', text)
    # Remove markers
    text = text.replace("**", "").replace("*", "")
    # Remove headers lines
    text = re.sub(r'(?m)^#+.*$', '', text)
    # Remove separator lines
    text = re.sub(r'(?m)^---+$', '', text)
    # Remove blockquotes
    text = text.replace(">", "")
    return text.strip()

def parse_blues_chapter(file_path):
    """
    Returns (sections_dict, endnotes_list, theological_notes_list)
    endnotes_list: list of strings (lines starting with superscript)
    theological_notes_list: list of strings (bullet points or text in notes section)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    sections = {}
    numbered_notes = {} # Key: superscript sequence, Value: Full text
    general_notes = []
    
    # 1. Split Content from Notes
    # Try finding the "Endnotes" or "Theological Notes" header
    # We'll look for the last occurrence of such headers to be safe? 
    # Usually at the bottom.
    
    main_body = content
    notes_block = ""
    
    # Check for splitters
    splitters = ["## Endnotes", "# Endnotes", "## Theological Notes", "# Theological Notes", "## Scholarly Apparatus"]
    for s in splitters:
        if s in content:
            parts = content.split(s)
            main_body = parts[0]
            if len(parts) > 1:
                notes_block = parts[1] # Take the part after the header
            # Stop after first split? Or the one that appears last in file?
            # Assuming one notes section at end.
            break
            
    # Parse Main Body Sections
    # First, find all headers
    header_matches = list(re.finditer(r'(?m)^## (.*)$', main_body))
    
    for i, match in enumerate(header_matches):
        title = match.group(1).strip()
        start = match.end()
        end = header_matches[i+1].start() if i < len(header_matches)-1 else len(main_body)
        
        section_text = main_body[start:end].strip()
        # Clean up separators if any left (like ---) is handled in clean_blues_text but we store raw here
        # Actually we store RAW here to find superscripts later, clean on demand
        sections[title] = section_text
        
    sections["All"] = main_body
    
    # Parse Notes Block
    # Look for lines starting with superscripts
    if notes_block:
        lines = notes_block.split('\n')
        for line in lines:
            line = line.strip()
            if not line: continue
            
            # Check for numbered note
            # Regex: starts with one or more superscripts
            m = re.match(r'^([¹²³⁴⁵⁶⁷⁸⁹⁰]+)\s*(.*)', line)
            if m:
                key = m.group(1)
                val = m.group(0) # Store full line
                numbered_notes[key] = val
            elif line.startswith("-") or line.startswith("*"):
                # Filter out unwanted metadata lines
                if any(line.startswith(prefix) for prefix in [
                    "**Blues interpretation completed**",
                    "**Interpreter**",
                    "**Verses**",
                    "**Source**",
                    "**Soul-check verification**"
                ]):
                    pass
                else:
                    general_notes.append(line)
            else:
                # Other text in notes (intro/outro?)
                pass

    return sections, numbered_notes, general_notes

def main():
    # 1. Parse all chapters
    chapter_data = {}
    files = sorted(glob.glob(os.path.join(SOURCE_DIR, "Chapter_*_Blues.md")))
    
    for fpath in files:
        fname = os.path.basename(fpath)
        try:
            num = int(fname.split("_")[1])
            chapter_data[num] = parse_blues_chapter(fpath)
            print(f"Parsed Ch {num}")
        except:
            pass

    # 2. Build Doc
    doc_content = []
    doc_content.append("# The Blues Lunar Path\n")
    doc_content.append("## Bodhicaryāvatāra: A 28-Day Practice\n\n")

    doc_content.append("### Introduction: Walking with the Moon\n")
    doc_content.append("This practice is designed to align your heart with the rhythm of the sky. The 28-day schedule follows the lunar cycle, turning the reading of Śāntideva's masterpiece into a living, breathing ritual.\n\n")
    doc_content.append("**How to Align Your Schedule:**\n")
    doc_content.append("- **Day 1 (Ignition):** Begin on the first day after the New Moon. As the sliver of light returns, you ignite the *bodhicitta*—the mind of awakening.\n")
    doc_content.append("- **Day 15 (Power):** Around the Full Moon, you encounter the perfection of Heroic Effort. The moon is full, and your energy is at its peak.\n")
    doc_content.append("- **Day 28 (The Silence):** On the day of the dark moon (New Moon), you stop. There is no reading today. You rest in the silence and let the month's practice settle into your bones.\n\n")
    doc_content.append("---\n")
    
    # Buffer for endnotes to append at the end
    all_days_notes = []

    for day in range(1, 28):
        title = TITLES[day]
        chap_num, headers = MAPPING[day]
        
        header_text = f"## Day {day}: {title}"
        doc_content.append(header_text + "\n")
        
        if chap_num not in chapter_data:
            doc_content.append("[Chapter Content Not Found]\n\n---\n")
            continue
            
        sections_map, numbered_map, general_list = chapter_data[chap_num]
        
        day_text_chunks = []
        raw_text_for_notes = ""
        
        if headers == "All":
            raw_chunk = sections_map.get("All", "")
            day_text_chunks.append(clean_blues_text(raw_chunk))
            raw_text_for_notes += raw_chunk
        else:
            for h in headers:
                # Logic to find header (exact or fuzzy)
                # Reusing previous logic slightly improved
                found_text = ""
                if h in sections_map:
                    found_text = sections_map[h]
                else:
                     # try fuzzy
                     for k in sections_map.keys():
                         if h in k or k in h:
                             found_text = sections_map[k]
                             break
                if found_text:
                    day_text_chunks.append(clean_blues_text(found_text))
                    raw_text_for_notes += found_text
                else:
                    print(f"WARNING: Header '{h}' not found in Ch {chap_num}")

        doc_content.append("\n\n".join(day_text_chunks) + "\n")
        doc_content.append("\n---\n")
        
        # Collect Notes for this Day
        day_notes = []
        
        # 1. Numbered notes present in text
        # Find all superscripts in raw text
        found_keys = re.findall(r'[¹²³⁴⁵⁶⁷⁸⁹⁰]+', raw_text_for_notes)
        # Deduplicate while preserving order? Or just set?
        # Order of appearance is better.
        seen_keys = set()
        ordered_keys = []
        for k in found_keys:
            if k not in seen_keys:
                seen_keys.add(k)
                ordered_keys.append(k)
        
        for k in ordered_keys:
            if k in numbered_map:
                day_notes.append(numbered_map[k])
                
        # 2. General notes (if last day for chapter)
        if day == LAST_DAY_FOR_CHAP.get(chap_num):
            if general_list:
                if day_notes: day_notes.append("\n*Theological/General Notes:*")
                day_notes.extend(general_list)
        
        if day_notes:
            all_days_notes.append((day, day_notes))

    # Day 28
    doc_content.append("## Day 28: The Silence\n")
    doc_content.append("Rest in the echo. No reading today.\n")
    doc_content.append("\n---\n")

    # Append Endnotes
    doc_content.append("# Endnotes for Extended Reading\n")
    for day, notes in all_days_notes:
        doc_content.append(f"### Day {day} Notes\n")
        for n in notes:
            doc_content.append(n + "\n")
        doc_content.append("\n")

    full_text = "\n".join(doc_content)
    
    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write(full_text)
        
    subprocess.run(["pandoc", OUTPUT_MD, "-o", OUTPUT_DOCX])
    print(f"Created {OUTPUT_DOCX}")

if __name__ == "__main__":
    main()
