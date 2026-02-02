#!/usr/bin/env python3
"""
Add proper END OF CHAPTER markers to chapters that are missing them.
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

# Read master to get END OF CHAPTER lines
with open(MASTER_FILE, 'r', encoding='utf-8') as f:
    master_content = f.read()

print("Fixing END OF CHAPTER markers in all chapters:\n")

for chapter_num in range(1, 29):
    chapter_word = NUM_TO_WORD.get(chapter_num)
    
    # Find the END OF CHAPTER line in master
    end_pattern = rf"END OF CHAPTER {chapter_word}:[^\n]*"
    end_match = re.search(end_pattern, master_content)
    
    if not end_match:
        print(f"Ch {chapter_num:2d}: ⚠️  No END OF CHAPTER marker found in master")
        continue
    
    end_line = end_match.group()
    
    # Find chapter file
    if chapter_num < 10:
        pattern_str = f"{chapter_num:02d}_CHAPTER"
    else:
        pattern_str = f"{chapter_num}_CHAPTER"
    
    matching_files = [f for f in os.listdir(CHAPTERS_DIR) 
                     if pattern_str in f and f.endswith("_OPTIMIZED.txt")]
    
    if not matching_files:
        print(f"Ch {chapter_num:2d}: ❌ File not found")
        continue
    
    filepath = os.path.join(CHAPTERS_DIR, matching_files[0])
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if END OF CHAPTER marker already exists
    if f"END OF CHAPTER {chapter_word}:" in content:
        print(f"Ch {chapter_num:2d}: ✓ Already has END OF CHAPTER marker")
        continue
    
    # Find where to insert it - before "INTERPRETATION NOTES:" or at end
    if "INTERPRETATION NOTES:" in content:
        insert_pos = content.find("INTERPRETATION NOTES:")
        # Back up to include the blues interpretation header
        notes_section_start = content.rfind("Blues Interpretation from Classical Chinese", 0, insert_pos)
        if notes_section_start == -1:
            notes_section_start = insert_pos
        
        # Insert the END OF CHAPTER marker
        new_content = content[:notes_section_start].rstrip() + "\n\n" + end_line + "\n\n" + content[notes_section_start:]
    else:
        # No interpretation notes found - add at end
        new_content = content.rstrip() + "\n\n" + end_line + "\n"
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Ch {chapter_num:2d}: ✓ Added END OF CHAPTER marker")
    except Exception as e:
        print(f"Ch {chapter_num:2d}: ❌ Error: {e}")

print("\n✅ Completed")
