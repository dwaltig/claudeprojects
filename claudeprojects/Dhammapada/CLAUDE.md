# CLAUDE.md - Dhammapada Translation Project

## Project Overview

The **Dhammapada Translation Project** is a scholarly and vernacular dual-translation effort for one of Buddhism's most beloved and widely-read texts. The Dhammapada ("Path of Dharma") comprises 423 verses in Pali. Originally transmitted in 26 chapters, this project has **reconstructed the text into 28 chapters** based on internal structural analysis and comparative evidence from the Sanskrit Udānavarga.

**Key Components:**
- **Source Text**: Pali (Theravada tradition) with metrical notation
- **Dual Translation**: Scholarly (academic with extensive footnotes) + Blues Vernacular (accessible)
- **Structure**: Reconstructed 28-Chapter Lunar Cycle (Original 26 + 2 new chapters split from Ch. 14 and Ch. 26)
- **Agent System**: Specialized AI personas for translation and review

---

## Critical Safety Protocol

**READ BEFORE EDITING:**
- **Preserve Scholarship**: Handle all text with extreme care
- **Verify Encodings**: Ensure UTF-8 and correct Pali diacritics (ṁ, ñ, ū, ā, ī, ṭ, ḍ, ṇ)
- **Ask First**: Confirm structural changes with the user
- **Document Everything**: Update session notes and status files

---

## Directory Structure

### Root Directory (`/Dhammapada/`)
- `CLAUDE.md`: **The Authoritative Guide** - Read this first
- `GEMINI.md`: AI agent context
- `01_TRANSLATIONS/`: Completed translation files
- `02_SOURCE_MATERIALS/`: Original Pali text with metrical scansion
- `03_DOCUMENTATION/`: Session notes, planning docs, status tracking
- `04_AGENTS/`: Specialized agent system prompts

---

## Specialized Agents

### The Professor (Dr. Rajesh Patel)
**Role**: Scholarly Translation
- Creates academic English translation with extensive footnotes
- Provides philosophical depth and cross-references
- Ensures doctrinal accuracy
- Contextualizes verses within broader Buddhist thought
- **File**: `04_AGENTS/The_Professor.md`

### The Bluesman (Master John Kim)
**Role**: Blues Vernacular Translation
- Reviews Professor's work for completeness
- Creates Blues idiom interpretation
- Ensures theological depth in accessible language
- Maintains the poetic power of the original verses
- **File**: `04_AGENTS/The_Bluesman.md`

---

## Translation Workflow

### Standard Process
1. **Professor translates** Pali → Scholarly English
2. **Bluesman reviews** Professor's translation for missed nuances
3. **Bluesman creates** Blues vernacular version
4. **Consolidation**: Both versions combined into chapter files

### Quality Assurance
- Cross-reference with traditional translations (Muller, Thanissaro, etc.)
- Verify Pali terms and diacritics
- Ensure philosophical consistency
- Maintain poetic structure in Blues version

---

## The Dhammapada: Special Considerations

### Unique Features
- **Verse Format**: Brief, memorable teachings (2-4 lines each)
- **Practical Ethics**: Emphasis on moral conduct and right action
- **Twin Verses**: Opening chapter uses pairs to contrast good/evil
- **Accessibility**: Designed for memorization and daily practice

### Translation Challenges
- **Poetic Compression**: Dense meaning in few words
- **Pali Wordplay**: Preserving etymology and resonance
- **Metrical Structure**: Respecting traditional scansion
- **Cultural Context**: Indian Buddhist concepts → English/Blues idiom

---

## File Naming Conventions

- Scholarly: `Chapter_[N]_[Title]_Scholarly.md`
- Blues: `Chapter_[N]_[Title]_Blues.md`
- Combined: `Chapter_[N]_[Title]_Complete.md`
- Source: `Dhammapada_Pali_Chapter_[N].txt`

Example: `Chapter_01_Yamakavagga_Scholarly.md`

---

## Chapter Overview (28 Reconstructed Chapters)

1. **Yamakavagga** (Twin Verses) - Good/evil, mind, karma
2. **Appamādavagga** (Heedfulness) - Vigilance and awareness
3. **Cittavagga** (Mind) - Training the mind
4. **Pupphavagga** (Flowers) - Impermanence
5. **Bālavagga** (Fools) - Folly and its consequences
6. **Paṇḍitavagga** (Wise) - Wisdom and the wise
7. **Arahantavagga** (Arahants) - The enlightened ones
8. **Sahassavagga** (Thousands) - Quality over quantity
9. **Pāpavagga** (Evil) - Avoiding unwholesome actions
10. **Daṇḍavagga** (Violence) - Non-harming
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

---

## Common Workflows

### Starting a New Chapter
1. Read `CLAUDE.md` for project overview
2. Check `03_DOCUMENTATION/COMPLETION_STATUS.md` for current progress
3. Review agent files in `04_AGENTS/`
4. Access source text in `02_SOURCE_MATERIALS/`
5. Follow dual-agent workflow (Professor → Bluesman)

### Documentation Updates
- Update `03_DOCUMENTATION/SESSION_NOTES_[DATE].md` after each session
- Update `03_DOCUMENTATION/COMPLETION_STATUS.md` when chapters complete
- Note any translation decisions or challenges

---

## Technical Context

- **Language**: Pali → English (scholarly + vernacular)
- **Encoding**: UTF-8 (preserve Pali diacritics)
- **Format**: Markdown for all translation files
- **Version Control**: Git recommended for tracking changes

---

## Getting Started

1. **Read** `CLAUDE.md` - The project bible
2. **Check** `03_DOCUMENTATION/COMPLETION_STATUS.md` - Current status
3. **Review** agent files in `04_AGENTS/` - Understand the personas
4. **Examine** source text structure in `02_SOURCE_MATERIALS/`
5. **Begin** with Professor translation, then Bluesman review

---

## Key Pali Terms

Familiarize yourself with these core concepts:

- **Dhamma** (धम्म): The teaching, truth, nature, phenomena
- **Kamma** (कम्म): Action, karma
- **Citta** (चित्त): Mind, consciousness
- **Paññā** (पञ्ञा): Wisdom, understanding
- **Mettā** (मेत्ता): Loving-kindness
- **Nibbāna** (निब्बान): Nirvana, liberation
- **Saṅkhārā** (सङ्खारा): Formations, conditioned phenomena

---

**Project Initialized**: 2025-12-05  
**Current Status**: Reconstructed 28-Chapter Structure Implemented (2026-01-12)