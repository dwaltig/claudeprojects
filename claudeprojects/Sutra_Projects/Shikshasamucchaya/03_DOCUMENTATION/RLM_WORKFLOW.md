# RLM Workflow (Project Use)

This workflow emulates the Recursive Language Model (RLM) pattern for long
inputs by treating source files as external environment data and retrieving
only the needed slices for each reasoning step.

## Core Loop
1. Load source file(s) as external data.
2. Inspect metadata (size, lines, basic structure).
3. Search for anchor points (headers, key terms).
4. Pull narrow slices or line ranges.
5. Summarize the slice and decide next query.
6. Recurse until the task is complete.
7. Record gaps, assumptions, and open questions.

## Helper Script
Use `scripts/rlm_env.py` to access large files without loading them fully.

Examples:
```bash
python3 scripts/rlm_env.py 02_SOURCE_MATERIALS/śantidevaviracitaḥ\ śikṣāsamuccayaḥ.txt info
python3 scripts/rlm_env.py 02_SOURCE_MATERIALS/śantidevaviracitaḥ\ śikṣāsamuccayaḥ.txt search --pattern "dānapāramitā" --context 2
python3 scripts/rlm_env.py 02_SOURCE_MATERIALS/śantidevaviracitaḥ\ śikṣāsamuccayaḥ.txt lines --start 1 --end 120
```

## Notes
- Keep Sanskrit diacritics intact (UTF-8).
- Prefer targeted slices over full-file reads.
