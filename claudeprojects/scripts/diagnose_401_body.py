
import os
import urllib.request
import urllib.error
import json
import sys

def diagnose_401():
    key = os.environ.get('OPENAI_API_KEY')
    if not key:
        print("No API Key found.")
        return

    url = "https://api.openai.com/v1/models"
    
    # Explicitly constructing headers. 
    # Validating that NO Organization or Project headers are included.
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }
    
    print("--- HEADERS SENT ---")
    for k, v in headers.items():
        if k == "Authorization":
            print(f"{k}: Bearer sk-proj-REDACTED... (Len: {len(v)})")
        else:
            print(f"{k}: {v}")
    
    print("\n--- CHECKING ENV FOR HIDDEN HEADERS ---")
    org = os.environ.get("OPENAI_ORGANIZATION")
    proj = os.environ.get("OPENAI_PROJECT_ID")
    print(f"OPENAI_ORGANIZATION env var: {org}")
    print(f"OPENAI_PROJECT_ID env var: {proj}")

    print("\n--- EXECUTING REQUEST ---")
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req) as response:
            print(f"Success! Status: {response.status}")
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} {e.reason}")
        body = e.read().decode('utf-8')
        try:
            # Pretty print JSON
            parsed = json.loads(body)
            print("--- JSON ERROR BODY ---")
            print(json.dumps(parsed, indent=2))
        except:
            print("--- RAW ERROR BODY ---")
            print(body)
    except Exception as e:
         print(f"Error: {e}")

if __name__ == "__main__":
    diagnose_401()
