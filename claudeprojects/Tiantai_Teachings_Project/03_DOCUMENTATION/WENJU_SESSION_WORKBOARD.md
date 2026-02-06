# Wenju Session Workboard

Purpose: Keep each Wenju working session source-locked, auditable, and easy to resume.

Last updated: 2026-02-06 (Fascicle 1 restart initiated)

---

## Authority Order

1. `Tiantai_Teachings_Project/03_DOCUMENTATION/QA_Wenju_Scholarly_Defect_Register.md`
2. `Tiantai_Teachings_Project/03_DOCUMENTATION/GLOBAL_DEFECT_TAXONOMY.md`
3. `Tiantai_Teachings_Project/01_TRANSLATIONS/The_Words_and_Phrases/TRANSLATION_SESSION_LOG.md`

If any file conflicts with another, follow this authority order.

---

## Current Program Snapshot

- Workflow mode: Workflow V2 (Source-Locked Compiler Loop)
- Register status at checkpoint date: 18/18 files PASS, 0 open defects, 198 closed
- Archive checkpoint in force: ARCHIVE-WENJU-2026-02-06
- Restart policy: source-first only, no style-only pass before source lock

---

## Session Kickoff Checklist

- [x] Confirm target block (fascicle + exact source line range).
- [x] Record CBETA start and end anchors.
- [x] Verify contiguity (no overlap and no gap with prior block).
- [x] Confirm target translation file path.
- [x] Confirm this run is source lock (not tone pass).

---

## Active Block Card (Fill Each Session)

Session date: 2026-02-06

Operator: Codex + William

Block ID: F02-B19

Source file: `Tiantai_Teachings_Project/Tiantai_Great_Works/T1718_Fahua_Wenju/T1718_002.txt`

Source lines: 129-139 (須菩提 約教/本迹/觀心 doctrinal compression + apparatus [＊7-2]/[6]/[7]/[8])

CBETA start anchor: 約教者，自有滅色空智生，體色空智生，從有智生空智，從空智生俗智，從俗智生中智，空生即有智，是圓空智生，而今是圓空智生也。

CBETA end anchor: [8] 不【大】，心不【甲】

Target translation file: `Tiantai_Teachings_Project/01_TRANSLATIONS/The_Words_and_Phrases/Scholarly/Full_Translation/Wenju_Fascicle_02_FULL_Scholarly.md`

Goal for this pass: Validate 須菩提 約教/本迹/觀心 doctrinal sequence and apparatus [＊7-2]/[6]/[7]/[8] under Workflow V2 (Gates 1-4 complete for F02-B19; PASS).

---

## Workflow V2 Gate Tracker (Must Stay In Order)

### Gate 1 - Boundary Map First
- [x] Boundaries explicitly mapped with CBETA locators.
- [x] Contiguity checked and confirmed.
- [x] Structural map drafted before English output.

### Gate 2 - Source Lock
- [x] Literal scholarly base built/repaired from CBETA.
- [x] Q/A and apparatus structures preserved.
- [x] No tone rewrite mixed into this gate.

### Gate 3 - Audit And Log
- [x] Defects logged with locator + post-edit excerpt. (No defects found for F02-B19; 0 entries required.)
- [x] Defect state moved only by lifecycle rules. (No state transitions required for F02-B19.)

### Gate 4 - Re-Audit Against CBETA
- [x] One-to-one coverage verified.
- [x] Doctrinal fidelity verified.
- [x] PASS condition met (Open=0, Pending=0 in scope).

### Gate 5 - Tone Pass (Only After PASS)
- [ ] Allowed only after source-locked PASS.
- [ ] Meaning preserved and traceable to base text.
- [ ] Any tone edit remains re-checkable.

---

## Defect Lifecycle Rules

Allowed status flow:

Open -> Repaired/Pending -> Closed

Rules:

- Do not skip state transitions.
- Do not mark Closed without re-audit evidence.
- Every defect entry needs source locator and post-edit excerpt.

---

## Session Output Log

Use one line per completed action.

- [x] Boundaries mapped: F01-B01 = T1718_001.txt lines 10-24 (preface unit), anchors locked.
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B01.
- [x] Defects added/updated: No defects detected for F01-B01 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Focused CBETA-to-translation check complete for F01-B01.
- [x] PASS/FAIL result: PASS (F01-B01).
- [x] Boundaries mapped: F01-B02 = T1718_001.txt lines 26-39 (title/attribution/opening heading + apparatus).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B02.
- [x] Defects added/updated: No defects detected for F01-B02 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Focused CBETA-to-translation check complete for F01-B02.
- [x] PASS/FAIL result: PASS (F01-B02).
- [x] Boundaries mapped: F01-B03 = T1718_001.txt lines 41-44 (opening analysis paragraph + apparatus [8]/[9]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B03.
- [x] Defects added/updated: No defects detected for F01-B03 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Focused CBETA-to-translation check complete for F01-B03.
- [x] PASS/FAIL result: PASS (F01-B03).
- [x] Boundaries mapped: F01-B04 = T1718_001.txt lines 46-48 (classification paragraph + apparatus [10]).
- [x] Source lock edits completed: Inserted missing apparatus note `各【大】，各憑【甲】` in scholarly file.
- [x] Defects added/updated: 1 omission defect repaired (apparatus [10] was missing before edit).
- [x] Re-audit completed: CBETA line 46 paragraph + line 48 apparatus both verified present after repair.
- [x] PASS/FAIL result: PASS (F01-B04).
- [x] Boundaries mapped: F01-B05 = T1718_001.txt lines 50-52 (commentator taxonomy paragraph + apparatus [11]).
- [x] Source lock edits completed: Inserted missing apparatus note `記【大】，記品【甲】` in scholarly file.
- [x] Defects added/updated: 1 omission defect repaired (apparatus [11] was missing before edit).
- [x] Re-audit completed: CBETA line 50 paragraph + line 52 apparatus both verified present after repair.
- [x] PASS/FAIL result: PASS (F01-B05).
- [x] Boundaries mapped: F01-B06 = T1718_001.txt line 54 (doctrinal warning + siddhānta contrast).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B06.
- [x] Defects added/updated: No defects detected for F01-B06 (0 open, 0 pending in block scope).
- [x] Re-audit completed: CBETA line 54 verified one-to-one with full doctrinal framing preserved.
- [x] PASS/FAIL result: PASS (F01-B06).
- [x] Boundaries mapped: F01-B07 = T1718_001.txt line 56 (threefold/twofold structural map + internal gate partitions).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B07.
- [x] Defects added/updated: No defects detected for F01-B07 (0 open, 0 pending in block scope).
- [x] Re-audit completed: All segmentation clauses, counts, and pivot phrase mapping verified.
- [x] PASS/FAIL result: PASS (F01-B07).
- [x] Boundaries mapped: F01-B08 = T1718_001.txt lines 58-66 (question/answer sequence + apparatus [1]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B08.
- [x] Defects added/updated: No defects detected for F01-B08 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Q/A turn structure and variant note mapping fully verified.
- [x] PASS/FAIL result: PASS (F01-B08).
- [x] Boundaries mapped: F01-B09 = T1718_001.txt lines 68-73 (method architecture + apparatus [2]/[3]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B09.
- [x] Defects added/updated: No defects detected for F01-B09 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Four-method framework and both variant markers verified.
- [x] PASS/FAIL result: PASS (F01-B09).
- [x] Boundaries mapped: F01-B10 = T1718_001.txt lines 75-86 (rationale Q/A expansion + apparatus [4]/[5]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B10.
- [x] Defects added/updated: No defects detected for F01-B10 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Middle-path argument flow and both variant markers verified.
- [x] PASS/FAIL result: PASS (F01-B10).
- [x] Boundaries mapped: F01-B11 = T1718_001.txt lines 88-91 (evidence chain + apparatus [6]/[7]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B11.
- [x] Defects added/updated: No defects detected for F01-B11 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Citation chain, doctrinal quotations, and both variant markers verified.
- [x] PASS/FAIL result: PASS (F01-B11).
- [x] Boundaries mapped: F01-B12 = T1718_001.txt lines 93-95 (示相 opening + apparatus [8]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B12.
- [x] Defects added/updated: No defects detected for F01-B12 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Causal-temporal framing and apparatus [8] mapping verified.
- [x] PASS/FAIL result: PASS (F01-B12).
- [x] Boundaries mapped: F01-B13 = T1718_001.txt lines 97-100 (first temporal schema + apparatus [9]/[10]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B13.
- [x] Defects added/updated: No defects detected for F01-B13 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Temporal schema clause sequence and both variant markers verified.
- [x] PASS/FAIL result: PASS (F01-B13).
- [x] Boundaries mapped: F01-B14 = T1718_001.txt lines 102-105 (expanded temporal schema + apparatus [11]/[12]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B14.
- [x] Defects added/updated: No defects detected for F01-B14 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Schema transitions and both variant markers verified.
- [x] PASS/FAIL result: PASS (F01-B14).
- [x] Boundaries mapped: F01-B15 = T1718_001.txt lines 107-109 (teaching-classification chain + apparatus [13]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B15.
- [x] Defects added/updated: No defects detected for F01-B15 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Classification contrasts and apparatus [13] mapping verified.
- [x] PASS/FAIL result: PASS (F01-B15).
- [x] Boundaries mapped: F01-B16 = T1718_001.txt line 111 (本迹 schema and root-analogy closure).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B16.
- [x] Defects added/updated: No defects detected for F01-B16 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Upper/middle/lower and fundamental/trace sequence verified end-to-end.
- [x] PASS/FAIL result: PASS (F01-B16).
- [x] Boundaries mapped: F01-B17 = T1718_001.txt line 113 (觀心 tripartite mapping for 戒/定/慧).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B17.
- [x] Defects added/updated: No defects detected for F01-B17 (0 open, 0 pending in block scope).
- [x] Re-audit completed: All戒定慧 mapping clauses and order verified.
- [x] PASS/FAIL result: PASS (F01-B17).
- [x] Boundaries mapped: F01-B18 = T1718_001.txt lines 115-116 (four-intent closure + proverb pair).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B18.
- [x] Defects added/updated: No defects detected for F01-B18 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Closure instructions and proverb pair retained without compression.
- [x] PASS/FAIL result: PASS (F01-B18).
- [x] Boundaries mapped: F01-B19 = T1718_001.txt line 117 (通序/別序 architecture declaration).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B19.
- [x] Defects added/updated: No defects detected for F01-B19 (0 open, 0 pending in block scope).
- [x] Re-audit completed: 通序/別序 boundaries and scope clauses verified one-to-one.
- [x] PASS/FAIL result: PASS (F01-B19).
- [x] Boundaries mapped: F01-B20 = T1718_001.txt lines 119-126 (因緣釋 expansion for 「如是」 + apparatus [1]-[3]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B20.
- [x] Defects added/updated: No defects detected for F01-B20 (0 open, 0 pending in block scope).
- [x] Re-audit completed: All causal clauses and apparatus [1]-[3] verified present in translation.
- [x] PASS/FAIL result: PASS (F01-B20).
- [x] Boundaries mapped: F01-B21 = T1718_001.txt lines 128-130 (約教釋 pivot + apparatus [4]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B21.
- [x] Defects added/updated: No defects detected for F01-B21 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Doctrinal pivot logic and apparatus [4] mapping verified.
- [x] PASS/FAIL result: PASS (F01-B21).
- [x] Boundaries mapped: F01-B22 = T1718_001.txt lines 132-135 (漸教分別 exposition + apparatus [5]-[6]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B22.
- [x] Defects added/updated: No defects detected for F01-B22 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Four-teaching progression and apparatus [5]-[6] verified.
- [x] PASS/FAIL result: PASS (F01-B22).
- [x] Boundaries mapped: F01-B23 = T1718_001.txt lines 137-145 (本迹 + 觀心 synthesis for 「如是」 + apparatus [7]-[10]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B23.
- [x] Defects added/updated: No defects detected for F01-B23 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Trace/fundamental mapping, contemplative sequence, and apparatus [7]-[10] verified.
- [x] PASS/FAIL result: PASS (F01-B23).
- [x] Boundaries mapped: F01-B24 = T1718_001.txt lines 146-158 (「我聞」 opening + Q/A + apparatus [1]-[3]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B24.
- [x] Defects added/updated: No defects detected for F01-B24 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Q/A flow, three-doubt dispelling sequence, and apparatus [1]-[3] verified.
- [x] PASS/FAIL result: PASS (F01-B24).
- [x] Boundaries mapped: F01-B25 = T1718_001.txt lines 160-164 (約教解釋 「我」 + apparatus [4]-[6]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B25.
- [x] Defects added/updated: No defects detected for F01-B25 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Four-teaching classification for 「我」 and apparatus [4]-[6] verified.
- [x] PASS/FAIL result: PASS (F01-B25).
- [x] Boundaries mapped: F01-B26 = T1718_001.txt lines 166-168 (本迹釋 「我聞」 + apparatus [7]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B26.
- [x] Defects added/updated: No defects detected for F01-B26 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Empty-King-Buddha origin reference and apparatus [7] verified.
- [x] PASS/FAIL result: PASS (F01-B26).
- [x] Boundaries mapped: F01-B27 = T1718_001.txt line 170 (觀心釋 closure for 「我聞」).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B27.
- [x] Defects added/updated: No defects detected for F01-B27 (0 open, 0 pending in block scope).
- [x] Re-audit completed: 即空/即假/即中 triad for 「我」 verified one-to-one.
- [x] PASS/FAIL result: PASS (F01-B27).
- [x] Boundaries mapped: F01-B28 = T1718_001.txt line 172 (釋「聞」因緣解 long-form).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B28.
- [x] Defects added/updated: No defects detected for F01-B28 (0 open, 0 pending in block scope).
- [x] Re-audit completed: All citation chain clauses for hearing-transmission preserved without omission.
- [x] PASS/FAIL result: PASS (F01-B28).
- [x] Boundaries mapped: F01-B29 = T1718_001.txt line 174 (約教釋「聞」 with four Ananda schema).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B29.
- [x] Defects added/updated: No defects detected for F01-B29 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Fourfold hearing typology and doctrinal role mapping verified.
- [x] PASS/FAIL result: PASS (F01-B29).
- [x] Boundaries mapped: F01-B30 = T1718_001.txt lines 176-178 (本迹 + 觀心 closure for 「聞」).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B30.
- [x] Defects added/updated: No defects detected for F01-B30 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Four-hearing contemplative sequence retained and complete.
- [x] PASS/FAIL result: PASS (F01-B30).
- [x] Boundaries mapped: F01-B31 = T1718_001.txt lines 180-182 (「一時」 opening + apparatus [8]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B31.
- [x] Defects added/updated: No defects detected for F01-B31 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Kāla/Samaya interpretive triad and apparatus [8] verified.
- [x] PASS/FAIL result: PASS (F01-B31).
- [x] Boundaries mapped: F01-B32 = T1718_001.txt line 184 (本迹釋 for 「一時」).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B32.
- [x] Defects added/updated: No defects detected for F01-B32 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Trace/Origin temporal contrast preserved one-to-one.
- [x] PASS/FAIL result: PASS (F01-B32).
- [x] Boundaries mapped: F01-B33 = T1718_001.txt line 186 (觀心釋 completion for 「一時」).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B33.
- [x] Defects added/updated: No defects detected for F01-B33 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Sequential and round contemplation forms both verified.
- [x] PASS/FAIL result: PASS (F01-B33).
- [x] Boundaries mapped: F01-B34 = T1718_001.txt lines 188-191 (「佛」因緣釋 matrix + apparatus [9]-[10]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B34.
- [x] Defects added/updated: No defects detected for F01-B34 (0 open, 0 pending in block scope).
- [x] Re-audit completed: All continent/kalpa contrasts, siddhānta pivots, and apparatus [9]-[10] verified.
- [x] PASS/FAIL result: PASS (F01-B34).
- [x] Boundaries mapped: F01-B35 = T1718_001.txt line 193 (約教分別 for 「佛」 with four-Buddha schema).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B35.
- [x] Defects added/updated: No defects detected for F01-B35 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Four-teaching Buddha-form sequence and citation chain verified one-to-one.
- [x] PASS/FAIL result: PASS (F01-B35).
- [x] Boundaries mapped: F01-B36 = T1718_001.txt line 195 (本迹釋 transition for 「佛」).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B36.
- [x] Defects added/updated: No defects detected for F01-B36 (0 open, 0 pending in block scope).
- [x] Re-audit completed: One-Buddha/three-Buddha contrast and trace/origin mapping verified.
- [x] PASS/FAIL result: PASS (F01-B36).
- [x] Boundaries mapped: F01-B37 = T1718_001.txt line 197 (觀心釋 completion for 「佛」).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B37.
- [x] Defects added/updated: No defects detected for F01-B37 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Partial/perfect awakening contemplative sequence verified.
- [x] PASS/FAIL result: PASS (F01-B37).
- [x] Boundaries mapped: F01-B38 = T1718_001.txt lines 199-201 (「住」因緣釋 + apparatus [1]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B38.
- [x] Defects added/updated: No defects detected for F01-B38 (0 open, 0 pending in block scope).
- [x] Re-audit completed: 能住/所住 grammar chain and apparatus [1] verified one-to-one.
- [x] PASS/FAIL result: PASS (F01-B38).
- [x] Boundaries mapped: F01-B39 = T1718_001.txt line 203 (約教釋 for 「住」 four-Buddha dwelling schema).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B39.
- [x] Defects added/updated: No defects detected for F01-B39 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Four-teaching dwelling structure and subtle/coarse contrast verified.
- [x] PASS/FAIL result: PASS (F01-B39).
- [x] Boundaries mapped: F01-B40 = T1718_001.txt lines 205-207 (本迹解 for 「住」 + apparatus [2]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B40.
- [x] Defects added/updated: No defects detected for F01-B40 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Compassion-response mapping and apparatus [2] verified.
- [x] PASS/FAIL result: PASS (F01-B40).
- [x] Boundaries mapped: F01-B41 = T1718_001.txt lines 209-211 (觀解 closure for 「住」 + apparatus [3]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B41.
- [x] Defects added/updated: No defects detected for F01-B41 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Dwelling-through-non-dwelling syntax and apparatus [3] verified.
- [x] PASS/FAIL result: PASS (F01-B41).
- [x] Boundaries mapped: F01-B42 = T1718_001.txt lines 213-218 (王舍城因緣 narrative + apparatus [4]-[7]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B42.
- [x] Defects added/updated: No defects detected for F01-B42 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Narrative sequence and all apparatus [4]-[7] verified.
- [x] PASS/FAIL result: PASS (F01-B42).
- [x] Boundaries mapped: F01-B43 = T1718_001.txt line 220 (約教釋 city-analogy bridge).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B43.
- [x] Defects added/updated: No defects detected for F01-B43 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Four-seeing structure and 住所/能住 linkage verified.
- [x] PASS/FAIL result: PASS (F01-B43).
- [x] Boundaries mapped: F01-B44 = T1718_001.txt lines 222-233 (靈鷲 etymology + five-vihāra list + apparatus [8]-[16]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B44.
- [x] Defects added/updated: No defects detected for F01-B44 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Place-name chain and apparatus clusters [8]-[16] verified.
- [x] PASS/FAIL result: PASS (F01-B44).
- [x] Boundaries mapped: F01-B45 = T1718_001.txt lines 235-250 (劫火 Q/A + 觀釋 city-model + apparatus [17]-[19]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B45.
- [x] Defects added/updated: No defects detected for F01-B45 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Q/A logic, doctrinal transition, and apparatus [17]-[19] verified.
- [x] PASS/FAIL result: PASS (F01-B45).
- [x] Boundaries mapped: F01-B46 = T1718_001.txt lines 252-265 (觀心山 + 同聞眾三分 + 本迹/觀心 closure).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B46.
- [x] Defects added/updated: No defects detected for F01-B46 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Structural triads and apparatus [*13-1]/[1]/[2] all verified.
- [x] PASS/FAIL result: PASS (F01-B46).
- [x] Boundaries mapped: F01-B47 = T1718_001.txt lines 267-287 (聲聞分類 + 七一 + 大多勝 schema).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B47.
- [x] Defects added/updated: No defects detected for F01-B47 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Classification sequence and apparatus [3]/[4]/[5]/[*13-2]/[6] verified.
- [x] PASS/FAIL result: PASS (F01-B47).
- [x] Boundaries mapped: F01-B48 = T1718_001.txt lines 289-303 (比丘 tri-meaning + 本迹/觀心 + apparatus [7]-[11], [1]-[2]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B48.
- [x] Defects added/updated: No defects detected for F01-B48 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Full tri-meaning chain and all attached apparatus markers verified.
- [x] PASS/FAIL result: PASS (F01-B48).
- [x] Boundaries mapped: F01-B49 = T1718_001.txt lines 305-311 (僧伽 definition + 本迹/觀解 + apparatus [3]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B49.
- [x] Defects added/updated: No defects detected for F01-B49 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Four-sangha ladder and apparatus [3] verified.
- [x] PASS/FAIL result: PASS (F01-B49).
- [x] Boundaries mapped: F01-B50 = T1718_001.txt lines 313-323 (明數/明位 + 本迹/觀心 + apparatus [4]-[5]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B50.
- [x] Defects added/updated: No defects detected for F01-B50 (0 open, 0 pending in block scope).
- [x] Re-audit completed: 12,000 framework, arhat triad, and apparatus [4]-[5] verified.
- [x] PASS/FAIL result: PASS (F01-B50).
- [x] Boundaries mapped: F01-B51 = T1718_001.txt lines 325-343 (歎德 five-sentence analysis + 本迹/觀心 + apparatus [6]-[7], [1]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B51.
- [x] Defects added/updated: No defects detected for F01-B51 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Praise-logic chain and all referenced apparatus markers verified.
- [x] PASS/FAIL result: PASS (F01-B51).
- [x] Boundaries mapped: F01-B52 = T1718_001.txt lines 345-353 (列名 opening + 阿若因緣 narrative + apparatus [2]-[6]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B52.
- [x] Defects added/updated: No defects detected for F01-B52 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Narrative continuity and apparatus [2]-[6] verified.
- [x] PASS/FAIL result: PASS (F01-B52).
- [x] Boundaries mapped: F01-B53 = T1718_001.txt lines 355-403 (三藏/通/別/圓無生觀 + 本迹/觀心 + apparatus chains).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B53.
- [x] Defects added/updated: No defects detected for F01-B53 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Multi-layer no-birth argument and all in-range apparatus markers verified.
- [x] PASS/FAIL result: PASS (F01-B53).
- [x] Boundaries mapped: F01-B54 = T1718_001.txt lines 405-420 (摩訶迦葉 profile + 行大/位大 opening + apparatus [13]/[1]-[7]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B54.
- [x] Defects added/updated: No defects detected for F01-B54 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Kāśyapa profile sequence and apparatus chain [13]/[1]-[7] verified.
- [x] PASS/FAIL result: PASS (F01-B54).
- [x] Boundaries mapped: F01-B55 = T1718_001.txt lines 422-427 (post-cremation transmission chain + apparatus [8]-[9]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B55.
- [x] Defects added/updated: No defects detected for F01-B55 (0 open, 0 pending in block scope).
- [x] Re-audit completed: 三藏/四阿含 attribution sequence and apparatus [8]-[9] verified.
- [x] PASS/FAIL result: PASS (F01-B55).
- [x] Boundaries mapped: F01-B56 = T1718_001.txt lines 429-450 (迦葉天上段 + 頭陀四教/本迹/觀心 + apparatus [1]-[4]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B56.
- [x] Defects added/updated: No defects detected for F01-B56 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Dhūta progression and in-range apparatus markers verified.
- [x] PASS/FAIL result: PASS (F01-B56).
- [x] Boundaries mapped: F01-B57 = T1718_001.txt lines 452-463 (三迦葉 narrative + 約教/本迹/觀心 + apparatus [5]-[8]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B57.
- [x] Defects added/updated: No defects detected for F01-B57 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Miracle sequence and apparatus [5]-[8] verified.
- [x] PASS/FAIL result: PASS (F01-B57).
- [x] Boundaries mapped: F01-B58 = T1718_001.txt lines 465-493 (舍利弗 etymology + lineage narratives + apparatus clusters).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B58.
- [x] Defects added/updated: No defects detected for F01-B58 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Full name-lineage narrative and all in-range apparatus markers verified.
- [x] PASS/FAIL result: PASS (F01-B58).
- [x] Boundaries mapped: F01-B59 = T1718_001.txt lines 495-510 (中阿含 citations + 約教/本迹/觀心 for 舍利弗 + apparatus [A2]/[1]-[5]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B59.
- [x] Defects added/updated: No defects detected for F01-B59 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Citation dialogue structure and apparatus set [A2]/[1]-[5] verified.
- [x] PASS/FAIL result: PASS (F01-B59).
- [x] Boundaries mapped: F01-B60 = T1718_001.txt lines 514-520 (大目揵連 opening profile + apparatus [6]-[10]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B60.
- [x] Defects added/updated: No defects detected for F01-B60 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Opening profile chain and apparatus [6]-[10] verified.
- [x] PASS/FAIL result: PASS (F01-B60).
- [x] Boundaries mapped: F01-B61 = T1718_001.txt lines 522-526 (難陀/跋難陀 dragon-subdual cycle + 雜阿含 Vinaya episode + 耆域 opening narrative).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B61.
- [x] Defects added/updated: No defects detected for F01-B61 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Miracle-event ordering, dialogue continuity, and in-line marker [1] continuity to the next apparatus witness verified.
- [x] PASS/FAIL result: PASS (F01-B61).
- [x] Boundaries mapped: F01-B62 = T1718_001.txt lines 528-539 (車乃得 apparatus + 梵聲 far-hearing episode + 約教/本迹/觀心 + apparatus [2]-[3]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B62.
- [x] Defects added/updated: No defects detected for F01-B62 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Apparatus chain [1]-[3], voice-hearing narrative, and doctrinal triad mapping verified.
- [x] PASS/FAIL result: PASS (F01-B62).
- [x] Boundaries mapped: F01-B63 = T1718_001.txt lines 541-557 (摩訶迦栴延 profile + 十番問答 + 律中案例 + 約教/本迹/觀心 + apparatus [4]-[8]/[1]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B63.
- [x] Defects added/updated: No defects detected for F01-B63 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Debate-cycle sequencing, apparatus witnesses [4]-[8]/[1], and doctrinal closure lines verified.
- [x] PASS/FAIL result: PASS (F01-B63).
- [x] Boundaries mapped: F01-B64 = T1718_001.txt lines 559-580 (阿㝹樓馱 identity + surname/cosmogony-genealogy + 賢愚 narrative + 教判/本迹 + apparatus [2]-[7]/[4]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B64.
- [x] Defects added/updated: No defects detected for F01-B64 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Name/genealogy sequence, number fidelity, apparatus witnesses [2]-[7]/[4], and 天眼 teaching chain verified.
- [x] PASS/FAIL result: PASS (F01-B64).
- [x] Boundaries mapped: F01-B65 = T1718_001.txt lines 582-589 (阿那律觀心 closure + 劫賓那 profile + apparatus [1]-[4]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B65.
- [x] Defects added/updated: No defects detected for F01-B65 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Transition boundary at line 582, 劫賓那 narrative flow, and apparatus witnesses [1]-[4] verified.
- [x] PASS/FAIL result: PASS (F01-B65).
- [x] Boundaries mapped: F01-B66 = T1718_001.txt lines 591-597 (約教/本迹/觀心 doctrine + apparatus [5]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F01-B66.
- [x] Defects added/updated: No defects detected for F01-B66 (0 open, 0 pending in block scope).
- [x] Re-audit completed: 四教房舍 imagery sequence, 本迹/觀心 closure, and apparatus [5] verified.
- [x] PASS/FAIL result: PASS (F01-B66).
- [x] Boundaries mapped: F01-B67 = T1718_001.txt line 599 (fascicle-close colophon line).
- [x] Source lock edits completed: No textual edits required; fascicle close line is source-locked for F01-B67.
- [x] Defects added/updated: No defects detected for F01-B67 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Closing colophon line verified against source.
- [x] PASS/FAIL result: PASS (F01-B67).
- [x] Boundaries mapped: F02-B01 = T1718_002.txt lines 9-23 (fascicle-2 header/attribution + 憍梵波提 opening profile + apparatus chain).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B01.
- [x] Defects added/updated: No defects detected for F02-B01 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Header/attribution continuity and apparatus witnesses [6]-[11]/[＊7-1]/[＊7-2]/[＊10-1] verified.
- [x] PASS/FAIL result: PASS (F02-B01).
- [x] Boundaries mapped: F02-B02 = T1718_002.txt lines 25-29 (憍梵波提 約教/本迹/觀心 doctrinal triad).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B02.
- [x] Defects added/updated: No defects detected for F02-B02 (0 open, 0 pending in block scope).
- [x] Re-audit completed: 四悉檀/本迹/觀心 category mapping and doctrinal continuity verified.
- [x] PASS/FAIL result: PASS (F02-B02).
- [x] Boundaries mapped: F02-B03 = T1718_002.txt lines 31-35 (離婆多 identity variants + haunted-body narrative chain + apparatus [12]/[A1]/[13]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B03.
- [x] Defects added/updated: No defects detected for F02-B03 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Identity etymology chain, argument flow, and apparatus witnesses [12]/[A1]/[13] verified.
- [x] PASS/FAIL result: PASS (F02-B03).
- [x] Boundaries mapped: F02-B04 = T1718_002.txt lines 37-41 (離婆多 約教/本迹/觀心 doctrinal triad).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B04.
- [x] Defects added/updated: No defects detected for F02-B04 (0 open, 0 pending in block scope).
- [x] Re-audit completed: 約教/本迹/觀心 doctrinal segmentation and lexical polarity verified.
- [x] PASS/FAIL result: PASS (F02-B04).
- [x] Boundaries mapped: F02-B05 = T1718_002.txt lines 43-45 (畢陵伽婆蹉 opening profile + quoted speech + apparatus [＊7-3]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B05.
- [x] Defects added/updated: No defects detected for F02-B05 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Name-gloss, quoted rebuke/apology sequence, and apparatus witness [＊7-3] verified.
- [x] PASS/FAIL result: PASS (F02-B05).
- [x] Boundaries mapped: F02-B06 = T1718_002.txt lines 47-51 (畢陵伽婆蹉 約教/本迹/觀心 doctrinal triad).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B06.
- [x] Defects added/updated: No defects detected for F02-B06 (0 open, 0 pending in block scope).
- [x] Re-audit completed: 四教 progression and 本迹/觀心 doctrinal closure verified.
- [x] PASS/FAIL result: PASS (F02-B06).
- [x] Boundaries mapped: F02-B07 = T1718_002.txt lines 53-58 (薄拘羅 long profile + karmic-causality chain + apparatus [1]-[4]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B07.
- [x] Defects added/updated: No defects detected for F02-B07 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Profile event order, longevity/karmic-causality chain, and apparatus witnesses [1]-[4] verified.
- [x] PASS/FAIL result: PASS (F02-B07).
- [x] Boundaries mapped: F02-B08 = T1718_002.txt lines 60-62 (薄拘羅 約教 triad + apparatus [5a]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B08.
- [x] Defects added/updated: No defects detected for F02-B08 (0 open, 0 pending in block scope).
- [x] Re-audit completed: 四教寂靜 progression and [5a] witness variant line verified.
- [x] PASS/FAIL result: PASS (F02-B08).
- [x] Boundaries mapped: F02-B09 = T1718_002.txt lines 64-66 ([5b] 本迹 clause + apparatus witness).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B09.
- [x] Defects added/updated: No defects detected for F02-B09 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Four-virtue mapping (常樂我淨) and [5b] witness note alignment verified.
- [x] PASS/FAIL result: PASS (F02-B09).
- [x] Boundaries mapped: F02-B10 = T1718_002.txt lines 68-73 (薄拘羅 觀心 close + 摩訶拘絺羅 opening debate narrative + apparatus [＊7-4]/[6]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B10.
- [x] Defects added/updated: No defects detected for F02-B10 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Debate logic chain, dilemma framing, and apparatus witnesses [＊7-4]/[6] verified.
- [x] PASS/FAIL result: PASS (F02-B10).
- [x] Boundaries mapped: F02-B11 = T1718_002.txt lines 75-82 (摩訶拘絺羅 約教/本迹/觀心 triad + apparatus [7]/[8]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B11.
- [x] Defects added/updated: No defects detected for F02-B11 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Four-level 辯 mapping, 本迹 clause, 觀心 closure, and apparatus [7]/[8] verified.
- [x] PASS/FAIL result: PASS (F02-B11).
- [x] Boundaries mapped: F02-B12 = T1718_002.txt lines 84-87 (難陀 opening profile + lexical variants + apparatus [9]/[10]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B12.
- [x] Defects added/updated: No defects detected for F02-B12 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Name equivalence chain and apparatus witnesses [9]/[10] verified.
- [x] PASS/FAIL result: PASS (F02-B12).
- [x] Boundaries mapped: F02-B13 = T1718_002.txt lines 89-95 (難陀 約教/本迹/觀心 triad + [＊7-1] witness).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B13.
- [x] Defects added/updated: No defects detected for F02-B13 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Joy polarity mapping, 本迹 clause, 觀心 closure, and [＊7-1] witness verified.
- [x] PASS/FAIL result: PASS (F02-B13).
- [x] Boundaries mapped: F02-B14 = T1718_002.txt lines 97-102 (孫陀羅難陀 extended narrative + apparatus [11]/[＊9-1]/[12]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B14.
- [x] Defects added/updated: No defects detected for F02-B14 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Narrative event order and apparatus witnesses [11]/[＊9-1]/[12] verified.
- [x] PASS/FAIL result: PASS (F02-B14).
- [x] Boundaries mapped: F02-B15 = T1718_002.txt lines 103-107 (孫陀羅難陀 約教 summary + 本迹觀心如前 + apparatus [13]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B15.
- [x] Defects added/updated: No defects detected for F02-B15 (0 open, 0 pending in block scope).
- [x] Re-audit completed: 約教法喜 mapping and [13] witness note verified.
- [x] PASS/FAIL result: PASS (F02-B15).
- [x] Boundaries mapped: F02-B16 = T1718_002.txt lines 109-113 (富樓那 opening mega-narrative + apparatus [14]/[15]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B16.
- [x] Defects added/updated: No defects detected for F02-B16 (0 open, 0 pending in block scope).
- [x] Re-audit completed: Naming-causality chain and apparatus witnesses [14]/[15] verified.
- [x] PASS/FAIL result: PASS (F02-B16).
- [x] Boundaries mapped: F02-B17 = T1718_002.txt lines 114-120 (富樓那 約教/本迹/觀心 triad + apparatus [1]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B17.
- [x] Defects added/updated: No defects detected for F02-B17 (0 open, 0 pending in block scope).
- [x] PASS/FAIL result: PASS (F02-B17).
- [x] Boundaries mapped: F02-B18 = T1718_002.txt lines 122-127 (須菩提 opening空生 narrative + apparatus [2]-[5]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B18.
- [x] Defects added/updated: No defects detected for F02-B18 (0 open, 0 pending in block scope).
- [x] Re-audit completed: 空生 narrative chain and apparatus witnesses [2]-[5] verified.
- [x] PASS/FAIL result: PASS (F02-B18).
- [x] Boundaries mapped: F02-B19 = T1718_002.txt lines 129-139 (須菩提 約教/本迹/觀心 doctrinal compression + apparatus [＊7-2]/[6]/[7]/[8]).
- [x] Source lock edits completed: No textual edits required; existing scholarly block is source-locked for F02-B19.
- [x] Defects added/updated: No defects detected for F02-B19 (0 open, 0 pending in block scope).
- [x] Re-audit completed: 約教 causal-wisdom ladder, 本迹 marker witness chain, and 觀心法身 closure with [8] variant verified.
- [x] PASS/FAIL result: PASS (F02-B19).

---

## Handoff Block (End Of Session)

Next recommended block: F02-B20

Next exact source range: T1718_002.txt lines 141-145

Carry-over risks: Next block opens 阿難 mega-narrative chain with rapid causality pivots (royal grief, Mara deception, heavenly correction, birth naming) and apparatus [9]/[10]/[11]; preserve event order and witness binding.

Open defects remaining: 0 (for F01-B01 through F01-B67 + F02-B01/F02-B02/F02-B03/F02-B04/F02-B05/F02-B06/F02-B07/F02-B08/F02-B09/F02-B10/F02-B11/F02-B12/F02-B13/F02-B14/F02-B15/F02-B16/F02-B17/F02-B18/F02-B19 scopes)

Pending re-audit items: None for F01-B01/F01-B02/F01-B03/F01-B04/F01-B05/F01-B06/F01-B07/F01-B08/F01-B09/F01-B10/F01-B11/F01-B12/F01-B13/F01-B14/F01-B15/F01-B16/F01-B17/F01-B18/F01-B19/F01-B20/F01-B21/F01-B22/F01-B23/F01-B24/F01-B25/F01-B26/F01-B27/F01-B28/F01-B29/F01-B30/F01-B31/F01-B32/F01-B33/F01-B34/F01-B35/F01-B36/F01-B37/F01-B38/F01-B39/F01-B40/F01-B41/F01-B42/F01-B43/F01-B44/F01-B45/F01-B46/F01-B47/F01-B48/F01-B49/F01-B50/F01-B51/F01-B52/F01-B53/F01-B54/F01-B55/F01-B56/F01-B57/F01-B58/F01-B59/F01-B60/F01-B61/F01-B62/F01-B63/F01-B64/F01-B65/F01-B66/F01-B67/F02-B01/F02-B02/F02-B03/F02-B04/F02-B05/F02-B06/F02-B07/F02-B08/F02-B09/F02-B10/F02-B11/F02-B12/F02-B13/F02-B14/F02-B15/F02-B16/F02-B17/F02-B18/F02-B19

Notes for next operator: Start F02-B20 at line 141 and carry through line 145 with apparatus [9]/[10]/[11], preserving narrative causality chain before moving to line 147 約教.

---

## Quick Start For Next Session

1. Open the Defect Register first.
2. Copy this template section and fill the Active Block Card.
3. Run gates in order; do not skip.
4. End by writing the Handoff Block.
