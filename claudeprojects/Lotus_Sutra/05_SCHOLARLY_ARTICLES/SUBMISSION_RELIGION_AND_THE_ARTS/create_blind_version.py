import re

input_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/05_SCHOLARLY_ARTICLES/SUBMISSION_RELIGION_AND_THE_ARTS/ARTICLE_Dharma_Sings_Blues_RELIGION_ARTS_CHICAGO.md"
output_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/05_SCHOLARLY_ARTICLES/SUBMISSION_RELIGION_AND_THE_ARTS/ARTICLE_Dharma_Sings_Blues_RELIGION_ARTS_CHICAGO_BLIND.md"

with open(input_file, 'r') as f:
    lines = f.readlines()

new_lines = []
skip_mode = False

for line in lines:
    # 1. Remove Title Page Info (Name, Email)
    if "William Altig" in line and not "References" in line and not "[^" in line:
        continue # Skip name in header
    if "Independent Scholar" in line:
        continue
    if "Houston, TX" in line:
        continue
    if "dwaltig@gmail.com" in line:
        continue
    
    # 2. Anonymize Citations in Footnotes and References
    # Check for "Altig" in footnotes or references
    if "Altig" in line:
        if line.strip().startswith("[^"): # Footnote
             # Handle short citations like 'Altig, "Blues Lotus Sutra"'
             if 'Altig, "' in line or "Altig," in line:
                  new_line = line.replace('Altig,', 'Author,')
                  new_lines.append(new_line)
             else:
                  new_lines.append(re.sub(r'[^\]]+Altig[^)]+\)', '[Citation omitted for blind review]', line))
        elif line.strip().startswith("Altig"): # Reference List
             new_lines.append("Reference omitted for blind review.\n")
        elif "William Altig" in line: # Generative AI or Bio
             # If it's the Bio section, we might skip the whole section
             if "Biographical Note" in line:
                 skip_mode = True # Skip the header
                 continue
             
             if not skip_mode:
                 # Replace in text if unavoidably present (e.g. AI disclosure)
                 line = line.replace("William Altig", "The Author")
                 new_lines.append(line)
        else:
            new_lines.append(line)
        continue

    # Manage sections to skip
    if "## Biographical Note" in line:
        skip_mode = True
        continue
    
    if "## References" in line:
        skip_mode = False # Stop skipping when we hit references
        new_lines.append(line)
        continue

    if skip_mode:
        continue

    new_lines.append(line)

with open(output_file, 'w') as f:
    f.writelines(new_lines)
