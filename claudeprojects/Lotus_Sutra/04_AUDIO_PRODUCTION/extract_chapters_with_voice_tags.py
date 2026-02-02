#!/usr/bin/env python3
"""
Extract all 28 chapters from the master manuscript WITH voice tags intact.
This script ensures compassionate attention to every voice tag detail.
"""

import re
import os
from pathlib import Path

# Master file path
MASTER_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript_production_v1_english_transliteration_CORRECTED.txt"
OUTPUT_DIR = "/Users/williamaltig/claudeprojects/Lotus_Sutra/audio_production/chapters"

# Chapter boundaries WITH VOICE TAG LINES
# Format: (chapter_line, voice_tag_line, title)
CHAPTER_MARKERS = [
    (262, 260, "CHAPTER ONE: THE OPENING"),
    (956, 962, "CHAPTER TWO: THE LOVING TRICKS"),
    (1917, 1909, "CHAPTER THREE: THE PARABLE"),
    (3495, 3503, "CHAPTER FOUR: FAITH AND UNDERSTANDING"),
    (4094, 4103, "CHAPTER FIVE: THE PARABLE OF THE MEDICINAL HERBS"),
    (4498, 4504, "CHAPTER SIX: THE NAMING"),
    (4874, 4895, "CHAPTER SEVEN: THE PHANTOM CITY BLUES"),
    (5682, 5703, "CHAPTER EIGHT: WHEN THE FIVE HUNDRED FINALLY HEARD THEIR NAMES CALLED"),
    (6019, 6144, "CHAPTER NINE: WHEN THE FAITHFUL GET THEIR DUE"),
    (6211, 6231, "CHAPTER TEN: HONOR THE WORD-CARRIERS"),
    (6567, 6581, "CHAPTER ELEVEN: WHEN THE JEWELED TOWER ROSE UP"),
    (7010, 7016, "CHAPTER TWELVE: WHEN YOUR ENEMY WAS YOUR TEACHER"),
    (7272, 7297, "CHAPTER THIRTEEN: WHEN THE ROAD GETS ROUGH, YOU GOTTA KEEP WALKING"),
    (7587, 7603, "CHAPTER FOURTEEN: HOW TO KEEP YOUR SOUL CLEAN WHEN THE WORLD'S GONE WRONG"),
    (8230, 8293, "CHAPTER FIFTEEN: WHEN THE UNDERGROUND ARMY ROSE UP"),
    (8770, 8779, "CHAPTER SIXTEEN: HOW LONG THE TATHAGATA'S BEEN ALIVE"),
    (9227, 9238, "CHAPTER SEVENTEEN: COUNTING UP THE GRACE"),
    (9709, 9718, "CHAPTER EIGHTEEN: THE JOY THAT MULTIPLIES"),
    (10147, 10157, "CHAPTER NINETEEN: WHEN YOUR SENSES WAKE UP"),
    (10889, 10896, "CHAPTER TWENTY: THE BODHISATTVA WHO NEVER LOOKED DOWN"),
    (11279, 11292, "CHAPTER TWENTY-ONE: WHEN THE LORD SHOWED HIS HAND"),
    (11613, 11779, "CHAPTER TWENTY-TWO: THE PASSING ON"),
    (11828, 11843, "CHAPTER TWENTY-THREE: MEDICINE KING BODHISATTVA - THE STORY OF HOW HE GAVE IT ALL"),
    (12303, 12435, "CHAPTER TWENTY-FOUR: WONDERFUL SOUND BODHISATTVA"),
    (12873, 12876, "CHAPTER TWENTY-FIVE: THE ONE WHO HEARS THE WORLD CRYING"),
    (13551, 13561, "CHAPTER TWENTY-SIX: THE PROTECTION SONGS"),
    (13912, 13924, "CHAPTER TWENTY-SEVEN: THE BEAUTIFUL KING AND HIS GOOD FRIENDS"),
    (14156, 14166, "CHAPTER TWENTY-EIGHT: UNIVERSAL WORTHY COMES TO ENCOURAGE YOU"),
]

# All voice tags to track
VOICE_TAGS = [
    'Charon', 'Orus', 'Puck', 'Orion', 'Iapetus', 'Rasalgethi',
    'Sulafat', 'Jove', 'Vulcan', 'Triton', 'Zubenelgenubi',
    'Sadaltager', 'Leda', 'Lyra', 'Aoede'
]

def extract_chapters():
    """Extract all chapters with voice tags intact."""

    print("Reading master file...")
    with open(MASTER_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    print(f"Total lines in master file: {total_lines}")

    # Create output directory if needed
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    results = []
    total_voice_tags = 0

    for i, (chapter_line, voice_tag_line, title) in enumerate(CHAPTER_MARKERS):
        # CRITICAL: Start extraction from VOICE TAG, not chapter header
        start_line = voice_tag_line

        # Determine end line (voice tag of next chapter or end of file)
        if i + 1 < len(CHAPTER_MARKERS):
            # End at the voice tag line of the NEXT chapter
            end_line = CHAPTER_MARKERS[i + 1][1]
        else:
            # Last chapter - go to end of file
            end_line = total_lines + 1

        # Extract chapter content (convert to 0-indexed)
        chapter_lines = lines[start_line - 1:end_line - 1]
        chapter_text = ''.join(chapter_lines)

        # Count voice tags in this chapter
        voice_tag_count = sum(chapter_text.count(f'[{tag}]') for tag in VOICE_TAGS)

        # Get list of unique voices used
        voices_used = sorted(set(tag for tag in VOICE_TAGS if f'[{tag}]' in chapter_text))

        # CRITICAL: Verify chapter starts with a voice tag
        first_line = chapter_lines[0].strip() if chapter_lines else ""
        starts_with_voice_tag = bool(re.match(r'^\[[^\]]+\]$', first_line))

        # Check for Chinese characters
        chinese_char_count = len(re.findall(r'[\u4e00-\u9fff]', chapter_text))

        # Determine chapter number and filename
        chapter_num = i + 1

        # Create filename from title
        title_upper = title.replace("CHAPTER ", "").replace(":", "")
        if title_upper.startswith("ONE"):
            title_upper = "THE OPENING"
        elif title_upper.startswith("TWO"):
            title_upper = "THE LOVING TRICKS"
        elif title_upper.startswith("THREE"):
            title_upper = "THE PARABLE"
        elif title_upper.startswith("FOUR"):
            title_upper = "FAITH AND UNDERSTANDING"
        elif title_upper.startswith("FIVE"):
            title_upper = "THE PARABLE OF THE MEDICINAL HERBS"
        elif title_upper.startswith("SIX"):
            title_upper = "THE NAMING"
        elif title_upper.startswith("SEVEN"):
            title_upper = "THE PHANTOM CITY BLUES"
        elif title_upper.startswith("EIGHT"):
            title_upper = "WHEN THE FIVE HUNDRED FINALLY HEARD THEIR NAMES CALLED"
        elif title_upper.startswith("NINE"):
            title_upper = "WHEN THE FAITHFUL GET THEIR DUE"
        elif title_upper.startswith("TEN"):
            title_upper = "HONOR THE WORD-CARRIERS"
        elif title_upper.startswith("ELEVEN"):
            title_upper = "WHEN THE JEWELED TOWER ROSE UP"
        elif title_upper.startswith("TWELVE"):
            title_upper = "WHEN YOUR ENEMY WAS YOUR TEACHER"
        elif title_upper.startswith("THIRTEEN"):
            title_upper = "WHEN THE ROAD GETS ROUGH, YOU GOTTA KEEP WALKING"
        elif title_upper.startswith("FOURTEEN"):
            title_upper = "HOW TO KEEP YOUR SOUL CLEAN WHEN THE WORLD'S GONE WRONG"
        elif title_upper.startswith("FIFTEEN"):
            title_upper = "WHEN THE UNDERGROUND ARMY ROSE UP"
        elif title_upper.startswith("SIXTEEN"):
            title_upper = "HOW LONG THE TATHAGATA'S BEEN ALIVE"
        elif title_upper.startswith("SEVENTEEN"):
            title_upper = "COUNTING UP THE GRACE"
        elif title_upper.startswith("EIGHTEEN"):
            title_upper = "THE JOY THAT MULTIPLIES"
        elif title_upper.startswith("NINETEEN"):
            title_upper = "WHEN YOUR SENSES WAKE UP"
        elif title_upper.startswith("TWENTY-ONE"):
            title_upper = "WHEN THE LORD SHOWED HIS HAND"
        elif title_upper.startswith("TWENTY-TWO"):
            title_upper = "THE PASSING ON"
        elif title_upper.startswith("TWENTY-THREE"):
            title_upper = "MEDICINE KING BODHISATTVA - THE STORY OF HOW HE GAVE IT ALL"
        elif title_upper.startswith("TWENTY-FOUR"):
            title_upper = "WONDERFUL SOUND BODHISATTVA"
        elif title_upper.startswith("TWENTY-FIVE"):
            title_upper = "THE ONE WHO HEARS THE WORLD CRYING"
        elif title_upper.startswith("TWENTY-SIX"):
            title_upper = "THE PROTECTION SONGS"
        elif title_upper.startswith("TWENTY-SEVEN"):
            title_upper = "THE BEAUTIFUL KING AND HIS GOOD FRIENDS"
        elif title_upper.startswith("TWENTY-EIGHT"):
            title_upper = "UNIVERSAL WORTHY COMES TO ENCOURAGE YOU"
        elif title_upper.startswith("TWENTY"):
            title_upper = "THE BODHISATTVA WHO NEVER LOOKED DOWN"

        # Truncate title if too long for filename
        if len(title_upper) > 60:
            title_upper = title_upper[:60]

        filename = f"{chapter_num:02d}_CHAPTER_{title_upper}.txt"
        filepath = os.path.join(OUTPUT_DIR, filename)

        # Write chapter file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(chapter_text)

        # Get file size and line count
        file_size = os.path.getsize(filepath)
        line_count = len(chapter_lines)

        # Store results
        results.append({
            'chapter_num': chapter_num,
            'title': title,
            'filename': filename,
            'voice_tags': voice_tag_count,
            'voices_used': voices_used,
            'chinese_chars': chinese_char_count,
            'file_size': file_size,
            'line_count': line_count,
            'starts_with_tag': starts_with_voice_tag,
            'first_line': first_line
        })

        total_voice_tags += voice_tag_count

        status = "✓" if starts_with_voice_tag else "✗"
        print(f"{status} Chapter {chapter_num:2d}: {voice_tag_count:3d} voice tags | {line_count:4d} lines | {len(voices_used)} speakers | First: {first_line[:30]}")

    return results, total_voice_tags

def generate_report(results, total_voice_tags):
    """Generate comprehensive verification report."""

    print("\n" + "="*80)
    print("CHAPTER EXTRACTION VERIFICATION REPORT")
    print("="*80)
    print()

    print(f"Total chapters extracted: {len(results)}")
    print(f"Total voice tags across all chapters: {total_voice_tags}")
    print()

    print("CHAPTER-BY-CHAPTER SUMMARY:")
    print("-" * 80)
    print(f"{'Ch':>3} | {'Voice Tags':>10} | {'Lines':>6} | {'Size':>8} | {'Speakers'}")
    print("-" * 80)

    for r in results:
        speakers_str = ', '.join([f"[{v}]" for v in r['voices_used'][:5]])
        if len(r['voices_used']) > 5:
            speakers_str += f"... (+{len(r['voices_used']) - 5})"

        print(f"{r['chapter_num']:>3} | {r['voice_tags']:>10} | {r['line_count']:>6} | {r['file_size']:>7}B | {speakers_str}")

    print("-" * 80)
    print()

    # Voice tag distribution
    print("VOICE TAG DISTRIBUTION ACROSS ALL CHAPTERS:")
    print("-" * 80)

    voice_totals = {tag: 0 for tag in VOICE_TAGS}

    for r in results:
        # Re-read chapter to count individual voices
        filepath = os.path.join(OUTPUT_DIR, r['filename'])
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        for tag in VOICE_TAGS:
            voice_totals[tag] += text.count(f'[{tag}]')

    # Sort by count
    sorted_voices = sorted(voice_totals.items(), key=lambda x: x[1], reverse=True)

    for voice, count in sorted_voices:
        if count > 0:
            print(f"  [{voice:15s}] : {count:4d} occurrences")

    print("-" * 80)
    print()

    # Check for issues
    print("QUALITY ASSURANCE CHECKS:")
    print("-" * 80)

    issues_found = []

    # Check for Chinese characters
    chinese_chapters = [r for r in results if r['chinese_chars'] > 0]
    if chinese_chapters:
        issues_found.append(f"Chinese characters found in {len(chinese_chapters)} chapter(s)")
        for r in chinese_chapters:
            print(f"  ⚠ Chapter {r['chapter_num']}: {r['chinese_chars']} Chinese characters found")
    else:
        print("  ✓ No Chinese characters found in any chapter")

    # Check for chapters with no voice tags
    no_tags = [r for r in results if r['voice_tags'] == 0]
    if no_tags:
        issues_found.append(f"{len(no_tags)} chapter(s) with no voice tags")
        for r in no_tags:
            print(f"  ⚠ Chapter {r['chapter_num']}: No voice tags found")
    else:
        print("  ✓ All chapters contain voice tags")

    # CRITICAL: Check if all chapters start with voice tags
    no_start_tag = [r for r in results if not r['starts_with_tag']]
    if no_start_tag:
        issues_found.append(f"{len(no_start_tag)} chapter(s) do NOT start with voice tag")
        for r in no_start_tag:
            print(f"  ⚠ Chapter {r['chapter_num']}: First line is '{r['first_line'][:50]}' (NOT a voice tag)")
    else:
        print("  ✓ All chapters start with voice tags")

    # Compare to expected total
    expected_tags = 553
    if total_voice_tags == expected_tags:
        print(f"  ✓ Voice tag count matches expected: {expected_tags}")
    else:
        diff = total_voice_tags - expected_tags
        print(f"  ⚠ Voice tag count: {total_voice_tags} (expected {expected_tags}, diff: {diff:+d})")
        issues_found.append(f"Voice tag count mismatch: {diff:+d}")

    print("-" * 80)
    print()

    if issues_found:
        print("ISSUES FOUND:")
        for issue in issues_found:
            print(f"  • {issue}")
    else:
        print("✓ All quality checks passed!")

    print()
    print("="*80)
    print("EXTRACTION COMPLETE")
    print("="*80)

if __name__ == "__main__":
    print("Starting chapter extraction with voice tag preservation...")
    print()
    results, total_voice_tags = extract_chapters()
    print()
    generate_report(results, total_voice_tags)
