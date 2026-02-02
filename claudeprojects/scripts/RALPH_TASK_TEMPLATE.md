# RALPH TASK TEMPLATE (Machine-Verifiable Schema)

**Task ID**: [Unique ID, e.g., TASK-2026-01-11-001]
**Objective**: [One sentence clear goal]
**Current Iteration**: 0
**Max Iterations**: 10

## 1. Context & Resources
- **Source Text**: [Path to source]
- **Previous Output**: [Path to last draft, if any]
- **Reference Materials**:
  - [ ] `agents/GUARDRAILS.md` (MUST READ)
  - [ ] `agents/MAS_MANIFEST.md`

## 2. The Checklist (The Definition of Done)
*The Ralph Loop continues until ALL boxes are checked [x].*

### Phase 1: Preparation
- [ ] **Context Load**: Read `agents/GUARDRAILS.md` and Source Text.
- [ ] **Safety Check**: Verify Source Text encoding (UTF-8) and diacritics.

### Phase 2: Execution (The Core Work)
- [ ] **Drafting**: Generate initial output (Translation/Code/Plan).
- [ ] **Self-Correction**: Review draft against Agent Role constraints.
- [ ] **Refinement**: Apply corrections to create Candidate Release.

### Phase 3: Verification (The Gate)
- [ ] **Schema Validation**: Does output match the YAML/JSON schema in Manifest?
- [ ] **Sign Check**: Did we violate any "Signs" in `GUARDRAILS.md`?
- [ ] **File Write**: Save output to target path.

## 3. Iteration Log (The "Gutter" Trace)
*If a step fails, log it here and STOP. The next agent will read this.*

| Iteration | Step Failed | Reason / Error | Action Taken (Sign Posted?) |
| :--- | :--- | :--- | :--- |
| | | | |

## 4. Final Output Location
- **Primary Artifact**: [Path to final file]
