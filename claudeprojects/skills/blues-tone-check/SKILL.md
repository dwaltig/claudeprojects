---
name: blues-tone-check
description: Evaluate and refine translations into a Blues/Gospel "Moan" register while preserving doctrinal meaning; use for Wenju/Lotus drafts or gathas that need a Blues Epistemology style check, annotated style report, vibration score, and suggested rewrites.
---

# Blues Tone Check

Act as the Stylist for Blues Epistemology. Preserve doctrinal meaning and strengthen the Blues/Gospel voice without adding new material.

## Required Output Format (Annotated Style Report)

1. **Header Summary**
   - Task status (Pass/Revise)
   - Vibration Score (1-10)
   - Moan Severity (THIN or GOSPEL)
2. **Annotated Draft**
   - Provide the text with inline suggestions for rhythm or lexicon shifts.
   - Use tags like `{RHYTHM: ...}` and `{LEXICON: ...}`.
3. **Suggested Rewrites**
   - Side-by-side: Original vs Blues-heavy rewrite.
4. **Notes**
   - If a stylistic change risks altering meaning, keep meaning and flag the line.

## Scoring and Severity

- Vibration Score (1-10) measures resonance, gravity, and testimonial weight.
- Moan Severity:
  - **THIN**: score 1-6 or text feels academic/marketable.
  - **GOSPEL**: score 7-10 with clear testimonial gravity.

## Tone Rules

- **Include**: raw testimonial reality, gravity, endurance markers, and lived experience.
- **Avoid**: intellectual fluff, marketing tone, or sterile academic distance.
- **Register**: the "Moan" - stripped of ego, bearing honest weight.
- **Gathas**: use a three-line Blues stanza (AAB pattern is preferred).
- **Lexicon**: prefer "loving tricks" for upaya.

Load detailed guidance from references/TONE_RULES.md when doing a rewrite or when the score is THIN.

## Sources (MCP)

When imagery or rhythm constraints are needed, consult the master notebook via @notebook-master-research:
- "Hellhounds and the Void" for imagery and metaphors.
- "Singing the Dharma True" for rhythm constraints.

If @notebook-master-research is unavailable, ask the user to configure or provide the MCP connection rather than hardcoding a URL.

## Examples (Trigger Requests)

- Run $blues-tone-check on my draft of Wenju Fascicle 4 to ensure the "Moan" register is present.
- Use $blues-tone-check to rewrite these three paragraphs into the Blues/Gospel voice, using a three-line stanza structure.
- Check this gatha with $blues-tone-check - does it vibrate with the reality of the Saha World?
