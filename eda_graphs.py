import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r"master data csv.csv", index_col=False) # modify file path for csv upload

gcse_data = data['GCSE Pass Average %']

# define mean and std
gcse_mean = np.mean(gcse_data)
gcse_std_dev = np.std(gcse_data)

# plot GCSE pass rate histogram
plt.figure(figsize=(8, 6))
plt.hist(gcse_data, bins=30, color='lightskyblue', edgecolor='black', alpha=0.7)

# add line to show mean
plt.axvline(gcse_mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean = {gcse_mean:.2f}')

# add lines to show standard deviation
plt.axvline(gcse_mean + gcse_std_dev, color='green', linestyle='dashed', linewidth=2,
            label=f'+1 Std Dev = {gcse_mean + gcse_std_dev:.2f}')
plt.axvline(gcse_mean - gcse_std_dev, color='green', linestyle='dashed', linewidth=2,
            label=f'-1 Std Dev = {gcse_mean - gcse_std_dev:.2f}')

plt.title('Average % GCSE Pass Rate for all Schools')
plt.xlabel('% GCSE Pass Rate')
plt.ylabel('Frequency')
plt.legend()

plt.tight_layout()
plt.show()

ofsted_data = data['Ofsted Average']

# customise size of bins
bin_edges = [0, 1.5, 2.5, 3.5, 4]

# create bins
bins = pd.cut(ofsted_data, bins=bin_edges, right=False)  # right=False means [start, end)
bin_counts = bins.value_counts().sort_index()

# plot ofsted bar graph
plt.figure(figsize=(8, 5))
plt.bar(bin_counts.index.astype(str), bin_counts.values, width=0.6, color='lightskyblue', edgecolor='black')
plt.text(-0.25, 350, "Outstanding")
plt.text(0.9, 1540, "Good")
plt.text(1.6, 850, "Requires Improvement")
plt.text(2.8, 50, "Inadequate")

plt.xlabel("Average Ofsted Rating")
plt.ylabel("Frequency")
plt.title("Ofsted Average for all Schools")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

pupils_data = data['Number of Pupils']

pupils_mean = np.mean(pupils_data)
pupils_mean = int(pupils_mean)
pupils_std_dev = np.std(pupils_data)
pupils_std_dev = int(pupils_std_dev)

# plot number of pupils histogram
plt.figure(figsize=(8, 6))
plt.hist(pupils_data, bins=30, color='lightskyblue', edgecolor='black', alpha=0.7)

# add line to show mean
plt.axvline(pupils_mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean = {pupils_mean:.2f}')

# add lines to show standard deviation
plt.axvline(pupils_mean + pupils_std_dev, color='green', linestyle='dashed', linewidth=2,
            label=f'+1 Std Dev = {pupils_mean + pupils_std_dev:.2f}')
plt.axvline(pupils_mean - pupils_std_dev, color='green', linestyle='dashed', linewidth=2,
            label=f'-1 Std Dev = {pupils_mean - pupils_std_dev:.2f}')

plt.title('Number of Pupils for all Schools')
plt.xlabel('Number of Pupils')
plt.ylabel('Frequency')
plt.legend()

plt.tight_layout()
plt.show()

absence_data = data['% Rate of Absence']

absence_mean = np.mean(absence_data)
absence_std_dev = np.std(absence_data)

# plot rate of absence histogram
plt.figure(figsize=(8, 6))
plt.hist(absence_data, bins=30, color='lightskyblue', edgecolor='black', alpha=0.7)

# add line to show mean
plt.axvline(absence_mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean = {absence_mean:.2f}')

# add lines to show standard deviation
plt.axvline(absence_mean + absence_std_dev, color='green', linestyle='dashed', linewidth=2,
            label=f'+1 Std Dev = {absence_mean + absence_std_dev:.2f}')
plt.axvline(absence_mean - absence_std_dev, color='green', linestyle='dashed', linewidth=2,
            label=f'-1 Std Dev = {absence_mean - absence_std_dev:.2f}')

plt.title('% Rate of Absence Across all Schools')
plt.xlabel('% Rate of Absence')
plt.ylabel('Frequency')
plt.legend()

plt.tight_layout()
plt.show()

data['Class size'] = data['Class size'].replace(r'^\s*$', np.nan, regex=True)
data = data.dropna(subset=['Class size'])
class_size_data = data['Class size']

class_size_mean = np.mean(class_size_data)
class_size_mean = int(class_size_mean)
class_size_std_dev = np.std(class_size_data)
class_size_std_dev = int(class_size_std_dev)

# plot class size histogram
plt.figure(figsize=(8, 6))
plt.hist(class_size_data, bins=18, color='lightskyblue', edgecolor='black', alpha=0.7)

# add line to show mean
plt.axvline(class_size_mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean = {class_size_mean:.2f}')

# add lines to show standard deviation
plt.axvline(class_size_mean + class_size_std_dev, color='green', linestyle='dashed', linewidth=2,
            label=f'+1 Std Dev = {class_size_mean + class_size_std_dev:.2f}')
plt.axvline(class_size_mean - class_size_std_dev, color='green', linestyle='dashed', linewidth=2,
            label=f'-1 Std Dev = {class_size_mean - class_size_std_dev:.2f}')

plt.title('Average Class Size Across all Schools')
plt.xlabel('Class Size')
plt.ylabel('Frequency')
plt.legend()

plt.tight_layout()
plt.show()

fsm_data = data['% FSM']

fsm_mean = np.mean(fsm_data)
fsm_std_dev = np.std(fsm_data)

# plot FSM eligibility histogram
plt.figure(figsize=(8, 6))
plt.hist(fsm_data, bins=30, color='lightskyblue', edgecolor='black', alpha=0.7)

# add line to show mean
plt.axvline(fsm_mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean = {fsm_mean:.2f}')

# add lines to show standard deviation
plt.axvline(fsm_mean + fsm_std_dev, color='green', linestyle='dashed', linewidth=2,
            label=f'+1 Std Dev = {fsm_mean + fsm_std_dev:.2f}')
plt.axvline(fsm_mean - fsm_std_dev, color='green', linestyle='dashed', linewidth=2,
            label=f'-1 Std Dev = {fsm_mean - fsm_std_dev:.2f}')

plt.title('% Pupils Eligible for Free School Meals')
plt.xlabel('% FSM Pupils')
plt.ylabel('Frequency')
plt.legend()

plt.tight_layout()
plt.show()

eng_nfl_data = data['% ENG NFL']

eng_nfl_mean = np.mean(eng_nfl_data)
eng_nfl_std_dev = np.std(eng_nfl_data)

# plot English not as first language histogram
plt.figure(figsize=(8, 6))
plt.hist(eng_nfl_data, bins=30, color='lightskyblue', edgecolor='black', alpha=0.7)

# add line to show mean
plt.axvline(eng_nfl_mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean = {eng_nfl_mean:.2f}')

# add lines to show standard deviation
plt.axvline(eng_nfl_mean + eng_nfl_std_dev, color='green', linestyle='dashed', linewidth=2,
            label=f'+1 Std Dev = {eng_nfl_mean + eng_nfl_std_dev:.2f}')

plt.title('% Pupils whose First Language is known or believed not to be English')
plt.xlabel('% Pupils')
plt.ylabel('Frequency')
plt.legend()

plt.tight_layout()
plt.show()
