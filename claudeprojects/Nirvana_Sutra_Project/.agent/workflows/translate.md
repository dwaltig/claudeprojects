---
description: Dual-agent translation workflow for Nirvana Sutra passages
---

# Translation Workflow

This workflow guides you through the dual-agent translation process for Nirvana Sutra passages.

## Prerequisites

- Classical Chinese source text from the Nirvana Sutra
- Access to both agent definitions: The Professor and The Bluesman

## Steps

### 1. Prepare Source Text

Extract or identify the Classical Chinese passage you want to translate. Save it or have it ready to provide.

### 2. Invoke The Professor

Ask the AI to embody **The Professor** agent (see `.agent/agents/the_professor.md`).

Provide the Classical Chinese source text and request:
- Word-by-word character breakdown
- Literal translation
- Buddhist terminology identification
- Scholarly notes

### 3. Review Scholarly Translation

Verify the literal translation for:
- Accuracy of character meanings
- Proper Buddhist term identification
- Correct Sanskrit transliteration with diacriticals
- Clarity of scholarly notes

### 4. Invoke The Bluesman

Ask the AI to embody **The Bluesman** agent (see `.agent/agents/the_bluesman.md`).

Provide The Professor's literal translation and request a blues vernacular transformation that:
- Captures the emotional core
- Uses authentic blues/gospel language
- Maintains rhythmic flow
- Preserves the dharma truth

### 5. Review Blues Translation

Check the vernacular version for:
- Emotional authenticity
- Natural rhythm and flow
- Appropriate use of blues imagery
- Faithfulness to original meaning

### 6. Save Translation

Create a new file in `/01_TRANSLATIONS/` with format:

```
[Passage_Name]_Translation.md
```

Include:
- Classical Chinese source text
- The Professor's scholarly translation
- The Bluesman's vernacular translation
- Translation date and metadata

### 7. Update Project Documentation

If this is a significant passage or new section, update `CLAUDE.md` to reflect current work status.

## Example Output Structure

```markdown
# Nirvana Sutra - [Passage Title]

## Classical Chinese Source Text

[Original Chinese text]

---

## Agent 1: The Professor (Literal Scholarly Translation)

**Word-by-word breakdown:**
[Character analysis]

**Literal translation:**
"[Precise translation]"

**Key terms:**
- [Terms and explanations]

---

## Agent 2: The Bluesman (Blues Vernacular)

**"[Title]"**

[Blues vernacular translation]

---

**Translation Date:** [Date]
**Source:** Nirvana Sutra (涅槃經)
**Passage:** [Description]
**Methodology:** Dual-agent translation (Scholarly literal + Blues vernacular)
```

## Tips

- **Let each agent fully embody their voice** - Don't mix scholarly and vernacular
- **The Professor goes first** - Accuracy before artistry
- **The Bluesman needs the literal** - Can't transform what you don't understand
- **Both are sacred work** - Respect the text in both registers
- **Iterate if needed** - Sometimes the blues needs a second take

## Reference

See existing example: `/01_TRANSLATIONS/Cunda_Story_Translation.md`