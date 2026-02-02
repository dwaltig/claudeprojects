
import os
import subprocess
import json

def diagnose_401_curl():
    key = os.environ.get('OPENAI_API_KEY')
    if not key:
        print("No API Key found.")
        return

    # Using curl to bypass python SSL cert issues and get the raw body
    cmd = [
        "curl", 
        "https://api.openai.com/v1/models",
        "-H", f"Authorization: Bearer {key}",
        "--silent", 
        "--show-error",
        "-v" # Verbose to see headers
    ]
    
    print("--- CURL COMMAND EXECUTION ---")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    print(f"Return Code: {result.returncode}")
    
    # Try to parse the output as JSON if possible
    try:
        data = json.loads(result.stdout)
        print("--- JSON RESPONSE BODY ---")
        print(json.dumps(data, indent=2))
    except:
        print("--- RAW STDOUT ---")
        print(result.stdout)
        
    print("\n--- RAW STDERR (Headers) ---")
    # Redact key from stderr
    safe_stderr = result.stderr.replace(key, "REDACTED_KEY")
    print(safe_stderr)

if __name__ == "__main__":
    diagnose_401_curl()
