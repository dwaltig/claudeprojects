import re

FILE_PATH = "/Users/williamaltig/claudeprojects/Sutra_Projects/Shikshasamucchaya/01_TRANSLATIONS/Shikshasamucchaya_Blues_Edition.md"

def demote_part_headers():
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex: Look for lines starting with "# Part" and add a hash to make them "## Part"
    # Wait, if they are consistent H1s, they are "# Part". 
    # We want them to be H2s "## Part" or distinct from Chapter headers.
    
    # Replace "# Part" with "## Part"
    # But check if some are already "## Part"
    
    def replacer(match):
        return "#" + match.group(0)

    # Replace start of line "# Part" -> "## Part"
    new_content = re.sub(r'^# Part', '## Part', content, flags=re.MULTILINE)
    
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Demoted '# Part' to '## Part'.")

if __name__ == "__main__":
    demote_part_headers()
