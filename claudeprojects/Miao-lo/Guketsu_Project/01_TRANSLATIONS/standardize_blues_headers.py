import re
import sys
import os

def clean_file(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove metadata blocks
    # Unified pattern to catch various Translator names and Source strings
    metadata_pattern = r'## Blues Translation \("The Luthier"\).*?\n\n\*\*Source\*\*:.*?\n\*\*Translator\*\*:.*?\n\*\*Date\*\*:.*?\n\s*\n---'
    content = re.sub(metadata_pattern, '', content, flags=re.DOTALL)

    # 2. Catch variants with horizontal rule at the end
    metadata_pattern_2 = r'## Blues Translation \("The Luthier"\).*?\n\n\*\*Source\*\*:.*?\n\*\*Translator\*\*:.*?\n\*\*Date\*\*:.*?\n\n---'
    content = re.sub(metadata_pattern_2, '', content, flags=re.DOTALL)

    # 3. Specific early metadata blocks
    content = re.sub(r'\*\*Transformed by Master John "The Bluesman" Kim.*?\n\*\*Source\*\*:.*?\n\n---\n', '', content, flags=re.DOTALL)
    content = re.sub(r'\*\*Translated by "The Luthier"\*\*\n\*\*Date\*\*:.*?\n\*\*Source\*\*:.*?\n\n---\n', '', content, flags=re.DOTALL)

    # 4. Remove session markers
    content = re.sub(r'\n+\*\*END OF TAPE\*\*\n+', '\n\n', content)
    content = re.sub(r'\n+\*\*END OF SIDE A\*\*\n+', '\n\n', content)
    content = re.sub(r'\n+\*\*\[End of the session\]\*\*\n+', '\n\n', content)
    
    # 5. Remove "Next:" lines
    content = re.sub(r'\n\*Next:.*?\n', '\n', content)
    content = re.sub(r'\n\*\*Next\*\*:.*?\n', '\n', content)
    
    # 6. Remove file lists
    files_pattern = r'## Files in the.*?Blues Series.*?\n\n.*?\n\n---'
    content = re.sub(files_pattern, '', content, flags=re.DOTALL)

    # 7. Cleanup extra horizontal rules
    content = re.sub(r'\n---\n\s*\n---\n', '\n---\n', content)
    
    # 8. Cleanup excessive newlines (max 2)
    content = re.sub(r'\n{3,}', '\n\n', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Cleanup complete.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        clean_file(sys.argv[1])
    else:
        print("Usage: python3 script.py <filepath>")
