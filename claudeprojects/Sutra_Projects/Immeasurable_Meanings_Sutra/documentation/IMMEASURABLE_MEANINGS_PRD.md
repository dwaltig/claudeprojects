# Product Requirements Document: Immeasurable Meanings Sutra - Scholarly Edition

## 1. Introduction & Context
The **Immeasurable Meanings Sutra (Wu Liang Yi Jing - 無量義經)** is the semantic prologue to the Lotus Sutra. It provides the doctrinal foundation for the "One Vehicle" by establishing that all meanings come from "One Law" (Emptiness/Nature of Mind). This project aims to complete the **Scholarly Edition** of the text.

**Current Status:**
*   **Chapter 1 (Virtuous Conduct):** Draft complete (`scholarly_edition/CHAPTER_01_...`).
*   **Chapter 2 (Preaching the Dharma):** To be created.
*   **Chapter 3 (Ten Merits):** To be created.

## 2. Goals & Objectives
*   **Primary Goal:** Translate Chapters 2 and 3 into rigorous, academic English.
*   **Philological Standard:** Use Sanskrit diacritics for reconstructed terms and Pinyin for Chinese-specific terms.
*   **Philosophical Standard:** Adhere to the **Zhiyi Protocol** (Tiantai interpretation), specifically highlighting the "Three Truths" and the "simultaneity of cause and effect."
*   **Integrity Standard:** Adhere to the **Seven-Factor Integrity Protocols**, ensuring "Right Speech" (accuracy without sycophancy) and "Right View" (doctrinal consistency).

## 3. User Stories & Acceptance Criteria

### Story 1: Chapter 2 Translation (Preaching the Dharma)
*   **As a** Scholar/Practitioner,
*   **I want** a translation of "Preaching the Dharma" (Shuo Fa Pin),
*   **So that** I can understand the specific connection between the "Three Laws" and the "One Reality."
*   **Acceptance Criteria:**
    *   [ ] Full translation of the prose section.
    *   [ ] Footnotes explaining the "Three Laws" (arising, abiding, ceasing).
    *   [ ] Scholarly Apparatus section defining key terms (`wúliángyì`, `shíxiàng`).
    *   [ ] File saved as `scholarly_edition/CHAPTER_02_PREACHING_DHARMA_SCHOLARLY.md`.

### Story 2: Chapter 3 Translation (Ten Merits)
*   **As a** Scholar/Practitioner,
*   **I want** a translation of "Ten Merits" (Shi Gong De Pin),
*   **So that** I can understand the functional power of the sutra in daily life.
*   **Acceptance Criteria:**
    *   [ ] Full translation of the ten specific merits.
    *   [ ] Footnotes explaining the "transformation of the body" (metaphorical vs. literal).
    *   [ ] Scholarly Apparatus section.
    *   [ ] File saved as `scholarly_edition/CHAPTER_03_TEN_MERITS_SCHOLARLY.md`.

### Story 3: Final Consolidation
*   **As a** Project Manager,
*   **I want** a consolidated PDF/DOCX of the full sutra,
*   **So that** it can be distributed for peer review.
*   **Acceptance Criteria:**
    *   [ ] All 3 chapters merged.
    *   [ ] Consistent formatting (Headers, Footnotes).

## 4. Agent Personas
*   **The Professor (Dr. Rajesh Patel):** Primary translator. Focus on *philology*, *history*, and *Tiantai exegesis*.
*   **The Bluesman (Master John Kim):** Cultural consultant (optional for Scholarly, mandatory for Blues edition).

## 5. Technical Specifications
*   **Source Text:** `/source/Chinese Immeasurable Meanings Sutra.txt`.
*   **Output Format:** Markdown (GitHub Flavored).
*   **Reference Material:** `tiantai-buddhist-tradition-lot` (NotebookLM).
