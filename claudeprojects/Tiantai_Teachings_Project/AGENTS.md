# Repository Guidelines

## Project Structure & Module Organization
- `01_TRANSLATIONS/`: Working translations. Subfolders by text (e.g., `The_Profound_Meaning/`, `Great_Cessation/`, `The_Words_and_Phrases/`) and by audience (`Scholarly/`, `Practitioner/`, `Modern_English/`, `English_Only/`).
- `02_SOURCE_MATERIALS/`: Classical Chinese source files (Taishō editions). Treat as read-only references.
- `03_DOCUMENTATION/`: Glossaries, protocol docs, completion status, and project notes.
- `04_AGENTS/`: Project agent prompts (Architect/Practitioner) used for consistency.
- `Tiantai_Great_Works/`: Source text archives, TOCs, and YAML metadata.
- Root scripts: `create_docx.py`, `generate_mohe_zhiguan_docx.py` for DOCX generation.

## Build, Test, and Development Commands
- `python create_docx.py` — converts specific Markdown files into DOCX (see `files_to_convert`).
- `python generate_mohe_zhiguan_docx.py` — concatenates multiple Markdown files into full Scholarly/Practitioner DOCX volumes.
- No formal build or test runner is defined; treat scripts as ad hoc utilities.

## Coding Style & Naming Conventions
- Primary formats: Markdown (`.md`), plain text (`.txt`), and YAML (`.yaml`).
- File naming pattern: `Title_Fascicle_##_SCHOLARLY.md`, `..._PRACTITIONER.md`, or `..._MODERN.md`.
- Preserve UTF-8, diacritics (e.g., macrons), and transliteration accuracy.
- Keep headings structured (`#`, `##`, `###`) to support DOCX conversion.

## Testing Guidelines
- No automated tests or coverage targets are present.
- Manual checks: verify doctrinal terms (Threefold Truth, Ten Suchnesses), and ensure headers/lists render correctly in DOCX outputs.

## Commit & Pull Request Guidelines
- Commit style in history is imperative and descriptive (e.g., “Complete …”, “Add …”, “Fix: …”).
- Keep commits focused on a single text or output.
- PRs should include: summary, files touched, and any generated artifacts (DOCX/EPUB) if applicable.

## Agent & Translation Workflow Notes
- Follow `CLAUDE.md` for doctrinal safeguards and workflow (Architect → Practitioner → Road Manager audit).
- Distinguish “Trace Gate” vs. “Fundamental Gate” where relevant; avoid paraphrase drift.
