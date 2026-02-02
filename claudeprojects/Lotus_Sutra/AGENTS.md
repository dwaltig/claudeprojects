# Repository Guidelines

## Project Structure & Module Organization
- Start with `documentation/00_PROJECT_INDEX.txt` for navigation.
- Keep `00_MASTER_VERSIONS/` read-only; draft in `01_BLUES_INTERPRETATION/` and `03_SCHOLARLY_TRANSLATION_2025/Scholarly_Chapters/`, then promote.
- Key areas: Blues narrative in `01_BLUES_INTERPRETATION/`; scholarly text and apparatus in `03_SCHOLARLY_TRANSLATION_2025/` (`Scholarly_Chapters/`, `BUILD/`); audio deliverables in `04_AUDIO_PRODUCTION/chapters/`; submissions and marketing in `07_PUBLISHING_MATERIALS/` and `marketing/`; references and drafts in `08_REFERENCE_MATERIALS/` and `09_WORKING_DRAFTS/`.
- Maintenance scripts are in `scripts/` and `03_SCHOLARLY_TRANSLATION_2025/TOOLS/`; superseded assets land in `10_ARCHIVE/`.

## Build, Test, and Development Commands
- Content-first workflow; ensure `python3` is available.
- `python3 scripts/extract_audio_chapters.py` — rebuilds the 28 audio chapter files from the Blues master; run after Blues edits.
- `python3 scripts/fix_stray_chinese_comprehensive.py` — cleans stray Chinese characters across Blues variants; paths are hard-coded, so review and back up if you have local edits.
- Scholarly utilities (apparatus standardization, audits) live in `03_SCHOLARLY_TRANSLATION_2025/`; read the file header to confirm targets before running.
- After any script, run `git diff --stat` and spot-check outputs to confirm only intended files changed.

## Coding Style & Naming Conventions
- Keep the zero-padded prefix pattern (`00_`, `01_`, `CHAPTER_XX_...`) so folders and chapters sort predictably.
- Prefer Markdown or UTF-8 text; preserve apparatus formatting and voice tags; avoid new smart quotes unless already present.
- Python helpers: 4-space indents, PEP 8 naming, with path/config constants near the top for easy review.

## Testing Guidelines
- No automated suite. After extraction, confirm all 28 chapter files exist and open cleanly; after cleanup, scan diffs for unintended removals.
- For scholarly chapters, check footnote numbering and apparatus headers against neighbors in `Scholarly_Chapters/`.
- Note checks or follow-ups in `documentation/DEVLOG.md` or `documentation/TODO_LIST_MASTER_TRACKER.md` for traceability.

## Commit & Pull Request Guidelines
- Follow repo log style: concise, action-first subjects with scope (e.g., "Extend pedagogical weaving across all chapters"); keep under ~72 characters.
- Group related edits; avoid touching `00_MASTER_VERSIONS/` unless releasing—work in staging folders first.
- Hand-offs/PRs should list: summary, directories touched, commands run, remaining manual checks, and supporting excerpts or screenshots for publisher-facing docs.
