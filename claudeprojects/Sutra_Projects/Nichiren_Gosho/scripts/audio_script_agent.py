import os
import sys
from pathlib import Path

from utils import (
    convert_md_to_docx,
    refine_docx_structure,
    generate_pdf,
)
from elevenreader_client import ElevenReaderClient


def main():
    # Paths
    project_root = Path(__file__).parents[1]  # /.../Sutra_Projects/Nichiren_Gosho
    md_path = project_root / "03_FINAL_DOCUMENTS" / "KAIMOKU_SHO_AUDIO_SHARED_READING.md"
    docx_path = project_root / "03_FINAL_DOCUMENTS" / "KAIMOKU_SHO_AUDIO_SCRIPT.docx"
    pdf_path = project_root / "03_FINAL_DOCUMENTS" / "KAIMOKU_SHO_AUDIO_SCRIPT.pdf"
    audio_dir = project_root / "03_FINAL_DOCUMENTS" / "Audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    audio_path = audio_dir / "KAIMOKU_SHO_AUDIO_FINAL.mp3"

    # Force a fresh conversion if structure issues are persistent, 
    # but here we'll just refine the existing one or create it.
    if not docx_path.exists():
        print("Converting Markdown to DOCX…")
        convert_md_to_docx(md_path, docx_path)
    
    # Surgically refine structure: Remove Parts, fix Chapters, insert Intro/Context in correct order
    print("Refining DOCX structure and removing distractions…")
    refine_docx_structure(docx_path)

    # Optional PDF preview
    # Delete old PDF to ensure it's fresh
    if pdf_path.exists():
        pdf_path.unlink()
        
    try:
        print("Generating PDF preview…")
        generate_pdf(docx_path, pdf_path)
    except Exception as e:
        print(f"PDF generation failed (ignored): {e}")

    # Upload to ElevenReader and generate audio (stub client)
    client = ElevenReaderClient()
    print("Uploading DOCX to ElevenReader…")
    upload_id = client.upload_docx(docx_path)
    print("Configuring TTS parameters…")
    client.set_tts_parameters(upload_id, voice="en_us_1", speed=1.0)
    print("Starting TTS generation…")
    client.start_tts(upload_id)
    print("Polling for completion…")
    client.wait_for_completion(upload_id)
    print("Downloading audio…")
    client.download_audio(upload_id, audio_path)
    print(f"Audio saved to {audio_path}")

    print("All steps completed successfully.")

if __name__ == "__main__":
    main()
