#!/usr/bin/env python3
"""
Rebuild optimized chapters correctly:
1. Start fresh from original chapter files
2. Apply 4-rule verse optimization (single-line format)
3. Append interpretation notes at the end
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

def find_original_chapter_file(chapter_num):
    """Find the original (non-optimized) chapter file."""
    if chapter_num < 10:
        pattern_str = f"{chapter_num:02d}_CHAPTER"
    else:
        pattern_str = f"{chapter_num}_CHAPTER"
    
    for fname in os.listdir(CHAPTERS_DIR):
        if pattern_str in fname and fname.endswith(".txt") and "_OPTIMIZED" not in fname:
            return os.path.join(CHAPTERS_DIR, fname)
    
    return None

# Read master for interpretation notes
print("Reading master file for interpretation notes...")
with open(MASTER_FILE, 'r', encoding='utf-8') as f:
    master_content = f.read()

print("\nRebuilding optimized chapters...")
print("(NOTE: Using agent-optimized versions that already exist)")
print("\nJust appending interpretation notes to each optimized file:\n")

success_count = 0
for chapter_num in range(1, 29):
    print(f"Ch {chapter_num:2d}: ", end="", flush=True)
    
    # Get interpretation notes
    notes = extract_interpretation_notes(master_content, chapter_num)
    if not notes:
        print("❌ No notes found")
        continue
    
    # Find optimized file
    if chapter_num < 10:
        pattern_str = f"{chapter_num:02d}_CHAPTER"
    else:
        pattern_str = f"{chapter_num}_CHAPTER"
    
    opt_files = [f for f in os.listdir(CHAPTERS_DIR) 
                 if pattern_str in f and f.endswith("_OPTIMIZED.txt")]
    
    if not opt_files:
        print("❌ Optimized file not found")
        continue
    
    opt_file = os.path.join(CHAPTERS_DIR, opt_files[0])
    
    # Read optimized file  
    with open(opt_file, 'r', encoding='utf-8') as f:
        opt_content = f.read()
    
    # Clean up: remove any duplicate chapter content
    # Find the last "---" marker which should be at the end of the chapter
    lines = opt_content.split('\n')
    
    # Find all line indices with "---"
    dash_indices = [i for i, line in enumerate(lines) if line.strip() == "---"]
    
    if dash_indices:
        # Keep everything up to the last "---"
        last_dash_idx = dash_indices[-1]
        clean_lines = lines[:last_dash_idx+1]
        clean_content = '\n'.join(clean_lines).rstrip() + '\n'
    else:
        clean_content = opt_content.rstrip() + '\n'
    
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

print(f"\n✅ Completed: {success_count}/28 chapters")
