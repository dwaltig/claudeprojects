#!/usr/bin/env python3
"""
Split THE_LOTUS_SUTRA_SCHOLARLY_EDITION_2025.md into:
1. THE_LOTUS_SUTRA_TRANSLATION.md (pure text, footnotes only)
2. THE_LOTUS_SUTRA_COMMENTARY.md (all scholarly apparatus and analysis)
"""

import re

INPUT_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/03_SCHOLARLY_TRANSLATION_2025/THE_LOTUS_SUTRA_SCHOLARLY_EDITION_2025.md"
TRANSLATION_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/03_SCHOLARLY_TRANSLATION_2025/THE_LOTUS_SUTRA_TRANSLATION.md"
COMMENTARY_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/03_SCHOLARLY_TRANSLATION_2025/THE_LOTUS_SUTRA_COMMENTARY.md"

# Read source file
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# Patterns to identify commentary blocks
APPARATUS_PATTERN = r'^## SCHOLARLY APPARATUS.*?(?=^# Chapter|\Z)'
ANALYSIS_PATTERN = r'^### Analytical Commentary.*?(?=^#|\Z)'
ADDITIONAL_ANALYSIS_PATTERN = r'^### Additional Analysis.*?(?=^#|\Z)'
PHILOSOPHICAL_PATTERN = r'^### Philosophical .*?(?=^#|\Z)'

# Split by chapters
chapters = re.split(r'(^# Chapter \d+:.*$)', content, flags=re.MULTILINE)

translation_lines = []
commentary_lines = []

# Add headers
translation_lines.append("# The Lotus Sutra: A Translation from the Classical Chinese")
translation_lines.append("")
translation_lines.append("**Translated from Kumārajīva's Chinese Edition (Taishō Shinshū Daizōkyō No. 262)**")
translation_lines.append("")
translation_lines.append("---")
translation_lines.append("")
translation_lines.append("> **Note on Imperial Prefaces**: The complete Taishō 262 edition includes the Imperial Preface (御製大乘妙法蓮華經序) by the Yongle Emperor and the Guanyin Chapter Preface (御製觀世音普門品經序). These prefaces are absent from the digitized source used for this translation and are omitted here with acknowledgment of their historical significance.")
translation_lines.append("")
translation_lines.append("---")
translation_lines.append("")

commentary_lines.append("# The Lotus Sutra: Comparative Commentary and Philosophical Analysis")
commentary_lines.append("")
commentary_lines.append("**A companion volume to *The Lotus Sutra: A Translation from the Classical Chinese***")
commentary_lines.append("")
commentary_lines.append("This volume contains interpretive commentary drawing connections between the Lotus Sutra and Western philosophy, modern science, and comparative religious studies. These observations represent scholarly interpretation rather than translation of the source text.")
commentary_lines.append("")
commentary_lines.append("---")
commentary_lines.append("")

current_chapter = ""

for i, part in enumerate(chapters):
    if part.startswith("# Chapter"):
        current_chapter = part.strip()
        translation_lines.append("")
        translation_lines.append(current_chapter)
        translation_lines.append("")
        commentary_lines.append("")
        commentary_lines.append(current_chapter)
        commentary_lines.append("")
    else:
        # Split this chapter's content
        # Find SCHOLARLY APPARATUS section
        apparatus_match = re.search(r'^## SCHOLARLY APPARATUS.*', part, flags=re.MULTILINE | re.DOTALL)
        
        if apparatus_match:
            # Text before apparatus goes to translation
            text_before = part[:apparatus_match.start()].strip()
            # Apparatus goes to commentary
            apparatus_text = apparatus_match.group(0).strip()
            
            if text_before:
                translation_lines.append(text_before)
            if apparatus_text:
                commentary_lines.append(apparatus_text)
        else:
            # No apparatus found, check for embedded analysis
            # Remove Analysis blocks for translation
            clean_text = part
            
            # Extract analysis for commentary
            analyses = []
            for pattern_name, pattern in [
                ("Analytical", ANALYSIS_PATTERN),
                ("Additional", ADDITIONAL_ANALYSIS_PATTERN),
                ("Philosophical", PHILOSOPHICAL_PATTERN),
            ]:
                matches = re.findall(pattern, clean_text, flags=re.MULTILINE | re.DOTALL)
                for m in matches:
                    analyses.append(m)
                clean_text = re.sub(pattern, '', clean_text, flags=re.MULTILINE | re.DOTALL)
            
            if clean_text.strip():
                translation_lines.append(clean_text.strip())
            
            for a in analyses:
                if a.strip():
                    commentary_lines.append(a.strip())

# Write translation file
with open(TRANSLATION_FILE, 'w', encoding='utf-8') as f:
    f.write('\n'.join(translation_lines))

# Write commentary file
with open(COMMENTARY_FILE, 'w', encoding='utf-8') as f:
    f.write('\n'.join(commentary_lines))

print(f"Created: {TRANSLATION_FILE}")
print(f"Created: {COMMENTARY_FILE}")
print("Split complete.")
