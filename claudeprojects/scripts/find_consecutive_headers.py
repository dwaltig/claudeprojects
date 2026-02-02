#!/usr/bin/env python3
"""Find consecutive headers at the same level in a markdown file."""

import sys
import re

def find_consecutive_headers(filepath):
    """Find all instances of consecutive headers at the same level."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    consecutive_groups = []
    i = 0
    
    while i < len(lines):
        # Check if current line is a header
        match = re.match(r'^(#+)\s+(.+)$', lines[i].strip())
        if match:
            level = len(match.group(1))
            group = [(i + 1, level, lines[i].strip())]
            
            # Look ahead for consecutive headers at the same level
            j = i + 1
            while j < len(lines):
                # Skip empty lines
                if lines[j].strip() == '':
                    j += 1
                    continue
                
                # Check if next non-empty line is a header at the same level
                next_match = re.match(r'^(#+)\s+(.+)$', lines[j].strip())
                if next_match and len(next_match.group(1)) == level:
                    group.append((j + 1, level, lines[j].strip()))
                    j += 1
                else:
                    break
            
            # If we found consecutive headers, record them
            if len(group) > 1:
                consecutive_groups.append(group)
            
            i = j
        else:
            i += 1
    
    return consecutive_groups

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 find_consecutive_headers.py <filepath>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    groups = find_consecutive_headers(filepath)
    
    if not groups:
        print("No consecutive headers found at the same level.")
    else:
        print(f"Found {len(groups)} groups of consecutive headers:\n")
        for idx, group in enumerate(groups, 1):
            print(f"Group {idx}:")
            for line_num, level, text in group:
                print(f"  Line {line_num}: {'#' * level} {text}")
            print()
