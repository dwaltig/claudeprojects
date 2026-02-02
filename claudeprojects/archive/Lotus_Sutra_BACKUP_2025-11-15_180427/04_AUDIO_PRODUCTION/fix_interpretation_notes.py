#!/usr/bin/env python3
"""
Fix interpretation notes placement - they should be appended AFTER all chapter content.
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

def extract_interpretation_notes(master_content, chapter_num):
    """Extract interpretation notes for a chapter."""
    chapter_word = NUM_TO_WORD.get(chapter_num)
    if not chapter_word:
        return None
    
    # Find the end marker for this chapter
    end_pattern = rf"END OF CHAPTER {chapter_word}:"
    end_match = re.search(end_pattern, master_content)
    
    if not end_match:
        return None
    
    end_pos = end_match.end()
    
    # Find the next chapter marker
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
        # Last chapter
        notes = master_content[end_pos:].strip()
    
    if notes and len(notes) > 50:
        return notes
    return None

def find_chapter_file(chapter_num):
    """Find the optimized chapter file."""
    if chapter_num < 10:
        pattern_str = f"{chapter_num:02d}_CHAPTER"
    else:
        pattern_str = f"{chapter_num}_CHAPTER"
    
    for fname in os.listdir(CHAPTERS_DIR):
        if pattern_str in fname and fname.endswith("_OPTIMIZED.txt"):
            return os.path.join(CHAPTERS_DIR, fname)
    
    return None

# Read master file
print("Reading master file...")
with open(MASTER_FILE, 'r', encoding='utf-8') as f:
    master_content = f.read()

# Process all 28 chapters
success_count = 0
for chapter_num in range(1, 29):
    print(f"Ch {chapter_num:2d}: ", end="", flush=True)
    
    notes = extract_interpretation_notes(master_content, chapter_num)
    if not notes:
        print("❌ No notes")
        continue
    
    chapter_file = find_chapter_file(chapter_num)
    if not chapter_file:
        print("❌ File not found")
        continue
    
    # Read current file
    with open(chapter_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove any interpretation notes that might already be there (from previous attempts)
    # This handles files that have duplicate/misplaced notes
    content_clean = content
    
    # Find where "INTERPRETATION NOTES:" might appear and remove everything after "---" that contains it
    # Actually, just ensure we end at the last "---" that marks end of chapter content
    if "---" in content:
        # Split on the last occurrence of --- in the main content area
        parts = content.rsplit("---", 1)
        content_clean = parts[0] + "---"
    
    # Ensure content ends properly
    content_clean = content_clean.rstrip() + "\n"
    
    # Now append the notes
    final_content = content_clean + "\n" + notes + "\n"
    
    # Write back
    try:
        with open(chapter_file, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"✓")
        success_count += 1
    except Exception as e:
        print(f"❌ Error: {e}")

print(f"\n✅ Fixed: {success_count}/28 chapters")
