#!/usr/bin/env python3
"""
Create clean audio script for ElevenLabs TTS
Removes all markdown, preserves dramatic structure
"""

import re

def clean_for_audio(text):
    """Remove markdown but preserve dramatic structure"""

    # Remove separator lines completely
    text = re.sub(r'^={10,}$', '', text, flags=re.MULTILINE)

    # Remove ALL ## symbols (headers)
    text = re.sub(r'#{1,6}\s*', '', text)

    # Convert **bold** to plain text (but keep the text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)

    # Convert *italic* to plain text (but keep the text)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)

    # Clean up multiple blank lines (max 2 consecutive)
    text = re.sub(r'\n{4,}', '\n\n\n', text)

    return text

# Read source
with open('SURANGAMA_SUTRA_VOLUMES_1-4_COMPLETE.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Clean for audio
audio_script = clean_for_audio(content)

# Save
output_file = 'SURANGAMA_SUTRA_AUDIO_SCRIPT.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(audio_script)

print(f"✅ Audio script created: {output_file}")
print(f"📢 Features:")
print(f"   - NO markdown syntax (**, *, ##)")
print(f"   - Speaker labels preserved (THE TEACHER:, ANANDA:)")
print(f"   - Stage directions preserved (parenthetical notes)")
print(f"   - Line breaks = natural pause points")
print(f"   - Voice annotations maintained")
print(f"   - Performance-ready for ElevenLabs TTS")
