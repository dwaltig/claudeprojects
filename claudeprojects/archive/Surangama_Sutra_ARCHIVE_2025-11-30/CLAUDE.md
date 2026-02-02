# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

This repository contains the **Surangama Sutra** (楞嚴經 *Lengyan Jing*), a significant Buddhist scripture. The project includes:

- **Master source text**: `楞嚴經 Surangama Sutra.txt` - Classical Chinese original with 1,486 lines
- **Chapters directory**: `Chapters/` - For chapter-by-chapter organization and analysis
- **UTF-8 encoding**: All text files use UTF-8 encoding with full support for Chinese characters

This is a Buddhist scripture translation and study project. Work focuses on preserving the sacred text and developing supporting materials for academic and spiritual study.

---

## Project Structure

```
/Surangama Sutra/
├── CLAUDE.md (this file)
├── 楞嚴經 Surangama Sutra.txt (1,486-line classical Chinese source text)
└── Chapters/ (for chapter organization and analysis)
```

---

## File Handling Guidelines

### Master Source Text
- **File**: `楞嚴經 Surangama Sutra.txt`
- **Format**: UTF-8 text with Chinese characters
- **Line count**: 1,486 lines
- **Content structure**: Contains the complete Surangama Sutra in classical Chinese (文言文)
- **Do NOT edit without clear justification**: This is the primary source text. Any modifications should preserve the original Buddhist scripture accurately.

### Encoding Requirements
- All text files must use **UTF-8 encoding**
- Chinese characters are critical to the text's authenticity
- Verify encoding after any file operations: `file -i [filename]` should show `charset=utf-8`
- Preserve all diacritical marks in Sanskrit terms if they appear in companion materials

---

## Common Development Tasks

### Working with the Surangama Sutra Text
- **Reading the text**: Use standard text editors that support UTF-8 and display Chinese characters properly
- **Extracting sections**: When creating chapter breakdowns, preserve the original structure and line integrity
- **Organizing by chapters**: The text contains 10 volumes (卷) - maintain this hierarchical structure
- **Creating translations or commentary**: Store in separate files within the `Chapters/` directory, maintaining references to the original line numbers

### File Organization
- Use descriptive filenames in English when creating derivative works
- Keep classical Chinese text and translations in separate files
- Maintain clear relationships between source and derived materials

---

## Important Notes

### Sacred Text Handling
This project contains sacred Buddhist scripture. Approach all work with:
- **Accuracy**: Preserve the integrity of the original text
- **Clear communication**: Document the purpose and nature of any modifications
- **Verification**: Double-check critical changes before committing
- **Respect**: Recognize the spiritual significance of the material

### Version Control
This directory is not currently a git repository. If version control is needed:
- Initialize git with: `git init`
- Create `.gitignore` to exclude temporary files
- Commit frequently with clear messages describing changes

### Character Encoding
- Classic Buddhist texts require proper character encoding
- The Surangama Sutra is in classical Chinese (文言文) - do not modernize without explicit purpose
- When adding new content, maintain consistency with the original Chinese presentation

---

## Related Resources

If working on related Buddhist sutra projects, refer to:
- Parent directory `/claudeprojects/Lotus_Sutra/` for examples of comprehensive sutra project structure
- `/claudeprojects/Lotus_Sutra/CLAUDE.md` for detailed guidance on Buddhist text workflows
- `/Lotus_Sutra/08_REFERENCE_MATERIALS/` for terminology and character conventions that may apply

---

## Quick Reference: Key Directories
- **Source text location**: Root directory - `楞嚴經 Surangama Sutra.txt`
- **Chapter materials**: `Chapters/`
- **Derivative works**: Create subdirectories as needed for translations, commentary, etc.

---

**Last Updated**: November 25, 2025
**Repository Type**: Buddhist Sutra Text Archive
