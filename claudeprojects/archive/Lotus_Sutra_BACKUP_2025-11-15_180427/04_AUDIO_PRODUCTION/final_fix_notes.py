#!/usr/bin/env python3
"""
Final fix: Keep only the first "---" marker and everything before it,
then append just the interpretation notes for THIS chapter at the end.
"""

import os
import re

CHAPTERS_DIR = "/Users/williamaltig/claudeprojects/Lotus_Sutra/04_AUDIO_PRODUCTION/chapters"
MASTER_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/00_MASTER_VERSIONS/LS_final_version/02_BLUES_INTERPRETATION_Contemporary_Vernacular.txt"

NUM_TO_WORD = {
    1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE",
    6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE", 10: "TEN",
    11: "ELEVEN", 12: "TWELVE", 13: "THIRTEEN", 14: "FOURTEEN", 15: "FIFTEEN",
    16: "SIXTEEN", 17: "SEVENTEEN", 18: "EIGHTEEN", 19: "NINETEEN", 20: "TWENTY",
    21: "TWENTY-ONE", 22: "TWENTY-TWO", 23: "TWENTY-THREE", 24: "TWENTY-FOUR", 25: "TWENTY-FIVE",
    26: "TWENTY-SIX", 27: "TWENTY-SEVEN", 28: "TWENTY-EIGHT"
}

def extract_interpretation_notes(master_content, chapter_num):
    """Extract interpretation notes from master file."""
    chapter_word = NUM_TO_WORD.get(chapter_num)
    if not chapter_word:
        return None
    
    end_pattern = rf"END OF CHAPTER {chapter_word}:"
    end_match = re.search(end_pattern, master_content)
    
    if not end_match:
        return None
    
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
    
    if notes and len(notes) > 50:
        return notes
    return None

# Read master
print("Reading master file...")
with open(MASTER_FILE, 'r', encoding='utf-8') as f:
    master_content = f.read()

print("\nFixing all optimized chapters - keeping only FIRST '---' marker + chapter notes:\n")

success_count = 0
for chapter_num in range(1, 29):
    print(f"Ch {chapter_num:2d}: ", end="", flush=True)
    
    notes = extract_interpretation_notes(master_content, chapter_num)
    if not notes:
        print("❌ No notes")
        continue
    
    if chapter_num < 10:
        pattern_str = f"{chapter_num:02d}_CHAPTER"
    else:
        pattern_str = f"{chapter_num}_CHAPTER"
    
    opt_files = [f for f in os.listdir(CHAPTERS_DIR) 
                 if pattern_str in f and f.endswith("_OPTIMIZED.txt")]
    
    if not opt_files:
        print("❌ File not found")
        continue
    
    opt_file = os.path.join(CHAPTERS_DIR, opt_files[0])
    
    # Read file
    with open(opt_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find FIRST "---" separator
    first_dash_idx = content.find("\n---\n")
    if first_dash_idx == -1:
        first_dash_idx = content.find("---")
    
    if first_dash_idx == -1:
        print("❌ No '---' marker found")
        continue
    
    # Keep everything up to and including the first "---"
    if content[first_dash_idx:first_dash_idx+5] == "\n---\n":
        clean_content = content[:first_dash_idx+5].rstrip() + '\n'
    else:
        # Handle case where --- is at start or without newlines
        dash_end = content.find("\n", first_dash_idx)
        if dash_end == -1:
            dash_end = len(content)
        clean_content = content[:dash_end].rstrip() + '\n---\n'
    
    # Append notes
    final_content = clean_content + '\n' + notes + '\n'
    
    # Write back
    try:
        with open(opt_file, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"✓")
        success_count += 1
    except Exception as e:
        print(f"❌ {e}")

print(f"\n✅ Fixed: {success_count}/28 chapters")
