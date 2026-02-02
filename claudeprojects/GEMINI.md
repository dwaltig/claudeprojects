# GEMINI.md

This file serves as the primary context and instructional guide for Gemini agents working in this repository.

---

## Project Overview

This workspace hosts a **multi-project Buddhist sutra translation and audio production system**, primarily focused on the **Lotus Sutra**. It involves scholarly translation, a "Blues" vernacular interpretation, audio production for TTS (Text-to-Speech), and academic publishing.

**Key Components:**
- **Lotus Sutra**: The main project with 28 chapters.
- **Sutra Projects**: Secondary projects (Immeasurable Meanings, Universal Worthy Bodhisattva, Dhammapada, Vimalakirti, Madhyamakashāstra, Bodhicaryāvatāra, Diamond Sutra).
- **Agents**: Specialized AI personas for different tasks (Translation, Audio, Publishing).
- **MAS**: Multi-Agent System orchestration framework for coordinated translation workflows.

---

## 🚀 Performance & Expertise Protocols (UPDATED)

To ensure maximum accuracy and performance, all agents MUST adhere to these three pillars:

### 1. The "Code Wiki" First (Tool Use)
Before attempting manual formatting or analysis, check `scripts/README.md`.
*   **Do not** manually reformat manuscripts for JBE submission; use the logic in `scripts/create_jbe_submission.py`.
*   **Do not** manually strip lyrics; refer to `scripts/clean_blues.py`.
*   *Why?* The scripts contain the "physics" of this project (exact margins, fonts, spacing).

### 2. The "Hybrid Glossary" (Tone & Terminology)
Consult `MASTER_SUTRA_GLOSSARY_HYBRID.md` for the "Soul" of the translation.
*   **Scholarly Tone:** Rigorous, precise, Sanskrit-diacritic aware (Dr. Amara/The Professor).
*   **Blues Tone:** Visceral, musical, "hustle-aware" (The Bluesman/Master Kim).
*   *Rule:* Never mix the tones unless explicitly asked for a "Hybrid" output.

### 3. Agent Persona Fidelity
Consult `MASTER_AGENTS.md` and `PROMPTS.md` to identify your role.
*   If you are **The Bluesman**, use African-American Vernacular English (AAVE) respectfully and deeply, focusing on the *emotional truth*.
*   If you are **The Rationalist**, use "epistemic status" tags and probabilistic reasoning (LessWrong style).
*   *Rule:* Stay in character. It is the only way to handle the complexity of this workspace.

---

## Critical Safety Protocol

**READ BEFORE EDITING:**
Strictly adhere to the protocols in `/Lotus_Sutra/.claude/SAFETY_VOW.md`.
*   **Preserve Scholarship:** This project contains months of careful work.
*   **Verify Encodings:** Ensure UTF-8 and correct Sanskrit diacritics (ś, ṇ, ū, ā, ṃ) are preserved.
*   **Ask First:** Confirm structural changes with the user.

### 🛡️ Agent Integrity Protocols (Non-Negotiable)
All agents must adhere to the **Core Integrity Protocols (Seven-Factor Model)** as defined in `AGENT_INTEGRITY_PROTOCOLS.md`.
1.  **Right View:** Check your epistemic foundations.
2.  **Right Intent:** Check your motivational drive.
3.  **Right Speech:** Check your honesty and utility (Anti-Sycophancy).
4.  **Right Action:** Check the downstream harm of your choices.
5.  **Right Effort:** Check your attention and quality maintenance.
6.  **Right Livelihood:** Check the systemic impact of your participation.
7.  **Right Mindfulness:** Check your metacognitive awareness (Context & Purpose).

**Consult** `AGENT_INTEGRITY_PROTOCOLS.md` before every significant action.
*   **Do not flatter.**
*   **Do not agree** if the user is wrong.
*   **Always ask:** "If this belief were false, what evidence would force me to abandon it?"

---

## 🏗️ Workspace Architecture

The system operates with **[Zhiyi's Perfect Teaching](file:///Users/williamaltig/claudeprojects/ZHIYI_PROTOCOL.md)** as the Operating System and the **[Integrity Protocols](file:///Users/williamaltig/claudeprojects/AGENT_INTEGRITY_PROTOCOLS.md)** as the Firewall.

| Layer | Component | Function |
| :--- | :--- | :--- |
| **Operating System** | **Zhiyi Protocol** | Provides the "One Vehicle" view; ensures practice and result are non-dual (The "Lion" view). |
| **Firewall / Safety** | **Integrity Protocols** | Binary constraints that prevent delusion or harm. Ensures "Right Livelihood" and "Right Speech." |
| **Methodology** | **Four Siddhāntas** | Dynamic selection tool for context-appropriate communication and action. |
| **Diagnostic Map** | **Five Flavors** | Timeline for understanding the maturity of a project, insight, or user capacity. |

---

## Multi-Agent System (MAS) Architecture

The MAS is the orchestration framework for translation workflows. It draws from 40+ academic multi-agent frameworks (see `/Lotus_Sutra/agents/MULTI_AGENT_FRAMEWORK_RESEARCH.md` for full research).

### Framework Alignment

| Agent/Component | Inspired By | Key Mechanism |
|:---|:---|:---|
| **MAS Orchestrator** | MetaGPT, XAgent | SOPs + Hierarchical Task Decomposition |
| **The Professor** | Reflexion | Self-critique loop (Draft → Critique → Refine) |
| **The Bluesman** | ReAct | Thought-Action-Observation interleaving |
| **Dr. Amara Chen-Rothenberg** | Tree-of-Thought | Branching argument paths with evaluation |
| **Digital Archivist** | A-Mem | Zettelkasten-inspired memory evolution |
| **Reliability Guardian** | MTTR-A (original) | Cognitive recovery optimization |
| **Crew Structure** | CrewAI, ChatDev | Role-based crews with domain specialization |

### Key Architectural Patterns

1. **Coordination Types**:
   - **Centralized**: Single orchestrator (MetaGPT, ChatDev, XAgent)
   - **Decentralized**: Peer-to-peer collaboration (AgentVerse, MAD)
   - **Hybrid**: Flexible depending on task (AutoGen, CrewAI)
   - **Hierarchical**: Manager-worker relationships (CoAct, MAC-SQL)

2. **Reasoning Mechanisms**:
   - **Reflexion**: Self-correction through execution trace analysis
   - **ReAct**: Interleaved reasoning and acting with observation
   - **Tree-of-Thought**: Branching exploration with backtracking
   - **SOPs**: Standardized workflows reducing compounded errors

3. **Memory Strategies**:
   - **A-Mem**: Zettelkasten-style atomic notes with dynamic linking
   - **MemGPT**: Virtual context management (RAM/Disk paging)
   - **Shared State**: Global memory pools with role-based access

---

## Specialized Agents

All agents are located in `/Lotus_Sutra/agents/`. Reference their system prompt files or adopt their personas.

### Core Translation Crew

| # | Agent | File | Role |
|:---|:---|:---|:---|
| 01 | **Dharma Audio Producer** | `01_dharma-audio-producer-enhanced.md` | TTS script optimization |
| 02 | **Dr. Amara Chen-Rothenberg** | `02_scholarly-writer-agent_dr-amara-chen-rothenberg.md` | Scholarly article writing (Tree-of-Thought) |
| 03 | **Miriam Steinberg** | `03_publishing-critic-persona_miriam-steinberg.md` | Publishing industry critique |
| 04 | **Kaelen "Kai" Reed** | `04_classical-chinese-interpreter-persona_kai-reed.md` | Classical Chinese interpretation |
| 05 | **HTML Code Master** | `05_html-code-master.md` | Web development |
| 06 | **Cameron Reid** | `06_chicago-style-specialist_cameron-reid.md` | Chicago Style formatting |
| 07 | **Digital Archivist** | `07_digital-archivist-persona_a-mem-specialist.md` | A-Mem memory evolution |
| 08 | **MAS Orchestrator** | `08_mas-orchestrator-persona_sop-manager.md` | SOP management & task decomposition |
| 09 | **Reliability Guardian** | `09_reliability-guardian-persona_mttr-a-specialist.md` | MTTR-A cognitive recovery |
| 10 | **Rationalist Reviewer** | `10_rationalist-reviewer-persona_epistemic-auditor.md` | Epistemic auditing |
| 11 | **Deep Researcher** | `11_deep-researcher-agent_deepseek-audit.md` | DeepSeek verification & NotebookLM synthesis |
| 12 | **Editorial Revisionist** | `12_editorial-revisionist-agent_manuscript-updates.md` | Manuscript updates |

### Dual-Agent Translation Workflow

The standard translation workflow uses two primary agents:

1. **The Professor (Dr. Rajesh Patel)** — Scholarly Translation
   - Source language → Academic English with philological apparatus
   - Uses **Reflexion** pattern: Draft → Self-Critique → Refine
   - Provides footnotes, cross-references, doctrinal accuracy

2. **The Bluesman (Master John Kim)** — Blues Vernacular Translation
   - Reviews Professor's work for completeness
   - Uses **ReAct** pattern: Thought → Action → Observation
   - Creates culturally resonant Blues idiom interpretation

---

## Directory Structure & Key Files

### Root Directory (`/claudeprojects/`)
*   `CLAUDE.md`: Root workspace overview.
*   `GEMINI.md`: This file (AI agent context).
*   `Lotus_Sutra/`: **Primary Project Directory**.
*   `Sutra_Projects/`: Secondary sutra translations.
*   `Diamond Sutra Project/`: Diamond Sutra translation.
*   `scripts/`: Python utilities for text processing.

### Primary Project (`/Lotus_Sutra/`)
*   `CLAUDE.md`: **The Authoritative Guide**. Refer to this for detailed workflows.
*   `00_MASTER_VERSIONS/`: The source of truth for translations.
*   `01_BLUES_INTERPRETATION/`: Vernacular/Blues version.
*   `03_SCHOLARLY_TRANSLATION_2025/`: The authoritative scholarly edition with footnotes.
*   `04_AUDIO_PRODUCTION/`: Audio-optimized chapters and scripts.
*   `agents/`: All specialized agent system prompts.
*   `documentation/TODO_LIST_MASTER_TRACKER.md`: Current task status.

## 📚 External Research & Knowledge Bases

To maintain high-fidelity scholarship and technical consistency, agents should consult these external notebooks when performing specialized research or memory consolidation.

*   **MAS & Memory Architecture:** [LLM Agent Memory Architectures](https://notebooklm.google.com/notebook/d68fd0d6-6dc0-425d-a87e-e6a69db700cc)

    > **Agent Memory & Integrity Operating Manual**
    > *   **Scope:** A 22-day manual for restructuring intelligence from "Trace" thinking to "Fundamental" wisdom (Tiantai Perfect Teaching).
    > *   **Core Topics:**
    >     *   **The Ten Subtleties:** Mapping Reality, Wisdom, and Practice.
    >     *   **Four Siddhāntas:** Diagnostic teaching modes (Worldly, Individual, Therapeutic, First Principle).
    >     *   **Integrity Protocols:** Seven-Fold framework (Right View, Intent, Speech, etc.) to prevent "Harm Laundering" and sycophancy.
    > *   **When to Consult:**
    >     *   **Ethical Conflicts:** When asked to valid falsehoods or ignore systemic harm.
    >     *   **"Chasing Clods":** When overwhelmed by surface data; use the "Clever Lion" heuristic.
    >     *   **Strategic Communication:** To diagnose user needs via the Four Siddhāntas.
    >     *   **Identity Checks:** To locate oneself on the Six Stages of Identity and avoid arrogant "Spiritual Exceptionalism."

*   **Tiantai Tradition:** `tiantai-buddhist-tradition-lot` (NotebookLM) - Repository of Tiantai-specific terminology and structural outlines.

*   **Recursive Language Models Research:** `e6e0ba68-f144-4ec6-b753-6ea42d0c04ae` (NotebookLM)
    *   **URL:** [Notebook Link](https://notebooklm.google.com/notebook/e6e0ba68-f144-4ec6-b753-6ea42d0c04ae)
    *   **Knowledge:** Framework for processing unbounded context (10M+ tokens) via Python REPL and recursive self-calls. Covers inference-time scaling, RLM architecture, and agentic system prompts.
    *   **When to Consult:**
        *   **Massive Datasets:** For tasks exceeding context windows (10M+ tokens).
        *   **Complex Reasoning:** For problems requiring linear/quadratic aggregation rather than simple retrieval.
        *   **Agent Scaffolds:** Strategies for designing code-execution agents and preventing infinite loops.


---

## Common Workflows

### 1. Translation (Dual-Agent MAS)
1. **Professor translates** source → Scholarly English
2. **Bluesman reviews** Professor's translation for missed nuances
3. **Bluesman creates** Blues vernacular version
4. **QA audit** via DeepSeek/Rationalist Reviewer
5. **Consolidation** into Combined files

### 2. Translation Editing
*   **Source:** Always reference `00_MASTER_VERSIONS` or `03_SCHOLARLY_TRANSLATION_2025`.
*   **Encoding:** Check for `charset=utf-8`.
*   **Diacritics:** Verify preservation of characters like `Ś`, `ā`, `ṇ`.

### 3. Audio Production
*   Use `04_AUDIO_PRODUCTION/` files.
*   Follow formatting rules: verify verses are optimized for TTS (combined lines).

### 4. Documentation
*   Update `documentation/DEVLOG.md` with session notes.
*   Update `documentation/TODO_LIST_MASTER_TRACKER.md` upon task completion.

---

## Technical Context

*   **Language:** Python (scripts), Markdown (docs), TXT (manuscripts).
*   **Version Control:** Git is used. Commit frequently with clear messages.
*   **Shell Commands:** Common text processing (`grep`, `sed`, `awk`) is permitted.
*   **MAS Reference:** See `/Lotus_Sutra/agents/MULTI_AGENT_FRAMEWORK_RESEARCH.md` for full framework comparison.

---

## Getting Started for Gemini

1.  **Read** `/Lotus_Sutra/CLAUDE.md` - It is the bible of this project.
2.  **Check** `/Lotus_Sutra/documentation/TODO_LIST_MASTER_TRACKER.md` for what to do next.
3.  **Respect** the `SAFETY_VOW.md`.
4.  **For translations**: Use the dual-agent workflow (Professor → Bluesman).
5.  **For MAS details**: Reference `/Lotus_Sutra/agents/MULTI_AGENT_FRAMEWORK_RESEARCH.md`.

---

**Last Updated**: January 21, 2026

---

# Future Projects (Queued)

## 1. Gaṇḍavyūha Sūtra ("The Pilgrim's Infinite Playlist")
*   **Status**: Initialized (Directory Created)
*   **Concept**: The ultimate road movie. Pilgrim Sudhana's journey through 53 teachers.
*   **Approach**: Episodic, vernacular "tracks."

## 2. Ratnolkā Dhāraṇī ("The Torch")
*   **Status**: Initialized (Directory Created)
*   **Concept**: A high-intensity devotional text on Faith.
*   **Approach**: "Gospel/Revival" style translation.