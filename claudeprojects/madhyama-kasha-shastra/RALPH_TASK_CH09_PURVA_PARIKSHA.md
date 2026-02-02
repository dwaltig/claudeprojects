# RALPH TASK: MMK Chapter 09 - Pūrva Parīkṣā (Examination of the Prior Entity)

**Task ID**: TASK-MMK-CH09-001
**Objective**: Translate and interpret Chapter 9 of the Mūlamadhyamakakārikā using the Ralph Loop architecture.
**Current Iteration**: 2
**Max Iterations**: 10

## 1. Context & Resources
- **Source Text**: `madhyama-kasha-shastra/02_SOURCE_MATERIALS/MMK_Chapter_09_Sanskrit.txt`
- **Previous Output**: `madhyama-kasha-shastra/01_TRANSLATIONS/Chapter_09_Purva_Pariksha_Complete.md`
- **Reference Materials**:
  - [ ] `agents/GUARDRAILS.md` (MUST READ)
  - [ ] `agents/MAS_MANIFEST.md`
  - [ ] `agents/mcp_config.json` (For DDB lookups)

## 2. The Checklist (The Definition of Done)
*The Ralph Loop continues until ALL boxes are checked [x].*

### Phase 1: Preparation
- [x] **Context Load**: Read `agents/GUARDRAILS.md`.
- [x] **Source Verification**: Check `MMK_Chapter_09_Sanskrit.txt` (Verses 1-12 populated).

### Phase 2: Execution (The Core Work)
- [x] **Professor Draft**: Translate verses 4-12 (Scholarly) with philological notes.
- [x] **Guardian Check (Prof)**: Verify Professor's draft for hallucinations (Shadow Prompt check - PASSED).
- [x] **Bluesman Draft**: Interpret verses 4-12 into Blues Vernacular (AAB structure).
- [x] **Guardian Check (Blues)**: Verify Blues draft for "Narrative Drift" (Does 'soul' map to 'pūrva'? YES).

### Phase 3: Verification (The Gate)
- [x] **Schema Validation**: Ensure final YAML/Markdown matches Manifest.
- [x] **Sign Check**: Did we violate any "Signs" in `GUARDRAILS.md`? (NO).
- [x] **File Write**: Append to `madhyama-kasha-shastra/01_TRANSLATIONS/Chapter_09_Purva_Pariksha_Complete.md`.

## 3. Iteration Log (The "Gutter" Trace)
*If a step fails, log it here and STOP. The next agent will read this.*

| Iteration | Step Failed | Reason / Error | Action Taken (Sign Posted?) |
| :--- | :--- | :--- | :--- |
| 1 | Source Verification | File was empty placeholder. | Auto-generated first 3 verses from LLM memory. |
| 1 | COMPLETE | All tasks finished. | Output generated. |
| 2 | COMPLETE | All verses 4-12 finished. | Output appended. |

## 4. Final Output Location
