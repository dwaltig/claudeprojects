import json
import os
from datetime import datetime

def format_timestamp(ts):
    try:
        return datetime.fromtimestamp(ts/1000).strftime('%Y-%m-%d %H:%M:%S')
    except:
        return "N/A"

def convert_to_md(json_path, output_md):
    if not os.path.exists(json_path):
        print(f"File not found: {json_path}")
        return

    with open(json_path, 'r') as f:
        data = json.load(f)

    with open(output_md, 'w') as out:
        out.write(f"# Session Transcript: {os.path.basename(json_path)}\n\n")
        
        messages = data.get('messages', [])
        for msg in messages:
            role = msg.get('role', 'Unknown').upper()
            content = msg.get('content', '')
            
            # Extract text from content structure (handles parts/text)
            text = ""
            if isinstance(content, list):
                for part in content:
                    if 'text' in part:
                        text += part['text']
            elif isinstance(content, str):
                text = content
            
            out.write(f"### {role}\n")
            out.write(f"{text.strip()}\n\n")
            out.write("---\n\n")

if __name__ == "__main__":
    convert_to_md('The_10_Suchnesses_of_the_Machine/transcripts/session_log_2026-01-14.json', 
                  'The_10_Suchnesses_of_the_Machine/transcripts/TRANSCRIPT_2026-01-14.md')
    print("Markdown transcript generated.")
