# AUDIT: Fascicle 3 Scholarly
## Road Manager Protocol (Wenju-style)

**Auditor**: Road Manager Protocol  
**Date**: February 7, 2026  
**Target scope**: `Fascicle_03_*_Scholarly.md` vs `T1912_003.txt`

---

## Header Summary

- **Task status**: **FAIL**
- **Model used**: Codex (GPT-5)
- **Source file**: `Guketsu_Project/02_SOURCE_MATERIALS/T1912/T1912_003.txt`
- **Source sentence units (punctuation-based)**: 6893
- **Current target sentence units (English punctuation-based, combined F03 scholarly files)**: 267
- **Total line delta**: **+6626 source units not explicitly mapped**

Interpretation: Fascicle 3 scholarly files are explanatory/doctrinal summaries and not strict source-sequence CN->EN mapping.

---

## Severity Scale

- **CRITICAL**: material omission (Sacca violation)
- **WARNING**: paraphrase/summary where literal mapping is required
- **INFO**: minor style/format variance

---

## Boundary Mapping

- **CBETA source**: `T1912_003.txt`
- **Audit mode**: fascicle-level structural and coverage audit
- **Scope rationale**: same Wenju/Guketsu compiler-loop gate used for F01-F02

---

## Findings by File

| File | Status | Defect ID | Severity | Finding |
|---|---|---|---|---|
| `Fascicle_03_Opening_Scholarly.md` | FAIL | `DEFECT-M03-OPEN-001` | CRITICAL | Intro/tables replace source-sequence line mapping. |
| `Fascicle_03_Section_01_Scholarly.md` | FAIL | `DEFECT-M03-S01-001` | CRITICAL | Doctrinal narrative instead of direct bilingual sequence. |
| `Fascicle_03_Section_02_Scholarly.md` | FAIL | `DEFECT-M03-S02-001` | CRITICAL | Structured exposition; source line order not explicitly preserved. |
| `Fascicle_03_Section_03_Scholarly.md` | FAIL | `DEFECT-M03-S03-001` | CRITICAL | Troubleshooting synthesis displaces source-proximal rendering. |
| `Fascicle_03_Section_04_Scholarly.md` | FAIL | `DEFECT-M03-S04-001` | CRITICAL | Overview chapter format; no one-line CN->EN traceability. |
| `Fascicle_03_Closing_Summary_Scholarly.md` | FAIL | `DEFECT-M03-CLS-001` | WARNING | Valid editorial summary artifact, not a source-translation mapping file. |

---

## Comparison Table (Representative)

| Source (T1912_003) | Current Translation | Required Correction |
|---|---|---|
| `大章第二釋名者。夫立名不同。` | `## Introduction: From Theory to Practice` | Replace with ordered CN->EN rendering for each source sentence. |
| `如大經云。或有因緣如目連等。或無因緣如桃李等。` | `Fascicle 3 marks the transition...` | Remove summary framing; preserve source sequence and logical pivots. |
| `涅槃亦爾。無有因緣彊為立名。` | Thematic tables and modern explanations | Insert omitted source material with explicit line mapping. |

---

## Corrections (Starter Block)

```text
[ADDED][CN] 大章第二釋名者。
[ADDED][EN] In the second major chapter, it explains the name.

[ADDED][CN] 夫立名不同。
[ADDED][EN] The establishment of names is not uniform.

[ADDED][CN] 如大經云。
[ADDED][EN] As the Mahaparinirvana Sutra says.

[ADDED][CN] 或有因緣如目連等。或無因緣如桃李等。
[ADDED][EN] Some names have causal conditions, like Mahamaudgalyayana and others; some are without such conditions, like peach and plum.
```

---

## Definition of Done Checklist

- [ ] Every source line is mapped to a translation line.
- [ ] No source material is omitted.
- [ ] No new material is added beyond the source.
- [ ] All CRITICAL items are corrected.
- [x] Line delta is reported and explained.
- [x] Corrected translation starter block is provided with `[ADDED]` tags.
- [ ] Full line mapping is included for the complete fascicle.

---

## Recommended Compiler-Loop Order

1. `Fascicle_03_Opening_Scholarly.md`
2. `Fascicle_03_Section_01_Scholarly.md`
3. `Fascicle_03_Section_02_Scholarly.md`
4. `Fascicle_03_Section_03_Scholarly.md`
5. `Fascicle_03_Section_04_Scholarly.md`
6. `Fascicle_03_Closing_Summary_Scholarly.md` (keep as summary artifact or relabel as non-source translation)

---

## Audit Verdict

**Fascicle 3 Scholarly is not yet source-aligned under Road Manager Sacca criteria.**

It needs a full compiler-loop rewrite from summary/expository style into strict CN->EN source-order mapping.
