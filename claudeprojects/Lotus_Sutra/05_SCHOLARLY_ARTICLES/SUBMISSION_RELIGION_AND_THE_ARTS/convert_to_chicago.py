import re

# File paths
input_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/05_SCHOLARLY_ARTICLES/SUBMISSION_RELIGION_AND_THE_ARTS/ARTICLE_Dharma_Sings_Blues_RELIGION_ARTS.md"
output_file = "/Users/williamaltig/claudeprojects/Lotus_Sutra/05_SCHOLARLY_ARTICLES/SUBMISSION_RELIGION_AND_THE_ARTS/ARTICLE_Dharma_Sings_Blues_RELIGION_ARTS_CHICAGO.md"

# Mapping Author-Date keys to Chicago Footnote strings
# Using a simplified approach: First citation full, subsequent could be short, but for now we might just use full or short consistently.
# Actually, standard Chicago notes: First full, then Short.
# I will use a tracker to decide.

citations_map = {
    "Altig 2025": {
        "full": 'William Altig, "The Lotus Sutra: A Blues Interpretation" (Unpublished manuscript, 2025).',
        "short": 'Altig, "Blues Lotus Sutra."'
    },
    "Baraka 1963": {
        "full": 'Amiri Baraka (LeRoi Jones), *Blues People: Negro Music in White America* (New York: William Morrow, 1963).',
        "short": 'Baraka, *Blues People*.'
    },
    "Clark 2015": {
        "full": 'Kiley Jon Clark, "Street Dharma: Buddhism in Urban America," *Lion\'s Roar*, accessed December 12, 2025, https://www.lionsroar.com/journeys-the-real-rodeo/.',
        "short": 'Clark, "Street Dharma."'
    },
    "Cone 1970": {
        "full": 'James H. Cone, *A Black Theology of Liberation* (Philadelphia: Lippincott, 1970).',
        "short": 'Cone, *Black Theology*.'
    },
    "Ellison 1964": {
        "full": 'Ralph Ellison, *Shadow and Act* (New York: Random House, 1964).',
        "short": 'Ellison, *Shadow and Act*.'
    },
    "Hua 2018": {
        "full": 'Manyuan Hua, "Reinterpreting The Wén-Zhì Debate in the Education of Translation History," *International Journal of Languages, Literature and Linguistics* 4, no. 4 (2018): 277–283.',
        "short": 'Hua, "Wén-Zhì Debate," 277.'
    },
    "Hureau 2010": {
        "full": 'Sylvie Hureau, "Translations, Apocrypha, and the Emergence of the Buddhist Canon," in *Early Chinese Religion, Part Two*, ed. John Lagerwey and Lü Pengzhi (Leiden: Brill, 2010), 741–774.',
        "short": 'Hureau, "Translations," 745.'
    },
    "Johnson 2003": {
        "full": 'Charles Johnson, *Turning the Wheel: Essays on Buddhism and Writing* (New York: Scribner, 2003).',
        "short": 'Johnson, *Turning the Wheel*.'
    },
    "Kinkead 2015": {
        "full": 'April Leigh Kinkead, "Black Rhetoric: The Art of Thinking Being" (PhD diss., University of Texas at Arlington, 2015).',
        "short": 'Kinkead, "Black Rhetoric."'
    },
    "Murray 1976": {
        "full": 'Albert Murray, *Stomping the Blues* (New York: McGraw-Hill, 1976).',
        "short": 'Murray, *Stomping the Blues*.'
    },
    "Nida 1964": {
        "full": 'Eugene A. Nida, *Toward a Science of Translating* (Leiden: Brill, 1964).',
        "short": 'Nida, *Toward a Science*.'
    },
    "Nida and Taber 1969": {
        "full": 'Eugene A. Nida and Charles R. Taber, *The Theory and Practice of Translation* (Leiden: Brill, 1969).',
        "short": 'Nida and Taber, *Theory and Practice*.'
    },
    "Norman 1983": {
        "full": 'K. R. Norman, *Pāli Literature* (Wiesbaden: Otto Harrassowitz, 1983).',
        "short": 'Norman, *Pāli Literature*.'
    },
    "Oliver 1990": {
        "full": 'Paul Oliver, *Blues Fell This Morning: Meaning in the Blues*, 2nd ed. (Cambridge: Cambridge University Press, 1990).',
        "short": 'Oliver, *Blues Fell This Morning*.'
    },
    "Sea Island Translation Team 2005": {
        "full": 'Sea Island Translation Team, *De Nyew Testament* (New York: American Bible Society, 2005).',
        "short": 'Sea Island Translation Team, *De Nyew Testament*.'
    },
    "Steinfeld 2016": {
        "full": 'Susanna Steinfeld, "The Social Significance of Blues Music" (Master\'s thesis, LUISS Guido Carli University, 2016).',
        "short": 'Steinfeld, "Social Significance."'
    },
    "Venuti 1995": {
        "full": 'Lawrence Venuti, *The Translator\'s Invisibility: A History of Translation* (London: Routledge, 1995).',
        "short": 'Venuti, *Translator\'s Invisibility*.'
    },
    "hooks 2000": {
        "full": 'bell hooks, *All About Love: New Visions* (New York: William Morrow, 2000).',
        "short": 'hooks, *All About Love*.'
    },
    "Maultsby 1990": {
        "full": 'Portia K. Maultsby, "Africanisms in African-American Music," in *Africanisms in American Culture*, ed. Joseph E. Holloway (Bloomington: Indiana University Press, 1990), 185–210.',
        "short": 'Maultsby, "Africanisms," 192.'
    },
    "Zürcher 2007": {
        "full": 'Erik Zürcher, *The Buddhist Conquest of China: The Spread and Adaptation of Buddhism in Early Medieval China*, 3rd ed. (Leiden: Brill, 2007).',
        "short": 'Zürcher, *Buddhist Conquest*.'
    },
    "Willis 2001": {
        "full": 'Jan Willis, *Dreaming Me: Black, Baptist, and Buddhist* (New York: Riverhead Books, 2001).',
        "short": 'Willis, *Dreaming Me*.'
    }
}

cited_status = {key: False for key in citations_map}
footnotes = []
footnote_counter = 1

def replace_citation(match):
    global footnote_counter
    content = match.group(1) # e.g. "Norman 1983" or "Nida 1964; Venuti 1995"
    
    # Split by semicolon to handle multiple citations
    raw_citations = [c.strip() for c in content.split(';')]
    processed_citations = []
    
    for raw_cit in raw_citations:
        # Check for page numbers
        parts = raw_cit.split(',')
        key_part = parts[0].strip()
        page_part = ""
        if len(parts) > 1:
            page_part = ", " + ",".join(parts[1:]).strip() 
        
        citation_text = ""
        
        # Find matching key
        if key_part in citations_map:
            if not cited_status[key_part]:
                citation_text = citations_map[key_part]["full"]
                cited_status[key_part] = True
            else:
                citation_text = citations_map[key_part]["short"]
            
            # Append page number if exists
            if page_part:
                 # remove period if exists at end of citation_text before adding page
                 if citation_text.endswith('.'):
                     citation_text = citation_text[:-1]
                 citation_text += page_part + "."
        else:
            # Fallback if key not found 
            citation_text = f"Unmapped citation: {key_part}"
        
        # Strip terminal punctuation before joining
        if citation_text.endswith('.'):
            citation_text = citation_text[:-1]
        elif citation_text.endswith('."'):
            citation_text = citation_text[:-2] + '"'
        elif citation_text.endswith(".'"):
            citation_text = citation_text[:-2] + "'"
        
        processed_citations.append(citation_text)

    # Join multiple citations with a semicolon and space, add final period
    final_footnote_text = "; ".join(processed_citations) + "."
    
    footnotes.append(f"[^{footnote_counter}]: {final_footnote_text}")
    marker = f"[^{footnote_counter}]"
    footnote_counter += 1
    return marker

with open(input_file, 'r') as f:
    text = f.read()

# Pattern: (Author Year) or (Author Year, p. xx)
# Regex: \(([^)]+ \d{4}.*?)\)
pattern = r'\(([^)]+ \d{4}.*?)\)'

new_text = re.sub(pattern, replace_citation, text)

# Append footnotes
new_text += "\n\n" + "\n".join(footnotes)

with open(output_file, 'w') as f:
    f.write(new_text)

print(f"Converted {len(footnotes)} citations.")
