# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains a manuscript translation project for the Lotus Sutra, a foundational Buddhist text. The primary content is an English translation with accompanying analysis documents.

## Repository Structure

```
/Lotus Sutra/
  ├── The Lotus Sutra English.txt    # Main translation manuscript (5,621 lines, 20+ chapters)
  └── Consistency_Analysis_Report.md # Detailed editorial analysis of the translation
```

## Working with the Translation

### File Format
- The main translation is in plain text format (.txt)
- 5,621 lines covering 20+ chapters
- Uses Sanskrit diacritical marks (ś, ṇ, ū, ā, ṃ) for proper names and terms
- Structured with chapter headings: "Chapter [Number]: [Title]"
- Contains both prose and verse sections

### Key Translation Elements

**Character Names (with diacritics):**
- Śāriputra, Mañjuśrī, Mahākāśyapa, Avalokiteśvara, Maitreya
- Always preserve exact diacritical marks when editing

**Standard Technical Terms:**
- Tathagata, Bodhisattva, Dharma, nirvāṇa, samādhi, śrāvaka
- Anuttara-samyak-sambodhi (supreme enlightenment)
- Maintain consistent capitalization (e.g., "Dharma" for teachings, "dharma" for phenomena)

**Formulaic Expressions:**
- Opening: "Thus have I heard. At one time, the Buddha was staying..."
- Verse transitions: "At that time, [Speaker], wishing to repeat this meaning, spoke in verse:"
- Buddha epithets: Full 10-fold epithet used in formal contexts

### Known Issues (from Analysis Report)

**CRITICAL: Stylistic Inconsistency**
- Prose sections: Formal Buddhist scriptural language (appropriate)
- Verse sections: Mixed styles including blues/gospel vernacular (problematic)
- Chapters 4-7, 15-19 particularly affected
- Contains informal language: contractions ("ain't", "gonna"), casual interjections, blues references

**Editorial Recommendations:**
- Maintain formal Buddhist scriptural tone throughout
- Remove vernacular contractions and colloquialisms from verses
- Eliminate blues/gospel stylistic markers
- Preserve elevated, reverent tone appropriate to sacred text

### Editing Guidelines

When making changes to the translation:

1. **Preserve Unicode diacritics** - Do not simplify names (e.g., never change Śāriputra to Sariputra)
2. **Maintain terminology consistency** - Use the established translation for recurring terms
3. **Check verse style** - Ensure verses match the formal tone of prose sections
4. **Respect Buddhist conventions** - Three-fold requests, formulaic openings, proper honorifics
5. **Line references** - When referencing specific passages, cite line numbers from the .txt file

### Character Encoding

- Files use UTF-8 encoding for proper display of Sanskrit diacriticals
- Ensure editor preserves Unicode characters when making edits
- Key Unicode characters: ś (U+015B), ṇ (U+1E47), ū (U+016B), ā (U+0101), ṃ (U+1E43)

## Analysis and Documentation

The `Consistency_Analysis_Report.md` provides comprehensive editorial analysis covering:
- Tone and style assessment
- Terminology consistency tracking
- Character name verification
- Chapter-by-chapter stylistic evaluation
- Detailed recommendations for revision

Reference this report when making editorial decisions about the translation.
