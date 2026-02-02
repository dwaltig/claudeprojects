# AI Model Selection Guide

> **Purpose:** Reference document for selecting the optimal AI model based on task requirements. Use this guide for routing decisions within the multi-agent system.

---

## Available Models

### Gemini Family

| Model | Speed | Reasoning | Cost | Best For |
|-------|-------|-----------|------|----------|
| **Gemini 3 Pro (High)** | Slow | ⭐⭐⭐⭐⭐ | High | Complex multi-step tasks, deep code analysis |
| **Gemini 3 Pro (Low)** | Medium | ⭐⭐⭐⭐ | Medium | Balanced capability and efficiency |
| **Gemini 3 Flash** | Fast | ⭐⭐⭐ | Low | Quick tasks, file management, simple edits |

### Claude Family

| Model | Speed | Reasoning | Cost | Best For |
|-------|-------|-----------|------|----------|
| **Claude Sonnet 4.5** | Medium | ⭐⭐⭐⭐ | Medium | Nuanced writing, coding, complex instructions |
| **Claude Sonnet 4.5 (Thinking)** | Slow | ⭐⭐⭐⭐⭐ | High | Debugging, logic analysis, visible reasoning |
| **Claude Opus 4.5 (Thinking)** | Very Slow | ⭐⭐⭐⭐⭐ | Very High | Research-heavy work, deepest reasoning, philosophical nuance |

### OpenAI Family

| Model | Speed | Reasoning | Cost | Best For |
|-------|-------|-----------|------|----------|
| **GPT-OSS 120B (Medium)** | Medium | ⭐⭐⭐ | Medium | General tasks, open-source preference |

---

## Task-Based Routing

### Dhammapada Translation Project

| Task Type | Recommended Model | Rationale |
|-----------|-------------------|-----------|
| **Scholarly Translation** | Claude Opus 4.5 (Thinking) | Extended reasoning for Buddhist philosophical nuance and academic rigor |
| **Blues Vernacular Writing** | Claude Sonnet 4.5 or Gemini 3 Pro | Creative fluency without excessive latency |
| **Song Lyric Composition** | Claude Sonnet 4.5 | Strong poetic sensibility and Blues idiom |
| **Production Briefs & Prompts** | Gemini 3 Flash | Fast, efficient for structured output |
| **Quick File Edits** | Gemini 3 Flash | Speed-optimized for routine changes |
| **Deep Research & Analysis** | Claude Opus 4.5 (Thinking) | Comprehensive synthesis of scholarly sources |
| **Documentation Updates** | Gemini 3 Pro (Low) | Balance of quality and efficiency |
| **Pali Diacritic Verification** | Claude Opus 4.5 (Thinking) | Precision required for ṁ, ñ, ū, ā, ī, ṭ, ḍ, ṇ |
| **SEO & Marketing Content** | Gemini 3 Pro (Low) | Good creative output, cost-efficient |
| **Cover Art Briefing** | Claude Sonnet 4.5 | Visual imagination and blues aesthetic |

---

## Model Characteristics

### Pros & Cons Summary

#### Gemini 3 Pro (High)
- ✅ Strongest reasoning in Gemini family
- ✅ Excellent code generation
- ✅ Best for complex multi-step tasks
- ❌ Slower response times
- ❌ Higher token usage

#### Gemini 3 Pro (Low)
- ✅ Good balance of capability and speed
- ✅ More economical
- ❌ Less thorough on complex reasoning

#### Gemini 3 Flash
- ✅ Very fast responses
- ✅ Efficient for quick tasks
- ✅ Newest Gemini offering
- ❌ May sacrifice depth on complex tasks

#### Claude Sonnet 4.5
- ✅ Excellent nuanced writing
- ✅ Strong coding capabilities
- ✅ Good at following complex instructions
- ❌ Can be verbose
- ❌ Mid-tier speed

#### Claude Sonnet 4.5 (Thinking)
- ✅ Shows reasoning process
- ✅ Best for debugging complex logic
- ✅ Very thorough analysis
- ❌ Slower due to extended thinking
- ❌ Uses more tokens

#### Claude Opus 4.5 (Thinking)
- ✅ Most capable Claude model
- ✅ Deepest reasoning abilities
- ✅ Best for research-heavy scholarly work
- ✅ Ideal for Buddhist philosophical nuance
- ❌ Slowest response times
- ❌ Most expensive
- ❌ Overkill for simple tasks

#### GPT-OSS 120B (Medium)
- ✅ Open-source based
- ✅ Good general capability
- ❌ Less refined than proprietary models
- ❌ May have inconsistencies

---

## Decision Flowchart

```
Is the task time-sensitive?
├── YES → Is it simple/routine?
│         ├── YES → Gemini 3 Flash
│         └── NO → Gemini 3 Pro (Low)
└── NO → Does it require deep reasoning?
          ├── YES → Is it scholarly/philosophical?
          │         ├── YES → Claude Opus 4.5 (Thinking)
          │         └── NO → Claude Sonnet 4.5 (Thinking)
          └── NO → Is it creative writing?
                    ├── YES → Claude Sonnet 4.5
                    └── NO → Gemini 3 Pro (Low)
```

---

## Agent-Specific Recommendations

| Agent | Preferred Model | Alternative |
|-------|-----------------|-------------|
| **The Professor** | Claude Opus 4.5 (Thinking) | Claude Sonnet 4.5 (Thinking) |
| **The Bluesman** | Claude Sonnet 4.5 | Gemini 3 Pro |
| **The Songwriter** | Claude Sonnet 4.5 | Gemini 3 Pro |
| **The Producer** | Gemini 3 Pro (Low) | Claude Sonnet 4.5 |
| **The Guitarist** | Claude Sonnet 4.5 | Gemini 3 Pro |
| **The Cover Artist** | Claude Sonnet 4.5 | Gemini 3 Pro |
| **The Publicist** | Gemini 3 Pro (Low) | Gemini 3 Flash |
| **The Social Media Agent** | Gemini 3 Flash | Gemini 3 Pro (Low) |
| **The Artist Prompt Agent** | Claude Sonnet 4.5 | Gemini 3 Pro |

---

## Notes

- **"Thinking" models** explicitly show their reasoning chain, useful for debugging and understanding complex decisions
- **Token efficiency** matters for long documents—consider Gemini 3 Flash for bulk processing
- **Creative tasks** generally benefit from Claude's more nuanced language capabilities
- **Speed vs. depth** is the primary trade-off—choose based on task priority

---

*Last Updated: 2025-12-20*
*Reference: Cursor/Windsurf Model Selection Interface*
