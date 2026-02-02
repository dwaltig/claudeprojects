#!/usr/bin/env python3
"""
Consolidate Śikṣāsamuccaya Blues chapters into complete audiobook manuscript.
Optimized for ElevenReader TTS production.
"""

import os
from pathlib import Path

def consolidate_audiobook():
    """Merge all 19 Blues chapters into single audiobook manuscript."""

    # Define chapter order
    chapters = [
        "Chapter_01_Danapramita_Blues_Complete.md",
        "Chapter_02_Saddharmaparigraha_Blues.md",
        "Chapter_03_Dharmabhanakadiraksa_Blues.md",
        "Chapter_04_Anarthavarjana_Blues.md",
        "Chapter_05_Silaparamita_Anarthavarjana_Blues.md",
        "Chapter_06_Atmabhavaraksa_Blues.md",
        "Chapter_07_Bhogapunyaraksa_Blues.md",
        "Chapter_08_Papasodhana_Blues.md",
        "Chapter_09_Ksantiparamita_Blues.md",
        "Chapter_10_Viryaparamita_Blues.md",
        "Chapter_11_Aranyasamshraya_Blues.md",
        "Chapter_12_Cittaparikarma_Blues.md",
        "Chapter_13_Smrtyupasthana_Blues.md",
        "Chapter_14_Atmabhavaparisuddhi_Blues.md",
        "Chapter_15_Bhogapunyasuddhi_Blues.md",
        "Chapter_16_Bhadracaryavidhi_Blues.md",
        "Chapter_17_Vandananusamsa_Blues.md",
        "Chapter_18_Ratnatrayanusmrti_Blues.md",
        "Chapter_19_Punyavrddhi_Blues.md"
    ]

    base_dir = Path("/Users/williamaltig/claudeprojects/Sutra_Projects/Shikshasamucchaya")
    chapters_dir = base_dir / "01_TRANSLATIONS"
    output_file = base_dir / "SHIKSHASAMUCCHAYA_COMPLETE_BLUES_AUDIOBOOK.md"

    # Front matter
    front_matter = """# The Śikṣāsamuccaya
## A Compendium of Training
### Blues Vernacular Translation by William Altig

---

*Śāntideva's 8th-century Buddhist manual, rendered through Delta Blues, Storefront Church, and the Road—for anyone who's ever tried to walk the dharma path with dust on their boots and doubt in their heart.*

---

## How to Listen to This Book

This is not light reading. This is not background noise.

This is a **training manual** for bodhisattvas—people who've decided to wake up not just for themselves, but for every living being they meet.

Śāntideva wrote this in 8th-century India, compiling quotations from hundreds of Mahāyāna sutras. I've translated it into American Blues vernacular because the dharma always sounds better when it's sung in the language of the road, the church, and the chain gang.

**Pacing**: Some chapters are short (5 minutes). Some are long (45 minutes). Don't rush. Let the teaching land.

**Repetition**: You'll hear the same teachings again and again. That's not a mistake—that's the method. The sutras repeat because we forget.

**Sanskrit terms**: I've kept some Buddhist technical terms (bodhisattva, dharma, nirvāṇa, samādhi). You'll learn them as you go. They're explained in context.

**Voice**: I'm speaking directly to you. This isn't academic. This is person-to-person transmission.

---

## Pronunciation Guide

**Common Sanskrit Terms** (approximate pronunciation):

- **Śāntideva**: SHAHN-tee-DAY-vah (the author)
- **Śikṣāsamuccaya**: SHIK-shah-sah-MOO-chah-yah (title: "Compendium of Training")
- **Bodhisattva**: BOH-dee-SAHT-vah (awakening being)
- **Dharma**: DAR-mah (teaching, truth, law)
- **Nirvāṇa**: neer-VAH-nah (liberation, peace)
- **Samādhi**: sah-MAH-dee (deep meditation)
- **Prajñā**: PRAH-nyah (wisdom)
- **Karuṇā**: kah-ROO-nah (compassion)

Don't worry if you don't get them perfect. The meaning matters more than the accent.

---

## About Śāntideva

Śāntideva lived in 8th-century India at Nālandā University, the greatest Buddhist center of learning in history.

Legend says he appeared lazy—sleeping all day, skipping classes. The monks got fed up and demanded he recite a teaching publicly to prove he belonged.

He stood up and recited the *Bodhicaryāvatāra* (Entering the Path of Awakening)—one of the greatest spiritual poems ever written—**from memory**.

The *Śikṣāsamuccaya* is the companion work: a massive anthology of sutra quotations that backs up every claim in the *Bodhicaryāvatāra* with scriptural evidence.

This is the text Śāntideva actually studied. This is the training manual.

---

## About This Translation

I've rendered Śāntideva's Sanskrit into **American Blues vernacular**—the language of Delta Blues, Storefront Church, Jazz Club, Chain Gang, and The Road.

Why Blues? Because:

1. **Blues is dharma music**. It's about suffering, impermanence, and finding freedom in the middle of it all.
2. **Blues is direct**. No pretense. No performance. Just truth.
3. **Blues is participatory**. Call-and-response. You're not a passive listener—you're in the conversation.
4. **Blues is concrete**. Instead of abstract philosophy, you get "hellhounds on my trail" and "body ain't got no landlord."
5. **Blues is sacred**. This isn't secular music. This is church. This is transmission.

If this style bothers you, there are scholarly translations available. But if you're tired of Buddhist texts that sound like philosophy textbooks, stick with me.

---

## Content Advisory

This text contains:

- References to death, suffering, and the hell realms (Buddhist cosmology)
- Extreme acts of devotion (e.g., Sadāprarudita selling his own flesh)
- Graphic descriptions of impermanence and bodily decay
- Strong language appropriate to Blues register ("ain't," "gonna," vernacular speech)

This is sacred literature, but it's not sanitized. Buddhism doesn't sugarcoat suffering.

If you're looking for feel-good spirituality, this isn't it.
If you're looking for the real thing, welcome.

---

## Let's Begin

**19 chapters. 8-10 hours of training.**

Take your time. Walk the road. Trust the teachings.

And remember: you're not alone on this path.

---

"""

    # Write front matter
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(front_matter)
        outfile.write("\n\n" + "="*80 + "\n")
        outfile.write("# THE NINETEEN CHAPTERS\n")
        outfile.write("="*80 + "\n\n")

        # Process each chapter
        for i, chapter_file in enumerate(chapters, 1):
            chapter_path = chapters_dir / chapter_file

            if not chapter_path.exists():
                print(f"WARNING: Chapter file not found: {chapter_file}")
                continue

            print(f"Processing Chapter {i:02d}: {chapter_file}")

            # Add chapter divider
            outfile.write("\n\n" + "-"*80 + "\n")
            outfile.write(f"## AUDIO CHAPTER {i:02d}\n")
            outfile.write("-"*80 + "\n\n")

            # Read and append chapter content
            with open(chapter_path, 'r', encoding='utf-8') as infile:
                chapter_content = infile.read()
                outfile.write(chapter_content)

            outfile.write("\n\n")

        # Back matter
        back_matter = """
---

# EPILOGUE: The Road Ahead

You've walked through 19 chapters of Śāntideva's training manual.

You've heard about:
- Giving everything away (Chapter 1)
- Holding on to what's real (Chapter 2)
- Protecting the preachers (Chapter 3)
- Avoiding harm (Chapter 4)
- Living with discipline (Chapter 5)
- Protecting your body and your merit (Chapters 6-7)
- Purifying your evil (Chapter 8)
- Practicing patience and effort (Chapters 9-10)
- Going to the Woodshed—the forest—to find freedom (Chapter 11)
- Preparing your mind and watching it closely (Chapters 12-13)
- Purifying everything you've got (Chapters 14-15)
- Conducting yourself properly (Chapter 16)
- Worshiping with your whole heart (Chapter 17)
- Remembering the Three Jewels (Chapter 18)
- Increasing your merit (Chapter 19)

That's the training. That's the path.

Now the question is: **What are you gonna do with it?**

---

## The Bodhisattva Vow (Simplified)

If this teaching has moved you, consider taking the vow:

> **I vow to wake up—not just for myself, but for all beings.**
> **I vow to walk the road—no matter how long it takes.**
> **I vow to hold the dharma—and never let it go.**

That's it. That's the whole thing.

Everything else is just commentary.

---

## Acknowledgments

**Śāntideva** (8th c. CE) - For compiling this training manual and trusting us to use it.

**The Mahāyāna Sutras** - For providing the source quotations Śāntideva drew from.

**Cecil Bendall & W.H.D. Rouse** (1922) - For the first English translation, which laid the groundwork.

**The Blues Tradition** - Delta Blues, Storefront Church, Chain Gang songs, and The Road—for teaching me how dharma sounds in American English.

**You, the listener** - For trusting this unconventional approach and walking the 19 chapters with me.

---

## About the Translator

**William Altig** is a scholar, translator, and practitioner working at the intersection of Buddhist studies and American vernacular spirituality.

His translations include the *Lotus Sutra* (Blues edition), the *Vimalakīrti Sutra*, and now the *Śikṣāsamuccaya*—all rendered in Blues/gospel register to make Mahāyāna Buddhism accessible to contemporary American audiences.

He believes the dharma always sounds better when it's sung.

---

## Colophon

**Title**: *The Śikṣāsamuccaya: A Compendium of Training*
**Author**: Śāntideva (8th c. CE)
**Translator**: William Altig
**Translation Style**: Blues Vernacular
**Completion Date**: January 2026
**Audio Production**: ElevenReader TTS (ElevenLabs)
**Duration**: Approximately 8-10 hours

**Source Text**: Sanskrit *Śikṣāsamuccaya* (ed. Bendall, 1902)
**Reference Translation**: Bendall & Rouse (1922)

---

*Thus ends the Śikṣāsamuccaya—A Compendium of Training.*

*May all beings benefit.*
*May all beings wake up.*
*May all beings walk the road home.*

**Dedicated to the liberation of all beings.**

---

"""

        outfile.write(back_matter)

    print(f"\n✅ Consolidation complete!")
    print(f"📄 Output file: {output_file}")
    print(f"📊 Total chapters processed: {len(chapters)}")

    # Calculate file size
    file_size = output_file.stat().st_size
    print(f"📦 File size: {file_size:,} bytes ({file_size / 1024:.1f} KB)")

    return output_file

if __name__ == "__main__":
    consolidate_audiobook()
