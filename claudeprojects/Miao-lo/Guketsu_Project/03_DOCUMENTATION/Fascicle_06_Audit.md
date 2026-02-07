# AUDIT: Fascicle 6 Scholarly
## Road Manager Protocol (Wenju-style)

**Auditor**: Road Manager Protocol  
**Date**: February 7, 2026  
**Target scope**: `Fascicle_06_*_Scholarly.md` vs `T1912_006.txt`

---

## Header Summary

- **Task status**: **FAIL**
- **Model used**: Codex (GPT-5)
- **Source file**: `Guketsu_Project/02_SOURCE_MATERIALS/T1912/T1912_006.txt`
- **Source sentence units (punctuation-based)**: 5268
- **Current target sentence units (English punctuation-based, combined F06 scholarly files)**: 242
- **Total line delta**: **+5026 source units not explicitly mapped**

Interpretation: Fascicle 6 scholarly files are explanatory translations and not strict source-sequence CN->EN line mapping.

---

## Severity Scale

- **CRITICAL**: material omission (Sacca violation)
- **WARNING**: paraphrase/summary where literal mapping is required
- **INFO**: minor style/format variance

---

## Findings by File

| File | Status | Defect ID | Severity | Finding |
|---|---|---|---|---|
| `Fascicle_06_Opening_Scholarly.md` | FAIL | `DEFECT-M06-OPEN-001` | CRITICAL | Introductory prose replaces source-sequence unit mapping. |
| `Fascicle_06_Section_01_Scholarly.md` | FAIL | `DEFECT-M06-S01-001` | CRITICAL | Didactic synthesis; direct CN->EN one-line correspondence missing. |
| `Fascicle_06_Section_02_Scholarly.md` | FAIL | `DEFECT-M06-S02-001` | CRITICAL | Reframed pedagogical structure obscures source order traceability. |
| `Fascicle_06_Closing_Summary_Scholarly.md` | FAIL | `DEFECT-M06-CLS-001` | WARNING | Editorial summary artifact; not source-mapped translation. |

---

## Comparison Table (Representative)

| Source (T1912_006) | Current Translation | Required Correction |
|---|---|---|
| `次明破思假。初列思假名。` | `## Introduction to Breaking Through Thought-Delusion` | Replace with strict sequential CN->EN mapping. |
| `云亦名正三毒者。思惑有四慢入癡攝。` | Expository framing on doctrinal context | Restore source sentence order and direct rendering. |
| `故但云三。一非背使二非習氣。` | Modern explanatory segmentation | Insert omitted source units with explicit line mapping. |

---

## Corrections (Starter Block)

```text
[ADDED][CN] 次明破思假。
[ADDED][EN] Next, it clarifies the breaking through of thought-delusion.

[ADDED][CN] 初列思假名。
[ADDED][EN] First, it lists the name of thought-delusion.

[ADDED][CN] 云亦名正三毒者。
[ADDED][EN] It says this is also called the three correct poisons.

[ADDED][CN] 思惑有四慢入癡攝。
[ADDED][EN] Thought-delusion has four; pride is included under delusion.
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

**Fascicle 6 Scholarly is not yet source-aligned under Road Manager Sacca criteria.**

It requires full compiler-loop rewriting into strict source-order CN->EN mapping.
