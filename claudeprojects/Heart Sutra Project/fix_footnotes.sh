#!/bin/bash
# Systematic footnote renumbering script
# Process in reverse order (high to low) to avoid conflicts

INPUT="ARTICLE_Hellhounds_VERSION_D.md"
OUTPUT="ARTICLE_Hellhounds_VERSION_D_RENUMBERED_FINAL.md"

# Start with a copy
cp "$INPUT" "$OUTPUT"

# Function to replace footnote citations in body text (after introduction)
# We'll use line number ranges to be more precise

# First, let's renumber footnote DEFINITIONS in the Notes section
# These appear starting around line 234

# Change [^44]: -> [^47]: (Tibetan exegesis)
sed -i.bak1 's/^\[^44\]: On the two obscurations/[^47]: On the two obscurations/' "$OUTPUT"

# Change [^43]: -> [^46]: (Wimbush)
sed -i.bak2 's/^\[^43\]: Vincent L\. Wimbush/[^46]: Vincent L. Wimbush/' "$OUTPUT"

# Change [^42]: -> [^45]: (Moten)
sed -i.bak3 's/^\[^42\]: Fred Moten/[^45]: Fred Moten/' "$OUTPUT"

# Change [^41]: -> [^44]: (Sharpe)
sed -i.bak4 's/^\[^41\]: Christina Sharpe/[^44]: Christina Sharpe/' "$OUTPUT"

# Change [^40]: -> [^43]: (Hartman Wayward Lives full)
sed -i.bak5 's/^\[^40\]: Saidiya Hartman, \*Wayward Lives, Beautiful/[^43]: Saidiya Hartman, *Wayward Lives, Beautiful/' "$OUTPUT"

# Change [^39]: -> [^42]: (Baker second with Chicago)
sed -i.bak6 's/^\[^39\]: Houston A\. Baker, \*Blues, Ideology, and Afro-American Literature: A Vernacular Theory\* (Chicago/[^42]: Houston A. Baker, *Blues, Ideology, and Afro-American Literature: A Vernacular Theory* (Chicago/' "$OUTPUT"

# Change [^38]: -> [^41]: (Nattier second with Journal)
sed -i.bak7 's/^\[^38\]: Jan Nattier, "The Heart Sūtra: A Chinese Apocryphal Text\?" \*Journal/[^41]: Jan Nattier, "The Heart Sūtra: A Chinese Apocryphal Text?" *Journal/' "$OUTPUT"

# Change [^37]: -> [^40]: (DiAngelo)
sed -i.bak8 's/^\[^37\]: Robin DiAngelo/[^40]: Robin DiAngelo/' "$OUTPUT"

# Change [^36]: -> [^39]: (Manuel second 47-52)
sed -i.bak9 's/^\[^36\]: Manuel, \*The Way of Tenderness\*, 47-52/[^39]: Manuel, *The Way of Tenderness*, 47-52/' "$OUTPUT"

# Change [^35]: -> [^38]: (Majied Joyfully)
sed -i.bak10 's/^\[^35\]: Kamilah Majied, \*Joyfully/[^38]: Kamilah Majied, *Joyfully/' "$OUTPUT"

# Change [^34]: -> [^37]: (Searle)
sed -i.bak11 's/^\[^34\]: John Searle/[^37]: John Searle/' "$OUTPUT"

# Change [^33]: -> [^36]: (Porges)
sed -i.bak12 's/^\[^33\]: Stephen W\. Porges/[^36]: Stephen W. Porges/' "$OUTPUT"

# Change [^32]: -> [^35]: (Cone)
sed -i.bak13 's/^\[^32\]: James H\. Cone/[^35]: James H. Cone/' "$OUTPUT"

# Change [^31]: -> [^34]: (Yetunde)
sed -i.bak14 's/^\[^31\]: Pamela Ayo Yetunde/[^34]: Pamela Ayo Yetunde/' "$OUTPUT"

# Change [^30]: -> [^33]: (Craig)
sed -i.bak15 's/^\[^30\]: Ralph H\. Craig III/[^33]: Ralph H. Craig III/' "$OUTPUT"

# Change [^29]: -> [^32]: (Thurman)
sed -i.bak16 's/^\[^29\]: Howard Thurman/[^32]: Howard Thurman/' "$OUTPUT"

# Change [^28]: -> [^31]: (Murray)
sed -i.bak17 's/^\[^28\]: Albert Murray/[^31]: Albert Murray/' "$OUTPUT"

# Change [^27]: -> [^30]: (Hartman Wayward short)
sed -i.bak18 's/^\[^27\]: Hartman, \*Wayward Lives/[^30]: Hartman, *Wayward Lives/' "$OUTPUT"

# Change [^26]: -> [^29]: (Baker first)
sed -i.bak19 's/^\[^26\]: Houston A\. Baker, \*Blues, Ideology/[^29]: Houston A. Baker, *Blues, Ideology/' "$OUTPUT"

# Change [^25a]: -> [^28a]: (Nāgārjuna 24.18)
sed -i.bak20 's/^\[^25a\]: Nāgārjuna, \*Mūlamadhyamakakārikā\* 24\.18/[^28a]: Nāgārjuna, *Mūlamadhyamakakārikā* 24.18/' "$OUTPUT"

# Change [^25]: -> [^28]: (Nāgārjuna MMK)
sed -i.bak21 's/^\[^25\]: Nāgārjuna, \*Mūlamadhyamakakārikā\* (The Fundamental/[^28]: Nāgārjuna, *Mūlamadhyamakakārikā* (The Fundamental/' "$OUTPUT"

# Change [^24]: -> [^27]: (Kabat-Zinn)
sed -i.bak22 's/^\[^24\]: Jon Kabat-Zinn/[^27]: Jon Kabat-Zinn/' "$OUTPUT"

# Change [^23]: -> [^26]: (Thich Nhat Hanh)
sed -i.bak23 's/^\[^23\]: Thich Nhat Hanh/[^26]: Thich Nhat Hanh/' "$OUTPUT"

# Change [^22]: -> [^25]: (Manuel first)
sed -i.bak24 's/^\[^22\]: Manuel, \*The Way of Tenderness\*, 47-52/[^25]: Manuel, *The Way of Tenderness*, 47-52/' "$OUTPUT"

# Change [^21]: -> [^24]: (Hartman Wayward first)
sed -i.bak25 's/^\[^21\]: Saidiya Hartman, \*Wayward Lives/[^24]: Saidiya Hartman, *Wayward Lives/' "$OUTPUT"

# Change [^20]: -> [^23]: (Heart Sutra Reborn)
sed -i.bak26 's/^\[^20\]: \*Heart Sutra Reborn/[^23]: *Heart Sutra Reborn/' "$OUTPUT"

# Change [^19]: -> [^22]: (Patterson analysis)
sed -i.bak27 's/^\[^19\]: Patterson.s analysis/[^22]: Patterson'"'"'s analysis/' "$OUTPUT"

# Change [^18]: -> [^21]: (Patterson first)
sed -i.bak28 's/^\[^18\]: Orlando Patterson/[^21]: Orlando Patterson/' "$OUTPUT"

# Change [^17]: -> [^20]: (Ellison)
sed -i.bak29 's/^\[^17\]: Ralph Ellison/[^20]: Ralph Ellison/' "$OUTPUT"

# Change [^16]: -> [^19]: (Xuanzang)
sed -i.bak30 's/^\[^16\]: Xuanzang (玄奘/[^19]: Xuanzang (玄奘/' "$OUTPUT"

# Change [^15]: -> [^18]: (vernacular)
sed -i.bak31 's/^\[^15\]: This line is adapted/[^18]: This line is adapted/' "$OUTPUT"

# Change [^14]: -> [^17]: (Yü)
sed -i.bak32 's/^\[^14\]: See Chün-fang Yü/[^17]: See Chün-fang Yü/' "$OUTPUT"

# Change [^13]: -> [^16]: (Davis)
sed -i.bak33 's/^\[^13\]: Angela Y\. Davis/[^16]: Angela Y. Davis/' "$OUTPUT"

# Change [^12]: -> [^15]: (coined)
sed -i.bak34 's/^\[^12\]: This phrase is coined/[^15]: This phrase is coined/' "$OUTPUT"

# Change [^11]: -> [^14]: (Woods Blues Block)
sed -i.bak35 's/^\[^11\]: Woods, \*Development Arrested\*, 25-29\. The "Blues Block"/[^14]: Woods, *Development Arrested*, 25-29. The "Blues Block"/' "$OUTPUT"

# Change [^10]: -> [^13]: (Woods first - need to be careful)
# This one is tricky - only change the standalone one, not the Blues Block one
sed -i.bak36 '/Blues Block/!s/^\[^10\]: Woods, \*Development Arrested\*, 25-29\./[^13]: Woods, *Development Arrested*, 25-29./' "$OUTPUT"

# Change [^9]: -> [^12]: (Pema)
sed -i.bak37 's/^\[^9\]: The concept of "groundlessness/[^12]: The concept of "groundlessness/' "$OUTPUT"

# Change [^8]: -> [^11]: (Tanahashi)
sed -i.bak38 's/^\[^8\]: Kazuaki Tanahashi/[^11]: Kazuaki Tanahashi/' "$OUTPUT"

# Change [^7]: Zacchetti -> [^10]: (but NOT Willis)
sed -i.bak39 's/^\[^7\]: Stefano Zacchetti/[^10]: Stefano Zacchetti/' "$OUTPUT"

# Change [^6]: Nattier -> [^9]: (but NOT Manuel)
sed -i.bak40 's/^\[^6\]: Jan Nattier, "The Heart/[^9]: Jan Nattier, "The Heart/' "$OUTPUT"

# Change [^5]: Lopez -> [^8]: (but NOT Vesely-Flad)
# Need to match on "Donald" to distinguish
sed -i.bak41 's/^\[^8\]: Donald S\. Lopez/[^8]: Donald S. Lopez/' "$OUTPUT"  # This is already [^8], keep it

echo "Footnote definitions renumbered. Intermediate backup files created (.bak*)"
echo "Now check the output file: $OUTPUT"

