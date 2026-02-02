import re

# File Path
BLUES_PATH = "/Users/williamaltig/claudeprojects/Sutra_Projects/Shikshasamucchaya/01_TRANSLATIONS/Shikshasamucchaya_Blues_Edition.md"

def polish_blues_edition():
    with open(BLUES_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Title and Subtitle
    new_title_block = """# The Long Game: A Manual for the Spiritual Hustle
## A Blues Vernacular Translation of Śāntideva's *Śikṣāsamuccaya*

---

**Translation and Interpretation by William Altig**

---

"""
    
    # Replace the existing header (rough matching)
    content = re.sub(r'# The Bluesman\'s Guide.*?\n## A Blues Vernacular Interpretation.*?\n', new_title_block, content, flags=re.DOTALL)

    # 2. Clean up redundant "Notes" or "Endnotes" separators if they clump together
    content = re.sub(r'\n---\n\n---\n', '\n---\n', content)

    # 3. Ensure consistent chapter headers. 
    # Some might be "# Chapter X:..." and some "# Chapter X..."
    # We'll leave them as is, they looked consistent in the preview.

    # 4. Remove any internal TOCs if they exist within chapters (unlikely, but good to check)
    # The preview showed a Master TOC at the start. That's good.

    # 5. Add a "Note on the Translation" (Pre-Preface)
    preface = """## Note on the Translation

This text is a creative, vernacular interpretation of the *Śikṣāsamuccaya* (Compendium of Training) by the 8th-century Indian master Śāntideva. 

While the **Scholarly Edition** provides a rigorous, academic translation with extensive philological apparatus, this **Blues Edition** aims for the *soul* of the text. It uses the language of the street, the jazz club, and the sermon to capture the urgency, the rhythm, and the radical demand of the Bodhisattva path.

The metaphors are shifted:
*   *Bodhicitta* becomes "The Waking-Up Heart."
*   *Kalyāṇamitra* becomes "Your People" or " The Crew."
*   *Śūnyatā* becomes "The Empty Room."
*   *Saṃsāra* becomes "The City of Noise."

This is not a simplification; it is an amplification. It seeks to make the ancient training manual sing again.

---

"""
    # Insert Preface after TOC
    toc_end_match = re.search(r'(- \[Chapter 19: Increase of Merit\]\(#chapter-19\)\n)', content)
    if toc_end_match:
        insert_point = toc_end_match.end()
        content = content[:insert_point] + "\n\n---\n\n" + preface + content[insert_point:]

    # 6. Final write
    with open(BLUES_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    polish_blues_edition()
