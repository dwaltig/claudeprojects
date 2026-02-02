#!/usr/bin/env python3
"""
Add interpretation notes from master file to optimized chapters.
"""

import os
import re

# Path to master file and chapters directory
MASTER_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/00_MASTER_VERSIONS/LS_final_version/02_BLUES_INTERPRETATION_Contemporary_Vernacular.txt"
CHAPTERS_DIR = "/Users/williamaltig/claudeprojects/Lotus_Sutra/04_AUDIO_PRODUCTION/chapters"

def extract_interpretation_notes(master_content, chapter_num):
    """
    Extract interpretation notes for a chapter from master file.
    Notes appear after "END OF CHAPTER X" and before the next chapter title.
    """
    # Format chapter number with leading zero
    chapter_title = f"CHAPTER {chapter_num:02d}" if chapter_num < 10 else f"CHAPTER {chapter_num}"
    
    # Look for the end marker for this chapter
    pattern = rf"END OF CHAPTER {chapter_num}[^\n]*\n\n(.*?)(?=CHAPTER|$)"
    
    match = re.search(pattern, master_content, re.DOTALL | re.IGNORECASE)
    
    if match:
        notes = match.group(1).strip()
        # Don't include the next chapter title if it snuck in
        if notes.startswith("CHAPTER"):
            notes = ""
        return notes
    
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
        content_with_notes = content.rstrip() + "\n\n" + interpretation_notes + "\n"
        
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
for chapter_num in range(1, 29):
    # Skip chapter 10 initially, will handle separately
    print(f"Processing Chapter {chapter_num}...", end=" ")
    
    # Extract interpretation notes from master
    notes = extract_interpretation_notes(master_content, chapter_num)
    
    if not notes:
        print("No interpretation notes found")
        continue
    
    # Find the optimized chapter file
    optimized_files = [f for f in os.listdir(CHAPTERS_DIR) 
                       if f.endswith("_OPTIMIZED.txt") and f.startswith(f"{chapter_num:02d}") or f.startswith(f"{chapter_num}_")]
    
    if not optimized_files:
        print(f"No optimized file found")
        continue
    
    chapter_file = os.path.join(CHAPTERS_DIR, optimized_files[0])
    
    if add_notes_to_chapter(chapter_file, notes):
        print(f"✓ Added {len(notes)} chars of notes")
        success_count += 1
    else:
        print("Failed")

print(f"\nCompleted: {success_count} chapters updated with interpretation notes")
