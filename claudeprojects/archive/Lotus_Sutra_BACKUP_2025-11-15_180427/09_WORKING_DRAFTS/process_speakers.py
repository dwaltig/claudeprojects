#!/usr/bin/env python3
"""
Process Trade_Publication_Edition_One.txt and add speaker tags for narration
"""

import re

def add_speaker_tags(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output = []
    current_speaker = None
    in_verse = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Skip empty lines - preserve them but don't change speaker
        if not stripped:
            output.append(line)
            continue

        # Front matter detection (before Chapter 1)
        if i < 260:  # Approximate - covers all front matter
            if current_speaker is None:
                output.append("[Charon]\n")
                current_speaker = "Charon"
            output.append(line)
            continue

        # Detect chapter headings
        if stripped.startswith("CHAPTER") or stripped.startswith("Chapter"):
            if current_speaker != "Charon":
                output.append("[Charon]\n")
                current_speaker = "Charon"
            output.append(line)
            continue

        # Detect section headings (all caps)
        if stripped.isupper() and len(stripped) > 5 and not stripped.startswith("==="):
            if current_speaker != "Charon":
                output.append("[Charon]\n")
                current_speaker = "Charon"
            output.append(line)
            continue

        # Detect speaker changes in prose
        # Buddha speaking patterns
        if re.search(r'(Buddha said|Buddha spoke|Buddha told|Buddha replied|Buddha answered|World-Honored One said)', stripped, re.IGNORECASE):
            new_speaker = "Iapetus"  # Default Buddha voice - contemplative wisdom
            if "commanded" in stripped.lower() or "declared" in stripped.lower():
                new_speaker = "Sadaltager"  # Authoritative Buddha
            if current_speaker != new_speaker:
                output.append(f"[{new_speaker}]\n")
                current_speaker = new_speaker
            output.append(line)
            continue

        # Mañjuśrī speaking
        if re.search(r"Mañjuśrī (said|spoke|told|replied|answered)", stripped):
            if current_speaker != "Gacrux":
                output.append("[Gacrux]\n")
                current_speaker = "Gacrux"
            output.append(line)
            continue

        # Maitreya speaking
        if re.search(r"Maitreya (said|spoke|told|asked|replied|thought)", stripped):
            if current_speaker != "Gacrux":
                output.append("[Gacrux]\n")
                current_speaker = "Gacrux"
            output.append(line)
            continue

        # Śāriputra speaking
        if re.search(r"Śāriputra (said|spoke|told|replied|answered)", stripped):
            if current_speaker != "Gacrux":
                output.append("[Gacrux]\n")
                current_speaker = "Gacrux"
            output.append(line)
            continue

        # Other male disciples
        if re.search(r"(Mahākāśyapa|Ānanda|Subhūti|Rāhula) (said|spoke|told)", stripped):
            if current_speaker != "Gacrux":
                output.append("[Gacrux]\n")
                current_speaker = "Gacrux"
            output.append(line)
            continue

        # Female characters
        if re.search(r"(Mahāprajāpatī|Yaśodharā|dragon girl) (said|spoke|told)", stripped):
            if current_speaker != "Leda":
                output.append("[Leda]\n")
                current_speaker = "Leda"
            output.append(line)
            continue

        # Generic "Right then" - usually narrator
        if stripped.startswith("Right then") or stripped.startswith("At that time"):
            if current_speaker != "Charon":
                output.append("[Charon]\n")
                current_speaker = "Charon"
            output.append(line)
            continue

        # Generic "Listen now" - storytelling mode
        if stripped.startswith("Listen now"):
            if current_speaker != "Rasalgethi":
                output.append("[Rasalgethi]\n")
                current_speaker = "Rasalgethi"
            output.append(line)
            continue

        # Default: continue with current speaker
        output.append(line)

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output)

    print(f"Processed {len(lines)} lines")
    print(f"Output written to {output_file}")

if __name__ == "__main__":
    input_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/Trade_Publication_Edition_One.txt"
    output_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript.txt"
    add_speaker_tags(input_file, output_file)
