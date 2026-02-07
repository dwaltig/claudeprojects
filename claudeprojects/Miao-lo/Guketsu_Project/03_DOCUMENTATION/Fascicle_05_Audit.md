# AUDIT: Fascicle 5 Scholarly
## Road Manager Protocol (Wenju-style)

**Auditor**: Road Manager Protocol  
**Date**: February 7, 2026  
**Target scope**: `Fascicle_05_*_Scholarly.md` vs `T1912_005.txt`

---

## Header Summary

- **Task status**: **FAIL**
- **Model used**: Codex (GPT-5)
- **Source file**: `Guketsu_Project/02_SOURCE_MATERIALS/T1912/T1912_005.txt`
- **Source sentence units (punctuation-based)**: 9281
- **Current target sentence units (English punctuation-based, combined F05 scholarly files)**: 182
- **Total line delta**: **+9099 source units not explicitly mapped**

Interpretation: Fascicle 5 scholarly files are high-level explanatory prose and not strict source-sequence CN->EN line mapping.

---

## Severity Scale

- **CRITICAL**: material omission (Sacca violation)
- **WARNING**: paraphrase/summary where literal mapping is required
- **INFO**: minor style/format variance

---

## Findings by File

| File | Status | Defect ID | Severity | Finding |
|---|---|---|---|---|
| `Fascicle_05_Opening_Scholarly.md` | FAIL | `DEFECT-M05-OPEN-001` | CRITICAL | Intro framework replaces source-sequence rendering. |
| `Fascicle_05_Section_01_Scholarly.md` | FAIL | `DEFECT-M05-S01-001` | CRITICAL | Analytical synthesis with missing explicit CN->EN mapping units. |
| `Fascicle_05_Section_02_Scholarly.md` | FAIL | `DEFECT-M05-S02-001` | CRITICAL | Reorganized doctrinal explanation obscures source-order fidelity. |
| `Fascicle_05_Closing_Summary_Scholarly.md` | FAIL | `DEFECT-M05-CLS-001` | WARNING | Editorial summary artifact; not a source-mapping translation file. |

---

## Comparison Table (Representative)

| Source (T1912_005) | Current Translation | Required Correction |
|---|---|---|
| `初釋正觀中先明來意。亦名結前生後。` | `## Introduction: The Final Four Objects` | Replace with strict ordered CN->EN mapping. |
| `於中初略次廣。初文結前。` | `Fascicle 5 completes the treatment...` | Remove summary framing and restore source progression. |
| `今依下生後。` | Tables and modern explanatory sections | Insert omitted source lines in original sequence. |

---

## Corrections (Starter Block)

```text
[ADDED][CN] 初釋正觀中先明來意。
[ADDED][EN] In first explaining Correct Contemplation, it first clarifies the intent.

[ADDED][CN] 亦名結前生後。
[ADDED][EN] This is also called concluding what precedes and giving rise to what follows.

[ADDED][CN] 於中初略次廣。
[ADDED][EN] Within this, it is first concise and then extensive.

[ADDED][CN] 初文結前。
[ADDED][EN] The first passage concludes what came before.
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

## Audit Verdict

**Fascicle 5 Scholarly is not yet source-aligned under Road Manager Sacca criteria.**

It requires full compiler-loop rewriting into strict source-order CN->EN mapping.
