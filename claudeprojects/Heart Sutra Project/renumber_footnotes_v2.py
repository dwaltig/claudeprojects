#!/usr/bin/env python3
"""
Systematically renumber footnotes in ARTICLE_Hellhounds_VERSION_D.md
Version 2: More careful handling of footnote definitions section
"""

import re

def renumber_footnotes(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Process line by line to have more control
    output_lines = []
    in_footnotes_section = False

    for i, line in enumerate(lines):
        # Detect when we've entered the footnotes section
        if line.strip() == '## Notes':
            in_footnotes_section = True
            output_lines.append(line)
            continue

        # If we're in footnotes section, handle footnote definitions carefully
        if in_footnotes_section:
            # Handle each footnote definition individually with unique identifiers

            # Keep [^1] through [^4] as is
            if re.match(r'^\[^1\]:', line):
                output_lines.append(line)
            elif re.match(r'^\[^2\]:', line):
                output_lines.append(line)
            elif re.match(r'^\[^3\]:', line):
                output_lines.append(line)
            elif re.match(r'^\[^4\]:', line):
                output_lines.append(line)

            # NEW [^5], [^6], [^7] - these are already correct
            elif line.startswith('[^5]: Rima Vesely-Flad'):
                output_lines.append(line)
            elif line.startswith('[^6]: Zenju Earthlyn Manuel'):
                output_lines.append(line)
            elif line.startswith('[^7]: Jan Willis'):
                output_lines.append(line)

            # OLD [^5] -> [^8] (Lopez)
            elif line.startswith('[^5]: Donald S. Lopez') or line.startswith('[^8]: Donald S. Lopez'):
                output_lines.append(line.replace('[^5]:', '[^8]:').replace('[^8]:', '[^8]:'))

            # OLD [^6] -> [^9] (Nattier first instance)
            elif line.startswith('[^6]: Jan Nattier, "The Heart'):
                output_lines.append(line.replace('[^6]:', '[^9]:'))

            # OLD [^7] -> [^10] (Zacchetti)
            elif line.startswith('[^7]: Stefano Zacchetti'):
                output_lines.append(line.replace('[^7]:', '[^10]:'))

            # [^8] -> [^11] (Tanahashi)
            elif line.startswith('[^8]: Kazuaki Tanahashi'):
                output_lines.append(line.replace('[^8]:', '[^11]:'))

            # [^9] -> [^12] (Pema Chödrön)
            elif line.startswith('[^9]: The concept of "groundlessness'):
                output_lines.append(line.replace('[^9]:', '[^12]:'))

            # [^10] -> [^13] (Woods first instance)
            elif re.match(r'^\[^10\]: Woods, \*Development Arrested\*, 25-29\.\s*$', line):
                output_lines.append(line.replace('[^10]:', '[^13]:'))

            # [^11] -> [^14] (Woods Blues Block)
            elif line.startswith('[^11]: Woods, *Development Arrested*, 25-29. The "Blues Block"'):
                output_lines.append(line.replace('[^11]:', '[^14]:'))

            # [^12] -> [^15] (coined here)
            elif line.startswith('[^12]: This phrase is coined'):
                output_lines.append(line.replace('[^12]:', '[^15]:'))

            # [^13] -> [^16] (Angela Davis)
            elif line.startswith('[^13]: Angela Y. Davis'):
                output_lines.append(line.replace('[^13]:', '[^16]:'))

            # [^14] -> [^17] (Chün-fang Yü)
            elif line.startswith('[^14]: See Chün-fang Yü'):
                output_lines.append(line.replace('[^14]:', '[^17]:'))

            # [^15] -> [^18] (vernacular translation)
            elif line.startswith('[^15]: This line is adapted'):
                output_lines.append(line.replace('[^15]:', '[^18]:'))

            # [^16] -> [^19] (Xuanzang Taishō)
            elif line.startswith('[^16]: Xuanzang'):
                output_lines.append(line.replace('[^16]:', '[^19]:'))

            # [^17] -> [^20] (Ellison)
            elif line.startswith('[^17]: Ralph Ellison'):
                output_lines.append(line.replace('[^17]:', '[^20]:'))

            # [^18] -> [^21] (Patterson first)
            elif re.match(r'^\[^18\]: Orlando Patterson.*Social Death', line):
                output_lines.append(line.replace('[^18]:', '[^21]:'))

            # [^19] -> [^22] (Patterson analysis)
            elif line.startswith('[^19]: Patterson\'s analysis'):
                output_lines.append(line.replace('[^19]:', '[^22]:'))

            # [^20] -> [^23] (Heart Sutra Reborn)
            elif line.startswith('[^20]: *Heart Sutra Reborn*'):
                output_lines.append(line.replace('[^20]:', '[^23]:'))

            # [^21] -> [^24] (Hartman Wayward Lives first)
            elif re.match(r'^\[^21\]: Saidiya Hartman, \*Wayward Lives', line):
                output_lines.append(line.replace('[^21]:', '[^24]:'))

            # [^22] -> [^25] (Manuel Way of Tenderness first)
            elif re.match(r'^\[^22\]: Manuel, \*The Way of Tenderness\*, 47-52', line):
                output_lines.append(line.replace('[^22]:', '[^25]:'))

            # [^23] -> [^26] (Thich Nhat Hanh)
            elif line.startswith('[^23]: Thich Nhat Hanh'):
                output_lines.append(line.replace('[^23]:', '[^26]:'))

            # [^24] -> [^27] (Kabat-Zinn)
            elif line.startswith('[^24]: Jon Kabat-Zinn'):
                output_lines.append(line.replace('[^24]:', '[^27]:'))

            # [^25] -> [^28] (Nāgārjuna MMK)
            elif line.startswith('[^25]: Nāgārjuna, *Mūlamadhyamakakārikā* (The Fundamental'):
                output_lines.append(line.replace('[^25]:', '[^28]:'))

            # [^25a] -> [^28a] (Nāgārjuna MMK 24.18)
            elif line.startswith('[^25a]: Nāgārjuna, *Mūlamadhyamakakārikā* 24.18'):
                output_lines.append(line.replace('[^25a]:', '[^28a]:'))

            # [^26] -> [^29] (Baker first)
            elif re.match(r'^\[^26\]: Houston A\. Baker, \*Blues, Ideology', line):
                output_lines.append(line.replace('[^26]:', '[^29]:'))

            # [^27] -> [^30] (Hartman Wayward Lives short)
            elif re.match(r'^\[^27\]: Hartman, \*Wayward Lives', line):
                output_lines.append(line.replace('[^27]:', '[^30]:'))

            # [^28] -> [^31] (Murray)
            elif line.startswith('[^28]: Albert Murray'):
                output_lines.append(line.replace('[^28]:', '[^31]:'))

            # [^29] -> [^32] (Thurman)
            elif line.startswith('[^29]: Howard Thurman'):
                output_lines.append(line.replace('[^29]:', '[^32]:'))

            # [^30] -> [^33] (Craig)
            elif line.startswith('[^30]: Ralph H. Craig III'):
                output_lines.append(line.replace('[^30]:', '[^33]:'))

            # [^31] -> [^34] (Yetunde)
            elif line.startswith('[^31]: Pamela Ayo Yetunde'):
                output_lines.append(line.replace('[^31]:', '[^34]:'))

            # [^32] -> [^35] (Cone)
            elif line.startswith('[^32]: James H. Cone'):
                output_lines.append(line.replace('[^32]:', '[^35]:'))

            # [^33] -> [^36] (Porges)
            elif line.startswith('[^33]: Stephen W. Porges'):
                output_lines.append(line.replace('[^33]:', '[^36]:'))

            # [^34] -> [^37] (Searle)
            elif line.startswith('[^34]: John Searle'):
                output_lines.append(line.replace('[^34]:', '[^37]:'))

            # [^35] -> [^38] (Majied Joyfully Just)
            elif line.startswith('[^35]: Kamilah Majied, *Joyfully'):
                output_lines.append(line.replace('[^35]:', '[^38]:'))

            # [^36] -> [^39] (Manuel second)
            elif re.match(r'^\[^36\]: Manuel, \*The Way of Tenderness\*, 47-52', line):
                output_lines.append(line.replace('[^36]:', '[^39]:'))

            # [^37] -> [^40] (DiAngelo)
            elif line.startswith('[^37]: Robin DiAngelo'):
                output_lines.append(line.replace('[^37]:', '[^40]:'))

            # [^38] -> [^41] (Nattier second)
            elif line.startswith('[^38]: Jan Nattier, "The Heart Sūtra: A Chinese Apocryphal Text?" *Journal'):
                output_lines.append(line.replace('[^38]:', '[^41]:'))

            # [^39] -> [^42] (Baker second)
            elif re.match(r'^\[^39\]: Houston A\. Baker, \*Blues, Ideology.*\(Chicago', line):
                output_lines.append(line.replace('[^39]:', '[^42]:'))

            # [^40] -> [^43] (Hartman third)
            elif line.startswith('[^40]: Saidiya Hartman, *Wayward Lives, Beautiful'):
                output_lines.append(line.replace('[^40]:', '[^43]:'))

            # [^41] -> [^44] (Sharpe)
            elif line.startswith('[^41]: Christina Sharpe'):
                output_lines.append(line.replace('[^41]:', '[^44]:'))

            # [^42] -> [^45] (Moten)
            elif line.startswith('[^42]: Fred Moten'):
                output_lines.append(line.replace('[^42]:', '[^45]:'))

            # [^43] -> [^46] (Wimbush)
            elif line.startswith('[^43]: Vincent L. Wimbush'):
                output_lines.append(line.replace('[^43]:', '[^46]:'))

            # [^44] -> [^47] (Tibetan exegesis)
            elif line.startswith('[^44]: On the two obscurations'):
                output_lines.append(line.replace('[^44]:', '[^47]:'))

            else:
                # Any other line in footnotes section (blank lines, continuations)
                output_lines.append(line)
        else:
            # We're in body text - need to renumber in-text citations
            # Do this in reverse order to avoid conflicts
            processed_line = line

            # Split into intro and rest to handle [^5], [^6], [^7] ambiguity
            # Actually, let's just process all citations in reverse numerical order

            # Define replacements in specific order
            replacements = [
                ('[^44]', '[^47]'),
                ('[^43]', '[^46]'),
                ('[^42]', '[^45]'),
                ('[^41]', '[^44]'),
                ('[^40]', '[^43]'),
                ('[^39]', '[^42]'),
                ('[^38]', '[^41]'),
                ('[^37]', '[^40]'),
                ('[^36]', '[^39]'),
                ('[^35]', '[^38]'),
                ('[^34]', '[^37]'),
                ('[^33]', '[^36]'),
                ('[^32]', '[^35]'),
                ('[^31]', '[^34]'),
                ('[^30]', '[^33]'),
                ('[^29]', '[^32]'),
                ('[^28]', '[^31]'),
                ('[^27]', '[^30]'),
                ('[^26]', '[^29]'),
                ('[^25a]', '[^28a]'),
                ('[^25]', '[^28]'),
                ('[^24]', '[^27]'),
                ('[^23]', '[^26]'),
                ('[^22]', '[^25]'),
                ('[^21]', '[^24]'),
                ('[^20]', '[^23]'),
                ('[^19]', '[^22]'),
                ('[^18]', '[^21]'),
                ('[^17]', '[^20]'),
                ('[^16]', '[^19]'),
                ('[^15]', '[^18]'),
                ('[^14]', '[^17]'),
                ('[^13]', '[^16]'),
                ('[^12]', '[^15]'),
                ('[^11]', '[^14]'),
                ('[^10]', '[^13]'),
                ('[^9]', '[^12]'),
                ('[^8]', '[^11]'),
            ]

            # For [^5], [^6], [^7] we need to be careful
            # Only replace them after line 27 (after the introduction)
            line_num = i + 1
            if line_num > 27:  # After introduction
                replacements.extend([
                    ('[^7]', '[^10]'),
                    ('[^6]', '[^9]'),
                    ('[^5]', '[^8]'),
                ])

            for old, new in replacements:
                processed_line = processed_line.replace(old, new)

            output_lines.append(processed_line)

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)

    print(f"Renumbered footnotes written to {output_file}")
    print("\nVerification:")
    print("- Footnotes 1-4 should be unchanged")
    print("- NEW footnotes 5-7 should be: Vesely-Flad, Manuel, Willis")
    print("- Lopez should now be [^8]")
    print("- Nattier (first instance) should now be [^9]")
    print("- Last footnote should be [^47] (Tibetan exegesis)")

if __name__ == '__main__':
    input_file = '/Users/williamaltig/claudeprojects/Heart Sutra Project/ARTICLE_Hellhounds_VERSION_D.md'
    output_file = '/Users/williamaltig/claudeprojects/Heart Sutra Project/ARTICLE_Hellhounds_VERSION_D_FIXED.md'
    renumber_footnotes(input_file, output_file)
