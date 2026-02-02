import google.generativeai as genai
import re
import json
import time
import os
import base64
from pydub import AudioSegment
import io

# --- 1. CONFIGURATION ---
#
# *** IMPORTANT ***
# Paste your Google AI Studio API Key here
API_KEY = "YOUR_API_KEY_HERE"
#
# File names
MANUSCRIPT_FILE = "manuscript.txt"
CASTING_FILE = "casting.json"
OUTPUT_FILENAME = "final_narration.mp3"
CACHE_DIR = "audio_cache"

# API Settings
MODEL_NAME = "models/text-to-speech-eager" 
# This is the 100 request/day model.
# The official limit is 15 RPM, we'll set it lower to be safe.
REQUESTS_PER_MINUTE = 10 
# --------------------------

genai.configure(api_key=API_KEY)

class Narrator:
    def __init__(self, manuscript_file, casting_file):
        self.manuscript_file = manuscript_file
        self.casting_file = casting_file
        self.output_filename = OUTPUT_FILENAME
        self.cache_dir = CACHE_DIR
        self.model = genai.GenerativeModel(MODEL_NAME)
        self.voice_cast = {}
        self.default_voice = "Charon" # Fallback voice
        self.final_audio = AudioSegment.empty()

        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
            print(f"Created cache directory: {self.cache_dir}")

    def load_files(self):
        """Loads the manuscript and casting files."""
        print(f"Loading manuscript from: {self.manuscript_file}")
        try:
            with open(self.manuscript_file, 'r', encoding='utf-8') as f:
                manuscript = f.read()
        except FileNotFoundError:
            print(f"ERROR: Manuscript file not found at {self.manuscript_file}")
            print("Please make sure it's in the same folder as this script.")
            return None

        print(f"Loading casting from: {self.casting_file}")
        try:
            with open(self.casting_file, 'r', encoding='utf-8') as f:
                self.voice_cast = json.load(f)
            # Set the default voice from the casting file
            if "[Default Narrator]" in self.voice_cast:
                self.default_voice = self.voice_cast["[Default Narrator]"]
            print(f"Casting loaded. Default Narrator is set to: {self.default_voice}")
        except FileNotFoundError:
            print(f"ERROR: Casting file not found at {self.casting_file}")
            print("Please make sure it's in the same folder as this script.")
            return None
        
        return manuscript

    def get_cache_key(self, text, voice):
        """Creates a unique cache key for a text-voice pair."""
        # Using hash() makes the filename manageable
        return f"{voice}_{hash(text)}.mp3"

    def get_from_cache(self, cache_key):
        """Tries to load an audio segment from the cache."""
        cache_path = os.path.join(self.cache_dir, cache_key)
        if os.path.exists(cache_path):
            try:
                # Load the audio from the cached file
                return AudioSegment.from_mp3(cache_path)
            except Exception as e:
                print(f"Cache Warning: Could not read {cache_path}. Will regenerate. Error: {e}")
                return None
        return None

    def save_to_cache(self, audio_data_bytes, cache_key):
        """Saves audio data (as bytes) to the cache."""
        cache_path = os.path.join(self.cache_dir, cache_key)
        try:
            with open(cache_path, 'wb') as f:
                f.write(audio_data_bytes)
        except Exception as e:
            print(f"Cache Error: Could not write to {cache_path}. Error: {e}")

    def parse_manuscript(self, text):
        """Parses the manuscript into structured chunks {speaker, text}."""
        print("Parsing manuscript into chunks...")
        # This regex splits the text by [Speaker] tags, keeping the tags.
        chunks = re.split(r'(\[.*?\])', text)
        
        structured_chunks = []
        # Start with the default narrator voice
        current_speaker = "[Default Narrator]" 
        
        for chunk in chunks:
            if not chunk.strip():
                continue # Skip empty lines

            if re.match(r'(\[.*?\])', chunk):
                # It's a speaker tag. Update the current speaker.
                current_speaker = chunk.strip()
            else:
                # It's text. Assign it to the current speaker.
                cleaned_text = re.sub(r'\n+', '\n', chunk).strip()
                if cleaned_text:
                    structured_chunks.append({
                        "speaker": current_speaker,
                        "text": cleaned_text
                    })
        
        print(f"Manuscript parsed into {len(structured_chunks)} text chunks.")
        return structured_chunks

    def generate_audio_api_call(self, text, voice):
        """
        The core API call function.
        This handles the request, rate limiting, and retries.
        """
        print(f"  > API Call: Generating '{text[:40]}...' with voice '{voice}'")
        
        while True: # Keep trying until success or fatal error
            try:
                # API Call
                response = self.model.generate_content(
                    f"[{voice}] {text}",
                    stream=True
                )
                
                # The response is a stream. We need to find the audio part.
                audio_data = None
                for chunk in response:
                    if chunk.audio_content:
                        audio_data = chunk.audio_content
                        break # Found it
                
                if audio_data:
                    return audio_data # Success! Return the audio bytes
                else:
                    print("  > API Warning: Response received but no audio data. Retrying in 5s...")
                    time.sleep(5)

            except Exception as e:
                # This is where we catch the "429" Rate Limit error
                if "429" in str(e) and "RESOURCE_EXHAUSTED" in str(e):
                    print("  > API Limit Hit (429). Pausing for 65 seconds...")
                    time.sleep(65) # Wait a bit over a minute
                    print("  > Retrying...")
                    continue # Try the same request again
                elif "500" in str(e): # Handle server-side errors
                    print(f"  > API Error (500 Server Error). Retrying in 15s... Error: {e}")
                    time.sleep(15)
                    continue
                else:
                    # A different, unexpected error
                    print(f"  > FATAL API ERROR: {e}")
                    print(f"  > Could not generate audio for: {text}")
                    return None # Give up on this chunk

    def process_chunks(self, structured_chunks):
        """
        Processes chunks using "Smarter Chunking" (Option 2).
        Groups consecutive chunks by the same speaker.
        """
        print("\n--- Starting 'Smarter Chunking' Process ---")
        
        total_chunks = len(structured_chunks)
        api_requests_made_this_run = 0
        cache_hits = 0
        
        # --- PASS 1: Create "Smart Batches" ---
        smart_batches = []
        if not structured_chunks:
            return

        # Start with the first chunk
        current_batch_text = structured_chunks[0]['text']
        current_batch_voice = self.voice_cast.get(structured_chunks[0]['speaker'], self.default_voice)
        
        for i, chunk in enumerate(structured_chunks[1:], 1): # Start from the second chunk
            speaker_tag = chunk['speaker']
            text_chunk = chunk['text']
            
            # Find the voice from our casting file, or use the default
            voice = self.voice_cast.get(speaker_tag, self.default_voice)
            
            if voice == current_batch_voice:
                # Same speaker, add text to the current batch
                current_batch_text += "\n" + text_chunk
            else:
                # Speaker changed! Save the previous batch
                smart_batches.append({
                    "text": current_batch_text.strip(),
                    "voice": current_batch_voice
                })
                
                # Start a new batch
                current_batch_text = text_chunk
                current_batch_voice = voice

            # If it's the last chunk, save the final batch
            if i == total_chunks - 1:
                smart_batches.append({
                    "text": current_batch_text.strip(),
                    "voice": current_batch_voice
                })

        print(f"Consolidated {total_chunks} text chunks into {len(smart_batches)} 'Smart Batches'.")
        print("This will be our total number of API requests (if not cached).\n")
        
        # --- PASS 2: Generation and Caching ---
        
        for i, batch in enumerate(smart_batches):
            text = batch['text']
            voice = batch['voice']
            
            print(f"Processing Batch {i+1} / {len(smart_batches)} (Voice: {voice})")
            
            # Create a cache key based on the *entire* batch
            cache_key = self.get_cache_key(text, voice)
            
            # Check cache
            cached_audio_segment = self.get_from_cache(cache_key)
            
            if cached_audio_segment:
                print(f"  > Cache HIT. Loading from {cache_key}")
                self.final_audio += cached_audio_segment
                cache_hits += 1
            else:
                print(f"  > Cache MISS. Preparing for API call.")
                
                # Check API limit *before* making the call
                if api_requests_made_this_run > 0 and api_requests_made_this_run % REQUESTS_PER_MINUTE == 0:
                    print(f"  > Reached {REQUESTS_PER_MINUTE} requests. Pausing for 65 seconds to respect rate limit...")
                    time.sleep(65)
                
                # Generate audio
                audio_data_bytes = self.generate_audio_api_call(text, voice)
                
                if audio_data_bytes:
                    api_requests_made_this_run += 1
                    print("  > Generation SUCCESS.")
                    
                    # Save the raw MP3 data to cache *before* trying to parse it
                    self.save_to_cache(audio_data_bytes, cache_key)
                    print(f"  > Saved to cache: {cache_key}")
                    
                    # Append to final audio
                    try:
                        # Load the audio data from bytes for pydub
                        audio_segment = AudioSegment.from_mp3(io.BytesIO(audio_data_bytes))
                        self.final_audio += audio_segment
                    except Exception as e:
                        print(f"  > Pydub Error: Could not parse generated MP3. Skipping. Error: {e}")
                else:
                    print("  > Generation FAILED. Skipping this batch.")

            # Add a small polite delay between batches
            time.sleep(1) 

        print("\n--- Processing Complete ---")
        print(f"Total Text Chunks: {total_chunks}")
        print(f"Smart Batches: {len(smart_batches)}")
        print(f"Cache Hits: {cache_hits}")
        print(f"API Requests Made This Run: {api_requests_made_this_run}")

    def save_final_audio(self):
        """Exports the combined audio to an MP3 file."""
        if len(self.final_audio) > 0:
            print(f"\nSaving final audio to: {self.output_filename}")
            try:
                # Export the combined Pydub audio segment
                self.final_audio.export(self.output_filename, format="mp3")
                print("--- ALL DONE! ---")
                print(f"You can find your complete narration at {self.output_filename}")
            except Exception as e:
                print(f"FATAL ERROR: Could not save final MP3 file. Error: {e}")
        else:
            print("\nNo audio was generated or loaded. Final file not saved.")

    def run(self):
        """Runs the complete narration process."""
        
        # 1. Check for API Key first
        if API_KEY == "YOUR_API_KEY_HERE":
            print("="*50)
            print("ERROR: API Key not set!")
            print("Please open narrate.py in a text editor and")
            print("replace 'YOUR_API_KEY_HERE' with your actual API key.")
            print("="*50)
            return # Stop
            
        # 2. Check for Python dependencies
        try:
            from pydub import AudioSegment
        except ImportError:
            print("="*50)
            print("ERROR: Required Python package 'pydub' is not installed.")
            print("Please install it by running this in your terminal:")
            print("pip install pydub")
            print("="*50)
            return # Stop

        # 3. Run the process
        manuscript = self.load_files()
        if manuscript:
            chunks = self.parse_manuscript(manuscript)
            self.process_chunks(chunks)
            self.save_final_audio()

# --- This is what runs the script ---
if __name__ == "__main__":
    narrator = Narrator(MANUSCRIPT_FILE, CASTING_FILE)
    narrator.run()