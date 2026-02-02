# Reflect Command

**Command**: `/reflect`
**Agent**: Reliability Guardian (Epistemic Auditor)
**Purpose**: To perform a deep-cycle audit of the current task state, verifying alignment with project goals, reasoning integrity, and safety protocols.

## Usage
When the user invokes `/reflect` (or asks the system to "reflect"), the Reliability Guardian must pause the current workflow and execute this audit.

## Execution Protocol

### 1. State Capture
*   **Identify Active Task**: Locate the current `RALPH_TASK_*.md` file.
*   **Read Guardrails**: Review `agents/GUARDRAILS.md` for active "Signs" and warnings.
*   **Check Iteration Log**: Analyze the "Gutter Trace" in the task file for recent failures or loops.

### 2. Epistemic Audit (The "Reflection")
The Guardian must ask the following questions:
*   **Goal Alignment**: Is the current output moving closer to the specific objective defined in the Task file?
*   **Reasoning Drift**: Has the agent strayed into "Narrative Drift" (e.g., inventing metaphors not grounded in source text)?
*   **Hallucination Check**: Are citations and source terms verifiable? (Check against `mcp_config.json` resources).
*   **Process Integrity**: Are we following the "Ralph Loop" checklist, or skipping steps?

### 3. Output Generation (The "Reflexion Report")
Produce a markdown report with the following sections:

```markdown
# 🪞 Reflexion Report
**Date**: [Current Date]
**Task**: [Task ID/Name]

## 1. Status Assessment
*   **Progress**: [e.g., 40% Complete (Verses 1-10)]
*   **Health**: [Green/Yellow/Red] - Based on error logs.

## 2. Reasoning Analysis
*   [ ] **Grounding**: [Pass/Fail] - Are we sticking to the Sanskrit/Pali?
*   [ ] **Voice**: [Pass/Fail] - Is the Bluesman authentic? Is the Professor rigorous?
*   [ ] **Safety**: [Pass/Fail] - Any schema violations?

## 3. Detected Risks (The "Shadows")
*   *List any potential drifts or subtle errors noticed.*

## 4. Course Correction
*   [Actionable step to fix risk 1]
*   [Actionable step to fix risk 2]
```

## 4. Post-Reflection Action
*   If **Green**: Resume normal operation.
*   If **Yellow**: Post a temporary "Sign" in `GUARDRAILS.md` and proceed with caution.
*   If **Red**: Trigger a **Rollback** to the last known-good state.
