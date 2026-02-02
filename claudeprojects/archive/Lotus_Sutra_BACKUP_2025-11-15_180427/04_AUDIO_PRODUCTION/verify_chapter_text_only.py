#!/usr/bin/env python3
"""
Verify that chapter text (excluding notes) matches master exactly.
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

print("Verifying chapter TEXT CONTENT (excluding notes) matches master:\n")

all_match = True
for chapter_num in range(1, 29):
    chapter_word = NUM_TO_WORD.get(chapter_num)
    
    # Extract from master: from "CHAPTER X:" to "END OF CHAPTER X:"
    start_pattern = rf"CHAPTER {chapter_word}:"
    start_match = re.search(start_pattern, master_content)
    
    end_pattern = rf"END OF CHAPTER {chapter_word}:"
    end_match = re.search(end_pattern, master_content[start_match.start():])
    
    master_chapter_text = master_content[start_match.start():start_match.start() + end_match.end()]
    
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
    
    # Extract ONLY the chapter text (from start to "END OF CHAPTER" line)
    end_marker_pattern = r"END OF CHAPTER.*:\n"
    end_marker_match = re.search(end_marker_pattern, file_content)
    
    if end_marker_match:
        file_chapter_text = file_content[:end_marker_match.end()]
    else:
        print(f"Ch {chapter_num:2d}: ❌ No END OF CHAPTER marker found in file")
        all_match = False
        continue
    
    # Compare text exactly
    if master_chapter_text == file_chapter_text:
        print(f"Ch {chapter_num:2d}: ✓ TEXT MATCHES MASTER EXACTLY")
    else:
        # Check if content is the same but formatting different
        master_words = master_chapter_text.split()
        file_words = file_chapter_text.split()
        
        if master_words == file_words:
            print(f"Ch {chapter_num:2d}: ✓ CONTENT MATCHES (formatting differs)")
        else:
            print(f"Ch {chapter_num:2d}: ❌ MISMATCH - Master: {len(master_words)} words, File: {len(file_words)} words")
            all_match = False

print(f"\n{'='*60}")
if all_match:
    print("✅ ALL CHAPTER TEXT ALIGNED WITH MASTER FILE")
else:
    print("⚠️  Some chapters have content mismatches")
