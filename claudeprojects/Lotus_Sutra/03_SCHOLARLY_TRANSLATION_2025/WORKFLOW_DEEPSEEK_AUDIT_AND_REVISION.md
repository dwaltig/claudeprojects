# Workflow: DeepSeek Scholarly Audit & Revision Loop

This document defines the formal dual-agent loop for auditing and revising the Lotus Sutra scholarly translation using DeepSeek reasoning capabilities.

---

## 1. Directory Structure

- **Auditor Agent**: `agents/11_deep-researcher-agent_deepseek-audit.md`
- **Revision Agent**: `agents/12_editorial-revisionist-agent_manuscript-updates.md`
- **Audit Reports**: `03_SCHOLARLY_TRANSLATION_2025/AUDITS/`
- **Master Manuscript**: `03_SCHOLARLY_TRANSLATION_2025/Scholarly_Chapters/`

---

## 2. The Operational Loop

Perform this loop for each of the 28 chapters:

### Step A: The Audit (The Deep Researcher)
1. **Source Prep**: Load the Classical Chinese (Kumārajīva) and the current Scholarly English translation for the chapter.
2. **Reasoning Call**: Invoke DeepSeek (`get-deepseek-thinker`) with a prompt from the Audit Agent persona.
3. **Report Generation**: Save the results as `AUDIT_REPORT_CHAPTER_[XX]_DEEPSEEK.md`.

### Step B: The Revision (The Editorial Revisionist)
1. **Analyze Findings**: Review the specific term corrections and philosophical suggestions in the Audit Report.
2. **Apply Edits**: Update the `.md` chapter file using the Editorial Revisionist persona.
3. **Verify Compliance**: Check diacritics, footnote numbering, and UT-8 encoding.

### Step C: Verification
1. Re-run the `manuscript-consistency-checker` to ensure no formatting errors were introduced during the revision.

---

## 3. Running the Workflow

To start a new audit session, use the following command structure or adopt the persona:

> "As **The Deep Researcher**, perform a DeepSeek audit of Chapter [X] using the Classical Chinese source in `00_MASTER_VERSIONS`."

Once the report is ready:

> "As **The Editorial Revisionist**, implement the findings from the Chapter [X] Audit Report into the scholarly manuscript."
