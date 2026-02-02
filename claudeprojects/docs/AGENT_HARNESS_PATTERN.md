# Agent Harness Pattern - Domain Memory System

**Last Updated**: December 8, 2025

This document explains how the claudeprojects workspace functions as a **domain memory system** for AI agents—enabling long-running, coherent collaboration across sessions where AI has no persistent memory.

---

## The Problem

AI agents are amnesiacs. Each conversation starts fresh. Without external memory, agents:
- Forget what was decided last session
- Rederive definitions of "done" every time
- Make disconnected progress that doesn't compound
- Behave like "an infinite sequence of disconnected interns"

---

## The Solution: Domain Memory

This workspace solves the problem with **persistent structured artifacts** that act as external memory:

### 1. Context Files (GEMINI.md / CLAUDE.md)
**Purpose**: Initializer agent pattern—sets the stage before work begins.

Each project contains these files that tell the agent:
- What the project is
- What the workflow is
- What files matter
- What rules to follow (safety vows, encoding, etc.)

### 2. Goal Backlog (TODO_LIST_MASTER_TRACKER.md)
**Purpose**: Persistent feature list with pass/fail status.

- `[ ]` = Not started
- `[/]` = In progress
- `[x]` = Done

Agent reads this, picks ONE task, works on it, updates status, exits.

### 3. Progress Logs (DEVLOG.md, Session Notes)
**Purpose**: Durable record of what happened each session.

Next agent run can read history and know:
- What was tried
- What broke
- What was reverted
- Decisions made and why

### 4. Specialized Agents (04_AGENTS/)
**Purpose**: Role-specific context for different tasks.

- The Professor (scholarly translation)
- The Bluesman (vernacular interpretation)
- The Songwriter (Blues songs)
- The Producer (Suno prompts)

Each agent file provides domain-specific instructions that persist.

### 5. Master Versions (00_MASTER_VERSIONS/)
**Purpose**: Source of truth for content.

This prevents agents from making conflicting edits across sessions.

---

## The Pattern

```
┌─────────────────────────────────────────────────────────┐
│  HUMAN provides prompt                                   │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│  AGENT reads domain memory:                              │
│  - GEMINI.md / CLAUDE.md (context)                       │
│  - TODO_TRACKER.md (goals)                               │
│  - DEVLOG.md (history)                                   │
│  - Agent files (role instructions)                       │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│  AGENT picks ONE task from backlog                       │
│  Works on it                                             │
│  Updates files                                           │
│  Updates tracker                                         │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│  SESSION ENDS - Agent memory disappears                  │
│  But domain memory persists in files                     │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│  NEXT SESSION - New agent reads same files               │
│  Picks up exactly where last session left off            │
└─────────────────────────────────────────────────────────┘
```

---

## Key Principles

1. **Externalize goals** — Turn "do X" into machine-readable backlog with pass/fail
2. **Make progress atomic** — One task per run, testable, observable
3. **Leave campsite cleaner** — End with updated docs, not just completed code
4. **Standardize bootup** — Every session starts with reading the same files
5. **Tie tests to memory** — Pass/fail status IS the source of truth

---

## Current Domain Memory Inventory

| Project | Context File | Tracker | Agent Files |
|---------|--------------|---------|-------------|
| Lotus Sutra | CLAUDE.md, GEMINI.md | TODO_LIST_MASTER_TRACKER.md | 5 specialized agents |
| Dhammapada | CLAUDE.md, GEMINI.md | COMPLETION_STATUS.md | Professor, Bluesman, Songwriter, Producer |
| Vimalakirti | CLAUDE.md, GEMINI.md | COMPLETION_STATUS.md | Professor, Bluesman |
| Heart Sutra | GEMINI.md | N/A | N/A |
| Diamond Sutra | GEMINI.md | N/A | N/A |

---

## Maintenance Rituals

**At session start:**
- Agent reads context files
- Agent reads tracker for current priorities
- Agent reads recent session notes if available

**At session end:**
- Update TODO tracker with completed items
- Add session notes to DEVLOG if significant work done
- Commit to git for versioning

**Periodically:**
- Review TODO tracker for stale items
- Update GEMINI.md if project structure changes
- Archive completed session notes

---

## The Moat

> "The moat isn't a smarter AI agent. The moat is your domain memory and harness."

The files in this workspace ARE the competitive advantage. Models will change. This structure will persist and compound.

---

*Based on principles from Anthropic's agent research and practical experience building the Dharma Reborn series.*
