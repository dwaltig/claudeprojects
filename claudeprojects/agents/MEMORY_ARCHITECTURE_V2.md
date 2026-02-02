# MAS Memory Architecture V2: Hybrid Graph-Vector & Cognitive Pruning

**Implemented:** January 2026
**Based on:** *LLM Agent Memory Architectures* (NotebookLM)

This document defines the upgraded memory protocols for the Lotus Sutra Project's Multi-Agent System (MAS). It addresses the limitations of simple "context window" management by introducing a **Hybrid Graph-Vector System** and formal **Forgetting Policies**.

## 1. The Core Problem: The Context-Consistency Trade-off
Long-horizon translation projects suffer from two opposing forces:
*   **Consistency Need:** We need to remember a translation decision made 4 months ago in Chapter 1.
*   **Context Scarcity:** We cannot stuff 4 months of logs into the active window without "bloat" and hallucination.

## 2. Solution: The Tri-Store Memory Architecture

We move from a simple "Tiered" system to a functional **Tri-Store**:

### A. Semantic Knowledge Graph (The "Encyclopedia")
*   **Structure:** Network of entities (terms, concepts) and edges (relationships).
*   **Tech:** Markdown links + Tagging (Simulated Graph).
*   **Use Case:** "What is the standard translation for *Sunyata*?" "How does *Upaya* relate to *Prajna*?"
*   **Owner:** Digital Archivist.

### B. Episodic Event Log (The "Diary")
*   **Structure:** Chronological log of **Decision Events** (not just chat logs).
*   **Format:** `[Date] [Chapter] [Decision] [Reasoning] [Result]`
*   **Use Case:** "Why did we choose 'Luminous Awareness' instead of 'Bright Mind' in the last session?"
*   **Owner:** Reliability Guardian (Logger) / The Professor (User).

### C. Procedural Skill Library (The "Playbook")
*   **Structure:** Library of **Verified SOPs** and **Prompt Templates**.
*   **Use Case:** "How do we format a Blues verse?" (Retrieves the 'Blues_Verse_Structure' skill).
*   **Owner:** Orchestrator.

## 3. The "Cognitive Pruning" Protocol (Forgetting Policy)

To prevent "Catastrophic Bloat," we implement a **Gated Forgetting Policy** based on the MaRS framework:

1.  **Intermediate Trace Decay:**
    *   *Rule:* All "reasoning traces" (inner monologue) are discarded after the session ends.
    *   *Exception:* Unless flagged as a "Novel Reasoning Pattern" (add to Skill Library).

2.  **FIFO with Significance Gating:**
    *   *Rule:* "Cold" logs are archived (moved to `archive/`) when they exceed 30 days.
    *   *Gate:* Any log tagged `#CRITICAL_DECISION` is never archived, but summarized into the Semantic Graph.

3.  **Consolidation Cycles:**
    *   *Trigger:* Every 5 chapters.
    *   *Action:* The Archivist scans the Episodic Log, extracts consistent patterns, updates the Semantic Graph, and *deletes* the raw episodic data.

## 4. Implementation Guidelines

### For The Archivist
*   **Action:** When a session ends, run `consolidate_memory()`.
*   **Prompt:** "Review the session logs. Extract any new definition of *Key Terms* into the Glossary. Summarize the rationale. Then, mark the raw logs for archival."

### For The Orchestrator
*   **Action:** Before starting a new chapter, run `retrieve_context(scope='episodic', depth=5)`.
*   **Prompt:** "Retrieve the last 5 decisions related to [Current Theme] from the Episodic Log."

---

**References:**
*   *LLM Agent Memory Architectures* (NotebookLM) - [Link](https://notebooklm.google.com/notebook/d68fd0d6-6dc0-425d-a87e-e6a69db700cc)
*   *MemGPT: Towards LLMs as Operating Systems*
*   *Generative Agents: Interactive Simulacra of Human Behavior*
