import os
import re
import subprocess

SOURCE_FILE = "/Users/williamaltig/claudeprojects/Dhammapada/DHAMMAPADA_REBORN_TTS_28_CHAPTERS.md"
DEST_FILE = "/Users/williamaltig/claudeprojects/Dhammapada/Dhammapada_SOLAR_PATH_BLUES_ELEVENREADER_v2.md"
DEST_DOCX = "/Users/williamaltig/claudeprojects/Dhammapada/Dhammapada_SOLAR_PATH_BLUES_ELEVENREADER_v2.docx"

INTRODUCTION = """# The Solar Earth Path
## The Dhammapada: A 28-Day Practice

### Introduction: Walking the Earth
If the **Lotus Sutra** is the Sun (Morning) and the **Bodhicaryāvatāra** is the Moon (Night), the **Dhammapada** is the **Earth**—the solid ground you walk on at Midday.

This 28-day schedule aligns with the solar calendar (Gregorian). Read **Day 1** on the 1st of the month, **Day 2** on the 2nd, and so on.

*   **Time:** Midday (Noon)
*   **Focus:** Ethics, Action, Integrity
*   **Goal:** To keep your feet on the ground while your head is in the stars.

---

"""

def process_file():
    if not os.path.exists(SOURCE_FILE):
        print(f"Error: Source file not found at {SOURCE_FILE}")
        return

    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output_lines = []
    output_lines.append(INTRODUCTION)
    
    print(f"Total lines in source: {len(lines)}")
    
    chapter_pattern = re.compile(r"# Chapter (\d+): (.+)")
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        match = chapter_pattern.match(stripped) 
        if match:
            day_num = match.group(1)
            title = match.group(2)
            # Ensure extra spacing before Day headers
            output_lines.append(f"\n\n# Day {day_num}: {title}\n")
        elif "## End of Chapter" in line:
            # Ensure spacing before End of Day
            output_lines.append("\n" + line.replace("Chapter", "Day").replace("##", "###"))
        elif stripped.startswith("## Verse"):
            output_lines.append(line.replace("##", "###"))
        elif stripped == "---":
            continue
        elif "27 chapters" in line:
             output_lines.append(line.replace("27 chapters", "28 chapters"))
        else:
            output_lines.append(line)

    with open(DEST_FILE, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)
    
    print(f"Successfully created {DEST_FILE}")
    
    # Convert to DOCX using Pandoc
    try:
        # Disable YAML metadata block parsing to avoid errors with '---' separators
        subprocess.run(["pandoc", DEST_FILE, "-f", "markdown-yaml_metadata_block", "-o", DEST_DOCX], check=True)
        print(f"Successfully created {DEST_DOCX}")
    except FileNotFoundError:
        print("Error: Pandoc not found. Please install pandoc to generate DOCX.")
    except subprocess.CalledProcessError as e:
        print(f"Error running pandoc: {e}")

if __name__ == "__main__":
    process_file()
