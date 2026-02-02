import os
import re

# Base Directory
BASE_DIR = "/Users/williamaltig/claudeprojects/Sutra_Projects/Shikshasamucchaya"
TRANS_DIR = os.path.join(BASE_DIR, "01_TRANSLATIONS")
OUTPUT_DIR = os.path.join(BASE_DIR, "01_TRANSLATIONS")

# Chapter Mapping
# Tuple: (Chapter Number, Title, Scholarly File(s), Blues File(s))
CHAPTERS = [
    (1, "The Perfection of Generosity", 
     ["Chapter_01_Danapramita_Scholarly_Part1.md", "Chapter_01_Danapramita_Scholarly_Part2.md", "Chapter_01_Danapramita_Scholarly_Part3.md", "Chapter_01_Danapramita_Scholarly_Part4.md"], 
     ["Chapter_01_Danapramita_Blues_Complete.md"]),
    (2, "Accepting the True Dharma", ["Chapter_02_Saddharmaparigraha_Scholarly.md"], ["Chapter_02_Saddharmaparigraha_Blues.md"]),
    (3, "Protection of the Preacher", ["Chapter_03_Dharmabhanakadiraksa_Scholarly.md"], ["Chapter_03_Dharmabhanakadiraksa_Blues.md"]),
    (4, "Avoiding Harm", ["Chapter_04_Anarthavarjana_Scholarly.md"], ["Chapter_04_Anarthavarjana_Blues.md"]),
    (5, "Perfection of Discipline", ["Chapter_05_Silaparamita_Anarthavarjana_Scholarly.md"], ["Chapter_05_Silaparamita_Anarthavarjana_Blues.md"]),
    (6, "Protecting the Body", ["Chapter_06_Atmabhavaraksa_Scholarly.md"], ["Chapter_06_Atmabhavaraksa_Blues.md"]),
    (7, "Protecting Merit & Enjoyment", ["Chapter_07_Bhogapunyaraksa_Scholarly.md"], ["Chapter_07_Bhogapunyaraksa_Blues.md"]),
    (8, "Purification of Evil", ["Chapter_08_Papasodhana_Scholarly.md"], ["Chapter_08_Papasodhana_Blues.md"]),
    (9, "Perfection of Patience", ["Chapter_09_Ksantiparamita_Scholarly.md"], ["Chapter_09_Ksantiparamita_Blues.md"]),
    (10, "Perfection of Effort", ["Chapter_10_Viryaparamita_Scholarly.md"], ["Chapter_10_Viryaparamita_Blues.md"]),
    (11, "Praise of the Forest", ["Chapter_11_Aranyasamshraya_Scholarly.md"], ["Chapter_11_Aranyasamshraya_Blues.md"]),
    (12, "Preparation of the Mind", ["Chapter_12_Cittaparikarma_Scholarly.md"], ["Chapter_12_Cittaparikarma_Blues.md"]),
    (13, "Foundations of Mindfulness", ["Chapter_13_Smrtyupasthana_Scholarly.md"], ["Chapter_13_Smrtyupasthana_Blues.md"]),
    (14, "Purification of the Body", ["Chapter_14_Atmabhavaparisuddhi_Scholarly.md"], ["Chapter_14_Atmabhavaparisuddhi_Blues.md"]),
    (15, "Purification of Merit", ["Chapter_15_Bhogapunyasuddhi_Scholarly.md"], ["Chapter_15_Bhogapunyasuddhi_Blues.md"]),
    (16, "Protocol of Good Conduct", ["Chapter_16_Bhadracaryavidhi_Scholarly.md"], ["Chapter_16_Bhadracaryavidhi_Blues.md"]),
    (17, "Benefits of Worship", ["Chapter_17_Vandananusamsa_Scholarly.md"], ["Chapter_17_Vandananusamsa_Blues.md"]),
    (18, "Recollection of the Three Jewels", ["Chapter_18_Ratnatrayanusmrti_Scholarly.md"], ["Chapter_18_Ratnatrayanusmrti_Blues.md"]),
    (19, "Increase of Merit", ["Chapter_19_Punyavrddhi_Scholarly.md"], ["Chapter_19_Punyavrddhi_Blues.md"]),
]

def read_and_clean(filepath, is_continuation=False):
    """Reads a file and optionally strips header metadata if it's a continuation part."""
    full_path = os.path.join(TRANS_DIR, filepath)
    if not os.path.exists(full_path):
        return f"\n\n[MISSING FILE: {filepath}]\n\n"
    
    with open(full_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    cleaned_lines = []
    header_found = False
    
    for line in lines:
        # Strip H1/H2 metadata only if it's a continuation part (Part 2, 3 etc of a chapter)
        # also strip author attributions
        if "Translation by" in line or "Translated by" in line:
            continue

        if is_continuation:
            if line.startswith("# Chapter") or line.startswith("## Śikṣāsamuccaya"):
                continue
            if line.strip() == "---":
                continue # Skip the first separator too often
        cleaned_lines.append(line)
        
    return "".join(cleaned_lines)

def compile_book(edition_type):
    """Compiles the book based on edition type ('Scholarly' or 'Blues')."""
    is_scholarly = edition_type == "Scholarly"
    title = "Śikṣāsamuccaya: The Compendium of Training" if is_scholarly else "The Bluesman's Guide to the Galaxy (Śikṣāsamuccaya Remix)"
    subtitle = "A Scholarly Translation" if is_scholarly else "A Blues Vernacular Interpretation"
    
    content = []
    
    # Title Page
    content.append(f"# {title}\n")
    content.append(f"## {subtitle}\n")
    content.append("\n---\n\n")
    
    # Table of Contents
    content.append("## Table of Contents\n\n")
    for ch_num, ch_title, _, _ in CHAPTERS:
        anchor = f"chapter-{ch_num}-{ch_title.lower().replace(' ', '-')}"
        # Simplified toc link, actual linking depends on renderer but this looks nice
        content.append(f"- [Chapter {ch_num}: {ch_title}](#chapter-{ch_num})\n")
    content.append("\n---\n\n")
    
    # Chapters
    for ch_num, ch_title, sch_files, blue_files in CHAPTERS:
        files = sch_files if is_scholarly else blue_files
        
        # Add Chapter Header Anchor (manually inserting an HTML anchor for navigation if needed, 
        # but markdown headers usually auto-anchor. We'll simply ensure the H1 is clean).
        # Actually, the files already have headers. We just need to make sure they are distinct.
        
        # We might want to inject a page break or separator
        content.append(f"\n\n<div id='chapter-{ch_num}'></div>\n\n") 
        
        for i, filename in enumerate(files):
            # Only the first file of a multi-part chapter is the 'Main' start. 
            # Subsequent files (Part 2, 3) are continuations.
            is_continuation = (i > 0) 
            chunk = read_and_clean(filename, is_continuation)
            content.append(chunk)
            content.append("\n\n") # Spacing between parts
            
        content.append("\n\n---\n\n") # Spacing between chapters

    output_filename = f"Shikshasamucchaya_{edition_type}_Edition.md"
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("".join(content))
        
    return output_path

if __name__ == "__main__":
    print("Compiling Scholarly Edition...")
    path1 = compile_book("Scholarly")
    print(f"Created: {path1}")
    
    print("Compiling Blues Edition...")
    path2 = compile_book("Blues")
    print(f"Created: {path2}")
