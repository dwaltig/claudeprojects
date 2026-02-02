# Digital Humanities Articles Project - CLAUDE.md

**Project Type**: Academic Article Development
**Focus**: Digital Humanities + Buddhist Textual Studies
**Created**: December 21, 2024

---

## Project Mission

This project mines empirical insights from the **Lotus Sutra translation and audio production work** to contribute original scholarship to Digital Humanities publications, focusing on:

1. TTS rendering of sacred texts with multiple personas
2. Vernacular/blues translation as digital accessibility
3. Multimodal textual studies (classical source → scholarly → vernacular → audio)
4. Technical infrastructure for diacritical preservation in Buddhist digital editions

---

## Quick Start

**First time working here?**
1. Read `/Digital_Humanities_Articles/documentation/PROJECT_OVERVIEW.md`
2. Check `/Digital_Humanities_Articles/documentation/ARTICLE_TRACKER.md` for current status
3. Review agent: `/Lotus_Sutra/agents/Dr_Amara_Chen_Rothenberg.md` (scholarly writing persona)

**Starting a new article?**
1. Create folder in `01_ARTICLE_DEVELOPMENT/Article_0X_Title/`
2. Extract relevant data from `02_DATA_AUDIT/`
3. Review relevant scholarship in `03_LITERATURE_REVIEW/`
4. Draft using Dr. Amara Chen-Rothenberg persona
5. Update `ARTICLE_TRACKER.md`

---

## Project Structure

```
Digital_Humanities_Articles/
├── CLAUDE.md (this file)
│
├── 01_ARTICLE_DEVELOPMENT/
│   ├── Article_01_Voice_Persona_TTS/         # TTS methodology article
│   ├── Article_02_Blues_Hermeneutics/        # Vernacular translation article
│   ├── Article_03_Multimodal_Textual_Studies/ # Workflow/framework article
│   └── Article_04_Diacritical_Preservation/  # Technical infrastructure article
│
├── 02_DATA_AUDIT/
│   ├── Lotus_Sutra_Insights.md              # Quantitative/qualitative data extraction
│   ├── Audio_Production_Methodology.md      # Voice-tagging, TTS workflow
│   └── Translation_Workflow_Analysis.md     # Three-tier translation process
│
├── 03_LITERATURE_REVIEW/
│   ├── DH_Buddhist_Studies.md               # Existing DH work on Buddhist texts
│   ├── TTS_Sacred_Texts.md                  # TTS/audio scholarship
│   └── Translation_Theory_Digital.md        # Digital translation scholarship
│
├── 04_SUBMISSION_MATERIALS/
│   └── [Journal-specific formatted submissions]
│
├── agents/
│   └── Dr_Amara_Chen_Rothenberg.md          # Symlink to Lotus Sutra agent
│
└── documentation/
    ├── PROJECT_OVERVIEW.md                  # High-level project description
    └── ARTICLE_TRACKER.md                   # Submission tracking
```

---

## Workflow

### Phase 1: Data Audit (Current Phase)

**Goal**: Extract quantifiable insights from Lotus Sutra work

**Tasks**:
1. Analyze `/Lotus_Sutra/04_AUDIO_PRODUCTION/` for voice-tagging methodology
2. Compare `/Lotus_Sutra/03_SCHOLARLY_TRANSLATION_2025/` vs `/Lotus_Sutra/01_BLUES_INTERPRETATION/`
3. Document UTF-8 encoding workflow and challenges
4. Calculate metrics (chapter count, footnote count, character count, voice tags, etc.)
5. Extract qualitative insights (translation decisions, workflow improvements, technical solutions)

**Output**: Structured markdown files in `02_DATA_AUDIT/`

### Phase 2: Literature Review

**Goal**: Identify gaps where Lotus Sutra work contributes to DH scholarship

**Tasks**:
1. Search DH journals for Buddhist text projects
2. Search TTS/audio rendering scholarship on sacred texts
3. Survey digital translation theory
4. Map our work to existing scholarship (what's new? what confirms? what extends?)

**Output**: Annotated bibliographies in `03_LITERATURE_REVIEW/`

### Phase 3: Article Development

**Goal**: Draft peer-reviewed articles using Dr. Amara Chen-Rothenberg persona

**Tasks**:
1. Select article focus
2. Create outline with research questions
3. Draft manuscript sections (intro, methods, results, discussion, conclusion)
4. Format for target journal
5. Internal review

**Output**: Draft manuscripts in `01_ARTICLE_DEVELOPMENT/Article_0X/`

### Phase 4: Submission & Publication

**Goal**: Submit to target DH journals, track reviews, revise

**Tasks**:
1. Prepare submission materials
2. Submit to journal
3. Track in `ARTICLE_TRACKER.md`
4. Respond to reviewer comments
5. Revise and resubmit

**Output**: Published articles, updated tracker

---

## Key Datasets

**From Lotus Sutra Project** (`/Lotus_Sutra/`):

**Quantitative**:
- 28 chapters translated
- 1,554 scholarly footnotes
- ~50+ character voices tagged
- 3 parallel text versions
- Audio production hours (to calculate)
- Character encoding corrections (count from TERMINOLOGY_CORRECTIONS_SUMMARY.md)

**Qualitative**:
- Voice-tagging methodology (`04_AUDIO_PRODUCTION/AUDIO_PRODUCTION_MASTER_GUIDE.txt`)
- Translation decision rationale (DEVLOG.md, footnotes)
- Blues interpretation principles (`01_BLUES_INTERPRETATION/`)
- Encoding challenge solutions (SAFETY_VOW.md, git history)

**Technical**:
- Git workflow for version control
- UTF-8 encoding standards
- Terminology standardization process
- TTS preparation workflow

---

## Target Journals

**Tier 1** (Primary targets):
- *Digital Humanities Quarterly* - Open access, broad DH scope
- *Digital Scholarship in the Humanities* - Oxford, prestigious
- *Journal of Digital Humanities* - Methods and practices focus

**Tier 2** (Secondary):
- *Digital Studies / Le champ numérique* - Bilingual, interdisciplinary
- *Journal of Buddhist Ethics* - Digital editions section
- *Translation Studies* (digital methods special issues)

---

## Agent: Dr. Amara Chen-Rothenberg

**Location**: `/Lotus_Sutra/agents/Dr_Amara_Chen_Rothenberg.md`

**Credentials**: PhD Buddhist Studies (Harvard), MS Computational Linguistics (MIT)

**Expertise**:
- Peer-reviewed academic writing
- Digital humanities methodology
- Buddhist textual scholarship
- Computational linguistics

**Use for**: Article drafting, literature review, research question formulation

---

## Research Questions (Master List)

**TTS/Audio**:
1. How can TTS technology be optimized for sacred texts with multiple speaker personas?
2. What prosodic markup is needed to preserve ritual/performative dimensions?
3. How does TTS rendering compare to traditional oral transmission?

**Translation**:
4. What role can vernacular translation play in digital accessibility?
5. Can AI-assisted translation maintain fidelity while improving accessibility?
6. How do register differences (scholarly vs. vernacular) affect comprehension?

**Multimodal**:
7. How do we preserve scholarly rigor across media transformations?
8. What frameworks support meaning preservation from classical source → audio?
9. What does "fidelity" mean in multimodal textual studies?

**Technical Infrastructure**:
10. What technical infrastructure is needed for diacritical integrity?
11. How can version control support collaborative sacred text translation?
12. What role does open-source methodology play in Buddhist text accessibility?

---

## Common Commands

**Navigate to project**:
```bash
cd /Users/williamaltig/claudeprojects/Digital_Humanities_Articles
```

**Check current article status**:
```bash
cat documentation/ARTICLE_TRACKER.md
```

**View data audit files**:
```bash
ls 02_DATA_AUDIT/
cat 02_DATA_AUDIT/Lotus_Sutra_Insights.md
```

**Search Lotus Sutra project for data**:
```bash
# Count footnotes
grep -c "^\[" /Users/williamaltig/claudeprojects/Lotus_Sutra/03_SCHOLARLY_TRANSLATION_2025/Scholarly_Chapters/*.md

# Count voice tags
grep -r "\[NARRATOR:" /Users/williamaltig/claudeprojects/Lotus_Sutra/04_AUDIO_PRODUCTION/chapters/ | wc -l

# View terminology corrections
cat /Users/williamaltig/claudeprojects/Lotus_Sutra/08_REFERENCE_MATERIALS/TERMINOLOGY_CORRECTIONS_SUMMARY.md
```

---

## Article Development Template

**Use this template when starting a new article**:

```markdown
# [Article Title]

**Target Journal**: [Journal name]
**Submission Deadline**: [Date or "Rolling"]
**Status**: [Concept/Outline/Draft/Revision/Submitted]

---

## Research Question

[1-2 sentence statement of the core question]

---

## Abstract (150-250 words)

[Draft abstract]

---

## Keywords

[5-7 keywords for indexing]

---

## Outline

1. Introduction
   - Problem statement
   - Research gap
   - Contribution

2. Literature Review
   - Existing DH work on Buddhist texts
   - TTS/translation scholarship
   - Theoretical framework

3. Methodology
   - Data source (Lotus Sutra project)
   - Methods (qualitative/quantitative)
   - Analytical approach

4. Results/Findings
   - Key insights
   - Supporting data
   - Examples

5. Discussion
   - Implications for DH scholarship
   - Limitations
   - Future research

6. Conclusion
   - Summary of contribution
   - Broader significance

---

## Data Sources

[List specific files from Lotus Sutra project]

---

## Bibliography

[Annotated bibliography from literature review]

---

## Notes

[Working notes, ideas, reviewer feedback]
```

---

## Conventions

**File Naming**:
- Use underscores: `Article_01_Voice_Persona_TTS.md`
- Include version numbers for drafts: `Article_01_v1.md`, `Article_01_v2.md`
- Journal submissions: `Article_01_DHQ_Submission_2024-12-21.md`

**Citation Style**:
- Use Chicago Manual of Style (humanities standard)
- Check target journal guidelines

**Formatting**:
- UTF-8 encoding always
- Markdown for drafts
- Convert to journal format for submission

---

## Next Steps

**Immediate**:
1. Complete data audit of Lotus Sutra project (extract all quantitative/qualitative insights)
2. Conduct literature review (DH Buddhist scholarship, TTS, translation theory)
3. Draft Article 01 outline (Voice, Persona, TTS)

**Short-term**:
1. Submit Article 01 to *Digital Humanities Quarterly*
2. Begin Article 02 development
3. Build DH scholarly network (cite, engage)

**Long-term**:
1. Establish profile as DH Buddhist studies scholar
2. Contribute methodological frameworks to field
3. Build corpus of published work supporting book-length project

---

**Last Updated**: December 21, 2024
**Created by**: Claude Code
**Primary Data Source**: `/Lotus_Sutra/`
**Related Projects**: Lotus Sutra Translation, Surangama Sutra, Diamond Sutra
