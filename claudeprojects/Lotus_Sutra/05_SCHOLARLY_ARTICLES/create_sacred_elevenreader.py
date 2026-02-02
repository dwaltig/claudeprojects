import re
import os
import subprocess

def create_eleven_reader():
    input_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/05_SCHOLARLY_ARTICLES/ARTICLE_Sacred_Architecture_Draft.md"
    output_md = "/Users/williamaltig/claudeprojects/Lotus_Sutra/05_SCHOLARLY_ARTICLES/ARTICLE_Sacred_Architecture_ELEVENREADER.md"
    output_docx = "/Users/williamaltig/claudeprojects/Lotus_Sutra/05_SCHOLARLY_ARTICLES/ARTICLE_Sacred_Architecture_ELEVENREADER.docx"

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Markdown Tables (lines starting with |)
    # We replace them with a placeholder textual note or just remove them.
    # The tables in this text are supplementary summaries, so for audio, it's best to remove or simplify.
    # We'll just remove them to avoid "Pipe... Header... Pipe" reading.
    content = re.sub(r'\|.*\|', '', content)
    # Remove the table separator lines |---|---|
    content = re.sub(r'\|:---.*\|', '', content)
    
    # 2. Remove Citations (Author Year)
    # Matches (Name Year) or (Name & Name Year)
    content = re.sub(r'\((?:[A-Z][a-zA-Z&]+(?:, [a-zA-Z&]+)* \d{4})\)', '', content)
    # Handle the specific ones like (Teiser & Stone 2009) which might need robust regex
    content = re.sub(r'\([A-Za-z\s&\.,]+\d{4}\)', '', content)

    # 3. Remove References Section
    if "## References" in content:
        content = content.split("## References")[0]

    # 4. Clean up whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = re.sub(r' +', ' ', content)

    # 5. Expand abbreviations for TTS
    content = content.replace("e.g.", "for example")
    content = content.replace("i.e.", "that is")
    
    # Write MD
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created MD: {output_md}")

    # Convert to DOCX using Pandoc
    # Assuming pandoc is installed
    cmd = [
        "pandoc",
        output_md,
        "-o",
        output_docx
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"Created DOCX: {output_docx}")
    except Exception as e:
        print(f"Pandoc failed: {e}")

if __name__ == "__main__":
    create_eleven_reader()
