import re

file_path = "/Users/williamaltig/claudeprojects-git-repository/claudeprojects/Tiantai_Teachings_Project/01_TRANSLATIONS/The_Words_and_Phrases/Scholarly/Full_Translation/Wenju_Fascicle_03_Part2_Scholarly.md"

def contains_cjk(text):
    return any("\u4e00" <= char <= "\u9fff" for char in text)

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    original = line
    if line.startswith("> "):
        content = line[2:].strip()
        
        # Check if it's the Chinese line or English line
        if contains_cjk(content):
            # Chinese: Simply wrap in bold
            # Sometimes Chinese lines have [123] line numbers, bold those too.
            new_lines.append(f"**{content}**\n")
        else:
            # English: Strip existing bold/italics
            # Remove **
            content = content.replace("**", "")
            # Remove leading/trailing *
            if content.startswith("*") and content.endswith("*") and len(content) > 2:
                content = content[1:-1]
            
            new_lines.append(f"**{content}**\n")
    else:
        new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Reformatting complete.")
