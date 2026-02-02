import re
import sys
import os

def standardize_headers(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    first_h1_found = False

    for i, line in enumerate(lines):
        # 1. Keep the very first H1 as the document title
        if line.startswith('# '):
            if not first_h1_found:
                new_lines.append(line)
                first_h1_found = True
            else:
                # Demote subsequent H1 to H2
                new_lines.append('## ' + line[2:])
        # 2. Demote H2 to H3
        elif line.startswith('## '):
            new_lines.append('### ' + line[3:])
        # 3. Demote H3 to H4
        elif line.startswith('### '):
            new_lines.append('#### ' + line[4:])
        # 4. Demote H4 to H5
        elif line.startswith('#### '):
            new_lines.append('##### ' + line[5:])
        else:
            new_lines.append(line)

    # Now deduplicate adjacent redundant headers
    # e.g., ## Title followed by ### Title
    deduplicated_lines = []
    prev_title = None
    prev_level = None

    for line in new_lines:
        match = re.match(r'^(#+)\s+(.*)', line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            
            # If this title is the same as the previous title and is at a deeper level, skip it
            if title == prev_title and level > prev_level:
                continue
            
            prev_title = title
            prev_level = level
            deduplicated_lines.append(line)
        else:
            deduplicated_lines.append(line)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(deduplicated_lines)
    print("Header standardization and deduplication complete.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        standardize_headers(sys.argv[1])
    else:
        print("Usage: python3 script.py <filepath>")
