#!/usr/bin/env python3
"""
Voice Enhancement Script for Lotus Sutra Narrated Manuscript
Replaces generic [Gacrux] tags with individual disciple voices
Adds parable character voices
"""

import re
from typing import List, Tuple, Dict

# Read the manuscript
with open('/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript_professional.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Initialize tracking
changes_log = []
voice_counts = {
    'Śāriputra': 0,
    'Mañjuśrī': 0,
    'Maitreya': 0,
    'Mahākāśyapa': 0,
    'Subhūti': 0,
    'Elder_Parable': 0,
    'Children_Voices': 0,
    'Guide_Phantom': 0,
    'Travelers_Voices': 0,
    'Sixteen_Princes': 0,
}

# Context window for speaker identification
def find_speaker_context(lines: List[str], gacrux_line_num: int, window: int = 10) -> Tuple[str, str]:
    """
    Find who's speaking by looking at context before [Gacrux] tag.
    Returns (speaker_name, context_snippet)
    """
    start = max(0, gacrux_line_num - window)
    context = ''.join(lines[start:gacrux_line_num])

    # Check for explicit speaker attribution in reverse order (most recent first)
    patterns = [
        (r'Śāriputra.*(?:spoke|said|addressed)', 'Śāriputra'),
        (r'Mañjuśrī.*(?:spoke|said)', 'Mañjuśrī'),
        (r'Maitreya.*(?:spoke|said)', 'Maitreya'),
        (r'Mahākāśyapa.*(?:said|spoke)', 'Mahākāśyapa'),
        (r'Subhūti.*(?:said|spoke)', 'Subhūti'),
        (r'Then Śāriputra', 'Śāriputra'),
        (r'At that time.*Śāriputra', 'Śāriputra'),
        (r'sixteen princes.*said', 'Sixteen_Princes'),
        (r'them sixteen princes', 'Sixteen_Princes'),
        (r'(?:the )?[Ee]lder.*(?:said|thought)', 'Elder_Parable'),
        (r'(?:the )?children.*(?:said|cried)', 'Children_Voices'),
        (r'guide.*said', 'Guide_Phantom'),
        (r'travelers.*said', 'Travelers_Voices'),
    ]

    for pattern, speaker in patterns:
        if re.search(pattern, context, re.IGNORECASE):
            return speaker, context[-200:]  # Return last 200 chars of context

    # If it's Buddha speaking TO someone, it's Buddha (keep as is)
    if re.search(r'(?:Buddha|World-Honored One).*(?:told|said to) Śāriputra', context):
        return 'Buddha', context[-200:]

    return 'Unknown', context[-200:]

# Process all lines
enhanced_lines = lines.copy()
total_gacrux = 0
total_replacements = 0

print("Scanning for [Gacrux] tags...")
for i, line in enumerate(lines):
    if '[Gacrux]' in line:
        total_gacrux += 1
        speaker, context = find_speaker_context(lines, i)

        if speaker in voice_counts:
            # Replace with individual voice
            new_voice = f'[{speaker}]'
            enhanced_lines[i] = line.replace('[Gacrux]', new_voice)
            voice_counts[speaker] += 1
            total_replacements += 1

            log_entry = {
                'line_num': i + 1,
                'original': '[Gacrux]',
                'replacement': new_voice,
                'speaker': speaker,
                'context_snippet': context.strip()[-100:]
            }
            changes_log.append(log_entry)

            if total_replacements <= 10 or total_replacements % 10 == 0:
                print(f"  Line {i+1}: [Gacrux] → {new_voice} ({speaker})")

print(f"\nTotal [Gacrux] tags found: {total_gacrux}")
print(f"Total replacements made: {total_replacements}")
print(f"Unresolved (kept as [Gacrux]): {total_gacrux - total_replacements}")

# Now scan for parable sections and add character voices
print("\n\nScanning for parable character dialogue...")

# Burning House Parable (Chapter 3, around lines 2245-2400)
parable_additions = 0
for i in range(len(enhanced_lines)):
    line = enhanced_lines[i]

    # Look for elder speaking in burning house parable (around line 2247+)
    if 2200 < i < 2500:  # Burning house range
        # Elder narration/thought
        if re.search(r'elder.*(?:thought|said|sees|got)', line, re.IGNORECASE) and '[' not in line and not line.strip().startswith('"'):
            # Check if next line is dialogue or narration
            if i+1 < len(enhanced_lines) and enhanced_lines[i+1].strip().startswith('"'):
                # Add voice tag before dialogue
                enhanced_lines[i+1] = '[Elder_Parable]\n' + enhanced_lines[i+1]
                parable_additions += 1
                voice_counts['Elder_Parable'] += 1

    # Phantom City Parable (Chapter 7, around lines 5300-5800)
    if 5300 < i < 5900:
        if re.search(r'guide.*(?:thought|said)', line, re.IGNORECASE) and '[' not in line:
            if i+1 < len(enhanced_lines) and enhanced_lines[i+1].strip().startswith('"'):
                enhanced_lines[i+1] = '[Guide_Phantom]\n' + enhanced_lines[i+1]
                parable_additions += 1
                voice_counts['Guide_Phantom'] += 1

print(f"Parable character voice tags added: {parable_additions}")

# Write enhanced manuscript
output_path = '/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript_enhanced.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.writelines(enhanced_lines)

print(f"\n✓ Enhanced manuscript written to: {output_path}")

# Write change log
log_path = '/Users/williamaltig/claudeprojects/Lotus_Sutra/VOICE_ENHANCEMENT_LOG.txt'
with open(log_path, 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write("VOICE ENHANCEMENT LOG\n")
    f.write("Lotus Sutra Narrated Manuscript - Individual Voice Assignment\n")
    f.write("=" * 80 + "\n\n")

    f.write(f"SUMMARY STATISTICS\n")
    f.write(f"-" * 80 + "\n")
    f.write(f"Total [Gacrux] tags found: {total_gacrux}\n")
    f.write(f"Total replaced with individual voices: {total_replacements}\n")
    f.write(f"Parable character voices added: {parable_additions}\n")
    f.write(f"Unresolved (kept as [Gacrux]): {total_gacrux - total_replacements}\n\n")

    f.write(f"NEW VOICE ASSIGNMENTS\n")
    f.write(f"-" * 80 + "\n")
    for voice, count in sorted(voice_counts.items(), key=lambda x: x[1], reverse=True):
        if count > 0:
            f.write(f"[{voice}]: {count} occurrences\n")

    f.write(f"\n\nDETAILED CHANGE LOG\n")
    f.write(f"=" * 80 + "\n\n")

    for i, change in enumerate(changes_log, 1):
        f.write(f"CHANGE #{i}\n")
        f.write(f"Line: {change['line_num']}\n")
        f.write(f"Speaker: {change['speaker']}\n")
        f.write(f"Replacement: {change['original']} → {change['replacement']}\n")
        f.write(f"Context: ...{change['context_snippet']}\n")
        f.write(f"-" * 80 + "\n\n")

print(f"✓ Change log written to: {log_path}")

# Print summary
print("\n" + "=" * 80)
print("VOICE ENHANCEMENT COMPLETE")
print("=" * 80)
print("\nNEW VOICES ASSIGNED:")
for voice, count in sorted(voice_counts.items(), key=lambda x: x[1], reverse=True):
    if count > 0:
        print(f"  [{voice}]: {count} occurrences")
print("\n" + "=" * 80)
