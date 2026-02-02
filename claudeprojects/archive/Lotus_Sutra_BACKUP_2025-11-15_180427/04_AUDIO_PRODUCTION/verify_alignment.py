#!/usr/bin/env python3
"""
Verify that extracted chapters match the master file exactly.
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

print("Verifying chapter alignment with master file:\n")

all_match = True
for chapter_num in range(1, 29):
    chapter_word = NUM_TO_WORD.get(chapter_num)
    
    # Extract from master
    start_pattern = rf"CHAPTER {chapter_word}:"
    start_match = re.search(start_pattern, master_content)
    
    end_pattern = rf"END OF CHAPTER {chapter_word}:"
    end_match = re.search(end_pattern, master_content[start_match.start():])
    
    master_chapter_content = master_content[start_match.start():start_match.start() + end_match.end()]
    master_words = len(master_chapter_content.split())
    
    # Find extracted file
    if chapter_num < 10:
        pattern_str = f"{chapter_num:02d}_CHAPTER"
    else:
        pattern_str = f"{chapter_num}_CHAPTER"
    
    matching_files = [f for f in os.listdir(CHAPTERS_DIR) 
                     if pattern_str in f and f.endswith("_OPTIMIZED.txt")]
    
    if not matching_files:
        print(f"Ch {chapter_num:2d}: ❌ File not found")
        all_match = False
        continue
    
    with open(os.path.join(CHAPTERS_DIR, matching_files[0]), 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    # Extract chapter portion (before INTERPRETATION NOTES)
    if "INTERPRETATION NOTES:" in file_content:
        file_chapter_content = file_content[:file_content.find("INTERPRETATION NOTES:")].strip()
    else:
        # If no interpretation notes, extract up to last --- marker
        if "---\n\nEND OF CHAPTER" in file_content:
            file_chapter_content = file_content[:file_content.find("---\n\nEND OF CHAPTER")+3]
        else:
            file_chapter_content = file_content
    
    file_words = len(file_chapter_content.split())
    
    # Compare
    if master_words == file_words:
        status = "✓"
    else:
        status = "❌"
        all_match = False
    
    print(f"Ch {chapter_num:2d}: {status} Master: {master_words:5d} words | File: {file_words:5d} words")

print(f"\n{'='*60}")
if all_match:
    print("✅ ALL CHAPTERS ALIGNED WITH MASTER FILE")
else:
    print("⚠️  Some chapters have word count mismatches")
