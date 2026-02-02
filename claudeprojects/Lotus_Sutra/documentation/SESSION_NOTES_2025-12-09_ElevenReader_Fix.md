# Session Notes: ElevenReader Book Rejections Fix
**Date**: 2025-12-09
**Session Focus**: Fixing three rejected ElevenReader books

---

## Problem
Three books from the **Dharma Reborn Series** were rejected by ElevenReader:
1. The Heart Sutra Reborn
2. The Diamond Sutra Reborn
3. The Immeasurable Meanings Sutra Reborn

**Rejection Reasons**:
- Cover art shows 3D book mockups (need FLAT images)
- Formatting issues (excessive whitespace, page numbers)

---

## Completed Actions

### 1. DOCX Formatting Fixed ✅
Created `scripts/clean_elevenreader_converter.py` that:
- Removes all page numbers
- Removes ALL blank paragraphs (no extra paragraph marks)
- Consistent layout

**Generated files**:
- `Heart Sutra Project/The_Heart_Sutra_Reborn_ELEVENREADER_CLEAN.docx`
- `Diamond Sutra Project/02_BLUES_INTERPRETATION/The_Diamond_Sutra_Reborn_ELEVENREADER_CLEAN.docx`
- `Sutra_Projects/Immeasurable_Meanings_Sutra/blues_edition/The_Immeasurable_Meanings_Sutra_Reborn_ELEVENREADER_CLEAN.docx`

### 2. Cover Art Prompts Created ✅
- `Heart Sutra Project/COVER_ART_SORA_PROMPT.md` - Detailed Sora AI prompt for flat cover

### 3. Series Documentation Updated ✅
- `Lotus_Sutra/documentation/DHARMA_REBORN_SERIES_DESCRIPTION.md`
  - Full series description
  - ElevenReader brief (567 chars)
  - Official volume ordering

---

## Dharma Reborn Series - Official Order

| Vol. | Title |
|------|-------|
| 1 | The Immeasurable Meanings Sutra Reborn |
| 2 | The Lotus Sutra: A Blues Interpretation |
| 3 | Universal Worthy Bodhisattva Sutra |
| 4 | The Dhammapada Reborn |
| 5 | The Heart Sutra Reborn |
| 6 | The Diamond Sutra Reborn |
| 7 | The Vimalakirti Sutra Reborn |

---

## Pending Actions

### Cover Art (User handling with Sora AI)
User will generate flat cover images using prompts in:
- `Heart Sutra Project/COVER_ART_SORA_PROMPT.md`

### Testing Strategy
User is submitting Heart Sutra first to test if formatting passes review before submitting the other two books.

---

## Key Files to Know About
- `ElevenReader Publishing Content Guidelines .txt` - Official guidelines
- `Lotus_Sutra/documentation/SUTRA_REBORN_SERIES_DESCRIPTIONS.md` - Individual book descriptions
- `scripts/clean_elevenreader_converter.py` - DOCX converter tool
