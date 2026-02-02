#!/usr/bin/env python3
"""
Systematically renumber footnotes in ARTICLE_Hellhounds_VERSION_D.md
after new citations 5, 6, 7 were added.
"""

import re

def renumber_footnotes(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Mapping of old footnote numbers to new ones
    # New [^5], [^6], [^7] are already correct (Vesely-Flad, Manuel, Willis)
    # Old numbering needs to shift by +3 starting from old [^5] (Lopez)
    mapping = {
        # Keep 1-4 as is
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        # New additions are already correct as 5, 6, 7
        # Old [^5] and above need to become [^8] and above
        '5': '8',   # Lopez (when it's the OLD one, not Vesely-Flad)
        '6': '9',   # Nattier (when it's the OLD one, not Manuel)
        '7': '10',  # Zacchetti (when it's the OLD one, not Willis)
        '8': '11',  # Tanahashi
        '9': '12',  # Pema Chödrön
        '10': '13', # Woods
        '11': '14', # Woods (Blues Block)
        '12': '15', # Liturgical hospitality
        '13': '16', # Angela Davis
        '14': '17', # Chün-fang Yü
        '15': '18', # Vernacular translation
        '16': '19', # Xuanzang (Taishō)
        '17': '20', # Ralph Ellison
        '18': '21', # Orlando Patterson
        '19': '22', # Patterson (natal alienation)
        '20': '23', # Heart Sutra Reborn
        '21': '24', # Hartman
        '22': '25', # Manuel (The Way of Tenderness)
        '23': '26', # Thich Nhat Hanh
        '24': '27', # Jon Kabat-Zinn
        '25': '28', # Nāgārjuna (MMK)
        '25a': '28a', # Nāgārjuna (MMK 24.18)
        '26': '29', # Houston Baker
        '27': '30', # Hartman
        '28': '31', # Albert Murray
        '29': '32', # Howard Thurman
        '30': '33', # Ralph H. Craig III
        '31': '34', # Pamela Ayo Yetunde
        '32': '35', # James Cone
        '33': '36', # Stephen Porges
        '34': '37', # John Searle
        '35': '38', # Kamilah Majied (Joyfully Just)
        '36': '39', # Manuel (second reference)
        '37': '40', # Robin DiAngelo
        '38': '41', # Jan Nattier (second reference)
        '39': '42', # Houston Baker (second reference)
        '40': '43', # Hartman (second reference)
        '41': '44', # Christina Sharpe
        '42': '45', # Fred Moten
        '43': '46', # Vincent Wimbush
        '44': '47', # Tibetan exegesis
    }

    # We need to be careful and renumber in reverse order to avoid double-replacements
    # Also, we need to distinguish between citation contexts

    # First, let's identify the sections
    # The footnote DEFINITIONS section starts around line 228

    # Strategy: Work backwards from highest numbers to avoid conflicts
    for old_num in sorted([int(k) if k != '25a' and k != '28a' else 0 for k in mapping.keys() if k.isdigit() or k == '25a'], reverse=True):
        if old_num == 0:
            continue
        old_str = str(old_num)
        new_str = mapping[old_str]

        # Replace footnote definitions [^N]:
        # But we need to be careful - Lopez is [^5] but Vesely-Flad is also [^5]
        # We'll handle this by targeting specific unique text in each footnote

    # Let's use a more targeted approach with unique text snippets
    replacements = [
        # Fix duplicate definition numbers (these need specific context)
        (r'\[^5\]: Donald S\. Lopez Jr\.', '[^8]: Donald S. Lopez Jr.'),
        (r'\[^6\]: Jan Nattier, "The Heart Sūtra: A Chinese Apocryphal Text\?"', '[^9]: Jan Nattier, "The Heart Sūtra: A Chinese Apocryphal Text?"'),
        (r'\[^7\]: Stefano Zacchetti', '[^10]: Stefano Zacchetti'),
        (r'\[^8\]: Kazuaki Tanahashi', '[^11]: Kazuaki Tanahashi'),
        (r'\[^9\]: The concept of "groundlessness as gift"', '[^12]: The concept of "groundlessness as gift"'),
        (r'\[^10\]: Woods, \*Development Arrested\*, 25-29\.(?!\s*The "Blues Block")', '[^13]: Woods, *Development Arrested*, 25-29.'),
        (r'\[^11\]: Woods, \*Development Arrested\*, 25-29\. The "Blues Block"', '[^14]: Woods, *Development Arrested*, 25-29. The "Blues Block"'),
        (r'\[^12\]: This phrase is coined here', '[^15]: This phrase is coined here'),
        (r'\[^13\]: Angela Y\. Davis', '[^16]: Angela Y. Davis'),
        (r'\[^14\]: See Chün-fang Yü', '[^17]: See Chün-fang Yü'),
        (r'\[^15\]: This line is adapted from the author', '[^18]: This line is adapted from the author'),
        (r'\[^16\]: Xuanzang \(玄奘', '[^19]: Xuanzang (玄奘'),
        (r'\[^17\]: Ralph Ellison', '[^20]: Ralph Ellison'),
        (r'\[^18\]: Orlando Patterson, \*Slavery and Social Death\*: A Comparative Study\*', '[^21]: Orlando Patterson, *Slavery and Social Death: A Comparative Study*'),
        (r'\[^19\]: Patterson\'s analysis reveals', '[^22]: Patterson\'s analysis reveals'),
        (r'\[^20\]: \*Heart Sutra Reborn\*', '[^23]: *Heart Sutra Reborn*'),
        (r'\[^21\]: Saidiya Hartman, \*Wayward Lives', '[^24]: Saidiya Hartman, *Wayward Lives'),
        (r'\[^22\]: Manuel, \*The Way of Tenderness\*', '[^25]: Manuel, *The Way of Tenderness*'),
        (r'\[^23\]: Thich Nhat Hanh', '[^26]: Thich Nhat Hanh'),
        (r'\[^24\]: Jon Kabat-Zinn', '[^27]: Jon Kabat-Zinn'),
        (r'\[^25\]: Nāgārjuna, \*Mūlamadhyamakakārikā\* \(The Fundamental Wisdom', '[^28]: Nāgārjuna, *Mūlamadhyamakakārikā* (The Fundamental Wisdom'),
        (r'\[^25a\]: Nāgārjuna, \*Mūlamadhyamakakārikā\* 24\.18', '[^28a]: Nāgārjuna, *Mūlamadhyamakakārikā* 24.18'),
        (r'\[^26\]: Houston A\. Baker, \*Blues, Ideology', '[^29]: Houston A. Baker, *Blues, Ideology'),
        (r'\[^27\]: Hartman, \*Wayward Lives\*', '[^30]: Hartman, *Wayward Lives*'),
        (r'\[^28\]: Albert Murray', '[^31]: Albert Murray'),
        (r'\[^29\]: Howard Thurman', '[^32]: Howard Thurman'),
        (r'\[^30\]: Ralph H\. Craig III', '[^33]: Ralph H. Craig III'),
        (r'\[^31\]: Pamela Ayo Yetunde', '[^34]: Pamela Ayo Yetunde'),
        (r'\[^32\]: James H\. Cone', '[^35]: James H. Cone'),
        (r'\[^33\]: Stephen W\. Porges', '[^36]: Stephen W. Porges'),
        (r'\[^34\]: John Searle', '[^37]: John Searle'),
        (r'\[^35\]: Kamilah Majied, \*Joyfully Just', '[^38]: Kamilah Majied, *Joyfully Just'),
        (r'\[^36\]: Manuel, \*The Way of Tenderness\*, 47-52', '[^39]: Manuel, *The Way of Tenderness*, 47-52'),
        (r'\[^37\]: Robin DiAngelo', '[^40]: Robin DiAngelo'),
        (r'\[^38\]: Jan Nattier, "The Heart Sūtra: A Chinese Apocryphal Text\?" \*Journal', '[^41]: Jan Nattier, "The Heart Sūtra: A Chinese Apocryphal Text?" *Journal'),
        (r'\[^39\]: Houston A\. Baker, \*Blues, Ideology, and Afro-American Literature: A Vernacular Theory\* \(Chicago', '[^42]: Houston A. Baker, *Blues, Ideology, and Afro-American Literature: A Vernacular Theory* (Chicago'),
        (r'\[^40\]: Saidiya Hartman, \*Wayward Lives, Beautiful Experiments', '[^43]: Saidiya Hartman, *Wayward Lives, Beautiful Experiments'),
        (r'\[^41\]: Christina Sharpe', '[^44]: Christina Sharpe'),
        (r'\[^42\]: Fred Moten', '[^45]: Fred Moten'),
        (r'\[^43\]: Vincent L\. Wimbush', '[^46]: Vincent L. Wimbush'),
        (r'\[^44\]: On the two obscurations', '[^47]: On the two obscurations'),
    ]

    # Apply footnote definition replacements
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)

    # Now fix in-text citations
    # We need to be more careful here - only replace citations in the body text, not definitions
    # Split content into body and footnotes sections

    # Find where footnotes section starts (after "## Notes")
    notes_match = re.search(r'^## Notes\s*$', content, re.MULTILINE)
    if notes_match:
        body = content[:notes_match.start()]
        footnotes_section = content[notes_match.start():]
    else:
        # Fallback: find first [^1]: definition
        first_def = re.search(r'^\[^1\]:', content, re.MULTILINE)
        if first_def:
            body = content[:first_def.start()]
            footnotes_section = content[first_def.start():]
        else:
            body = content
            footnotes_section = ""

    # Now renumber in-text citations in body only (in reverse order to avoid conflicts)
    in_text_replacements = [
        (r'\[^44\]', '[^47]'),
        (r'\[^43\]', '[^46]'),
        (r'\[^42\]', '[^45]'),
        (r'\[^41\]', '[^44]'),
        (r'\[^40\]', '[^43]'),
        (r'\[^39\]', '[^42]'),
        (r'\[^38\]', '[^41]'),
        (r'\[^37\]', '[^40]'),
        (r'\[^36\]', '[^39]'),
        (r'\[^35\]', '[^38]'),
        (r'\[^34\]', '[^37]'),
        (r'\[^33\]', '[^36]'),
        (r'\[^32\]', '[^35]'),
        (r'\[^31\]', '[^34]'),
        (r'\[^30\]', '[^33]'),
        (r'\[^29\]', '[^32]'),
        (r'\[^28\]', '[^31]'),
        (r'\[^27\]', '[^30]'),
        (r'\[^26\]', '[^29]'),
        (r'\[^25a\]', '[^28a]'),
        (r'\[^25\]', '[^28]'),
        (r'\[^24\]', '[^27]'),
        (r'\[^23\]', '[^26]'),
        (r'\[^22\]', '[^25]'),
        (r'\[^21\]', '[^24]'),
        (r'\[^20\]', '[^23]'),
        (r'\[^19\]', '[^22]'),
        (r'\[^18\]', '[^21]'),
        (r'\[^17\]', '[^20]'),
        (r'\[^16\]', '[^19]'),
        (r'\[^15\]', '[^18]'),
        (r'\[^14\]', '[^17]'),
        (r'\[^13\]', '[^16]'),
        (r'\[^12\]', '[^15]'),
        (r'\[^11\]', '[^14]'),
        (r'\[^10\]', '[^13]'),
        (r'\[^9\]', '[^12]'),
        (r'\[^8\]', '[^11]'),
        (r'\[^7\]', '[^10]'),  # This will catch OLD [^7] (Zacchetti) but not NEW [^7] (Willis)
        (r'\[^6\]', '[^9]'),   # This will catch OLD [^6] (Nattier) but not NEW [^6] (Manuel)
        (r'\[^5\]', '[^8]'),   # This will catch OLD [^5] (Lopez) but not NEW [^5] (Vesely-Flad)
    ]

    # Actually, we need to be smarter. Let's find specific contexts for the ambiguous ones
    # Search for [^5], [^6], [^7] in body and determine context

    # Better approach: Replace specific instances by context
    # For instance, Lopez [^5] appears in body near "Donald Lopez has traced"
    body = re.sub(r'(\bDonald Lopez has traced its functions across Asia.*?\.)(\[^5\])', r'\1[^8]', body, flags=re.DOTALL)

    # Actually, let me re-read the text and find the exact citations
    # Let me use exact text matching for problematic cases

    # For now, let's just do the straightforward replacements in reverse order
    for pattern, replacement in in_text_replacements:
        # But skip 5, 6, 7 for now as they're ambiguous
        if pattern not in [r'\[^5\]', r'\[^6\]', r'\[^7\]']:
            body = re.sub(pattern, replacement, body)

    # Now handle the tricky [^5], [^6], [^7] cases
    # The NEW ones appear early in the document (Introduction section)
    # The OLD ones appear later

    # Find the Introduction section and Section 2
    intro_end = body.find('## 2. The Heart Sūtra as Crisis Text')
    if intro_end > 0:
        intro_section = body[:intro_end]
        rest_of_body = body[intro_end:]

        # In intro, [^5], [^6], [^7] are NEW (Vesely-Flad, Manuel, Willis) - keep them
        # In rest, [^5], [^6], [^7] are OLD and need to become [^8], [^9], [^10]
        rest_of_body = re.sub(r'\[^7\]', '[^10]', rest_of_body)
        rest_of_body = re.sub(r'\[^6\]', '[^9]', rest_of_body)
        rest_of_body = re.sub(r'\[^5\]', '[^8]', rest_of_body)

        body = intro_section + rest_of_body
    else:
        # Fallback: just replace all
        body = re.sub(r'\[^7\]', '[^10]', body)
        body = re.sub(r'\[^6\]', '[^9]', body)
        body = re.sub(r'\[^5\]', '[^8]', body)

    # Recombine
    content = body + footnotes_section

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Renumbered footnotes written to {output_file}")
    print("\nPlease review the changes carefully before using the output file!")

if __name__ == '__main__':
    input_file = '/Users/williamaltig/claudeprojects/Heart Sutra Project/ARTICLE_Hellhounds_VERSION_D.md'
    output_file = '/Users/williamaltig/claudeprojects/Heart Sutra Project/ARTICLE_Hellhounds_VERSION_D_RENUMBERED.md'
    renumber_footnotes(input_file, output_file)
