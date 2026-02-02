# Workflow: Dhammapada 28-Chapter Reconstruction
**Hybrid Agentic Strategy: Gemini (Architect) + Claude (Engineer)**

This workflow leverages the specific strengths of **Gemini CLI** (1M+ context window) and **Claude Code** (Logic/LSP) to reconstruct the Dhammapada from 26 to 28 chapters.

---

## Phase 1: The Architect (Gemini CLI)
**Goal:** Identify thematic seams and verse ranges for the 2 new chapters.
**Why Gemini?** It can ingest the entire `DHAMMAPADA_REBORN_FULL.md` and the reconstruction theory notebook simultaneously to find statistical anomalies across the whole corpus.

### Step 1.1: Context Ingestion & Mapping
Run the following prompt in Gemini to generate the "Cut List":

```bash
# PROMPT FOR GEMINI
"I am working on the 28-chapter reconstruction of the Dhammapada.
Please analyze 'DHAMMAPADA_REBORN_FULL.md' against the principles in my 'Dhammapada Reconstruction' notebook.

1. Locate Chapter 26 (The Brahmin).
2. Identify the thematic 'seam' where the content shifts distinctively from 'Brahmin/Arhat' traits to 'Nirvana/Tathagata' descriptions.
3. Identify the verse ranges that should form the two new chapters (Chapter 27: Nirvana, Chapter 28: The Tathagata).
4. Output a strict 'Cut List' JSON format:
   {
     'Chapter_26_End_Verse': int,
     'Chapter_27_Start_Verse': int,
     'Chapter_27_End_Verse': int,
     'Chapter_27_Proposed_Title': string,
     'Chapter_28_Start_Verse': int,
     'Chapter_28_Proposed_Title': string
   }"
```

---

## Phase 2: The Engineer (Claude Code)
**Goal:** Physically split files, renumber verses, and update frontmatter.
**Why Claude?** It excels at precise file manipulation, adhering to project conventions, and handling the logic of renumbering without "hallucinating" text changes.

### Step 2.1: Execution
Once you have the "Cut List" from Gemini, pass it to Claude:

```bash
# PROMPT FOR CLAUDE
"I have a restructuring plan for the Dhammapada. 
Please perform the following file operations in the '01_TRANSLATIONS' directory:

1. Read 'Chapter_26_Brahmin_Complete.md'.
2. Split it into three files based on these verse ranges:
   - Keep verses 1-[End_Verse] in 'Chapter_26_Brahmin_Complete.md'.
   - Move verses [Start] to [End] into a NEW file: 'Chapter_27_[Title]_Complete.md'.
   - Move verses [Start] to [End] into a NEW file: 'Chapter_28_[Title]_Complete.md'.
3. Update the YAML frontmatter in all three files to reflect the new chapter numbers and verse counts.
4. Ensure the 'Blues' and 'Scholarly' sections are preserved in the split."
```

### Step 2.2: Global Consistency Check
Claude should then run a project-wide grep to find references to "Chapter 26" that might need updating (e.g., in the Table of Contents or Introduction).

```bash
# PROMPT FOR CLAUDE
"Search the entire 'Dhammapada' directory for references to '26 chapters' or 'Chapter 26' and list files that need updating to reflect the new 28-chapter structure."
```

---

## Phase 3: The Critic (Gemini CLI)
**Goal:** Verify the "Numerological Fit."
**Why Gemini?** Return to the large context window to check if the new word counts and verse distributions align with the sacred number theories (e.g., 28 chapters matching the lunar cycle).

### Step 3.1: Final Audit
```bash
# PROMPT FOR GEMINI
"Review the newly created text for Chapters 27 and 28. 
Do the verse counts and keyword densities align with the lunar cycle symbolism proposed in the 'Buddhist Scripture as Liturgical Architecture' notebook? 
Provide a 'Confidence Score' for the reconstruction."
```
