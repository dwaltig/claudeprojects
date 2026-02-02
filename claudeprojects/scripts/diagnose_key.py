
import os
import sys

def inspect_key():
    key = os.environ.get('OPENAI_API_KEY')
    
    print("--- API Key Diagnostic ---")
    
    if not key:
        print("❌ Key is Missing (None)")
        return

    print(f"Length: {len(key)}")
    print(f"Prefix: '{key[:5]}...'")
    print(f"Suffix: '...{key[-5:]}'")
    
    # Check for whitespace
    if key.strip() != key:
        print("❌ WHITESPACE DETECTED:")
        print(f"   Leading whitespace: {len(key) - len(key.lstrip())} chars")
        print(f"   Trailing whitespace: {len(key) - len(key.rstrip())} chars")
    else:
        print("✅ No leading/trailing whitespace.")

    # Check for quotes
    if key.startswith('"') or key.startswith("'"):
        print(f"❌ STARTS WITH QUOTE: {key[0]}")
    if key.endswith('"') or key.endswith("'"):
        print(f"❌ ENDS WITH QUOTE: {key[-1]}")
    
    # Check for common prefixes
    if not key.startswith("sk-"):
        print(f"⚠️ WARNING: Does not start with 'sk-'. Starts with: '{key[:3]}'")
    else:
        print("✅ Starts with 'sk-'")

    # Check for newlines
    if "\n" in key:
        print("❌ CONTAINS NEWLINE CHARACTER")
    if "\r" in key:
        print("❌ CONTAINS CARRIAGE RETURN")

if __name__ == "__main__":
    inspect_key()
