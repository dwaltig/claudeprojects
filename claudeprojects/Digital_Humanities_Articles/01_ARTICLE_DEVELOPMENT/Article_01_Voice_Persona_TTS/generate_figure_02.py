import matplotlib.pyplot as plt
import numpy as np

# Data
passages = ['Ch. 2\nŚāriputra', 'Ch. 2\nThree Vehicles', 'Ch. 2\nCompassion', 'Ch. 3\nBurning House', 'Ch. 16\nEternal']
before = [95, 115, 121, 86, 60]
after = [75, 91, 97, 68, 48]
reduction = [20, 24, 24, 18, 12]

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Bar positions
x = np.arange(len(passages))
width = 0.35

# Create grouped bars
bars1 = ax.bar(x - width/2, before, width, label='Before Optimization', color='#8B4513', alpha=0.8)
bars2 = ax.bar(x + width/2, after, width, label='After Optimization', color='#228B22', alpha=0.8)

# Add reduction labels above bars
for i, (b, a, r) in enumerate(zip(before, after, reduction)):
    # Show reduction amount above the taller bar
    ax.text(i, max(b, a) + 3, f'-{r}', ha='center', va='bottom', fontweight='bold', fontsize=10, color='#CC0000')
    # Show percentage reduction
    pct = round((r/b)*100)
    ax.text(i, max(b, a) + 8, f'({pct}%)', ha='center', va='bottom', fontsize=9, color='#CC0000')

# Customize chart
ax.set_xlabel('Verse Passage', fontsize=12, fontweight='bold')
ax.set_ylabel('Token Count', fontsize=12, fontweight='bold')
ax.set_title('Figure 2: Verse Optimization Token Reduction\n4-Rule Formatting System Achieves 20-21% Reduction Across All Examples',
             fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(passages, fontsize=10)
ax.legend(fontsize=11, loc='upper left')
ax.grid(axis='y', alpha=0.3, linestyle='--')

# Add average line
avg_before = np.mean(before)
avg_after = np.mean(after)
ax.axhline(y=avg_before, color='#8B4513', linestyle='--', linewidth=1, alpha=0.5)
ax.axhline(y=avg_after, color='#228B22', linestyle='--', linewidth=1, alpha=0.5)

# Add text box with summary
textstr = f'Average Reduction: 19.6 tokens (20.6%)\nRange: 12-24 tokens (20-21%)\nConsistent efficiency across all verse types'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.3)
ax.text(0.98, 0.97, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', horizontalalignment='right', bbox=props)

plt.tight_layout()
plt.savefig('Figure_02_Verse_Optimization.png', dpi=300, bbox_inches='tight')
print("✓ Figure 2 saved: Figure_02_Verse_Optimization.png")
plt.close()
