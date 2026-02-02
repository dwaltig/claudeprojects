
import os

base_dir = "/Users/williamaltig/claudeprojects/Sutra_Projects/Immeasurable_Meanings_Sutra/blues_edition"
chapters = [
    "TOC_LIONS_ROAR.md",
    "INTRODUCTION_THE_ALCHEMISTS_BLUES.md",
    "PREFACE_LIU_QIU_BLUES.md",
    "CHAPTER_01_VIRTUOUS_CONDUCT_BLUES.md",
    "CHAPTER_02_PREACHING_DHARMA_BLUES.md",
    "CHAPTER_03_TEN_MERITS_BLUES.md",
    "GLOSSARY_THE_STONE_AND_THE_GOLD.md",
    "APPENDIX_MECHANICS_OF_THE_ROAR.md",
    "INDEX_LIONS_ROAR.md"
]
outfile = "/Users/williamaltig/claudeprojects/Sutra_Projects/Immeasurable_Meanings_Sutra/blues_edition/THE_IMMEASURABLE_MEANINGS_SUTRA_LIONS_ROAR_COMPLETE.md"

def consolidate():
    with open(outfile, 'w') as out:
        out.write("# THE IMMEASURABLE MEANINGS SUTRA\n")
        out.write("## (THE LION'S ROAR EDITION)\n\n")
        out.write("**Translated and Adapted by Master John Kim (The Bluesman)**\n")
        out.write("**Based on the 'Alchemist's Blues' Methodology**\n\n")
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
