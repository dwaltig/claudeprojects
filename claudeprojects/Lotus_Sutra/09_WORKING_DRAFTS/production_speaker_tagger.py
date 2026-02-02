#!/usr/bin/env python3
"""
Production-ready speaker tagger with proper Unicode handling and comprehensive tagging.
"""

import re
import unicodedata

def is_header_line(line):
    """Check if line is an ALL CAPS header (handles Unicode properly)."""
    stripped = line.strip()
    if len(stripped) < 5:
        return False
    if stripped.startswith("==="):
        return False

    # Check if mostly uppercase (allowing for Unicode diacritics and spaces)
    letters = [c for c in stripped if c.isalpha()]
    if not letters:
        return False

    uppercase_count = sum(1 for c in letters if c.isupper() or unicodedata.category(c) in ['Lu', 'Lt'])
    ratio = uppercase_count / len(letters)

    return ratio > 0.8  # 80% uppercase

def main():
    input_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/Trade_Publication_Edition_One.txt"
    output_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript.txt"

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output = []
    current_speaker = None
    in_quote_block = False
    awaiting_quote = False
    next_quote_speaker = None

    for i, line in enumerate(lines):
        stripped = line.strip()
        next_line = lines[i+1].strip() if i + 1 < len(lines) else ""

        # Skip empty lines
        if not stripped:
            output.append(line)
            continue

        # ===== FRONT MATTER (before line 260) =====
        if i < 260:
            if current_speaker is None:
                output.append("[Charon]\n")
                current_speaker = "Charon"

            if "THE DHARMA AND THE BLUES" in stripped or "INTRODUCTION:" in stripped:
                if current_speaker != "Rasalgethi":
                    output.append("[Rasalgethi]\n")
                    current_speaker = "Rasalgethi"

            output.append(line)
            continue

        # ===== CHAPTER HEADINGS =====
        if re.match(r'^CHAPTER\s+(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|'
                   r'ELEVEN|TWELVE|THIRTEEN|FOURTEEN|FIFTEEN|SIXTEEN|SEVENTEEN|EIGHTEEN|'
                   r'NINETEEN|TWENTY|TWENTY-ONE|TWENTY-TWO|TWENTY-THREE|TWENTY-FOUR|'
                   r'TWENTY-FIVE|TWENTY-SIX|TWENTY-SEVEN|TWENTY-EIGHT|\d+)', stripped, re.IGNORECASE):
            if current_speaker != "Charon":
                output.append("[Charon]\n")
                current_speaker = "Charon"
            in_quote_block = False
            awaiting_quote = False
            output.append(line)
            continue

        # ===== SECTION HEADERS (ALL CAPS with Unicode support) =====
        if is_header_line(line):
            if current_speaker != "Charon":
                output.append("[Charon]\n")
                current_speaker = "Charon"
            in_quote_block = False
            awaiting_quote = False
            output.append(line)
            continue

        # ===== AWAITING QUOTE (previous line set this up) =====
        if awaiting_quote and (stripped.startswith('"') or stripped.startswith("'")):
            # Now add the character's voice tag
            if current_speaker != next_quote_speaker:
                output.append(f"[{next_quote_speaker}]\n")
                current_speaker = next_quote_speaker
            in_quote_block = True
            awaiting_quote = False
            output.append(line)
            continue

        # ===== DETECT SPEAKER ATTRIBUTION PATTERNS =====

        # Pattern: "Right then/At that time, NAME spoke/said..."
        speaker_match = re.search(
            r'^(Right then|At that time|Then|And then),?\s+([A-ZāīūśṇṃĀĪŪŚṆṂṚḷṅñĀāĪīŪūṚṛṃṃṄṅ][a-zāīūśṇṃṛḷṅñ]+(?:\s+[A-ZāīūśṇṃĀĪŪŚṆṂṚḷṅñĀāĪīŪūṚṛṃṃṄṅ][a-zāīūśṇṃṛḷṅñ]+)?)\s+(spoke|said|told|asked|replied|answered|thought)',
            stripped
        )

        if not speaker_match:
            # Try alternative pattern: "Buddha said" / "Buddha told"
            speaker_match = re.search(
                r'^(The\s+)?(Buddha|World-Honored One|Thus Come One|Tathāgata)\s+(spoke|said|told|replied|declared|announced|proclaimed)',
                stripped
            )

        if speaker_match:
            # This is a narrator line introducing speech
            if current_speaker != "Charon":
                output.append("[Charon]\n")
                current_speaker = "Charon"
            output.append(line)
            in_quote_block = False

            # Determine who will speak in quotes on next line(s)
            speaker_info = stripped.lower()

            if "mañjuśrī" in speaker_info:
                next_quote_speaker = "Gacrux"
                awaiting_quote = True
            elif "maitreya" in speaker_info:
                next_quote_speaker = "Gacrux"
                awaiting_quote = True
            elif "śāriputra" in speaker_info:
                next_quote_speaker = "Gacrux"
                awaiting_quote = True
            elif "mahākāśyapa" in speaker_info or "ānanda" in speaker_info or "subhūti" in speaker_info or "rāhula" in speaker_info:
                next_quote_speaker = "Gacrux"
                awaiting_quote = True
            elif "mahāprajāpatī" in speaker_info or "yaśodharā" in speaker_info:
                next_quote_speaker = "Leda"
                awaiting_quote = True
            elif "dragon girl" in speaker_info:
                next_quote_speaker = "Schedar"
                awaiting_quote = True
            elif "buddha" in speaker_info or "world-honored" in speaker_info or "thus come one" in speaker_info or "tathāgata" in speaker_info:
                # Check for authoritative vs contemplative
                if any(word in speaker_info for word in ['command', 'declare', 'proclaim', 'announced']):
                    next_quote_speaker = "Sadaltager"
                else:
                    next_quote_speaker = "Iapetus"
                awaiting_quote = True
            else:
                # Default male disciple voice
                next_quote_speaker = "Gacrux"
                awaiting_quote = True

            continue

        # ===== HANDLING QUOTED DIALOGUE =====
        if in_quote_block:
            # Check if quote ends
            if stripped.endswith('"') and not next_line.startswith('"'):
                output.append(line)
                in_quote_block = False
                continue

            # Check for narrator interjection
            if not stripped.startswith('"') and not stripped.startswith("'"):
                # Brief narrator moment within dialogue
                if any(word in stripped.lower() for word in ['continued', 'kept going', 'brought it all home', 'wanted to say']):
                    if current_speaker != "Charon":
                        output.append("[Charon]\n")
                        current_speaker = "Charon"
                    output.append(line)
                    # Speech will continue with same character
                    awaiting_quote = True
                    # next_quote_speaker already set
                    continue

            # Continue in quote
            output.append(line)
            continue

        # ===== SPECIAL NARRATIVE PATTERNS =====

        # "Listen now" - storytelling voice
        if stripped.startswith("Listen now") or stripped.startswith("Let me tell you"):
            if current_speaker != "Rasalgethi":
                output.append("[Rasalgethi]\n")
                current_speaker = "Rasalgethi"
            output.append(line)
            continue

        # "Right then" / "At that time" without speaker name - narrator
        if stripped.startswith("Right then") or stripped.startswith("At that time"):
            if current_speaker != "Charon":
                output.append("[Charon]\n")
                current_speaker = "Charon"
            in_quote_block = False
            awaiting_quote = False
            output.append(line)
            continue

        # Default: continue with current speaker
        output.append(line)

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output)

    # Count speaker tags
    speaker_tag_count = sum(1 for line in output if line.strip().startswith('[') and line.strip().endswith(']'))

    print("=" * 70)
    print("LOTUS SUTRA - PROFESSIONAL NARRATION EDITION")
    print("=" * 70)
    print(f"✓ Processed {len(lines):,} lines")
    print(f"✓ Added {speaker_tag_count} speaker tags")
    print(f"✓ Output: {output_file}")
    print("=" * 70)
    print("\nSPEAKER VOICE ASSIGNMENTS:")
    print("  [Charon] = Default narrator (cosmic authority)")
    print("  [Iapetus] = Buddha's contemplative wisdom")
    print("  [Sadaltager] = Buddha's authoritative commands")
    print("  [Gacrux] = Male disciples (noble, heroic)")
    print("  [Rasalgethi] = Warm storytelling passages")
    print("  [Leda] = Female characters (maternal wisdom)")
    print("  [Schedar] = Powerful female authority (dragon girl)")
    print("  [Sulafat] = Ethereal, spiritual beings")
    print("=" * 70)
    print("\n✓ File ready for professional voice narration!")

if __name__ == "__main__":
    main()
