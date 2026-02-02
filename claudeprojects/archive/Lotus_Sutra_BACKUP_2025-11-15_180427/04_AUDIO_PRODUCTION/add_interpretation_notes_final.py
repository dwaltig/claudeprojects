#!/usr/bin/env python3
"""
Add interpretation notes from master file to optimized chapters.
"""

import os
import re

MASTER_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/00_MASTER_VERSIONS/LS_final_version/02_BLUES_INTERPRETATION_Contemporary_Vernacular.txt"
CHAPTERS_DIR = "/Users/williamaltig/claudeprojects/Lotus_Sutra/04_AUDIO_PRODUCTION/chapters"

# Map numbers to words
NUM_TO_WORD = {
    1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE",
    6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE", 10: "TEN",
    11: "ELEVEN", 12: "TWELVE", 13: "THIRTEEN", 14: "FOURTEEN", 15: "FIFTEEN",
    16: "SIXTEEN", 17: "SEVENTEEN", 18: "EIGHTEEN", 19: "NINETEEN", 20: "TWENTY",
    21: "TWENTY-ONE", 22: "TWENTY-TWO", 23: "TWENTY-THREE", 24: "TWENTY-FOUR", 25: "TWENTY-FIVE",
    26: "TWENTY-SIX", 27: "TWENTY-SEVEN", 28: "TWENTY-EIGHT"
}

def extract_interpretation_notes(master_content, chapter_num):
    """
    Extract interpretation notes for a chapter from master file.
    Master file uses "END OF CHAPTER ONE:", "END OF CHAPTER TWO:", etc.
    """
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
            # This shouldn't happen unless we're on the last chapter
            notes = master_content[end_pos:].strip()
    else:
        # Last chapter (28)
        notes = master_content[end_pos:].strip()
    
    # Filter out the next chapter's header if it got included
    lines = notes.split('\n')
    filtered_lines = []
    for line in lines:
        if line.startswith("END OF CHAPTER"):
            break
        filtered_lines.append(line)
    
    notes = '\n'.join(filtered_lines).strip()
    
    if notes and len(notes) > 50:  # Must have meaningful content
        return notes
    return None

def find_chapter_file(chapter_num):
    """Find the optimized chapter file for a given chapter number."""
    if chapter_num < 10:
        pattern_str = f"{chapter_num:02d}_CHAPTER"
    else:
        pattern_str = f"{chapter_num}_CHAPTER"
    
    for fname in os.listdir(CHAPTERS_DIR):
        if pattern_str in fname and fname.endswith("_OPTIMIZED.txt"):
            return os.path.join(CHAPTERS_DIR, fname)
    
    return None

def add_notes_to_chapter(chapter_file, interpretation_notes):
    """
    Append interpretation notes to the end of an optimized chapter file.
    """
    if not interpretation_notes:
        return False
    
    try:
        with open(chapter_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add the notes at the end
        content_with_notes = content.rstrip() + "\n\n" + interpretation_notes.strip() + "\n"
        
        with open(chapter_file, 'w', encoding='utf-8') as f:
            f.write(content_with_notes)
        
        return True
    except Exception as e:
        print(f"Error processing {chapter_file}: {e}")
        return False

# Read master file
print("Reading master file...")
with open(MASTER_FILE, 'r', encoding='utf-8') as f:
    master_content = f.read()

# Process all 28 chapters
success_count = 0
failed_chapters = []

for chapter_num in range(1, 29):
    print(f"Ch {chapter_num:2d}: ", end="", flush=True)
    
    # Extract interpretation notes from master
    notes = extract_interpretation_notes(master_content, chapter_num)
    
    if not notes:
        print("❌ No notes")
        failed_chapters.append(chapter_num)
        continue
    
    # Find the optimized chapter file
    chapter_file = find_chapter_file(chapter_num)
    
    if not chapter_file:
        print("❌ File not found")
        failed_chapters.append(chapter_num)
        continue
    
    if add_notes_to_chapter(chapter_file, notes):
        print(f"✓ ({len(notes)} chars)")
        success_count += 1
    else:
        print("❌ Failed to write")
        failed_chapters.append(chapter_num)

print(f"\n✅ SUCCESS: {success_count}/28 chapters updated")
if failed_chapters:
    print(f"⚠️  Failed: Chapters {failed_chapters}")
else:
    print("🎉 All chapters updated successfully!")
