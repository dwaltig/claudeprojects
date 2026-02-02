# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

This repository contains the **Diamond Sutra** (金剛般若波羅蜜經 *Jīnāng Bōruò Bōluómì Jīng*), one of the most influential Buddhist texts emphasizing the concept of emptiness (śūnyatā) and the illusory nature of all phenomena.

**Current Status**: Active development with scholarly translation complete and blues interpretation in progress.

### Project Contents

- **Source text**: `00_SOURCE/金剛般若波羅蜜經 Diamond Sutra.txt` - Classical Chinese original
- **Scholarly translation**: Complete (Parts 1-3, Chapters 1-32) in `01_SCHOLARLY_TRANSLATION/`
- **Blues interpretation**: Three versions available in `02_BLUES_INTERPRETATION/`
- **Audio production**: ElevenLabs-optimized files in `03_AUDIO_PRODUCTION/`

---

## Project Structure

```
/Diamond Sutra Project/
├── CLAUDE.md (this file)
├── 00_SOURCE/
│   └── 金剛般若波羅蜜經 Diamond Sutra.txt (classical Chinese source)
├── 01_SCHOLARLY_TRANSLATION/
│   ├── DIAMOND_SUTRA_SCHOLARLY_PART_1.md (Chapters 1-10)
│   ├── DIAMOND_SUTRA_SCHOLARLY_PART_2.md (Chapters 11-22)
│   └── DIAMOND_SUTRA_SCHOLARLY_PART_3.md (Chapters 23-32)
├── 02_BLUES_INTERPRETATION/
│   ├── diamond_sutra_blues_interpretation_FINAL.txt
│   ├── diamond_sutra_blues_interpretation_POLISHED.txt
│   └── diamond_sutra_blues_interpretation_PHASE_1.txt
└── 03_AUDIO_PRODUCTION/
    ├── diamond_sutra_for_elevenreader_AUDIO_OPTIMIZED.txt
    ├── diamond_sutra_for_elevenreader_AUDIO_OPTIMIZED.docx
    └── diamond_sutra_for_elevenreader_FORMATTED.txt
```

---

## File Handling Guidelines

### Master Source Text

- **File**: `金剛般若波羅蜜經 Diamond Sutra.txt`
- **Format**: UTF-8 text with classical Chinese characters
- **Content**: Complete Diamond Sutra in classical Chinese (文言文)
- **Do NOT edit without clear justification**: This is the primary source text. Preserve the original Buddhist scripture accurately.

### Encoding Requirements

- All text files must use **UTF-8 encoding**
- Chinese characters are essential to the text's authenticity
- Verify encoding after file operations: `file -i [filename]` should show `charset=utf-8`

---

## Getting Started with the Diamond Sutra

### Understanding the Source Text

The Diamond Sutra is a Mahāyāna Buddhist scripture known for:
- Philosophical depth on emptiness (śūnyatā) and non-dualism
- Relatively brief and focused compared to longer sutras
- Central to Zen/Chan Buddhist practice
- Rich imagery and paradoxical teachings

### Key Concepts to Know

**śūnyatā (emptiness)** - The doctrine that all phenomena lack intrinsic, independent existence
**Bodhisattva** - One dedicated to enlightenment for the sake of all beings
**Dharma** - Buddhist teachings or the nature of reality
**Tathagata** - An epithet for the Buddha, meaning "thus-gone one"

---

## Translation Conventions (From Parent Workspace)

When beginning translation and interpretation work on the Diamond Sutra, apply these workspace-wide conventions:

### Sanskrit Diacritical Marks - CRITICAL

Always preserve exact diacritical marks:
- Śāriputra (not Sariputra)
- śūnyatā (emptiness - critical philosophical term)
- Mañjuśrī, Avalokiteśvara, Bodhisattva
- Key Unicode characters: ś (U+015B), ṇ (U+1E47), ū (U+016B), ā (U+0101), ṃ (U+1E43)

### Terminology Consistency

- Buddhist terms consistently capitalized: Dharma, Buddha, Bodhisattva, Tathagata, nirvāṇa
- Reference `/Lotus_Sutra/08_REFERENCE_MATERIALS/TERMINOLOGY_CORRECTIONS_SUMMARY.md` for standards
- Character names: Use `/Lotus_Sutra/08_REFERENCE_MATERIALS/CHARACTER_VOICE_MAPPING_FINAL.txt`

### Stylistic Register

**For Scholarly Version**:
- Formal, reverent tone befitting sacred scripture
- Traditional Buddhist terminology with consistent English equivalents
- Poetic but dignified language in verse sections

**For Blues Version**:
- Vernacular, accessible language
- Blues/gospel registers reflecting contemporary expression
- Different from formal version intentionally (not an error)

---

## Related Resources

### Reference Materials from Lotus Sutra Project

All of these apply to Diamond Sutra work when translation begins:

**Translation & Terminology**:
- `DIAMOND_SUTRA_GLOSSARY_HYBRID.md` - **The Authoritative Scholarly/Blues Glossary**
- `/Lotus_Sutra/08_REFERENCE_MATERIALS/TERMINOLOGY_CORRECTIONS_SUMMARY.md` - Consistent Buddhist terminology
- `/Lotus_Sutra/08_REFERENCE_MATERIALS/CHARACTER_VOICE_MAPPING_FINAL.txt` - Character names with diacriticals
- `/Lotus_Sutra/CLAUDE.md` - Comprehensive guidance on translation conventions

**Specialized Agents** (Available when your project expands):
- Dharma Audio Producer - For audio script optimization
- Dr. Amara Chen-Rothenberg - For scholarly article writing
- Miriam Steinberg - For publishing industry evaluation
- Kaelen "Kai" Reed - For poetic interpretation of classical texts
- HTML Code Master - For web development

See `/Lotus_Sutra/agents/` for detailed agent descriptions.

---

## Version Control

This directory **is not currently a git repository**. When translation work begins:

1. Initialize git: `git init`
2. Create `.gitignore` for temporary files
3. Commit frequently with clear messages
4. Reference the Lotus Sutra recovery procedures in `/Lotus_Sutra/CLAUDE.md`

---

## Important Notes

### Sacred Text Handling

This project contains sacred Buddhist scripture. Approach all work with:

- **Accuracy**: Preserve the integrity of the original text
- **Clear communication**: Document the purpose and nature of any modifications
- **Verification**: Double-check critical changes before committing
- **Respect**: Recognize the spiritual significance of the material

### Character Encoding

- Classical Buddhist texts require proper character encoding
- The Diamond Sutra is in classical Chinese (文言文) - do not modernize without explicit purpose
- Verify encoding after any edits: `file -i [filename]`

### Looking Ahead

When your team is ready to begin translation and interpretation:

1. Read `/Lotus_Sutra/CLAUDE.md` for comprehensive project methodology
2. Read `/Lotus_Sutra/.claude/SAFETY_VOW.md` - Understand the commitment to careful, sacred work
3. Consider using the Dharma Audio Producer agent for TTS optimization planning
4. Consider using Kaelen "Kai" Reed agent for poetic/musical interpretation of classical text

---

## Quick Reference: Navigation

- **Source text location**: Root directory - `金剛般若波羅蜜經 Diamond Sutra.txt`
- **Workspace overview**: Parent directory - `../CLAUDE.md`
- **Reference materials**: `../Lotus_Sutra/08_REFERENCE_MATERIALS/`
- **Project template**: Consult `/Lotus_Sutra/` folder structure for guidance on expansion

---

## Status & Next Steps

**Current Status**: 🟢 Well-Organized & In Progress

**Completed**:
- Classical Chinese source text (complete) in `00_SOURCE/`
- Scholarly translation (complete, Chapters 1-32) in `01_SCHOLARLY_TRANSLATION/`
- Blues interpretation (three versions) in `02_BLUES_INTERPRETATION/`
- Audio production files (ElevenLabs-optimized) in `03_AUDIO_PRODUCTION/`
- Project structure organized and documented

**Next Steps** (Potential Development):
1. Expand scholarly apparatus with additional footnotes
2. Consolidate blues interpretation versions
3. Record audio production
4. Create web application or interactive reader
5. Develop additional reference materials

---

**Last Updated**: November 29, 2025
**Created by**: Claude Code
**Repository Type**: Buddhist Sutra Translation Project (Active Development)
**Status**: Scholarly translation complete; blues interpretation and audio production in progress

