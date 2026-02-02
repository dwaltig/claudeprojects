# Translation Workflow - Vimalakirti Sutra

## Overview

This workflow defines the dual-agent translation process for the Vimalakirti Sutra project.

## Agents

1. **The Professor (Dr. Rajesh Patel)**: Scholarly translation
2. **The Bluesman (Master John Kim)**: Blues vernacular translation

## Standard Workflow

### Phase 1: Scholarly Translation (The Professor)

1. **Select Chapter**: Choose next chapter from source text
2. **First Pass**: Translate Classical Chinese → English (literal)
3. **Refinement**: Polish for clarity and philosophical precision
4. **Annotation**: Add comprehensive footnotes
   - Textual variants
   - Philosophical commentary
   - Cross-references
   - Sanskrit terms
   - Modern parallels
5. **Save**: Create `Chapter_[N]_[Title]_Scholarly.md`

### Phase 2: Review (The Bluesman)

1. **Read Carefully**: Review Professor's translation
2. **Check Completeness**: Ensure no nuances missed
3. **Provide Feedback**: Note any gaps or unclear passages
4. **Verify Doctrine**: Confirm theological accuracy

### Phase 3: Blues Translation (The Bluesman)

1. **Capture Context**: Set the dramatic scene
2. **Translate Dialogue**: Use authentic Blues idiom
3. **Maintain Doctrine**: Preserve theological depth
4. **Add Endnotes**: Explain Blues terms and connections
5. **Save**: Create `Chapter_[N]_[Title]_Blues.md`

### Phase 4: Consolidation

1. **Combine**: Merge both versions into `Chapter_[N]_[Title]_Complete.md`
2. **Update Status**: Mark chapter as complete in `COMPLETION_STATUS.md`
3. **Session Notes**: Document any decisions or challenges

## Quality Checks

- [ ] Sanskrit diacritics preserved (ś, ṇ, ū, ā, ṃ)
- [ ] UTF-8 encoding verified
- [ ] Footnotes/endnotes properly formatted
- [ ] Cross-references accurate
- [ ] Blues idiom authentic and respectful
- [ ] Theological accuracy maintained in both versions

## File Locations

- **Source**: `/02_SOURCE_MATERIALS/T0475.txt/T0475_00[1-3].txt`
- **Output**: `/01_TRANSLATIONS/`
- **Documentation**: `/03_DOCUMENTATION/`

## Special Considerations

- **Chapter 9 (Non-Duality)**: Requires extra care for philosophical precision
- **Dialectical Exchanges**: Preserve logical structure in both versions
- **Paradoxical Language**: Explain function in scholarly, embody in Blues
