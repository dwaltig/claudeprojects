# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains a complete scholarly translation of the **Lotus Sutra** (妙法蓮華經) from Classical Chinese into contemporary American English with integrated philosophical and scientific apparatus. The project is fully complete (100%) with all 28 chapters translated, documented, and cross-referenced for academic use.

## Repository Structure

```
/03_SCHOLARLY_TRANSLATION_2025/
  ├── CHAPTER_01-28_*.md          # Main chapter translations with scholarly apparatus
  ├── CHAPTER_01-28_*.txt         # Text-only versions of chapters
  ├── PROJECT_COMPLETION_MASTER_SUMMARY.md       # Complete project overview and metrics
  ├── LOTUS_SUTRA_SCHOLARLY_APPARATUS.md        # Index of footnotes and scholarly notes
  ├── GLOSSARY_BUDDHIST_TERMS.md                # Terminology reference (Sanskrit + definitions)
  ├── PROJECT_STATUS_PHASE3_UPDATE.md           # Phase 3 completion status
  ├── CHAPTER_AUDIT_MATRIX.txt                 # Chapter-by-chapter completion checklist
  ├── QA_REPORT_2025.md                        # Quality assurance findings
  ├── build_index.sh              # Generate HTML index from chapters
  ├── convert_chapters.sh         # Convert markdown chapters to HTML
  └── PROJECT_README.md           # Project vision and file guide
```

## Project Completion Status

**Status**: ✓ COMPLETE (100%)
- **28 of 28 chapters**: Fully translated and documented
- **~232,600 words**: Total translation volume
- **692+ integrated footnotes**: Scholarly apparatus
- **Phase completion**: 4 phases completed across 5 sessions
- **Quality assurance**: Complete

## Working with the Translation

### File Format and Encoding

- **Encoding**: UTF-8 (essential for Sanskrit diacriticals)
- **Main format**: Markdown (.md) with integrated footnotes
- **Alternative format**: Plain text (.txt) for distribution
- **Structure**: Chapter headings + prose sections + verse sections + philosophical implications + apparatus summaries

### Character Names and Sanskrit Terms

**Always preserve exact diacritical marks**:
- Śāriputra (s-cedilla, macron a)
- Mañjuśrī (n-tilde, s-cedilla, macron i)
- Mahākāśyapa (macron a, macron a)
- Avalokiteśvara (s-cedilla, v)
- Maitreya (standard spelling)
- anuttara-samyak-sambodhi (macrons on both 'a's)

**Key terminology consistency**:
- "Tathagata" (the Buddha's epithet, formal)
- "Bodhisattva" (enlightenment-being)
- "Dharma" (teachings, capitalized); "dharma" (phenomena, lowercase)
- "nirvāṇa" (with macron over a)
- "samādhi" (meditative concentration)
- "śrāvaka" (hearer-disciple)

### Translation Methodology

The translation follows these core principles:

1. **Formal Buddhist Scriptural Tone**: Maintains reverent, elevated language appropriate to sacred text
2. **Contemporary American English**: Accessible to modern readers without sacrificing precision
3. **Fidelity to Classical Chinese Original**: Accurate rendering of Kumarajiva's 5th-century translation
4. **Integrated Philosophical Apparatus**: Footnotes connect Buddhist teachings to modern philosophy (phenomenology, existentialism, systems theory)
5. **Scientific Resonances**: Cross-references to quantum mechanics, cognitive science, information theory where relevant

### Chapter Structure

Each chapter follows a standardized format:

```
# Chapter [N]: [Title]

## Prose Section
[Main narrative translation with inline footnotes]

## Verse Section
[Poetic translation maintaining meaning and rhythm]

## Philosophical Implications
[Modern philosophical connections and significance]

## Apparatus Summary
[Overview of key concepts, terms, and scholarly notes]
```

### Footnote Format

Integrated footnotes appear inline using markdown footnote syntax:

```markdown
This is a teaching[^1] with scholarly context.

[^1]: Translation note: Sanskrit term connections;
Philosophical context: Connection to phenomenology or systems theory;
Scientific parallel: Relationship to contemporary science if applicable.
```

## Architectural Layers (4-Phase Delivery)

### Phase 1: Foundation (Chapters 1-8)
- Establishes Buddhist doctrine fundamentals
- Introduces translation terminology and voice
- Integrates first layer of philosophical apparatus (phenomenology, being-in-the-world)

### Phase 2: Validation (Chapters 9-16)
- Demonstrates Buddha-nature universality through prophecy mechanism
- Expands scientific apparatus (quantum entanglement, systems theory)
- Validates core doctrine through narrative examples

### Phase 3: Theory & Cosmic Verification (Chapters 17-22)
- Merit-transformation frameworks
- Cosmic timescale revelations (Buddha's eternal lifespan)
- Advanced philosophical connections (Whitehead, systems theory)

### Phase 4: Bodhisattva Exemplars (Chapters 23-28)
- Practical applications through bodhisattva models
- Specific practice methodologies
- Integration with modern science and philosophy

## Common Development Tasks

### Editing a Chapter

1. Open the target chapter markdown file (e.g., `CHAPTER_05_MEDICINAL_HERBS.md`)
2. Preserve all Sanskrit diacriticals (never simplify names or terms)
3. Maintain the formal Buddhist scriptural tone
4. Keep footnotes inline using markdown syntax
5. After editing, verify consistency against `GLOSSARY_BUDDHIST_TERMS.md` and `LOTUS_SUTRA_SCHOLARLY_APPARATUS.md`

### Checking Consistency

1. **Character names**: Use `GLOSSARY_BUDDHIST_TERMS.md` as the authoritative reference
2. **Terminology**: Cross-reference with glossary for consistent translation choices
3. **Philosophical terms**: Verify footnote connections align with established apparatus patterns
4. **Overall tone**: Compare prose sections—should maintain formal scriptural voice throughout

### Building HTML Output

Generate web-readable versions of chapters:

```bash
# Build the index page with chapter links
./build_index.sh

# Convert all markdown chapters to HTML with navigation
./convert_chapters.sh
```

These scripts create a browsable HTML reader with chapter navigation, table of contents, and consistent styling.

### Quality Assurance

Refer to `QA_REPORT_2025.md` for known findings and resolution status. The `CHAPTER_AUDIT_MATRIX.txt` provides a checklist of completion requirements for each chapter.

## Key Project Documents

- **PROJECT_COMPLETION_MASTER_SUMMARY.md**: Comprehensive overview with metrics and phase breakdowns
- **LOTUS_SUTRA_SCHOLARLY_APPARATUS.md**: Template and index for all scholarly footnotes
- **GLOSSARY_BUDDHIST_TERMS.md**: Definitive reference for terminology and character names
- **QA_REPORT_2025.md**: Quality findings and editorial notes

## Critical Translation Standards

1. **No simplification of diacriticals** — Never convert Śāriputra to Sariputra
2. **Consistent terminology** — Use glossary as the single source of truth
3. **Formal tone throughout** — Prose and verse should both maintain scriptural reverence
4. **Accurate philosophical apparatus** — Footnotes must be historically/philosophically accurate
5. **Proper honorifics** — Follow Buddhist conventions for respectful address and attribution

## Filename Convention for Chapter 25

**Established Decision** (Audit Verified 2025-11-16):

Chapter 25 uses a **dual-format approach** for maximum compatibility and scholarly accuracy:

- **Filename**: `CHAPTER_25_AVALOKITESHVARA.md` (ASCII-safe, no diacritical marks)
- **Content**: Text uses proper Sanskrit diacriticals: `Avalokiteśvara` (with ś cedilla)

**Rationale**:
- Filenames use ASCII characters only for maximum cross-platform compatibility (Windows, macOS, Linux, web servers)
- Chapter content preserves proper Sanskrit diacritical marks essential for scholarly accuracy and proper transliteration
- This approach balances technical compatibility (filesystem stability) with scholarly integrity (accurate Sanskrit)

**Precedent**: This convention applies to Chapter 25 specifically, as it features Avalokiteśvara (观世音菩萨) as the primary subject. Other chapters follow standard naming patterns where chapter titles don't require special characters.

## Source Material Reference

**Classical Chinese Original**: Located at `/Users/williamaltig/claudeprojects/Lotus_Sutra/03_CLASSICAL_CHINESE/妙法蓮華經 Lotus Sutra.txt`
- Kumarajiva's 5th-century translation (鳩摩羅什)
- 4,610 lines covering all 28 chapters
- Primary reference for fidelity verification

## Project Context

This translation fills a gap in English Buddhist scholarship by providing:
- Academic rigor suitable for citation in philosophical and religious studies
- Connection to contemporary Western philosophical traditions
- Accessibility for educated readers without oversimplification
- Appropriate reverence for a sacred text

The complete translation, with its integrated scholarly apparatus, serves both academic study and contemplative engagement with the Lotus Sutra's teachings.
