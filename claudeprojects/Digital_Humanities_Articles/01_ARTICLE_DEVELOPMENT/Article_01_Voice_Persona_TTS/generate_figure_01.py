import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

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
legend_elements = [
    Patch(facecolor='#3498db', label='Narrator'),
    Patch(facecolor='#f39c12', label='Buddha'),
    Patch(facecolor='#2ecc71', label='Disciples'),
    Patch(facecolor='#9b59b6', label='Bodhisattvas'),
    Patch(facecolor='#e74c3c', label='Parables')
]
ax.legend(handles=legend_elements, loc='lower right', title='Dharma Role')

plt.tight_layout()
plt.savefig('Figure_01_Voice_Distribution.png', dpi=300, bbox_inches='tight')
print("✓ Figure 1 saved: Figure_01_Voice_Distribution.png")
plt.close()
