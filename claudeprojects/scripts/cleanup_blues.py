
import re

def process_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        # 1. Replace Master Kim with The Luthier
        # Simple string replacement might be enough, but let's be careful.
        # "Master Kim's Note" -> "The Luthier's Note"
        # "Master Kim" -> "The Luthier"
        # "Kim" (standalone) -> "The Luthier" (if referring to the person)
        
        # Replace specific known patterns first
        line = line.replace("Master Kim's", "The Luthier's")
        line = line.replace("Master Kim", "The Luthier")
        # Check for standalone "Kim,"
        line = line.replace("Kim,", "Luthier,")
        
        # 2. Downgrade H2 headers that are NOT Chapters
        # Regex for line starting with ## (and not ###)
        if line.startswith('## ') and not line.startswith('### '):
            # Check if it starts with "## Chapter" or "## Book" (just in case)
            if not line.startswith('## Chapter'):
                # It's a non-chapter H2. Downgrade to H3.
                # Only add one #
                line = '#' + line
        
        new_lines.append(line)

    with open(file_path, 'w') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    process_file('/Users/williamaltig/claudeprojects/Miao-lo/Guketsu_Project/01_TRANSLATIONS/Guketsu_Complete_Blues.md')
