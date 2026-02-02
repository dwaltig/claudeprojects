#!/usr/bin/env python3
"""
Final definitive footnote renumbering script.
This handles both footnote definitions and in-text citations.
"""

import re

def fix_footnotes(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # STEP 1: Fix footnote DEFINITIONS
    # These are line-start patterns like [^N]:
    # We'll use very specific text to avoid ambiguity

    definitions = [
        # OLD -> NEW mappings with unique text identifiers
        (r'^\[^44\]: On the two obscurations', r'[^47]: On the two obscurations'),
        (r'^\[^43\]: Vincent L\. Wimbush', r'[^46]: Vincent L. Wimbush'),
        (r'^\[^42\]: Fred Moten', r'[^45]: Fred Moten'),
        (r'^\[^41\]: Christina Sharpe', r'[^44]: Christina Sharpe'),
        (r'^\[^40\]: Saidiya Hartman, \*Wayward Lives, Beautiful', r'[^43]: Saidiya Hartman, *Wayward Lives, Beautiful'),
        (r'^\[^39\]: Houston A\. Baker, \*Blues, Ideology, and Afro-American Literature: A Vernacular Theory\* \(Chicago', r'[^42]: Houston A. Baker, *Blues, Ideology, and Afro-American Literature: A Vernacular Theory* (Chicago'),
        (r'^\[^38\]: Jan Nattier, "The Heart Sūtra: A Chinese Apocryphal Text\?" \*Journal', r'[^41]: Jan Nattier, "The Heart Sūtra: A Chinese Apocryphal Text?" *Journal'),
        (r'^\[^37\]: Robin DiAngelo', r'[^40]: Robin DiAngelo'),
        (r'^\[^36\]: Manuel, \*The Way of Tenderness\*, 47-52', r'[^39]: Manuel, *The Way of Tenderness*, 47-52'),
        (r'^\[^35\]: Kamilah Majied, \*Joyfully', r'[^38]: Kamilah Majied, *Joyfully'),
        (r'^\[^34\]: John Searle', r'[^37]: John Searle'),
        (r'^\[^33\]: Stephen W\. Porges', r'[^36]: Stephen W. Porges'),
        (r'^\[^32\]: James H\. Cone', r'[^35]: James H. Cone'),
        (r'^\[^31\]: Pamela Ayo Yetunde', r'[^34]: Pamela Ayo Yetunde'),
        (r'^\[^30\]: Ralph H\. Craig III', r'[^33]: Ralph H. Craig III'),
        (r'^\[^29\]: Howard Thurman', r'[^32]: Howard Thurman'),
        (r'^\[^28\]: Albert Murray', r'[^31]: Albert Murray'),
        (r'^\[^27\]: Hartman, \*Wayward Lives\*', r'[^30]: Hartman, *Wayward Lives*'),
        (r'^\[^26\]: Houston A\. Baker, \*Blues, Ideology', r'[^29]: Houston A. Baker, *Blues, Ideology'),
        (r'^\[^25a\]: Nāgārjuna, \*Mūlamadhyamakakārikā\* 24\.18', r'[^28a]: Nāgārjuna, *Mūlamadhyamakakārikā* 24.18'),
        (r'^\[^25\]: Nāgārjuna, \*Mūlamadhyamakakārikā\* \(The Fundamental', r'[^28]: Nāgārjuna, *Mūlamadhyamakakārikā* (The Fundamental'),
        (r'^\[^24\]: Jon Kabat-Zinn', r'[^27]: Jon Kabat-Zinn'),
        (r'^\[^23\]: Thich Nhat Hanh', r'[^26]: Thich Nhat Hanh'),
        (r'^\[^22\]: Manuel, \*The Way of Tenderness\*, 47-52', r'[^25]: Manuel, *The Way of Tenderness*, 47-52'),
        (r'^\[^21\]: Saidiya Hartman, \*Wayward Lives', r'[^24]: Saidiya Hartman, *Wayward Lives'),
        (r'^\[^20\]: \*Heart Sutra Reborn\*', r'[^23]: *Heart Sutra Reborn*'),
        (r'^\[^19\]: Patterson\'s analysis', r'[^22]: Patterson\'s analysis'),
        (r'^\[^18\]: Orlando Patterson', r'[^21]: Orlando Patterson'),
        (r'^\[^17\]: Ralph Ellison', r'[^20]: Ralph Ellison'),
        (r'^\[^16\]: Xuanzang \(玄奘', r'[^19]: Xuanzang (玄奘'),
        (r'^\[^15\]: This line is adapted', r'[^18]: This line is adapted'),
        (r'^\[^14\]: See Chün-fang Yü', r'[^17]: See Chün-fang Yü'),
        (r'^\[^13\]: Angela Y\. Davis', r'[^16]: Angela Y. Davis'),
        (r'^\[^12\]: This phrase is coined', r'[^15]: This phrase is coined'),
        (r'^\[^11\]: Woods, \*Development Arrested\*, 25-29\. The "Blues Block"', r'[^14]: Woods, *Development Arrested*, 25-29. The "Blues Block"'),
        (r'^\[^10\]: Woods, \*Development Arrested\*, 25-29\.$', r'[^13]: Woods, *Development Arrested*, 25-29.'),
        (r'^\[^9\]: The concept of "groundlessness', r'[^12]: The concept of "groundlessness'),
        (r'^\[^8\]: Kazuaki Tanahashi', r'[^11]: Kazuaki Tanahashi'),
        (r'^\[^7\]: Stefano Zacchetti', r'[^10]: Stefano Zacchetti'),
        (r'^\[^6\]: Jan Nattier, "The Heart Sūtra: A Chinese Apocryphal', r'[^9]: Jan Nattier, "The Heart Sūtra: A Chinese Apocryphal'),
        # Note: [^5]: Lopez is already [^8], and [^5]: Vesely-Flad stays as [^5]
        # Note: [^6]: Manuel stays as [^6]
        # Note: [^7]: Willis stays as [^7]
        # The original [^8] (Lopez) is already correct
    ]

    # Apply definition replacements
    for pattern, replacement in definitions:
        content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

    # STEP 2: Fix in-text CITATIONS
    # Split into sections to handle [^5], [^6], [^7] ambiguity
    # The new [^5], [^6], [^7] appear in Section 1 (Introduction)
    # The old [^5], [^6], [^7] appear from Section 2 onward

    # Find section 2
    section_2_match = re.search(r'^## 2\. The Heart Sūtra as Crisis Text', content, re.MULTILINE)

    if section_2_match:
        intro = content[:section_2_match.start()]
        rest = content[section_2_match.start():]

        # In intro, [^5], [^6], [^7] are NEW - don't change them
        # In rest, [^5], [^6], [^7] are OLD - change to [^8], [^9], [^10]
        # But first handle all other numbers in reverse order in BOTH sections

        # Citations to update (reverse order to avoid conflicts)
        # Do NOT include 1-7 here as those are handled separately
        citation_updates = [
            (r'\[^44\]', r'[^47]'),
            (r'\[^43\]', r'[^46]'),
            (r'\[^42\]', r'[^45]'),
            (r'\[^41\]', r'[^44]'),
            (r'\[^40\]', r'[^43]'),
            (r'\[^39\]', r'[^42]'),
            (r'\[^38\]', r'[^41]'),
            (r'\[^37\]', r'[^40]'),
            (r'\[^36\]', r'[^39]'),
            (r'\[^35\]', r'[^38]'),
            (r'\[^34\]', r'[^37]'),
            (r'\[^33\]', r'[^36]'),
            (r'\[^32\]', r'[^35]'),
            (r'\[^31\]', r'[^34]'),
            (r'\[^30\]', r'[^33]'),
            (r'\[^29\]', r'[^32]'),
            (r'\[^28\]', r'[^31]'),
            (r'\[^27\]', r'[^30]'),
            (r'\[^26\]', r'[^29]'),
            (r'\[^25a\]', r'[^28a]'),
            (r'\[^25\]', r'[^28]'),
            (r'\[^24\]', r'[^27]'),
            (r'\[^23\]', r'[^26]'),
            (r'\[^22\]', r'[^25]'),
            (r'\[^21\]', r'[^24]'),
            (r'\[^20\]', r'[^23]'),
            (r'\[^19\]', r'[^22]'),
            (r'\[^18\]', r'[^21]'),
            (r'\[^17\]', r'[^20]'),
            (r'\[^16\]', r'[^19]'),
            (r'\[^15\]', r'[^18]'),
            (r'\[^14\]', r'[^17]'),
            (r'\[^13\]', r'[^16]'),
            (r'\[^12\]', r'[^15]'),
            (r'\[^11\]', r'[^14]'),
            (r'\[^10\]', r'[^13]'),
            (r'\[^9\]', r'[^12]'),
            (r'\[^8\]', r'[^11]'),
        ]

        # Apply to both sections
        for old, new in citation_updates:
            intro = intro.replace(old, new)
            rest = rest.replace(old, new)

        # Now handle [^5], [^6], [^7] in rest section only
        rest = rest.replace('[^7]', '[^10]')
        rest = rest.replace('[^6]', '[^9]')
        rest = rest.replace('[^5]', '[^8]')

        content = intro + rest
    else:
        # Fallback: treat entire document the same way
        citation_updates = [
            (r'\[^44\]', r'[^47]'),
            (r'\[^43\]', r'[^46]'),
            (r'\[^42\]', r'[^45]'),
            (r'\[^41\]', r'[^44]'),
            (r'\[^40\]', r'[^43]'),
            (r'\[^39\]', r'[^42]'),
            (r'\[^38\]', r'[^41]'),
            (r'\[^37\]', r'[^40]'),
            (r'\[^36\]', r'[^39]'),
            (r'\[^35\]', r'[^38]'),
            (r'\[^34\]', r'[^37]'),
            (r'\[^33\]', r'[^36]'),
            (r'\[^32\]', r'[^35]'),
            (r'\[^31\]', r'[^34]'),
            (r'\[^30\]', r'[^33]'),
            (r'\[^29\]', r'[^32]'),
            (r'\[^28\]', r'[^31]'),
            (r'\[^27\]', r'[^30]'),
            (r'\[^26\]', r'[^29]'),
            (r'\[^25a\]', r'[^28a]'),
            (r'\[^25\]', r'[^28]'),
            (r'\[^24\]', r'[^27]'),
            (r'\[^23\]', r'[^26]'),
            (r'\[^22\]', r'[^25]'),
            (r'\[^21\]', r'[^24]'),
            (r'\[^20\]', r'[^23]'),
            (r'\[^19\]', r'[^22]'),
            (r'\[^18\]', r'[^21]'),
            (r'\[^17\]', r'[^20]'),
            (r'\[^16\]', r'[^19]'),
            (r'\[^15\]', r'[^18]'),
            (r'\[^14\]', r'[^17]'),
            (r'\[^13\]', r'[^16]'),
            (r'\[^12\]', r'[^15]'),
            (r'\[^11\]', r'[^14]'),
            (r'\[^10\]', r'[^13]'),
            (r'\[^9\]', r'[^12]'),
            (r'\[^8\]', r'[^11]'),
            (r'\[^7\]', r'[^10]'),
            (r'\[^6\]', r'[^9]'),
            (r'\[^5\]', r'[^8]'),
        ]

        for old, new in citation_updates:
            content = content.replace(old, new)

    return content

if __name__ == '__main__':
    input_file = '/Users/williamaltig/claudeprojects/Heart Sutra Project/ARTICLE_Hellhounds_VERSION_D.md'
    output_file = '/Users/williamaltig/claudeprojects/Heart Sutra Project/ARTICLE_Hellhounds_VERSION_D.md.fixed'

    fixed_content = fix_footnotes(input_file)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)

    print(f"Fixed file written to: {output_file}")
    print("\nVerification steps:")
    print("1. Check that footnotes 1-4 are unchanged")
    print("2. Check that footnotes 5-7 are: Vesely-Flad, Manuel, Willis")
    print("3. Check that Lopez is now [^8]")
    print("4. Check that last footnote is [^47]")
    print("\nReview the file, then:")
    print(f"  mv {output_file} {input_file}")
