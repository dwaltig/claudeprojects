#!/usr/bin/env python3
"""
Simple single-chapter processor for Lotus Sutra TTS optimization
Combines verse lines into single paragraphs
"""

import sys
import re

def process_chapter_simple(input_file, output_file):
    """Process a chapter with simple verse detection."""

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = [line.rstrip() for line in f]

    result = []
    i = 0
    verse_count = 0

    while i < len(lines):
        line = lines[i]

        # Empty line - keep
        if not line:
            result.append('')
            i += 1
            continue

        # Very long lines are prose - keep
        if len(line) > 150:
            result.append(line)
            i += 1
            continue

        # Check if this looks like start of verse section
        # Verse = multiple consecutive short-ish lines
        if len(line) < 100:
            # Look ahead to count short lines
            short_count = 0
            j = i
            while j < len(lines) and j < i + 15:
                test_line = lines[j].strip()
                if test_line and len(test_line) < 100:
                    short_count += 1
                elif test_line and len(test_line) > 150:
                    break
                j += 1

            # If we see 4+ short lines, treat as verse
            if short_count >= 4:
                verse_lines = []
                while i < len(lines):
                    curr = lines[i].strip()

                    # Empty line  - might be end
                    if not curr:
                        # Check if more verse follows
                        if i + 1 < len(lines):
                            next_line = lines[i + 1].strip()
                            if next_line and len(next_line) < 100:
                                i += 1
                                continue
                        break

                    # Long line = end of verse
                    if len(curr) > 150:
                        break

                    verse_lines.append(curr)
                    i += 1

                # Combine verse lines
                combined = []
                for vline in verse_lines:
                    if vline.endswith(('.', '!', '?', ',', ';', ':')):
                        combined.append(vline + ' ')
                    else:
                        combined.append(vline + ', ')

                verse_para = ''.join(combined).strip()
                if verse_para.endswith(','):
                    verse_para = verse_para[:-1]

                result.append(verse_para)
                result.append('')
                verse_count += 1
                continue

        # Default: regular line
        result.append(line)
        i += 1

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result))

    # Stats
    orig_words = sum(len(l.split()) for l in lines)
    new_words = sum(len(l.split()) for l in result)

    print(f"✅ Processed: {orig_words:,} words → {new_words:,} words")
    print(f"   Verses combined: {verse_count}")
    print(f"   Word preservation: {(new_words/orig_words*100):.2f}%")

    return {
        'verse_count': verse_count,
        'orig_words': orig_words,
        'new_words': new_words,
    }

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 simple_process_one.py INPUT_FILE OUTPUT_FILE")
        sys.exit(1)

    process_chapter_simple(sys.argv[1], sys.argv[2])
