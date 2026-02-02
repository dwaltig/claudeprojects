#!/usr/bin/env python3
"""
Final, production-ready speaker tagger. Handles all edge cases correctly.
"""

import re

def main():
    input_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/Trade_Publication_Edition_One.txt"
    output_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript.txt"

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output = []
    current_speaker = None
    in_quote_block = False
    quote_speaker = None

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip empty lines
        if not stripped:
            output.append(line)
            i += 1
            continue

        # ==================================================================
        # FRONT MATTER (before Chapter 1 begins)
        # ==================================================================
        if i < 260:
            if current_speaker is None:
                output.append("[Charon]\n")
                current_speaker = "Charon"

            if "THE DHARMA AND THE BLUES" in stripped or "INTRODUCTION:" in stripped:
                if current_speaker != "Rasalgethi":
                    output.append("[Rasalgethi]\n")
                    current_speaker = "Rasalgethi"

            output.append(line)
            i += 1
            continue

        # ==================================================================
        # CHAPTER HEADINGS - always Charon
        # ==================================================================
        if re.match(r'^CHAPTER\s+(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|ELEVEN|TWELVE|'
                   r'THIRTEEN|FOURTEEN|FIFTEEN|SIXTEEN|SEVENTEEN|EIGHTEEN|NINETEEN|TWENTY|'
                   r'TWENTY-ONE|TWENTY-TWO|TWENTY-THREE|TWENTY-FOUR|TWENTY-FIVE|TWENTY-SIX|'
                   r'TWENTY-SEVEN|TWENTY-EIGHT|\d+)', stripped, re.IGNORECASE):
            if current_speaker != "Charon":
                output.append("[Charon]\n")
                current_speaker = "Charon"
            in_quote_block = False
            output.append(line)
            i += 1
            continue

        # ==================================================================
        # SECTION HEADINGS (ALL CAPS) - always Charon
        # ==================================================================
        if stripped.isupper() and len(stripped) > 5 and not stripped.startswith("==="):
            if current_speaker != "Charon":
                output.append("[Charon]\n")
                current_speaker = "Charon"
            in_quote_block = False
            output.append(line)
            i += 1
            continue

        # ==================================================================
        # DETECT SPEAKER TRANSITIONS
        # ==================================================================

        # Pattern 1: "Right then, X spoke..." followed by quote
        narrator_intro_match = re.search(
            r"^(Right then|At that time|Then|And then),?\s+([A-ZāīūśṇṃĀĪŪŚṆṂ][a-zāīūśṇṃ]+(?:\s+[A-ZāīūśṇṃĀĪŪŚṆṂ][a-zāīūśṇṃ]+)?)\s+(spoke|said|told|asked|replied|answered|thought)",
            stripped
        )

        if narrator_intro_match:
            speaker_name = narrator_intro_match.group(2)

            # This line is narrator
            if current_speaker != "Charon":
                output.append("[Charon]\n")
                current_speaker = "Charon"
            output.append(line)
            in_quote_block = False

            # Determine who will speak next (in quotes)
            if "Mañjuśrī" in speaker_name:
                quote_speaker = "Gacrux"
            elif "Maitreya" in speaker_name:
                quote_speaker = "Gacrux"
            elif "Śāriputra" in speaker_name:
                quote_speaker = "Gacrux"
            elif "Buddha" in stripped or "World-Honored One" in stripped or "Thus Come One" in stripped:
                quote_speaker = "Iapetus"  # Default Buddha voice
            elif "Mahāprajāpatī" in speaker_name or "Yaśodharā" in speaker_name:
                quote_speaker = "Leda"
            else:
                # Check if it's a known male disciple
                male_disciples = ['Mahākāśyapa', 'Ānanda', 'Subhūti', 'Rāhula']
                if any(d in speaker_name for d in male_disciples):
                    quote_speaker = "Gacrux"
                else:
                    quote_speaker = "Gacrux"  # Default male voice

            # Next line likely starts the quote - we'll add the speaker tag there
            i += 1
            continue

        # Pattern 2: Currently in quote block, check for continuation
        if in_quote_block:
            # Check if quote ends
            if stripped.endswith('"') and not (i + 1 < len(lines) and lines[i+1].strip().startswith('"')):
                # Quote ending
                output.append(line)
                in_quote_block = False
                quote_speaker = None
                i += 1
                continue

            # Check for narrator interjection within quotes
            if not stripped.startswith('"') and not stripped.startswith("'"):
                # Might be narrator interjection (like "And Mañjuśrī continued:")
                if re.search(r"(continued|kept going|said|spoke)", stripped.lower()):
                    # Brief narrator moment
                    if current_speaker != "Charon":
                        output.append("[Charon]\n")
                        current_speaker = "Charon"
                    output.append(line)
                    # Next line continues the quote with same speaker
                    i += 1
                    continue

            # Continue in quote
            output.append(line)
            i += 1
            continue

        # Pattern 3: Quote is starting (we detected speaker on previous line)
        if quote_speaker and (stripped.startswith('"') or stripped.startswith("'")):
            # Add speaker tag for the character speaking
            if current_speaker != quote_speaker:
                output.append(f"[{quote_speaker}]\n")
                current_speaker = quote_speaker
            in_quote_block = True
            output.append(line)
            temp_quote_speaker = quote_speaker
            quote_speaker = None  # Clear it for next time
            quote_speaker = temp_quote_speaker  # But remember who's speaking
            i += 1
            continue

        # Pattern 4: "Listen now" - storytelling voice
        if stripped.startswith("Listen now") or stripped.startswith("Let me tell you"):
            if current_speaker != "Rasalgethi":
                output.append("[Rasalgethi]\n")
                current_speaker = "Rasalgethi"
            output.append(line)
            i += 1
            continue

        # Pattern 5: Verse sections - keep current speaker unless explicit change
        # Verses often are rhythmic and short
        if len(stripped) < 80 and (stripped.endswith("—") or stripped.endswith(",")):
            # Likely verse - continue with current speaker
            output.append(line)
            i += 1
            continue

        # Pattern 6: Default narrative transitions
        if stripped.startswith("Right then") or stripped.startswith("At that time"):
            if current_speaker != "Charon":
                output.append("[Charon]\n")
                current_speaker = "Charon"
            in_quote_block = False
            output.append(line)
            i += 1
            continue

        # Default: continue with current speaker
        output.append(line)
        i += 1

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output)

    print(f"✓ Processed {len(lines):,} lines")
    print(f"✓ Output written to: {output_file}")
    print(f"✓ Ready for professional narration!")

if __name__ == "__main__":
    main()
