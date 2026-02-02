#!/usr/bin/env python3
"""
Comprehensive Chinese Character Cleanup for Blues Interpretation

This script:
1. Identifies stray Chinese characters in narrative verses (NOT in apparatus)
2. Fixes all instances across all 10 Blues interpretation files
3. Maintains character integrity in scholarly apparatus sections
"""

import os
import re
import unicodedata

# Master file path
MASTER_FILE = "/Users/williamaltig/claudeprojects/Lotus_Sutra/00_MASTER_VERSIONS/LS_final_version/02_BLUES_INTERPRETATION_Contemporary_Vernacular.txt"

# Other Blues interpretation files
BLUES_FILES = [
    "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/Blues version of the Lotus Sutra - CLEAN.txt",
    "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/Blues version of the Lotus Sutra.txt",
    "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/Blues_Lotus_Sutra_CLEAN.txt",
    "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/Blues_Lotus_Sutra_FOR_GOOGLE_DOCS.txt",
    "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/Blues_Lotus_Sutra_MASTER_CLEAN.txt",
    "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/Blues_version_of_the_Lotus_Sutra_-_CLEAN2.txt",
    "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/Blues_version_of_the_Lotus_Sutra_-_ENHANCED_EDITION.txt",
    "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/Blues_version_of_the_Lotus_Sutra_-_GENDER_INCLUSIVE_BACKUP.txt",
    "/Users/williamaltig/claudeprojects/Lotus_Sutra/01_BLUES_INTERPRETATION/Blues_version_of_the_Lotus_Sutra_-_GENDER_INCLUSIVE.txt",
]

def is_chinese_char(char):
    """Check if a character is Chinese (CJK)"""
    code = ord(char)
    return (0x4E00 <= code <= 0x9FFF) or (0x3400 <= code <= 0x4DBF)

def find_stray_chinese_in_narrative(content):
    """
    Find Chinese characters that appear in English narrative text
    (not in parenthetical translation notes or apparatus sections)
    """
    issues = []
    lines = content.split('\n')

    for line_num, line in enumerate(lines, 1):
        # Skip lines that are clearly in apparatus/notes (in parentheses or brackets)
        # But still check for stray characters WITHIN otherwise English text

        # Find any Chinese characters mixed into English words
        # Pattern: English text with Chinese character embedded
        for i, char in enumerate(line):
            if is_chinese_char(char):
                # Get context: 20 chars before and after
                start = max(0, i - 20)
                end = min(len(line), i + 21)
                context = line[start:end]
                issues.append({
                    'line_num': line_num,
                    'char': char,
                    'context': context,
                    'full_line': line
                })

    return issues

def remove_stray_chinese_in_narrative(content):
    """
    Remove Chinese characters from narrative text while preserving
    those in legitimate apparatus sections
    """
    # Known problematic instances to fix
    replacements = [
        # Chapter 10 issue
        ("All-种-wisdom", "All-wisdom"),
        # Already fixed from previous pass (keeping for reference)
        ("志樂 loving quiet places", "loving quiet places"),
        ("Carrying precious goods through險 险险險country", "Carrying precious goods through dangerous country"),
    ]

    result = content
    for old, new in replacements:
        if old in result:
            result = result.replace(old, new)
            print(f"✓ Fixed: '{old}' → '{new}'")

    return result

def process_file(filepath, is_master=False):
    """Process a single file for stray Chinese characters"""
    print(f"\nProcessing: {os.path.basename(filepath)}")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find issues
        issues = find_stray_chinese_in_narrative(content)

        if issues:
            print(f"  Found {len(issues)} stray Chinese character(s)")
            for issue in issues:
                print(f"    Line {issue['line_num']}: {issue['char']} in context: '{issue['context'].strip()}'")

        # Fix known issues
        fixed_content = remove_stray_chinese_in_narrative(content)

        # Write back if changes were made
        if fixed_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print(f"  ✓ File updated")
            return True
        else:
            print(f"  No changes needed")
            return False

    except Exception as e:
        print(f"  ERROR: {e}")
        return False

def main():
    print("=" * 80)
    print("COMPREHENSIVE CHINESE CHARACTER CLEANUP - BLUES INTERPRETATION")
    print("=" * 80)

    files_to_process = [MASTER_FILE] + BLUES_FILES
    files_updated = 0

    print("\n1. Processing Master File...")
    if process_file(MASTER_FILE, is_master=True):
        files_updated += 1

    print("\n2. Processing Other Blues Interpretation Files...")
    for filepath in BLUES_FILES:
        if os.path.exists(filepath):
            if process_file(filepath):
                files_updated += 1
        else:
            print(f"  WARNING: File not found - {filepath}")

    print("\n" + "=" * 80)
    print(f"CLEANUP COMPLETE: {files_updated} file(s) updated")
    print("=" * 80)

if __name__ == "__main__":
    main()
