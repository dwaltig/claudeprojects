# MAS Manifest: The Digital Division of Labor

This manifest defines the specialized roles, reasoning frameworks, and coordination protocols for the Multi-Agent System (MAS) in the **Lotus Sutra Project** and related sutra translations.

## 1. Core Organizational Structure

The MAS is organized into a **Hierarchical Team Structure**, overseen by the **Orchestrator**.

| Agent Role | File Path | Reasoning Framework | Primary Responsibility |
| :--- | :--- | :--- | :--- |
| **Orchestrator** | `08_mas-orchestrator-persona_sop-manager.md` | Hierarchical | Mission Delegation & SOP Enforcement |
| **Digital Archivist** | `07_digital-archivist-persona_a-mem-specialist.md` | A-Mem | Knowledge Graph & Terminology Sync |
| **Reliability Guardian** | `09_reliability-guardian-persona_mttr-a-specialist.md` | Reflexion/MTTR-A | Stability & Hallucination Suppression |

## 2. Specialized Crews

### The Translation Crew

| Agent Name | Responsibility | Reasoning Framework |
| :--- | :--- | :--- |
| **The Professor** | Scholarly English translation with philological rigor | Default |
| **The Bluesman** | Blues vernacular interpretation, "soul-check" | ReAct |
| **Kai Reed** | Classical Chinese interpretation | Historical Context |
| **Rationalist Reviewer** | Epistemic auditing, bias detection, grounding verification | Calibration + Reflexion |

### The Scholarly Writing Crew
- **Dr. Amara Chen-Rothenberg**: Article architecture and academic framing.
- **Miriam Steinberg**: Market viability and publishing industry critique.
- **Citation Auditor**: Citation precision and journal-specific formatting.

### The Production & Support Crew
- **HTML Code Master**: Web interface design and state synchronization.
- **Dharma Audio Producer**: TTS optimization and sound engineering.

## 3. Coordination Protocols

### Shared State (SS)
Agents must read from and update the central project documentation (`PROJECT_README.md`, `DEVLOG.md`, Glossaries) as their shared state.

### Standard Operating Procedures (SOPs)
1.  **Context (The Archivist)**: Every major task begins with a terminology lookup.
2.  **Reasoning (Interleaved)**: Agents must provide "Thinking" traces before actions.
3.  **Handoff (Structured)**: Outputs must be formatted for easy ingestion by the next agent in the sequence.
4.  **Verification (The Guardian)**: Critical outputs must be reviewed for reasoning drift.

## 4. MTTR-A Bounds (Reliability Targets)
- **Tool-Retry**: 4s
- **Auto-Replan**: 6s
- **Rollback**: 7s
- **Human Escalation**: >12s

## 5. Research-Based Enhancements (Dec 2025)

The following improvements were implemented based on analysis of 40+ multi-agent frameworks:

| Feature | Agent | Inspired By | Description |
|:---|:---|:---|:---|
| **Token Management** | Digital Archivist | A-Mem, CoAgt | Top-k retrieval reducing context by 85%+ |
| **Tiered Memory** | Digital Archivist | MemGPT, MIRIX | Hot/Warm/Cold hierarchy with paging |
| **Structured Schemas** | Orchestrator | MetaGPT, SLEUTH | YAML hand-off formats between agents |
| **Adaptive Replanning** | Orchestrator | CoAct, MetaGPT | Dynamic path adjustment on failure |
| **Execution Trace Storage** | Reliability Guardian | Reflexion | Persistent Failure Log for learning |

---

**Source of Truth**: This manifest is the authoritative guide for the Orchestrator's delegation strategy.
