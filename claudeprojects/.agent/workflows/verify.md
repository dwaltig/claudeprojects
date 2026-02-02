---
description: Verify any output for errors using DeepSeek Auditor
---

# /verify Workflow

Use this workflow to verify any output (translation, article, analysis) for errors using the DeepSeek Auditor Agent.

## Usage

```
/verify [content or file path]
```

## Workflow Steps

### 1. Identify the Content to Verify

Determine what needs verification:
- **File path:** If user provides a path, read that file
- **Inline content:** If user pastes content directly, use that
- **Previous output:** If user says "verify that" or "verify the last output", use the most recent AI-generated content

### 2. Determine Verification Depth

Ask or infer the verification level:
- **Quick check:** Simple outputs, drafts, general review → Use DeepSeek Chat
- **Full audit:** Final translations, scholarly articles, publication-ready work → Use DeepSeek Reasoner

Default to **Full audit** unless user specifies "quick" or content is clearly informal.

### 3. Load the Auditor Agent Context

Reference the Auditor Agent:
```
/Users/williamaltig/claudeprojects/agents/DeepSeek_Auditor_Agent.md
```

### 4. Construct the Verification Prompt

Build the prompt for DeepSeek:

```
You are The Auditor, a verification specialist. Review the following content for:

1. FACTUAL ERRORS - Wrong facts, dates, names, misattributed quotes
2. TRANSLATION ERRORS - Over-translation, under-translation, ghost characters
3. LOGICAL INCONSISTENCIES - Self-contradictions, unsupported claims
4. DOCTRINAL ERRORS - Buddhist concepts misrepresented
5. CITATION ERRORS - Misquoted sources, broken references
6. MISSED NUANCES - Subtle meanings lost

CONTENT TO VERIFY:
---
[INSERT CONTENT HERE]
---

Provide your analysis in this format:

## Confidence Score: [1-10]
Brief justification for the score.

## Issues Found
List each issue with location and description:
- [LOCATION] Issue Type: Description

## Corrections
Specific fixes for each issue.

## Verification Notes
Any caveats or limitations.
```

### 5. Call DeepSeek

// turbo
For **Full audit**, use DeepSeek Reasoner:
```
mcp_deepseek-reasoner_get-deepseek-thinker
```

For **Quick check**, use DeepSeek Chat:
```
mcp_deepseek-chat_get-deepseek-thinker
```

### 6. Present Results

Format the DeepSeek response clearly:

```markdown
# Verification Report

**Content:** [file name or description]
**Verification Level:** [Quick Check / Full Audit]
**Model Used:** [DeepSeek Chat / DeepSeek Reasoner]

---

[DeepSeek's analysis]

---

## Next Steps
- [ ] Address issues listed above
- [ ] Re-verify after corrections (optional)
```

### 7. Offer Follow-up

Ask if user wants to:
- Apply the corrections automatically
- Re-verify after edits
- Save the verification report

---

## Examples

### Verify a file
```
/verify /Users/williamaltig/claudeprojects/Vimalakirti_Sutra_Project/01_TRANSLATIONS/Chapter_05_Blues.md
```

### Verify pasted content
```
/verify

The Buddha's teaching on emptiness means that nothing exists...
```

### Quick verification
```
/verify quick - just check this draft for obvious errors
```

### Verify previous output
```
/verify that
```

---

## Integration with Other Workflows

This workflow pairs well with:
- `/translate` - Verify after translation
- `/blues_dhammapada_song_*` - Verify song lyrics
- Any scholarly article workflow

---

*Workflow Created: 2025-12-30*
