import os
import re

# Configuration
BASE_DIR = "/Users/williamaltig/claudeprojects/Tiantai_Teachings_Project/01_TRANSLATIONS/Great_Cessation/Scholarly"
OUTPUT_MD = "/Users/williamaltig/claudeprojects/Mohe_Zhiguan_Publication_Ready.md"

def get_chapter_files(chapter_num):
    pattern = f"Mohe_Zhiguan_Chapter_{chapter_num:02d}_"
    files = [f for f in os.listdir(BASE_DIR) if f.startswith(pattern) and "SCHOLARLY" in f]
    
    def sort_key(filename):
        part_match = re.search(r"Part_(\d+)", filename)
        if part_match: return int(part_match.group(1))
        if "Summary" in filename: return 999
        return 0
        
    files.sort(key=sort_key)
    return files

def read_markdown_file(filename):
    path = os.path.join(BASE_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()

def clean_header_text(text):
    text = re.sub(r'^Mohe Zhiguan - Chapter \d+[:]? ', '', text)
    text = re.sub(r'\(Part \d+.*?\)', '', text)
    return text.strip()

def process_mohe_md():
    compiled_lines = []
    
    # Metadata for Pandoc
    compiled_lines.append(f"% Mohe Zhiguan: The Great Cessation and Contemplation\n")
    compiled_lines.append(f"% Master Zhiyi\n")
    compiled_lines.append(f"% Translated by William Altig\n\n")

    for i in range(1, 11):
        files = get_chapter_files(i)
        if not files: continue
        
        print(f"Processing Chapter {i}...")
        
        compiled_lines.append(f"\n# Chapter {i}\n\n")
        
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
                if clean_line.startswith('Source:') or clean_line.startswith('Author:') or clean_line.startswith('Translator:') or clean_line.startswith('Date:') or clean_line.startswith('CBETA:'):
                    continue
                
                if "End of Section" in clean_line or "End of Chapter" in clean_line: continue
                if line.startswith('---'): continue

                # Header Demotion
                if line.startswith('# '):
                    text = clean_header_text(line[2:])
                    compiled_lines.append(f"## {text}\n")
                    continue
                if line.startswith('## '):
                    text = clean_header_text(line[3:])
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
    process_mohe_md()
