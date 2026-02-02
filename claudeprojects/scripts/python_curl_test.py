
import os
import subprocess
import sys

def test_auth():
    key = os.environ.get('OPENAI_API_KEY')
    if not key:
        print("No API Key found in env.")
        return

    print(f"Testing Key: {key[:10]}... (Len: {len(key)})")
    
    # Construct command list to avoid shell expansion issues
    cmd = [
        "curl", 
        "https://api.openai.com/v1/models", 
        "-H", f"Authorization: Bearer {key}",
        "--fail", "--silent", "--show-error",
        "--max-time", "10"
    ]
    
    try:
        # Run curl
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ SUCCESS: API Key Accepted.")
            print(result.stdout[:200])
        else:
            print(f"❌ FAILED: Return Code {result.returncode}")
            print(f"Stderr: {result.stderr}")
            print(f"Stdout: {result.stdout}")

    except Exception as e:
        print(f"Execution Error: {e}")

if __name__ == "__main__":
    test_auth()
