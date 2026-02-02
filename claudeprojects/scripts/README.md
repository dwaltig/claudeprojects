# scripts/ Reference (Code Wiki)

This directory contains the automation logic for the Lotus Sutra and associated scholarship projects. These scripts bridge the gap between Markdown-based drafting and professional publishing formats.

## 📦 Core Publishing Tools

| Script | Purpose | Key Inputs | Outputs |
|:---|:---|:---|:---|
| `generate_blues_docx.py` | Converts Blues lyrics to Word. | `.md` translations | `.docx` formatted lyrics |
| `clean_blues.py` | Extracts raw lyrics from translations. | `..._Complete.md` | `..._Lyrics_Only.md` |
| `create_silicon_samsara_docx.py` | JBE-standard academic formatting. | `..._HUMANIZED.md` | Professional `.docx` (Gentium Plus font, double-spaced) |
| `create_jbe_submission.py` | Prepares final JBE submission bundles. | Multiple drafts | Cleaned submission copies |

## 🤖 Agentic & System Utilities

### `agent_cli.py`
The primary interface for the **Scholarly Agent**. Use this to run complex cross-project tasks.
- **Command:** `python3 scripts/agent_cli.py "Your prompt"`
- **Capabilities:** Terminology analysis, diacritic validation, and consistent capitalization checks across all sutra projects.

### `ralph.sh`
The "task-runner" utility. Provides a template-driven approach to complex workflows.
- **Related:** `RALPH_TASK_TEMPLATE.md`

### Gender & Inclusivity Edits
A suite of scripts used for modernizing translations to be gender-inclusive without losing scholarly accuracy.
- `apply_gender_inclusive_edits.py`
- `revise_gender_inclusive.py`
- `complete_gender_edits.py`


## 🎨 Design & Media

| Script | Purpose | Key Inputs | Outputs |
|:---|:---|:---|:---|
| `add_cover_typography.py` | Enforces cover art dimensions and overlays text. | Generated Art (`.png`) | Final Asset (1200x1800px) |

### Cover Art Protocols (MANDATORY)
1. **Dimensions:** All final cover art **MUST** be **1200x1800px**. Use `add_cover_typography.py` to enforce this via crop/resize.
2. **Historical Accuracy:** Portrayals of Nichiren must feature authentic **13th-century Tiantai/Tendai robes** (grey + kesa).
3. **Attribution:** Author credit: **WILLIAM ALTIG**.

## 🛠 Maintenance & Quality

- `stability_audit.py`: Checks for file corruption or structural breaks in the translation directories.
- `memory_pruner.py`: Utility for cleaning up agent memory/context files.
- `clean_elevenreader_converter.py`: Optimizes text for the ElevenReader TTS (Text-to-Speech) platform.

---

### ⚠️ Note for AI Agents
When using these scripts:
1. **Check Paths:** Most scripts currently use hardcoded paths. Always read the script content before execution to ensure it points to the correct input file.
2. **Environment:** Ensure you are in the `.venv` if Python dependencies (like `python-docx`) are required.
3. **Encoding:** All scripts MUST maintain `UTF-8` to preserve Sanskrit/Pali diacritics.
