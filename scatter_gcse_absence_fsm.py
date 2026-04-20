import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv(r"master data csv.csv", index_col=False) # modify file path for csv upload

x = data["% Rate of Absence"]
y = data["% FSM"]
z = data["GCSE Pass Average %"]

# specify colour conditions for markers
colours = np.where(
    data["Admissions"] == "Selective",
    'yellow',
    np.where(
        data["Establishment Type"] == "Special schools",
        'red',
        'blue'
    )
)

# plot and show scatter graph
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=data,
    x='GCSE Pass Average %', y='% Rate of Absence',
    size='% FSM', hue=colours,
    sizes=(0, 100),
    alpha=1,
    edgecolor='k'
)

legend_labels = ['School type and FSM%', 'all other schools', 'special schools', 'selective schools', '15', '30',
                 '45', '60', '75']

plt.title('GCSE Pass Average by Rate of Absence and FSM eligibility')
plt.legend(legend_labels)
plt.grid(True)
plt.show()
