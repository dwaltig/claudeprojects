#!/usr/bin/env python3
"""
Update chapter HTML files with study guide links
"""

import os
import re

# Map of chapters that have study guides
CHAPTERS_WITH_GUIDES = {
    1: "Chapter 1: Introduction",
    2: "Chapter 2: Skillful Means",
    3: "Chapter 3: Parables",
    4: "Chapter 4: Faith & Understanding",
    5: "Chapter 5: Medicinal Herbs",
    6: "Chapter 6: Prophecies",
    7: "Chapter 7: Phantom City",
    8: "Chapter 8: Five Hundred Disciples",
    9: "Chapter 9: Learning & Unlearning Disciples",
    10: "Chapter 10: Dharma-Teacher",
    11: "Chapter 11: Emergence of Prabhūtaratna's Stupa",
    12: "Chapter 12: Devadatta and the Nāga Princess",
    13: "Chapter 13: Exhortation to Uphold",
    14: "Chapter 14: Peaceful Practice",
    15: "Chapter 15: Emergence of Bodhisattvas from the Earth",
    16: "Chapter 16: Buddha's Eternal Lifespan",
    17: "Chapter 17: Discrimination of Merits",
    18: "Chapter 18: Merit of Rejoicing",
    19: "Chapter 19: Dharma-Teacher's Merits",
    20: "Chapter 20: Never-Despiser Bodhisattva",
    21: "Chapter 21: Tathāgata's Supernatural Powers",
    22: "Chapter 22: Entrustment",
    23: "Chapter 23: Medicine King's Original Practice",
    24: "Chapter 24: Wonderful-Sound Bodhisattva",
    25: "Chapter 25: Avalokiteśvara",
    26: "Chapter 26: Dharani of Protective Formulas",
    27: "Chapter 27: Wonderful-Adornment King's Original Practice",
    28: "Chapter 28: Samantabhadra's Vows",
}

def update_chapter_file(chapter_num):
    """Update a single chapter HTML file"""
    filepath = f"chapters/chapter_{chapter_num:02d}.html"
    
    if not os.path.exists(filepath):
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Determine the replacement text
    if chapter_num in CHAPTERS_WITH_GUIDES:
        # Study guide exists
        guide_name = f"CHAPTER_{chapter_num:02d}_STUDY_GUIDE.md"
        replacement = f'''<h3>Deepen Your Study</h3>
                <p>
                    <strong><a href="../_PRACTICE_LAYER/02_Chapter_Study_Guides/{guide_name}" target="_blank">📖 Complete Study Guide</a></strong>
                </p>
                <p style="color: #666; font-size: 0.9em; margin-top: 1rem;">
                    Comprehensive guide with learning objectives, key passages, reflection questions, five practices, 
                    30-40 minute meditation, and group discussion.
                </p>
                <a href="../_PRACTICE_LAYER/04_Meditation_Practice/MEDITATION_FOCAL_POINTS_COMPILED.md" class="study-link">🧘 Meditation</a>
                <a href="../_PRACTICE_LAYER/03_Daily_Practice/DAILY_DHARMA_EXTRACTS.md" class="study-link">📖 Daily Extract</a>'''
    else:
        # Study guide coming soon
        replacement = f'''<h3>Deepen Your Study</h3>
                <p style="color: #666; font-style: italic; margin-bottom: 1rem;">
                    📚 <strong>Study Guide for this chapter is coming soon.</strong> In the meantime, explore our <a href="../index.html#practice">practice materials</a>.
                </p>
                <a href="../_PRACTICE_LAYER/04_Meditation_Practice/MEDITATION_FOCAL_POINTS_COMPILED.md" class="study-link">🧘 Meditation</a>
                <a href="../_PRACTICE_LAYER/03_Daily_Practice/DAILY_DHARMA_EXTRACTS.md" class="study-link">📖 Daily Extract</a>'''
    
    # Pattern to find and replace the section
    pattern = r'<h3>Deepen Your Study</h3>.*?(?=<div class="chapter-nav")'
    
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, replacement + '\n\n                ', content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    return False

# Update all chapters
updated_count = 0
for chapter_num in range(1, 29):
    if update_chapter_file(chapter_num):
        updated_count += 1

print(f"✅ Successfully updated {updated_count} chapter files")
print(f"📊 Study Guides Available: {len(CHAPTERS_WITH_GUIDES)}/28 chapters")
