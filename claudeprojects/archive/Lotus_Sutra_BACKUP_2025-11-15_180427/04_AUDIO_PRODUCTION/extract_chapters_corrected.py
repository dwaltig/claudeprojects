#!/usr/bin/env python3
"""
CORRECTED CHAPTER EXTRACTION - All 28 chapters with voice tags preserved
Extracts from CHAPTER HEADER (not from voice tags), so all voice tags within chapter are preserved
"""

import re
import os
from pathlib import Path

# Master file path
MASTER_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript_production_v1_english_transliteration_CORRECTED.txt"
OUTPUT_DIR = "/Users/williamaltig/claudeprojects/Lotus_Sutra/audio_production/chapters"

# Chapter header lines (1-indexed) and titles
CHAPTER_MARKERS = [
    (262, "ONE", "THE OPENING"),
    (956, "TWO", "THE LOVING TRICKS"),
    (1917, "THREE", "THE PARABLE"),
    (3495, "FOUR", "FAITH AND UNDERSTANDING"),
    (4094, "FIVE", "THE PARABLE OF THE MEDICINAL HERBS"),
    (4498, "SIX", "THE NAMING"),
    (4874, "SEVEN", "THE PHANTOM CITY BLUES"),
    (5682, "EIGHT", "WHEN THE FIVE HUNDRED FINALLY HEARD THEIR NAMES CALLED"),
    (6019, "NINE", "WHEN THE FAITHFUL GET THEIR DUE"),
    (6211, "TEN", "HONOR THE WORD-CARRIERS"),
    (6567, "ELEVEN", "WHEN THE JEWELED TOWER ROSE UP"),
    (7010, "TWELVE", "WHEN YOUR ENEMY WAS YOUR TEACHER"),
    (7272, "THIRTEEN", "WHEN THE ROAD GETS ROUGH, YOU GOTTA KEEP WALKING"),
    (7587, "FOURTEEN", "HOW TO KEEP YOUR SOUL CLEAN WHEN THE WORLD'S GONE WRONG"),
    (8230, "FIFTEEN", "WHEN THE UNDERGROUND ARMY ROSE UP"),
    (8770, "SIXTEEN", "HOW LONG THE TATHAGATA'S BEEN ALIVE"),
    (9227, "SEVENTEEN", "COUNTING UP THE GRACE"),
    (9709, "EIGHTEEN", "THE JOY THAT MULTIPLIES"),
    (10147, "NINETEEN", "WHEN YOUR SENSES WAKE UP"),
    (10889, "TWENTY", "THE BODHISATTVA WHO NEVER LOOKED DOWN"),
    (11279, "TWENTY-ONE", "WHEN THE LORD SHOWED HIS HAND"),
    (11613, "TWENTY-TWO", "THE PASSING ON"),
    (11828, "TWENTY-THREE", "MEDICINE KING BODHISATTVA - THE STORY OF HOW HE GAVE IT ALL"),
    (12303, "TWENTY-FOUR", "WONDERFUL SOUND BODHISATTVA"),
    (12873, "TWENTY-FIVE", "THE ONE WHO HEARS THE WORLD CRYING"),
    (13551, "TWENTY-SIX", "THE PROTECTION SONGS"),
    (13912, "TWENTY-SEVEN", "THE BEAUTIFUL KING AND HIS GOOD FRIENDS"),
    (14156, "TWENTY-EIGHT", "UNIVERSAL WORTHY COMES TO ENCOURAGE YOU"),
]

# Map chapter words to numbers
WORD_TO_NUM = {
    'ONE': 1, 'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5, 'SIX': 6,
    'SEVEN': 7, 'EIGHT': 8, 'NINE': 9, 'TEN': 10, 'ELEVEN': 11, 'TWELVE': 12,
    'THIRTEEN': 13, 'FOURTEEN': 14, 'FIFTEEN': 15, 'SIXTEEN': 16, 'SEVENTEEN': 17,
    'EIGHTEEN': 18, 'NINETEEN': 19, 'TWENTY': 20, 'TWENTY-ONE': 21, 'TWENTY-TWO': 22,
    'TWENTY-THREE': 23, 'TWENTY-FOUR': 24, 'TWENTY-FIVE': 25, 'TWENTY-SIX': 26,
    'TWENTY-SEVEN': 27, 'TWENTY-EIGHT': 28
}

def extract_chapters():
    """Extract all chapters from CHAPTER HEADER lines with voice tags preserved."""

    print("="*80)
    print("CORRECTED CHAPTER EXTRACTION - Starting from CHAPTER HEADERS")
    print("="*80)
    print()

    # Read entire source file
    print(f"Reading source file: {MASTER_FILE}")
    with open(MASTER_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    print(f"Total lines in source: {len(lines)}")
    print()

    # Create output directory if needed
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    extraction_report = []
    voice_tag_pattern = re.compile(r'^\[([^\]]+)\]$')

    for i, (chapter_line, chapter_word, chapter_title) in enumerate(CHAPTER_MARKERS):
        chapter_num = WORD_TO_NUM[chapter_word]

        print(f"\n--- Chapter {chapter_num}: {chapter_title} ---")

        # Start extraction from CHAPTER HEADER LINE
        start_line = chapter_line - 1  # Convert to 0-indexed

        # Find where this chapter ends (start of next chapter or EOF)
        if i < len(CHAPTER_MARKERS) - 1:
            end_line = CHAPTER_MARKERS[i + 1][0] - 1  # Next chapter header
        else:
            end_line = len(lines)

        # Extract chapter content
        chapter_content = lines[start_line:end_line]

        # Count voice tags in this chapter
        voice_tags = []
        for line in chapter_content:
            match = voice_tag_pattern.match(line.strip())
            if match:
                voice_tags.append(match.group(1))

        # Track unique speakers
        unique_speakers = sorted(set(voice_tags))

        print(f"Lines extracted: {start_line + 1} to {end_line}")
        print(f"Total voice tags found: {len(voice_tags)}")
        print(f"Unique speakers: {', '.join(unique_speakers) if unique_speakers else 'NONE'}")

        # Check first voice tag position
        first_tag_line = None
        for j, line in enumerate(chapter_content[:20]):  # Check first 20 lines
            if voice_tag_pattern.match(line.strip()):
                first_tag_line = j + 1
                first_tag = line.strip()
                print(f"First voice tag at line {first_tag_line} of chapter: {first_tag}")
                break

        if first_tag_line is None:
            print(f"⚠ WARNING: No voice tags found in first 20 lines")

        # Create filename
        chapter_num_str = f"{chapter_num:02d}"
        # Clean title for filename
        clean_title = re.sub(r'[^\w\s-]', '', chapter_title)
        clean_title = re.sub(r'\s+', '_', clean_title.strip())
        filename = f"{chapter_num_str}_CHAPTER_{clean_title}.txt"
        filepath = os.path.join(OUTPUT_DIR, filename)

        # Write chapter file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(chapter_content)

        print(f"Saved to: {filename}")

        extraction_report.append({
            "chapter": chapter_num,
            "title": chapter_title,
            "filename": filename,
            "voice_tag_count": len(voice_tags),
            "unique_speakers": unique_speakers,
            "line_count": len(chapter_content),
            "first_tag_line": first_tag_line
        })

    # Generate summary report
    print("\n" + "="*80)
    print("EXTRACTION COMPLETE - SUMMARY REPORT")
    print("="*80)
    print()

    total_tags = sum(r["voice_tag_count"] for r in extraction_report)

    print(f"Total chapters extracted: {len(extraction_report)}")
    print(f"Total voice tags across all chapters: {total_tags}")
    print()

    print("CHAPTER-BY-CHAPTER BREAKDOWN:")
    print("-" * 80)

    for report in extraction_report:
        first_tag_info = f"1st tag @ line {report['first_tag_line']}" if report['first_tag_line'] else "NO TAGS IN FIRST 20 LINES"
        speakers = ', '.join(report["unique_speakers"][:4]) if report["unique_speakers"] else "NONE"
        if len(report["unique_speakers"]) > 4:
            speakers += f"... (+{len(report['unique_speakers']) - 4})"

        print(f"Ch {report['chapter']:2d}: {report['voice_tag_count']:3d} tags | "
              f"{len(report['unique_speakers']):2d} speakers | {report['line_count']:4d} lines | "
              f"{first_tag_info}")

    print()
    print("UNIQUE SPEAKERS BY CHAPTER:")
    print("-" * 80)

    for report in extraction_report:
        speakers = ", ".join(report["unique_speakers"]) if report["unique_speakers"] else "NONE"
        print(f"Chapter {report['chapter']:2d}: {speakers}")

    print()
    print("="*80)

    return extraction_report, total_tags

if __name__ == "__main__":
    print("Starting corrected chapter extraction with voice tag preservation...")
    print()
    results, total_tags = extract_chapters()
    print()
    print(f"✓ SUCCESS: All 28 chapters extracted with {total_tags} voice tags preserved")
