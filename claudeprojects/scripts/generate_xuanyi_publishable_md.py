import os
import re

# Configuration
BASE_DIR = "/Users/williamaltig/claudeprojects/Tiantai_Teachings_Project/01_TRANSLATIONS/The_Profound_Meaning/Scholarly"
OUTPUT_MD = "/Users/williamaltig/claudeprojects/Fahua_Xuanyi_Publication_Ready.md"

def get_fascicle_files(fascicle_num):
    pattern = f"Xuanyi_Fascicle_{fascicle_num:02d}_"
    files = [f for f in os.listdir(BASE_DIR) if f.startswith(pattern) and "SCHOLARLY" in f]
    
    def sort_key(filename):
        part_match = re.search(r"Part_(\d+)", filename)
        if part_match: return int(part_match.group(1))
        return 0
        
    files.sort(key=sort_key)
    return files

def read_markdown_file(filename):
    path = os.path.join(BASE_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()

def clean_header_text(text):
    text = re.sub(r'^Xuanyi [-–] Fascicle \d+[:]? ', '', text)
    text = re.sub(r'^Fascicle \d+[:]? ', '', text)
    return text.strip()

def process_xuanyi_md():
    compiled_lines = []
    
    # Metadata Block for Pandoc (YAML-like)
    compiled_lines.append(f"% Fahua Xuanyi: The Profound Meaning of the Lotus Sutra\n")
    compiled_lines.append(f"% Master Zhiyi\n")
    compiled_lines.append(f"% Translated by The Tiantai Teachings Project\n")
    compiled_lines.append(f"% ISBN: 9798245493282\n\n")

    for i in range(1, 11):
        files = get_fascicle_files(i)
        if not files: continue
        
        print(f"Processing Fascicle {i}...")
        
        compiled_lines.append(f"\n# Fascicle {i}\n\n")
        
        for filename in files:
            lines = read_markdown_file(filename)
            for line in lines:
                line = line.strip()
                
                if not line:
                    compiled_lines.append("\n")
                    continue
                
                # Metadata Stripping
                if line.startswith('<!--') or line.startswith('Next:') or line.startswith('**Next') or line.startswith('**Translated by'):
                    continue
                
                clean_line = line.replace('*', '').strip()
                if clean_line.startswith('Source:') or clean_line.startswith('Author:') or clean_line.startswith('Translator:') or clean_line.startswith('Date:') or clean_line.startswith('CBETA:') or clean_line.startswith('Section:'):
                    continue
                if "The Architect" in clean_line or "MAS Agent" in clean_line: continue
                
                if "Translation continues" in clean_line or "complete. Translation continues" in clean_line or "translation complete" in clean_line or "fully translated" in clean_line: continue
                if "End of Section" in clean_line or "End of Fascicle" in clean_line: continue
                if "Colophon" in clean_line: continue
                if "🎉" in clean_line: continue
                if line.startswith('---'): continue
                
                if clean_line == "Footnotes" or clean_line == "## Footnotes": continue

                # Header Demotion
                if line.startswith('# '):
                    text = clean_header_text(line[2:])
                    compiled_lines.append(f"## {text}\n")
                    continue
                if line.startswith('## '):
                    text = clean_header_text(line[3:])
                    # Remove "Fascicle X, Part Y:" prefix
                    text = re.sub(r'Fascicle \d+(, Part \d+)?: ', '', text).strip()
                    
                    if "Source Text" in text or "Architect's Translation" in text or "Scholarly Translation" in text or "Colophon" in text or "Footnotes" in text:
                        continue
                    compiled_lines.append(f"### {text}\n")
                    continue
                if line.startswith('### '):
                    text = clean_header_text(line[4:])
                    compiled_lines.append(f"#### {text}\n")
                    continue
                
                compiled_lines.append(f"{line}\n")
    
    # --- Append Methodology ---
    methodology_path = "/Users/williamaltig/claudeprojects/TRANSLATION_METHODOLOGY.md"
    if os.path.exists(methodology_path):
        with open(methodology_path, 'r', encoding='utf-8') as f:
            meth_lines = f.readlines()
            compiled_lines.append("\n\n---\n\n")
            for line in meth_lines:
                compiled_lines.append(line)

    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.writelines(compiled_lines)
    
    print(f"Successfully created: {OUTPUT_MD}")

if __name__ == "__main__":
    process_xuanyi_md()
