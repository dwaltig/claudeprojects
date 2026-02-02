---
description: Create a Blues Dhammapada song for verses 3-4 using AI agents
---

## Workflow Steps

1. **Gather Source Verses**
   - Retrieve verses 3 and 4 from the Dhammapada source files (e.g., `00_MASTER_VERSIONS` or scholarly translation).
   - Use the **Scholarly Translation Agent** to obtain a literal English rendering.

2. **Generate Blues Vernacular Lyrics**
   - Feed the literal translation to the **Blues Agent** to produce lyrical verses in a blues style, preserving key themes and diacritics.

3. **Structure the Song**
   - Use the **Songwriter Agent** to arrange the lyrics into a song format (e.g., Verse‑Chorus‑Bridge), deciding where verses 3 and 4 appear.
   - Define sections, repeat hooks, and any spoken interludes.

4. **Compose Music**
   - Invoke the **Music Composition Agent** to create a chord progression, melody, and basic arrangement suitable for a blues track.
   - Output chord charts and optional MIDI/audio generation instructions.

5. **Assemble Final Song Document**
   - Combine lyrics, chord symbols, and any audio generation commands into a single markdown file `Blues_Dhammapada_Song_Verses_3_4.md`.
   - Include metadata: title, author, timestamp, and agent credits.

6. **Review & Export**
   - Perform a manual review of the assembled song for lyrical flow, musical coherence, and correct diacritics.
   - Export the markdown to desired formats (e.g., PDF, audio via external tools).

## Verification Plan
- **Manual Review**: Read through the final markdown to ensure verses 3‑4 are accurately represented and the blues style is consistent.
- **Audio Check** (optional): Run the generated music instructions through a local audio synthesis tool and listen for correctness.
- **Agent Audit**: Verify that each agent step completed without errors and that outputs are saved in the appropriate project directories.
