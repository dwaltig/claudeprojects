# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Safety Protocol

**Before modifying any files**, read `claudeprojects/Lotus_Sutra/.claude/SAFETY_VOW.md`. This workspace contains months of sacred scholarly work. A previous careless edit deleted months of translated chapters and footnotes. Always ask before acting, verify changes, and preserve existing work.

## Operating Protocols

All work in this repository operates under two mandatory protocol layers:

1. **Zhiyi Protocol** (`claudeprojects/ZHIYI_PROTOCOL.md`) -- Decision-making methodology based on Tiantai "Perfect Teaching" (Three Truths, Four Siddhāntas, Six Stages of Identity)
2. **Integrity Protocols** (`claudeprojects/AGENT_INTEGRITY_PROTOCOLS.md`) -- Seven-Factor ethical firewall with Three Gates anti-sycophancy check (Sacca/truth, Attha/benefit, Kāla/timeliness)

---

## What This Repository Contains

A multi-project workspace combining Buddhist sutra translation/audio production with AI research infrastructure.

### Primary: Buddhist Sutra Translation (`claudeprojects/Lotus_Sutra/`)

28-chapter Lotus Sutra with 1,554+ scholarly footnotes, a parallel blues/gospel vernacular version, classical Chinese source (Kumarajiva 406 CE), and professional audio production materials. This is the active primary project.

**Detailed guidance**: `claudeprojects/Lotus_Sutra/CLAUDE.md` (659 lines -- read this before any Lotus Sutra work)

### Secondary Sutra Projects

| Project | Location | Status |
|---------|----------|--------|
| Vimalakirti Sutra | `claudeprojects/Vimalakirti_Sutra_Project/` | Active |
| Sutra Projects (Immeasurable Meanings, Universal Worthy) | `claudeprojects/Sutra_Projects/` | Secondary |
| Diamond Sutra | `claudeprojects/Diamond Sutra Project/` | Early stage |
| Dhammapada | `claudeprojects/Dhammapada/` | In progress |
| Nirvana Sutra | `claudeprojects/Nirvana_Sutra_Project/` | In progress |
| Tiantai Teachings | `claudeprojects/Tiantai_Teachings_Project/` | In progress |

Each project has its own CLAUDE.md with project-specific guidance.

### GPT Researcher (`claudeprojects/gpt-researcher/`)

Autonomous LLM-based research agent system. Python 3.11+ / FastAPI backend with LangChain/LangGraph multi-agent orchestration. Next.js frontend.

### AGENTS.md Website (`claudeprojects/agents.md/`)

Next.js 16 / React 19 / TypeScript / Tailwind CSS website for the AGENTS.md specification.

---

## Build & Run Commands

### Lotus Sutra (Python scripts)

```bash
# Assemble multi-version Buddhist texts
python claudeprojects/scripts/assemble_guketsu.py

# Generate DOCX books from Markdown
python claudeprojects/scripts/generate_wenju_books.py

# Compile and format commentaries
python claudeprojects/scripts/compile_and_format_xuanyi.py
python claudeprojects/scripts/compile_and_format_guketsu.py
```

### GPT Researcher (Python/FastAPI)

```bash
cd claudeprojects/gpt-researcher
poetry install
poetry run pytest                    # Run tests (asyncio strict mode)
python -m pytest tests/              # Alternative test invocation
python -m uvicorn backend.server.server:app --reload  # Dev server
docker-compose up                    # Start all services via Docker
```

### AGENTS.md Website (Next.js)

```bash
cd claudeprojects/agents.md
pnpm install
pnpm run dev      # Dev server with Turbopack (port 3000)
pnpm run build    # Production build
pnpm run lint     # ESLint
```

---

## Architecture

### Lotus Sutra: Multi-Version Translation System

Three parallel content pipelines maintained from a single source of truth:

- `00_MASTER_VERSIONS/` -- Canonical source of truth for all translations
- `03_SCHOLARLY_TRANSLATION_2025/Scholarly_Chapters/` -- 28 chapter files with full scholarly apparatus (1,554 footnotes). **Authoritative** for academic work. Replaces deprecated `02_SCHOLARLY_ENGLISH/`.
- `01_BLUES_INTERPRETATION/` -- Blues/gospel vernacular version (intentionally different register, not an error)
- `04_AUDIO_PRODUCTION/chapters/` -- Voice-tagged chapters optimized for Google Gemini TTS (530+ voice tags, verses combined into single paragraphs for API efficiency)

**Do not confuse these three "master" sources** -- each serves a distinct purpose.

### Lotus Sutra: Five Specialized Agents (`claudeprojects/Lotus_Sutra/agents/`)

| Agent | File | Purpose |
|-------|------|---------|
| Dharma Audio Producer | `01_dharma-audio-producer-enhanced.md` | TTS audio script optimization for Gemini |
| Dr. Amara Chen-Rothenberg | `02_scholarly-writer-agent_*.md` | Peer-review-ready academic articles |
| Miriam Steinberg | `03_publishing-critic-persona_*.md` | Brutally honest commercial viability assessment |
| Kaelen "Kai" Reed | `04_classical-chinese-interpreter-persona_*.md` | Poetic/musical classical Chinese interpretation |
| HTML Code Master | `05_html-code-master.md` | Web development |

### GPT Researcher: Multi-Agent Research Pipeline

`backend/multi_agents/` coordinates Browser, Editor, Researcher, Reviewer, Revisor, Writer, and Publisher agents through a Plan -> Execute -> Review -> Publish pipeline. Core research engine in `gpt_researcher/`. Report output via Jinja2 templates in multiple formats (PDF, Markdown, DOCX).

### Agent Skills System (`claudeprojects/.agent/skills/`)

229 modular agent capabilities with workflow definitions in `claudeprojects/.agent/workflows/`.

---

## Translation Conventions

- **UTF-8 encoding** required for all translation files. Verify with `file -i [filename]`.
- **Sanskrit diacriticals are critical**: Sariputra, Mahakasyapa, Manjusri, Avalokitesvara (ś, ṇ, ū, ā, ṃ). Loss of diacriticals = text corruption.
- **Terminology reference**: `claudeprojects/Lotus_Sutra/08_REFERENCE_MATERIALS/TERMINOLOGY_CORRECTIONS_SUMMARY.md`
- **Character names**: `claudeprojects/Lotus_Sutra/08_REFERENCE_MATERIALS/CHARACTER_VOICE_MAPPING_FINAL.txt`
- **Capitalization**: Dharma (teachings) vs. dharma (phenomena); Buddha (historical) vs. buddha (awakened being); Tathagata, Bodhisattva, Arhat always capitalized.

---

## Project Tracking

```bash
# Active tasks
cat claudeprojects/Lotus_Sutra/documentation/TODO_LIST_MASTER_TRACKER.md

# Recent work log
cat claudeprojects/Lotus_Sutra/documentation/DEVLOG.md

# Recent commits
git log --oneline -20

# Publication progress
cat claudeprojects/MASTER_PUBLICATION_TRACKER.md
```

---

## Key Files to Read First

| Priority | File | Purpose |
|----------|------|---------|
| CRITICAL | `claudeprojects/Lotus_Sutra/.claude/SAFETY_VOW.md` | Safety protocols for editing |
| Before Lotus work | `claudeprojects/Lotus_Sutra/CLAUDE.md` | Full project guidance (659 lines) |
| Before workspace work | `claudeprojects/CLAUDE.md` | Workspace-level overview (526 lines) |
| Before gpt-researcher work | `claudeprojects/gpt-researcher/.cursorrules` | Development standards |
| Operating system | `claudeprojects/ZHIYI_PROTOCOL.md` | AI decision-making methodology |
| Ethical constraints | `claudeprojects/AGENT_INTEGRITY_PROTOCOLS.md` | Seven-Factor integrity model |
