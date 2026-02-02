# GEMINI.md - Scholarly Articles Context

## 1. Project Overview

This directory (`05_SCHOLARLY_ARTICLES`) serves as the academic publishing arm of the **Lotus Sutra Project**. Its primary focus is bridging African-American Blues tradition with Buddhist philosophy through rigorous scholarly inquiry.

**Current Focus:**
*   **Primary Manuscript:** "The Blues as Buddhist Epistemology" (Article 4).
*   **Target Journals:** *Philosophy East and West* (Academic), *Tricycle* (Popular/Practitioner).
*   **Objective:** Establish academic credibility for the vernacular translation methodology.

## 2. Directory Structure & Key Files

### Manuscripts & Drafts
*   `ARTICLE_4_...BLIND_FOR_SUBMISSION.txt`: The anonymized version ready for peer review.
*   `ARTICLE_4_...FORMATTED_FOR_ELEVENREADER.txt`: Optimized for TTS proofing.
*   `ARTICLE_4_DRAFT_...txt`: The working draft.
*   `The_Blues_as_Buddhist_Epistemology.docx`: The final output document.

### Strategy & Documentation
*   `SUBMISSION_STRATEGY_REPORT_Blues_Buddhist_Epistemology.md`: **CRITICAL**. The roadmap for revision and submission. Read this first to understand the current status.
*   `article_materials_checklist.md`: Comprehensive list of required materials for all planned articles.
*   `ARTICLE_APPARATUS_STANDARDIZATION_METHODOLOGY.md`: Style guide for citations and formatting.

### Automation Utilities
*   `create_formatted_manuscript.py`: Converts the TXT draft into a submission-ready DOCX file. It handles double-spacing, margins, and converting Markdown italics (`*text*`) to Word italics.
*   `create_pdf_manuscript.py`: Generates a PDF version of the manuscript.

## 3. Operational Workflows

### A. Editing & Revision
1.  **Edit the TXT file:** Make content changes in the `ARTICLE_4_...txt` file.
2.  **Maintain Markdown:** Use `*italics*` for emphasis/titles in the text file.
3.  **Verify References:** Ensure all citations match the `ARTICLE_APPARATUS_STANDARDIZATION_METHODOLOGY.md`.

### B. Generating Submission Documents
To create the `.docx` file for submission:
```bash
python3 create_formatted_manuscript.py
```
*Note: This script relies on the `python-docx` library. If missing, install via `pip install python-docx`.*

### C. Submission Process
Refer to `SUBMISSION_STRATEGY_REPORT...md` for the specific requirements of *Philosophy East and West*:
*   **Formatting:** 12pt Times New Roman, double-spaced.
*   **Anonymization:** Ensure the "Blind" version has no author details.
*   **Cover Letter:** Use the template in the strategy report.

## 4. Specialized Agents

When working in this directory, adopt or reference these personas:

*   **Dr. Amara Chen-Rothenberg:** Academic tone, focus on rigorous argumentation, citation accuracy, and philosophical nuance.
*   **Miriam Steinberg:** Publishing industry critic, focus on "sellability," platform building, and submission strategy.

## 5. Safety & Standards

*   **Academic Integrity:** Ensure all claims are cited.
*   **Encoding:** Maintain UTF-8 to preserve Sanskrit diacritics (e.g., Ś, ā, ṇ).
*   **Version Control:** Do not overwrite the `MASTER` versions without confirmation. Always work on a draft copy first.
