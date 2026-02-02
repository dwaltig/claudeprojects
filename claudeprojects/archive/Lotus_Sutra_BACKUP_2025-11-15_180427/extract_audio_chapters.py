#!/usr/bin/env python3
"""
Extract all 28 Blues interpretation chapters from cleaned master file
for audio production. This ensures all chapter files match the cleaned
master version perfectly.
"""

import os
import re

MASTER_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/00_MASTER_VERSIONS/LS_final_version/02_BLUES_INTERPRETATION_Contemporary_Vernacular.txt"
OUTPUT_DIR = "/Users/williamaltig/claudeprojects/Lotus_Sutra/04_AUDIO_PRODUCTION/chapters/"

# Read the master file
with open(MASTER_FILE, 'r', encoding='utf-8') as f:
    content = f.read()
    lines = content.split('\n')

# Define chapter information - with EXACT titles from master file
chapters = [
    {'num': 1, 'title': 'THE OPENING'},
    {'num': 2, 'title': 'THE LOVING TRICKS'},
    {'num': 3, 'title': 'THE PARABLE'},
    {'num': 4, 'title': 'FAITH AND UNDERSTANDING'},
    {'num': 5, 'title': 'THE PARABLE OF THE MEDICINAL HERBS'},
    {'num': 6, 'title': 'THE NAMING'},
    {'num': 7, 'title': 'THE PHANTOM CITY BLUES'},
    {'num': 8, 'title': 'WHEN THE FIVE HUNDRED FINALLY HEARD THEIR NAMES CALLED'},
    {'num': 9, 'title': 'WHEN THE FAITHFUL GET THEIR DUE'},
    {'num': 10, 'title': 'HONOR THE WORD-CARRIERS'},
    {'num': 11, 'title': 'WHEN THE JEWELED TOWER ROSE UP'},
    {'num': 12, 'title': 'WHEN YOUR ENEMY WAS YOUR TEACHER'},
    {'num': 13, 'title': 'WHEN THE ROAD GETS ROUGH, YOU GOTTA KEEP WALKING'},
    {'num': 14, 'title': 'HOW TO KEEP YOUR SOUL CLEAN WHEN THE WORLD\'S GONE WRONG'},
    {'num': 15, 'title': 'WHEN THE UNDERGROUND ARMY ROSE UP'},
    {'num': 16, 'title': 'HOW LONG THE TATHĀGATA\'S BEEN ALIVE'},
    {'num': 17, 'title': 'COUNTING UP THE GRACE'},
    {'num': 18, 'title': 'THE JOY THAT MULTIPLIES'},
    {'num': 19, 'title': 'WHEN YOUR SENSES WAKE UP'},
    {'num': 20, 'title': 'THE BODHISATTVA WHO NEVER LOOKED DOWN'},
    {'num': 21, 'title': 'WHEN THE LORD SHOWED HIS HAND'},
    {'num': 22, 'title': 'THE PASSING ON'},
    {'num': 23, 'title': 'MEDICINE KING BODHISATTVA - THE STORY OF HOW HE GAVE IT ALL'},
    {'num': 24, 'title': 'WONDERFUL SOUND BODHISATTVA'},
    {'num': 25, 'title': 'THE ONE WHO HEARS THE WORLD CRYING'},
    {'num': 26, 'title': 'THE PROTECTION SONGS'},
    {'num': 27, 'title': 'THE BEAUTIFUL KING AND HIS GOOD FRIENDS'},
    {'num': 28, 'title': 'UNIVERSAL WORTHY COMES TO ENCOURAGE YOU'},
]

def num_to_word(num):
    """Convert number to word (1 -> ONE, 21 -> TWENTY-ONE, etc)."""
    ones = ['', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
    teens = ['TEN', 'ELEVEN', 'TWELVE', 'THIRTEEN', 'FOURTEEN', 'FIFTEEN',
             'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN']
    tens = ['', '', 'TWENTY', 'THIRTY', 'FORTY', 'FIFTY', 'SIXTY', 'SEVENTY', 'EIGHTY', 'NINETY']

    if num < 10:
        return ones[num]
    elif num < 20:
        return teens[num - 10]
    elif num < 30:
        return 'TWENTY' + ('-' + ones[num - 20] if num > 20 else '')
    elif num < 100:
        return tens[num // 10] + ('-' + ones[num % 10] if num % 10 != 0 else '')

def extract_chapter(content, chapter_num, chapter_title):
    """Extract chapter content by finding chapter header and next END marker."""
    # Build chapter number word
    num_word = num_to_word(chapter_num)

    # Build start marker
    start_marker = f"CHAPTER {num_word}: {chapter_title}"

    # Build end marker
    end_marker = f"END OF CHAPTER {num_word}"

    start_idx = content.find(start_marker)
    if start_idx == -1:
        return None

    # Find the end marker
    end_idx = content.find(end_marker, start_idx)
    if end_idx == -1:
        # If no end marker found, try to find next chapter
        for next_num in range(chapter_num + 1, 100):
            next_num_word = num_to_word(next_num)
            next_chapter = content.find(f"CHAPTER {next_num_word}:", start_idx + 1)
            if next_chapter != -1:
                end_idx = next_chapter
                break
        if end_idx == -1:
            end_idx = len(content)
    else:
        # Include the end marker line
        end_idx = content.find('\n', end_idx)

    return content[start_idx:end_idx]

def format_filename(num, title):
    """Format chapter filename."""
    title_clean = title.replace(' ', '_').upper()
    return f"{num:02d}_CHAPTER_{title_clean}.txt"

# Extract and save all chapters
print("=" * 80)
print("EXTRACTING CHAPTERS FROM CLEANED MASTER FILE")
print("=" * 80)
print()

extracted = 0
failed = 0

for chapter in chapters:
    chapter_content = extract_chapter(content, chapter['num'], chapter['title'])

    if chapter_content:
        filename = format_filename(chapter['num'], chapter['title'])
        filepath = os.path.join(OUTPUT_DIR, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(chapter_content)

        print(f"✓ Chapter {chapter['num']:2d}: {chapter['title']:<60} ({len(chapter_content):>7} bytes)")
        extracted += 1
    else:
        print(f"✗ Chapter {chapter['num']:2d}: {chapter['title']:<60} FAILED")
        failed += 1

print()
print("=" * 80)
print(f"EXTRACTION COMPLETE: {extracted} chapters extracted, {failed} failed")
print("=" * 80)
print()
print(f"All chapters saved to: {OUTPUT_DIR}")
print("All chapters are now synchronized with the cleaned master file.")
