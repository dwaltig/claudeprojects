# AUDIT: Fascicle 4 Scholarly
## Road Manager Protocol (Wenju-style)

**Auditor**: Road Manager Protocol  
**Date**: February 7, 2026  
**Target scope**: `Fascicle_04_*_Scholarly.md` vs `T1912_004.txt`

---

## Header Summary

- **Task status**: **FAIL**
- **Model used**: Codex (GPT-5)
- **Source file**: `Guketsu_Project/02_SOURCE_MATERIALS/T1912/T1912_004.txt`
- **Source sentence units (punctuation-based)**: 4764
- **Current target sentence units (English punctuation-based, combined F04 scholarly files)**: 240
- **Total line delta**: **+4524 source units not explicitly mapped**

Interpretation: Fascicle 4 scholarly files are explanatory synthesis and not strict source-sequence CN->EN mapping.

---

## Severity Scale

- **CRITICAL**: material omission (Sacca violation)
- **WARNING**: paraphrase/summary where literal mapping is required
- **INFO**: minor style/format variance

---

## Findings by File

| File | Status | Defect ID | Severity | Finding |
|---|---|---|---|---|
| `Fascicle_04_Opening_Scholarly.md` | FAIL | `DEFECT-M04-OPEN-001` | CRITICAL | Introductory abstraction in place of source-line mapping. |
| `Fascicle_04_Section_01_Scholarly.md` | FAIL | `DEFECT-M04-S01-001` | CRITICAL | Doctrinal teaching notes replace sequential translation units. |
| `Fascicle_04_Section_02_Scholarly.md` | FAIL | `DEFECT-M04-S02-001` | CRITICAL | Reorganized explanatory structure breaks source order traceability. |
| `Fascicle_04_Section_03_Scholarly.md` | FAIL | `DEFECT-M04-S03-001` | CRITICAL | Integrative prose format omits explicit one-line CN->EN correspondence. |
| `Fascicle_04_Closing_Summary_Scholarly.md` | FAIL | `DEFECT-M04-CLS-001` | WARNING | Useful editorial summary, but not source-mapped translation. |

---

## Comparison Table (Representative)

| Source (T1912_004) | Current Translation | Required Correction |
|---|---|---|
| `釋二十五方便。初且通明漸頓二種。` | `## Introduction: From Foundation to Depth` | Replace with strict sequential CN->EN mapping. |
| `次今就下。方始別明今文方便。` | `Fascicle 4 continues the exposition...` | Remove summary framing; preserve source progression and argument flow. |
| `言善巧者。從初發心權實不二。` | Thematic tables and section summaries | Insert missing source material in order with explicit mapping. |

---

## Corrections (Starter Block)

```text
[ADDED][CN] 釋二十五方便。
[ADDED][EN] This explains the twenty-five skillful means.

[ADDED][CN] 初且通明漸頓二種。
[ADDED][EN] First, it generally clarifies the two kinds: gradual and sudden.

[ADDED][CN] 次今就下。方始別明今文方便。
[ADDED][EN] Next, in what follows, it begins specifically to explain the skillful means in this text.

[ADDED][CN] 初文通論頓方便者。
[ADDED][EN] In the first part, it generally discusses the sudden skillful means.
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

**Fascicle 4 Scholarly is not yet source-aligned under Road Manager Sacca criteria.**

It requires full compiler-loop rewriting into strict source-order CN->EN mapping.
