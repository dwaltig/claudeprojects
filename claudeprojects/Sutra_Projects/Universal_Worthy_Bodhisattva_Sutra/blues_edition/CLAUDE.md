# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Context

This is the **blues_edition** subdirectory of the Universal Worthy Bodhisattva Sutra translation project. It contains complete blues-vernacular translations of this important Mahayana Buddhist text, which serves as the epilogue to the Lotus Sutra.

**Parent Project Documentation**: See `/Sutra_Projects/documentation/CLAUDE.md` for broader project context and conventions that apply to all sutra translation work.

**Workspace Overview**: See `/claudeprojects/CLAUDE.md` for the complete Buddhist sutra translation workspace structure.

## Directory Contents

```
blues_edition/
  ├── Universal Worthy Bodhisattva Sutra - COMPLETE Blues Translation.txt (1,214 lines)
  ├── Universal Worthy Bodhisattva Sutra - COMPLETE Blues Translation - AUDIOBOOK_READY.txt (1,211 lines)
  └── CLAUDE.md (this file)
```

**Two Versions Available:**
- **COMPLETE Blues Translation.txt**: Standard blues-vernacular translation with full Sanskrit diacritics
- **COMPLETE Blues Translation - AUDIOBOOK_READY.txt**: TTS-optimized version (diacritics removed for text-to-speech compatibility)

## File Encoding and Character Standards

**Critical Encoding Requirements:**
- All files use **UTF-8 encoding** (`charset=utf-8`)
- Verify encoding after edits: `file -I [filename]` should show `charset=utf-8`

**Sanskrit Diacriticals (Standard Version Only):**
- Required Unicode marks: ś (U+015B), ṇ (U+1E47), ū (U+016B), ā (U+0101), ṃ (U+1E43)
- Standard names: Śākyamuni, Śāriputra, Mañjuśrī, Mahākāśyapa, Avalokiteśvara, Vaiśālī
- Buddhist terms: Tathāgata, nirvāṇa, samādhi, Jambudvīpa, Anuttara-samyak-sambodhi
- **AUDIOBOOK_READY version**: Uses simplified ASCII (Sakyamuni, Sariputra, nirvana, etc.)

## Text Structure

The sutra follows classical Mahayana structure with blues-vernacular interpretation:

### Primary Sections
1. **Opening Frame**: "THUS HAVE I HEARD - WHEN THE BUDDHA SAID HE WAS LEAVING"
2. **Core Teaching**: The Buddha's answer and Universal Worthy's description
3. **Detailed Vision**: Six-Tusked White Elephant, jade maidens, celestial music, transformation-Buddha
4. **Repentance Method**: Purification of the six sense-faculties (eye, ear, nose, tongue, body, mind)
5. **Universal Vision**: Pure lands in ten directions, no-sin-mark repentance
6. **Closing**: Assembly response, blues reflection, formal colophon

**Section Headers**: All-caps with descriptive titles (e.g., "THE SIX-TUSKED WHITE ELEPHANT - A LIVING CHARIOT OF LIGHT")

**Confessional Sections**: Numbered confessions with specific titles:
- FIRST CONFESSION: Correct the Mind Toward the Sacred
- SECOND CONFESSION: Honor Your Roots
- THIRD CONFESSION: Rule with Justice
- FOURTH CONFESSION: Preserve Life
- FIFTH CONFESSION: Trust Cause and Effect

See `/Universal_Worthy_Bodhisattva_Sutra/analysis/Blues Worthy Bodhisattva Sutra - Structural Elements.md` for complete structural analysis.

## Blues-Vernacular Style Conventions

**Language Characteristics:**
- Contemporary informal American English with blues/gospel phrasing
- Deliberate contractions: "ain't", "gonna", "got to", "them" (for "those")
- Call-and-response patterns and oral storytelling rhythms
- Sacred register maintained through vivid imagery and emotional authenticity
- Maintains complete doctrinal fidelity to original while using accessible language

**Preservation of Buddhist Elements:**
- Formulaic openings: "This is what I heard, what come down to me, what got told"
- Traditional epithets: "World-Honored One", "Blessed One", "Tathāgata"
- Complete Mahayana terminology preserved with explanations woven into text
- Three-fold circumambulation, prostrations, formal requests all retained

## Common Verification Tasks

### Encoding Integrity Check
```bash
# Verify UTF-8 encoding
file -I "Universal Worthy Bodhisattva Sutra - COMPLETE Blues Translation.txt"

# Should output: text/plain; charset=utf-8
```

### Diacritical Marks Audit
```bash
# Search for proper diacritical usage in standard version
grep -n "Śākyamuni\|Śāriputra\|Mañjuśrī\|nirvāṇa" "Universal Worthy Bodhisattva Sutra - COMPLETE Blues Translation.txt"

# Verify audiobook version has simplified forms
grep -n "Sakyamuni\|Sariputra\|Manjusri\|nirvana" "Universal Worthy Bodhisattva Sutra - COMPLETE Blues Translation - AUDIOBOOK_READY.txt"
```

### Section Structure Verification
```bash
# List all major section headers
grep "^[A-Z\-\s]*:" "Universal Worthy Bodhisattva Sutra - COMPLETE Blues Translation.txt"

# Count confession sections
grep -c "CONFESSION:" "Universal Worthy Bodhisattva Sutra - COMPLETE Blues Translation.txt"
```

### Line Count Verification
```bash
# Both versions should have similar line counts (±5 lines acceptable)
wc -l *.txt
```

## Editing Guidelines

**When modifying the standard blues translation:**
1. **Preserve diacritics**: Never change Śāriputra → Sariputra
2. **Maintain vernacular tone**: Keep blues phrasing and contractions
3. **Verify encoding**: Always check `file -I` after edits
4. **Protect structure**: Don't alter section headers or confession numbering
5. **Consistency**: Reference parent CLAUDE.md for Buddhist terminology standards

**When modifying the AUDIOBOOK_READY version:**
1. **Use ASCII only**: No diacritical marks (for TTS compatibility)
2. **Match content**: Changes should parallel the standard version
3. **Line parity**: Keep line counts similar between versions
4. **Same structure**: Maintain identical section organization

**Never do:**
- Mix formal scholarly tone with blues vernacular
- Remove or alter Buddhist formulaic elements
- Change character encoding from UTF-8
- Modify section header formatting
- Alter confession numbering or sequence

## Relationship to Lotus Sutra Project

The Universal Worthy Bodhisattva Sutra functions as the **epilogue to the Lotus Sutra**.

**Cross-Reference:**
- Main Lotus Sutra project: `/Lotus_Sutra/`
- Character name standards: `/Lotus_Sutra/08_REFERENCE_MATERIALS/CHARACTER_VOICE_MAPPING_FINAL.txt`
- Terminology standards: `/Lotus_Sutra/08_REFERENCE_MATERIALS/TERMINOLOGY_CORRECTIONS_SUMMARY.md`

When making terminology or character name decisions, defer to Lotus Sutra conventions for consistency across the complete trilogy (Immeasurable Meanings Sutra → Lotus Sutra → Universal Worthy Bodhisattva Sutra).

## Version Comparison

**Differences Between the Two Versions:**

| Feature | Standard Version | AUDIOBOOK_READY Version |
|---------|-----------------|-------------------------|
| Diacritics | Full Unicode (ś, ṇ, ū, ā, ṃ) | ASCII simplified |
| TTS-Compatible | No | Yes |
| Print-Ready | Yes | No |
| Character Names | Śāriputra, Mañjuśrī | Sariputra, Manjusri |
| Terms | nirvāṇa, samādhi | nirvana, samadhi |
| Content | Identical | Identical |
| Structure | Identical | Identical |
| Line Count | 1,214 | 1,211 |

## Parent Directory Resources

**Related files in parent `/Universal_Worthy_Bodhisattva_Sutra/`:**
- `analysis/Blues Worthy Bodhisattva Sutra - Structural Elements.md` - Complete structural breakdown
- `source/佛說觀普賢菩薩行法經...txt` - Original Chinese source text
- `archive/` - Earlier partial versions and drafts
- `scholarly_edition/` - (Currently empty, reserved for future formal translation)

## Quick Reference: File Operations

```bash
# View specific section of sutra (e.g., lines 100-200)
sed -n '100,200p' "Universal Worthy Bodhisattva Sutra - COMPLETE Blues Translation.txt"

# Search for specific Buddhist term
grep -n "Universal Worthy\|Samantabhadra" "Universal Worthy Bodhisattva Sutra - COMPLETE Blues Translation.txt"

# Compare versions (check diacritical differences)
diff "Universal Worthy Bodhisattva Sutra - COMPLETE Blues Translation.txt" \
     "Universal Worthy Bodhisattva Sutra - COMPLETE Blues Translation - AUDIOBOOK_READY.txt" | head -20

# Count occurrences of a character/term
grep -o "Universal Worthy" "Universal Worthy Bodhisattva Sutra - COMPLETE Blues Translation.txt" | wc -l
```

## Publication Status

Both manuscripts are complete and represent final blues-vernacular translations ready for:
- **Standard version**: Print publication, scholarly reference, general reading
- **AUDIOBOOK_READY version**: Text-to-speech conversion, audio production, narration scripts

No active development is currently planned unless editorial revisions are requested.

---

**Last Updated**: December 4, 2025
**Translation Style**: Blues-Vernacular (Contemporary American English)
**Source Text**: 佛說觀普賢菩薩行法經 (The Buddha Speaks the Sutra on Contemplating Universal Worthy Bodhisattva)
**Status**: Complete manuscripts, publication-ready
