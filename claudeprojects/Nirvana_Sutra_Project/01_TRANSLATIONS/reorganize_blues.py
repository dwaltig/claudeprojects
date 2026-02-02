import re

# Read the complete file
with open('Chapter_2_Blues_Complete.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Split into sections
sections = content.split('# Nirvana Sutra - Chapter 2, Section')
sections = ['# Nirvana Sutra - Chapter 2, Section' + s for s in sections[1:]]  # Skip empty first element

# Storage for reorganized content
narratives = []
atmospheres = []
key_terms = []
lotus_connections = []

for i, section in enumerate(sections, 1):
    # Extract section number and title
    title_match = re.search(r'# Nirvana Sutra - Chapter 2, Section (\d+): (.+?) \(Blues Version\)', section)
    if title_match:
        section_num = title_match.group(1)
        section_title = title_match.group(2)
    else:
        section_num = str(i)
        section_title = "Unknown"
    
    # Split on the major headers
    parts = re.split(r'\n## (THE ATMOSPHERE|Key Terms \(Endnotes for Learners\)|Lotus Sutra Connections)\n', section)
    
    # First part is the narrative (before any apparatus)
    narrative = parts[0]
    
    # Clean up the narrative - remove metadata lines
    narrative_lines = narrative.split('\n')
    cleaned_narrative = []
    skip_next = False
    for line in narrative_lines:
        if line.startswith('**Source Text:**') or line.startswith('**Section Title:**') or line.startswith('**Translator:**'):
            continue
        if line.startswith('---') and len(cleaned_narrative) < 5:
            continue
        if line.startswith('## Agent 2:'):
            continue
        cleaned_narrative.append(line)
    
    narrative = '\n'.join(cleaned_narrative).strip()
    
    # Add section header for narrative
    narratives.append(f"\n---\n\n## Section {section_num}: {section_title}\n\n{narrative}")
    
    # Extract apparatus sections
    for j in range(1, len(parts), 2):
        if j < len(parts):
            header = parts[j]
            content_part = parts[j+1] if j+1 < len(parts) else ""
            
            if header == "THE ATMOSPHERE":
                atmospheres.append(f"\n### Section {section_num}: {section_title}\n\n{content_part.strip()}")
            elif header == "Key Terms (Endnotes for Learners)":
                key_terms.append(f"\n### Section {section_num}: {section_title}\n\n{content_part.strip()}")
            elif header == "Lotus Sutra Connections":
                lotus_connections.append(f"\n### Section {section_num}: {section_title}\n\n{content_part.strip()}")

# Assemble the reorganized file
output = []

# Header
output.append("# Nirvana Sutra - Chapter 2: The Longevity Chapter (Blues Version)")
output.append("\n**Translator:** Kai \"Smokestack\" Johnson")
output.append("\n**Translation of:** 大般涅槃經卷第二 (Great Parinirvāṇa Sūtra, Volume Two)")
output.append("\n**Translated by:** Tripiṭaka Master Dharmakṣema of Northern Liang (421-432 CE)")
output.append("\n\n---\n")

# All narratives
output.append("\n# The Story\n")
output.extend(narratives)

# Endnotes section
output.append("\n\n---\n\n# Endnotes\n")

# THE ATMOSPHERE sections
output.append("\n## Part I: The Atmosphere\n")
output.append("\n*How to read and feel each section*\n")
output.extend(atmospheres)

# Key Terms sections
output.append("\n\n## Part II: Key Terms for Learners\n")
output.append("\n*Accessible explanations of Buddhist concepts*\n")
output.extend(key_terms)

# Lotus Sutra Connections sections
output.append("\n\n## Part III: Lotus Sutra Connections\n")
output.append("\n*The Bluesman's Take on how these teachings connect*\n")
output.extend(lotus_connections)

# Write the reorganized file
with open('Chapter_2_Blues_Complete_Reorganized.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

print("Reorganized file created: Chapter_2_Blues_Complete_Reorganized.md")
