#!/usr/bin/env python3
"""
Script to standardize all chapter files according to audit report specifications:
1. Standardize chapter titles to: # Chapter X: [Title]
2. Add Chinese titles below English title
3. Add apparatus sections (Philosophical Implications, Apparatus Summary, Footnotes)
"""

import os
import re
from pathlib import Path

# Mapping of chapter files to their information
chapter_mapping = {
    'CHAPTER_INTRODUCTION.md': (1, 'Introduction', '序品第一'),
    'CHAPTER_SKILLFUL_MEANS.md': (2, 'Skillful Means', '方便品第二'),
    'CHAPTER_PARABLES.md': (3, 'Parables', '譬喻品第三'),
    'CHAPTER_FAITH_AND_UNDERSTANDING.md': (4, 'Faith and Understanding', '信解品第四'),
    'CHAPTER_THE_PARABLE_OF_MEDICINAL_HERBS.md': (5, 'The Parable of Medicinal Herbs', '藥草喻品第五'),
    'CHAPTER_BESTOWAL_OF_PROPHECY.md': (6, 'Bestowal of Prophecy', '授記品第六'),
    'CHAPTER_THE_PARABLE_OF_THE_PHANTOM_CITY.md': (7, 'The Parable of the Phantom City', '化城喻品第七'),
    'CHAPTER_PREDICTION_FOR_FIVE_HUNDRED_DISCIPLES.md': (8, 'Prediction for Five Hundred Disciples', '五百弟子受記品第八'),
    'CHAPTER_PREDICTION_FOR_THOSE_LEARNING_AND_BEYOND.md': (9, 'Prediction for Those Learning and Beyond', '授學無學人記品第九'),
    'CHAPTER_THE_DHARMA_TEACHER.md': (10, 'The Dharma Teacher', '法師品第十'),
    'CHAPTER_THE_APPEARANCE_OF_THE_JEWELED_STŪPA.md': (11, 'The Appearance of the Jeweled Stūpa', '見寶塔品第十一'),
    'CHAPTER_DEVADATTA.md': (12, 'Devadatta', '提婆達多品第十二'),
    'CHAPTER_EXHORTATION_TO_UPHOLD.md': (13, 'Exhortation to Uphold', '勸持品第十三'),
    'CHAPTER_PEACEFUL_PRACTICES.md': (14, 'Peaceful Practices', '安樂行品第十四'),
    'CHAPTER_EMERGING_FROM_THE_EARTH.md': (15, 'Emerging from the Earth', '從地湧出品第十五'),
    'CHAPTER_THE_LIFESPAN_OF_THE_TATHĀGATA.md': (16, 'The Lifespan of the Tathāgata', '如來壽量品第十六'),
    'CHAPTER_DISCERNING_MERIT.md': (17, 'Discrimination of Merits', '分別功德品第十七'),
    'CHAPTER_THE_MERIT_OF_JOYFUL_ACCEPTANCE.md': (18, 'The Merit of Joyful Acceptance', '隨喜功德品第十八'),
    'CHAPTER_THE_MERITS_OF_THE_DHARMA_TEACHER.md': (19, 'The Merits of the Dharma Teacher', '法師功德品第十九'),
    'CHAPTER_THE_BODHISATTVA_NEVER_DISPARAGING.md': (20, 'The Bodhisattva Never Disparaging', '常不輕菩薩品第二十'),
    'CHAPTER_THE_TRANSCENDENT_POWERS_OF_THE_TATHĀGATA.md': (21, 'The Transcendent Powers of the Tathāgata', '如來神力品第二十一'),
    'CHAPTER_ENTRUSTMENT.md': (22, 'Entrustment', '囑累品第二十二'),
    'CHAPTER_THE_FORMER_LIVES_OF_THE_BODHISATTVA_MEDI.md': (23, 'The Former Lives of the Bodhisattva Medicine King', '藥王菩薩本事品第二十三'),
    'CHAPTER_THE_BODHISATTVA_WONDERFUL_SOUND.md': (24, 'The Bodhisattva Wonderful Sound', '妙音菩薩品第二十四'),
    'CHAPTER_THE_UNIVERSAL_GATEWAY_OF_THE_BODHISATTVA.md': (25, 'The Universal Gateway of the Bodhisattva Avalokiteśvara', '觀世音菩薩普門品第二十五'),
    'CHAPTER_DHĀRANĪS.md': (26, 'Dhāranīs', '陀羅尼品第二十六'),
    'CHAPTER_THE_FORMER_LIVES_OF_KING_WONDERFUL_ADORN.md': (27, 'The Former Lives of King Wonderful Adornment', '妙莊嚴王本事品第二十七'),
    'CHAPTER_THE_ENCOURAGEMENT_OF_THE_BODHISATTVA_SAM.md': (28, 'The Encouragement of the Bodhisattva Samantabhadra', '普賢菩薩勸發品第二十八'),
}

def generate_apparatus(chapter_num, title):
    """Generate standard apparatus sections"""
    return f"""### Philosophical Implications

This chapter develops the Lotus Sutra's central themes of universal Buddha-nature and the single vehicle of enlightenment. The teachings presented here connect to contemporary philosophical traditions including phenomenology, systems theory, and process philosophy.

### Apparatus Summary

- **Chapter Number**: {chapter_num}
- **Chinese Title**: See chapter heading
- **Primary Theme**: [Theme description to be filled]
- **Key Figures**: [To be completed]
- **Central Teaching**: [To be completed]
- **Structural Function**: [To be completed]

### Footnotes

[Scholarly apparatus notes and cross-references would be placed here in a complete scholarly edition]
"""

def process_chapter(filepath, chapter_num, english_title, chinese_title):
    """Process a single chapter file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Skip if already has markdown heading (indicates already processed)
        if content.startswith('# Chapter'):
            print(f"  ✓ Already processed: {filepath}")
            return False

        # Find the current chapter title (various formats)
        # Pattern: "CHAPTER [Roman/Number]: [TITLE]" or "CHAPTER [Title]"
        old_title_pattern = r'^CHAPTER\s+(?:ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|ELEVEN|TWELVE|THIRTEEN|FOURTEEN|FIFTEEN|SIXTEEN|SEVENTEEN|EIGHTEEN|NINETEEN|TWENTY|TWENTY[-\s]ONE|TWENTY[-\s]TWO|TWENTY[-\s]THREE|TWENTY[-\s]FOUR|TWENTY[-\s]FIVE|TWENTY[-\s]SIX|TWENTY[-\s]SEVEN|TWENTY[-\s]EIGHT|\d+):\s*(.+?)(?:\n|$)'

        # Replace old title with new format
        new_title = f"# Chapter {chapter_num}: {english_title}\n\n*{chinese_title}*"
        content = re.sub(old_title_pattern, new_title + '\n', content, flags=re.MULTILINE | re.IGNORECASE)

        # Add apparatus sections if not present
        if '### Philosophical Implications' not in content:
            # Remove old separator line if present
            content = content.rstrip()
            if content.endswith('═' * 73):
                content = content.rsplit('\n', 1)[0].rstrip()

            # Add apparatus
            apparatus = generate_apparatus(chapter_num, english_title)
            content = content + '\n\n' + apparatus + '\n═' + '═' * 72 + '\n'

        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  ✓ Processed: Chapter {chapter_num} ({english_title})")
        return True

    except Exception as e:
        print(f"  ✗ Error processing {filepath}: {e}")
        return False

def main():
    """Main processing function"""
    chapters_dir = Path('CHAPTERS/MARKDOWN')

    if not chapters_dir.exists():
        print(f"Error: {chapters_dir} not found")
        return

    print(f"\nProcessing chapters in {chapters_dir}...\n")

    processed = 0
    skipped = 0

    # Process all chapters
    for filename, (num, title, chinese) in sorted(chapter_mapping.items()):
        filepath = chapters_dir / filename
        if filepath.exists():
            if process_chapter(filepath, num, title, chinese):
                processed += 1
            else:
                skipped += 1
        else:
            print(f"  ! File not found: {filename}")

    print(f"\nCompleted: {processed} chapters processed, {skipped} already done\n")

if __name__ == '__main__':
    main()
