#!/usr/bin/env python3
"""
Refined speaker tagging for Lotus Sutra - handles dialogue continuity properly.
"""

import re
from typing import List, Optional

class RefinedSpeakerTagger:
    def __init__(self):
        self.current_speaker = None
        self.in_quoted_dialogue = False
        self.dialogue_speaker = None

    def detect_dialogue_start(self, line: str) -> Optional[str]:
        """Detect if a character starts speaking in quoted dialogue."""
        stripped = line.strip()

        # Mañjuśrī speaking
        if re.search(r"Mañjuśrī\s+(spoke|said|told|replied|answered)", stripped):
            # Check if dialogue starts on same line or next
            if '"' in line or "'" in line:
                return "Gacrux"
            return None

        # Maitreya speaking
        if re.search(r"Maitreya\s+(spoke|said|told|replied|asked)", stripped):
            if '"' in line or "'" in line:
                return "Gacrux"
            return None

        # Buddha speaking
        if re.search(r"(Buddha|World-Honored One|Thus Come One)\s+(spoke|said|told|replied|declared|announced)", stripped):
            if any(word in stripped.lower() for word in ['command', 'declare', 'proclaim']):
                return "Sadaltager"
            return "Iapetus"

        # Śāriputra and other male disciples
        male_disciples = ['Śāriputra', 'Mahākāśyapa', 'Ānanda', 'Subhūti', 'Rāhula']
        for disciple in male_disciples:
            if re.search(rf"{disciple}\s+(spoke|said|told)", stripped):
                return "Gacrux"

        # Female characters
        if re.search(r"(Mahāprajāpatī|Yaśodharā)\s+(spoke|said|told)", stripped):
            return "Leda"

        if "dragon girl" in stripped.lower() and any(word in stripped.lower() for word in ['spoke', 'said']):
            return "Schedar"

        return None

    def is_dialogue_line(self, line: str) -> bool:
        """Check if line is part of quoted dialogue."""
        stripped = line.strip()
        # Starts with quote or is clearly continuation
        return stripped.startswith('"') or stripped.startswith("'") or \
               (self.in_quoted_dialogue and not self.is_narrator_interjection(line))

    def is_narrator_interjection(self, line: str) -> bool:
        """Check if line is narrator interjecting into dialogue."""
        stripped = line.strip()
        # Narrator patterns that break dialogue
        return (stripped.startswith("Right then") or
                stripped.startswith("At that time") or
                stripped.startswith("And then") or
                re.search(r"^(And\s+)?[A-Z][a-zāīūśṇṃ]+\s+(said|spoke|continued|kept going)", stripped))

    def process_file(self, input_path: str, output_path: str):
        """Process file with refined speaker detection."""
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        output = []
        i = 0

        while i < len(lines):
            line = lines[i]
            stripped = line.strip()

            # Skip empty lines - preserve but don't change speaker
            if not stripped:
                output.append(line)
                i += 1
                continue

            # Front matter (before Chapter One starts around line 260)
            if i < 260:
                if self.current_speaker is None:
                    output.append("[Charon]\n")
                    self.current_speaker = "Charon"

                # Special handling for Introduction sections
                if "THE DHARMA AND THE BLUES" in stripped or "INTRODUCTION:" in stripped:
                    if self.current_speaker != "Rasalgethi":
                        output.append("[Rasalgethi]\n")
                        self.current_speaker = "Rasalgethi"

                output.append(line)
                i += 1
                continue

            # Chapter and section headings - always Charon
            if re.match(r'^CHAPTER\s+(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|' +
                       r'ELEVEN|TWELVE|THIRTEEN|FOURTEEN|FIFTEEN|SIXTEEN|SEVENTEEN|' +
                       r'EIGHTEEN|NINETEEN|TWENTY|TWENTY-ONE|TWENTY-TWO|TWENTY-THREE|' +
                       r'TWENTY-FOUR|TWENTY-FIVE|TWENTY-SIX|TWENTY-SEVEN|TWENTY-EIGHT|' +
                       r'\d+):', stripped, re.IGNORECASE):
                if self.current_speaker != "Charon":
                    output.append("[Charon]\n")
                    self.current_speaker = "Charon"
                self.in_quoted_dialogue = False
                output.append(line)
                i += 1
                continue

            # All-caps section headers
            if stripped.isupper() and len(stripped) > 5 and not stripped.startswith("==="):
                if self.current_speaker != "Charon":
                    output.append("[Charon]\n")
                    self.current_speaker = "Charon"
                self.in_quoted_dialogue = False
                output.append(line)
                i += 1
                continue

            # Check for dialogue start
            dialogue_speaker = self.detect_dialogue_start(line)
            if dialogue_speaker:
                # Speaker identified - add tag and enter dialogue mode
                if self.current_speaker != dialogue_speaker:
                    output.append(f"[{dialogue_speaker}]\n")
                    self.current_speaker = dialogue_speaker
                self.in_quoted_dialogue = True
                self.dialogue_speaker = dialogue_speaker
                output.append(line)
                i += 1
                continue

            # Handle lines within dialogue
            if self.in_quoted_dialogue:
                # Check if this is a narrator interjection
                if self.is_narrator_interjection(line):
                    # Brief narrator moment
                    if self.current_speaker != "Charon":
                        output.append("[Charon]\n")
                        self.current_speaker = "Charon"
                    output.append(line)
                    # Check next line - if it continues dialogue, switch back
                    if i + 1 < len(lines):
                        next_line = lines[i + 1].strip()
                        if next_line.startswith('"') or next_line.startswith("'"):
                            # Continue dialogue with same speaker
                            if self.current_speaker != self.dialogue_speaker:
                                output.append(f"[{self.dialogue_speaker}]\n")
                                self.current_speaker = self.dialogue_speaker
                    i += 1
                    continue

                # Check if dialogue ends
                if stripped.endswith('"') and not (i + 1 < len(lines) and
                                                   lines[i + 1].strip().startswith('"')):
                    # Dialogue likely ending
                    output.append(line)
                    self.in_quoted_dialogue = False
                    i += 1
                    continue

                # Continue in dialogue
                output.append(line)
                i += 1
                continue

            # Outside dialogue - check for narrator patterns
            if stripped.startswith("Right then") or stripped.startswith("At that time"):
                if self.current_speaker != "Charon":
                    output.append("[Charon]\n")
                    self.current_speaker = "Charon"
                output.append(line)
                i += 1
                continue

            if stripped.startswith("Listen now"):
                if self.current_speaker != "Rasalgethi":
                    output.append("[Rasalgethi]\n")
                    self.current_speaker = "Rasalgethi"
                output.append(line)
                i += 1
                continue

            # Default: continue with current speaker
            output.append(line)
            i += 1

        # Write output
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(output)

        print(f"✓ Processed {len(lines):,} lines")
        print(f"✓ Output written to: {output_path}")

def main():
    input_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/Trade_Publication_Edition_One.txt"
    output_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript.txt"

    print("Processing Lotus Sutra Trade Edition with refined speaker detection...")
    print(f"Input: {input_file}")
    print(f"Output: {output_file}\n")

    tagger = RefinedSpeakerTagger()
    tagger.process_file(input_file, output_file)
    print("\n✓ File ready for professional voice narration!")

if __name__ == "__main__":
    main()
