# Fix duplicates in footnote definitions (in order from high to low)
# Match specific text to target only the second instance

/^\[^44\]: On the two obscurations/ s/^\[^44\]:/[^47]:/
/^\[^43\]: Vincent L\. Wimbush/ s/^\[^43\]:/[^46]:/
/^\[^42\]: Fred Moten/ s/^\[^42\]:/[^45]:/
/^\[^41\]: Christina Sharpe/ s/^\[^41\]:/[^44]:/
/^\[^40\]: Saidiya Hartman.*Beautiful Experiments/ s/^\[^40\]:/[^43]:/
/^\[^39\]: Houston A\. Baker.*Chicago/ s/^\[^39\]:/[^42]:/
/^\[^38\]: Jan Nattier.*Journal/ s/^\[^38\]:/[^41]:/
/^\[^37\]: Robin DiAngelo/ s/^\[^37\]:/[^40]:/
/^\[^36\]: Manuel.*Way of Tenderness.*47-52/ s/^\[^36\]:/[^39]:/
/^\[^35\]: Kamilah Majied.*Joyfully/ s/^\[^35\]:/[^38]:/
/^\[^34\]: John Searle/ s/^\[^34\]:/[^37]:/
/^\[^33\]: Stephen W\. Porges/ s/^\[^33\]:/[^36]:/
/^\[^32\]: James H\. Cone/ s/^\[^32\]:/[^35]:/
/^\[^31\]: Pamela Ayo Yetunde/ s/^\[^31\]:/[^34]:/
/^\[^30\]: Ralph H\. Craig III/ s/^\[^30\]:/[^33]:/
/^\[^29\]: Howard Thurman/ s/^\[^29\]:/[^32]:/
/^\[^28\]: Albert Murray/ s/^\[^28\]:/[^31]:/
/^\[^27\]: Hartman.*Wayward Lives\*$/ s/^\[^27\]:/[^30]:/
/^\[^26\]: Houston A\. Baker.*Blues, Ideology/ s/^\[^26\]:/[^29]:/
/^\[^25a\]: Nāgārjuna.*24\.18/ s/^\[^25a\]:/[^28a]:/
/^\[^25\]: Nāgārjuna.*Fundamental/ s/^\[^25\]:/[^28]:/
/^\[^24\]: Jon Kabat-Zinn/ s/^\[^24\]:/[^27]:/
/^\[^23\]: Thich Nhat Hanh/ s/^\[^23\]:/[^26]:/
/^\[^22\]: Manuel.*Way of Tenderness.*47-52/ s/^\[^22\]:/[^25]:/
/^\[^21\]: Saidiya Hartman.*Wayward Lives/ s/^\[^21\]:/[^24]:/
/^\[^20\]: \*Heart Sutra Reborn/ s/^\[^20\]:/[^23]:/
/^\[^19\]: Patterson.*analysis/ s/^\[^19\]:/[^22]:/
/^\[^18\]: Orlando Patterson/ s/^\[^18\]:/[^21]:/
/^\[^17\]: Ralph Ellison/ s/^\[^17\]:/[^20]:/
/^\[^16\]: Xuanzang.*玄奘/ s/^\[^16\]:/[^19]:/
/^\[^15\]: This line is adapted/ s/^\[^15\]:/[^18]:/
/^\[^14\]: See Chün-fang Yü/ s/^\[^14\]:/[^17]:/
/^\[^13\]: Angela Y\. Davis/ s/^\[^13\]:/[^16]:/
/^\[^12\]: This phrase is coined/ s/^\[^12\]:/[^15]:/

