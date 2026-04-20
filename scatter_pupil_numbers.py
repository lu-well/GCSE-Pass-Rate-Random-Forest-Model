# import required libraries and modules
import matplotlib.pyplot as plt
import pandas as pd

# import csv file
data = pd.read_csv(r"num pupils gcse ave.csv", index_col=False) # modify file path to upload csv

fig, ax = plt.subplots(figsize=(8, 6))

marker_sizes = data['% Rate of Absence'] * 3

# create scatter plot and show graph
scatter = ax.scatter(
    data['Number of Pupils'],
    data['GCSE Pass Average %'],
    s=marker_sizes,
    c=data['% Rate of Absence'],
    cmap='viridis_r',
    alpha=0.9,
)


cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('% Rate of Absence')

# create rolling average line in graph
avg_number_pupils = data.groupby('Number of Pupils', as_index=False)['GCSE Pass Average %'].mean()
avg_number_pupils['gcse_smooth'] = avg_number_pupils['GCSE Pass Average %'].rolling(window=10, center=True, min_periods=1).mean()
ax.plot(avg_number_pupils['Number of Pupils'], avg_number_pupils['gcse_smooth'], color='black', linestyle='-', linewidth=1, label='Smoothed average')

ax.set_xlabel('Number of pupils')
ax.set_ylabel('GCSE Pass Average %')
ax.set_title('Number of Pupils per School by GCSE Pass Average with Rolling Average and Rate of Absence')

ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
