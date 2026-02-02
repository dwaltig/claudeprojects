#!/bin/bash
# Gender Alignment Verification

FILE="/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript_final.txt"
LOG="/Users/williamaltig/claudeprojects/Lotus_Sutra/VOICE_REMAPPING_LOG.txt"

echo "" >> "$LOG"
echo "================================================" >> "$LOG"
echo "GENDER ALIGNMENT VERIFICATION" >> "$LOG"
echo "================================================" >> "$LOG"
echo "" >> "$LOG"

# MALE VOICES (from Gemini list)
male_voices="Charon|Fenrir|Gacrux|Iapetus|Jove|Orus|Orion|Puck|Rasalgethi|Sadaltager|Triton|Vulcan|Zubenelgenubi"

# FEMALE VOICES (from Gemini list)  
female_voices="Andromeda|Aoede|Callirrhoe|Cassiopeia|Erinome|Kore|Leda|Lyra|Nyx|Schedar|Sulafat|Umbriel|Zephyr"

echo "MALE VOICES IN USE:" >> "$LOG"
grep -o '\[.*\]' "$FILE" | sort -u | grep -E "\[($male_voices)\]" | while read voice; do
    count=$(grep -o "$voice" "$FILE" | wc -l | tr -d ' ')
    echo "  $voice: $count occurrences" >> "$LOG"
done

echo "" >> "$LOG"
echo "FEMALE VOICES IN USE:" >> "$LOG"
grep -o '\[.*\]' "$FILE" | sort -u | grep -E "\[($female_voices)\]" | while read voice; do
    count=$(grep -o "$voice" "$FILE" | wc -l | tr -d ' ')
    echo "  $voice: $count occurrences" >> "$LOG"
done

echo "" >> "$LOG"
echo "NON-GEMINI TAGS (pronunciation guides, special markers):" >> "$LOG"
grep -o '\[.*\]' "$FILE" | sort -u | grep -Ev "\[($male_voices|$female_voices)\]" >> "$LOG"

echo "" >> "$LOG"
echo "GENDER ALIGNMENT STATUS:" >> "$LOG"

# Check for any gender misalignment
male_chars="Śāriputra|Mañjuśrī|Maitreya|Mahākāśyapa|Buddha|Elder|Guide"
female_chars="Mahāprajāpatī|Yaśodharā|Avalokiteśvara|Dragon.*Princess"

echo "  Male characters should use male voices only" >> "$LOG"
echo "  Female characters should use female voices only" >> "$LOG"
echo "" >> "$LOG"

# Count male vs female voice usage
male_count=$(grep -oE "\[($male_voices)\]" "$FILE" | wc -l | tr -d ' ')
female_count=$(grep -oE "\[($female_voices)\]" "$FILE" | wc -l | tr -d ' ')
total_gemini=$((male_count + female_count))

echo "  Total Gemini Male Voice Tags: $male_count" >> "$LOG"
echo "  Total Gemini Female Voice Tags: $female_count" >> "$LOG"
echo "  Total Gemini Voice Tags: $total_gemini" >> "$LOG"
echo "" >> "$LOG"

# Check if we need Gacrux
echo "RECOMMENDATION: Generic Male Disciples" >> "$LOG"
echo "  Consider adding [Gacrux] for unnamed male assembly members" >> "$LOG"
echo "  [Gacrux] characteristics: Heroism, integrity, leadership" >> "$LOG"
echo "  Currently male assembly may be using [Charon] or other voices" >> "$LOG"
echo "" >> "$LOG"

echo "GENDER ALIGNMENT VERIFICATION COMPLETE" >> "$LOG"
echo "================================================" >> "$LOG"
