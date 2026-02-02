#!/usr/bin/env python3
"""
Add interpretation notes to chapters that are missing them.
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

chapters_needing_notes = [9, 11, 13, 14, 15, 18, 19, 21, 25, 28]

# Read master
with open(MASTER_FILE, 'r', encoding='utf-8') as f:
    master_content = f.read()

print("Adding interpretation notes to chapters that need them:\n")

for chapter_num in chapters_needing_notes:
    chapter_word = NUM_TO_WORD.get(chapter_num)
    
    # Extract notes from master
    end_pattern = rf"END OF CHAPTER {chapter_word}:"
    end_match = re.search(end_pattern, master_content)
    
    if not end_match:
        print(f"Ch {chapter_num:2d}: ❌ Chapter not found in master")
        continue
    
    end_pos = end_match.end()
    next_chapter_num = chapter_num + 1
    next_chapter_word = NUM_TO_WORD.get(next_chapter_num)
    
    if next_chapter_word:
        next_pattern = rf"END OF CHAPTER {next_chapter_word}:"
        next_match = re.search(next_pattern, master_content[end_pos:])
        if next_match:
            notes = master_content[end_pos:end_pos + next_match.start()].strip()
        else:
            notes = master_content[end_pos:].strip()
    else:
        notes = master_content[end_pos:].strip()
    
    if not notes or len(notes) < 50:
        print(f"Ch {chapter_num:2d}: ⚠️  No notes found")
        continue
    
    # Find file
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
    
    # Check if notes already present
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "INTERPRETATION NOTES:" in content:
        print(f"Ch {chapter_num:2d}: ✓ Already has notes")
        continue
    
    # Append notes after the END OF CHAPTER marker
    end_marker = f"END OF CHAPTER {chapter_word}:"
    if end_marker in content:
        insert_pos = content.find(end_marker) + len(end_marker)
        new_content = content[:insert_pos] + "\n\n" + notes + "\n"
    else:
        # No marker - just append to end
        new_content = content.rstrip() + "\n\n" + notes + "\n"
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Ch {chapter_num:2d}: ✓ Added {len(notes)} chars of notes")
    except Exception as e:
        print(f"Ch {chapter_num:2d}: ❌ Error: {e}")

print("\n✅ Done")
