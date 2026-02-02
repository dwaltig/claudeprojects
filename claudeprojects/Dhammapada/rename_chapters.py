#!/usr/bin/env python3
"""Rename the extracted chapter files to match actual Dhammapada chapter numbers"""
from pathlib import Path

source_dir = Path("02_SOURCE_MATERIALS")

# The EPUB files 5-30 correspond to Dhammapada chapters 1-26
for epub_num in range(5, 31):
    dhamma_num = epub_num - 4  # File 5 = Chapter 1, etc.
    old_file = source_dir / f"Dhammapada_Pali_Chapter_{epub_num}.txt"
    new_file = source_dir / f"Dhammapada_Pali_Chapter_{dhamma_num}.txt"
    
    if old_file.exists():
        old_file.rename(new_file)
        print(f"✓ Renamed Chapter {epub_num} → Chapter {dhamma_num}")

print("\nRenaming complete! Now we have chapters 1-26.")
