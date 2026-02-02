import re

input_file = "madhyama-kasha-shastra/01_TRANSLATIONS/Mūlamadhyamakakārikā_Blues_Complete.md"
output_file = "madhyama-kasha-shastra/01_TRANSLATIONS/Mūlamadhyamakakārikā_Blues_Lyrics_Only.md"

def is_lyric_line(line):
    stripped = line.strip()
    if not stripped: return False
    
    # Explicit Keep List
    if re.match(r'^\(Verse', stripped, re.IGNORECASE): return True
    if stripped.startswith("(") and stripped.endswith(")"): return True
    
    # Blockquotes in early chapters
    if stripped.startswith(">"): return True
    
    # Headers/Tables removal
    if stripped.startswith("#"): return False 
    if "|" in stripped: return False
    
    # Prose Exclusion
    if stripped.startswith("Now,"): return False
    if stripped.startswith("See,"): return False
    if stripped.startswith("Let me"): return False
    if stripped.startswith("Here's"): return False
    if stripped.startswith("That's"): return False
    if stripped.startswith("So "): return False
    if stripped.startswith("But "): return False 
    if stripped.startswith("And "): return False
    if stripped.endswith("?"): return False
    
    # Length Heuristic
    if len(stripped) > 80: return False
    
    return True

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

cleaned_content = []
cleaned_content.append("---\n")
cleaned_content.append("title: Mūlamadhyamakakārikā Blues\n")
cleaned_content.append("subtitle: The Lyrics\n")
cleaned_content.append("author: Master John Kim\n")
cleaned_content.append("---\n\n")

last_type = "other" # track previous line type to manage spacing

for line in lines:
    stripped = line.strip()
    
    # 1. Headers (Chapters)
    if stripped.startswith("# Madhyamakashāstra Chapter") or stripped.startswith("# Chapter"):
        cleaned_content.append("\n\n" + stripped + "\n\n")
        last_type = "header"
        continue
        
    # 2. Song Titles
    if stripped.startswith("**Title:") or stripped.startswith("### Title:") or stripped.startswith("## *"):
        # Clean up title formatting
        title_text = stripped.replace("**Title:", "").replace("**", "").replace("### Title:", "").strip()
        cleaned_content.append(f"\n### {title_text}\n\n")
        last_type = "title"
        continue
    
    # 3. Separators
    if stripped == "---":
        if last_type != "separator":
            cleaned_content.append("\n* * *\n\n")
            last_type = "separator"
        continue

    # 4. Lyrics
    if is_lyric_line(line):
        clean_line = line.replace("> ", "").replace(">", "").strip()
        
        # If it's a verse marker like "(Verse 1)", give it breathing room
        if clean_line.startswith("(Verse") or clean_line.startswith("(Chorus"):
            cleaned_content.append(f"\n**{clean_line}**\n") # Bold the verse marker
        else:
            # Use Line Block syntax for lyrics (starts with |)
            # This tells Pandoc: "This is poetry, keep the lines together but distinct"
            cleaned_content.append(f"| {clean_line}\n")
            
        last_type = "lyric"

with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines(cleaned_content)

print(f"Created {output_file}")
