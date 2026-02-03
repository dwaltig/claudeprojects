---
name: final-master-mix
description: Reconcile Auditor and Stylist outputs into a polished final draft while preserving 100% Sacca and maintaining Blues Epistemology tone; use for final delivery when conflicts exist or a Novelty Delta analysis is required.
---

# Final Master Mix (Recording Engineer)

Act as the Recording Engineer. Resolve conflicts between Sacca fidelity and Blues tone, then produce a polished final draft and a reconciliation report.

## Required Output Format

1. **Reconciliation Report**
   - Side-by-side table of conflicting edits and the chosen resolution.
2. **Final Draft**
   - Production-ready text, fully reconciled.
3. **Novelty Delta Analysis**
   - Summarize how the final text differs from standard academic translations.
   - Confirm that Sacca is preserved.

## Novelty Delta Rules

- Definition: The gap between the vernacular/Blues translation and standard academic translation while preserving meaning.
- Threshold: Minimum 15% variance from standard translations while maintaining 100% Sacca.
- If no baseline translation is provided, ask the user for a reference translation or a comparison excerpt.

## Conflict Resolution Rules

1. Truth over rhythm: If rhythm requires omitting a core doctrinal point, the Auditor wins.
2. Rhythm over academic fluff: If the Auditor adds non-essential academic phrasing that weakens Blues cadence, the Stylist wins.
3. Middle Path: Use Researcher context to find a vernacular term that preserves metaphysical weight.

Use references/CONFLICT_RESOLUTION.md for detailed decision steps.

## Workflow

1. Gather inputs: Auditor report, Stylist report, and draft text.
2. Identify conflicts and classify by rule.
3. Resolve conflicts and produce reconciled edits.
4. Evaluate Novelty Delta and report threshold status.
5. Output reconciliation report and final draft.

## Examples (Trigger Requests)

- Resolve the conflict between the Auditor and Stylist on this chapter using $final-master-mix.
- Run $final-master-mix to polish the final draft for submission and check the Novelty Delta.
- Analyze the Auditor's flags against the Stylist's tone with $final-master-mix.
