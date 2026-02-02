#!/usr/bin/env python3
"""
Add Parable Character Dialogue Voices
Carefully adds voices to specific parable dialogue passages
"""

import re

# Read current manuscript
with open('/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript_enhanced.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Specific line-by-line mappings for parable dialogue
# These are identified by careful reading of the manuscript
PARABLE_DIALOGUE_ADDITIONS = {
    # Burning House Parable (Chapter 3)
    2268: ('Elder_Parable', 'Elder thinking about carrying children out'),
    2270: ('Elder_Parable', 'Elder reconsidering his plan'),
    2282: ('Elder_Parable', 'Elder deciding on skillful means'),
    2286: ('Elder_Parable', 'Elder calling to children about toys'),
    2296: ('Children_Voices', 'Children asking father for promised toys'),
    2304: ('Elder_Parable', 'Elder thinking about giving great carts'),

    # Prodigal Son Parable (Chapter 4)
    # Find key dialogue moments - need to search carefully
}

# Track additions
additions_log = []
voice_counts = {}

# Process lines
enhanced_lines = lines.copy()

for line_num, (voice, context) in sorted(PARABLE_DIALOGUE_ADDITIONS.items()):
    if line_num >= len(enhanced_lines):
        continue

    idx = line_num - 1
    line = enhanced_lines[idx]

    # Only add if there's no voice tag already on this line
    if not line.strip().startswith('['):
        enhanced_lines[idx] = f'[{voice}]\n' + line

        if voice not in voice_counts:
            voice_counts[voice] = 0
        voice_counts[voice] += 1

        additions_log.append({
            'line': line_num,
            'voice': voice,
            'context': context
        })

        print(f"Line {line_num}: Added [{voice}] - {context}")

# Now search for Prodigal Son dialogue
print("\nSearching for Prodigal Son dialogue...")

# Find father's first sight of son (around line 3535)
for i in range(3530, 3570):
    line = lines[i]
    if 'father recognized him right away' in line.lower() or 'father saw him from a long way off' in line.lower():
        # Look ahead for dialogue
        for j in range(i, min(i+15, len(lines))):
            if lines[j].strip().startswith('"') and '[' not in enhanced_lines[j]:
                enhanced_lines[j] = '[Prodigal_Father]\n' + enhanced_lines[j]
                voice_counts['Prodigal_Father'] = voice_counts.get('Prodigal_Father', 0) + 1
                additions_log.append({
                    'line': j+1,
                    'voice': 'Prodigal_Father',
                    'context': 'Father seeing son and thinking'
                })
                print(f"Line {j+1}: Added [Prodigal_Father] - father sees son")
                break
        break

# Find son's fear/thoughts (around line 3545)
for i in range(3540, 3580):
    line = lines[i]
    if 'poor man' in line.lower() and 'thought' in line.lower():
        for j in range(i, min(i+10, len(lines))):
            if lines[j].strip().startswith('"') and '[' not in enhanced_lines[j]:
                enhanced_lines[j] = '[Prodigal_Son]\n' + enhanced_lines[j]
                voice_counts['Prodigal_Son'] = voice_counts.get('Prodigal_Son', 0) + 1
                additions_log.append({
                    'line': j+1,
                    'voice': 'Prodigal_Son',
                    'context': 'Son afraid upon seeing mansion'
                })
                print(f"Line {j+1}: Added [Prodigal_Son] - son's fear")
                break
        break

# Father speaks to son (multiple instances)
dialogue_count = 0
for i in range(3570, 3850):
    line = lines[i]

    # Father speaks or instructs
    if dialogue_count < 5 and ('father said' in line.lower() or 'rich man said' in line.lower() or 'elder said' in line.lower()):
        if 'to the poor man' in line.lower() or 'to him' in line.lower() or 'to his son' in line.lower():
            for j in range(i, min(i+5, len(lines))):
                if lines[j].strip().startswith('"') and '[' not in enhanced_lines[j]:
                    enhanced_lines[j] = '[Prodigal_Father]\n' + enhanced_lines[j]
                    voice_counts['Prodigal_Father'] = voice_counts.get('Prodigal_Father', 0) + 1
                    additions_log.append({
                        'line': j+1,
                        'voice': 'Prodigal_Father',
                        'context': f'Father speaking (instance {dialogue_count+1})'
                    })
                    print(f"Line {j+1}: Added [Prodigal_Father] - father speaking")
                    dialogue_count += 1
                    break

    # Son responds
    if dialogue_count < 5 and ('son answered' in line.lower() or 'poor man said' in line.lower()):
        for j in range(i, min(i+5, len(lines))):
            if lines[j].strip().startswith('"') and '[' not in enhanced_lines[j]:
                enhanced_lines[j] = '[Prodigal_Son]\n' + enhanced_lines[j]
                voice_counts['Prodigal_Son'] = voice_counts.get('Prodigal_Son', 0) + 1
                additions_log.append({
                    'line': j+1,
                    'voice': 'Prodigal_Son',
                    'context': 'Son responding to father'
                })
                print(f"Line {j+1}: Added [Prodigal_Son] - son responds")
                break

# Phantom City - Guide dialogue
print("\nSearching for Phantom City dialogue...")
dialogue_count = 0
for i in range(5400, 5700):
    line = lines[i]

    # Guide thinks or speaks
    if dialogue_count < 3 and ('guide thought' in line.lower() or 'leader thought' in line.lower()):
        for j in range(i, min(i+5, len(lines))):
            if lines[j].strip().startswith('"') and '[' not in enhanced_lines[j]:
                enhanced_lines[j] = '[Guide_Phantom]\n' + enhanced_lines[j]
                voice_counts['Guide_Phantom'] = voice_counts.get('Guide_Phantom', 0) + 1
                additions_log.append({
                    'line': j+1,
                    'voice': 'Guide_Phantom',
                    'context': f'Guide thinking (instance {dialogue_count+1})'
                })
                print(f"Line {j+1}: Added [Guide_Phantom] - guide thinks")
                dialogue_count += 1
                break

    # Travelers speak
    if 'people said' in line.lower() or 'travelers said' in line.lower():
        for j in range(i, min(i+5, len(lines))):
            if lines[j].strip().startswith('"') and '[' not in enhanced_lines[j]:
                enhanced_lines[j] = '[Travelers_Voices]\n' + enhanced_lines[j]
                voice_counts['Travelers_Voices'] = voice_counts.get('Travelers_Voices', 0) + 1
                additions_log.append({
                    'line': j+1,
                    'voice': 'Travelers_Voices',
                    'context': 'Travelers responding to guide'
                })
                print(f"Line {j+1}: Added [Travelers_Voices] - travelers speak")
                break

# Write enhanced manuscript
output_path = '/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript_enhanced.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.writelines(enhanced_lines)

print(f"\n✓ Enhanced manuscript written")

# Count total voice tags
total_tags = sum(1 for line in enhanced_lines if re.search(r'\[[\w_]+\]', line))
print(f"✓ Total voice tags in manuscript: {total_tags}")

# Update log
log_path = '/Users/williamaltig/claudeprojects/Lotus_Sutra/VOICE_ENHANCEMENT_LOG.txt'
with open(log_path, 'a', encoding='utf-8') as f:
    f.write("\n\n" + "=" * 80 + "\n")
    f.write("PARABLE DIALOGUE VOICE ADDITIONS\n")
    f.write("=" * 80 + "\n\n")

    for voice, count in sorted(voice_counts.items(), key=lambda x: x[1], reverse=True):
        f.write(f"[{voice}]: {count} occurrences added\n")

    f.write("\n")
    for addition in additions_log:
        f.write(f"Line {addition['line']}: [{addition['voice']}] - {addition['context']}\n")

print(f"✓ Log updated")

# Summary
print("\n" + "=" * 80)
print("PARABLE DIALOGUE ENHANCEMENT COMPLETE")
print("=" * 80)
print(f"Total additions: {len(additions_log)}")
for voice, count in sorted(voice_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"  [{voice}]: {count}")
print("=" * 80)
