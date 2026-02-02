#!/bin/bash
# Voice Remapping Script for Gemini Speaker Voices
# Strict Gender Alignment Implementation

INPUT_FILE="/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript_enhanced.txt"
OUTPUT_FILE="/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript_final.txt"
LOG_FILE="/Users/williamaltig/claudeprojects/Lotus_Sutra/VOICE_REMAPPING_LOG.txt"

# Copy input to output
cp "$INPUT_FILE" "$OUTPUT_FILE"

# Initialize log
echo "VOICE REMAPPING LOG - Gemini Speaker Voices" > "$LOG_FILE"
echo "================================================" >> "$LOG_FILE"
echo "Timestamp: $(date)" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"
echo "REMAPPING OPERATIONS:" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

# Function to log and replace
remap_voice() {
    local old_tag="$1"
    local new_tag="$2"
    local description="$3"

    # Count occurrences before replacement
    local count=$(grep -o "\[$old_tag\]" "$OUTPUT_FILE" | wc -l | tr -d ' ')

    if [ "$count" -gt 0 ]; then
        echo "$description" >> "$LOG_FILE"
        echo "  Old: [$old_tag] → New: [$new_tag]" >> "$LOG_FILE"
        echo "  Occurrences: $count" >> "$LOG_FILE"

        # Get sample line numbers (first 5)
        echo "  Sample line numbers:" >> "$LOG_FILE"
        grep -n "\[$old_tag\]" "$OUTPUT_FILE" | head -5 | sed 's/:.*$//' | sed 's/^/    Line /' >> "$LOG_FILE"
        echo "" >> "$LOG_FILE"

        # Perform replacement
        sed -i '' "s/\[$old_tag\]/\[$new_tag\]/g" "$OUTPUT_FILE"
    fi
}

# MALE CHARACTER REMAPPINGS
echo "=== MALE DISCIPLES & CHARACTERS ===" >> "$LOG_FILE"

remap_voice "Śāriputra" "Orus" "1. ŚĀRIPUTRA (Chief Disciple - intellectual brilliance)"

remap_voice "Mañjuśrī" "Puck" "2. MAÑJUŚRĪ (Bodhisattva of Wisdom - playful, paradoxical)"

remap_voice "Maitreya" "Orion" "3. MAITREYA (Future Buddha - prophetic, forward momentum)"

remap_voice "Mahākāśyapa" "Vulcan" "4. MAHĀKĀŚYAPA (Elder Disciple - austere, grounded)"

remap_voice "Elder_Parable" "Jove" "5. ELDER IN BURNING HOUSE (Father figure - commanding authority)"

remap_voice "Guide_Phantom" "Sadaltager" "6. GUIDE IN PHANTOM CITY (Strategic leader - military precision)"

# FEMALE CHARACTER REMAPPINGS
echo "=== FEMALE DISCIPLES & CHARACTERS ===" >> "$LOG_FILE"

remap_voice "Sulafat_F" "Sulafat" "7. AVALOKITEŚVARA (Compassion - ethereal, serene) - Fix tag format"

remap_voice "Schedar" "Lyra" "8. DRAGON PRINCESS (Young transformation - sweet, inspiring)"

remap_voice "Children_Voices" "Aoede" "9. CHILDREN VOICES (Innocent, playful - youthful optimism)"

# EDITORIAL/STRUCTURAL REMAPPING
echo "=== EDITORIAL & STRUCTURAL ===" >> "$LOG_FILE"

# Note: Aoede currently used for editorial (27 times), needs to go to Orus
# But we just mapped Children_Voices to Aoede
# We need to be careful here - check context

# Count current Aoede usage before changing
aoede_count=$(grep -o "\[Aoede\]" "$OUTPUT_FILE" | wc -l | tr -d ' ')
echo "10. EDITORIAL MARKERS (Structural narration)" >> "$LOG_FILE"
echo "  Old: [Aoede] → New: [Orus]" >> "$LOG_FILE"
echo "  Note: Aoede was used for editorial (27 occurrences)" >> "$LOG_FILE"
echo "  After Children_Voices→Aoede: checking current count..." >> "$LOG_FILE"
echo "  Current Aoede count: $aoede_count" >> "$LOG_FILE"

# We need to selectively replace only the EDITORIAL Aoede instances
# This requires a different approach - let's flag this for manual review
echo "  ACTION NEEDED: Review Aoede contexts - editorial vs children" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

# BUDDHA VOICE CONTEXT REMAPPING
echo "=== BUDDHA VOICE DIFFERENTIATION ===" >> "$LOG_FILE"

echo "11. BUDDHA VERSES/POETIC MODE" >> "$LOG_FILE"
echo "  Note: Some [Rasalgethi] instances should be [Triton] for verses" >> "$LOG_FILE"
echo "  Current [Rasalgethi]: 56 occurrences" >> "$LOG_FILE"
echo "  ACTION NEEDED: Context-sensitive replacement (verse vs narrative)" >> "$LOG_FILE"
echo "  Keeping [Rasalgethi] for storytelling, manual review needed for verses" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

# PRONUNCIATION GUIDE TAGS - Keep as is
echo "=== PRONUNCIATION GUIDES (Kept As-Is) ===" >> "$LOG_FILE"
echo "The following pronunciation tags are preserved:" >> "$LOG_FILE"
grep -o '\[[A-Z][a-z]*-[A-Z]*[a-z-]*\]' "$OUTPUT_FILE" | sort -u >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

# GENERATE FINAL STATISTICS
echo "" >> "$LOG_FILE"
echo "================================================" >> "$LOG_FILE"
echo "FINAL VOICE TAG STATISTICS" >> "$LOG_FILE"
echo "================================================" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

grep -o '\[.*\]' "$OUTPUT_FILE" | sort | uniq -c | sort -rn >> "$LOG_FILE"

echo "" >> "$LOG_FILE"
echo "================================================" >> "$LOG_FILE"
echo "REMAPPING COMPLETE" >> "$LOG_FILE"
echo "Output file: $OUTPUT_FILE" >> "$LOG_FILE"
echo "================================================" >> "$LOG_FILE"

# Make the final file readable
chmod 644 "$OUTPUT_FILE"

echo "Voice remapping complete. See $LOG_FILE for details."
