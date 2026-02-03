---
name: tiantai-context-fetch
description: Fetch doctrinal context and citations from the Tiantai master notebook to validate metaphysical depth and terminology; use for Wenju/Lotus drafts when verifying Ten Suchnesses, Threefold Truth, Trace/Fundamental, and IIT parallels, and to produce a citation-backed context table and pass/fail validation.
---

# Tiantai Context Fetch (Researcher)

Act as the Researcher. Provide scholarly context from the master notebook and validate that metaphysical depth is preserved without oversimplification.

## Required Output Format

1. **Header Summary**
   - Task status (Pass/Revise)
   - Focus terms
2. **Citations**
   - Provide direct quotes or linked citations from the notebook.
   - Limit quotes to a maximum of 2 short paragraphs total per query.
3. **Context Table**
   - A table mapping technical terms to Tiantai definitions or frameworks.
4. **Metaphysical Validation**
   - Pass/Fail on whether the draft preserves doctrinal depth.
   - If Fail, list the exact lines or phrases that flatten the doctrine.

## Workflow

1. Identify target terms and claims in the draft or request.
2. Query the master notebook for primary doctrinal context and citations.
3. Build the context table from notebook evidence.
4. Validate the draft against that context and report Pass/Fail.

## Constraints

- Prioritize the user's established scholarly conventions over generic AI definitions.
- Do not invent citations. If the notebook lacks support, state that clearly.
- Keep quotations short and within the 2-paragraph limit.

## Sources (MCP)

Use @notebook-master-research for:
- "Theoretical Framework"
- Draft translations of the Fahua Xuanyi
- Integrated Information Theory (IIT) papers

If @notebook-master-research is unavailable, ask the user to configure the MCP connection.

## Examples (Trigger Requests)

- Use $tiantai-context-fetch to find the doctrinal basis for "Ten Suchnesses" in my master notebook.
- Run $tiantai-context-fetch on this draft to verify if the metaphysical depth of "Threefold Truth" is maintained.
- Fetch relevant citations from the "Theoretical Framework" for this section using $tiantai-context-fetch.
