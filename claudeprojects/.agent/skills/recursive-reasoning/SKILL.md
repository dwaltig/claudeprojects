---
description: >-
  Enables "Recursive Language Model" (RLM) capabilities. Allows the agent to
  load large contexts into a Python REPL, interact with them programmatically,
  and recursively call an LLM to process sub-chunks. Use this for "Inference
  Time Reasoning" on large files or complex tasks that require decomposition.
---

# Recursive Reasoning Skill

This skill allows you to transcend your fixed context window by using an "Inference Time Reasoner" scaffold. Instead of reading a massive file directly, you load it into a Python environment and manipulate it via code.

## When to Use
*   **Large Files**: When a file is too big to fit in your context window (or would cause "context rot").
*   **Complex Analysis**: When you need to iterate, filter, or transform data before processing it.
*   **Recursive Decomposition**: When a task requires splitting a problem into chunks and processing each chunk separately.

## How to Use

### 1. Start the Reasoner
Run the scaffold script pointing to your target file:
```bash
python3 scripts/inference_time_reasoner.py --context "path/to/large_file.txt"
```

### 2. Interact via REPL
The script opens a Python REPL. You **MUST** use the `send_command_input` tool to interact with it.
**DO NOT** use `run_command` for subsequent interactions; the process is already running.

#### Available Variables:
*   `CONTEXT` (str): The full content of the loaded file.
*   `llm_query(task, content, depth=0, max_depth=3)`: A function that calls a sub-agent (GPT-5.2) to process `content` with the given `task`.
    *   **Safety:** Stops automatically if `depth > max_depth` (default 3) to prevent infinite loops.
*   `inspect(variable)`: Prints type, length, and a preview of any variable.

### 3. Strategy: Divide & Conquer
1.  **Inspect**: Check `len(CONTEXT)` to see what you're dealing with.
2.  **Slice**: Create chunks using Python slicing (e.g., `chunk1 = CONTEXT[:5000]`).
3.  **Process**: Call `llm_query` on the chunks.
    ```python
    summary1 = llm_query("Summarize the key philosophical arguments", chunk1)
    ```
4.  **Synthesize**: Combine the results.
    ```python
    final_answer = llm_query("Combine these summaries into a final report", summary1 + summary2)
    print(final_answer)
    ```

## Best Practices (NotebookLM Verified)

### 1. Defensive Coding
When iterating over data chunks, **ALWAYS** use `try...except` blocks. If one chunk fails (e.g., API timeout), your entire script shouldn't crash.

```python
results = []
for chunk in chunks:
    try:
        res = llm_query("Task...", chunk)
        results.append(res)
    except Exception as e:
        print(f"Error on chunk: {e}")
        # Optionally add a placeholder or retry
```

### 2. No Placeholders
Never use placeholder text like "[Insert Data]" in your code or prompts. The REPL executes code AS-IS.

### 3. Efficient Batching
Avoid spawning thousands of microscopic `llm_query` calls. Batch your data into meaningful chunks (e.g., 5000-10000 chars) to balance granularity with API rate limits.

## Example Workflow

**User**: "Analyze the themes in this 5MB book."

**Agent**:
1.  start process: `python3 scripts/inference_time_reasoner.py --context book.txt`
2.  `send_command_input`:
    ```python
    print(len(CONTEXT))
    # Output: 5242880
    
    # Split into 5 parts (simplified logic)
    chunk_size = len(CONTEXT) // 5
    part1 = CONTEXT[:chunk_size]
    
    # Analyze part 1
    result1 = llm_query("List main themes", part1)
    print(result1)
    ```
3.  Read output from `command_status`.
4.  Repeat for other parts or refined queries.
5.  Exit: `exit()`
