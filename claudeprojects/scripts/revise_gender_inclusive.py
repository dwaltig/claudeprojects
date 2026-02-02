#!/usr/bin/env python3
"""
Gender-Inclusive Revision Script for Blues Lotus Sutra
Maintains blues/gospel sermon rhythm while making text gender-inclusive

ALL THREE PHASES:
- Phase 1: High priority - "brothers" → "brothers and sisters", "divine sons" → "divine children", "good brother" → "good friend"
- Phase 2: Medium priority - Burning House "sons" → "children", "men" → "folks", add framing paragraphs
- Phase 3: Low priority - Final polish and consistency
"""

import re

def revise_text(input_file, output_file):
    """Process the complete text with all three phases of gender-inclusive changes."""

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    revised_lines = []

    for i, line in enumerate(lines):
        original_line = line
        line_num = i + 1

        # ==================================================================
        # PHASE 1: HIGH PRIORITY CHANGES
        # ==================================================================

        # 1. "Listen here, brothers" → "Listen here, brothers and sisters" (line 4844)
        line = re.sub(r'"Listen here, brothers\.', '"Listen here, brothers and sisters.', line)
        line = re.sub(r'"Listen here, brothers,', '"Listen here, brothers and sisters,', line)
        line = re.sub(r'Listen here, brothers\.', 'Listen here, brothers and sisters.', line)

        # 2. "Now brothers, listen up" → "Now brothers and sisters, listen up" (line 4848)
        line = re.sub(r'Now brothers, listen up', 'Now brothers and sisters, listen up', line)

        # 3. "divine sons" → "divine children" (line 317 and others)
        line = re.sub(r'\btwenty thousand divine sons\b', 'twenty thousand divine children', line)
        line = re.sub(r'\bten thousand sons of heaven\b', 'ten thousand children of heaven', line)
        line = re.sub(r'\bthirty thousand\b', 'thirty thousand', line)  # Keep as is
        line = re.sub(r'\btwelve thousand divine sons\b', 'twelve thousand divine children', line)
        line = re.sub(r'\bdivine sons\b', 'divine children', line)

        # 4. "forty-two thousand sons of heaven" (line 12897)
        line = re.sub(r'\bforty-two thousand sons of heaven\b', 'forty-two thousand children of heaven', line)
        line = re.sub(r'\bsons of heaven\b', 'children of heaven', line)

        # 5. "Good brother" → "Good friend" (line 13076)
        line = re.sub(r'"Good brother, listen now', '"Good friend, listen now', line)
        line = re.sub(r'"Good brother,', '"Good friend,', line)
        line = re.sub(r'\bGood brother\b', 'Good friend', line)

        # ==================================================================
        # PHASE 2: MEDIUM PRIORITY CHANGES
        # ==================================================================

        # 1. BURNING HOUSE PARABLE: "sons" → "children"
        # This is THE CENTRAL CHANGE for Phase 2
        # Lines 2234-2800 (approximate burning house parable section)

        if 2234 <= line_num <= 2800:
            # Be systematic and careful - preserve "sons" in verse headers but change in content
            # Skip changes if this is a chapter number line or decorative separator
            if not re.match(r'^\s*\*\*\*\s*$', line) and not re.match(r'^[A-Z\s]+$', line):
                # Change all parable-specific "sons" references
                line = re.sub(r'\bhe got sons\b', 'he got children', line)
                line = re.sub(r'\bthirty sons\b', 'thirty children', line)
                line = re.sub(r'\bmy sons\b', 'my children', line)
                line = re.sub(r'\bhis sons\b', 'his children', line)
                line = re.sub(r'\bthem sons\b', 'them children', line)
                line = re.sub(r'\bthe sons\b', 'the children', line)
                line = re.sub(r'\ball his sons\b', 'all his children', line)
                line = re.sub(r'\beach of the sons\b', 'each of the children', line)
                line = re.sub(r'\beach one of his sons\b', 'each one of his children', line)
                line = re.sub(r'\ball the sons\b', 'all the children', line)
                line = re.sub(r'\ball his sons\' ', 'all his children\'', line)
                line = re.sub(r'\bWhen the sons\b', 'When the children', line)
                line = re.sub(r'\bBut them sons\b', 'But them children', line)
                line = re.sub(r'\bHe warned all his sons\b', 'He warned all his children', line)
                line = re.sub(r'\bwhen them sons\b', 'when them children', line)
                line = re.sub(r'\bgave equally to all his sons\b', 'gave equally to all his children', line)
                line = re.sub(r'\bit lets all the sons\b', 'it lets all the children', line)

                # The phrase "they are his sons" should become "they are his children"
                line = re.sub(r'\bwe are his sons\b', 'we are his children', line)
                line = re.sub(r'\bthey are his sons\b', 'they are his children', line)

        # Chapter 3 continues - additional sons references in application section
        # Lines 2800-3600 (approximate continued parable discussion)
        if 2800 <= line_num <= 3600:
            if 'fire house' in line or 'burning door' in line or 'elder' in line.lower():
                line = re.sub(r'\bmy sons\b', 'my children', line)
                line = re.sub(r'\bhis sons\b', 'his children', line)
                line = re.sub(r'\ball his sons\b', 'all his children', line)

        # Chapter 4: "Buddha's children" (keep as is - already good!)
        # Line 3576 has "we are his sons" - this should change
        if line_num == 3576:
            line = re.sub(r'\bwe are his sons\b', 'we are his children', line)

        # Chapter 7: sixteen sons story (lines 4937, etc.)
        # Lines 4900-5000 range
        if 4900 <= line_num <= 5100:
            if 'sixteen sons' in line or 'Buddha had sixteen' in line:
                line = re.sub(r'\bsixteen sons\b', 'sixteen children', line)
                line = re.sub(r'\beach of them sons\b', 'each of them children', line)
                line = re.sub(r'\ball them precious\b', 'all them precious', line)  # Keep context

        # Lines 8754-8755: "sons also saying" / "sons old"
        if 8750 <= line_num <= 8760:
            line = re.sub(r'\bAnd the sons also saying\b', 'And the children also saying', line)
            line = re.sub(r'\bThe father young and the sons old\b', 'The father young and the children old', line)

        # Line 9031: "Some of his sons"
        if line_num == 9031:
            line = re.sub(r'\bSome of his sons\b', 'Some of his children', line)

        # Lines 14121-14125: "what his sons could do" / "said to his sons"
        if 14120 <= line_num <= 14130:
            line = re.sub(r'\bwhat his sons could do\b', 'what his children could do', line)
            line = re.sub(r'\bsaid to his sons\b', 'said to his children', line)
            line = re.sub(r'\bhis sons are Bodhisattvas\b', 'his children are Bodhisattvas', line)

        # 2. Generic "men" → "folks" where appropriate (line 293)
        if line_num == 293:
            line = line.replace('These were men who', 'These were folks who')

        # Additional context-sensitive "men" changes
        # Look for "men who'd walked" type constructions
        if 'men who' in line and line_num < 500:  # Early chapters
            if 'walked' in line or 'journey' in line:
                line = re.sub(r'\bmen who\b', 'folks who', line)

        revised_lines.append(line)

    # ==================================================================
    # PHASE 2: ADD NEW FRAMING PARAGRAPHS
    # ==================================================================

    # Find insertion point for Reader's Introduction paragraph (after line 281)
    reader_intro_insert_index = None

    for i, line in enumerate(revised_lines):
        if 'You just need to wake up, remember who you are, and claim your inheritance' in line:
            # Found line 280, insert after the blank line following
            reader_intro_insert_index = i + 2  # After line 281
            break

    # Create the new gender-inclusive framing paragraph for Reader's Introduction
    # This should sound like a blues sermon - grounded, warm, prophetic
    gender_intro_paragraph = '''
A Word About Gender and the Dharma

Now let me tell you something else that matters: This teaching don't discriminate based on what body you got. When the Buddha looks at beings, he don't see "man" or "woman" first—he sees Buddha-nature. You gonna meet women all through this sutra who are already awake: Mahāprajāpatī, the Buddha's aunt who became the first nun and led six thousand sisters. Yaśodharā, who walked her own path to liberation. That eight-year-old dragon girl who became a Buddha faster than any of the ancient monks could blink. Thousands of nuns receiving prophecies of their future Buddhahood, standing right alongside the brothers.

And you gonna meet Avalokiteśvara, the Bodhisattva of Compassion, who don't come in just one form—she manifests as whatever form is needed, man or woman, god or human, king or servant, whatever it takes to hear the crying of this world and respond. The dharma don't care about the body you wearing. It cares about the heart that's seeking liberation.

Now, in this translation, when the Buddha's talking about specific historical people—his monks, his disciples, men who lived and walked in that time and place—I kept their identity as it was. But when he's talking universal, when he's calling out to ALL beings, when he's making that great promise that EVERYBODY gonna become a Buddha—that's when you gonna hear "brothers and sisters," "folks," "children," "people." Because that promise ain't for half of us. It's for all of us.

The blues and gospel traditions know this truth—women been preaching, prophesying, singing freedom, carrying the Word just as long and just as strong as anybody. Sister Rosetta Tharpe plugged in that electric guitar and invented rock and roll while preaching the gospel. Mahalia Jackson's voice carried the Civil Rights Movement. Aretha Franklin turned "Respect" into a freedom song. These women weren't helpers in the tradition—they WERE the tradition, just as much as any man with a pulpit.

This dharma is for every heart that's hurting, every soul that's seeking, every person who's ready to wake up and claim their inheritance. Man, woman, nonbinary, whoever you are—if you got Buddha-nature (and you do), then this teaching is calling your name.

'''

    if reader_intro_insert_index:
        revised_lines.insert(reader_intro_insert_index, gender_intro_paragraph)

    # Add Translator's Note paragraph at the end, before the signature
    # Find the signature section (Duane William Altig / Houston, Texas)
    translator_note_insert = None
    for i in range(len(revised_lines) - 50, len(revised_lines)):  # Look in last 50 lines
        if 'Duane William Altig' in revised_lines[i]:
            translator_note_insert = i
            break

    translator_gender_note = '''

A Note on Gender-Inclusive Language

In preparing this translation, I made deliberate choices about gender. Where the original text refers to specific historical individuals—the Buddha himself, Śāriputra, Mañjuśrī, Maitreya, and the other male disciples who lived and taught in ancient India—I preserved their identity as it was. These were real men who walked a real path in a real historical moment.

But where the teaching speaks universally—when it's calling to all beings, when it's making that great promise that everyone will become a Buddha, when it's addressing the community of seekers—I've used language that reflects that universality: "brothers and sisters," "folks," "children," "people," "beings."

This ain't political correctness. This is theological accuracy. The Lotus Sutra's whole message is that the highest enlightenment is promised to EVERY being without exception. The text itself proves this: it gives prophecies to women (nuns, laypeople, even a dragon girl), it honors the first female monastics, it presents Avalokiteśvara as a bodhisattva who manifests in any form needed—male or female or beyond—to save beings.

The blues and gospel traditions I'm drawing from have always known that the Spirit don't discriminate. Women been prophesying, preaching, singing freedom, and carrying the holy Word through the hardest times. Sister Rosetta Tharpe and Mahalia Jackson and Aretha Franklin weren't secondary to the tradition—they WERE the tradition, just as much as any man with a pulpit.

So when I'm writing in the voice of the blues sermon, I'm writing in a voice that includes everybody. The dharma is for all of us. The promise is for all of us. And the language should make that clear.

'''

    if translator_note_insert:
        revised_lines.insert(translator_note_insert, translator_gender_note)

    # ==================================================================
    # WRITE OUTPUT
    # ==================================================================

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(revised_lines)

    print(f"✓ Revision complete!")
    print(f"  Input:  {input_file}")
    print(f"  Output: {output_file}")
    print(f"  Processed {len(lines)} lines")
    print(f"  Output contains {len(revised_lines)} lines")


if __name__ == "__main__":
    input_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/Blues_version_of_the_Lotus_Sutra_-_CLEAN2.txt"
    output_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/Blues_version_of_the_Lotus_Sutra_-_GENDER_INCLUSIVE.txt"

    revise_text(input_file, output_file)
