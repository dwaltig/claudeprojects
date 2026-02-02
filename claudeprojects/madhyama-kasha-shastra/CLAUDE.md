# CLAUDE.md - Madhyamakashāstra Translation Project

## Project Overview

This project translates Nāgārjuna's **Mūlamadhyamakakārikā** (Root Verses of the Middle Way) with Candrakīrti's **Prasannapadā** (Clear Words) commentary from Sanskrit into English. The project uses a **dual-translation methodology**:
1. **Scholarly Edition**: Full academic apparatus with extensive footnotes
2. **Blues Vernacular**: Accessible American English preserving philosophical depth

## Source Text

- **Edition**: Mithila Institute (1960), edited by Dr. P.L. Vaidya
- **Base Text**: La Vallée Poussin critical edition (1912)
- **File**: `madhyama-kasha-shastra-of-nagarjuna.txt` (OCR scan)
- **Structure**: 27 chapters (*parīkṣā* - "examinations")

## Critical Safety Protocol

**READ BEFORE EDITING:**
- **Preserve Sanskrit**: Handle diacritics with extreme care (ś, ṣ, ṇ, ā, ī, ū, ṃ, ḥ)
- **Verify UTF-8**: Ensure proper encoding
- **Ask First**: Confirm structural changes with the user
- **OCR Awareness**: Source text has OCR noise—verify readings

## Directory Structure

```
madhyama-kasha-shastra/
├── CLAUDE.md                    # This file
├── GEMINI.md                    # AI agent context
├── 01_TRANSLATIONS/             # Scholarly and Blues versions
├── 02_SOURCE_MATERIALS/         # Extracted Sanskrit chapters  
├── 03_DOCUMENTATION/            # Session notes, glossary
├── 04_AGENTS/                   # Professor and Bluesman definitions
└── madhyama-kasha-shastra-of-nagarjuna.txt  # Full OCR source
```

## Specialized Agents

### The Professor (Dr. Rajesh Patel)
- Sanskrit → Scholarly English with philological apparatus
- Dialectical structure (pūrvapakṣa/uttarapakṣa)
- Cross-references with other Mādhyamaka texts
- **File**: `04_AGENTS/The_Professor.md`

### The Bluesman (Master John Kim)
- Reviews Professor's work for completeness
- Creates Blues vernacular version
- Transforms dialectical arguments into Blues narratives
- **File**: `04_AGENTS/The_Bluesman.md`

## Translation Workflow

1. **Professor translates** Sanskrit → Scholarly English
2. **Bluesman reviews** for missed nuances
3. **Bluesman creates** Blues vernacular version
4. **QA audit** via DeepSeek/Rationalist Reviewer
5. **Consolidate** into Combined files

## The 27 Chapters (Parīkṣā)

| Ch | Sanskrit Title | English Title |
|:---|:---------------|:--------------|
| 1 | Pratyaya-parīkṣā | Examination of Conditions |
| 2 | Gatagata-parīkṣā | Examination of Motion |
| 3 | Cakṣurādīndriya-parīkṣā | Examination of the Senses |
| 4 | Skandha-parīkṣā | Examination of Aggregates |
| 5 | Dhātu-parīkṣā | Examination of Elements |
| 6 | Rāgarakta-parīkṣā | Examination of Desire |
| 7 | Saṃskṛta-parīkṣā | Examination of the Conditioned |
| 8 | Karmakāraka-parīkṣā | Examination of Action and Agent |
| 9 | Pūrva-parīkṣā | Examination of the Prior |
| 10 | Agnīndhana-parīkṣā | Examination of Fire and Fuel |
| 11 | Pūrvāparakoṭi-parīkṣā | Examination of Beginning and End |
| 12 | Duḥkha-parīkṣā | Examination of Suffering |
| 13 | Saṃskāra-parīkṣā | Examination of Formations |
| 14 | Saṃsarga-parīkṣā | Examination of Conjunction |
| 15 | Svabhāva-parīkṣā | Examination of Own-Nature |
| 16 | Bandhamokṣa-parīkṣā | Examination of Bondage and Liberation |
| 17 | Karmaphala-parīkṣā | Examination of Action and Result |
| 18 | Ātma-parīkṣā | Examination of Self |
| 19 | Kāla-parīkṣā | Examination of Time |
| 20 | Sāmagrī-parīkṣā | Examination of Totality |
| 21 | Saṃbhavavibhava-parīkṣā | Examination of Arising and Passing |
| 22 | Tathāgata-parīkṣā | Examination of the Tathāgata |
| 23 | Viparyāsa-parīkṣā | Examination of Error |
| 24 | Āryasatya-parīkṣā | Examination of Noble Truths |
| 25 | Nirvāṇa-parīkṣā | Examination of Nirvāṇa |
| 26 | Dvādaśāṅga-parīkṣā | Examination of Twelve Links |
| 27 | Dṛṣṭi-parīkṣā | Examination of Views |

## Key Philosophical Concepts

- **śūnyatā** (शून्यता): Emptiness—absence of intrinsic nature (svabhāva)
- **pratītyasamutpāda** (प्रतीत्यसमुत्पाद): Dependent origination
- **svabhāva** (स्वभाव): Intrinsic/own-nature (what is negated)
- **catuṣkoṭi** (चतुष्कोटि): Tetralemma (four-cornered negation)
- **prasaṅga** (प्रसङ्ग): Consequence/reductio argument

## Technical Context

- **Language**: Sanskrit → English (scholarly + vernacular)
- **Encoding**: UTF-8 (preserve IAST diacritics)
- **Format**: Markdown for all translation files

---

**Project Initialized**: 2026-01-10
