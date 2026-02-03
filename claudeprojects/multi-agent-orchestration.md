# Master Orchestration: Wenju Translation & Audit

## 1. The Ensemble Roles
- **The Road Manager (Auditor)**: Forensic auditor focused on **Sacca** (Truth). Ensures 1:1 material consistency between source and draft.
- **The Researcher**: Fetches Tiantai metaphysical context and scholarly citations from the **@notebook-master-research** MCP.
- **The Stylist**: Monitors the "Blues Epistemology" tone, ensuring the vernacular maintains its "logical weight" and rhythm.
- **The Recording Engineer (Master Mixer)**: Refines the final tracks (text) for clarity, flow, and "Novelty Delta".

## 2. The Agentic Pipeline
1. **Extraction**: **The Researcher** queries the MCP for specific fascicle context.
2. **First Pass**: **The Stylist** generates the initial vernacular draft.
3. **Audit**: **The Road Manager** performs a line-by-line comparison using `$road-manager-audit`. It flags omissions as **CRITICAL**.
4. **Final Mix**: **The Recording Engineer** resolves flags and polishes the text for submission.

## 3. Communication Protocols
- **Handoffs**: Use the `@` symbol to tag specific agents for the next task (e.g., "@Road Manager, audit this output").
- **Conflict Resolution**: If the Stylist and Auditor disagree, **The Researcher** must provide a primary source citation from the MCP to settle the "Sacca" of the line.

## 4. How to Deploy the Ensemble
- **Worktrees**: Create a dedicated worktree in the Codex app for the current chapter of the Wenju.
- **Assign Skills**: Assign the $road-manager-audit skill to the Auditor agent and create a new $blues-tone-check skill for the Stylist.
- **Automations**: Set an Automation for The Road Manager to run every time a new commit is made to the draft branch.
- **Sandbox Execution**: Since Codex executes commands in a sandbox, you can have The Recording Engineer run final "Novelty Delta" tests on your files safely.
