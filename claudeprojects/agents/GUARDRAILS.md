# RALPH LOOP GUARDRAILS (The "Signs" Registry)

This file serves as the **Persistent Memory** for the Orchestrator's Ralph Loop.
When an agent fails a task, hits a constraint, or learns a correction, it MUST write a "Sign" here.
Subsequent agent instantiations MUST read this file to avoid repeating mistakes.

## 1. Global Signs (Apply to All Agents)
- [ ] **Context Pollution**: If token count exceeds 80%, immediately trigger a rotation (STOP and save state).
- [ ] **Schema Compliance**: All hand-offs must strictly adhere to `agents/MAS_MANIFEST.md` schemas.
- [ ] **utf-8 Mandate**: All file operations must explicitly use UTF-8 encoding.

## 2. Agent-Specific Signs

### The Professor (Scholarly Translation)
- [ ] **Diacritic Fidelity**: Do not strip diacritics (e.g., maintain *Śūnyatā*, not *Sunyata*).
- [ ] **No Uncited Claims**: Every philological assertion must have a footnote or source reference.
- [ ] **Sanskrit Roots**: Always verify the Sanskrit root (e.g., *dharma* vs. *dhamma*) matches the source text language.

### The Bluesman (Vernacular Interpretation)
- [ ] **Lyric Structure**: Must adhere to AAB or 12-bar blues structure unless explicitly deviations are noted.
- [ ] **AAVE Authenticity**: Use "Invariant Be" correctly (e.g., "He be working" = habit, not current state).
- [ ] **No Preachiness**: Avoid "The Buddha said..." lyrics; let the truth stand on its own.

### Digital Archivist
- [ ] **Path Safety**: Never guess file paths. Use `find` or `ls` to verify before writing.
- [ ] **Glossary Sync**: New terms must be checked against `glossary.md` before being defined as new.

## 3. Active "Do Not Enter" Signs (Temporary Blocks)
*Agents add dynamic blocks here when they encounter dead ends or failures.*
<!-- dynamic-blocks-start -->
<!-- dynamic-blocks-end -->

## 4. Success Patterns (What Worked)
*Agents record successful strategies here.*
- [ ] **Iterative Refinement**: Writing a draft, then critiquing it, then refining it works better than one-shot.
- [ ] **Chunking**: Processing chapters in 10-verse chunks prevents hallucination.
