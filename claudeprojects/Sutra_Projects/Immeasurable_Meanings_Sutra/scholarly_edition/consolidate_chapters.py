
import os

base_dir = "/Users/williamaltig/claudeprojects/Sutra_Projects/Immeasurable_Meanings_Sutra/scholarly_edition"
chapters = ["CHAPTER_01_VIRTUOUS_CONDUCT_SCHOLARLY.md", "CHAPTER_02_PREACHING_DHARMA_SCHOLARLY.md", "CHAPTER_03_TEN_MERITS_SCHOLARLY.md"]
outfile = "/Users/williamaltig/claudeprojects/Sutra_Projects/Immeasurable_Meanings_Sutra/scholarly_edition/IMMEASURABLE_MEANINGS_COMPLETE_SCHOLARLY.md"

def consolidate():
    with open(outfile, 'w') as out:
        out.write("# THE IMMEASURABLE MEANINGS SUTRA\n\n")
        out.write("**Scholarly Edition**\n")
        out.write("**Translated by The Professor (Dr. Rajesh Patel)**\n\n")
        out.write("---\n\n")
        
        for chapter in chapters:
            path = os.path.join(base_dir, chapter)
            if os.path.exists(path):
                print(f"Adding {chapter}...")
                with open(path, 'r') as f:
                    content = f.read()
                    out.write(content)
                    out.write("\n\n---\n\n")
            else:
                print(f"MISSING: {chapter}")

    print(f"Consolidation complete: {outfile}")

if __name__ == "__main__":
    consolidate()
