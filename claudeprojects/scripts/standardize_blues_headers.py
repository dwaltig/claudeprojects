import re
import sys

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove metadata blocks
    # Pattern: ## Blues Translation ("The Luthier") ... ---
    # We use re.DOTALL to match across newlines.
    # We make it non-greedy with *?
    metadata_pattern = r'## Blues Translation \("The Luthier"\).*?---\n'
    content = re.sub(metadata_pattern, '', content, flags=re.DOTALL)

    # 2. Remove other internal metadata headers if they vary slightly
    # Some early ones might have different styles
    # We already cleaned some manually, but let's be exhaustive
    early_metadata_pattern = r'\*\*Transformed by Master John "The Bluesman" Kim.*?\n\*\*Source\*\*:.*?\n\n---\n'
    content = re.sub(early_metadata_pattern, '', content, flags=re.DOTALL)
    
    # 3. Remove "END OF TAPE" lines
    content = re.sub(r'\*\*END OF TAPE\*\*\n', '', content)
    content = re.sub(r'\*\*END OF SIDE A\*\*\n', '', content)
    
    # 4. Remove "[End of the session]"
    content = re.sub(r'\*\*\[End of the session\]\*\*\n', '', content)
    
    # 5. Remove "Next:" lines
    content = re.sub(r'\*Next:.*?\n', '', content)
    content = re.sub(r'\*\*Next\*\*:.*?\n', '', content)
    
    # 6. Remove "Files in the manual Blues Series" blocks
    files_pattern = r'## Files in the.*?Blues Series.*?\n\n.*?\n\n---'
    content = re.sub(files_pattern, '', content, flags=re.DOTALL)

    # 7. Clean up multiple horizontal rules and excessive blank lines
    # Replace 3 or more newlines with 2
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Remove redundant horizontal rules (two rules with only whitespace between them)
    content = re.sub(r'---\s*\n\s*---', '---', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    clean_file(sys.argv[1])
