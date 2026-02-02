#!/usr/bin/env python3
"""
Gender-inclusive revision script for Blues Lotus Sutra
Implements three-phase strategy while preserving theological power of women's appearances
"""

import re

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def apply_phase_1_edits(text):
    """
    PHASE 1: HIGH PRIORITY - Universal addresses and generic references
    ~20-25 instances total
    """
    changes_made = []

    # 1. Universal assembly addresses: "brothers" → "brothers and sisters"
    # Only in direct address contexts, NOT narrative

    # Line 4844: "Listen here, brothers."
    old = '"Listen here, brothers. I\'m gonna tell you'
    new = '"Listen here, brothers and sisters. I\'m gonna tell you'
    if old in text:
        text = text.replace(old, new)
        changes_made.append(f"Line ~4844: {old} → {new}")

    # Line 4848: "Now brothers, listen up."
    old = 'Now brothers, listen up.'
    new = 'Now brothers and sisters, listen up.'
    if old in text:
        text = text.replace(old, new)
        changes_made.append(f"Line ~4848: {old} → {new}")

    # 2. Divine beings: "divine sons" → "divine children"
    old = 'twenty thousand divine sons'
    new = 'twenty thousand divine children'
    if old in text:
        text = text.replace(old, new)
        changes_made.append(f"Divine sons → divine children (20,000)")

    old = 'twelve thousand divine sons'
    new = 'twelve thousand divine children'
    if old in text:
        text = text.replace(old, new)
        changes_made.append(f"Divine sons → divine children (12,000)")

    # "sons of heaven" → "children of heaven"
    old = 'ten thousand sons of heaven'
    new = 'ten thousand children of heaven'
    if old in text:
        text = text.replace(old, new)
        changes_made.append(f"Sons of heaven → children of heaven (10,000)")

    old = 'sons of heaven attained'
    new = 'children of heaven attained'
    if old in text:
        text = text.replace(old, new)
        changes_made.append(f"Sons of heaven → children of heaven (attained)")

    # 3. Generic "good brother" → "good friend"
    # Line 13076 and 13207
    old = '"Good brother, listen now.'
    new = '"Good friend, listen now.'
    if old in text:
        text = text.replace(old, new)
        changes_made.append(f"Good brother → Good friend (direct address)")

    return text, changes_made

def apply_phase_2_edits(text):
    """
    PHASE 2: MEDIUM PRIORITY - Burning house parable + men→folks + framing paragraphs
    ~30-35 instances + 2 new paragraphs
    """
    changes_made = []

    # 1. BURNING HOUSE PARABLE: "sons" → "children"
    # This parable is Chapter 3, lines ~2240-2360
    # We need to be surgical here - only change the parable, not narrative references

    burning_house_changes = [
        ('my sons—they in there in that fire house', 'my children—they in there in that fire house'),
        ('told all his sons:', 'told all his children:'),
        ('If me and my sons don\'t get out', 'If me and my children don\'t get out'),
        ('to get my sons out of this danger', 'to get my children out of this danger'),
        ('that father knew what his sons liked', 'that father knew what his children liked'),
        ('he saw his sons get out safe', 'he saw his children get out safe'),
        ('each of the sons came to their father', 'each of the children came to their father'),
        ('gave each one of his sons the same thing', 'gave each one of his children the same thing'),
        ('I shouldn\'t give my sons these small', 'I shouldn\'t give my children these small'),
        ('These children, they all my sons', 'These children, they all my children'),
        ('How much more for my own sons', 'How much more for my own children'),
        ('each of the sons got to ride', 'each of the children got to ride'),
        ('gave all his sons these precious great carts', 'gave all his children these precious great carts'),
        ('That elder just wanted his sons to get free', 'That elder just wanted his children to get free'),
        ('I\'m gonna use skillful means to get my sons out', 'I\'m gonna use skillful means to get my children out'),
        ('to save his sons from that fire-house disaster', 'to save his children from that fire-house disaster'),
        ('when he saw his sons get out of the fire house', 'when he saw his children get out of the fire house'),
        ('he gave equally to all his sons', 'he gave equally to all his children'),
        ('first he used three carts to entice his sons', 'first he used three carts to entice his children'),
        ('He warned all his sons,', 'He warned all his children,'),
        ('He told all his sons:', 'He told all his children:'),
        ('When the sons heard him describe', 'When the children heard him describe'),
        ('When the elder saw his sons', 'When the elder saw his children'),
        ('Right then, all the sons,', 'Right then, all the children,'),
        ('it lets all the sons', 'it lets all the children'),
    ]

    for old, new in burning_house_changes:
        if old in text:
            text = text.replace(old, new)
            changes_made.append(f"Burning house: {old[:40]}... → {new[:40]}...")

    # 2. Generic "men" → "folks" in UNIVERSAL contexts only
    # Line 293: "These were men who'd walked"
    old = 'These weren\'t no beginners, you understand. These were men who\'d walked the long hard road'
    new = 'These weren\'t no beginners, you understand. These were folks who\'d walked the long hard road'
    if old in text:
        text = text.replace(old, new)
        changes_made.append("Line 293: men → folks (universal context)")

    # 3. ADD FRAMING PARAGRAPHS

    # Find insertion point for Reader's Introduction addition (after line 270)
    # Look for the paragraph starting "This is the sutra's great promise"
    reader_insertion_marker = 'This is the sutra\'s great promise. The old disciples who thought they were finished, the women who were told they couldn\'t, the evil-doers like Devadatta, the non-humans like the 8-year-old dragon girl—all of them, and all of us, are destined for perfect, complete enlightenment.'

    reader_new_paragraph = '''
And let me tell you something else you need to know. This sutra's been written down by men, and mostly men talking. But pay attention when the women show up—because when they do, everything changes. Mahāprajāpatī, the aunt who raised the Buddha when his mama died, she walks up and asks the Buddha straight out: 'Can we practice? Can we be free too?' And the Buddha's got to stop and reckon with her. Then later, eight thousand nuns come through and get their prophecies of Buddhahood. And then—this is the thing that's gonna shake you—a dragon girl, eight years old, becomes a Buddha right there in front of everybody. Just like that. No waiting, no 'you gotta come back as a man next time.' The dharma don't work that way.

The blues knows this truth. Sister Rosetta Tharpe didn't wait for permission. Mahalia Jackson carried the Spirit. The mothers and grandmothers held the church together. When women move in the dharma, when women practice, when women teach—that's when you know it's real. That's the sign that this teaching ain't just for the chosen few. It's for everybody. The dragon girl's enlightenment ain't incidental. It's the proof. It's the promise written in the flesh of a child who shouldn't be able to do it—but does.
'''

    if reader_insertion_marker in text:
        text = text.replace(reader_insertion_marker, reader_insertion_marker + reader_new_paragraph)
        changes_made.append("Added women's paradigm-shifting paragraph to Reader's Introduction")

    # Find insertion point for Translator's Note addition (before signature, around line 114)
    translator_insertion_marker = 'My hope is that this voice allows the Dharma to be heard in a new way, in the key that sang freedom in chains and prophesied justice in the dark. May all beings hear the teaching in the voice that reaches their hearts.'

    translator_new_paragraph = '''
About gender in this translation: You'll notice the text maintains male characters where they're specific—the Buddha, Śāriputra, Mañjuśrī, and the other historical disciples. This is deliberate. Because this sutra's power doesn't come from pretending women were always fully centered in a male-dominated world. It comes from showing women breaking into that narrative, claiming their place, and in doing so, shattering the categories entirely. When that dragon girl becomes a Buddha, it matters because the story up to that point has been mostly men. When Mahāprajāpatī demands recognition, it carries weight because the Buddha had to think about it. I've kept that narrative reality. But in the universal teachings, in the addresses to all practitioners, in the parables that apply to every living being—there I've made sure the language includes everybody. The dharma doesn't have gender restrictions, so the language addressing 'all beings' shouldn't either. This is a translation that lets the Sutra's own revolution speak: first you think this is a man's world, then you discover it's not, and that discovery IS the teaching.
'''

    if translator_insertion_marker in text:
        text = text.replace(translator_insertion_marker, translator_insertion_marker + '\n' + translator_new_paragraph)
        changes_made.append("Added gender strategy paragraph to Translator's Note")

    return text, changes_made

def apply_phase_3_edits(text):
    """
    PHASE 3: LOW PRIORITY - Consistency polish
    """
    changes_made = []

    # Verify women are visible - just check, don't change
    women_markers = [
        'Mahāprajāpatī',
        'Yaśodharā',
        'dragon girl',
        'eight thousand nuns',
    ]

    for marker in women_markers:
        count = text.count(marker)
        changes_made.append(f"Verified '{marker}' appears {count} times")

    return text, changes_made

def main():
    input_file = '/Users/williamaltig/claudeprojects/Lotus_Sutra/Blues_version_of_the_Lotus_Sutra_-_CLEAN2.txt'
    output_file = '/Users/williamaltig/claudeprojects/Lotus_Sutra/Blues_version_of_the_Lotus_Sutra_-_GENDER_INCLUSIVE.txt'

    print("Reading file...")
    text = read_file(input_file)

    print("\n=== PHASE 1: HIGH PRIORITY ===")
    text, changes = apply_phase_1_edits(text)
    for change in changes:
        print(f"  ✓ {change}")

    print("\n=== PHASE 2: MEDIUM PRIORITY ===")
    text, changes = apply_phase_2_edits(text)
    for change in changes:
        print(f"  ✓ {change}")

    print("\n=== PHASE 3: LOW PRIORITY ===")
    text, changes = apply_phase_3_edits(text)
    for change in changes:
        print(f"  ✓ {change}")

    print("\nWriting revised file...")
    write_file(output_file, text)

    print(f"\n✅ Complete! Revised file written to:")
    print(f"   {output_file}")
    print(f"\n📊 Original file: {len(text.splitlines())} lines")

if __name__ == '__main__':
    main()
