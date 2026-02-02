from docx import Document
from pathlib import Path

docx_path = Path('/Users/williamaltig/claudeprojects/Sutra_Projects/Nichiren_Gosho/03_FINAL_DOCUMENTS/KAIMOKU_SHO_AUDIO_SCRIPT.docx')
doc = Document(docx_path)

print("--- DOCX Header Verification ---")
for i, para in enumerate(doc.paragraphs[:15]):
    style = para.style.name if para.style else "N/A"
    print(f"{i}: [{style}] {para.text[:100]}")
