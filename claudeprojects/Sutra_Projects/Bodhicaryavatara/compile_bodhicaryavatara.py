import os
import glob

# Constants
BASE_DIR = "/Users/williamaltig/claudeprojects/Sutra_Projects/Bodhicaryavatara/01_TRANSLATIONS"
SCHOLARLY_DIR = os.path.join(BASE_DIR, "Scholarly")
BLUES_DIR = os.path.join(BASE_DIR, "Blues")
OUTPUT_SCHOLARLY = os.path.join(BASE_DIR, "Bodhicaryavatara_Scholarly_Complete.md")
OUTPUT_BLUES = os.path.join(BASE_DIR, "Bodhicaryavatara_Blues_Complete.md")
OUTPUT_DUAL = os.path.join(BASE_DIR, "Bodhicaryavatara_Dual_Edition_Complete.md")

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    print("Starting Bodhicaryāvatāra Compilation...")

    # Get sorted lists of files
    scholarly_files = sorted(glob.glob(os.path.join(SCHOLARLY_DIR, "Chapter_*.md")))
    blues_files = sorted(glob.glob(os.path.join(BLUES_DIR, "Chapter_*.md")))

    if len(scholarly_files) != 10 or len(blues_files) != 10:
        print(f"Error: Expected 10 files each. Found {len(scholarly_files)} Scholarly and {len(blues_files)} Blues.")
        return

    scholarly_content = ["# Bodhicaryāvatāra: The Way of the Bodhisattva\n\n## Scholarly Edition\n\nTranslated by Dr. Rajesh Patel\n\n---"]
    blues_content = ["# Bodhicaryāvatāra: The Way of the Bodhisattva\n\n## Blues Vernacular Edition\n\nTranslated by William Altig\n\n---"]
    dual_content = ["# Bodhicaryāvatāra: The Way of the Bodhisattva\n\n## Dual Scholarly & Blues Edition\n\n---"]

    for i in range(10):
        s_path = scholarly_files[i]
        b_path = blues_files[i]
        
        print(f"Processing Chapter {i+1}...")
        
        s_text = read_file(s_path)
        b_text = read_file(b_path)

        # Append to individual editions
        scholarly_content.append(s_text)
        blues_content.append(b_text)

        # Append to dual edition
        dual_content.append(f"# PART {i+1}: SCHOLARLY TRANSLATION\n\n{s_text}")
        dual_content.append(f"# PART {i+1}: BLUES INTERPRETATION\n\n{b_text}")
        dual_content.append("\n---\n")

    # Write Output Files
    print(f"Writing {OUTPUT_SCHOLARLY}...")
    with open(OUTPUT_SCHOLARLY, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(scholarly_content))

    print(f"Writing {OUTPUT_BLUES}...")
    with open(OUTPUT_BLUES, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(blues_content))

    print(f"Writing {OUTPUT_DUAL}...")
    with open(OUTPUT_DUAL, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(dual_content))

    print("Compilation Complete! ✅")

if __name__ == "__main__":
    main()
