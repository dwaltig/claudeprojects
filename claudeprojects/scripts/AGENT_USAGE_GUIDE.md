# Scholarly Agent MVP - Usage Guide

## What This Is

A minimal viable autonomous agent built on the same architecture as Claude Cowork. It demonstrates:

- **Autonomous task planning**: Give it a natural language prompt, it figures out what to do
- **Multi-file analysis**: Scans your entire project for patterns and issues
- **Terminology consistency checking**: Finds inconsistent spellings and capitalizations
- **Diacritical validation**: Checks UTF-8 encoding and Sanskrit marks
- **Automated reporting**: Generates actionable reports with specific recommendations

## Architecture

```
User Prompt → Planning → Execution → Verification → Report Generation
                  ↓
         [Task Decomposition]
                  ↓
         [Parallel Processing]
                  ↓
         [Result Aggregation]
```

This is the same "agentic loop" architecture used by Claude Cowork and Claude Code.

## Quick Start

### Run the Demo

```bash
# From your workspace root
python3 scripts/scholarly_agent.py
```

This will run the default demo task: "Analyze terminology consistency in Dhammapada translations"

### Run Custom Tasks

```bash
# Analyze a specific project
python3 -c "
from scripts.scholarly_agent import ScholarlyAgent
from pathlib import Path

agent = ScholarlyAgent(Path('/Users/williamaltig/claudeprojects'))
result = agent.execute_task('Analyze terminology in Lotus Sutra scholarly translations')
print(result['report'])
"
```

## Supported Task Types

### 1. Terminology Consistency Analysis

**Prompt examples:**
- "Analyze terminology consistency in Dhammapada"
- "Check term usage in Lotus Sutra scholarly versions"
- "Find inconsistent Buddhist terms across all projects"

**What it does:**
- Scans all translation files
- Extracts Buddhist terminology (Sanskrit/Pali terms, proper names, technical terms)
- Identifies variant spellings (e.g., Pali vs Pāli)
- Finds capitalization inconsistencies
- Recommends standardization

**Example output:**
```
ISSUES FOUND
--------------------------------------------------------------------------------
Total issues: 37

MEDIUM PRIORITY:
  • variant_spelling: nibbana
    Variants: Nibbāna, Nibbana
    → Standardize to most common variant: Nibbāna
```

### 2. Diacritical Validation

**Prompt examples:**
- "Check diacriticals in Dhammapada"
- "Validate Sanskrit marks in all files"
- "Find encoding errors"

**What it does:**
- Verifies UTF-8 encoding
- Checks for combining vs precomposed diacriticals
- Identifies encoding errors
- Validates Sanskrit character usage

### 3. General Analysis

**Prompt examples:**
- "What files are in the Diamond Sutra project?"
- "Analyze the Vimalakirti Sutra structure"

**What it does:**
- Scans and lists files
- Provides basic content analysis

## Understanding the Output

### Console Output

Real-time execution log showing:
```
[13:27:14] 🤖 Agent activated with task: ...
[13:27:14] 📋 Created plan with 5 steps
[13:27:14] 🔍 Starting terminology analysis...
[13:27:14] 📁 Found 224 files to analyze
[13:27:14] 📚 Extracted 4083 unique terms
[13:27:14] ⚠️  Found 37 potential issues
```

### Generated Files

**agent_report.txt**: Human-readable report
- Summary statistics
- Prioritized issues
- Top terms by frequency
- Verification status

**agent_output.json**: Machine-readable data
- Execution plan
- Detailed results
- Execution log
- Raw data for further processing

## Project Detection

The agent automatically detects which project to analyze from your prompt:

| Keyword in Prompt | Projects Scanned |
|-------------------|------------------|
| "dhammapada" | Dhammapada/ |
| "lotus" | Lotus_Sutra/ |
| "diamond" | Diamond Sutra Project/ |
| "surangama" | Surangama Sutra/ |
| "vimalakirti" | Vimalakirti_Sutra_Project/ |

**Refine with file types:**
- "scholarly" → Only `*Scholarly*.md` files
- "blues" → Only `*Blues*.md` files

## Real Issues Found in Your Workspace

The agent found these actual inconsistencies in your Dhammapada translations:

1. **Pāli vs Pali** (diacritical inconsistency)
2. **Nibbāna vs Nibbana** (should always use diacritical)
3. **Theravāda vs Theravada** (diacritical inconsistency)
4. **Appamāda vs Appamada** (diacritical inconsistency)
5. **Sūtra vs Sutra** (inconsistent throughout)

These are actionable findings you can fix now!

## Extending the Agent

### Add New Skills

```python
def _execute_glossary_generation(self, plan: Dict) -> Dict:
    """New skill: Generate glossary from terms"""
    files = self._scan_files(plan['scope'])
    terms = {}

    for file_path in files:
        # Extract terms and definitions
        # Your custom logic here
        pass

    return {'glossary': terms}
```

### Add New Task Types

```python
# In _create_plan method
elif "glossary" in prompt.lower():
    return {
        'task_type': 'glossary_generation',
        'steps': [
            {'id': 1, 'action': 'scan_files', 'target': 'translation_files'},
            {'id': 2, 'action': 'extract_terms', 'target': 'buddhist_terms'},
            {'id': 3, 'action': 'extract_definitions', 'target': 'footnotes'},
            {'id': 4, 'action': 'generate_glossary', 'target': 'hybrid_glossary'},
            {'id': 5, 'action': 'format_output', 'target': 'markdown_glossary'}
        ],
        'scope': self._detect_scope(prompt)
    }
```

## Comparison to Claude Cowork

| Feature | Scholarly Agent (MVP) | Claude Cowork (Production) |
|---------|----------------------|---------------------------|
| Architecture | Same agentic loop | Same agentic loop |
| Planning | Pattern-based (simple) | LLM-powered (sophisticated) |
| File access | Full workspace | Sandboxed folder |
| Background tasks | No (runs synchronously) | Yes (queue and walk away) |
| Skills | 2 built-in | Many built-in + extensible |
| UI | CLI | Desktop app GUI |
| Security | Trust-based | VM-isolated |

## Upgrading to Production Quality

To make this production-ready like Cowork:

1. **Use Claude API for planning**: Replace pattern matching with intelligent task decomposition
2. **Add background execution**: Implement async task queue
3. **Add more skills**:
   - Glossary generation
   - Format conversion (MD → DOCX → EPUB)
   - Citation validation
   - Cross-reference checking
4. **Add GUI**: Wrap in desktop app
5. **Add sandboxing**: Run in isolated environment
6. **Add persistence**: Save agent state between runs

## Performance

**Test run results:**
- Files analyzed: 224
- Terms extracted: 4,083 unique (130,451 total occurrences)
- Issues found: 37
- Execution time: <1 second

This demonstrates the agent can handle real-world scholarly workloads efficiently.

## Troubleshooting

### No files found
- Check that the project name in your prompt matches folder names
- Verify workspace path is correct
- Try being more specific: "Analyze Dhammapada scholarly translations"

### Too many false positives
- The term extraction is intentionally broad for MVP
- Refine the regex patterns in `_extract_buddhist_terms` for your needs

### Want different analysis
- Add new task types in `_create_plan`
- Implement custom execution methods
- Customize report format in `_generate_report`

## Next Steps

**Immediate value:**
1. Review the 37 issues found in Dhammapada
2. Standardize diacritical usage
3. Run on other projects (Lotus Sutra, etc.)

**Short-term expansion:**
1. Add glossary generation skill
2. Add format conversion skill
3. Add citation validation

**Long-term evolution:**
1. Integrate Claude API for intelligent planning
2. Add background task execution
3. Build custom skills for your specific workflow
4. Consider GUI wrapper

## Questions?

This is a minimal viable agent that demonstrates the core concepts. It's fully functional and already finding real issues in your work.

What would you like to add next?
- Glossary generation?
- Format conversion?
- Citation validation?
- Something else?

---

**Built in**: ~1 hour
**Lines of code**: ~600
**Dependencies**: Python 3 standard library only
**Inspired by**: Claude Cowork (January 2026)
