# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains the Lotus Sutra (妙法蓮華經 / Saddharma-puṇḍarīka-sūtra), one of the most influential Buddhist texts, in multiple English translations, along with the original Classical Chinese source. The project includes three distinct versions: a formal scholarly translation, a blues/gospel vernacular interpretation, and audio production materials with voice tags.

## Project Structure

The repository is organized into 11 primary folders and supporting directories:

### Primary Content Folders

**00_MASTER_VERSIONS/** - Complete publication-ready translations
- Source of truth for finished work
- Contains all three versions consolidated
- Files: THE_LOTUS_SUTRA_OF_THE_WONDERFUL_DHARMA.txt, narrated manuscript with voice tags

**01_BLUES_INTERPRETATION/** - Blues/gospel vernacular interpretation
- Alternative rendering emphasizing accessibility and cultural relevance
- Multiple format versions (TXT, RTF, HTML, DOCX, WAV)
- Primary file: Blues_Lotus_Sutra_MASTER_CLEAN.txt

**02_SCHOLARLY_ENGLISH/** - Academic translation organized by chapters
- 28 individual chapter files (01_CHAPTER_INTRODUCTION.txt through 28_CHAPTER_THE_ENCOURAGEMENT...)
- scholarly_english_chapters/00_INDEX_GUIDE.txt provides comprehensive navigation
- Suitable for academic citations and research

**03_CLASSICAL_CHINESE/** - Original source material
- 妙法蓮華經 Lotus Sutra.txt - Kumārajīva's Classical Chinese version (406 CE)
- Reference source for all translation work

**04_AUDIO_PRODUCTION/** - Audio narration materials and voice tags
- Chapters with 530+ voice tags for Gemini TTS production
- Voice specifications, reference guides, quality control documentation
- Front and ending materials (pronunciation guides, scholarly apparatus)
- File: AUDIO_PRODUCTION_MASTER_GUIDE.txt explains complete workflow

### Supporting Folders

**05_SCHOLARLY_ARTICLES/** - Academic papers for peer-reviewed publication
- ARTICLE_4_DRAFT_Blues_Buddhist_Epistemology.txt (complete, ready for submission)
- Three additional articles identified for future writing

**06_PROJECT_DOCUMENTATION/** - Project metadata and evolution records
- Change reports, status reports, project completion notes
- Guides for understanding project history and organization

**07_PUBLISHING_MATERIALS/** - Publisher queries and book proposals
- Query letters for major publishers (Beacon Press, Shambhala, Wisdom Publications)
- Book proposals in detailed and submission-ready formats
- Submission checklists and publishing guides

**08_REFERENCE_MATERIALS/** - Quick lookup resources
- CHARACTER_VOICE_MAPPING_FINAL.txt - Character to voice assignments
- AUTHOR_BIOGRAPHY.txt
- PRONUNCIATION_MASTER_GUIDE.txt
- TERMINOLOGY_CORRECTIONS_SUMMARY.md
- VOICE_CASTING_GUIDE.txt
- Translation methodology notes and gender-inclusive language recommendations

**09_WORKING_DRAFTS/** - Scripts, experimental versions, and development materials
- Python text processing scripts (extract_audio_chapters.py, fix_stray_chinese_comprehensive.py)
- Individual chapter draft files
- Development logs (DEVLOG.md)
- Agent descriptions and experimental versions
- Not intended for publication

**10_ARCHIVE/** - Older versions and backups
- For historical reference and recovery

## Translation Conventions and Character Names

### Sanskrit Diacritical Marks - CRITICAL

Always preserve exact diacritical marks. Never simplify character names:

- Śāriputra (not Sariputra)
- Mahākāśyapa, Mañjuśrī, Avalokiteśvara
- Ājñāta-Kauṇḍinya, Pūrṇa-Maitrāyaṇīputra
- Anuttara-samyak-sambodhi (supreme perfect enlightenment)

**Key Unicode characters**: ś (U+015B), ṇ (U+1E47), ū (U+016B), ā (U+0101), ṃ (U+1E43)

All files use UTF-8 encoding. Ensure editors preserve Unicode characters during modifications.

### Terminology Consistency

**Capitalization patterns:**
- Dharma (teachings/law) vs. dharma (phenomena/things)
- Buddha (the historical Buddha) vs. buddha (awakened being)
- Tathagata, Bodhisattva, Arhat - always capitalized

**Standard Buddhist terms:**
- nirvāṇa, samādhi, dhāraṇī
- śrāvaka (hearer/disciple), pratyekabuddha (solitary realizer)

### Formulaic Expressions

**Opening formula:**
"Thus have I heard. At one time, the Buddha was staying..."

**Verse transition formula:**
"At that time, [Speaker], wishing to repeat this meaning, spoke in verse:"

**Buddha's ten epithets** (used in formal contexts):
Tathagata, Arhat, Perfectly Enlightened One, Perfect in Knowledge and Conduct, Well-Gone, Knower of the World, Unsurpassed One, Tamer of Beings, Teacher of Devas and Humans, Buddha, World-Honored One

## Chapter Structure

The Lotus Sutra contains 28 chapters:

1. Introduction (序品)
2. Expedient Means (方便品)
3. A Parable (譬喻品)
4. Belief and Understanding (信解品)
5. A Parable of the Medicinal Herbs (藥草喻品)
6. Bestowal of Prophecies (授記品)
7. A Parable of the Phantom City (化城喻品)
8-9. Bestowal of Prophecies (continued)
10-28. Various teachings on Dharma teachers, supernatural manifestations, and Bodhisattva practices

## Common Workflows and Commands

### Working with Translation Files

When editing the main translation files:

1. **File references**: Cite by line number when discussing specific passages
2. **Consistency check**: Use grep to find parallel passages for terminology verification
3. **Encoding**: All files are UTF-8 - verify editor preserves Unicode
4. **Style verification**: Maintain formal Buddhist scriptural register throughout

### Audio Production Workflow

For work in 04_AUDIO_PRODUCTION/:

1. Reference DEVLOG.md for extraction and optimization processes
2. Use extract_clean_chapters_with_notes.py for chapter extraction aligned with master files
3. Follow 4-rule verse formatting system for API efficiency:
   - Identify poetry blocks (short intentional line breaks)
   - Combine all lines into ONE paragraph
   - Preserve pacing with original punctuation + add commas where needed
   - Leave narrative prose completely unchanged
4. Verify chapter alignment with master source files

### Working with Scholarly Chapters

The 28 scholarly chapters in 02_SCHOLARLY_ENGLISH/ are individually indexed:

- Use 00_INDEX_GUIDE.txt for navigation
- Reference for academic citations
- Each file numbered NN_CHAPTER_[TITLE].txt

### Published Work

Files in 00_MASTER_VERSIONS/ and 01_BLUES_INTERPRETATION/MASTER_CLEAN versions are publication-ready and should not require editing. If changes are needed, trace back to source files and regenerate.

## Stylistic Considerations

### Appropriate for Formal Scholarly Version
- Formal, reverent tone befitting sacred scripture
- Traditional Buddhist terminology with consistent English equivalents
- Poetic but dignified language in verse sections
- Preservation of formulaic repetitions characteristic of oral transmission

### Avoid in Formal Version
- Modern colloquialisms or contractions (unless in Blues Translation)
- Inconsistent rendering of technical terms
- Over-interpretation or explanatory additions beyond source text

### Blues Version Differs Intentionally
- The Blues interpretation uses vernacular language, blues/gospel registers
- This is a distinct stylistic choice, not an error
- Keep separate from formal scholarly version

## File Format Guidelines

- **Primary format**: UTF-8 encoded .txt files
- **Master versions**: Plain text for maximum compatibility
- **Alternative formats**: RTF, DOCX, HTML available in specific folders for distribution
- **Line references**: Always use .txt files for accuracy (word counts and line numbers may differ in formatted versions)

## Editing Guidelines

When making modifications to translation files:

1. **Preserve Unicode** - Do not simplify Sanskrit diacritical marks
2. **Check parallel passages** - Ensure terminology consistency across chapters
3. **Maintain register** - Keep formal, elevated tone appropriate to sacred text
4. **Respect oral tradition** - Preserve formulaic elements and repetitions
5. **Line citations** - When referencing passages, cite line numbers from .txt source files
6. **Documentation** - Update relevant index files if making structural changes

## Key Reference Files

**For navigation:**
- 00_PROJECT_INDEX.txt - Master index and navigation guide (start here for unfamiliar tasks)
- FOLDER_ORGANIZATION_GUIDE.txt - Visual folder organization and workflow examples

**For translation work:**
- 08_REFERENCE_MATERIALS/TERMINOLOGY_CORRECTIONS_SUMMARY.md - Terminology guide
- 08_REFERENCE_MATERIALS/CHARACTER_VOICE_MAPPING_FINAL.txt - Character names and voice assignments
- 02_SCHOLARLY_ENGLISH/scholarly_english_chapters/00_INDEX_GUIDE.txt - Chapter index

**For audio production:**
- 04_AUDIO_PRODUCTION/AUDIO_PRODUCTION_MASTER_GUIDE.txt - Complete audio workflow
- DEVLOG.md - Development notes on extraction and optimization processes

**For publishing:**
- 07_PUBLISHING_MATERIALS/ - All publisher queries and proposals
- 08_REFERENCE_MATERIALS/AUTHOR_BIOGRAPHY.txt - Author biographical information

## File Naming Conventions

- **MASTER_CLEAN** = Best, final version ready for use
- **FINAL** = Complete, final version
- **PROFESSIONAL** = Formatted for publication
- **GENDER_INCLUSIVE** = Inclusive language version
- **ENHANCED_EDITION** = Version with improvements or additions
- **CLEAN** = Streamlined, no markup version
- **_OPTIMIZED** = For audio production with formatting optimizations
- Chapter files: NN_CHAPTER_[TITLE].txt where NN is zero-padded number

## Important Configuration

The .claude/settings.local.json file whitelists specific bash commands:
- Bash(sed:*) and Bash(awk:*) - text processing
- Bash(cat:*) - file reading
- for loop and echo commands for batch operations

These are pre-approved for use in this repository without additional permissions.

## Project Philosophy

This project follows traditional Buddhist sutra translation principles:
- Fidelity to Kumārajīva's Classical Chinese rendering
- Preservation of formulaic repetitions characteristic of oral transmission
- Balance between literal accuracy and readable English
- Maintenance of religious register appropriate to sacred text
- Recognition that the Blues version represents an intentional alternative register, not a revision error
