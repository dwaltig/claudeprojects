#!/usr/bin/env python3
"""
Comprehensive Voice Enhancement for Lotus Sutra Narrated Manuscript
Analyzes every [Gacrux] instance and makes context-aware replacements
"""

import re

# Read the manuscript
with open('/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript_professional.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Manual mapping of line numbers to correct voices based on analysis
# Format: line_number: (replacement_voice, speaker_name, context_note)
MANUAL_VOICE_MAPPINGS = {
    # Chapter 1-2: Mañjuśrī and Maitreya dialogue
    # (Line 963 is Buddha speaking - skip)
    # Lines 1099, 1165, 1185, 1219 are Śāriputra - already handled
    1099: ('Śāriputra', 'Śāriputra speaking in verse'),
    1165: ('Śāriputra', 'Śāriputra addressing Buddha second time in verse'),
    1185: ('Śāriputra', 'Śāriputra addressing Buddha third time in verse'),
    1219: ('Śāriputra', 'Śāriputra affirming he wants to hear'),

    # Line 1249 is Buddha speaking - skip
    # Line 1911 is a list marker - skip

    # Chapter 3: Śāriputra's joy and response
    1928: ('Śāriputra', 'Śāriputra expressing joy at prophecy'),

    # Chapter 3: Buddha's teaching (line 2043 likely Buddha)
    # Line 2087 likely Buddha
    # Line 2221 likely Śāriputra responding
    2221: ('Śāriputra', 'Śāriputra responding about the parable'),

    # Line 2314 Śāriputra responding about elder
    2314: ('Śāriputra', 'Śāriputra answering Buddha\'s question about the elder'),
    # Line 2327 Buddha

    # Chapter 4: Four elder disciples (Mahākāśyapa, Subhūti, etc.)
    3499: ('Mahākāśyapa', 'Mahākāśyapa and four elders speaking together'),

    # Line 3625 continuation of elder disciples
    3625: ('Mahākāśyapa', 'Continuation of four elders\' discourse'),

    # Line 4100 Buddha responding
    # Line 4472 Buddha
    # Line 4504 Buddha

    # Chapter 9-10
    # Line 5701, 5834 likely Buddha

    # Chapter 11
    # Line 6142, 6227 likely Buddha

    # Chapter 15: Maitreya questions about bodhisattvas from earth
    8373: ('Maitreya', 'Maitreya asking about bodhisattvas emerging from earth'),
    8383: ('Maitreya', 'Maitreya continuing question'),
    8495: ('Charon', 'Narrator transition - emanation Buddhas'),
    8501: ('Maitreya', 'Maitreya will ask the Buddha'),
    8542: ('Maitreya', 'Maitreya asking Buddha'),
    8612: ('Maitreya', 'Maitreya verse about bodhisattvas'),
    8664: ('Maitreya', 'Maitreya stating meaning in verse'),
    # Line 8785 Buddha responding
    # Line 8824 Buddha

    # Line 9233 Buddha to Maitreya
    9287: ('Maitreya', 'Maitreya responding in verse'),
    # Line 9388 Buddha

    # Line 9715, 9730 Buddha
    9819: ('Maitreya', 'Maitreya expressing doubt'),
    9831: ('Maitreya', 'Maitreya in verse'),

    # Line 11243 likely Buddha

    # Chapter 28: Glossary pronunciation section
    14262: ('Aoede', 'Pronunciation guide section marker'),
    14370: ('Aoede', 'Technical terms section'),
    14399: ('Aoede', 'Buddha epithets section'),
    14669: ('Aoede', 'Additional terms section'),
    14675: ('Aoede', 'Continued glossary'),
    14705: ('Aoede', 'Continued glossary'),
    14847: ('Aoede', 'Cultural context section'),
    14865: ('Aoede', 'Continued cultural notes'),
    14929: ('Aoede', 'Blues tradition section'),
    14945: ('Aoede', 'Continued blues section'),
    15419: ('Aoede', 'Final editorial note'),
}

# Track changes
changes_log = []
voice_counts = {}

# Process each mapped line
enhanced_lines = lines.copy()

for line_num, voice_name in sorted(MANUAL_VOICE_MAPPINGS.items()):
    if line_num > len(enhanced_lines):
        continue

    idx = line_num - 1  # Convert to 0-indexed
    if '[Gacrux]' in enhanced_lines[idx]:
        original_line = enhanced_lines[idx]
        new_voice = f'[{voice_name[0]}]'
        enhanced_lines[idx] = original_line.replace('[Gacrux]', new_voice)

        # Track
        if voice_name[0] not in voice_counts:
            voice_counts[voice_name[0]] = 0
        voice_counts[voice_name[0]] += 1

        changes_log.append({
            'line': line_num,
            'from': '[Gacrux]',
            'to': new_voice,
            'note': voice_name[1] if len(voice_name) > 1 else ''
        })

        print(f"Line {line_num}: [Gacrux] → {new_voice}")

# Now add parable character voices
print("\n\nAdding parable character voices...")

# Search for specific parable passages and add voices
parable_additions = []

# Burning House Elder (Chapter 3, around line 2247)
for i in range(2200, 2400):
    if i >= len(enhanced_lines):
        break

    line = enhanced_lines[i]

    # Look for elder's direct speech in burning house
    if i == 2253:  # Elder sees fire and thinks
        if 'The elder sees' in line or 'elder, he saw' in line:
            # Check if dialogue follows
            if i+1 < len(enhanced_lines) and '[' not in enhanced_lines[i+1]:
                # This is narrative, not direct speech - skip
                pass

    # Elder thinking to himself (around line 2254-2290)
    if 2253 < i < 2260:
        if 'he thinks to himself' in line or 'And he thought' in line:
            # Next line might be his thought - mark it
            if i+1 < len(enhanced_lines) and enhanced_lines[i+1].strip().startswith('"'):
                enhanced_lines[i+1] = '[Elder_Parable]\n' + enhanced_lines[i+1]
                parable_additions.append({
                    'line': i+2,
                    'voice': '[Elder_Parable]',
                    'context': 'Elder thinking in burning house'
                })
                if 'Elder_Parable' not in voice_counts:
                    voice_counts['Elder_Parable'] = 0
                voice_counts['Elder_Parable'] += 1
                print(f"Line {i+2}: Added [Elder_Parable] - elder's thought in burning house")
                break

# Prodigal Son parable (Chapter 4, around lines 3512-4050)
# Father and son voices
for i in range(3510, 3850):
    if i >= len(enhanced_lines):
        break

    line = enhanced_lines[i]

    # Father's thoughts
    if 'father thought' in line.lower() or 'old man thought' in line.lower():
        if i+1 < len(enhanced_lines) and enhanced_lines[i+1].strip().startswith('"'):
            if '[' not in enhanced_lines[i+1]:
                enhanced_lines[i+1] = '[Prodigal_Father]\n' + enhanced_lines[i+1]
                if 'Prodigal_Father' not in voice_counts:
                    voice_counts['Prodigal_Father'] = 0
                voice_counts['Prodigal_Father'] += 1
                parable_additions.append({
                    'line': i+2,
                    'voice': '[Prodigal_Father]',
                    'context': 'Father in prodigal son parable'
                })
                print(f"Line {i+2}: Added [Prodigal_Father]")

    # Son's thoughts
    if 'son thought' in line.lower() or 'young man thought' in line.lower():
        if i+1 < len(enhanced_lines) and enhanced_lines[i+1].strip().startswith('"'):
            if '[' not in enhanced_lines[i+1]:
                enhanced_lines[i+1] = '[Prodigal_Son]\n' + enhanced_lines[i+1]
                if 'Prodigal_Son' not in voice_counts:
                    voice_counts['Prodigal_Son'] = 0
                voice_counts['Prodigal_Son'] += 1
                parable_additions.append({
                    'line': i+2,
                    'voice': '[Prodigal_Son]',
                    'context': 'Son in prodigal son parable'
                })
                print(f"Line {i+2}: Added [Prodigal_Son]")

# Phantom City parable (Chapter 7, around lines 5340-5800)
for i in range(5340, 5850):
    if i >= len(enhanced_lines):
        break

    line = enhanced_lines[i]

    # Guide speaks or thinks
    if 'guide thought' in line.lower() or 'guide said' in line.lower() or 'leader thought' in line.lower():
        if i+1 < len(enhanced_lines) and enhanced_lines[i+1].strip().startswith('"'):
            if '[' not in enhanced_lines[i+1]:
                enhanced_lines[i+1] = '[Guide_Phantom]\n' + enhanced_lines[i+1]
                if 'Guide_Phantom' not in voice_counts:
                    voice_counts['Guide_Phantom'] = 0
                voice_counts['Guide_Phantom'] += 1
                parable_additions.append({
                    'line': i+2,
                    'voice': '[Guide_Phantom]',
                    'context': 'Guide in phantom city parable'
                })
                print(f"Line {i+2}: Added [Guide_Phantom]")

    # Travelers speak
    if 'travelers said' in line.lower() or 'people said' in line.lower():
        if i+1 < len(enhanced_lines) and enhanced_lines[i+1].strip().startswith('"'):
            if '[' not in enhanced_lines[i+1]:
                enhanced_lines[i+1] = '[Travelers_Voices]\n' + enhanced_lines[i+1]
                if 'Travelers_Voices' not in voice_counts:
                    voice_counts['Travelers_Voices'] = 0
                voice_counts['Travelers_Voices'] += 1
                parable_additions.append({
                    'line': i+2,
                    'voice': '[Travelers_Voices]',
                    'context': 'Travelers in phantom city'
                })
                print(f"Line {i+2}: Added [Travelers_Voices]")

# Write enhanced manuscript
output_path = '/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript_enhanced.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.writelines(enhanced_lines)

print(f"\n✓ Enhanced manuscript written to: {output_path}")
print(f"  Total lines: {len(enhanced_lines)}")

# Write detailed change log
log_path = '/Users/williamaltig/claudeprojects/Lotus_Sutra/VOICE_ENHANCEMENT_LOG.txt'
with open(log_path, 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write("VOICE ENHANCEMENT LOG\n")
    f.write("Lotus Sutra Narrated Manuscript - Individual Character Voice Assignment\n")
    f.write("=" * 80 + "\n\n")

    f.write("SUMMARY STATISTICS\n")
    f.write("-" * 80 + "\n")
    f.write(f"Total [Gacrux] replacements: {len(changes_log)}\n")
    f.write(f"Total parable character voices added: {len(parable_additions)}\n")
    f.write(f"Total voice assignments made: {len(changes_log) + len(parable_additions)}\n\n")

    f.write("NEW VOICE ASSIGNMENTS\n")
    f.write("-" * 80 + "\n")
    for voice, count in sorted(voice_counts.items(), key=lambda x: x[1], reverse=True):
        f.write(f"[{voice}]: {count} occurrences\n")

    f.write("\n\nDETAILED CHANGE LOG - [Gacrux] REPLACEMENTS\n")
    f.write("=" * 80 + "\n\n")
    for change in changes_log:
        f.write(f"Line {change['line']}: {change['from']} → {change['to']}\n")
        f.write(f"  Note: {change['note']}\n\n")

    f.write("\n\nPARABLE CHARACTER VOICE ADDITIONS\n")
    f.write("=" * 80 + "\n\n")
    for addition in parable_additions:
        f.write(f"Line {addition['line']}: Added {addition['voice']}\n")
        f.write(f"  Context: {addition['context']}\n\n")

print(f"✓ Change log written to: {log_path}")

# Summary
print("\n" + "=" * 80)
print("VOICE ENHANCEMENT COMPLETE")
print("=" * 80)
print(f"\nVOICE REPLACEMENTS: {len(changes_log)}")
print(f"PARABLE ADDITIONS: {len(parable_additions)}")
print(f"TOTAL NEW ASSIGNMENTS: {len(changes_log) + len(parable_additions)}")
print("\nNEW VOICES:")
for voice, count in sorted(voice_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"  [{voice}]: {count}")
print("=" * 80)
