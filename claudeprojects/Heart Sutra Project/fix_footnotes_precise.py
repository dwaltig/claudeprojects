#!/usr/bin/env python3
"""
Precise footnote renumbering - handles duplicates correctly.
"""

import re

def fix_footnotes_precisely(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Track which footnote numbers we've seen in definitions
    seen_footnote_nums = {}
    output_lines = []

    # Pass 1: Fix footnote definitions
    for i, line in enumerate(lines):
        # Check if this is a footnote definition
        match = re.match(r'^\[^(\d+a?)\]:', line)
        if match:
            num = match.group(1)

            # Check if we've seen this number before
            if num in seen_footnote_nums:
                # This is a duplicate - needs renumbering
                # Map based on unique content
                if 'groundlessness' in line:
                    # [^9]: Pema -> [^12]
                    line = line.replace(f'[^{num}]:', '[^12]:', 1)
                elif 'Woods' in line and 'Blues Block' not in line and num == '10':
                    # [^10]: Woods (first) -> [^13]
                    line = line.replace(f'[^{num}]:', '[^13]:', 1)
                elif 'Blues Block' in line:
                    # [^11]: Woods Blues Block -> [^14]
                    line = line.replace(f'[^{num}]:', '[^14]:', 1)
                elif 'coined' in line:
                    # [^12]: coined -> [^15]
                    line = line.replace(f'[^{num}]:', '[^15]:', 1)
                elif 'Angela Y. Davis' in line:
                    # [^13]: Davis -> [^16]
                    line = line.replace(f'[^{num}]:', '[^16]:', 1)
                elif 'Chün-fang Yü' in line:
                    # [^14]: Yü -> [^17]
                    line = line.replace(f'[^{num}]:', '[^17]:', 1)
                elif 'adapted from the author' in line:
                    # [^15]: adapted -> [^18]
                    line = line.replace(f'[^{num}]:', '[^18]:', 1)
                elif 'Xuanzang' in line and '玄奘' in line:
                    # [^16]: Xuanzang -> [^19]
                    line = line.replace(f'[^{num}]:', '[^19]:', 1)
                elif 'Ralph Ellison' in line:
                    # [^17]: Ellison -> [^20]
                    line = line.replace(f'[^{num}]:', '[^20]:', 1)
                elif 'Orlando Patterson' in line:
                    # [^18]: Patterson -> [^21]
                    line = line.replace(f'[^{num}]:', '[^21]:', 1)
                elif "Patterson's analysis" in line or 'Patterson\'s analysis' in line:
                    # [^19]: Patterson analysis -> [^22]
                    line = line.replace(f'[^{num}]:', '[^22]:', 1)
                elif 'Heart Sutra Reborn' in line:
                    # [^20]: Heart Sutra Reborn -> [^23]
                    line = line.replace(f'[^{num}]:', '[^23]:', 1)
                elif 'Saidiya Hartman, *Wayward Lives' in line:
                    # [^21]: Hartman Wayward Lives (full) -> [^24]
                    line = line.replace(f'[^{num}]:', '[^24]:', 1)
                elif 'Manuel, *The Way of Tenderness*, 47-52' in line and num == '22':
                    # [^22]: Manuel -> [^25]
                    line = line.replace(f'[^{num}]:', '[^25]:', 1)
                elif 'Thich Nhat Hanh' in line:
                    # [^23]: Thich -> [^26]
                    line = line.replace(f'[^{num}]:', '[^26]:', 1)
                elif 'Jon Kabat-Zinn' in line:
                    # [^24]: Kabat-Zinn -> [^27]
                    line = line.replace(f'[^{num}]:', '[^27]:', 1)
                elif 'Nāgārjuna' in line and 'Fundamental' in line:
                    # [^25]: Nāgārjuna MMK -> [^28]
                    line = line.replace(f'[^{num}]:', '[^28]:', 1)
                elif 'Nāgārjuna' in line and '24.18' in line:
                    # [^25a]: Nāgārjuna 24.18 -> [^28a]
                    line = line.replace(f'[^{num}]:', '[^28a]:', 1)
                elif 'Houston A. Baker' in line and num == '26':
                    # [^26]: Baker -> [^29]
                    line = line.replace(f'[^{num}]:', '[^29]:', 1)
                elif 'Hartman, *Wayward Lives*' in line and num == '27':
                    # [^27]: Hartman (short) -> [^30]
                    line = line.replace(f'[^{num}]:', '[^30]:', 1)
                elif 'Albert Murray' in line:
                    # [^28]: Murray -> [^31]
                    line = line.replace(f'[^{num}]:', '[^31]:', 1)
                elif 'Howard Thurman' in line:
                    # [^29]: Thurman -> [^32]
                    line = line.replace(f'[^{num}]:', '[^32]:', 1)
                elif 'Ralph H. Craig III' in line:
                    # [^30]: Craig -> [^33]
                    line = line.replace(f'[^{num}]:', '[^33]:', 1)
                elif 'Pamela Ayo Yetunde' in line:
                    # [^31]: Yetunde -> [^34]
                    line = line.replace(f'[^{num}]:', '[^34]:', 1)
                elif 'James H. Cone' in line:
                    # [^32]: Cone -> [^35]
                    line = line.replace(f'[^{num}]:', '[^35]:', 1)
                elif 'Stephen W. Porges' in line:
                    # [^33]: Porges -> [^36]
                    line = line.replace(f'[^{num}]:', '[^36]:', 1)
                elif 'John Searle' in line:
                    # [^34]: Searle -> [^37]
                    line = line.replace(f'[^{num}]:', '[^37]:', 1)
                elif 'Kamilah Majied, *Joyfully' in line:
                    # [^35]: Majied Joyfully -> [^38]
                    line = line.replace(f'[^{num}]:', '[^38]:', 1)
                elif 'Manuel, *The Way of Tenderness*, 47-52' in line and num == '36':
                    # [^36]: Manuel (second) -> [^39]
                    line = line.replace(f'[^{num}]:', '[^39]:', 1)
                elif 'Robin DiAngelo' in line:
                    # [^37]: DiAngelo -> [^40]
                    line = line.replace(f'[^{num}]:', '[^40]:', 1)
                elif 'Jan Nattier' in line and '*Journal' in line:
                    # [^38]: Nattier (second) -> [^41]
                    line = line.replace(f'[^{num}]:', '[^41]:', 1)
                elif 'Houston A. Baker' in line and 'Chicago' in line:
                    # [^39]: Baker (second) -> [^42]
                    line = line.replace(f'[^{num}]:', '[^42]:', 1)
                elif 'Saidiya Hartman' in line and 'Beautiful Experiments' in line:
                    # [^40]: Hartman (third) -> [^43]
                    line = line.replace(f'[^{num}]:', '[^43]:', 1)
                elif 'Christina Sharpe' in line:
                    # [^41]: Sharpe -> [^44]
                    line = line.replace(f'[^{num}]:', '[^44]:', 1)
                elif 'Fred Moten' in line:
                    # [^42]: Moten -> [^45]
                    line = line.replace(f'[^{num}]:', '[^45]:', 1)
                elif 'Vincent L. Wimbush' in line:
                    # [^43]: Wimbush -> [^46]
                    line = line.replace(f'[^{num}]:', '[^46]:', 1)
                elif 'two obscurations' in line:
                    # [^44]: Tibetan -> [^47]
                    line = line.replace(f'[^{num}]:', '[^47]:', 1)

            # Mark this number as seen
            seen_footnote_nums[num] = True

        output_lines.append(line)

    # Now fix in-text citations
    content = ''.join(output_lines)

    # Split into intro and rest for [^5], [^6], [^7] ambiguity
    section_2_match = re.search(r'^## 2\. The Heart Sūtra as Crisis Text', content, re.MULTILINE)

    if section_2_match:
        intro = content[:section_2_match.start()]
        rest = content[section_2_match.start():]

        # In rest section, update all citations in reverse order
        citation_map = [
            ('[^47]', '[^TEMP47]'),  # Temporary markers to avoid conflicts
            ('[^46]', '[^TEMP46]'),
            ('[^45]', '[^TEMP45]'),
            ('[^44]', '[^TEMP44]'),
            ('[^43]', '[^TEMP43]'),
            ('[^42]', '[^TEMP42]'),
            ('[^41]', '[^TEMP41]'),
            ('[^40]', '[^TEMP40]'),
            ('[^39]', '[^TEMP39]'),
            ('[^38]', '[^TEMP38]'),
            ('[^37]', '[^TEMP37]'),
            ('[^36]', '[^TEMP36]'),
            ('[^35]', '[^TEMP35]'),
            ('[^34]', '[^TEMP34]'),
            ('[^33]', '[^TEMP33]'),
            ('[^32]', '[^TEMP32]'),
            ('[^31]', '[^TEMP31]'),
            ('[^30]', '[^TEMP30]'),
            ('[^29]', '[^TEMP29]'),
            ('[^28a]', '[^TEMP28a]'),
            ('[^28]', '[^TEMP28]'),
            ('[^27]', '[^TEMP27]'),
            ('[^26]', '[^TEMP26]'),
            ('[^25]', '[^TEMP25]'),
            ('[^24]', '[^TEMP24]'),
            ('[^23]', '[^TEMP23]'),
            ('[^22]', '[^TEMP22]'),
            ('[^21]', '[^TEMP21]'),
            ('[^20]', '[^TEMP20]'),
            ('[^19]', '[^TEMP19]'),
            ('[^18]', '[^TEMP18]'),
            ('[^17]', '[^TEMP17]'),
            ('[^16]', '[^TEMP16]'),
            ('[^15]', '[^TEMP15]'),
            ('[^14]', '[^TEMP14]'),
            ('[^13]', '[^TEMP13]'),
            ('[^12]', '[^TEMP12]'),
            ('[^11]', '[^TEMP11]'),
            ('[^10]', '[^TEMP10]'),
            ('[^9]', '[^TEMP9]'),
            ('[^8]', '[^TEMP8]'),
        ]

        # Apply temporary markers (intro gets 8-47, rest gets all)
        for old, temp in citation_map:
            intro = intro.replace(old, temp)
            rest = rest.replace(old, temp)

        # Now convert TEMP back to final numbers
        intro = intro.replace('[^TEMP', '[^')
        rest = rest.replace('[^TEMP', '[^')

        content = intro + rest
    else:
        # No section split found - just do straightforward replacement
        for num in range(47, 7, -1):
            if num == 25:
                content = content.replace('[^25a]', '[^28a]')
            content = content.replace(f'[^{num}]', f'[^{num}]')  # These are already correct

    return content

if __name__ == '__main__':
    input_file = '/Users/williamaltig/claudeprojects/Heart Sutra Project/ARTICLE_Hellhounds_VERSION_D.md'
    output_file = '/Users/williamaltig/claudeprojects/Heart Sutra Project/ARTICLE_Hellhounds_VERSION_D.md'

    fixed_content = fix_footnotes_precisely(input_file)

    # Write to output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)

    print(f"Fixed footnotes written to: {output_file}")
    print("\nDone! The original file has been updated.")
