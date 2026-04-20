import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.lines import Line2D

# upload required csv file
data = pd.read_csv(r"gender split.csv", index_col=False) # modify file path to upload csv

fig, ax = plt.subplots(figsize=(8, 6))

# specify marker size
marker_sizes = data['% split']

# specify colour rule for markers
colours = np.where(data["Gender"] == "Girls", 'pink', 'blue')

# create scatter plot and show
scatter = ax.scatter(
    data['% Rate of Absence'],
    data['GCSE Pass Average %'],
    s=marker_sizes,
    c=colours,  # Color based on third variable
    alpha=0.9,                        # Transparency
)

custom_legend = [
    Line2D([0], [0], marker='o', color='w', label='girls',
           markerfacecolor='pink', markersize=10),
    Line2D([0], [0], marker='o', color='w', label='boys',
           markerfacecolor='blue', markersize=10)
]

ax.set_xlabel('% Rate of Absence')
ax.set_ylabel('GCSE Pass Average %')
ax.set_title('Rate of Absence by GCSE Pass Average in Schools with >90% of one Gender')
ax.legend(handles=custom_legend, title="Gender", loc='upper right')

ax.grid(True, linestyle='--', alpha=0.5)

legend_labels = ['boys', 'girls']

plt.tight_layout()
plt.show()
