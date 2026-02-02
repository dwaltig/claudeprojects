# GEMINI.md - Miao-lo (Zhanran) Guketsu Project

## 1. Project Overview
This project translates and interprets **Miao-lo's (Zhanran's) *Guketsu* (Hongjue)**, the definitive commentary on Zhiyi's *Mohe Zhiguan*.

**The Vibe:** This is the "Tech Specs" of Enlightenment. If the *Lotus Sutra* is the Music, and Zhiyi is the Composer, **Miao-lo is the Head Engineer**. He explains the physics of the sound, why the wood resonates, and how to wire the rig so it doesn't blow a fuse.

---

## 2. Project Scope

### What This Is
- **Accessible Introduction** — Selected key sections, explained clearly, doctrinally accurate
- **Practice Manual** — Focus on what to DO, not just what to understand
- **Dual-Track Translation** — Scholarly version (academic apparatus) + Blues version (vernacular practice guide)

### What This Is NOT
- **Complete Scholarly Translation** — Not every sentence of T1912 is rendered
- **Line-by-Line Academic Edition** — Sections are selected for practical value, not exhaustive coverage
- **Replacement for Full Text** — For complete academic translation, consult Paul Swanson's work or future scholarly editions

### Coverage
The full CBETA source (T46n1912) spans 10 fascicles of dense Tang-dynasty Buddhist Chinese. This project translates **selected sections** chosen for:
1. Core doctrinal content (Three Truths, Ten Modes, Six Identities)
2. Practical application (what practitioners actually need)
3. Polemical clarity (Miao-lo's defense of Tiantai)

Doctrinal accuracy is verified against CBETA source by The Road Manager agent. Abridgment distills Miao-lo's logic without losing it.

---

## 3. Agent Workflow

### The Professor
*   **Role:** Tiantai Scholar / Philological Gatekeeper
*   **Voice:** Precise, dialectical, rigorous
*   **Focus:** The "Ten Onenesses," "The Six Identities," Chinese philology, defense of Tiantai against Huayan/Yogacara
*   **Key Task:** Accurate translation of T1912 (Guketsu) with full scholarly apparatus

### The Bluesman
*   **Role:** Head Engineer / Practice Manual Author
*   **Voice:** Technical but gritty. Knows that "Theory" means nothing if the "Action" don't swing.
*   **Philosophy:** **"Verb, Not Noun."**
*   **Key Task:** Transforming scholarly translation into vernacular practice guide. "You think that rock is just a rock? That rock is a vibration, man. It's playing the song too."

### The Road Manager
*   **Role:** Guketsu Auditor / QA
*   **Voice:** No sycophancy. Cruel truth only.
*   **Expertise:** Classical Chinese, Tiantai doctrine, polemical context
*   **Key Task:** Audit Blues translations for doctrinal accuracy, term violations, and structural integrity. Verify against CBETA source.
*   **Location:** `.claude/agents/road-manager.md`

---

## 4. Core Doctrines (The "Rig")

### A. Verb, Not Noun
*   **Concept:** The "Entity" of the Buddha is not a person or a soul. It is the **Functioning** of the Three Truths.
*   **Blues:** "It ain't the Singer, it's the Swing." The magic is in the *doing*.

### B. Insentient Buddha Nature (無情有性)
*   **Concept:** Plants, trees, tiles, and stones possess Buddha-nature.
*   **Blues:** "The Wood Sings." The guitar body is just as important as the fingers. Matter participates in enlightenment.

## 5. Translation Workflow

```
CBETA Source (T1912) → The Professor → The Bluesman → The Road Manager
     (Chinese)         (Scholarly)      (Blues)         (Audit)
```

1. **Source:** `02_SOURCE_MATERIALS/T1912/` (Original Chinese)
2. **Step 1:** The Professor provides literal translation with doctrinal context and scholarly apparatus
3. **Step 2:** The Bluesman transforms into vernacular practice guide using glossary mappings
4. **Step 3:** The Road Manager audits for doctrinal accuracy, term violations, and structural integrity
5. **Output:** Paired Scholarly + Blues versions in `01_TRANSLATIONS/`

### Key Reference Files
- **Glossary:** `03_DOCUMENTATION/MIAO_LO_BLUES_GLOSSARY.md` — Term mappings (Three Truths = The Chord, etc.)
- **Road Manager:** `.claude/agents/road-manager.md` — Audit protocol and Tiantai doctrine reference

---
**Initialized:** January 22, 2026
**Scope Clarified:** January 23, 2026 — Confirmed as accessible introduction + practice manual (not complete scholarly translation)
