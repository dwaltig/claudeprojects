#!/usr/bin/env python3
"""
Concatenate T1715 Fahua Jing Yiji fascicles (001-008) into a single file.
Preserves CBETA format and adds clear fascicle dividers.
"""

import os
from pathlib import Path

def concatenate_fascicles():
    source_dir = Path(__file__).parent
    output_file = source_dir / "T1715_FULL.txt"
    
    # Fascicle files in order
    fascicle_files = [f"T1715_{i:03d}.txt" for i in range(1, 9)]
    
    with open(output_file, 'w', encoding='utf-8') as outf:
        # Write master header
        outf.write("#" + "=" * 70 + "\n")
        outf.write("# T1715 法華經義記 (Fahua Jing Yiji) - COMPLETE TEXT\n")
        outf.write("# Compiled from CBETA source files T1715_001.txt through T1715_008.txt\n")
        outf.write("# Author: 光宅寺沙門法雲 (Fayun of Guangzhai Temple)\n")
        outf.write("# Period: Liang Dynasty (梁朝), 6th century\n")
        outf.write("#" + "=" * 70 + "\n\n")
        
        total_lines = 0
        for i, fname in enumerate(fascicle_files, 1):
            filepath = source_dir / fname
            if not filepath.exists():
                print(f"Warning: {fname} not found, skipping...")
                continue
            
            with open(filepath, 'r', encoding='utf-8') as inf:
                content = inf.read()
            
            # Add fascicle divider
            outf.write("\n" + "#" + "-" * 70 + "\n")
            outf.write(f"# FASCICLE {i} (卷第{['一','二','三','四','五','六','七','八'][i-1]})\n")
            outf.write("#" + "-" * 70 + "\n\n")
            
            outf.write(content)
            if not content.endswith('\n'):
                outf.write('\n')
            
            lines = content.count('\n') + 1 if content else 0
            total_lines += lines
            print(f"Added {fname}: {lines} lines")
        
        print(f"\nTotal: {total_lines} lines written to {output_file}")

if __name__ == "__main__":
    concatenate_fascicles()
