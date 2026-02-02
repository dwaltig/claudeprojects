import os
import re

# Configuration
BASE_DIR = "/Users/williamaltig/claudeprojects/Miao-lo/Guketsu_Project/01_TRANSLATIONS"
OUTPUT_MD = "/Users/williamaltig/claudeprojects/Guketsu_Scholarly_Publication_Ready.md"

def get_fascicle_files(fascicle_num):
    """Finds and sorts files for a specific fascicle."""
    files = [f for f in os.listdir(BASE_DIR) if f.startswith(f"Fascicle_{fascicle_num:02d}") and "Scholarly" in f]
    
    sections = []
    preface = None
    opening = None
    closing = None
    
    for f in files:
        if "Preface" in f:
            preface = f
        elif "Opening" in f:
            opening = f
        elif "Closing" in f:
            closing = f
        elif "Section" in f:
            match = re.search(r"Section_?0?(\d+)", f)
            if match:
                 sec_num = int(match.group(1))
                 sections.append((sec_num, f))
        elif "Index" in f:
             pass 

    sections.sort(key=lambda x: x[0])
    
    ordered_files = []
    if preface: ordered_files.append(preface)
    if opening: ordered_files.append(opening)
    for _, f in sections: ordered_files.append(f)
    if closing: ordered_files.append(closing)
    
    return ordered_files

def read_markdown_file(filename):
    path = os.path.join(BASE_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()

def clean_header_text(text):
    """Removes 'Part N' and 'Fascicle N' artifacts from headers."""
    text = re.sub(r', Part \d+', '', text)
    text = re.sub(r'Part \d+: ', '', text)
    text = re.sub(r'^Fascicle \d+[,:]? ', '', text)
    return text.strip()

def process_markdown_compile():
    compiled_lines = []
    
    # Metadata Block for Pandoc
    compiled_lines.append(f"% The Great Calming and Contemplation: The Guketsu Commentary\n")
    compiled_lines.append(f"% Zhanran (Miao-lo)\n")
    compiled_lines.append(f"% Translated by Dr. Rajesh Patel\n\n")

    # --- Add General Introduction ---
    intro_path = "/Users/williamaltig/claudeprojects/GUKETSU_INTRODUCTION.md"
    if os.path.exists(intro_path):
        with open(intro_path, 'r', encoding='utf-8') as f:
            compiled_lines.append(f.read())
        compiled_lines.append("\n\n---\n\n")

    for i in range(1, 11):
        files = get_fascicle_files(i)
        if not files: continue
        
        print(f"Processing Fascicle {i}...")
        
        # New Chapter (Fascicle)
        compiled_lines.append(f"\n# Fascicle {i}\n\n")
        
        for filename in files:
            lines = read_markdown_file(filename)
            for line in lines:
                line = line.strip()
                
                # --- Artifact Stripping (Same as DOCX script) ---
                if not line:
                    compiled_lines.append("\n")
                    continue
                
                if line.startswith('<!--') or line.startswith('Next:') or line.startswith('**Next') or line.startswith('**Translated by'):
                    continue
                
                # Check for various metadata key formats (bolded or plain)
                clean_line = line.replace('*', '').strip()
                if clean_line.startswith('Source:') or clean_line.startswith('Author:') or clean_line.startswith('Translator:') or clean_line.startswith('Date:') or clean_line.startswith('CBETA:') or clean_line.startswith('Section:'):
                    continue

                # Robust Stripping
                if "The Architect" in clean_line or "MAS Agent" in clean_line: continue
                if "Colophon" in clean_line: continue
                if "🎉" in clean_line: continue
                if "Translation continues" in clean_line or "complete. Translation continues" in clean_line or "translation complete" in clean_line or "fully translated" in clean_line: continue

                if "END OF FASCICLE" in line.upper() or "END OF SECTION" in line.upper(): continue
                if line.startswith('**END'): continue
                if line.startswith('---'): continue
                if clean_line == "Footnotes" or clean_line == "## Footnotes": continue

                # --- Header Demotion ---
                if line.startswith('# '):
                    text = clean_header_text(line[2:])
                    compiled_lines.append(f"## {text}\n")
                    continue
                if line.startswith('## '):
                    text = clean_header_text(line[3:])
                    if "Scholarly Translation" in text or "Translation" == text.strip() or "Colophon" in text or "Footnotes" in text:
                        continue
                    compiled_lines.append(f"### {text}\n")
                    continue
                if line.startswith('### '):
                    text = clean_header_text(line[4:])
                    compiled_lines.append(f"#### {text}\n")
                    continue
                if line.startswith('#### '):
                    text = clean_header_text(line[5:])
                    compiled_lines.append(f"##### {text}\n")
                    continue
                
                # Default Text
                compiled_lines.append(f"{line}\n")
    
    # --- Append Methodology ---
    methodology_path = "/Users/williamaltig/claudeprojects/TRANSLATION_METHODOLOGY.md"
    if os.path.exists(methodology_path):
        with open(methodology_path, 'r', encoding='utf-8') as f:
            meth_lines = f.readlines()
            # Add Page Break (horizontal rule in MD)
            compiled_lines.append("\n\n---\n\n")
            for line in meth_lines:
                compiled_lines.append(line)

    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.writelines(compiled_lines)
    
    print(f"Successfully created: {OUTPUT_MD}")

if __name__ == "__main__":
    process_markdown_compile()
