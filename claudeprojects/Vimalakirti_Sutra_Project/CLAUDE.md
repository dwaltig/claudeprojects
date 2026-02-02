# Vimalakirti Sutra Translation Project

## Project Overview

This directory contains a dual-agent translation project for the **Vimalakirti Sutra** (維摩詰所說經), one of the most philosophically profound Mahayana Buddhist texts. The project produces two parallel translations:

1. **Scholarly Translation**: Academic, philosophically rigorous translation with extensive footnotes
2. **Blues Vernacular Translation**: African-American Blues idiom interpretation for accessibility

## Source Text

- **Original**: Classical Chinese (Kumarajiva translation, T0475)
- **Structure**: 3 volumes, 14 chapters
- **Location**: `02_SOURCE_MATERIALS/T0475.txt/`

## Directory Structure

```
Vimalakirti_Sutra_Project/
├── 01_TRANSLATIONS/          # Completed translation files
├── 02_SOURCE_MATERIALS/      # Original Classical Chinese text
├── 03_DOCUMENTATION/         # Project documentation, session notes
├── 04_AGENTS/               # Specialized agent system prompts
└── .agent/workflows/        # Translation workflow definitions
```

## Translation Workflow

### The Dual-Agent System

**The Professor (Dr. Rajesh Patel)**
- Creates scholarly translation with footnotes
- Provides philosophical depth and cross-references
- Ensures doctrinal accuracy

**The Bluesman (Master John Kim)**
- Creates Blues vernacular interpretation
- Reviews Professor's work for missed nuances
- Ensures theological depth in accessible language

### Standard Process

1. **Professor translates** from Classical Chinese → English (scholarly)
2. **Bluesman reviews** Professor's translation for completeness
3. **Bluesman creates** Blues vernacular version
4. **Both versions** are consolidated into chapter files

## Chapter Structure (14 Chapters)

1. 佛國品 - Buddha Land
2. 方便品 - Skillful Means
3. 弟子品 - Disciples
4. 菩薩品 - Bodhisattvas
5. 文殊師利問疾品 - Manjushri Inquires About the Illness
6. 不思議品 - Inconceivable
7. 觀眾生品 - Observing Sentient Beings
8. 佛道品 - Buddha Path
9. 入不二法門品 - Entering the Dharma Gate of Non-Duality
10. 香積佛品 - Accumulated Fragrance Buddha
11. 菩薩行品 - Bodhisattva Practices
12. 見阿閦佛品 - Seeing Akshobhya Buddha
13. 法供養品 - Dharma Offering
14. 囑累品 - Entrusting

## File Naming Convention

- Scholarly: `Chapter_[N]_[Title]_Scholarly.md`
- Blues: `Chapter_[N]_[Title]_Blues.md`
- Combined: `Chapter_[N]_[Title]_Complete.md`

## Key Principles

1. **Preserve Scholarship**: This is months of careful work
2. **Verify Encodings**: Ensure UTF-8 and correct Sanskrit diacritics
3. **Ask First**: Confirm structural changes with the user
4. **Document Progress**: Update session notes and completion status

## Special Considerations

The Vimalakirti Sutra features:
- **Dharma Combat**: Brilliant dialectical exchanges
- **Non-Duality**: Central philosophical theme
- **Lay Buddhism**: Vimalakirti as enlightened layman
- **Skillful Means**: Multiple teaching methods

These themes require careful handling in both scholarly and vernacular translations.

## Current Status

Project initialized: 2025-11-30

See `03_DOCUMENTATION/COMPLETION_STATUS.md` for detailed progress tracking.
