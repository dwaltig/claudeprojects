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
    Notes appear after "END OF CHAPTER X:" and before "CHAPTER X+1:"
    """
    # First find the end marker for this chapter
    end_pattern = rf"END OF CHAPTER {chapter_num}[^:]*:"
    end_match = re.search(end_pattern, master_content)
    
    if not end_match:
        return None
    
    end_pos = end_match.end()
    
    # Now find the next chapter marker
    next_chapter = chapter_num + 1
    next_pattern = rf"\nCHAPTER {next_chapter}[^:]*:"
    next_match = re.search(next_pattern, master_content[end_pos:])
    
    if next_match:
        notes = master_content[end_pos:end_pos + next_match.start()].strip()
    else:
        # Last chapter - get everything to the end
        notes = master_content[end_pos:].strip()
    
    if notes:
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
for chapter_num in range(1, 29):
    print(f"Processing Chapter {chapter_num}...", end=" ")
    
    # Extract interpretation notes from master
    notes = extract_interpretation_notes(master_content, chapter_num)
    
    if not notes:
        print("No notes found")
        continue
    
    # Find the optimized chapter file
    # Look for files with the pattern XX_CHAPTER*OPTIMIZED.txt
    pattern_str = f"{chapter_num:02d}_CHAPTER" if chapter_num < 10 else f"{chapter_num}_CHAPTER"
    optimized_files = [f for f in os.listdir(CHAPTERS_DIR) 
                       if pattern_str in f and f.endswith("_OPTIMIZED.txt")]
    
    if not optimized_files:
        print(f"No file found for pattern {pattern_str}")
        continue
    
    chapter_file = os.path.join(CHAPTERS_DIR, optimized_files[0])
    
    if add_notes_to_chapter(chapter_file, notes):
        print(f"✓ Added {len(notes)} chars")
        success_count += 1
    else:
        print("Failed")

print(f"\n✅ Completed: {success_count} chapters updated with interpretation notes")
