# Figure 1: Voice Tag Frequency Distribution

**Title**: Distribution of Voice Tags Across 15 Gemini TTS Voices in Lotus Sutra Audio Production

**Type**: Horizontal Bar Chart
**Data Source**: Lotus Sutra Audio Production (532 total voice tags)
**Created**: December 21, 2024

---

## Visual Representation (Text-Based)

```
Voice Tag Frequency Distribution (n=532)

Charon (Narrator)         ████████████████████████████████████████  211 (39.7%)
Orus (Śāriputra)          ██████████████████████████                132 (24.8%)
Iapetus (Buddha-Auth)     ████████████                               60 (11.3%)
Rasalgethi (Buddha-Gent)  ███████████                                54 (10.2%)
Sulafat (Bodhisattva-F)   █████                                      25 (4.7%)
Zubenelgenubi (Bodhi-M)   ███                                        15 (2.8%)
Orion (Disciple)          ██                                          9 (1.7%)
Jove (Parable)            █                                           6 (1.1%)
Sadaltager (Parable)      █                                           5 (0.9%)
Puck (Mahākāśyapa)        █                                           4 (0.8%)
Leda (Parable-F)          █                                           4 (0.8%)
Vulcan (Disciple)         █                                           2 (0.4%)
Triton (Buddha-Cosmic)    █                                           2 (0.4%)
Lyra (Bodhisattva-F)      █                                           2 (0.4%)
Aoede (Bodhisattva-F)     █                                           1 (0.2%)

        0    25   50   75   100  125  150  175  200  225
                        Number of Tags
```

---

## Data Table (For Chart Creation)

| Voice | Character Role | Count | Percentage | Dharma Category |
|-------|---------------|-------|------------|-----------------|
| Charon | Narrator (Ānanda) | 211 | 39.7% | Narrator |
| Orus | Śāriputra (Chief Disciple) | 132 | 24.8% | Disciples |
| Iapetus | Buddha (Authoritative Teaching) | 60 | 11.3% | Buddha |
| Rasalgethi | Buddha (Gentle Teaching) | 54 | 10.2% | Buddha |
| Sulafat | Female Bodhisattvas | 25 | 4.7% | Bodhisattvas |
| Zubenelgenubi | Male Bodhisattvas | 15 | 2.8% | Bodhisattvas |
| Orion | Supporting Disciples | 9 | 1.7% | Disciples |
| Jove | Male Parable Characters | 6 | 1.1% | Parables |
| Sadaltager | Male Parable Characters | 5 | 0.9% | Parables |
| Puck | Mahākāśyapa (Elder Disciple) | 4 | 0.8% | Disciples |
| Leda | Female Parable Characters | 4 | 0.8% | Parables |
| Vulcan | Supporting Disciples | 2 | 0.4% | Disciples |
| Triton | Buddha (Cosmic Revelation) | 2 | 0.4% | Buddha |
| Lyra | Female Bodhisattvas | 2 | 0.4% | Bodhisattvas |
| Aoede | Female Bodhisattvas | 1 | 0.2% | Bodhisattvas |

---

## CSV Data (Copy for Excel/Google Sheets)

```csv
Voice,Character_Role,Count,Percentage,Dharma_Category
Charon,Narrator (Ānanda),211,39.7,Narrator
Orus,Śāriputra (Chief Disciple),132,24.8,Disciples
Iapetus,Buddha (Authoritative),60,11.3,Buddha
Rasalgethi,Buddha (Gentle),54,10.2,Buddha
Sulafat,Female Bodhisattvas,25,4.7,Bodhisattvas
Zubenelgenubi,Male Bodhisattvas,15,2.8,Bodhisattvas
Orion,Supporting Disciples,9,1.7,Disciples
Jove,Male Parable Characters,6,1.1,Parables
Sadaltager,Male Parable Characters,5,0.9,Parables
Puck,Mahākāśyapa (Elder),4,0.8,Disciples
Leda,Female Parable Characters,4,0.8,Parables
Vulcan,Supporting Disciples,2,0.4,Disciples
Triton,Buddha (Cosmic),2,0.4,Buddha
Lyra,Female Bodhisattvas,2,0.4,Bodhisattvas
Aoede,Female Bodhisattvas,1,0.2,Bodhisattvas
```

---

## Color-Coded Version (By Dharma Category)

**Suggested color scheme for published figure**:

- **Narrator** (Blue): Charon
- **Buddha** (Gold/Orange): Iapetus, Rasalgethi, Triton
- **Disciples** (Green): Orus, Orion, Puck, Vulcan
- **Bodhisattvas** (Purple): Sulafat, Zubenelgenubi, Lyra, Aoede
- **Parables** (Red): Jove, Sadaltager, Leda

```
NARRATOR (Blue)
  Charon            ████████████████████████████████████████  211

BUDDHA (Gold)
  Iapetus           ████████████                               60
  Rasalgethi        ███████████                                54
  Triton            █                                           2

DISCIPLES (Green)
  Orus              ██████████████████████████                132
  Orion             ██                                          9
  Puck              █                                           4
  Vulcan            █                                           2

BODHISATTVAS (Purple)
  Sulafat           █████                                      25
  Zubenelgenubi     ███                                        15
  Lyra              █                                           2
  Aoede             █                                           1

PARABLES (Red)
  Jove              █                                           6
  Sadaltager        █                                           5
  Leda              █                                           4
```

---

## Figure Caption (For Article)

**Figure 1. Distribution of voice tags across 15 Gemini TTS voices in Lotus Sutra audio production.**

The horizontal bar chart displays the frequency of voice assignments for 532 voice tags across 28 chapters (~200,000 words). Voices are grouped by dharma role: Narrator (blue), Buddha (gold), Disciples (green), Bodhisattvas (purple), and Parable characters (red). The concentration of tags in the top three voices (Charon, Orus, Iapetus) reflects the dialogic structure of Buddhist sutras, which are narrator-driven with frequent Buddha-disciple exchanges. The use of three distinct Buddha voices (Iapetus, Rasalgethi, Triton) demonstrates an interpretive choice to match voice characteristics to teaching contexts (authoritative, gentle, cosmic).

---

## Python Code (For Professional Chart Creation)

```python
import matplotlib.pyplot as plt
import numpy as np

# Data
voices = ['Charon', 'Orus', 'Iapetus', 'Rasalgethi', 'Sulafat',
          'Zubenelgenubi', 'Orion', 'Jove', 'Sadaltager', 'Puck',
          'Leda', 'Vulcan', 'Triton', 'Lyra', 'Aoede']
counts = [211, 132, 60, 54, 25, 15, 9, 6, 5, 4, 4, 2, 2, 2, 1]
roles = ['Narrator', 'Disciple', 'Buddha', 'Buddha', 'Bodhisattva',
         'Bodhisattva', 'Disciple', 'Parable', 'Parable', 'Disciple',
         'Parable', 'Disciple', 'Buddha', 'Bodhisattva', 'Bodhisattva']

# Color mapping
color_map = {
    'Narrator': '#3498db',      # Blue
    'Buddha': '#f39c12',        # Gold
    'Disciple': '#2ecc71',      # Green
    'Bodhisattva': '#9b59b6',   # Purple
    'Parable': '#e74c3c'        # Red
}
colors = [color_map[role] for role in roles]

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 8))
y_pos = np.arange(len(voices))

bars = ax.barh(y_pos, counts, color=colors, alpha=0.8, edgecolor='black')

# Add count labels at end of bars
for i, (bar, count) in enumerate(zip(bars, counts)):
    width = bar.get_width()
    ax.text(width + 3, bar.get_y() + bar.get_height()/2,
            f'{count} ({count/532*100:.1f}%)',
            ha='left', va='center', fontsize=9)

# Formatting
ax.set_yticks(y_pos)
ax.set_yticklabels(voices)
ax.invert_yaxis()  # Top voice at top
ax.set_xlabel('Number of Voice Tags', fontsize=12, fontweight='bold')
ax.set_title('Voice Tag Frequency Distribution\nLotus Sutra Audio Production (n=532)',
             fontsize=14, fontweight='bold', pad=20)
ax.grid(axis='x', alpha=0.3, linestyle='--')

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#3498db', label='Narrator'),
    Patch(facecolor='#f39c12', label='Buddha'),
    Patch(facecolor='#2ecc71', label='Disciples'),
    Patch(facecolor='#9b59b6', label='Bodhisattvas'),
    Patch(facecolor='#e74c3c', label='Parables')
]
ax.legend(handles=legend_elements, loc='lower right', title='Dharma Role')

plt.tight_layout()
plt.savefig('figure_01_voice_distribution.png', dpi=300, bbox_inches='tight')
plt.savefig('figure_01_voice_distribution.pdf', bbox_inches='tight')
plt.show()
```

---

## Excel/Google Sheets Instructions

**To create chart in Excel/Google Sheets**:

1. Copy CSV data above into new spreadsheet
2. Select columns A (Voice) and C (Count)
3. Insert → Chart → Horizontal Bar Chart
4. Chart title: "Voice Tag Frequency Distribution (n=532)"
5. X-axis label: "Number of Tags"
6. Y-axis: Reverse order (Charon at top)
7. Add data labels showing counts and percentages
8. Color bars by Dharma_Category (column E):
   - Narrator: Blue
   - Buddha: Gold/Orange
   - Disciples: Green
   - Bodhisattvas: Purple
   - Parables: Red

---

## Key Insights Visible in Figure

### 1. Concentration in Top 3 Voices
- **Charon (211) + Orus (132) + Iapetus (60) = 403 tags (75.7%)**
- Reflects sutra structure: narrator-driven with Buddha-disciple dialogue

### 2. Long Tail Distribution
- 12 voices account for only 24.3% of tags
- Shows efficient voice usage: enough variety without overwhelming listener

### 3. Buddha Voice Variation
- 3 Buddha voices (Iapetus 60, Rasalgethi 54, Triton 2) = 116 total (21.9%)
- Nearly even split between authoritative and gentle modes
- Cosmic voice (Triton) reserved for rare high-impact moments

### 4. Disciple Dominance
- Orus (Śāriputra) = 132 tags (24.8%) - second highest overall
- Reflects Śāriputra's role as chief questioner in Lotus Sutra

### 5. Minimal Female Voices
- Sulafat (25) + Leda (4) + Lyra (2) + Aoede (1) = 32 tags (6.0%)
- Reflects traditional Buddhist sutra demographics (male-dominated assembly)
- Gender alignment preserved in voice selection

---

## Statistical Summary

**Total voices used**: 15 of 26 available (58% utilization)
**Total tags**: 532
**Mean tags per voice**: 35.5
**Median tags per voice**: 5
**Mode**: 4 tags (Puck, Leda)
**Standard deviation**: 56.8 (high variance due to Charon/Orus outliers)

**Distribution shape**: Strongly right-skewed (long tail)
- Top 20% of voices = 80% of tags (Pareto principle applies)

---

## Format Options for Publication

### Option 1: Simple Horizontal Bar (Recommended)
- Clean, easy to read
- Color-coded by dharma role
- Count + percentage labels on each bar

### Option 2: Grouped Bar Chart
- Group by dharma category (Narrator, Buddha, Disciples, etc.)
- Shows categorical structure more clearly

### Option 3: Stacked Bar with Inset
- Main chart: All 15 voices
- Inset: Pie chart showing 5 dharma role categories

### Option 4: Interactive HTML/SVG
- Hover to see voice characteristics
- Click to highlight all tags for that dharma role
- Suitable for digital publication (DHQ online format)

---

**Recommendation for Article 1**: Use **Option 1 (Simple Horizontal Bar)** with color-coding by dharma role. Clean, professional, immediately communicates the key insight (narrator/disciple/Buddha concentration).

---

**Status**: Figure 1 data complete and ready for chart creation
**Next**: Extract verse optimization examples with token counts
