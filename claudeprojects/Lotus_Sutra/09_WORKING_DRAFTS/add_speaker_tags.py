#!/usr/bin/env python3
"""
Intelligently add speaker tags to the Lotus Sutra Trade Edition for professional narration.
"""

import re
from typing import List, Tuple, Optional

class SpeakerTagger:
    def __init__(self):
        self.current_speaker = None
        self.in_verse_section = False
        self.last_prose_speaker = None

    def get_speaker_for_line(self, line: str, line_num: int, context_lines: List[str]) -> Optional[str]:
        """Determine the appropriate speaker for a given line."""
        stripped = line.strip()

        # Empty lines don't change speaker
        if not stripped:
            return None

        # Front matter (before line 260) - use Charon for epic/cosmic narration
        if line_num < 260:
            # Introduction by author - use Rasalgethi for warm storytelling
            if "THE DHARMA AND THE BLUES" in stripped or "INTRODUCTION:" in stripped:
                return "Rasalgethi"
            # Default narrator
            return "Charon"

        # Chapter headings - always Charon
        if re.match(r'^CHAPTER\s+(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|ELEVEN|TWELVE|' +
                    r'THIRTEEN|FOURTEEN|FIFTEEN|SIXTEEN|SEVENTEEN|EIGHTEEN|NINETEEN|TWENTY|' +
                    r'TWENTY-ONE|TWENTY-TWO|TWENTY-THREE|TWENTY-FOUR|TWENTY-FIVE|TWENTY-SIX|' +
                    r'TWENTY-SEVEN|TWENTY-EIGHT|\d+)', stripped, re.IGNORECASE):
            return "Charon"

        # Section headings (all caps) - always Charon
        if stripped.isupper() and len(stripped) > 5 and not stripped.startswith("==="):
            return "Charon"

        # Check for quoted dialogue in verse - these are character voices
        if stripped.startswith('"') or stripped.startswith("'"):
            # In verse, Buddha's direct speech
            if any(word in stripped.lower() for word in ['buddha', 'dharma', 'teaching', 'path', 'beings']):
                return "Iapetus"  # Buddha's contemplative wisdom

        # Explicit speaker identification patterns
        # Buddha speaking
        buddha_patterns = [
            r'(Buddha|World-Honored One|Thus Come One|Tathāgata)\s+(said|spoke|told|replied|answered|declared|announced|proclaimed)',
            r'^(The Buddha|Buddha)\s+(?:then\s+)?(?:said|spoke|told)',
        ]
        for pattern in buddha_patterns:
            if re.search(pattern, stripped, re.IGNORECASE):
                # Check tone for appropriate voice
                if any(word in stripped.lower() for word in ['command', 'declare', 'proclaim']):
                    return "Sadaltager"  # Authoritative Buddha
                return "Iapetus"  # Default Buddha - contemplative wisdom

        # Mañjuśrī speaking
        if re.search(r"Mañjuśrī\s+(said|spoke|told|replied|answered|thought)", stripped):
            return "Gacrux"  # Noble, heroic male disciple

        # Maitreya speaking
        if re.search(r"Maitreya\s+(said|spoke|told|replied|answered|asked|thought)", stripped):
            return "Gacrux"  # Noble, heroic male disciple

        # Śāriputra speaking
        if re.search(r"Śāriputra\s+(said|spoke|told|replied|answered)", stripped):
            return "Gacrux"  # Noble, heroic male disciple

        # Other named male disciples
        male_disciples = ['Mahākāśyapa', 'Ānanda', 'Subhūti', 'Rāhula', 'Ājñāta-Kauṇḍinya',
                         'Mahā-Maudgalyāyana', 'Mahā-Kātyāyana', 'Aniruddha']
        for disciple in male_disciples:
            if re.search(rf"{disciple}\s+(said|spoke|told|replied|answered)", stripped):
                return "Gacrux"

        # Female characters - maternal wisdom and power
        if re.search(r"Mahāprajāpatī\s+(said|spoke|told|replied|answered)", stripped):
            return "Leda"  # Maternal wisdom, compassion

        if re.search(r"Yaśodharā\s+(said|spoke|told|replied|answered)", stripped):
            return "Leda"  # Maternal wisdom

        if re.search(r"dragon girl\s+(said|spoke|told|replied|answered)", stripped):
            return "Schedar"  # Powerful, authoritative female

        # Avalokiteśvara (bodhisattva of compassion) - could be either voice
        # Using ethereal/spiritual voice
        if re.search(r"Avalokiteśvara\s+(said|spoke|told|replied|answered)", stripped):
            return "Sulafat"  # Ethereal, spiritual, gentle

        # Narrative transitions
        if stripped.startswith("Right then") or stripped.startswith("At that time"):
            return "Charon"  # Default cosmic narrator

        # Storytelling openings
        if stripped.startswith("Listen now") or stripped.startswith("Let me tell you"):
            return "Rasalgethi"  # Warm, grandfatherly storytelling

        # Verse section detection
        # Check if we're in a verse section by looking at rhyme/rhythm patterns
        if re.search(r'(—|,)$', stripped) and len(stripped) < 80:
            # Likely verse - maintain continuity unless explicit speaker change
            return None

        # Parable and story sections - warm storytelling
        if re.search(r"(parable|story|once upon|there was a)", stripped, re.IGNORECASE):
            return "Rasalgethi"

        # Default: don't change speaker (None means continue with current)
        return None

    def process_file(self, input_path: str, output_path: str):
        """Process the entire file and add speaker tags."""
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        output_lines = []
        context_window = 5  # Look at nearby lines for context

        for i, line in enumerate(lines):
            # Get context lines
            context_start = max(0, i - context_window)
            context_end = min(len(lines), i + context_window + 1)
            context = lines[context_start:context_end]

            # Determine if we need a speaker tag
            new_speaker = self.get_speaker_for_line(line, i + 1, context)

            # Add speaker tag if speaker changed
            if new_speaker and new_speaker != self.current_speaker:
                output_lines.append(f"[{new_speaker}]\n")
                self.current_speaker = new_speaker

            # Add the actual line
            output_lines.append(line)

        # Write output
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(output_lines)

        print(f"✓ Processed {len(lines):,} lines")
        print(f"✓ Output written to: {output_path}")
        print(f"✓ File ready for professional narration")

def main():
    input_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/Trade_Publication_Edition_One.txt"
    output_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript.txt"

    print("Processing Lotus Sutra Trade Edition for narration...")
    print(f"Input: {input_file}")
    print(f"Output: {output_file}")
    print()

    tagger = SpeakerTagger()
    tagger.process_file(input_file, output_file)

if __name__ == "__main__":
    main()
