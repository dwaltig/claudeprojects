import re
import os

def create_elevenreader_version(input_file="ARTICLE_Dharma_Sings_Blues_RELIGION_ARTS.md", output_file="ARTICLE_Dharma_Sings_Blues_RELIGION_ARTS_ELEVENREADER.txt"):
    """
    Creates a clean version of the manuscript for ElevenReader (TTS)
    by removing footnotes, citations, and reference sections.
    """
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found!")
        return
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"Processing '{input_file}'...")
    
    # 1. Remove footnotes: [^1], [^12], etc.
    content = re.sub(r'\[\^\d+\]', '', content)
    
    # 2. Remove in-text citations: (Author Year) or (Author Year, p. xx)
    # Updated regex to allowed lowercase start (e.g. bell hooks)
    # Match parentheses containing:
    #   Author Name (letters, spaces, ., -, &)
    #   Space
    #   Year (4 digits)
    #   Optional: , page info
    #   Optional: ; (multiple citations)
    
    citation_pattern = r'\((?:(?:[a-zA-Z][a-zA-Z\s\.\-\&]+ \d{4}(?:, [^)]*)?)(?:; )?)+\)'
    content = re.sub(citation_pattern, '', content)
    
    # 3. Remove "References" section and everything after
    references_start = content.find("## References")
    if references_start != -1:
        content = content[:references_start]
    
    # 4. Collapse spaces
    content = re.sub(r'[ \t]+', ' ', content)
    
    # 5. Clean up residual punctuation and spacing issues
    # Fix "text ." -> "text."
    content = re.sub(r'\s+([.,;?!])', r'\1', content)
    
    # Fix double punctuation from removals: "theory, , philosophy" -> "theory, philosophy"
    content = re.sub(r',\s*,', ',', content)
    content = re.sub(r',\s*\.', '.', content)
    
    # Fix empty list items or awkward phrasing caused by removal
    # e.g. "—, , and —"
    content = content.replace("—, , and —", "—")
    content = re.sub(r'—\s*,\s*,\s*and\s*—', '—', content)
    
    # General cleanup of " , "
    content = content.replace(" , ", ", ")
    
    # 6. Max 2 newlines
    content = re.sub(r'\n\s*\n', '\n\n', content) 
    
    # 7. Basic TTS expansions
    content = content.replace("i.e.", "that is")
    content = content.replace("e.g.", "for example")
    content = content.replace("et al.", "and others")
    
    output_file = output_file.replace(".txt", ".md")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"ElevenReader version saved to '{output_file}'")
    print(f"Total characters: {len(content)}")

if __name__ == "__main__":
    create_elevenreader_version(output_file="ARTICLE_Dharma_Sings_Blues_RELIGION_ARTS_ELEVENREADER.md")
