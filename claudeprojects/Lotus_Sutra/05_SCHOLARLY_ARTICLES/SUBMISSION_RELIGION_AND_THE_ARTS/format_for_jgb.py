import re
import os

def format_for_jgb(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define regex patterns for modification
    
    # Pattern 1: (Author Year, p. xx) -> (Author Year: xx)
    # Handles: (Nida 1964, p. 120) -> (Nida 1964: 120)
    # Handles: (Bakhtin 1981, pp. 84–85) -> (Bakhtin 1981: 84–85)
    
    def repl_page(match):
        full_match = match.group(0)
        # We want to replace ", p. " or ", pp. " with ": "
        # But we need to be careful about multiple citations in one block
        return full_match.replace(", p. ", ": ").replace(", pp. ", ": ").replace(", p.", ": ").replace(", pp.", ": ")

    # We run this on the whole citations component
    # A citation block looks like (text...)
    # But simpler: just replace ", p. " with ": " inside parentheses?
    # No, strictly speaking we should only do it for Author-Date citations.
    # But looking at the text, ", p. " is almost exclusively used for citations.
    
    # Let's try a regex that matches the specific citation structure to be safe.
    # Matches: (Name Year, p. Page)
    # We iterate over all parenthetical content
    
    formatted_content = content

    # Strategy: Find all parenthesized blocks, then sub inside them
    # This handles (Author 1999, p. 1; Author 2000, p. 2)
    
    def process_citation_block(match):
        block = match.group(0)
        # Inside the block, replace ", p. " and ", pp. " with ": "
        new_block = re.sub(r', pp?\. ', ': ', block)
        # Also handle cases like (Author Year, Page) if they exist (without p.)
        # But the source text seems to explicitly use p./pp. based on my analysis.
        return new_block

    # Regex for parenthetical blocks that look like citations (contain a year and maybe p.)
    # \([^\)]*\d{4}[^\)]*\)
    citation_pattern = re.compile(r'\((?:[^)(]*\d{4}(?:, [^)(]*)?(?:; [^)(]*)?)+\)')
    
    formatted_content = citation_pattern.sub(process_citation_block, formatted_content)
    
    # Also, check for "Author (Year, p. xx)" format if it occurs in narrative flow?
    # e.g. "Nida (1964, p. 12)" -> "Nida (1964: 12)"
    # The pattern above handles (...) but distinct narrative ones?
    # Let's handle (Year, p. xx) patterns separately just in case
    narrative_pattern = re.compile(r'\(\d{4}, pp?\. [^\)]+\)')
    formatted_content = narrative_pattern.sub(lambda m: m.group(0).replace(", p. ", ": ").replace(", pp. ", ": "), formatted_content)

    print(f"JGB Formatting applied to {input_file}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(formatted_content)

if __name__ == "__main__":
    base_dir = "/Users/williamaltig/claudeprojects/Lotus_Sutra/05_SCHOLARLY_ARTICLES/SUBMISSION_RELIGION_AND_THE_ARTS/"
    input_filename = "ARTICLE_Dharma_Sings_Blues_RELIGION_ARTS.md"
    output_filename = "ARTICLE_Dharma_Sings_Blues_JGB.md"
    
    format_for_jgb(os.path.join(base_dir, input_filename), 
                   os.path.join(base_dir, output_filename))
