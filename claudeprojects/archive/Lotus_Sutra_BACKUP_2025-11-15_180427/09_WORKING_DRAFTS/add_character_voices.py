#!/usr/bin/env python3
"""
Add Individual Character Voices to Lotus Sutra Narrated Manuscript
- Mañjuśrī speaks in Chapter 1
- Parable characters (Elder, Father/Son, Guide, Travelers)
- Other individual disciples (Subhūti when distinct)
"""

import re

# Read current enhanced manuscript
with open('/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript_enhanced.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Track all additions
additions_log = []
voice_counts = {}

def add_voice_before_line(lines, line_num, voice_tag, context):
    """Add a voice tag before the specified line"""
    global additions_log, voice_counts

    idx = line_num - 1
    if idx < 0 or idx >= len(lines):
        return False

    # Check if there's already a voice tag
    if lines[idx].strip().startswith('['):
        return False

    # Add the voice tag
    lines[idx] = f'[{voice_tag}]\n' + lines[idx]

    # Track
    if voice_tag not in voice_counts:
        voice_counts[voice_tag] = 0
    voice_counts[voice_tag] += 1

    additions_log.append({
        'line': line_num,
        'voice': voice_tag,
        'context': context
    })

    return True

# Process lines
enhanced_lines = lines.copy()

# ============================================================================
# MAÑJUŚRĪ'S DIALOGUES IN CHAPTER 1
# ============================================================================
print("Adding Mañjuśrī's voice...")

# Line 630-645: Mañjuśrī's prose response to Maitreya (line 629 says "Mañjuśrī spoke")
if add_voice_before_line(enhanced_lines, 631, 'Mañjuśrī', 'Mañjuśrī responding to Maitreya about the signs'):
    print("  Line 631: Added [Mañjuśrī] - prose response to Maitreya")

# Line 647-695: Mañjuśrī continues telling story of past Buddha
if add_voice_before_line(enhanced_lines, 649, 'Mañjuśrī', 'Mañjuśrī continuing story of Moon-Sun-Lamp Buddha'):
    print("  Line 649: Added [Mañjuśrī] - continuing narration")

# Line 701-890+: Mañjuśrī speaks in verse (line 701 says "Mañjuśrī...spoke in rhythm and rhyme")
if add_voice_before_line(enhanced_lines, 703, 'Mañjuśrī', 'Mañjuśrī speaking in verse about past Buddha'):
    print("  Line 703: Added [Mañjuśrī] - verse narration")

# Line 12476: Mañjuśrī speaks to Buddha in later chapter
if add_voice_before_line(enhanced_lines, 12477, 'Mañjuśrī', 'Mañjuśrī asking Buddha about merit'):
    print("  Line 12477: Added [Mañjuśrī] - speaking to Buddha")

# ============================================================================
# PARABLE CHARACTER VOICES
# ============================================================================
print("\nAdding parable character voices...")

# BURNING HOUSE PARABLE (Chapter 3, lines ~2245-2390)
# Search for Elder's direct speech/thought

for i in range(2245, 2320):
    line = enhanced_lines[i]

    # Look for elder's thoughts when he sees fire (around line 2254)
    if i == 2253:
        # "The elder sees this great fire" - next few lines are his thoughts
        # Find first quoted speech
        for j in range(i+1, min(i+10, len(enhanced_lines))):
            if enhanced_lines[j].strip().startswith('"') and '[' not in enhanced_lines[j]:
                if add_voice_before_line(enhanced_lines, j+1, 'Elder_Parable', 'Elder thinking when seeing fire'):
                    print(f"  Line {j+1}: Added [Elder_Parable] - elder's thought in burning house")
                break
        break

# Look for elder calling to children (around line 2265)
for i in range(2255, 2285):
    line = enhanced_lines[i]
    if 'said to his children' in line.lower() or 'called to them' in line.lower():
        # Next line is likely his speech
        if i+1 < len(enhanced_lines) and enhanced_lines[i+1].strip().startswith('"'):
            if '[' not in enhanced_lines[i+1]:
                if add_voice_before_line(enhanced_lines, i+2, 'Elder_Parable', 'Elder calling to children in burning house'):
                    print(f"  Line {i+2}: Added [Elder_Parable] - elder calling children")
                    break

# Look for elder's joy when children escape (around line 2303)
for i in range(2295, 2310):
    line = enhanced_lines[i]
    if 'he thought' in line.lower() and i > 2295:
        if i+1 < len(enhanced_lines) and enhanced_lines[i+1].strip().startswith('"'):
            if '[' not in enhanced_lines[i+1]:
                if add_voice_before_line(enhanced_lines, i+2, 'Elder_Parable', 'Elder rejoicing after children escape'):
                    print(f"  Line {i+2}: Added [Elder_Parable] - elder's relief")
                    break

# PRODIGAL SON PARABLE (Chapter 4, lines ~3510-4050)
print("\nProdigal Son parable...")

# Father's thoughts and speech
for i in range(3510, 3900):
    line = enhanced_lines[i]

    # Father sees son
    if 'father saw him' in line.lower() and 'from a distance' in line.lower():
        # Next thought/speech is father's
        for j in range(i+1, min(i+15, len(enhanced_lines))):
            if enhanced_lines[j].strip().startswith('"') and '[' not in enhanced_lines[j]:
                if add_voice_before_line(enhanced_lines, j+1, 'Prodigal_Father', 'Father seeing lost son'):
                    print(f"  Line {j+1}: Added [Prodigal_Father] - father sees son")
                break

    # Father instructs messengers
    if 'father told' in line.lower() and i > 3550 and i < 3650:
        if i+1 < len(enhanced_lines) and enhanced_lines[i+1].strip().startswith('"'):
            if '[' not in enhanced_lines[i+1]:
                if add_voice_before_line(enhanced_lines, i+2, 'Prodigal_Father', 'Father giving instructions'):
                    print(f"  Line {i+2}: Added [Prodigal_Father] - father's instructions")

    # Father speaks to son
    if 'father said to him' in line.lower() or 'old man said' in line.lower():
        if i+1 < len(enhanced_lines) and enhanced_lines[i+1].strip().startswith('"'):
            if '[' not in enhanced_lines[i+1]:
                if add_voice_before_line(enhanced_lines, i+2, 'Prodigal_Father', 'Father speaking to son'):
                    print(f"  Line {i+2}: Added [Prodigal_Father] - father to son")

    # Son's thoughts
    if 'son thought' in line.lower() or 'poor man thought' in line.lower():
        if i+1 < len(enhanced_lines) and enhanced_lines[i+1].strip().startswith('"'):
            if '[' not in enhanced_lines[i+1]:
                if add_voice_before_line(enhanced_lines, i+2, 'Prodigal_Son', 'Son\'s thoughts'):
                    print(f"  Line {i+2}: Added [Prodigal_Son] - son's thoughts")

    # Son replies
    if 'son said' in line.lower() or 'man replied' in line.lower():
        if i+1 < len(enhanced_lines) and enhanced_lines[i+1].strip().startswith('"'):
            if '[' not in enhanced_lines[i+1]:
                if add_voice_before_line(enhanced_lines, i+2, 'Prodigal_Son', 'Son responding'):
                    print(f"  Line {i+2}: Added [Prodigal_Son] - son responds")

# PHANTOM CITY PARABLE (Chapter 7, lines ~5340-5850)
print("\nPhantom City parable...")

for i in range(5340, 5850):
    line = enhanced_lines[i]

    # Guide thinks or speaks
    if 'guide thought' in line.lower() or 'leader thought' in line.lower():
        if i+1 < len(enhanced_lines) and enhanced_lines[i+1].strip().startswith('"'):
            if '[' not in enhanced_lines[i+1]:
                if add_voice_before_line(enhanced_lines, i+2, 'Guide_Phantom', 'Guide thinking about travelers'):
                    print(f"  Line {i+2}: Added [Guide_Phantom] - guide's thoughts")

    if 'guide said' in line.lower() or 'leader told them' in line.lower():
        if i+1 < len(enhanced_lines) and enhanced_lines[i+1].strip().startswith('"'):
            if '[' not in enhanced_lines[i+1]:
                if add_voice_before_line(enhanced_lines, i+2, 'Guide_Phantom', 'Guide speaking to travelers'):
                    print(f"  Line {i+2}: Added [Guide_Phantom] - guide speaks")

    # Travelers respond
    if 'travelers said' in line.lower() or 'people said' in line.lower() or 'they said' in line.lower():
        # Make sure this is in parable context
        if i > 5400 and i < 5750:
            if i+1 < len(enhanced_lines) and enhanced_lines[i+1].strip().startswith('"'):
                if '[' not in enhanced_lines[i+1]:
                    if add_voice_before_line(enhanced_lines, i+2, 'Travelers_Voices', 'Travelers responding'):
                        print(f"  Line {i+2}: Added [Travelers_Voices] - travelers respond")

# ============================================================================
# Write enhanced manuscript
# ============================================================================
output_path = '/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript_enhanced.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.writelines(enhanced_lines)

print(f"\n✓ Enhanced manuscript written to: {output_path}")

# Count total voice tags in final manuscript
total_tags = sum(1 for line in enhanced_lines if re.search(r'\[[\w_]+\]', line))
print(f"✓ Total voice tags in manuscript: {total_tags}")

# Update change log
log_path = '/Users/williamaltig/claudeprojects/Lotus_Sutra/VOICE_ENHANCEMENT_LOG.txt'
with open(log_path, 'a', encoding='utf-8') as f:
    f.write("\n\n" + "=" * 80 + "\n")
    f.write("CHARACTER VOICE ADDITIONS - DISCIPLES AND PARABLE CHARACTERS\n")
    f.write("=" * 80 + "\n\n")

    f.write("NEW INDIVIDUAL CHARACTER VOICES ADDED\n")
    f.write("-" * 80 + "\n")
    for voice, count in sorted(voice_counts.items(), key=lambda x: x[1], reverse=True):
        f.write(f"[{voice}]: {count} occurrences\n")

    f.write("\n\nDETAILED ADDITIONS LOG\n")
    f.write("-" * 80 + "\n")
    for addition in additions_log:
        f.write(f"Line {addition['line']}: Added [{addition['voice']}]\n")
        f.write(f"  Context: {addition['context']}\n\n")

print(f"✓ Updated log at: {log_path}")

# Summary
print("\n" + "=" * 80)
print("CHARACTER VOICE ENHANCEMENT COMPLETE")
print("=" * 80)
print(f"Total new character voices added: {len(additions_log)}")
print("\nNew character voices:")
for voice, count in sorted(voice_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"  [{voice}]: {count}")
print("=" * 80)
