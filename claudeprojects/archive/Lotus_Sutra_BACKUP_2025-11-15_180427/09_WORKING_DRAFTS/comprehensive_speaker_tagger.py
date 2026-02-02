#!/usr/bin/env python3
"""
Comprehensive speaker tagger for Lotus Sutra - properly handles all dialogue patterns.
"""

import re
from typing import Optional, Tuple

class ComprehensiveTagger:
    def __init__(self):
        self.current_speaker = None
        self.in_quoted_speech = False
        self.speech_owner = None

    def identify_speaker_change(self, line: str, next_line: str = "") -> Optional[str]:
        """Identify if a new speaker begins on this line."""
        stripped = line.strip()
        next_stripped = next_line.strip() if next_line else ""

        # Check for direct speech attribution followed by quotes
        # Pattern: "X said/spoke:" followed by quotes

        # Mañjuśrī speaking
        if re.search(r"Mañjuśrī\s+(spoke|said|told|replied|answered|thought)", stripped):
            # If dialogue starts immediately or on next line
            if '"' in stripped or '"' in next_stripped or "'" in stripped:
                return "Gacrux"
            return None

        # Maitreya speaking
        if re.search(r"Maitreya\s+(spoke|said|told|asked|replied|thought)", stripped):
            if '"' in stripped or '"' in next_stripped:
                return "Gacrux"
            return None

        # Buddha speaking - check for tone
        if re.search(r"(Buddha|World-Honored One|Thus Come One|Tathāgata)\s+(spoke|said|told|replied|declared|announced|proclaimed)", stripped):
            # Authoritative vs contemplative
            if any(word in stripped.lower() for word in ['command', 'declare', 'proclaim', 'announced']):
                return "Sadaltager"
            return "Iapetus"

        # Śāriputra and major disciples
        if re.search(r"Śāriputra\s+(spoke|said|told|replied)", stripped):
            return "Gacrux"

        # Other male disciples
        male_disciples = ['Mahākāśyapa', 'Ānanda', 'Subhūti', 'Rāhula', 'Mahā-Kātyāyana',
                         'Mahā-Maudgalyāyana', 'Aniruddha', 'Kapphina', 'Pūrṇa']
        for disciple in male_disciples:
            if re.search(rf"{disciple}\s+(spoke|said|told|replied)", stripped):
                return "Gacrux"

        # Female characters
        if re.search(r"Mahāprajāpatī\s+(spoke|said|told|asked)", stripped):
            return "Leda"

        if re.search(r"Yaśodharā\s+(spoke|said|told)", stripped):
            return "Leda"

        if "dragon girl" in stripped.lower() and any(v in stripped.lower() for v in ['spoke', 'said', 'told']):
            return "Schedar"  # Powerful female authority

        # Avalokiteśvara - ethereal, spiritual
        if re.search(r"Avalokiteśvara\s+(spoke|said|told)", stripped):
            return "Sulafat"

        return None

    def is_narrative_line(self, line: str) -> bool:
        """Check if line is narrative (not dialogue)."""
        stripped = line.strip()

        # Common narrative patterns
        narrative_starts = [
            'Right then', 'At that time', 'Right there',
            'And then', 'After', 'When', 'Before',
            'Now', 'There was', 'There were',
            'Every', 'All', 'These', 'Those',
            'Let me tell you'
        ]

        for start in narrative_starts:
            if stripped.startswith(start):
                return True

        # Check if it's describing action rather than speech
        action_verbs = ['went', 'came', 'saw', 'heard', 'thought', 'felt', 'stood', 'sat', 'walked']
        if any(f' {verb} ' in stripped.lower() for verb in action_verbs):
            if not stripped.startswith('"'):
                return True

        return False

    def process_file(self, input_path: str, output_path: str):
        """Process the entire file with comprehensive speaker detection."""
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        output = []

        for i, line in enumerate(lines):
            stripped = line.strip()
            next_line = lines[i+1] if i + 1 < len(lines) else ""

            # Empty lines - preserve
            if not stripped:
                output.append(line)
                continue

            # Front matter (before line 260)
            if i < 260:
                if self.current_speaker is None:
                    output.append("[Charon]\n")
                    self.current_speaker = "Charon"

                # Check for special intro sections
                if "THE DHARMA AND THE BLUES" in stripped:
                    if self.current_speaker != "Rasalgethi":
                        output.append("[Rasalgethi]\n")
                        self.current_speaker = "Rasalgethi"
                elif "INTRODUCTION:" in stripped or "HOW TO READ" in stripped:
                    if self.current_speaker != "Rasalgethi":
                        output.append("[Rasalgethi]\n")
                        self.current_speaker = "Rasalgethi"

                output.append(line)
                continue

            # Chapter headings
            if re.match(r'^CHAPTER\s+(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|' +
                       r'ELEVEN|TWELVE|THIRTEEN|FOURTEEN|FIFTEEN|SIXTEEN|SEVENTEEN|EIGHTEEN|' +
                       r'NINETEEN|TWENTY|TWENTY-ONE|TWENTY-TWO|TWENTY-THREE|TWENTY-FOUR|' +
                       r'TWENTY-FIVE|TWENTY-SIX|TWENTY-SEVEN|TWENTY-EIGHT|\d+)',
                       stripped, re.IGNORECASE):
                if self.current_speaker != "Charon":
                    output.append("[Charon]\n")
                    self.current_speaker = "Charon"
                self.in_quoted_speech = False
                output.append(line)
                continue

            # Section headings (ALL CAPS)
            if stripped.isupper() and len(stripped) > 5 and not stripped.startswith("==="):
                if self.current_speaker != "Charon":
                    output.append("[Charon]\n")
                    self.current_speaker = "Charon"
                self.in_quoted_speech = False
                output.append(line)
                continue

            # Check for speaker attribution
            new_speaker = self.identify_speaker_change(line, next_line)

            if new_speaker:
                # Found a speaker attribution
                if self.is_narrative_line(line):
                    # This line itself is narrative (e.g., "Right then, Mañjuśrī spoke...")
                    if self.current_speaker != "Charon":
                        output.append("[Charon]\n")
                        self.current_speaker = "Charon"
                    output.append(line)

                    # Next line likely starts the actual speech
                    if '"' in next_line or next_line.strip().startswith('"'):
                        self.in_quoted_speech = True
                        self.speech_owner = new_speaker
                        # Will add speaker tag before next line
                        continue
                else:
                    # Speaker attribution and speech start on same line
                    if self.current_speaker != new_speaker:
                        output.append(f"[{new_speaker}]\n")
                        self.current_speaker = new_speaker
                    self.in_quoted_speech = True
                    self.speech_owner = new_speaker
                    output.append(line)
                continue

            # Handle continuation of quoted speech
            if self.in_quoted_speech:
                # Check if we need to add speaker tag (previous line set us up for it)
                if self.speech_owner and self.current_speaker != self.speech_owner:
                    output.append(f"[{self.speech_owner}]\n")
                    self.current_speaker = self.speech_owner
                    self.speech_owner = None  # Clear it

                # Check if speech ends
                if stripped.endswith('"') and not stripped.startswith('"'):
                    # Likely end of speech
                    output.append(line)
                    # Check if next line continues
                    if i + 1 < len(lines):
                        next_stripped = lines[i+1].strip()
                        if not next_stripped.startswith('"'):
                            self.in_quoted_speech = False
                    continue

                # Continue in speech
                output.append(line)
                continue

            # Check for narrative transitions
            if self.is_narrative_line(line):
                if self.current_speaker != "Charon":
                    output.append("[Charon]\n")
                    self.current_speaker = "Charon"
                self.in_quoted_speech = False
                output.append(line)
                continue

            # Special: "Listen now" - storytelling voice
            if stripped.startswith("Listen now"):
                if self.current_speaker != "Rasalgethi":
                    output.append("[Rasalgethi]\n")
                    self.current_speaker = "Rasalgethi"
                output.append(line)
                continue

            # Default: preserve line with current speaker
            output.append(line)

        # Write output
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(output)

        print(f"✓ Processed {len(lines):,} lines")
        print(f"✓ Added speaker tags throughout")
        print(f"✓ Output: {output_path}")

def main():
    input_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/Trade_Publication_Edition_One.txt"
    output_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript.txt"

    print("=" * 70)
    print("LOTUS SUTRA SPEAKER TAGGER - Professional Voice Narration Edition")
    print("=" * 70)
    print(f"\nInput:  {input_file}")
    print(f"Output: {output_file}\n")

    tagger = ComprehensiveTagger()
    tagger.process_file(input_file, output_file)

    print("\n✓ File is ready for professional voice narration!")
    print("=" * 70)

if __name__ == "__main__":
    main()
