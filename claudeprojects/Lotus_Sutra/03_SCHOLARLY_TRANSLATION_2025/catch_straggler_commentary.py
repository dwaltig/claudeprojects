
import re

file_path = "/Users/williamaltig/claudeprojects/Lotus_Sutra/03_SCHOLARLY_TRANSLATION_2025/THE_LOTUS_SUTRA_SCHOLARLY_EDITION_2025.md"

def catch_stragglers():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by chapters
    parts = re.split(r'(^# Chapter \d+:.*?$)', content, flags=re.MULTILINE)
    new_content_parts = [parts[0]]
    
    commentary_starters_specific = [
        "Perfect equality of teaching",
        "A statement of transcendence", # Matches the list item (if regex splits at number)
        "Detailed classification",
        "The difference in growth",
    ]
    
    total_moved = 0
    
    for i in range(1, len(parts), 2):
        header = parts[i]
        body = parts[i+1]
        
        # We need to split lines or blocks?
        # Numbered lists "1. Text" are often adjacent.
        # "1. Text\n2. Text\n3. Text" might be one block or multiple.
        # Let's split by double newline first.
        
        blocks = body.split('\n\n')
        clean_blocks = []
        moved_blocks = []
        
        for block in blocks:
            clean_block = block.strip()
            if not clean_block:
                clean_blocks.append(block)
                continue
            
            # Skip Headers/Blockquotes
            if clean_block.startswith('#') or clean_block.startswith('>'):
                clean_blocks.append(block)
                continue
                
            is_commentary = False
            
            # 1. Check for specific stragglers
            for sig in commentary_starters_specific:
                if sig in clean_block:
                     is_commentary = True
                     break
            
            # 2. Check for Numbered Lists of Analysis (e.g. "1. **Statement**" or "1. A statement")
            # Regex: Start of block is Digit + Dot + Space.
            # And it's NOT a verse line (verses rarely start with "1. ").
            if re.match(r'^\d+\.\s+[A-Z\*\*]', clean_block):
                 is_commentary = True
                 
            # 3. Check for Bold "Headers" that are not Markdown Headers (e.g. "**Metaphysical Implication**")
            if clean_block.startswith("**") and "**:" in clean_block:
                 # "**Title**: Content..."
                 is_commentary = True
                 
            if is_commentary:
                moved_blocks.append(clean_block)
                total_moved += 1
            else:
                clean_blocks.append(block)

        new_body = "\n\n".join(clean_blocks)

        if moved_blocks:
            notes_text = "\n\n### Additional Analysis (Moved)\n\n"
            for j, note in enumerate(moved_blocks):
                 notes_text += f"**Analysis {90+j}**: {note}\n\n"
            
            if "## SCHOLARLY APPARATUS" in new_body:
                 new_body += notes_text
            else:
                 new_body += "\n\n## SCHOLARLY APPARATUS (Auto)\n\n" + notes_text
        
        new_content_parts.append(header)
        new_content_parts.append(new_body)

    final_content = "".join(new_content_parts)
    final_content = re.sub(r'\n{3,}', '\n\n', final_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"Moved {total_moved} straggler blocks.")

if __name__ == "__main__":
    catch_stragglers()
