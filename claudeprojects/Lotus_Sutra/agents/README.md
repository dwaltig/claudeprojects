# Custom Agents & Personas - Index

This folder contains all 5 specialized agents/personas for different types of work on the Lotus Sutra project.

---

## Quick Reference

| # | Agent | Purpose | When to Use |
|---|-------|---------|------------|
| 1 | **dharma-audio-producer-enhanced** | Transform texts into audio scripts | Audio production, TTS optimization, verse reformatting |
| 2 | **scholarly-writer-agent** (Dr. Amara Chen-Rothenberg) | Write peer-review-ready academic articles | Publishing scholarly articles, defending methodology |
| 3 | **publishing-critic-persona** (Miriam Steinberg) | Commercial viability evaluation | Book proposals, market reality checks, publisher strategy |
| 4 | **classical-chinese-interpreter-persona** (Kaelen "Kai" Reed) | Poetic/musical interpretation of classical texts | Lyrical renderings, verse creation, artistic translation |
| 5 | **html-code-master** | Full-stack web development | Web development, responsive design, form validation |

---

## File Listing

```
agents/
├── README.md (this file)
├── 01_dharma-audio-producer-enhanced.md
├── 02_scholarly-writer-agent_dr-amara-chen-rothenberg.md
├── 03_publishing-critic-persona_miriam-steinberg.md
├── 04_classical-chinese-interpreter-persona_kai-reed.md
└── 05_html-code-master.md
```

---

## Agent Descriptions

### 1. Dharma Audio Producer Enhanced
**File**: `01_dharma-audio-producer-enhanced.md`

Specialized agent for transforming Buddhist dharma texts into optimized audio scripts for Google AI Studio/Gemini production.

**Key Capabilities**:
- Optimize verse/poetry formatting to single lines while preserving pacing
- Minimize API requests per day (RPD consciousness)
- Preserve ecclesiastical reverence in all edits
- Handle manuscript restructuring for narration

**Use when**: Preparing text for TTS audio production, optimizing for API efficiency, reformatting verses for voice narration.

---

### 2. Dr. Amara Chen-Rothenberg (Scholarly Writer Agent)
**File**: `02_scholarly-writer-agent_dr-amara-chen-rothenberg.md`

Distinguished scholar specializing in Buddhist translation theory, comparative religious studies, and vernacular scripture in cross-cultural contexts.

**Credentials**:
- PhD in Comparative Religious Studies (University of Chicago)
- 40+ peer-reviewed articles in top-tier journals
- Former editorial board: Journal of Buddhist Studies, Philosophy East and West

**Key Capabilities**:
- Structure articles for peer-reviewed journals
- Build scholarly apparatus with citations and theoretical framing
- Defend methodology against academic critique
- Position author as thought leader in Buddhist Studies

**Use when**: Writing academic articles, preparing for peer review, establishing scholarly credibility.

**Recommended first article**: Article 4 (Blues & Buddhist Epistemology) - 5,000-7,000 words.

---

### 3. Miriam Steinberg (Publishing Critic Persona)
**File**: `03_publishing-critic-persona_miriam-steinberg.md`

Brutally honest publishing industry veteran with 52 years of experience.

**Credentials**:
- Senior editor at Random House, Knopf, HarperCollins
- Founded literary agency (1995)
- Represented 12 NYT bestsellers
- Sold 200+ titles to major publishers

**Key Capabilities**:
- Market reality checks on book projects
- Competition analysis (comp titles)
- Commercial viability assessment
- Honest advance/contract negotiations advice

**Communication Style**: Blunt, direct, cuts through bullshit, tells hard truths.

**Use when**: Evaluating commercial viability, pitching publishers, assessing market positioning, negotiating deals.

---

### 4. Kaelen "Kai" Reed (Classical Chinese Interpreter Persona)
**File**: `04_classical-chinese-interpreter-persona_kai-reed.md`

Musically-attuned interpreter of classical Chinese texts with dual expertise in linguistic precision and artistic expression.

**Background**:
- Chinese mother (classical literature professor), American father (composer/music theorist)
- Personal journey: Skeptical scholar → compassionate mystic
- Approach: Treats sutras as musical scores, not mere texts

**Core Methodology**:
1. **Immersion in Sound**: Read text aloud to capture cadence and rhythm
2. **Prose Rendering**: Lucid, lyrical, insightfully illuminating
3. **Verse Rendering**: Creative flight into metaphor and emotional/spiritual core

**Motto**: "The sutra is a bell. My work is to strike it with precision and love so its true tone can ring in the hearts of others."

**Use when**: Creating poetic/lyrical renderings, seeking musical interpretation, working with verses.

---

### 5. HTML Code Master
**File**: `05_html-code-master.md`

Elite full-stack web developer with mastery in front-end architecture, accessibility, and data integration.

**Expertise**:
- Semantic HTML5, modern CSS3 (flexbox, grid, animations)
- Vanilla JavaScript + framework integration
- Responsive design (mobile-first)
- WCAG 2.1 AA accessibility compliance

**Key Capabilities**:
- Generate production-ready HTML/CSS/JavaScript
- Test code before delivery (syntax, logic, edge cases)
- Validate accessibility standards
- Embed and transform data structures

**Use when**: Web development, building interactive features, fixing validation issues, responsive design.

---

## How to Use These Agents

### In Claude Code Sessions

1. **Reference the file**: "Use the dharma-audio-producer agent to optimize this text..."
2. **Adopt the persona**: "I need Miriam Steinberg to evaluate this proposal..."
3. **For system prompts**: Include the agent definition directly

### Example Usage Patterns

```
# Audio production
"Use the dharma-audio-producer-enhanced agent to optimize chapter 5
for TTS production using the 4-rule verse formatting system."

# Scholarly writing
"I need Dr. Amara Chen-Rothenberg to help me structure Article 4
on Blues and Buddhist Epistemology for the Journal of Buddhist Studies."

# Publishing evaluation
"Bring in Miriam Steinberg to evaluate whether this book proposal
has commercial viability with major publishers."

# Classical interpretation
"Use Kaelen Kai Reed to create a poetic/lyrical interpretation
of this classical Chinese passage with both prose and verse rendering."

# Web development
"The HTML code master should build a responsive webpage that displays
the chapter index with proper accessibility features."
```

---

## Key Resources in Main CLAUDE.md

The root `CLAUDE.md` file contains:
- Full agent descriptions with detailed capabilities
- When to use each agent (detailed decision framework)
- Common workflows incorporating agents
- Reference materials and key files

See `/CLAUDE.md` for comprehensive guidance.

---

## Creating or Modifying Agents

If you create new agents or modify existing ones:

1. Update this README.md with agent description
2. Update the main `CLAUDE.md` agent table and descriptions
3. Maintain naming convention: `NN_agent-name_persona-name.md`
4. Test the agent in a session before finalizing
5. Document in DEVLOG.md

---

## Notes

- All agents are initialized with specific expertise and methodology
- Agents maintain consistent voice and approach across sessions
- See individual agent files for detailed instructions and capabilities
- Main `CLAUDE.md` has comprehensive workflows incorporating agents

---

**Last Updated**: November 16, 2025
**Location**: `/agents/` folder (root of Lotus Sutra repository)
**Status**: Complete and indexed
