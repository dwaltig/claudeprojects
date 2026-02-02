#!/usr/bin/env python3
"""
Add interpretation notes from master file to optimized chapters.
"""

import os
import re

MASTER_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/00_MASTER_VERSIONS/LS_final_version/02_BLUES_INTERPRETATION_Contemporary_Vernacular.txt"
CHAPTERS_DIR = "/Users/williamaltig/claudeprojects/Lotus_Sutra/04_AUDIO_PRODUCTION/chapters"

def extract_interpretation_notes(master_content, chapter_num):
    """
    Extract interpretation notes for a chapter from master file.
    Notes appear after "END OF CHAPTER X: TITLE" and before "CHAPTER X+1:"
    """
    # Find the end marker - it looks like "END OF CHAPTER 1: THE OPENING"
    end_pattern = rf"END OF CHAPTER {chapter_num}[^:]*:[^\n]*"
    end_match = re.search(end_pattern, master_content, re.IGNORECASE)
    
    if not end_match:
        return None
    
    end_pos = end_match.end()
    
    # Now find the next chapter marker
    next_chapter = chapter_num + 1
    next_pattern = rf"CHAPTER {next_chapter}[^:]*:"
    next_match = re.search(next_pattern, master_content[end_pos:], re.IGNORECASE)
    
    if next_match:
        # Get everything between end of current chapter and start of next
        notes = master_content[end_pos:end_pos + next_match.start()].strip()
    else:
        # Last chapter - get everything to the end
        notes = master_content[end_pos:].strip()
    
    if notes and len(notes) > 100:  # Must have meaningful content
        return notes
    return None

def find_chapter_file(chapter_num):
    """Find the optimized chapter file for a given chapter number."""
    # Format the search pattern
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
    print(f"❌ Failed: Chapters {failed_chapters}")
