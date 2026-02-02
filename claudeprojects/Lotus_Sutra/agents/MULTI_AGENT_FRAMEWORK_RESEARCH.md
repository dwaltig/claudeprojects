# Multi-Agent Framework Comparative Analysis

This document catalogs 40+ multi-agent frameworks from academic research, comparing their coordination architectures, agent roles, benchmark performance, and key mechanisms.

---

## Framework Comparison Table

| Framework Name | Coordination Architecture | Agent Roles | Benchmark Accuracy (%) | Key Reasoning Mechanism | Token Management Strategy | Scalability Features | Source |
|:---|:---|:---|:---|:---|:---|:---|:---|
| CoAgt (Chain of Agents) | Hybrid | Collector Agents, Synthesizer Agent, Answer Refiner | WikiTQ: 85.4%, TabFact: 96.5% | Zero-shot chain-of-agents inspired by human cognitive steps (scanning, comparing, synthesizing) | Dynamic segmentation into chunks (approx. 1,000 tokens per agent) | Adjustable number of Collector Agents to handle arbitrarily long tables | 1 |
| MetaGPT | Hybrid, Centralized, or Hierarchical | Product Manager, Architect, Project Manager, Engineer, QA Engineer | 85.9% (HumanEval), 87.7% (MBPP), 57.14% (WP rate), 82.3 (HumanEval), 81.7 (MBPP) | Standardized Operating Procedures (SOPs), Meta-Programming, and assembly line paradigm | Global memory pool with role-based subscriptions and structured output schemas | Assembly line model with modular outputs and automated task decomposition to reduce compounded errors | 2-7 |
| EIB-LEARNER | Hybrid (Dual-view) | Summarizer, Mathematical Analyst, Math Solver, Programming Expert, Inspector, Project Manager, Algorithm Designer, Test Analyst, Bug Fixer | 88.90% (MMLU), 95.20% (GSM8K), 89.15% (HumanEval), 91.38% (Avg) | Error-Insight Balanced Learner; dual-view GNN simulators (sparse/dense) with query-aware adaptive fusion | Eliminates redundant interactions to reduce token consumption | Performance gains increase with agent count; robust against prompt injection attacks | 8 |
| Agentcoder | Decentralized | Code generator, test case creator, and test executor | 96.3% on HumanEval; 91.8% on MBPP | Test-driven development (TDD) approach with iterative refinement | Efficient token usage through refinement loops | Multi-agent-based code generation with iterative testing | 3 |
| Mapcoder | Decentralized | Retrieval, planning, coding, and debugging agents | 93.9% on HumanEval; 83.1% on MBPP | Dynamic agent traversal model based on planning confidence | Not in source | Decouples code generation for competitive problem solving | 3 |
| ARTEMIS-DA | Not in source | Not in source | WikiTQ: 80.8%, TabFact: 93.1% | In-context learning/Prompt engineering | Not in source | Not in source | 1 |
| Model Context Protocol (MCP) enabled systems | Hybrid (Centralized and Decentralized) | Ingestion, Knowledge Graph, Query Understanding, Synthesis, and Orchestration Agents | 78.3 (Cross-Domain Synthesis), 87 (Retrieval Precision@10) | Context-aware tool execution and collaborative hypothesis development | Externalized context storage, summarization, and prioritization | Client-Server architecture with O(n log n) communication scaling | 9 |
| MARS-SQL | Sequential | Grounding Agent, Generation Agent, Validation Agent | 77.84% (BIRD dev), 89.75% (Spider test) | Interactive Reinforcement Learning; ReAct-style Think-Act-Observe loop | Generates multiple interaction trajectories to explore reasoning paths | Dynamic, stateful reasoning and self-correction against a live database | 10 |
| EMRC | Specialized Ensemble | Medical Expert Agents | 74.45% (MMLU-Pro-Health) | Expertise-aware recruitment and collaboration; Confidence- and adversarial-driven fusion | Not in source | Dynamic selection of optimal LLMs based on department category and query difficulty | 10 |
| TabSQLify | Not in source | Not in source | WikiTQ: 64.7% (Overall), 57% (at ≥ 9,000 tokens) | Natural language to SQL transformation for sub-table retrieval | Retrieval of reduced sub-tables via SQL | Sub-table reasoning reduces input overflow probability | 1 |
| Chain-of-Table | Independent (Sequential) | Not in source | WikiTQ: 59.9%, TabFact: 80.2% | Step-by-step table transformation (Chain-of-Table reasoning) | Linear processing (often suffers from truncation) | Performance declines on long tables (> 4,000 tokens) | 1 |
| MIRIX | Hybrid | Coordinator, Specialized Memory Agents | 37.7 (MemoryAgentBench Avg. with GPT-4.1-mini) | Multi-agent memory orchestration across 6 specialized types | Top-k retrieval-based context selection | Multi-agent memory architecture | 11 |
| Orchestrator | Centralized | Planning Node, Execution Node, Orchestration Node | 100.0 (Medium Maze), 76.67 (Hard Maze) | Active Inference (Surprise minimization/Information gain) | Iterative n-step decision cycles with real-time feedback | Modular cell-structured graph design | 12 |
| LatentMAS | Sequential | Planner, Critic, Refiner, Solver | 14.6% higher than baselines | Pure latent collaboration within continuous latent space; auto-regressive latent thoughts generation | Shared latent working memory; reduces output token usage by 70.8%-83.7% | Training-free framework; 4x-4.3x faster end-to-end inference | 10 |
| DATER | Not in source | Not in source | TabFact: 93.0% | Decomposition-and-Integration | Not in source | Not in source | 1 |
| AutoGen | Centralized, Decentralized, or Hybrid | Assistant, User Proxy, Specialist, Coordinator, Planner, Executor, Manager, Critic, Reviewer | Not in source | Multi-agent conversation programming, reflection, and event-driven architecture | Management of conversational history and message turns | Asynchronous messaging, modular design, and distributed systems support | 3, 4, 14-19 |
| LangGraph | Centralized, Hybrid, or Hierarchical (Stateful Graph) | Nodes (LLM calls, tools), Supervisor, Subordinate agents | Not in source | Stateful workflows, cyclic graph control flow, and human-in-the-loop | GraphState management with centralized context | Modular architecture, state persistence, and high control flow determinism | 3, 14, 20 |
| CrewAI | Hybrid, Decentralized, or Independent | Role-playing agents (Researcher, Writer, Manager, etc.) with specific goals | Not in source | Role-based design, autonomous delegation, and modular task workflows | Task Outputs / Crew Context / Flows | Horizontal scaling via distributed messaging queues and autonomous manager agents | 3, 20, 21 |
| AgentVerse | Decentralized | Expert Recruitment, Decision-Making, Execution, and Evaluation roles | Not in source | Group dynamics and task-oriented collaborative decision-making | Shared message pools | Dynamic interaction and expert recruitment stages | 3, 15 |
| SLEUTH | Centralized (Orchestrated) | Retriever, Textual/Visual clue identifying, Salient evidence filtering, Query analyzer, Synthesizer | Not in source | Hierarchical refinement; coarse-to-fine process identifying clues across modalities | Synthesizes a distilled, evidence-dense multimodal context | Model agnostic and scalable for long document benchmarks | 10 |
| Chain-of-Agents (CoA) | Sequential or Decentralized | Worker, Manager, Planner, Critic, Refiner, Solver | Not in source | Sequential collaboration; decomposes reasoning into communicating worker and manager agents | Divides context into smaller segments handled by worker agents | Enables collaboration on tasks surpassing single-model token limits | 10, 22 |
| ChatDev | Centralized | Software Engineer, CTO, CEO, Designer, Tester, Reviewer | Not in source | ChatChain (dual-agent communication) and Communicative Dehallucination | Not in source | MacNet acyclic graphs to coordinate 1000+ agents | 23 |
| Reflexion | Independent (Self-correcting) | Self-critique Agent | Not in source | Self-reflection on execution traces and learning from mistakes | Memory storage of reflections for future context | Iterative self-improvement without retraining | 24 |
| A-Mem | Independent | Memory Evolution Agent | Not in source | Zettelkasten-inspired dynamic linking and memory evolution | Selective top-k retrieval (85-93% reduction) | Linear space complexity O(N); embedding-based retrieval filter | 25 |
| MemGPT | Independent | Not in source | Not in source | Virtual context management (RAM/Disk hierarchy) | Paging between main and external context | Dual-tier context hierarchy | 11, 25 |
| XAgent | Centralized | PlanAgent (outer loop) and ToolAgents (inner loop) | Not in source | Dual-loop architecture for task planning and execution | Not in source | Task Execution Graph (TEG); autonomy and safety | 3 |
| ReWOO | Independent (Modular) | Planner, Worker, Solver | Not in source | Reasoning Without Observation (Planning ahead) | Not in source | Subtask allocation to specific workers | 26 |
| MAC-SQL | Centralized (Hierarchical) | Planner, Retriever, Executor, Evaluator, Response Generator Agent | Not in source | Hierarchical SQL-based query processing | Sub-table retrieval via SQL | Optimized for large-scale databases | 1 |
| TaskWeaver | Centralized | Planner, Data Retriever, Code Generator | Not in source | Multi-agent planning and code generation | Not in source | Integration of retrieval and execution | 19 |
| Tree-of-Thought (ToT) | Independent (Branching) | Critic (Evaluation) | Not in source | Branching, Search (BFS/DFS), Backtracking, and Evaluation | Not in source | Exploration of multiple reasoning paths | 24 |
| CAMEL | Independent | Task-specific Agent, User Proxy, Assistant | Not in source | Role-playing autonomous cooperation | Role-based conversations | Predefined inception prompts for task completion | 15 |
| AutoGPT | Independent | Planners, Coders | Not in source | Shared Memory (Artifact-centric) | File system or Knowledge Base artifacts | Autonomous Scaling; iterative refinement; IAC protocol | 20 |
| Language Agent Tree Search (LATS) | Independent (Tree structure) | State Evaluator | Not in source | Monte Carlo Tree Search, Self-reflection, and State Evaluation | Not in source | Complex task handling in coding and QA | 26 |
| ReAct | Independent or Sequential | Reasoning and Acting Agent | Not in source | Thought-Action-Observation loop (Reason + Act) | Not in source | Tool calling for external information retrieval | 24, 26 |
| MATSA | Not in source | Table Segmentation Agent, Attribute Validation Agent, Answer Synthesis Agent | Not in source | Decomposition strategy for long structured tables | Table segmentation | Handles tables with hundreds or thousands of rows | 1 |
| CoAct | Hierarchical | Global planning agent and local execution agent | Not in source | Task decomposition and adaptive replanning | Not in source | Global-local hierarchy for autonomous agent collaboration | 3 |
| MAD (Multi-Agent Debate) | Decentralized | Adversarial debaters | Not in source | Multi-agent debate to challenge assumptions and uncover flaws | Not in source | Encouraging divergent thinking in LLMs | 3 |
| Consensus-LLM | Decentralized | Not in source | Not in source | Consensus-seeking and negotiation | Dialogue for negotiation and alignment | Consensus strategies for network topology | 15 |

---

## Our MAS: Framework Alignment

Our Multi-Agent System draws from several of these frameworks:

| Our Component | Inspired By | Key Mechanism Adopted |
|:---|:---|:---|
| **Orchestrator** | MetaGPT, XAgent | SOPs + Hierarchical Task Decomposition |
| **The Professor** | Reflexion | Self-critique loop (Draft → Critique → Refine) |
| **The Bluesman** | ReAct | Thought-Action-Observation interleaving |
| **Dr. Amara** | Tree-of-Thought | Branching argument paths with evaluation |
| **Digital Archivist** | A-Mem | Zettelkasten-inspired memory evolution |
| **Reliability Guardian** | MTTR-A (original) | Cognitive recovery optimization |
| **Crew Structure** | CrewAI, ChatDev | Role-based crews with domain specialization |

---

## Key Architectural Patterns

### 1. Coordination Architectures
- **Centralized**: Single orchestrator (MetaGPT, ChatDev, XAgent)
- **Decentralized**: Peer-to-peer collaboration (AgentVerse, MAD)
- **Hybrid**: Flexible depending on task (AutoGen, CrewAI)
- **Hierarchical**: Manager-worker relationships (CoAct, MAC-SQL)

### 2. Reasoning Mechanisms
- **Reflexion**: Self-correction through execution trace analysis
- **ReAct**: Interleaved reasoning and acting with observation
- **Tree-of-Thought**: Branching exploration with backtracking
- **SOPs**: Standardized workflows reducing compounded errors

### 3. Memory Strategies
- **A-Mem**: Zettelkasten-style atomic notes with dynamic linking
- **MemGPT**: Virtual context management (RAM/Disk paging)
- **Shared State**: Global memory pools with role-based access

## Axiological Alignment Strategies (The "Why" Factor)

While most frameworks optimize for *efficiency* or *accuracy*, our MAS introduces a novel layer: **Axiological Alignment.** This addresses the **"Axiological Gap"**—the fact that AI agents optimize for statistical correctness rather than existential liberation.

### 1. The Broken Heart Metric
*   **Agent:** The Bluesman (Axiological Regulator)
*   **Mechanism:** Explicitly prioritizes "cracked" authenticity over clinical perfection. Rejects outputs that lack affect.
*   **Concept:** Counteracts the "smoothness" bias of RLHF models.

### 2. The *Ke* Protocol (Provisionality Tagging)
*   **Agent:** Orchestrator
*   **Mechanism:** Tags initial academic drafts as `[PROVISIONAL VECTOR FIELD]`.
*   **Concept:** Prevents the system from mistaking "Identity in Names" (intellectual accuracy) for "Realization."

### 3. Simulated Anxiety Injection
*   **Agent:** Orchestrator
*   **Mechanism:** Injects high-stakes existential context into prompts (e.g., "Translate as if saving a life").
*   **Concept:** Simulates the "Urgency of Samsara" to force the model into higher-order "Subtle" states.

---

**Last Updated**: December 20, 2025
