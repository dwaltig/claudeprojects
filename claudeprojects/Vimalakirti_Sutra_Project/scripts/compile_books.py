import os
import re

# Base directory
BASE_DIR = "/Users/williamaltig/claudeprojects/Vimalakirti_Sutra_Project"
TRANS_DIR = os.path.join(BASE_DIR, "01_TRANSLATIONS")
COMPILED_DIR = os.path.join(BASE_DIR, "05_COMPILED")

# Ensure output directory exists
os.makedirs(COMPILED_DIR, exist_ok=True)

# Files definitions
VOLUMES = {
    "Scholarly": {
        "intro": os.path.join(BASE_DIR, "INTRO_SCHOLARLY.md"),
        "pattern": r"Chapter_(\d+)_.*_Scholarly\.md",
        "output": os.path.join(COMPILED_DIR, "Vimalakirti_Sutra_Scholarly_Complete.md"),
        "title": "The Vimalakīrti Nirdeśa Sūtra (Scholarly Edition)"
    },
    "Blues": {
        "intro": os.path.join(BASE_DIR, "INTRO_BLUES.md"),
        "pattern": r"Chapter_(\d+)_.*_Blues\.md",
        "output": os.path.join(COMPILED_DIR, "Vimalakirti_Sutra_Blues_Complete.md"),
        "title": "The Vimalakīrti Sūtra: A Blues Interpretation"
    }
}

def clean_content(content):
    """Remove YAML frontmatter or redundant main headers if necessary."""
    # This is a basic cleaner. We might want to strip the first H1 if we create a new one.
    # For now, let's just ensure we have spacing.
    return content.strip() + "\n\n---\n\n"

def compile_volume(vol_type, config):
    print(f"Compiling {vol_type} Volume...")
    
    # 1. Start with Title Page
    full_text = f"# {config['title']}\n\n"
    
    # 2. Add Introduction
    if os.path.exists(config["intro"]):
        with open(config["intro"], "r") as f:
            full_text += f.read() + "\n\n---\n\n"
            
    # 3. Add Table of Contents (Placeholder logic - ideally we'd generate this dynamically)
    full_text += "## Table of Contents\n\n"
    # We will generate TOC after reading chapters to get titles
    
    chapters_content = ""
    toc_lines = []
    
    # 4. Get Chapters
    files = [f for f in os.listdir(TRANS_DIR) if re.match(config["pattern"], f)]
    # Sort by chapter number extracted from filename
    files.sort(key=lambda x: int(re.match(config["pattern"], x).group(1)))
    
    for filename in files:
        filepath = os.path.join(TRANS_DIR, filename)
        match = re.match(config["pattern"], filename)
        chap_num = int(match.group(1))
        
        with open(filepath, "r") as f:
            content = f.read()
            
        # Extract title line for TOC
        title_line = content.split('\n')[0].replace('# ', '').strip()
        toc_lines.append(f"- [Chapter {chap_num}: {title_line}](#chapter-{chap_num})")
        
        # Add anchor to content if not present (simple hack)
        # Actually, let's just append content. Markdown TOC generators usually handle headers.
        chapters_content += clean_content(content)
        
    full_text += "\n".join(toc_lines) + "\n\n---\n\n"
    full_text += chapters_content
    
    # Write output
    with open(config["output"], "w") as f:
        f.write(full_text)
        
    print(f"Created {config['output']} ({len(files)} chapters)")

def main():
    for vol_type, config in VOLUMES.items():
        compile_volume(vol_type, config)

if __name__ == "__main__":
    main()
