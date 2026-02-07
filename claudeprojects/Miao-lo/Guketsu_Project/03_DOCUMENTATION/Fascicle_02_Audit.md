# AUDIT: Fascicle 2 Scholarly
## Road Manager Protocol (Wenju-style)

**Auditor**: Road Manager Protocol  
**Date**: February 7, 2026  
**Target scope**: `Fascicle_02_*_Scholarly.md` vs `T1912_002.txt`

---

## Header Summary

- **Task status**: **FAIL**
- **Model used**: Codex (GPT-5)
- **Source file**: `Guketsu_Project/02_SOURCE_MATERIALS/T1912/T1912_002.txt`
- **Source sentence units (punctuation-based)**: 6408
- **Current target sentence units (English punctuation-based, combined F02 scholarly files)**: 333
- **Total line delta**: **+6075 source units not explicitly mapped**

Interpretation: current Fascicle 2 scholarly files are editorial summaries and structured exposition, not strict source-sequence CN->EN line mapping.

---

## Severity Scale

- **CRITICAL**: material omission (Sacca violation)
- **WARNING**: paraphrase/summary where literal mapping is required
- **INFO**: minor style/format variance

---

## Boundary Mapping

- **CBETA source**: `T1912_002.txt`
- **Audit mode**: fascicle-level structural and coverage audit
- **Scope rationale**: replicate Wenju-style gate first (coverage + fidelity), then drive file-by-file compiler loops

---

## Findings by File

| File | Status | Defect ID | Severity | Finding |
|---|---|---|---|---|
| `Fascicle_02_Section_01_Scholarly.md` | FAIL | `DEFECT-M02-S01-001` | CRITICAL | Summary/expository prose; no one-line CN->EN source mapping. |
| `Fascicle_02_Section_02_Scholarly.md` | FAIL | `DEFECT-M02-S02-001` | CRITICAL | Doctrinal paraphrase replaces direct sequential rendering. |
| `Fascicle_02_Section_03_Scholarly.md` | FAIL | `DEFECT-M02-S03-001` | CRITICAL | Chapterized synthesis not aligned to source sentence order. |
| `Fascicle_02_Section_04_Scholarly.md` | FAIL | `DEFECT-M02-S04-001` | CRITICAL | High-level taxonomy; missing explicit source-line correspondence. |
| `Fascicle_02_Section_05_Scholarly.md` | FAIL | `DEFECT-M02-S05-001` | CRITICAL | Enumerative recap; no strict bilingual sequence. |
| `Fascicle_02_Section_06_Scholarly.md` | FAIL | `DEFECT-M02-S06-001` | CRITICAL | Practice summary substitutes for source-mapped translation. |
| `Fascicle_02_Closing_Summary_Scholarly.md` | FAIL | `DEFECT-M02-CLS-001` | WARNING | Acceptable as editorial summary artifact, but not a source-translation file. |

---

## Comparison Table (Representative)

| Source (T1912_002) | Current Translation | Required Correction |
|---|---|---|
| `次釋修大行中。初明來意者。發心無行無位可論。` | `## Introduction: What Does the Name Mean?` | Replace with strict ordered CN->EN lines preserving source sequence. |
| `故云修行入菩薩位說是修大行之止觀者。標也。` | `Miao-lo explains that Zhiyi analyzes...` | Remove summary narration; render sentence directly and literally. |
| `善解下舉譬也。酪須鑽成酥假搖熟。` | Thematic tables and modern explanatory sections | Insert omitted source lines in-order with one English line per Chinese line. |

---

## Corrections (Starter Block)

Note: Per audit protocol, omissions are auto-corrected in output. The block below is a **starter correction package** for the opening span and should be expanded across the full fascicle in compiler loops.

```text
[ADDED][CN] 次釋修大行中。
[ADDED][EN] Next, it explains the section on cultivating the great practice.

[ADDED][CN] 初明來意者。
[ADDED][EN] First, it clarifies the intent for this section.

[ADDED][CN] 發心無行無位可論。
[ADDED][EN] Without arousing the mind, there is no practice and no stage to discuss.

[ADDED][CN] 故云修行入菩薩位說是修大行之止觀者。標也。
[ADDED][EN] Therefore it says: "Cultivating practice and entering the bodhisattva stages"; this states the heading of the great-practice zhiguan.
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

1. `Fascicle_02_Section_01_Scholarly.md`
2. `Fascicle_02_Section_02_Scholarly.md`
3. `Fascicle_02_Section_03_Scholarly.md`
4. `Fascicle_02_Section_04_Scholarly.md`
5. `Fascicle_02_Section_05_Scholarly.md`
6. `Fascicle_02_Section_06_Scholarly.md`
7. `Fascicle_02_Closing_Summary_Scholarly.md` (keep as summary artifact or relabel explicitly as non-source translation)

---

## Audit Verdict

**Fascicle 2 Scholarly is not yet source-aligned under Road Manager Sacca criteria.**

Translation intent is strong, but fidelity format must be repaired from summary/exposition into strict CN->EN sequence mapping.
