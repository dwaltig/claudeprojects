import sys
from pathlib import Path
from docx import Document

DOCX_PATH = Path('/Users/williamaltig/claudeprojects/Sutra_Projects/Nichiren_Gosho/03_FINAL_DOCUMENTS/KAIMOKU_SHO_AUDIO_SCRIPT.docx')

if not DOCX_PATH.exists():
    print(f'Error: {DOCX_PATH} not found')
    sys.exit(1)

doc = Document(DOCX_PATH)

# Define keywords that indicate a chapter title
chapter_keywords = ['Chapter', 'CHAPTER', 'Part', 'PART']

changed = 0
for para in doc.paragraphs:
    text = para.text.strip()
    if any(text.startswith(k) for k in chapter_keywords):
        # Set to Heading 1 style
        if para.style.name != 'Heading 1':
            para.style = doc.styles['Heading 1']
            changed += 1

# Save back to same file (overwrite)
if changed:
    doc.save(DOCX_PATH)
    print(f'Updated {changed} headings to Heading 1 in {DOCX_PATH.name}')
else:
    print('No heading changes needed')
