#!/bin/bash
# Phase 2: Context-Sensitive Voice Remapping
# Handle Aoede editorial→Orus and identify Rasalgethi→Triton for verses

FILE="/Users/williamaltig/claudeprojects/Lotus_Sutra/narrated_manuscript_final.txt"
LOG="/Users/williamaltig/claudeprojects/Lotus_Sutra/VOICE_REMAPPING_LOG.txt"

echo "" >> "$LOG"
echo "================================================" >> "$LOG"
echo "PHASE 2: CONTEXT-SENSITIVE REMAPPING" >> "$LOG"
echo "================================================" >> "$LOG"
echo "" >> "$LOG"

# Strategy: Replace all Aoede with temp marker, then replace back context-sensitively
# Line 2300 is children speaking - keep as Aoede
# All others are editorial - change to Orus

# Get all Aoede line numbers
aoede_lines=$(grep -n "\[Aoede\]" "$FILE" | cut -d: -f1)

echo "AOEDE REMAPPING (Editorial vs Children):" >> "$LOG"
echo "" >> "$LOG"

editorial_count=0
children_count=0

# Process each Aoede occurrence
for line_num in $aoede_lines; do
    # Get context
    context=$(sed -n "$((line_num-1)),$((line_num+1))p" "$FILE")

    # Check if this is the children speaking (around line 2300)
    if [ $line_num -eq 2300 ]; then
        echo "  Line $line_num: CHILDREN speaking - KEEP as [Aoede]" >> "$LOG"
        children_count=$((children_count + 1))
    else
        # This is editorial - change to Orus
        echo "  Line $line_num: EDITORIAL marker - CHANGE to [Orus]" >> "$LOG"
        sed -i '' "${line_num}s/\[Aoede\]/\[Orus\]/" "$FILE"
        editorial_count=$((editorial_count + 1))
    fi
done

echo "" >> "$LOG"
echo "  Editorial (→Orus): $editorial_count" >> "$LOG"
echo "  Children (keep Aoede): $children_count" >> "$LOG"
echo "" >> "$LOG"

# Now handle Orus duplicates
# Current Orus count includes: Śāriputra (7) + editorial (27) = 124 before this fix
# After this fix: Śāriputra (7) + editorial-fixed (~27) = we need to verify

echo "ŚĀRIPUTRA vs EDITORIAL ORUS USAGE:" >> "$LOG"
echo "  Note: [Orus] now represents both Śāriputra character voice" >> "$LOG"
echo "        and editorial/structural markers (both male voice)" >> "$LOG"
echo "  This is acceptable as they serve different narrative functions" >> "$LOG"
echo "" >> "$LOG"

# Check for [Leda] - female assembly voices
leda_count=$(grep -o "\[Leda\]" "$FILE" | wc -l | tr -d ' ')
echo "FEMALE ASSEMBLY VOICES:" >> "$LOG"
echo "  [Leda] occurrences: $leda_count" >> "$LOG"
echo "  Recommendation: Keep [Leda] for general female assembly" >> "$LOG"
echo "  Alternative: Could map to [Kore] for warmer, more welcoming tone" >> "$LOG"
echo "" >> "$LOG"

# Identify verse contexts for Rasalgethi→Triton
echo "BUDDHA VOICE CONTEXTS (Rasalgethi analysis):" >> "$LOG"
echo "  Checking for verse markers near [Rasalgethi]..." >> "$LOG"
echo "" >> "$LOG"

rasalgethi_lines=$(grep -n "\[Rasalgethi\]" "$FILE" | head -20 | cut -d: -f1)
verse_contexts=0
narrative_contexts=0

for line_num in $rasalgethi_lines; do
    # Check 5 lines before for "spoke in verse" or "chanted" or verse markers
    context=$(sed -n "$((line_num-5)),$((line_num+2))p" "$FILE")

    if echo "$context" | grep -qi "verse\|chant\|sing"; then
        echo "  Line $line_num: VERSE context detected" >> "$LOG"
        verse_contexts=$((verse_contexts + 1))
        # Change to Triton for verse delivery
        sed -i '' "${line_num}s/\[Rasalgethi\]/\[Triton\]/" "$FILE"
    else
        echo "  Line $line_num: NARRATIVE context (keep Rasalgethi)" >> "$LOG"
        narrative_contexts=$((narrative_contexts + 1))
    fi
done

echo "" >> "$LOG"
echo "  Verse contexts (→Triton): $verse_contexts" >> "$LOG"
echo "  Narrative contexts (keep Rasalgethi): $narrative_contexts" >> "$LOG"
echo "  (Showing first 20 instances only)" >> "$LOG"
echo "" >> "$LOG"

echo "================================================" >> "$LOG"
echo "UPDATED VOICE TAG STATISTICS (After Phase 2)" >> "$LOG"
echo "================================================" >> "$LOG"
echo "" >> "$LOG"

grep -o '\[.*\]' "$FILE" | sort | uniq -c | sort -rn >> "$LOG"

echo "" >> "$LOG"
echo "PHASE 2 COMPLETE" >> "$LOG"
echo "================================================" >> "$LOG"
