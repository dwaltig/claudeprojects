# AUDIT: Fascicle 1 Scholarly
## Compiler Loop Log

**Auditor**: Road Manager Protocol  
**Date**: February 6, 2026  
**Target file**: `Fascicle_01_Opening_Scholarly.md`

---

## Boundary Mapping

- **CBETA source**: `T1912_001.txt`
- **Mapped span**: source line 20, sentence units 1-29
- **Scope rationale**: opening Q/A and ten-intention block through the third-version redaction note.

---

## Initial Audit

- **Status**: FAIL
- **Finding**:
  - Existing file body was summary/commentary-heavy and not strict source-sequence mapping for the mapped span.
- **Defect**: `DEFECT-M01-OPEN-001`
  - **Type**: Omission + Addition
  - **Omission**: no one-line CN->EN mapping for units 1-29.
  - **Addition**: extensive non-source analytical prose displaced source-line fidelity.

---

## Repair Applied

- Replaced body with strict bilingual sequence for mapped span.
- Preserved exact Chinese sentence order for units 1-29.
- Added one English line per Chinese source line.

---

## Re-Audit Verification

- `source_units=29`
- `target_cn_units=29`
- `target_en_units=29`
- `cn_sequence_match=PASS`

---

## Status

- `DEFECT-M01-OPEN-001`: **Closed**
- File status: **PASS** (for mapped opening span only)

---

## Compiler Loop #2

**Auditor**: Road Manager Protocol  
**Date**: February 6, 2026  
**Target file**: `Fascicle_01_Preface_Scholarly.md`

### Boundary Mapping

- **CBETA source**: `T1912_001.txt`
- **Mapped span**: source line 12, sentence units 1-59
- **Scope rationale**: preface prose from the anti-anti-text opening argument through the dated colophon.

### Initial Audit

- **Status**: FAIL
- **Finding**:
  - Existing file body was commentary/annotation-heavy and not strict source-sequence line mapping for the mapped span.
- **Defect**: `DEFECT-M01-PREF-001`
  - **Type**: Omission + Addition
  - **Omission**: no one-line CN->EN mapping for units 1-59.
  - **Addition**: extensive non-source contextual prose displaced source-line fidelity.

### Repair Applied

- Replaced body with strict bilingual sequence for mapped span.
- Preserved exact Chinese sentence order for units 1-59.
- Added one English line per Chinese source line.

### Re-Audit Verification

- `source_units=59`
- `target_cn_units=59`
- `target_en_units=59`
- `cn_sequence_match=PASS`

### Status

- `DEFECT-M01-PREF-001`: **Closed**
- File status: **PASS** (for mapped preface span only)

---

## Compiler Loop #3

**Auditor**: Road Manager Protocol  
**Date**: February 6, 2026  
**Target file**: `Fascicle_01_Section02_Title_Scholarly.md`

### Boundary Mapping

- **CBETA source**: `T1912_001.txt`
- **Mapped span**: source line 20, sentence units 91-154
- **Scope rationale**: "Mohe" title rationale, general/particular structure, and common-preface framing through the "previous generations" claim.

### Initial Audit

- **Status**: FAIL
- **Finding**:
  - Existing file body used expanded analytical exposition and was not strict source-sequence line mapping for the mapped span.
- **Defect**: `DEFECT-M01-S02-001`
  - **Type**: Omission + Addition
  - **Omission**: no one-line CN->EN mapping for units 91-154.
  - **Addition**: non-source doctrinal commentary displaced direct source fidelity.

### Repair Applied

- Replaced body with strict bilingual sequence for mapped span.
- Preserved exact Chinese sentence order for units 91-154.
- Added one English line per Chinese source line.

### Re-Audit Verification

- `source_units=64`
- `target_cn_units=64`
- `target_en_units=64`
- `cn_sequence_match=PASS`

### Status

- `DEFECT-M01-S02-001`: **Closed**
- File status: **PASS** (for mapped Section 2 span only)

---

## Compiler Loop #4

**Auditor**: Road Manager Protocol  
**Date**: February 6, 2026  
**Target file**: `Fascicle_01_Section_03_Scholarly.md`

### Boundary Mapping

- **CBETA source**: `T1912_001.txt`
- **Mapped span**: source line 20, sentence units 270-319
- **Scope rationale**: bridge from the "Five Summaries" reference into the lineage/source-root argument and the twenty-three patriarch transmission framing.

### Initial Audit

- **Status**: FAIL
- **Finding**:
  - Existing file body was synthesized exposition/commentary and not strict source-sequence line mapping for the mapped span.
- **Defect**: `DEFECT-M01-S03-001`
  - **Type**: Omission + Addition
  - **Omission**: no one-line CN->EN mapping for units 270-319.
  - **Addition**: non-source analytical content displaced direct source fidelity.

### Repair Applied

- Replaced body with strict bilingual sequence for mapped span.
- Preserved exact Chinese sentence order for units 270-319.
- Added one English line per Chinese source line.

### Re-Audit Verification

- `source_units=50`
- `target_cn_units=50`
- `target_en_units=50`
- `cn_sequence_match=PASS`

### Status

- `DEFECT-M01-S03-001`: **Closed**
- File status: **PASS** (for mapped Section 3 span only)

---

## Compiler Loop #5

**Auditor**: Road Manager Protocol  
**Date**: February 6, 2026  
**Target file**: `Fascicle_01_Section_04_Scholarly.md`

### Boundary Mapping

- **CBETA source**: `T1912_001.txt`
- **Mapped span**: source line 20, sentence units 1060-1093
- **Scope rationale**: biography segment covering birth signs, Dasu encounter, Lotus-samadhi entry, and Huisi's recognition statement.

### Initial Audit

- **Status**: FAIL
- **Finding**:
  - Existing file body was synthesized commentary and not strict source-sequence line mapping for the mapped span.
- **Defect**: `DEFECT-M01-S04-001`
  - **Type**: Omission + Addition
  - **Omission**: no one-line CN->EN mapping for units 1060-1093.
  - **Addition**: non-source interpretation displaced direct source fidelity.

### Repair Applied

- Replaced body with strict bilingual sequence for mapped span.
- Preserved exact Chinese sentence order for units 1060-1093.
- Added one English line per Chinese source line.

### Re-Audit Verification

- `source_units=34`
- `target_cn_units=34`
- `target_en_units=34`
- `cn_sequence_match=PASS`

### Status

- `DEFECT-M01-S04-001`: **Closed**
- File status: **PASS** (for mapped Section 4 span only)

---

## Compiler Loop #6

**Auditor**: Road Manager Protocol  
**Date**: February 6, 2026  
**Target file**: `Fascicle_01_Section_05_Scholarly.md`

### Boundary Mapping

- **CBETA source**: `T1912_001.txt`
- **Mapped span**: source line 20, sentence units 1094-1158
- **Scope rationale**: continuation from Zhizhe's certification into proxy-lecture transmission, Chen/Sui movement context, and imperial memorial/edict record.

### Initial Audit

- **Status**: FAIL
- **Finding**:
  - Existing file body contained non-canonical "Ten Wrongs" synthesis not matching the verified contiguous source sequence for this fascicle workflow.
- **Defect**: `DEFECT-M01-S05-001`
  - **Type**: Canonical Misalignment + Addition
  - **Misalignment**: content block was not mapped to the active verified source boundary sequence.
  - **Addition**: non-source analytical content displaced direct source fidelity.

### Repair Applied

- Replaced body with strict bilingual sequence for mapped span.
- Preserved exact Chinese sentence order for units 1094-1158.
- Added one English line per Chinese source line.

### Re-Audit Verification

- `source_units=65`
- `target_cn_units=65`
- `target_en_units=65`
- `cn_sequence_match=PASS`

### Status

- `DEFECT-M01-S05-001`: **Closed**
- File status: **PASS** (for mapped Section 5 span only)

---

## Compiler Loop #7

**Auditor**: Road Manager Protocol  
**Date**: February 6, 2026  
**Target file**: `Fascicle_01_Section_06_Scholarly.md`

### Boundary Mapping

- **CBETA source**: `T1912_001.txt`
- **Mapped span**: source line 20, sentence units 1159-1225
- **Scope rationale**: final-life practice-rank narrative, terminal instruction, doctrinal final words, and seated nirvana entry.

### Initial Audit

- **Status**: FAIL
- **Finding**:
  - Existing file body was non-canonical synthesis and not strict source-sequence line mapping for the mapped span.
- **Defect**: `DEFECT-M01-S06-001`
  - **Type**: Canonical Misalignment + Addition
  - **Misalignment**: content was not mapped to the active verified contiguous source sequence.
  - **Addition**: non-source analytical content displaced direct source fidelity.

### Repair Applied

- Replaced body with strict bilingual sequence for mapped span.
- Preserved exact Chinese sentence order for units 1159-1225.
- Added one English line per Chinese source line.

### Re-Audit Verification

- `source_units=67`
- `target_cn_units=67`
- `target_en_units=67`
- `cn_sequence_match=PASS`

### Status

- `DEFECT-M01-S06-001`: **Closed**
- File status: **PASS** (for mapped Section 6 span only)

---

## Compiler Loop #8

**Auditor**: Road Manager Protocol  
**Date**: February 6, 2026  
**Target file**: `Fascicle_01_Section_07_Scholarly.md`

### Boundary Mapping

- **CBETA source**: `T1912_001.txt`
- **Mapped span**: source line 20, sentence units 1226-1310
- **Scope rationale**: post-extinction auspicious signs, fifth-grade validation with sutra citations, and the transition into Nanyue/Huiwen training up through the variant-transmission note.

### Initial Audit

- **Status**: FAIL
- **Finding**:
  - Existing file body was non-canonical synthesis ("Six Identities" exposition) and not strict source-sequence line mapping for the mapped span.
- **Defect**: `DEFECT-M01-S07-001`
  - **Type**: Canonical Misalignment + Addition
  - **Misalignment**: content was not mapped to the active verified contiguous source sequence.
  - **Addition**: non-source analytical exposition displaced direct source fidelity.

### Repair Applied

- Replaced body with strict bilingual sequence for mapped span.
- Preserved exact Chinese sentence order for units 1226-1310.
- Added one English line per Chinese source line.

### Re-Audit Verification

- `source_units=85`
- `target_cn_units=85`
- `target_en_units=85`
- `cn_sequence_match=PASS`

### Status

- `DEFECT-M01-S07-001`: **Closed**
- File status: **PASS** (for mapped Section 7 span only)

---

## Compiler Loop #9

**Auditor**: Road Manager Protocol  
**Date**: February 6, 2026  
**Target file**: `Fascicle_01_Section_08_Scholarly.md`

### Boundary Mapping

- **CBETA source**: `T1912_001.txt`
- **Mapped span**: source line 20, sentence units 1311-1386
- **Scope rationale**: Nanyue/Huiwen lineage exposition, nine-master method list, and the high-ancestor naming rationale through the setup of the next hypothetical question.

### Initial Audit

- **Status**: FAIL
- **Finding**:
  - Existing file body was non-canonical synthesis ("Ten Chapters / Five Abbreviations") and not strict source-sequence line mapping for the mapped span.
- **Defect**: `DEFECT-M01-S08-001`
  - **Type**: Canonical Misalignment + Addition
  - **Misalignment**: content was not mapped to the active verified contiguous source sequence.
  - **Addition**: non-source analytical exposition displaced direct source fidelity.

### Repair Applied

- Replaced body with strict bilingual sequence for mapped span.
- Preserved exact Chinese sentence order for units 1311-1386.
- Added one English line per Chinese source line.

### Re-Audit Verification

- `source_units=76`
- `target_cn_units=76`
- `target_en_units=76`
- `cn_sequence_match=PASS`

### Status

- `DEFECT-M01-S08-001`: **Closed**
- File status: **PASS** (for mapped Section 8 span only)

---

## Compiler Loop #10

**Auditor**: Road Manager Protocol  
**Date**: February 6, 2026  
**Target file**: `Fascicle_01_Section_09_Scholarly.md`

### Boundary Mapping

- **CBETA source**: `T1912_001.txt`
- **Mapped span**: source line 20, sentence units 1387-1477
- **Scope rationale**: lineage-consistency objection and reply, Madhyamaka commentary transmission evidence, "ji" doctrinal clarification, and Tiantai-name etymology through the listed teaching/object/name marker.
- **Boundary note**: raw tokenizer emitted a trailing newline token at unit 1478; excluded as non-text.

### Initial Audit

- **Status**: FAIL
- **Finding**:
  - Existing file body was non-canonical synthesis ("Three Kinds of Zhiguan") and not strict source-sequence line mapping for the mapped span.
- **Defect**: `DEFECT-M01-S09-001`
  - **Type**: Canonical Misalignment + Addition
  - **Misalignment**: content was not mapped to the active verified contiguous source sequence.
  - **Addition**: non-source analytical exposition displaced direct source fidelity.

### Repair Applied

- Replaced body with strict bilingual sequence for mapped span.
- Preserved exact Chinese sentence order for units 1387-1477.
- Added one English line per Chinese source line.

### Re-Audit Verification

- `source_units=91`
- `target_cn_units=91`
- `target_en_units=91`
- `cn_sequence_match=PASS`

### Status

- `DEFECT-M01-S09-001`: **Closed**
- File status: **PASS** (for mapped Section 9 span only)

---

## Compiler Loop #11

**Auditor**: Road Manager Protocol  
**Date**: February 6, 2026  
**Target file**: `Fascicle_01_Closing_Summary_Scholarly.md`

### Boundary Mapping

- **CBETA source**: `T1912_001.txt`
- **Mapped span**: source line 69, sentence units 1-89
- **Scope rationale**: opening of the "unconditioned vows" doctrinal block, including three-truth analysis, mirror analogy setup, and Huayan citation cluster through the concluding interpretive line.

### Initial Audit

- **Status**: FAIL
- **Finding**:
  - Existing file body was synthetic summary prose and not strict source-sequence line mapping.
- **Defect**: `DEFECT-M01-CLOSE-001`
  - **Type**: Canonical Misalignment + Addition
  - **Misalignment**: content was not mapped to the active verified source boundary.
  - **Addition**: non-source synthetic exposition displaced direct source fidelity.

### Repair Applied

- Replaced body with strict bilingual sequence for mapped span.
- Preserved exact Chinese sentence order for units 1-89.
- Added one English line per Chinese source line.

### Re-Audit Verification

- `source_units=89`
- `target_cn_units=89`
- `target_en_units=89`
- `cn_sequence_match=PASS`

### Status

- `DEFECT-M01-CLOSE-001`: **Closed**
- File status: **PASS** (for mapped Closing span only)

---

## Compiler Loop #12

**Auditor**: Road Manager Protocol  
**Date**: February 6, 2026  
**Target file**: `Fascicle_01_Opening_Scholarly.md`

### Boundary Mapping

- **CBETA source**: `T1912_001.txt`
- **Mapped span**: source line 20, sentence units 1-90
- **Scope rationale**: continuation immediately after the original opening span, covering the redaction-structure discussion through the completion of the "general preface" placement rationale.

### Initial Audit

- **Status**: FAIL
- **Finding**:
  - Existing file had been source-aligned only for units 1-29, leaving units 30-90 omitted under strict contiguous coverage requirements.
- **Defect**: `DEFECT-M01-OPEN-002`
  - **Type**: Omission (Coverage Gap)
  - **Omission**: no one-line CN->EN mapping for units 30-90.

### Repair Applied

- Extended the file boundary from units 1-29 to units 1-90.
- Appended strict bilingual sequence for units 30-90.
- Preserved exact Chinese sentence order and one English line per source line.

### Re-Audit Verification

- `source_units=90`
- `target_cn_units=90`
- `target_en_units=90`
- `cn_sequence_match=PASS`

### Status

- `DEFECT-M01-OPEN-002`: **Closed**
- File status: **PASS** (for mapped Opening span 1-90)

---

## Compiler Loop #13

**Auditor**: Road Manager Protocol  
**Date**: February 6, 2026  
**Target file**: `Fascicle_01_Section02_Title_Scholarly.md`

### Boundary Mapping

- **CBETA source**: `T1912_001.txt`
- **Mapped span**: source line 20, sentence units 91-269
- **Scope rationale**: continuation of the section immediately after unit 154, covering lineage-time/place exposition, naming etymologies, historical chronology, and transmission-context analysis through the thinkable-domain closing sentence.

### Initial Audit

- **Status**: FAIL
- **Finding**:
  - Existing file had been source-aligned only for units 91-154, leaving units 155-269 omitted under strict contiguous coverage requirements.
- **Defect**: `DEFECT-M01-S02-002`
  - **Type**: Omission (Coverage Gap)
  - **Omission**: no one-line CN->EN mapping for units 155-269.

### Repair Applied

- Extended the file boundary from units 91-154 to units 91-269.
- Appended strict bilingual sequence for units 155-269.
- Preserved exact Chinese sentence order and one English line per source line.

### Re-Audit Verification

- `source_units=179`
- `target_cn_units=179`
- `target_en_units=179`
- `cn_sequence_match=PASS`

### Status

- `DEFECT-M01-S02-002`: **Closed**
- File status: **PASS** (for mapped Section 2 span 91-269)

---

## Compiler Loop #14

**Auditor**: Road Manager Protocol  
**Date**: February 6, 2026  
**Target file**: `Fascicle_01_Section_03_Scholarly.md`

### Boundary Mapping

- **CBETA source**: `T1912_001.txt`
- **Mapped span**: source line 20, sentence units 270-420
- **Scope rationale**: continuation after the initial section-3 span, covering "teacher/no-teacher" doctrinal proof, prediction logic, and lineage-axiom exposition through the kalpa-definition setup.

### Initial Audit

- **Status**: FAIL
- **Finding**:
  - Existing file had been source-aligned only for units 270-319, leaving units 320-420 omitted under strict contiguous coverage requirements.
- **Defect**: `DEFECT-M01-S03-002`
  - **Type**: Omission (Coverage Gap)
  - **Omission**: no one-line CN->EN mapping for units 320-420.

### Repair Applied

- Extended the file boundary from units 270-319 to units 270-420.
- Appended strict bilingual sequence for units 320-420.
- Preserved exact Chinese sentence order and one English line per source line.

### Re-Audit Verification

- `source_units=151`
- `target_cn_units=151`
- `target_en_units=151`
- `cn_sequence_match=PASS`

### Status

- `DEFECT-M01-S03-002`: **Closed**
- File status: **PASS** (for mapped Section 3 span 270-420)

---

## Compiler Loop #15

**Auditor**: Road Manager Protocol  
**Date**: February 6, 2026  
**Target file**: `Fascicle_01_Section_03_Scholarly.md`

### Boundary Mapping

- **CBETA source**: `T1912_001.txt`
- **Mapped span**: source line 20, sentence units 270-520
- **Scope rationale**: contiguous extension covering kalpa-measure analogies, six-year austerity and Mara-subjugation citations, and Deer Park narrative through the bodhisattva deer-king substitution declaration.

### Initial Audit

- **Status**: FAIL
- **Finding**:
  - Existing file had been source-aligned only for units 270-420, leaving units 421-520 omitted under strict contiguous coverage requirements.
- **Defect**: `DEFECT-M01-S03-003`
  - **Type**: Omission (Coverage Gap)
  - **Omission**: no one-line CN->EN mapping for units 421-520.

### Repair Applied

- Extended the file boundary from units 270-420 to units 270-520.
- Appended strict bilingual sequence for units 421-520.
- Preserved exact Chinese sentence order and one English line per source line.

### Re-Audit Verification

- `source_units=251`
- `target_cn_units=251`
- `target_en_units=251`
- `cn_sequence_match=PASS`

### Status

- `DEFECT-M01-S03-003`: **Closed**
- File status: **PASS** (for mapped Section 3 span 270-520)
