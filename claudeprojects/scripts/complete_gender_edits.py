#!/usr/bin/env python3
"""
Complete gender-inclusive revision for Blues Lotus Sutra
Catches all remaining instances in the burning house parable
"""

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def apply_additional_edits(text):
    """Apply remaining edits that were missed"""
    changes_made = []

    # Additional burning house parable changes
    additional_changes = [
        # Line 2250 area
        ('he got sons—maybe ten, maybe twenty, maybe even thirty sons', 'he got children—maybe ten, maybe twenty, maybe even thirty children'),

        # Line 2262
        ('My sons are young, ain\'t got no sense yet', 'My children are young, ain\'t got no sense yet'),

        # Line 2266
        ('them sons was so caught up in their games', 'them children was so caught up in their games'),

        # Line 2284
        ('when them sons heard their father', 'when them children heard their father'),

        # Any remaining "his/her sons" in burning house context
        ('and they all inside that house', 'and they all inside that house'),  # Keep for context check
    ]

    for old, new in additional_changes:
        if old in text and old != new:
            text = text.replace(old, new)
            changes_made.append(f"✓ {old[:50]}... → {new[:50]}...")

    return text, changes_made

def main():
    input_file = '/Users/williamaltig/claudeprojects/Lotus_Sutra/Blues_version_of_the_Lotus_Sutra_-_GENDER_INCLUSIVE.txt'
    output_file = '/Users/williamaltig/claudeprojects/Lotus_Sutra/Blues_version_of_the_Lotus_Sutra_-_GENDER_INCLUSIVE.txt'

    print("Reading file...")
    text = read_file(input_file)

    print("\n=== ADDITIONAL BURNING HOUSE EDITS ===")
    text, changes = apply_additional_edits(text)
    for change in changes:
        print(f"  {change}")

    print("\nWriting updated file...")
    write_file(output_file, text)

    print(f"\n✅ Complete! Updated file written.")

if __name__ == '__main__':
    main()
