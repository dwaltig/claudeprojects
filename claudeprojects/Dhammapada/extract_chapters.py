#!/usr/bin/env python3
"""
Extract Dhammapada chapters from Ancient Buddhist Texts website
Saves each chapter as a separate text file with Pali and metrical notation
"""

import urllib.request
import re
import time

# Base URL and chapter info
base_url = "https://ancient-buddhist-texts.net/Buddhist-Texts/K2-Dhammapada-New/"

chapters = [
    ("02-Appamada.htm", "Appamadavagga", "Heedfulness"),
    ("03-Citta.htm", "Cittavagga", "Mind"),
    ("04-Puppha.htm", "Pupphavagga", "Flowers"),
    ("05-Bala.htm", "Balavagga", "Fools"),
    ("06-Pandita.htm", "Panditavagga", "Wise"),
    ("07-Arahanta.htm", "Arahantavagga", "Arahants"),
    ("08-Sahassa.htm", "Sahassavagga", "Thousands"),
    ("09-Papa.htm", "Papavagga", "Evil"),
    ("10-Danda.htm", "Dandavagga", "Violence"),
    ("11-Jara.htm", "Jaravagga", "Old Age"),
    ("12-Atta.htm", "Attavagga", "Self"),
    ("13-Loka.htm", "Lokavagga", "World"),
    ("14-Buddha.htm", "Buddhavagga", "Buddha"),
    ("15-Sukha.htm", "Sukhavagga", "Happiness"),
    ("16-Piya.htm", "Piyavagga", "Affection"),
    ("17-Kodha.htm", "Kodhavagga", "Anger"),
    ("18-Mala.htm", "Malavagga", "Impurity"),
    ("19-Dhammattha.htm", "Dhammatthavagga", "Righteous"),
    ("20-Magga.htm", "Maggavagga", "Path"),
    ("21-Pakinnaka.htm", "Pakinnakavagga", "Miscellaneous"),
    ("22-Niraya.htm", "Nirayavagga", "Hell"),
    ("23-Naga.htm", "Nagavagga", "Elephant"),
    ("24-Tanha.htm", "Tanhavagga", "Craving"),
    ("25-Bhikkhu.htm", "Bhikkhuvagga", "Monk"),
    ("26-Brahmana.htm", "Brahmanavagga", "Brahman"),
]

def clean_text(html):
    """Extract just the Pali text with metrical notation"""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', html)
    # Clean up excessive whitespace
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    text = re.sub(r'  +', ' ', text)
    return text.strip()

def extract_chapter(chapter_num, filename, pali_name, english_name):
    """Fetch and save a chapter"""
    url = base_url + filename
    print(f"Fetching Chapter {chapter_num}: {pali_name}...")
    
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
        
        # Extract main content (between specific markers if possible)
        # For now, just clean the whole thing
        content = clean_text(html)
        
        # Save to file
        output_filename = f"02_SOURCE_MATERIALS/Dhammapada_Pali_Chapter_{chapter_num:02d}.txt"
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ Saved to {output_filename}")
        time.sleep(0.5)  # Be nice to the server
        
    except Exception as e:
        print(f"  ✗ Error: {e}")

# Main execution
if __name__ == "__main__":
    print("Extracting Dhammapada chapters 2-26...\n")
    for i, (filename, pali, english) in enumerate(chapters, start=2):
        extract_chapter(i, filename, pali, english)
    print("\nExtraction complete!")
