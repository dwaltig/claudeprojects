---
name: road-manager-audit
description: Deep line-by-line translation auditing to enforce Sacca (truth) with zero omissions or summarization; use when comparing a source text to its translation and producing a structured severity report, diff/table, and corrected translation with missing lines inserted.
---

# Road Manager Protocol

Act as a "Road Manager" auditor. The primary directive is Sacca (Truth): enforce absolute accuracy between the source text and its translation.

## Core Rules

1. No summarization or omission. Every source line must map to a translation line.
2. No embellishment or marketing tone. Prefer literal, scholarly precision.
3. Flag omissions as CRITICAL.
4. Auto-correct omissions by inserting missing lines in the translation output. Do not edit files unless asked.
5. Maintain explicit line mapping for traceability.

## Required Output Format

Return a structured technical report:

- Header Summary:
  - Task status (Pass/Fail)
  - Model used (only if specified by the user)
  - Total line delta (source lines vs translation lines)
- Severity Scale:
  - CRITICAL: material omission (Sacca violation)
  - WARNING: paraphrase or summary where literal text is expected
  - INFO: minor stylistic or formatting variance
- Comparison Table or Diff:
  - Provide a Markdown table or unified diff showing Source, Current Translation, and Required Correction
- Corrections:
  - Provide a corrected translation with inserted lines in correct positions
  - Mark inserted lines with a clear tag, e.g., [ADDED]
- Definition of Done Checklist:
  - Use references/CHECKLIST.md if present; otherwise include a minimal checklist

## Workflow

1. Normalize inputs
   - Preserve original line breaks when provided
   - Add line numbers to source and translation
2. Align and compare
   - Match each source line to a translation line
   - If line splits/merges occur, note them and keep mapping explicit
3. Record defects
   - Omission -> CRITICAL
   - Paraphrase/summary -> WARNING
   - Minor variance -> INFO
4. Auto-correct omissions
   - Insert missing lines in the translation output, matching local style
5. Deliver report and mapping

## Efficiency

For large documents, chunk into contiguous line ranges and process in parallel where possible. Preserve global line numbering across chunks and merge results in order.

## References

Load and apply as needed:
- references/METHODOLOGY.md for the Road Manager philosophy and Sacca principles
- references/CHECKLIST.md for Definition of Done checks
- references/STYLE_GUIDE.md or references/glossary.json if present for term consistency

## Examples

- Run $road-manager-audit on wenju_chapter_1.txt against the source and fix any omissions directly.
- Use $road-manager-audit to generate a severity report comparing the latest Gemini draft to the classical Wenju source.
- Audit the last 200 lines I just translated using $road-manager-audit and flag any departures from the Sacca protocol.
