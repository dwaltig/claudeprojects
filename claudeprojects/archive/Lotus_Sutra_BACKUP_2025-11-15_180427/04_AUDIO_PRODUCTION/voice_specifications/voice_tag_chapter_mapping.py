#!/usr/bin/env python3
"""
Voice Tag Chapter Mapping Tool
Maps voice tags from master file to individual chapter files
"""

# Chapter boundaries from master file (line numbers)
CHAPTER_BOUNDARIES = {
    1: (262, 955),      # Chapter 1: THE OPENING
    2: (956, 1916),     # Chapter 2: THE LOVING TRICKS
    3: (1917, 3494),    # Chapter 3: THE PARABLE
    4: (3495, 4093),    # Chapter 4: FAITH AND UNDERSTANDING
    5: (4094, 4497),    # Chapter 5: THE PARABLE OF THE MEDICINAL HERBS
    6: (4498, 4873),    # Chapter 6: THE NAMING
    7: (4874, 5681),    # Chapter 7: THE PHANTOM CITY BLUES
    8: (5682, 6018),    # Chapter 8: WHEN THE FIVE HUNDRED FINALLY HEARD THEIR NAMES CALLED
    9: (6019, 6210),    # Chapter 9: WHEN THE FAITHFUL GET THEIR DUE
    10: (6211, 6566),   # Chapter 10: HONOR THE WORD-CARRIERS
    11: (6567, 7009),   # Chapter 11: WHEN THE JEWELED TOWER ROSE UP
    12: (7010, 7271),   # Chapter 12: WHEN YOUR ENEMY WAS YOUR TEACHER
    13: (7272, 7586),   # Chapter 13: WHEN THE ROAD GETS ROUGH, YOU GOTTA KEEP WALKING
    14: (7587, 8229),   # Chapter 14: HOW TO KEEP YOUR SOUL CLEAN WHEN THE WORLD'S GONE WRONG
    15: (8230, 8769),   # Chapter 15: WHEN THE UNDERGROUND ARMY ROSE UP
    16: (8770, 9226),   # Chapter 16: HOW LONG THE TATHAGATA'S BEEN ALIVE
    17: (9227, 9708),   # Chapter 17: COUNTING UP THE GRACE
    18: (9709, 10146),  # Chapter 18: THE JOY THAT MULTIPLIES
    19: (10147, 10888), # Chapter 19: WHEN YOUR SENSES WAKE UP
    20: (10889, 11278), # Chapter 20: THE BODHISATTVA WHO NEVER LOOKED DOWN
    21: (11279, 11612), # Chapter 21: WHEN THE LORD SHOWED HIS HAND
    22: (11613, 11827), # Chapter 22: THE PASSING ON
    23: (11828, 12302), # Chapter 23: MEDICINE KING BODHISATTVA
    24: (12303, 12872), # Chapter 24: WONDERFUL SOUND BODHISATTVA
    25: (12873, 13550), # Chapter 25: THE ONE WHO HEARS THE WORLD CRYING
    26: (13551, 13911), # Chapter 26: THE PROTECTION SONGS
    27: (13912, 14155), # Chapter 27: THE BEAUTIFUL KING AND HIS GOOD FRIENDS
    28: (14156, 15485), # Chapter 28: UNIVERSAL WORTHY COMES TO ENCOURAGE YOU
}

# Voice tag data (line number: voice tag)
voice_tags = {}

# Read voice tags from file
with open('/Users/williamaltig/claudeprojects/Lotus_Sutra/audio_production/voice_tags_master_list.txt', 'r') as f:
    for line in f:
        if ':' in line:
            parts = line.strip().split(':')
            if len(parts) >= 2:
                line_num = int(parts[0].strip())
                voice_tag = ':'.join(parts[1:]).strip()
                voice_tags[line_num] = voice_tag

# Map voice tags to chapters
chapter_voice_tags = {i: [] for i in range(1, 29)}

for line_num, voice_tag in voice_tags.items():
    for chapter_num, (start, end) in CHAPTER_BOUNDARIES.items():
        if start <= line_num <= end:
            chapter_voice_tags[chapter_num].append((line_num, voice_tag))
            break

# Generate comprehensive report
output = []
output.append("=" * 80)
output.append("COMPREHENSIVE VOICE TAG MAPPING BY CHAPTER")
output.append("Lotus Sutra Blues Interpretation - Audio Production Edition")
output.append("=" * 80)
output.append("")
output.append(f"Total Voice Tags in Master File: {len(voice_tags)}")
output.append("")

# Voice tag distribution summary
total_mapped = sum(len(tags) for tags in chapter_voice_tags.values())
output.append(f"Total Voice Tags Mapped to Chapters: {total_mapped}")
output.append("")

# Chapter-by-chapter breakdown
for chapter_num in range(1, 29):
    tags = chapter_voice_tags[chapter_num]
    start, end = CHAPTER_BOUNDARIES[chapter_num]
    
    output.append("=" * 80)
    output.append(f"CHAPTER {chapter_num}")
    output.append(f"Line Range: {start}-{end}")
    output.append(f"Total Voice Tags: {len(tags)}")
    output.append("=" * 80)
    output.append("")
    
    if tags:
        # Count voices in this chapter
        voice_counts = {}
        for _, voice in tags:
            voice_counts[voice] = voice_counts.get(voice, 0) + 1
        
        output.append("Voice Distribution:")
        for voice in sorted(voice_counts.keys()):
            output.append(f"  {voice}: {voice_counts[voice]} occurrences")
        output.append("")
        
        output.append("Detailed Voice Tag Locations:")
        for line_num, voice in tags:
            output.append(f"  Line {line_num}: {voice}")
        output.append("")
    else:
        output.append("  (No voice tags in this chapter)")
        output.append("")

# Summary statistics
output.append("=" * 80)
output.append("VOICE TAG SUMMARY STATISTICS")
output.append("=" * 80)
output.append("")

all_voices = {}
for tags in chapter_voice_tags.values():
    for _, voice in tags:
        all_voices[voice] = all_voices.get(voice, 0) + 1

output.append("Total Voice Tag Usage Across All Chapters:")
for voice in sorted(all_voices.keys(), key=lambda x: all_voices[x], reverse=True):
    count = all_voices[voice]
    output.append(f"  {voice}: {count} times")
output.append("")

# Chapters by tag count
output.append("Chapters Ranked by Voice Tag Count:")
sorted_chapters = sorted(chapter_voice_tags.items(), key=lambda x: len(x[1]), reverse=True)
for chapter_num, tags in sorted_chapters:
    output.append(f"  Chapter {chapter_num}: {len(tags)} tags")
output.append("")

# Write report
report_content = '\n'.join(output)
with open('/Users/williamaltig/claudeprojects/Lotus_Sutra/audio_production/VOICE_TAG_COMPREHENSIVE_MAPPING.txt', 'w') as f:
    f.write(report_content)

print("Comprehensive voice tag mapping completed!")
print(f"Report saved to: /Users/williamaltig/claudeprojects/Lotus_Sutra/audio_production/VOICE_TAG_COMPREHENSIVE_MAPPING.txt")
