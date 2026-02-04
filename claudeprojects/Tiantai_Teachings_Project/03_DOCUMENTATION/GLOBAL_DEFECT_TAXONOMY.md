# Wenju Scholarly Translation - Global Defect Taxonomy
## Systematic Classification for Repair Planning

**Date Created:** 2026-02-04
**Audit Scope:** Fascicles 1-8 (13 files audited)
**Purpose:** Classification of defects by type for systematic repair passes

---

## EXECUTIVE SUMMARY

**Total Files Audited:** 13 of 14
**Total Defects Found:** 12 (all CRITICAL)
**Defect Classes Detected:** 1 (Apparatus Omission only)
**Files Requiring Repair:** 12 (F2-F8)
**Files PASS:** 1 (F1 only)

---

## DEFECT CLASS TAXONOMY

### CLASS 1: APPARATUS OMISSION (CATASTROPHIC)

**Definition:** Complete absence of textual variant apparatus footnotes documenting differences between manuscript editions (Taishō 【大】, Jiaxing 【甲】, CBETA corrections 【CB】)

**Scope:** SYSTEMATIC - affects 92.3% of translated corpus

**Files Affected:** 12
- F2 FULL
- F3 Part 1
- F3 Part 2
- F4 FULL
- F4 Part 1
- F4 Part 2
- F5 FULL
- F6 Part 1
- F6 Part 2
- F7 Part 1
- F7 Part 2
- F8 Part 1

**Total Missing Entries:** 695

**Omission Rate:** 100% in all affected files (absolute systematic failure)

**Repair Estimate:** 26-30 hours

**Priority:** CRITICAL - BLOCKS PUBLICATION

**Repair Strategy:** Systematic Apparatus Restoration Pass (see below)

---

### CLASS 2: CONTENT OMISSIONS

**Defects Found:** 0
**Status:** ✅ PASS - All files show complete bilingual coverage

---

### CLASS 3: ADDITIONS (Unauthorized Content)

**Defects Found:** 0
**Status:** ✅ PASS - No extra-textual additions detected

---

### CLASS 4: PARAPHRASES (Summary Blocks)

**Defects Found:** 0
**Status:** ✅ PASS - All translations verbatim, no summarization

---

### CLASS 5: STRUCTURE ISSUES (問/答 Formatting)

**Defects Found:** 0
**Status:** ✅ PASS - All Question/Answer pairs properly preserved

---

### CLASS 6: FOOTNOTE ERRORS (Non-Apparatus)

**Defects Found:** 0
**Status:** ✅ PASS - Scholarly footnotes properly anchored and accurate

---

### CLASS 7: TERMINOLOGY DRIFT

**Defects Found:** 0
**Status:** ✅ PASS - All terms consistent with WENJU_SCHOLARLY_GLOSSARY.md

---

## APPARATUS OMISSION BREAKDOWN BY FASCICLE

| Fascicle | Files | Missing Entries | Repair Time | Priority Rank |
|----------|-------|----------------|-------------|---------------|
| F6 | Part 1, Part 2 | 161 (93+68) | 6.7 hours | 1 (HIGHEST) |
| F2 | FULL | 141 | 5.9 hours | 2 |
| F7 | Part 1, Part 2 | 94 (50+44) | 3.9 hours | 3 |
| F4 | FULL, Parts | 79 | 3.3 hours | 4 |
| F5 | FULL | 60 | 2.5 hours | 5 |
| F3 | Part 1, Part 2 | 52 (47+5) | 2.2 hours | 6 |
| F8 | Part 1 | 36 | 1.5 hours | 7 (LOWEST) |
| **TOTAL** | **12 files** | **695** | **26.0 hours** | — |

---

## SYSTEMATIC REPAIR PASSES REQUIRED

### PASS 1: APPARATUS RESTORATION (REQUIRED)

**Target:** Restore all 695 missing apparatus entries across F2-F8

**Method:**
1. Extract apparatus from CBETA sources (T1718_002-008.txt)
2. Map to translation file locations (Chinese text matching)
3. Generate footnote insertions with proper formatting
4. Insert inline markers [^N] and footnotes
5. Verify sequential numbering (avoid ID conflicts)

**Execution Order:** By impact (F6 → F2 → F7 → F4 → F5 → F3 → F8)

**Quality Gate:** Re-audit each file after repair until PASS status achieved

**Estimated Duration:** 26-30 hours

---

### PASS 2: VARIANT REINSERTION (NOT REQUIRED)

**Status:** ✅ NO DEFECTS DETECTED - Skip this pass

---

### PASS 3: Q/A FORMATTING CORRECTION (NOT REQUIRED)

**Status:** ✅ NO DEFECTS DETECTED - Skip this pass

---

### PASS 4: GLOSSARY NORMALIZATION (NOT REQUIRED)

**Status:** ✅ NO DEFECTS DETECTED - Skip this pass

---

### PASS 5: CONTENT OMISSION REPAIR (NOT REQUIRED)

**Status:** ✅ NO DEFECTS DETECTED - Skip this pass

---

## ROOT CAUSE ANALYSIS

**Hypothesis:** Workflow breakdown occurred between F1 completion and F2 start

**Evidence:**
- F1: Apparatus present (0% omission) ← **BASELINE ESTABLISHED**
- F2-F8: Apparatus absent (100% omission) ← **SYSTEMATIC FAILURE**

**Possible Causes:**
1. Apparatus extraction script disabled or removed from pipeline
2. Workflow change (manual → automated or vice versa)
3. Missing build step in translation process
4. Different translator/team unfamiliar with apparatus requirements
5. CBETA source files inaccessible during F2-F8 translation
6. Environmental change (different machine, missing dependencies)

**Investigation Required:**
- Review commit history F1 → F2
- Check translation protocol documentation
- Interview translators (if multiple contributors)
- Verify CBETA source availability timeline

---

## TRANSLATION QUALITY ASSESSMENT (NON-APPARATUS)

**All files (F1-F8) demonstrate EXCELLENT quality:**

✅ **Bilingual Coverage:** 100% (every Chinese phrase has English translation)
✅ **Structure Preservation:** Perfect (all 問/答 pairs formatted correctly)
✅ **Terminology Consistency:** Perfect (aligns with glossary)
✅ **Content Fidelity:** Perfect (no omissions, no paraphrases)
✅ **Scholarly Footnotes:** Excellent (non-apparatus footnotes properly anchored)
✅ **Technical Accuracy:** Excellent (Sanskrit diacriticals, proper names correct)

**Conclusion:** This is a **pipeline/tooling defect**, NOT a translation quality issue. The content work is exemplary; only the apparatus documentation step failed.

---

## REPAIR WORKFLOW REQUIREMENTS

### Pre-Repair Phase (4 hours)
1. Root cause analysis (2 hours)
2. Develop apparatus extraction script (2 hours)
3. Test on F3P2 sample (5 entries) as proof of concept (30 minutes)

### Repair Phase (26-30 hours)
4. Execute systematic apparatus restoration (F6 → F2 → F7 → F4 → F5 → F3 → F8)
5. Insert all 695 apparatus entries with proper formatting

### Post-Repair Phase (10 hours)
6. Re-audit all 12 files (8 hours)
7. Implement apparatus verification quality gate (2 hours)

**TOTAL PROJECT TIME: 40-44 hours**

---

## APPARATUS FOOTNOTE FORMAT SPECIFICATION

**Standard Format:**
```markdown
[^N]: *Critical apparatus: X【大】，Y【甲】 — [explanation]*
```

**Examples:**

**Type 1: Character Variant**
```markdown
[^7]: *Critical apparatus: 笑【大】＊，咲【甲】＊ — "Laugh/ridicule." Taishō uses standard form 笑; Jiaxing uses variant 咲. Both pronounced xiào.*
```

**Type 2: CBETA Correction**
```markdown
[^A1]: *Critical apparatus: 己【CB】，已【大】 — CBETA correction: 己 (jǐ, "self"); Taishō original: 已 (yǐ, "already").*
```

**Type 3: Jiaxing Omission**
```markdown
[^4]: *Critical apparatus: 為【大】，〔－〕【甲】 — "To be called/named as." Taishō: 稱為諦; Jiaxing omits 為.*
```

**Type 4: Edition Note**
```markdown
[^2]: *Critical apparatus: 不分卷【甲】 — Jiaxing edition note: "Not divided into fascicles" at this point.*
```

**Type 5: Lacuna Marker**
```markdown
[^2]: *Critical apparatus: 已下斷缺【甲】 — Jiaxing edition note: "Text breaks/is missing below this point."*
```

---

## SUCCESS CRITERIA

**File passes re-audit only if:**
1. ✅ Apparatus count in translation = Apparatus count in CBETA source (100% coverage)
2. ✅ All apparatus entries properly formatted with inline markers [^N]
3. ✅ All footnotes include scholarly explanation of variant
4. ✅ Footnote numbering sequential without conflicts
5. ✅ No orphan or duplicate apparatus IDs

**Project completion requires:**
- All 12 failed files reach PASS status
- Zero open defects in register
- Cross-file consistency check passes
- Footnote integrity check passes

---

## RISK ASSESSMENT

**LOW RISK:**
- Translation content quality excellent (easy foundation for repair)
- Only one defect class (focused repair effort)
- Clear repair methodology (apparatus extraction)
- Defect is additive (no content removal required)

**MEDIUM RISK:**
- Large scale (695 entries across 12 files)
- Time-intensive (26-30 hours repair time)
- Requires careful Chinese text matching

**MITIGATION:**
- Start with smallest file (F3P2 - 5 entries) as proof of concept
- Use semi-automated script for apparatus extraction
- Implement quality gate after each file repair
- Re-audit immediately after repair (catch errors early)

---

## PUBLICATION ROADMAP

**Phase 1: Immediate (Week 1)**
- F1: ✅ APPROVED FOR PUBLICATION (already PASS)

**Phase 2: After Repair (Week 2-3)**
- Repair F3P2 (proof of concept)
- Repair F6, F2, F7 (high-impact fascicles)
- Re-audit and approve for publication

**Phase 3: Final (Week 4)**
- Repair F4, F5, F3, F8 (remaining fascicles)
- Final cross-file consistency check
- Approve entire corpus for publication

---

## DEFECT TAXONOMY VERSION

**Version:** 1.0
**Date:** 2026-02-04
**Status:** COMPLETE
**Next Update:** After systematic repair pass (re-classification if new defects discovered)

---

**Classification Complete ✓**
**Ready for Systematic Repair Phase ✓**
