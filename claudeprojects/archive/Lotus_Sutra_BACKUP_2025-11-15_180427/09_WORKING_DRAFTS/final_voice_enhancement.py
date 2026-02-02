#!/usr/bin/env python3
"""
FINAL Comprehensive Voice Enhancement for Lotus Sutra
Handles ALL remaining [Gacrux] instances
"""

import re

# Read the current enhanced manuscript
with open('/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript_enhanced.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Complete mapping of ALL remaining [Gacrux] instances
# Line number: (voice_tag, description)
FINAL_MAPPINGS = {
    # Buddha speaking in prose dialogue
    963: ('Iapetus', 'Buddha speaking to Śāriputra about deep wisdom'),
    1249: ('Iapetus', 'Buddha teaching about past/future Buddhas'),
    2087: ('Iapetus', 'Buddha giving prophecy to Śāriputra'),
    2327: ('Iapetus', 'Buddha explaining the parable to Śāriputra'),
    4100: ('Iapetus', 'Buddha responding to Mahākāśyapa'),
    4504: ('Iapetus', 'Buddha prophesying Mahākāśyapa\'s Buddhahood'),
    5702: ('Iapetus', 'Buddha teaching about Pūrṇa'),
    5835: ('Iapetus', 'Buddha giving prophecies to 1200 arhats'),
    6228: ('Iapetus', 'Buddha speaking to Medicine King'),
    8825: ('Iapetus', 'Buddha asking Maitreya a question'),
    9234: ('Iapetus', 'Buddha turning to Maitreya'),
    9389: ('Iapetus', 'Buddha telling Maitreya about the comparison'),
    9731: ('Iapetus', 'Buddha answering Maitreya about transmission'),

    # Buddha speaking in verse/poetic form
    2043: ('Rasalgethi', 'Buddha in verse about past/future Buddhas'),
    6143: ('Rasalgethi', 'Buddha prophesying in verse'),

    # Narrator describing bodhisattvas
    8786: ('Charon', 'Narrator describing bodhisattvas addressing Buddha'),

    # Section markers/editorial voice
    1911: ('Aoede', 'Section list marker - chapter contents'),
    4472: ('Aoede', 'Section list marker - medicinal herbs explanation'),
    9716: ('Charon', 'Narrator transition - Maitreya stands to ask'),
    11244: ('Aoede', 'Editorial commentary on "gonna" usage'),
    15466: ('Aoede', 'Glossary entry for Mahāprajāpatī'),
}

# Track changes
changes_log = []
voice_counts = {}

# Process each mapping
enhanced_lines = lines.copy()

for line_num, (voice, description) in sorted(FINAL_MAPPINGS.items()):
    if line_num > len(enhanced_lines):
        continue

    idx = line_num - 1  # Convert to 0-indexed
    if '[Gacrux]' in enhanced_lines[idx]:
        original_line = enhanced_lines[idx]
        new_voice = f'[{voice}]'
        enhanced_lines[idx] = original_line.replace('[Gacrux]', new_voice)

        # Track
        if voice not in voice_counts:
            voice_counts[voice] = 0
        voice_counts[voice] += 1

        changes_log.append({
            'line': line_num,
            'from': '[Gacrux]',
            'to': new_voice,
            'note': description
        })

        print(f"Line {line_num}: [Gacrux] → {new_voice} ({description})")

# Write final enhanced manuscript
output_path = '/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript_enhanced.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.writelines(enhanced_lines)

print(f"\n✓ Final enhanced manuscript written to: {output_path}")

# Verify no [Gacrux] tags remain
remaining_gacrux = sum(1 for line in enhanced_lines if '[Gacrux]' in line)
print(f"✓ Remaining [Gacrux] tags: {remaining_gacrux}")

if remaining_gacrux == 0:
    print("✓✓✓ ALL [Gacrux] TAGS SUCCESSFULLY REPLACED! ✓✓✓")

# Append to change log
log_path = '/Users/williamaltig/claudeprojects/Lotus_Sutra/VOICE_ENHANCEMENT_LOG.txt'
with open(log_path, 'a', encoding='utf-8') as f:
    f.write("\n\n" + "=" * 80 + "\n")
    f.write("FINAL ROUND - REMAINING [Gacrux] REPLACEMENTS\n")
    f.write("=" * 80 + "\n\n")

    for change in changes_log:
        f.write(f"Line {change['line']}: {change['from']} → {change['to']}\n")
        f.write(f"  Note: {change['note']}\n\n")

    f.write("\n" + "=" * 80 + "\n")
    f.write("FINAL VOICE COUNTS (this round)\n")
    f.write("=" * 80 + "\n")
    for voice, count in sorted(voice_counts.items(), key=lambda x: x[1], reverse=True):
        f.write(f"[{voice}]: {count} occurrences\n")

print(f"✓ Updated change log at: {log_path}")

# Summary
print("\n" + "=" * 80)
print("FINAL VOICE ENHANCEMENT COMPLETE")
print("=" * 80)
print(f"Final round replacements: {len(changes_log)}")
print("\nVoices assigned this round:")
for voice, count in sorted(voice_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"  [{voice}]: {count}")
print("=" * 80)
