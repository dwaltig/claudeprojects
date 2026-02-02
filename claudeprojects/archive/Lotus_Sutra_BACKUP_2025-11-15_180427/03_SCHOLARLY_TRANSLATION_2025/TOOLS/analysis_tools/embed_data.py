#!/usr/bin/env python3
"""Convert JSON to JavaScript variable for embedding."""

import json

# Read JSON
with open('chapters_polished.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create JS variable
js = "const CHAPTERS_DATA = "
js += json.dumps(data, ensure_ascii=False, separators=(',', ':'))
js += ";"

# Write to file
with open('chapters_data.js', 'w', encoding='utf-8') as f:
    f.write(js)

print(f"✓ Created chapters_data.js")
print(f"  Size: {len(js) / 1024:.1f} KB")
