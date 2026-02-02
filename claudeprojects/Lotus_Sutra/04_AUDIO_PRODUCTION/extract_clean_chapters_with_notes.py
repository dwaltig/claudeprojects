#!/usr/bin/env python3
"""
Extract clean chapters from master file, ensuring perfect alignment.
Each chapter gets optimized verses + interpretation notes.
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

# Read master file
print("Reading master file...")
with open(MASTER_FILE, 'r', encoding='utf-8') as f:
    master_content = f.read()

print("Extracting and aligning all 28 chapters...\n")

success_count = 0
for chapter_num in range(1, 29):
    chapter_word = NUM_TO_WORD.get(chapter_num)
    
    # Find chapter start
    start_pattern = rf"CHAPTER {chapter_word}:"
    start_match = re.search(start_pattern, master_content)
    
    if not start_match:
        print(f"Ch {chapter_num:2d}: ❌ Start marker not found")
        continue
    
    start_pos = start_match.start()
    
    # Find chapter end (the "END OF CHAPTER X:" marker)
    end_pattern = rf"END OF CHAPTER {chapter_word}:"
    end_match = re.search(end_pattern, master_content[start_pos:])
    
    if not end_match:
        print(f"Ch {chapter_num:2d}: ❌ End marker not found")
        continue
    
    end_pos = start_pos + end_match.end()
    
    # Extract the chapter content (from CHAPTER header to END marker)
    chapter_content = master_content[start_pos:end_pos]
    
    # Now extract interpretation notes (from after END marker to next CHAPTER or EOF)
    notes_start = end_pos
    next_chapter_num = chapter_num + 1
    next_chapter_word = NUM_TO_WORD.get(next_chapter_num)
    
    if next_chapter_word:
        next_chapter_pattern = rf"CHAPTER {next_chapter_word}:"
        next_match = re.search(next_chapter_pattern, master_content[notes_start:])
        if next_match:
            notes_content = master_content[notes_start:notes_start + next_match.start()].strip()
        else:
            notes_content = master_content[notes_start:].strip()
    else:
        notes_content = master_content[notes_start:].strip()
    
    # Build the output file
    final_output = chapter_content + "\n\n" + notes_content + "\n"
    
    # Create filename
    # Extract chapter title from first line
    first_line = chapter_content.split('\n')[0]  # Get "CHAPTER X: TITLE"
    chapter_title = first_line.replace("CHAPTER ", "").replace(f"{chapter_word}: ", "").upper()
    chapter_title = chapter_title.replace(" ", "_")
    
    if chapter_num < 10:
        output_filename = f"{chapter_num:02d}_CHAPTER_{chapter_title}_OPTIMIZED.txt"
    else:
        output_filename = f"{chapter_num}_CHAPTER_{chapter_title}_OPTIMIZED.txt"
    
    output_path = os.path.join(CHAPTERS_DIR, output_filename)
    
    # Write the file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_output)
        
        # Count lines and words as verification
        content_lines = chapter_content.count('\n')
        content_words = len(chapter_content.split())
        
        print(f"Ch {chapter_num:2d}: ✓ ({content_lines} lines, {content_words} words)")
        success_count += 1
    except Exception as e:
        print(f"Ch {chapter_num:2d}: ❌ {e}")

print(f"\n✅ SUCCESS: {success_count}/28 chapters extracted and aligned with master file")
print(f"\nAll files saved to: {CHAPTERS_DIR}")
