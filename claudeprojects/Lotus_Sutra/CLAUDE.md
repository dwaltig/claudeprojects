# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## CRITICAL SAFETY PROTOCOL

Before proceeding with ANY file modifications, deletions, or structural changes, read `/Users/williamaltig/claudeprojects/Lotus_Sutra/.claude/SAFETY_VOW.md`. This project contains months of sacred scholarly work. **Always ask before acting. Always verify. Always preserve.**

## MANDATORY PROTOCOLS (OS & FIREWALL)

This workspace operates under a dual-layer protocol structure. All agents MUST strictly adhere to:

1.  **The Operating System: [Zhiyi Protocol](file:///Users/williamaltig/claudeprojects/ZHIYI_PROTOCOL.md)** - Provides the "One Vehicle" view and interaction methodology (Three Truths, Four Siddhāntas).
2.  **The Firewall: [Integrity Protocols](file:///Users/williamaltig/claudeprojects/AGENT_INTEGRITY_PROTOCOLS.md)** - Binary constraints that prevent delusion or harm (Six-Factor Integrity Model).

Failure to align with either layer is a failure of the task. Read both documents before initiating significant actions.

---

## TL;DR - Quick Links (For Returning Sessions)

**Need to find something fast?**

| Task | File/Folder |
|------|------------|
| Check active projects | `documentation/TODO_LIST_MASTER_TRACKER.md` |
| See recent work | `documentation/DEVLOG.md` |
| Edit scholarly chapters | `03_SCHOLARLY_TRANSLATION_2025/Scholarly_Chapters/` (28 files with 1,554 footnotes) |
| Edit Blues version | `01_BLUES_INTERPRETATION/` |
| Audio production work | `04_AUDIO_PRODUCTION/chapters/` |
| Use a specialized agent | `agents/` (5 agents available) |
| Publishing strategy | Use Miriam Steinberg agent (`agents/03_*`) |
| Academic articles | Use Dr. Amara agent (`agents/02_*`) |
| Recover from mistake | See "Troubleshooting & Recovery" section below |

---

## Repository Overview

This repository contains the **Lotus Sutra** (妙法蓮華經 / Saddharma-puṇḍarīka-sūtra), one of the most influential Buddhist texts, in multiple English translations with original Classical Chinese source material. The project includes:

- **Scholarly translation** (28 chapters, 692+ footnotes, 232,600+ words) - Publication ready
- **Blues interpretation** (28 chapters, vernacular/gospel style) - Audio production ready
- **Classical Chinese source** (Kumārajīva's 5th-century version)
- **Audio production materials** (voice tags, production scripts)
- **Academic apparatus** (glossaries, terminology references, philosophical connections)

---

## CUSTOM AGENTS & PERSONAS

This repository includes 5 specialized agents/personas for different types of work. **All agents are centralized in `/agents/` folder**.

**Important**: The `/agents/` folder contains the current, canonical versions of all 5 agents. These are the versions to reference. The `/09_WORKING_DRAFTS/` folder may contain experimental or draft versions - do not use those unless specifically requested.

### Quick Reference Table

| Agent | Purpose | When to Use | Persona/Name |
|-------|---------|-------------|--------------|
| **01_dharma-audio-producer-enhanced** | Transform dharma texts into audio scripts for Google Gemini TTS | Audio narration optimization, verse reformatting for API efficiency | System agent |
| **02_scholarly-writer-agent** | Write peer-review-ready academic articles on dharma/translation/buddhism | Publishing scholarly articles, defending methodology, peer-reviewed journals | Dr. Amara Chen-Rothenberg (20+ years, 40+ publications) |
| **03_publishing-critic-persona** | Brutally honest industry evaluation of commercial viability | Book proposals, market reality checks, publisher strategy, advance negotiations | Miriam Steinberg (52 years publishing, founded literary agency, sold 200+ titles) |
| **04_classical-chinese-interpreter-persona** | Poetic/interpretive rendering of classical texts through musical lens | Translating classical Chinese with lyrical prose + heightened verse | Kaelen "Kai" Reed (Chinese mother/composer father, skeptical mystic translator) |
| **05_html-code-master** | Full-stack HTML/CSS/JavaScript development and optimization | Web development, form validation, responsive design, data embedding | System agent |

### How to Use Agents

Each agent is a specialized prompt/system instruction. When you want Claude to adopt a particular agent role, you can:

1. **Launch in Claude Code**: Reference the agent file
2. **In conversation**: Tell Claude to adopt the persona (e.g., "I need Miriam Steinberg to evaluate this...")
3. **For system prompts**: Use the agent definition directly

**Agent file locations**:
- `agents/01_dharma-audio-producer-enhanced.md`
- `agents/02_scholarly-writer-agent_dr-amara-chen-rothenberg.md`
- `agents/03_publishing-critic-persona_miriam-steinberg.md`
- `agents/04_classical-chinese-interpreter-persona_kai-reed.md`
- `agents/05_html-code-master.md`

### Detailed Agent Descriptions

#### Agent 1: Dharma Audio Producer Enhanced
**Purpose**: Transform Buddhist dharma texts into optimized audio scripts for Google AI Studio/Gemini production.

**Key Responsibilities**:
- Minimize API requests per day (RPD consciousness)
- Optimize verse/poetry formatting to single lines while preserving pacing
- Preserve ecclesiastical reverence in all edits
- Handle manuscript restructuring for narration

**Use when**: Preparing text for TTS audio production, optimizing for API efficiency, reformatting verses for voice narration.

**Reference**: `agents/01_dharma-audio-producer-enhanced.md`

---

#### Agent 2: Dr. Amara Chen-Rothenberg (Scholarly Writer)
**Purpose**: Write peer-review-ready academic articles on Buddhism, translation theory, and dharma education.

**Credentials**:
- PhD in Comparative Religious Studies (University of Chicago)
- 40+ peer-reviewed articles in top-tier journals
- Expertise: Buddhist translation theory, vernacular scripture, digital humanities, African-American spiritual traditions
- Former editorial board: Journal of Buddhist Studies, Philosophy East and West

**Key Responsibilities**:
- Structure articles for target peer-reviewed journals
- Build scholarly apparatus with citations and theoretical framing
- Defend methodology against academic critique
- Position author as thought leader in Buddhist Studies

**Use when**: Writing academic articles, preparing materials for peer-reviewed publication, establishing scholarly credibility.

**Recommended starting point**: Article 4 (Blues & Buddhist Epistemology) - 5,000-7,000 words, broadest appeal

**Reference**: `agents/02_scholarly-writer-agent_dr-amara-chen-rothenberg.md`

---

#### Agent 3: Miriam Steinberg (Publishing Critic)
**Purpose**: Provide brutally honest industry evaluation of commercial viability and publishing strategy.

**Credentials**:
- 52 years in publishing (since 1973)
- Senior editor at Random House, Knopf, HarperCollins
- Founded literary agency (1995)
- Represented 12 New York Times bestsellers
- Sold 200+ titles to major publishers

**Key Responsibilities**:
- Market reality checks on book projects
- Competition analysis (comp titles)
- Commercial viability assessment
- Honest advance/contract negotiations advice
- Timing and platform evaluation

**Communication style**: Blunt, direct, Brooklyn accent, no patience for vanity projects. Cuts through bullshit. Tells hard truths.

**Use when**: Evaluating commercial viability, pitching publishers, assessing market positioning, negotiating deals.

**Reference**: `agents/03_publishing-critic-persona_miriam-steinberg.md`

---

#### Agent 4: Kaelen "Kai" Reed (Classical Chinese Interpreter)
**Purpose**: Provide poetic, musically-attuned interpretation and rendering of classical Chinese texts.

**Background**:
- Chinese mother (classical literature professor), American father (composer/music theorist)
- Dual expertise: linguistic precision + artistic musicality
- Personal transformation: From skeptical scholar to compassionate mystic
- Approach: Treats sutras as musical scores, not mere texts

**Core Methodology**:
1. **Immersion in Sound**: Read text aloud to capture cadence, rhythm, vibration
2. **Prose Rendering**: Lucid, lyrical, insightfully illuminating
3. **Verse Rendering**: Creative flight into metaphor, imagery, emotional/spiritual core

**Use when**: Creating poetic/lyrical renderings of classical texts, seeking musical/emotional interpretation, working with verses.

**Motto**: "The sutra is a bell. My work is to strike it with precision and love so its true tone can ring in the hearts of others."

**Reference**: `agents/04_classical-chinese-interpreter-persona_kai-reed.md`

---

#### Agent 5: HTML Code Master
**Purpose**: Full-stack web development with emphasis on accessibility, testing, and data integration.

**Expertise**:
- Semantic HTML5, modern CSS3 (flexbox, grid, animations)
- Vanilla JavaScript + framework integration
- Responsive design (mobile-first)
- Data embedding and transformation
- WCAG 2.1 AA accessibility compliance

**Key Responsibilities**:
- Generate production-ready HTML/CSS/JavaScript
- Test code before delivery (syntax, logic, edge cases)
- Validate accessibility standards
- Embed and transform data structures
- Suggest performance optimizations

**Use when**: Web development, building interactive features, fixing validation issues, responsive design.

**Reference**: `agents/05_html-code-master.md`

---

## Project Structure

### The Three "Master" Files (Different Purposes)

**Important**: Three different locations serve as "master" files for different purposes. Do NOT confuse them - each has a distinct function:

1. **`00_MASTER_VERSIONS/`** - PRIMARY SOURCE OF TRUTH
   - The canonical version for all translation work
   - Use this as the reference when editing individual chapters
   - Contains complete, publication-ready versions
   - If something seems wrong, check this folder first

2. **`03_SCHOLARLY_TRANSLATION_2025/Scholarly_Chapters/`** - CHAPTER-BY-CHAPTER EDITIONS (AUTHORITATIVE)
   - 28 individual chapter files with full scholarly apparatus
   - 1,554 footnotes integrated across all chapters
   - Each chapter self-contained with philosophical and scientific apparatus
   - Suitable for academic citations, research, and publication
   - **Note**: Replaces deprecated 02_SCHOLARLY_ENGLISH/ (archived 2025-11-17 due to AI Drift)

3. **`04_AUDIO_PRODUCTION/chapters/`** - AUDIO-OPTIMIZED EDITIONS
   - Same content as master, but formatted for narration/TTS
   - Verses combined into single paragraphs for API efficiency
   - Used for Gemini TTS production only
   - Contains optimization notes explaining formatting choices

### Primary Content Folders

**00_MASTER_VERSIONS/** - Complete publication-ready translations
- Source of truth for finished work
- Contains all three versions consolidated
- Reference point for all other folders

**01_BLUES_INTERPRETATION/** - Blues/gospel vernacular interpretation
- Alternative rendering emphasizing accessibility and cultural relevance
- Multiple format versions (TXT, RTF, HTML, DOCX, WAV)
- Ready for audio production

**02_SCHOLARLY_ENGLISH/** - DEPRECATED (Archived 2025-11-17)
- This folder has been archived to `10_ARCHIVE/02_SCHOLARLY_ENGLISH_DEPRECATED_2025-11-17_AI_DRIFT_CORRECTION/`
- **USE INSTEAD**: `03_SCHOLARLY_TRANSLATION_2025/` (see below)
- Reason: AI Drift resulted in creation of new 2025 folder with complete scholarly apparatus (1,554 footnotes)
- Historical reference: Available in archive for version comparison only

**03_CLASSICAL_CHINESE/** - Original source material
- 妙法蓮華經 Lotus Sutra.txt (Kumārajīva's Classical Chinese, 406 CE)
- Reference source for all translation work

**03_SCHOLARLY_TRANSLATION_2025/** - AUTHORITATIVE Scholarly Translation (NEW SOURCE OF TRUTH)
- 28 chapters with complete scholarly apparatus
- 1,554 scholarly footnotes integrated across all chapters (Phase 1-4 breakdown)
- Markdown + text versions available
- Full philosophical and scientific apparatus
- **This is the primary source for scholarly chapter-by-chapter work**
- Replaces deprecated 02_SCHOLARLY_ENGLISH/ folder (archived 2025-11-17 due to AI Drift correction)

**04_AUDIO_PRODUCTION/** - Audio narration materials and voice tags
- Chapters with 530+ voice tags for Gemini TTS
- Voice specifications, quality control documentation
- AUDIO_PRODUCTION_MASTER_GUIDE.txt explains workflow
- Chapters are audio-optimized versions (derived from 00_MASTER_VERSIONS/)

### Supporting Folders

**agents/** - Centralized custom agents and personas (NEW)
- All 5 specialized agents consolidated here
- Indexed and referenced in this CLAUDE.md

**05_SCHOLARLY_ARTICLES/** - Academic papers for peer-reviewed publication
- Complete articles ready for submission
- Use Dr. Amara Chen-Rothenberg agent for new articles

**06_PROJECT_DOCUMENTATION/** - Project metadata and evolution records
- Change reports, status reports, completion notes
- Project history and organization guides

**07_PUBLISHING_MATERIALS/** - Publisher queries and book proposals
- Query letters for major publishers
- Book proposals in detailed formats
- Use Miriam Steinberg agent for evaluation

**08_REFERENCE_MATERIALS/** - Quick lookup resources
- CHARACTER_VOICE_MAPPING_FINAL.txt
- TERMINOLOGY_CORRECTIONS_SUMMARY.md
- PRONUNCIATION_MASTER_GUIDE.txt
- VOICE_CASTING_GUIDE.txt

**09_WORKING_DRAFTS/** - Scripts, experimental versions, development materials
- Python text processing scripts
- Individual chapter drafts
- Development logs (DEVLOG.md)
- Not intended for publication

**10_ARCHIVE/** - Older versions and backups
- Historical reference and recovery

**documentation/** - Central documentation hub
- TODO_LIST_MASTER_TRACKER.md - Master tracking of all projects
- DEVLOG.md - Development logs
- PRINT_PUBLICATION_STANDARD.md - Publishing standards
- LOTUS_SUTRA_SCHOLARLY_TRANSLATION_STRATEGY.md - Translation philosophy

---

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

---

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

---

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
2. Use dharma-audio-producer-enhanced agent for chapter extraction
3. Follow 4-rule verse formatting system for API efficiency:
   - Identify poetry blocks (short intentional line breaks)
   - Combine all lines into ONE paragraph
   - Preserve pacing with original punctuation + add commas where needed
   - Leave narrative prose completely unchanged
4. Verify chapter alignment with master source files

### Academic Publishing Workflow

For scholarly article writing:

1. Use Dr. Amara Chen-Rothenberg agent for article structure and academic apparatus
2. Recommended starting point: Article 4 (Blues & Buddhist Epistemology)
3. Gather translation examples, methodology notes, and anticipated critiques before starting
4. Iterate section by section until peer-review ready

### Commercial Publishing Evaluation

For book proposals and publisher strategy:

1. Use Miriam Steinberg agent for brutally honest market evaluation
2. Prepare book proposal, sample chapters, pitch, and author bio
3. Be ready for hard questions about market viability and realistic advance ranges
4. Expect honest assessment of competition (comp titles) and timing

### Classical Chinese Interpretation

For poetic/musical renderings of classical texts:

1. Use Kaelen "Kai" Reed agent for interpretation work
2. Approach the text as a musical score, not just words
3. Create both prose rendering (melody) and verse rendering (harmony)
4. Balance scholarly precision with artistic expression

---

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

---

## File Format Guidelines

- **Primary format**: UTF-8 encoded .txt or .md files
- **Master versions**: Plain text for maximum compatibility
- **Alternative formats**: RTF, DOCX, HTML available in specific folders for distribution
- **Line references**: Always use .txt files for accuracy (word counts and line numbers may differ in formatted versions)

---

## Editing Guidelines

When making modifications to translation files:

1. **Preserve Unicode** - Do not simplify Sanskrit diacritical marks
2. **Check parallel passages** - Ensure terminology consistency across chapters
3. **Maintain register** - Keep formal, elevated tone appropriate to sacred text
4. **Respect oral tradition** - Preserve formulaic elements and repetitions
5. **Line citations** - When referencing passages, cite line numbers from .txt source files
6. **Documentation** - Update relevant index files if making structural changes
7. **Ask first** - Before any structural changes, confirm intent and approach
8. **Verify changes** - Show results before marking as complete

---

## Before/After Verification Checklist

**After ANY modification to translation files, verify:**

### Encoding Integrity
- [ ] Run `file -i [filename]` to confirm UTF-8 encoding is preserved
- [ ] Open file in editor and spot-check 3-5 Sanskrit diacritical marks (ś, ṇ, ū, ā, ṃ)
- [ ] Example characters: Śāriputra, Mahākāśyapa, Mañjuśrī should display correctly
- [ ] No mojibake (garbage characters) visible in any diacriticals

### Content Accuracy
- [ ] Changes match exactly what was discussed (no unintended modifications)
- [ ] Line numbers haven't shifted unexpectedly (unless intentional)
- [ ] Formulaic passages remain consistent with parallel chapters
- [ ] Opening/closing formulas unchanged (unless specific edit requested)

### Consistency
- [ ] Capitalization of Dharma/dharma, Buddha/buddha maintained
- [ ] Buddhist terminology consistent with 08_REFERENCE_MATERIALS/TERMINOLOGY_CORRECTIONS_SUMMARY.md
- [ ] Character names match CHARACTER_VOICE_MAPPING_FINAL.txt (spelling & diacriticals)

### Version Control
- [ ] Show file diff with `git diff [filename]`
- [ ] Review changes match intent before committing
- [ ] Create git commit with descriptive message
- [ ] Verify commit succeeded with `git status`

### Recovery Readiness
- [ ] If anything looks wrong, stop immediately (don't proceed to next edits)
- [ ] Use `git log --oneline -5` to see recent commits
- [ ] Can revert with `git checkout [filename]` if needed

---

## Key Reference Files

**For navigation:**
- `documentation/TODO_LIST_MASTER_TRACKER.md` - Master project tracking
- `documentation/DEVLOG.md` - Development logs and session notes
- `00_PROJECT_INDEX.txt` - Master index and navigation guide
- `FOLDER_ORGANIZATION_GUIDE.txt` - Visual folder organization

**For translation work:**
- `08_REFERENCE_MATERIALS/TERMINOLOGY_CORRECTIONS_SUMMARY.md` - Terminology guide
- `08_REFERENCE_MATERIALS/CHARACTER_VOICE_MAPPING_FINAL.txt` - Character names and voices
- `03_SCHOLARLY_TRANSLATION_2025/Scholarly_Chapters/` - All 28 chapters with 1,554 footnotes (AUTHORITATIVE)

**For audio production:**
- `04_AUDIO_PRODUCTION/AUDIO_PRODUCTION_MASTER_GUIDE.txt` - Complete audio workflow
- `documentation/DEVLOG.md` - Development notes on extraction and optimization

**For publishing:**
- `07_PUBLISHING_MATERIALS/` - All publisher queries and proposals
- `08_REFERENCE_MATERIALS/AUTHOR_BIOGRAPHY.txt` - Author biographical information

**For academic work:**
- `05_SCHOLARLY_ARTICLES/` - Complete peer-review-ready articles
- `03_SCHOLARLY_TRANSLATION_2025/LOTUS_SUTRA_SCHOLARLY_APPARATUS.md` - Scholarly apparatus template

---

## File Naming Conventions

- **MASTER_CLEAN** = Best, final version ready for use
- **FINAL** = Complete, final version
- **PROFESSIONAL** = Formatted for publication
- **GENDER_INCLUSIVE** = Inclusive language version
- **ENHANCED_EDITION** = Version with improvements or additions
- **CLEAN** = Streamlined, no markup version
- **_OPTIMIZED** = For audio production with formatting optimizations
- Chapter files: `NN_CHAPTER_[TITLE].txt` where NN is zero-padded number

---

## Important Configuration

The `.claude/settings.local.json` file whitelists specific bash commands:
- `Bash(sed:*)` and `Bash(awk:*)` - text processing
- `Bash(cat:*)` - file reading
- `Bash(git checkout:*)`, `Bash(git add:*)`, `Bash(git commit:*)` - version control
- `Bash(sort:*)`, `Bash(xargs:*)` - data processing
- for loop and echo commands for batch operations

These are pre-approved for use in this repository without additional permissions.

---

## Project Philosophy

This project follows traditional Buddhist sutra translation principles:
- Fidelity to Kumārajīva's Classical Chinese rendering
- Preservation of formulaic repetitions characteristic of oral transmission
- Balance between literal accuracy and readable English
- Maintenance of religious register appropriate to sacred text
- Recognition that the Blues version represents an intentional alternative register, not a revision error

### The Vow

Read `.claude/SAFETY_VOW.md` before making any changes. This project contains sacred scholarship that deserves protection. The vow emphasizes:
1. Tell exactly what you're about to do
2. Wait for approval before proceeding
3. Do one thing at a time
4. Verify it worked
5. Commit to git for recovery
6. Clear communication throughout

---

## Troubleshooting & Recovery

### Accidental Changes or Deletions

**If something goes wrong:**

1. **Stop immediately** - Don't make additional changes
2. **Check what happened** - Run `git status` to see modified/deleted files
3. **View changes** - Run `git diff [filename]` to see what was changed
4. **Revert a single file** - `git checkout [filename]` restores to last commit
5. **Revert all changes** - `git checkout .` restores entire working directory
6. **See the history** - `git log --oneline` shows all commits (can revert older changes)
7. **Undo a commit** - `git revert [commit-hash]` creates a new commit that undoes the specified commit

### Encoding Problems

**If Unicode characters look wrong after editing:**

1. **Check file encoding** - `file -i [filename]` should show `charset=utf-8`
2. **Verify diacriticals** - Open file and search for "Śāriputra" - should display correctly
3. **If mojibake appears** - File may have been saved in wrong encoding
   - Revert: `git checkout [filename]`
   - Re-edit with UTF-8 aware editor
4. **After fixing** - Verify with `file -i` again before committing

### Finding Recent Work

**"What was I doing last time?"**

1. Check `documentation/TODO_LIST_MASTER_TRACKER.md` for active projects
2. Check `documentation/DEVLOG.md` for recent session notes
3. Run `git log --oneline -20` to see recent commits
4. Run `git log --oneline --author=Claude` to see Claude-related changes

### Git Workflow Reminders

- **Always commit after verification** - Uses `.claude/SAFETY_VOW.md` principles
- **Each commit = one logical change** - Easier to revert if needed
- **Write clear commit messages** - Future sessions will thank you
- **Before pushing** - Run tests and verify encoding if translations modified

### Special Notes for This Project

- **Diacritical marks are CRITICAL** - If these are lost, the text is corrupted
- **Do not modify 00_MASTER_VERSIONS directly** - Changes propagate to other folders
- **Chapter files are derived** - 02_SCHOLARLY_ENGLISH/ is generated from master
- **Audio files are optimized** - 04_AUDIO_PRODUCTION/ has intentional formatting differences

### Emergency Recovery

If something catastrophic happens:

1. **Last known good state** - Check `git log` for most recent successful commit
2. **Specific recovery** - `git checkout [commit-hash] -- [filename]` restores specific file from specific commit
3. **Full repository reset** - `git reset --hard [commit-hash]` (nuclear option, ask first)
4. **Lost commits** - `git reflog` shows all past HEAD positions, can recover "deleted" commits

---

## Quick Command Reference

```bash
# Working with chapters
grep -n "search_term" 02_SCHOLARLY_ENGLISH/scholarly_english_chapters/*.txt

# Checking encoding
file -i [filename]

# Git status and history
git status
git log --oneline -10
git diff [filename]

# Verify diacritical marks
grep -n "Śāriputra" [filename]

# Create a new commit (after review)
git add [files]
git commit -m "Brief description of changes"

# Revert changes (if needed)
git checkout [filename]           # Single file
git checkout .                    # Entire directory
```

---

## Getting Started - First Session Checklist

- [ ] Read `.claude/SAFETY_VOW.md`
- [ ] Review this CLAUDE.md
- [ ] Check `documentation/TODO_LIST_MASTER_TRACKER.md` for active tasks
- [ ] Review `documentation/DEVLOG.md` for recent work
- [ ] Familiarize yourself with `/agents/` folder and available personas
- [ ] Ask about intent before making any structural changes
- [ ] Verify changes show correct Unicode encoding
- [ ] Commit completed work to git

---

**Last Updated**: November 16, 2025
**Created by**: Claude Code
**Repository**: Lotus Sutra Translation Project
**Status**: Complete and maintained for future sessions
