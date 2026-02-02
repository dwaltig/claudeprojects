#!/usr/bin/env python3
"""
Extract Dhammapada chapters from EPUB file
EPUB files are just zipped HTML/XHTML, so we can easily extract the text
"""

import zipfile
import re
from pathlib import Path

epub_path = "02_SOURCE_MATERIALS/Dhammapada.epub"
output_dir = Path("02_SOURCE_MATERIALS")

def clean_html(html_text):
    """Remove HTML tags and clean up text"""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', html_text)
    # Decode HTML entities
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = text.replace('&amp;', '&')
    # Clean up whitespace
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    text = re.sub(r'  +', ' ', text)
    return text.strip()

def extract_chapters():
    """Extract all chapters from the EPUB"""
    with zipfile.ZipFile(epub_path, 'r') as epub:
        # List all files in the EPUB
        file_list = epub.namelist()
        
        # Find chapter files (usually in OEBPS or similar folder)
        chapter_files = [f for f in file_list if f.endswith('.htm') or f.endswith('.html') or f.endswith('.xhtml')]
        
        print(f"Found {len(chapter_files)} HTML files in EPUB:")
        for f in sorted(chapter_files):
            print(f"  {f}")
        
        # Extract each chapter
        for file_path in sorted(chapter_files):
            # Try to extract chapter number from filename
            match = re.search(r'(\d+)', Path(file_path).stem)
            if match:
                chapter_num = int(match.group(1))
                
                # Read the file content
                content = epub.read(file_path).decode('utf-8')
                cleaned = clean_html(content)
                
                # Save to file
                output_file = output_dir / f"Dhammapada_Pali_Chapter_{chapter_num}.txt"
                output_file.write_text(cleaned, encoding='utf-8')
                print(f"✓ Extracted Chapter {chapter_num} to {output_file.name}")

if __name__ == "__main__":
    print("Extracting Dhammapada chapters from EPUB...\n")
    extract_chapters()
    print("\nExtraction complete!")
