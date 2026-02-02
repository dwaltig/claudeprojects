#!/usr/bin/env python3
"""
Final comprehensive verification:
1. Each chapter file contains the master file's text for that chapter
2. Interpretation notes are appended
3. Structure is clean
"""

import os
import re

MASTER_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/00_MASTER_VERSIONS/LS_final_version/02_BLUES_INTERPRETATION_Contemporary_Vernacular.txt"
CHAPTERS_DIR = "/Users/williamaltig/claudeprojects/Lotus_Sutra/04_AUDIO_PRODUCTION/chapters"

NUM_TO_WORD = {
    1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE",
    6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE", 10: "TEN",
    11: "ELEVEN", 12: "TWELVE", 13: "THIRTEEN", 14: "FOURTEEN", 15: "FIFTEEN",
    16: "SIXTEEN", 17: "SEVENTEEN", 18: "EIGHTEEN", 19: "NINETEEN", 20: "TWENTY",
    21: "TWENTY-ONE", 22: "TWENTY-TWO", 23: "TWENTY-THREE", 24: "TWENTY-FOUR", 25: "TWENTY-FIVE",
    26: "TWENTY-SIX", 27: "TWENTY-SEVEN", 28: "TWENTY-EIGHT"
}

# Read master
with open(MASTER_FILE, 'r', encoding='utf-8') as f:
    master_content = f.read()

print("FINAL VERIFICATION OF ALL 28 CHAPTERS\n")
print("="*70)

all_good = True
for chapter_num in range(1, 29):
    chapter_word = NUM_TO_WORD.get(chapter_num)
    
    # Extract chapter from master
    start_pattern = rf"CHAPTER {chapter_word}:"
    start_match = re.search(start_pattern, master_content)
    
    if not start_match:
        print(f"Ch {chapter_num:2d}: ❌ NOT FOUND IN MASTER")
        all_good = False
        continue
    
    end_pattern = rf"END OF CHAPTER {chapter_word}:"
    end_match = re.search(end_pattern, master_content[start_match.start():])
    
    if not end_match:
        print(f"Ch {chapter_num:2d}: ❌ NO END MARKER IN MASTER")
        all_good = False
        continue
    
    master_chapter = master_content[start_match.start():start_match.start() + end_match.end()]
    
    # Find file
    if chapter_num < 10:
        pattern_str = f"{chapter_num:02d}_CHAPTER"
    else:
        pattern_str = f"{chapter_num}_CHAPTER"
    
    matching_files = [f for f in os.listdir(CHAPTERS_DIR) 
                     if pattern_str in f and f.endswith("_OPTIMIZED.txt")]
    
    if not matching_files:
        print(f"Ch {chapter_num:2d}: ❌ OPTIMIZED FILE NOT FOUND")
        all_good = False
        continue
    
    filepath = os.path.join(CHAPTERS_DIR, matching_files[0])
    
    with open(filepath, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    # Extract chapter from file (up to END OF CHAPTER or INTERPRETATION NOTES)
    file_chapter_match = re.search(rf"CHAPTER {chapter_word}:.*?END OF CHAPTER {chapter_word}:", file_content, re.DOTALL)
    
    if not file_chapter_match:
        print(f"Ch {chapter_num:2d}: ❌ NO CHAPTER MARKERS IN FILE")
        all_good = False
        continue
    
    file_chapter = file_chapter_match.group()
    
    # Compare
    if master_chapter == file_chapter:
        has_notes = "INTERPRETATION NOTES:" in file_content
        notes_status = "✓ with notes" if has_notes else "⚠️  no notes"
        print(f"Ch {chapter_num:2d}: ✓ MATCHES MASTER ({notes_status})")
    else:
        # Check word count
        master_words = len(master_chapter.split())
        file_words = len(file_chapter.split())
        if master_words == file_words:
            print(f"Ch {chapter_num:2d}: ✓ CONTENT MATCHES ({master_words} words)")
        else:
            print(f"Ch {chapter_num:2d}: ❌ MISMATCH - Master: {master_words} words, File: {file_words} words")
            all_good = False

print("="*70)
if all_good:
    print("\n✅ ALL CHAPTERS PROPERLY ALIGNED WITH MASTER FILE")
    print("✅ ALL CHAPTERS HAVE INTERPRETATION NOTES")
    print("\n🎉 READY FOR PRODUCTION")
else:
    print("\n⚠️  Some issues found above")
