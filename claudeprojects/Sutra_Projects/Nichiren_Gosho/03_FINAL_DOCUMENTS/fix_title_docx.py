
import docx
import os

file_path = "/Users/williamaltig/claudeprojects/Sutra_Projects/Nichiren_Gosho/03_FINAL_DOCUMENTS/KAIMOKU_SHO_AUDIO_SCRIPT.docx"
output_path = "/Users/williamaltig/claudeprojects/Sutra_Projects/Nichiren_Gosho/03_FINAL_DOCUMENTS/KAIMOKU_SHO_AUDIO_SCRIPT_v2.docx"

doc = docx.Document(file_path)

replacements = {
    "OPENING YOUR EYES": "ON OPENING THE EYES",
    "Opening Your Eyes": "On Opening the Eyes",
    "KAIMOKU SHOL OPENING YOUR EYES": "KAIMOKU SHO: ON OPENING THE EYES" # Just in case
}

count = 0
for para in doc.paragraphs:
    for key, value in replacements.items():
        if key in para.text:
            print(f"Replacing '{key}' with '{value}' in paragraph: {para.text[:50]}...")
            para.text = para.text.replace(key, value)
            count += 1

doc.save(file_path) # Overwrite original based on user request ("consistency"), or I could save to v2 and move. The prompt implied fixing "the problem" which usually means fixing the file. I will overwrite to fix it directly.

print(f"Finished. Replaced {count} instances.")
