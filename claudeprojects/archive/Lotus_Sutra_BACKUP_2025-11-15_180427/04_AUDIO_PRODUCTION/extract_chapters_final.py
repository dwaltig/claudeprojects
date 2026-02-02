#!/usr/bin/env python3
"""
FINAL CORRECTED CHAPTER EXTRACTION
Extracts all 28 chapters WITH ALL VOICE TAGS PRESERVED
- For chapters with voice tags BEFORE chapter header: starts from voice tag
- For chapters with voice tags AFTER chapter header: starts from chapter header
"""

import re
import os
from pathlib import Path

# Master file path
MASTER_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript_production_v1_english_transliteration_CORRECTED.txt"
OUTPUT_DIR = "/Users/williamaltig/claudeprojects/Lotus_Sutra/audio_production/chapters"

# Chapter definitions: (chapter_num, start_line, chapter_header_line, title)
# start_line = voice tag line if before header, or chapter header line if voice tag is after
CHAPTER_MARKERS = [
    (1, 260, 262, "THE OPENING"),  # [Charon] at 260, CHAPTER at 262
    (2, 956, 956, "THE LOVING TRICKS"),  # CHAPTER at 956, [Iapetus] at 962
    (3, 1916, 1917, "THE PARABLE"),  # [Charon] at 1916, CHAPTER at 1917
    (4, 3495, 3495, "FAITH AND UNDERSTANDING"),  # CHAPTER at 3495, [Vulcan] at 3503
    (5, 4094, 4094, "THE PARABLE OF THE MEDICINAL HERBS"),  # CHAPTER at 4094, [Iapetus] at 4103
    (6, 4497, 4498, "THE NAMING"),  # [Charon] at 4497, CHAPTER at 4498
    (7, 4874, 4874, "THE PHANTOM CITY BLUES"),  # CHAPTER at 4874, [Iapetus] at 4895
    (8, 5681, 5682, "WHEN THE FIVE HUNDRED FINALLY HEARD THEIR NAMES CALLED"),  # [Charon] at 5681, CHAPTER at 5682
    (9, 6019, 6019, "WHEN THE FAITHFUL GET THEIR DUE"),  # CHAPTER at 6019, [Rasalgethi] at 6144
    (10, 6210, 6211, "HONOR THE WORD-CARRIERS"),  # [Charon] at 6210, CHAPTER at 6211
    (11, 6567, 6567, "WHEN THE JEWELED TOWER ROSE UP"),  # CHAPTER at 6567, [Rasalgethi] at 6581
    (12, 7010, 7010, "WHEN YOUR ENEMY WAS YOUR TEACHER"),  # CHAPTER at 7010, [Rasalgethi] at 7016
    (13, 7271, 7272, "WHEN THE ROAD GETS ROUGH, YOU GOTTA KEEP WALKING"),  # [Charon] at 7271, CHAPTER at 7272
    (14, 7587, 7587, "HOW TO KEEP YOUR SOUL CLEAN WHEN THE WORLD'S GONE WRONG"),  # CHAPTER at 7587, [Iapetus] at 7603
    (15, 8230, 8230, "WHEN THE UNDERGROUND ARMY ROSE UP"),  # CHAPTER at 8230, [Orus] at 8293
    (16, 8769, 8770, "HOW LONG THE TATHAGATA'S BEEN ALIVE"),  # [Charon] at 8769, CHAPTER at 8770
    (17, 9208, 9227, "COUNTING UP THE GRACE"),  # [Charon] at 9208, CHAPTER at 9227
    (18, 9709, 9709, "THE JOY THAT MULTIPLIES"),  # CHAPTER at 9709, [Charon] at 9718
    (19, 10129, 10147, "WHEN YOUR SENSES WAKE UP"),  # [Charon] at 10129, CHAPTER at 10147
    (20, 10889, 10889, "THE BODHISATTVA WHO NEVER LOOKED DOWN"),  # CHAPTER at 10889, [Iapetus] at 10896
    (21, 11279, 11279, "WHEN THE LORD SHOWED HIS HAND"),  # CHAPTER at 11279, [Orus] at 11292
    (22, 11613, 11613, "THE PASSING ON"),  # CHAPTER at 11613, [Iapetus] at 11779
    (23, 11828, 11828, "MEDICINE KING BODHISATTVA - THE STORY OF HOW HE GAVE IT ALL"),  # CHAPTER at 11828, [Iapetus] at 11843
    (24, 12303, 12303, "WONDERFUL SOUND BODHISATTVA"),  # CHAPTER at 12303, [Iapetus] at 12435
    (25, 12873, 12873, "THE ONE WHO HEARS THE WORLD CRYING"),  # CHAPTER at 12873, [Charon] at 12876
    (26, 13550, 13551, "THE PROTECTION SONGS"),  # [Charon] at 13550, CHAPTER at 13551
    (27, 13912, 13912, "THE BEAUTIFUL KING AND HIS GOOD FRIENDS"),  # CHAPTER at 13912, [Sulafat] at 13924
    (28, 14156, 14156, "UNIVERSAL WORTHY COMES TO ENCOURAGE YOU"),  # CHAPTER at 14156, [Rasalgethi] at 14166
]

def extract_chapters():
    """Extract all 28 chapters with ALL voice tags preserved."""

    print("="*90)
    print("FINAL CHAPTER EXTRACTION - All Voice Tags Preserved")
    print("="*90)
    print()

    # Read entire source file
    with open(MASTER_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    print(f"Source file: {len(lines)} lines")
    print()

    # Create output directory if needed
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    extraction_report = []
    voice_tag_pattern = re.compile(r'^\[([^\]]+)\]$')

    for i, (chapter_num, start_line, chapter_header_line, chapter_title) in enumerate(CHAPTER_MARKERS):

        print(f"Chapter {chapter_num:2d}: {chapter_title[:50]}")

        # Start extraction from start_line (which may be voice tag or chapter header)
        start_idx = start_line - 1  # Convert to 0-indexed

        # Find where this chapter ends
        if i < len(CHAPTER_MARKERS) - 1:
            end_idx = CHAPTER_MARKERS[i + 1][1] - 1  # Start line of next chapter
        else:
            end_idx = len(lines)

        # Extract chapter content
        chapter_content = lines[start_idx:end_idx]

        # Count voice tags
        voice_tags = []
        for line in chapter_content:
            match = voice_tag_pattern.match(line.strip())
            if match:
                voice_tags.append(match.group(1))

        unique_speakers = sorted(set(voice_tags))

        # Check first line
        first_line = chapter_content[0].strip() if chapter_content else ""
        starts_with_voice_tag = bool(voice_tag_pattern.match(first_line))

        # Check if chapter header is included
        has_chapter_header = any("CHAPTER" in line for line in chapter_content[:30])

        # Create filename
        clean_title = re.sub(r'[^\w\s-]', '', chapter_title)
        clean_title = re.sub(r'\s+', '_', clean_title.strip())
        filename = f"{chapter_num:02d}_CHAPTER_{clean_title}.txt"
        filepath = os.path.join(OUTPUT_DIR, filename)

        # Write chapter file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(chapter_content)

        status = "✓" if starts_with_voice_tag or has_chapter_header else "✗"
        print(f"  {status} Lines {start_line}-{end_idx}: {len(voice_tags)} tags, {len(unique_speakers)} speakers")
        print(f"     First line: {first_line[:60]}")
        print(f"     Speakers: {', '.join(unique_speakers) if unique_speakers else 'NONE'}")

        extraction_report.append({
            "chapter": chapter_num,
            "title": chapter_title,
            "filename": filename,
            "voice_tag_count": len(voice_tags),
            "unique_speakers": unique_speakers,
            "line_count": len(chapter_content),
            "starts_with_voice_tag": starts_with_voice_tag,
            "has_chapter_header": has_chapter_header
        })

    # Generate summary
    print("\n" + "="*90)
    print("EXTRACTION SUMMARY")
    print("="*90)

    total_tags = sum(r["voice_tag_count"] for r in extraction_report)
    chapters_with_voice_start = sum(1 for r in extraction_report if r["starts_with_voice_tag"])

    print(f"\nTotal chapters: {len(extraction_report)}")
    print(f"Total voice tags: {total_tags}")
    print(f"Chapters starting with voice tag: {chapters_with_voice_start}/{len(extraction_report)}")
    print()

    # Check for issues
    issues = []
    for r in extraction_report:
        if r["voice_tag_count"] == 0:
            issues.append(f"Chapter {r['chapter']} has ZERO voice tags")
        if not r["has_chapter_header"]:
            issues.append(f"Chapter {r['chapter']} missing CHAPTER header")

    if issues:
        print("ISSUES FOUND:")
        for issue in issues:
            print(f"  ⚠ {issue}")
    else:
        print("✓ ALL QUALITY CHECKS PASSED")

    # Save detailed report
    report_file = os.path.join(OUTPUT_DIR, "EXTRACTION_REPORT_FINAL.txt")
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("LOTUS SUTRA CHAPTER EXTRACTION REPORT\n")
        f.write("="*90 + "\n\n")
        f.write(f"Total chapters: {len(extraction_report)}\n")
        f.write(f"Total voice tags: {total_tags}\n\n")

        for r in extraction_report:
            f.write(f"\nChapter {r['chapter']:2d}: {r['title']}\n")
            f.write(f"  File: {r['filename']}\n")
            f.write(f"  Voice tags: {r['voice_tag_count']}\n")
            f.write(f"  Unique speakers: {len(r['unique_speakers'])}\n")
            f.write(f"  Speakers: {', '.join(r['unique_speakers']) if r['unique_speakers'] else 'NONE'}\n")
            f.write(f"  Starts with voice tag: {'YES' if r['starts_with_voice_tag'] else 'NO'}\n")
            f.write(f"  Lines: {r['line_count']}\n")

    print(f"\nDetailed report saved: {report_file}")
    print("\n" + "="*90)

    return extraction_report, total_tags

if __name__ == "__main__":
    results, total_tags = extract_chapters()
    print(f"\n✓ SUCCESS: All 28 chapters extracted with {total_tags} voice tags preserved\n")
