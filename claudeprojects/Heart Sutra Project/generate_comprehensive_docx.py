#!/usr/bin/env python3
"""Generate DOCX from the comprehensive editorial review markdown.
This script reuses the `markdown_to_docx` function defined in `generate_version_d_docx.py`.
"""
import os
import sys

# Ensure the script directory is in the path to import the helper
script_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, script_dir)

try:
    from generate_version_d_docx import markdown_to_docx
except ImportError as e:
    print(f"Failed to import markdown_to_docx: {e}")
    sys.exit(1)

def main():
    input_md = "COMPREHENSIVE_EDITORIAL_REVIEW_VERSION_D.md"
    output_docx = "COMPREHENSIVE_EDITORIAL_REVIEW_VERSION_D.docx"
    if not os.path.exists(input_md):
        print(f"Error: {input_md} not found in {script_dir}")
        sys.exit(1)
    markdown_to_docx(input_md, output_docx, blind=False)
    print(f"Generated DOCX: {output_docx}")

if __name__ == "__main__":
    main()
