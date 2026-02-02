# GEMINI.md - Dhammapada Translation Project

## 1. Project Overview

The **Dhammapada Translation Project** is a scholarly and vernacular dual-translation effort for the Dhammapada, one of the most widely-read Buddhist texts. The Dhammapada contains 423 verses. Originally transmitted in 26 chapters, this project has **reconstructed the text into 28 chapters** based on structural analysis and comparative evidence from the Sanskrit Udānavarga.

**Key Components:**
*   **Source Text:** Pali with metrical scansion notation
*   **Dual Translation:** Scholarly (Academic) + Blues Vernacular (Accessible)
*   **Structure:** Reconstructed 28-Chapter Lunar Cycle (Original 26 + 2 new chapters split from Ch. 14 and Ch. 26).
*   **Agent System:** Specialized AI personas (Professor & Bluesman)

## 2. Critical Safety Protocol

**READ BEFORE EDITING:**
*   **Preserve Scholarship:** Handle all text with extreme care
*   **Verify Encodings:** Ensure UTF-8 and correct Pali diacritics (ṁ, ñ, ū, ā, ī, ṭ, ḍ, ṇ)
*   **Ask First:** Confirm structural changes with the user
*   **Document Everything:** Update session notes and status files

## 3. Directory Structure & Key Files

### Root Directory (`/Dhammapada/`)
*   `CLAUDE.md`: **The Authoritative Guide** - Read this first
*   `GEMINI.md`: This file - AI agent context
*   `01_TRANSLATIONS/`: Completed translation files
*   `02_SOURCE_MATERIALS/`: Original Pali text with metrical notation
*   `03_DOCUMENTATION/`: Session notes, planning docs, status tracking
    *   `DHAMMAPADA_GLOSSARY_HYBRID.md`: The authoritative Scholarly/Blues terminology bridge
*   `04_AGENTS/`: Specialized agent system prompts

## 4. Specialized Agents

### The Professor (Dr. Rajesh Patel)
**Role:** Scholarly Translation
*   Creates academic English translation with extensive footnotes
*   Provides philosophical depth and cross-references
*   Ensures doctrinal accuracy
*   **File:** `04_AGENTS/The_Professor.md`

### The Bluesman (Master John Kim)
**Role:** Blues Vernacular Translation
*   Reviews Professor's work for completeness
*   Creates Blues idiom interpretation
*   Ensures theological depth in accessible language
*   **File:** `04_AGENTS/The_Bluesman.md`

## 5. Translation Workflow

### Standard Process
1.  **Professor translates** Pali → Scholarly English
2.  **Bluesman reviews** Professor's translation for missed nuances
3.  **Bluesman creates** Blues vernacular version
4.  **Consolidation:** Both versions combined into chapter files

### Quality Assurance
*   Cross-reference with other translations (Muller, Thanissaro, Buddharakkhita, etc.)
*   Verify Pali terms and diacritics
*   Ensure philosophical consistency
*   Maintain poetic power in Blues version

## 6. The Dhammapada: Special Considerations

### Unique Features
*   **Verse Format:** Brief, memorable teachings (typically 2-4 lines)
*   **Practical Ethics:** Emphasis on moral conduct and daily practice
*   **Twin Verses:** Opening chapter uses contrasting pairs (good/evil, wise/foolish)
*   **Memorability:** Designed for oral transmission and recitation

### Translation Challenges
*   **Poetic Compression:** Dense meaning packed into few words
*   **Pali Wordplay:** Preserving etymological connections
*   **Metrical Structure:** Respecting traditional prosody
*   **Cultural Context:** Indian Buddhist concepts → English/Blues idiom

## 7. File Naming Conventions

*   Scholarly: `Chapter_[N]_[Title]_Scholarly.md`
*   Blues: `Chapter_[N]_[Title]_Blues.md`
*   Combined: `Chapter_[N]_[Title]_Complete.md`
*   Source: `Dhammapada_Pali_Chapter_[N].txt`

Example: `Chapter_01_Yamakavagga_Complete.md`

## 8. Chapter Overview (28 Reconstructed Chapters)

1.  **Yamakavagga** (Twin Verses)
2.  **Appamādavagga** (Heedfulness)
3.  **Cittavagga** (Mind)
4.  **Pupphavagga** (Flowers)
5.  **Bālavagga** (Fools)
6.  **Paṇḍitavagga** (Wise)
7.  **Arahantavagga** (Arahants)
8.  **Sahassavagga** (Thousands)
9.  **Pāpavagga** (Evil)
10. **Daṇḍavagga** (Violence)
11. **Jarāvagga** (Old Age)
12. **Attavagga** (Self)
13. **Lokavagga** (World)
14. **Buddhavagga** (The Buddha) - *Split 1/2*
15. **Tathāgatavagga** (The Tathagata) - *Split 2/2 (New)*
16. **Sukhavagga** (Happiness) - *Shifted from 15*
...
26. **Bhikkhuvagga** (The Monk) - *Shifted from 25*
27. **Nibbānavagga** (Nirvana) - *Split 1/2 (New)*
28. **Brāhmaṇavagga** (The Brahmin) - *Split 2/2*

## 9. Common Workflows

### Starting a New Chapter
1.  Read `CLAUDE.md` for project overview
2.  Check `03_DOCUMENTATION/COMPLETION_STATUS.md` for current progress
3.  Review agent files in `04_AGENTS/`
4.  Access source text in `02_SOURCE_MATERIALS/`
5.  Follow dual-agent workflow (Professor → Bluesman)

### Documentation Updates
*   Update `03_DOCUMENTATION/SESSION_NOTES_[DATE].md` after each session
*   Update `03_DOCUMENTATION/COMPLETION_STATUS.md` when chapters complete
*   Note any translation decisions or challenges

## 10. Technical Context

*   **Language:** Pali → English (scholarly + vernacular)
*   **Encoding:** UTF-8 (preserve Pali diacritics)
*   **Format:** Markdown for all translation files
*   **Version Control:** Git recommended for tracking changes

## 11. Getting Started

1.  **Read** `CLAUDE.md` - The project bible
2.  **Check** `03_DOCUMENTATION/COMPLETION_STATUS.md` - Current status
3.  **Review** agent files in `04_AGENTS/` - Understand the personas
4.  **Examine** source text structure in `02_SOURCE_MATERIALS/`
5.  **Begin** with Professor translation, then Bluesman review

## 12. Key Pali Terms

Familiarize yourself with these core concepts:

*   **Dhamma** (धम्म): The teaching, truth, law, nature
*   **Kamma** (कम्म): Action, karma, volitional deed
*   **Citta** (चित्त): Mind, consciousness, heart
*   **Paññā** (पञ्ञा): Wisdom, discernment, understanding
*   **Mettā** (मेत्ता): Loving-kindness, benevolence
*   **Nibbāna** (निब्बान): Nirvana, liberation, extinction
*   **Saṅkhārā** (सङ्खारा): Formations, conditioned phenomena

---

## 13. Song Production Guidelines (05_SONGS)

### Key Rules
*   **No Buddha references in lyrics:** Songs should let the truth speak for itself without religious attribution. Avoid "The Buddha said..." or similar phrases in lyrics, outros, and spoken sections.
*   **Universal wisdom:** Present teachings as timeless truth, not doctrinal Buddhism.
*   **Blues authenticity:** Keep the vernacular genuine to Blues tradition.

### Song Package Components
Each song should include:
1.  Teaching exposition (Pali source + interpretation)
2.  Full lyrics with verse/chorus/bridge structure
3.  Suno production brief and prompts
4.  Cover art brief and image prompts
5.  SoundCloud description
6.  YouTube description
7.  Facebook/Instagram posts
8.  SEO tags and hashtags
9.  Agent credits

---

**Project Initialized:** 2025-12-05  
**Current Status:** Reconstructed 28-Chapter Structure Implemented (2026-01-12)