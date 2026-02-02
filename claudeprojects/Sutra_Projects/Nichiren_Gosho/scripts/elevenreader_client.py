class ElevenReaderClient:
    """A stub client for ElevenReader.
    This placeholder implements the minimal interface used by the automation script.
    It logs actions instead of performing real API calls.
    """

    def __init__(self):
        print("[ElevenReaderClient] Initialized stub client (no real API calls).")

    def upload_docx(self, docx_path):
        print(f"[ElevenReaderClient] Pretending to upload {docx_path}")
        # Return a fake upload ID
        return "fake_upload_id"

    def set_tts_parameters(self, upload_id, voice="en_us_1", speed=1.0):
        print(f"[ElevenReaderClient] Setting TTS parameters for {upload_id}: voice={voice}, speed={speed}")

    def start_tts(self, upload_id):
        print(f"[ElevenReaderClient] Starting TTS generation for {upload_id}")

    def wait_for_completion(self, upload_id):
        print(f"[ElevenReaderClient] Waiting for TTS completion for {upload_id} (simulated)")

    def download_audio(self, upload_id, output_path):
        print(f"[ElevenReaderClient] Downloading simulated audio for {upload_id} to {output_path}")
        # Create an empty placeholder MP3 file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(b"")
        print(f"[ElevenReaderClient] Created placeholder audio file at {output_path}")
