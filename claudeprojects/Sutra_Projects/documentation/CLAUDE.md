# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains Buddhist sutra translation projects, including traditional scholarly translations and experimental "blues" vernacular translations. The focus is on translating and publishing foundational Buddhist texts (Mahayana sutras) in accessible and contemporary English styles.

## Repository Structure

```
/Sutra Projects/
  ├── Immeasurable Meanings Sutra/
  │   ├── The Immeasurable Meanings Sutra - Blues Edition.md        # Master edition in markdown
  │   ├── The Immeasurable Meanings Sutra - Blues Edition - PUBLICATION READY.txt
  │   ├── Blues Immeasurable Meanings Sutra v3 - Complete.txt       # Latest complete version
  │   ├── Consistency_Analysis_Report.md                             # Editorial analysis
  │   ├── Flow_and_Pacing_Analysis_Report.md                         # Narrative rhythm analysis
  │   ├── Blues Immeasurable Meanings Sutra - Structural Elements.md # Design documentation
  │   ├── Immeasurable_Meanings_Sutra_Formatting_Guide.txt          # Print/digital formatting specs
  │   ├── Introduction to The Immeasurable Meanings Sutra- A Blues Translation.txt
  │   ├── Blues Immeasurable Meanings Sutra Glossory.txt            # Terminology reference
  │   ├── Chinese Immeasurable Meanings Sutra.txt                   # Source text in Chinese
  │   └── [other versions and working drafts]
  ├── Universal Worthy Bodhisattva Sutra/
  │   ├── Universal Worthy Bodhisattva Sutra - COMPLETE Blues Translation.txt
  │   └── Universal Worthy Bodhisattva Sutra - Blues Translation (Part 2).txt
  ├── Samantabhadra Practices Sutra/
  │   ├── 佛說觀普賢菩薩行法經 The Buddha Speaks of the Sutra...txt (Chinese source + translation)
  ├── Final_Sections_Blues_Translation.md                            # Work in progress sections
  └── [other project files]
```

## Working with Sutra Translations

### File Formats and Versions

- **Primary manuscripts:** `.txt` files (plain text with UTF-8 encoding for Sanskrit diacritics)
- **Editorial/Design documents:** `.md` files (markdown with analysis and structural notes)
- **Multiple versions:** Blues edition projects have v1, v2, v3 iterations showing revision progression
- **Status files:** "PUBLICATION READY" or "COMPLETE MANUSCRIPT" indicate final/near-final states

### Key Translation Standards

**Sanskrit Names and Terminology (with required diacritics):**
- Always preserve Unicode diacritical marks: ś (U+015B), ṇ (U+1E47), ū (U+016B), ā (U+0101), ṃ (U+1E43)
- Examples: Śāriputra, Mañjuśrī, Mahākāśyapa, Avalokiteśvara, Maitreya, Bodhisattva
- Buddhist technical terms: Tathagata, Dharma, nirvāṇa, samādhi, śrāvaka, Anuttara-samyak-sambodhi
- Maintain consistent capitalization (Dharma for Buddha's teachings, dharma for phenomena)

**Sutra Formulaic Elements:**
- Opening formula: "Thus have I heard. At one time, the Buddha was staying..."
- Verse transitions: "At that time, [Speaker], wishing to repeat this meaning, spoke in verse:"
- Buddha epithets: Full 10-fold epithet in formal contexts
- Request pattern: Three-fold requests by assembly members

### Project-Specific Issues and Standards

**The Immeasurable Meanings Sutra - Blues Edition:**
- Blues/vernacular translation intentionally uses informal contemporary language
- Maintains blues musical phrasing, call-and-response patterns, and vernacular contractions
- See `Consistency_Analysis_Report.md` for detailed style assessment
- Production specs in `Immeasurable_Meanings_Sutra_Formatting_Guide.txt` (6×9″ trade paperback, Georgia font, KDP standard)
- Formatting: Chapter headers with ✦ symbol, section dividers "— • —", drop caps, right-aligned verse

**The Lotus Sutra English Translation:**
- Formal Buddhist scriptural tone throughout (applies to Consistency_Analysis_Report.md in parent context)
- Critical issue: Verse sections incorrectly contain blues/vernacular language (should be formal)
- Diacritical marks: Generally consistent
- Terminology: Mostly consistent across chapters

**Editorial Reports:**
- `Consistency_Analysis_Report.md`: Tracks tone/style shifts, terminology consistency, character names, diacritical accuracy
- `Flow_and_Pacing_Analysis_Report.md`: Analyzes narrative rhythm, chapter pacing, thematic development
- These reports identify problem areas and provide specific line-number references

### Character Encoding

- All files use UTF-8 encoding for proper display of Sanskrit diacriticals
- Ensure editor preserves Unicode when making edits
- When copying text between files, verify diacritics remain intact

### Editing Guidelines

1. **Preserve Unicode diacritics** - Never simplify or remove (e.g., never change Śāriputra to Sariputra)
2. **Maintain terminology consistency** - Reference established translations in glossaries and analysis reports
3. **Check stylistic consistency** - Verify tone matches project scope (formal scholarly vs. blues vernacular)
4. **Verify verse formatting** - Check indentation, line breaks, and alignment match project standards
5. **Respect Buddhist conventions** - Follow proper forms for requests, epithets, and honorifics
6. **Line references** - When citing passages, use line numbers from the .txt or markdown file

## Specialized Analysis Documents

- **Consistency_Analysis_Report.md:** Deep editorial review covering tone, terminology, character names, diacriticals, chapter-by-chapter assessment with specific examples
- **Flow_and_Pacing_Analysis_Report.md:** Analyzes narrative arc distribution, chapter rhythm, pacing consistency, transitions between sections
- **Structural Elements documents:** Design and organizational guidelines for specific translations
- **Formatting Guides:** Production specifications for print (KDP) and digital (EPUB/Kindle) editions

## Publishing and Production

**Current Production Format:**
- Trim Size: 6″ × 9″ (Trade Paperback, KDP standard)
- Font: Georgia (11 pt body, 12 pt verse)
- Line Spacing: 1.15 for prose, single for verse
- Margins: 1″ top/bottom/outside, 1.25″ inside (for binding)
- Front matter: Half-title, title page, copyright, dedication, TOC, introduction
- Back matter: Glossary, about author section, closing note

**Digital Navigation:**
- Word bookmarks for Kindle/EPUB (HalfTitle, TitlePage, Chapter1, etc.)
- Hyperlinked table of contents
- EPUB conversion: Select "Preserve line breaks" for verse formatting

## Common Editorial Tasks

When reviewing or revising sutra translations:

1. **Style consistency check:** Use Consistency_Analysis_Report.md as reference for tone issues
2. **Terminology verification:** Reference glossaries and analysis documents for proper Buddhist terms
3. **Diacritical audit:** Verify all Sanskrit names retain correct Unicode marks
4. **Formatting verification:** Check verse indentation, drop caps, section dividers against guide
5. **Line-number citations:** Reference specific line numbers when identifying passages
6. **Version comparison:** Compare versions (v1, v2, v3) to understand revision evolution

## Notes on Dual-Format Projects

This repository contains both:
- **Scholarly traditional translations** (formal Buddhist scriptural English)
- **Experimental blues/vernacular translations** (contemporary informal style)

These are distinct translation approaches with different stylistic standards. Always verify which style applies to your current task by checking file names, version indicators, and the Consistency/Structural Elements documents.
