import pandas as pd
import numpy as np
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"master data csv.csv", index_col=False) # modify file path for csv upload

# create variables for all features to be used in correlation matrix
gcse = data["GCSE Pass Average %"]
number_pupils = data["Number of Pupils"]
percent_boys = data["% Boys"]
percent_girls = data["% Girls"]
rate_absence = data["% Rate of Absence"]
percent_fsm = data["% FSM"]
percent_eng_nfl = data["% English not first language"]
class_size = data["Class size"]
white_british = data["white British"]
irish = data["Irish"]
irish_traveller = data["traveller of Irish heritage"]
white_other = data["any other white background"]
gypsy_roma = data["Gypsy/Roma"]
wb_caribbean = data["white and black Caribbean"]
wb_african = data["white and black African"]
w_asian = data["white and Asian"]
other_mixed = data["any other mixed background"]
indian = data["Indian"]
pakistani = data["Pakistani"]
bangladeshi = data["Bangladeshi"]
asian_other = data["any other Asian background"]
caribbean = data["Caribbean"]
african = data["African"]
black_other = data["any other black background"]
chinese = data["Chinese"]
any_other = data["any other"]
unclassified = data["unclassified"]
ofsted_average = data["Ofsted Average"]
interaction = data["interaction"]

# convert all variables into numpy arrays
gcse_array = np.array(gcse, dtype=float)
number_pupils_array = np.array(number_pupils, dtype=float)
percent_boys_array = np.array(percent_boys, dtype=float)
percent_girls_array = np.array(percent_girls, dtype=float)
rate_absence_array = np.array(rate_absence, dtype=float)
percent_fsm_array = np.array(percent_fsm, dtype=float)
percent_eng_nfl_array = np.array(percent_eng_nfl, dtype=float)
class_size_array = np.array(class_size, dtype=float)
white_british_array = np.array(white_british, dtype=float)
irish_array = np.array(irish, dtype=float)
irish_traveller_array = np.array(irish_traveller, dtype=float)
white_other_array = np.array(white_other, dtype=float)
gypsy_roma_array = np.array(gypsy_roma, dtype=float)
wb_caribbean_array = np.array(wb_caribbean, dtype=float)
wb_african_array = np.array(wb_african, dtype=float)
w_asian_array = np.array(w_asian, dtype=float)
other_mixed_array = np.array(other_mixed, dtype=float)
indian_array = np.array(indian, dtype=float)
pakistani_array = np.array(pakistani, dtype=float)
bangladeshi_array = np.array(bangladeshi, dtype=float)
asian_other_array = np.array(asian_other, dtype=float)
caribbean_array = np.array(caribbean, dtype=float)
african_array = np.array(african, dtype=float)
black_other_array = np.array(black_other, dtype=float)
chinese_array = np.array(chinese, dtype=float)
any_other_array = np.array(any_other, dtype=float)
unclassified_array = np.array(unclassified, dtype=float)
ofsted_average_array = np.array(ofsted_average, dtype=float)
interaction_array = np.array(interaction, dtype=float)

# manually calculate correlation coefficients between selected features
corr_coef, p_value = pearsonr(gcse_array, number_pupils_array)
print(f"Pearson correlation coefficient with number of pupils: {corr_coef:.4f}")
print(f"P-value number of pupils: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, percent_boys_array)
print(f"Pearson correlation coefficient with % boys: {corr_coef:.4f}")
print(f"P-value % boys: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, percent_girls_array)
print(f"Pearson correlation coefficient with % girls: {corr_coef:.4f}")
print(f"P-value % girls: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, rate_absence_array)
print(f"Pearson correlation coefficient with absence rate: {corr_coef:.4f}")
print(f"P-value absence rate: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, percent_fsm_array)
print(f"Pearson correlation coefficient with % FSM: {corr_coef:.4f}")
print(f"P-value % FSM: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, percent_eng_nfl_array)
print(f"Pearson correlation coefficient with % ENG NFL: {corr_coef:.4f}")
print(f"P-value % ENG NFL: {p_value:.4e}")



corr_coef, p_value = pearsonr(gcse_array, white_british_array)
print(f"Pearson correlation coefficient with white British: {corr_coef:.4f}")
print(f"P-value white British: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, irish_array)
print(f"Pearson correlation coefficient with Irish: {corr_coef:.4f}")
print(f"P-value Irish: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, irish_traveller_array)
print(f"Pearson correlation coefficient with Irish traveller: {corr_coef:.4f}")
print(f"P-value Irish traveller: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, white_other_array)
print(f"Pearson correlation coefficient with white other: {corr_coef:.4f}")
print(f"P-value white other: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, gypsy_roma_array)
print(f"Pearson correlation coefficient with Gypsy Roma: {corr_coef:.4f}")
print(f"P-value Gypsy Roma: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, wb_caribbean_array)
print(f"Pearson correlation coefficient with white black Caribbean: {corr_coef:.4f}")
print(f"P-value white black Caribbean: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, wb_african_array)
print(f"Pearson correlation coefficient with white black African: {corr_coef:.4f}")
print(f"P-value white black African: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, w_asian_array)
print(f"Pearson correlation coefficient with white & Asian: {corr_coef:.4f}")
print(f"P-value white & Asian: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, other_mixed_array)
print(f"Pearson correlation coefficient with any other mixed: {corr_coef:.4f}")
print(f"P-value any other mixed: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, indian_array)
print(f"Pearson correlation coefficient with Indian: {corr_coef:.4f}")
print(f"P-value Indian: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, pakistani_array)
print(f"Pearson correlation coefficient with Pakistani: {corr_coef:.4f}")
print(f"P-value Pakistani: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, bangladeshi_array)
print(f"Pearson correlation coefficient with Bangladeshi: {corr_coef:.4f}")
print(f"P-value Bangladeshi: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, asian_other_array)
print(f"Pearson correlation coefficient with Asian other: {corr_coef:.4f}")
print(f"P-value Asian other: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, caribbean_array)
print(f"Pearson correlation coefficient with Caribbean: {corr_coef:.4f}")
print(f"P-value Caribbean: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, african_array)
print(f"Pearson correlation coefficient with African: {corr_coef:.4f}")
print(f"P-value African: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, black_other_array)
print(f"Pearson correlation coefficient with black other: {corr_coef:.4f}")
print(f"P-value black other: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, chinese_array)
print(f"Pearson correlation coefficient with Chinese: {corr_coef:.4f}")
print(f"P-value Chinese: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, any_other_array)
print(f"Pearson correlation coefficient with any other: {corr_coef:.4f}")
print(f"P-value any other: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, unclassified_array)
print(f"Pearson correlation coefficient with unclassified: {corr_coef:.4f}")
print(f"P-value unclassified: {p_value:.4e}")

corr_coef, p_value = pearsonr(gcse_array, interaction_array)
print(f"Pearson correlation coefficient with FSM absence interaction: {corr_coef:.4f}")
print(f"P-value FSM absence interaction: {p_value:.4e}")

correlation, p_value = spearmanr(gcse_array, ofsted_average_array)
print("Spearman Correlation GCSE pass rate with Ofsted average:", correlation)
print("P-value Ofsted average:", p_value)

correlation, p_value = spearmanr(ofsted_average_array, percent_fsm_array)
print("Spearman Correlation % FSM with Ofsted average:", correlation)
print("P-value Ofsted average:", p_value)

correlation, p_value = spearmanr(ofsted_average_array, rate_absence_array)
print("Spearman Correlation Absence with Ofsted average:", correlation)
print("P-value Ofsted average:", p_value)

correlation, p_value = spearmanr(ofsted_average_array, number_pupils_array)
print("Spearman Correlation Number of pupils with Ofsted average:", correlation)
print("P-value Ofsted average:", p_value)

# create correlation matrix for all continuous and discrete variables
correlation_matrix_data = data[["GCSE Pass Average %", "Number of Pupils", "% Boys", "% Girls", "% Rate of Absence",
                                "% FSM", "% English not first language", "Class size", "white British", "Irish",
                                "traveller of Irish heritage", "any other white background", "Gypsy/Roma",
                                "white and black Caribbean", "white and black African", "white and Asian",
                                "any other mixed background", "Indian", "Pakistani", "Bangladeshi",
                                "any other Asian background", "Caribbean", "African", "any other black background",
                                "Chinese", "any other", "unclassified"]]

correlation_matrix = correlation_matrix_data.corr(method='pearson')
print(correlation_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, annot_kws={"size": 6})
plt.xticks(fontsize=8, rotation=45, ha='right')
plt.yticks(fontsize=8, rotation=0)
plt.title('Correlations Between Continuous and Discrete Features Including Ethnicity')
plt.show()

# create correlation matrix for selected continuous and discrete variables
correlation_matrix_w_data = data[["GCSE Pass Average %", "Number of Pupils", "% Boys", "% Girls", "% Rate of Absence",
                                 "% FSM", "% English not first language", "Class size"]]

correlation_matrix_w = correlation_matrix_w_data.corr(method='pearson')
print(correlation_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix_w, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, annot_kws={"size": 8})
plt.xticks(fontsize=8, rotation=45, ha='right')
plt.yticks(fontsize=8, rotation=0)
plt.title('Correlations Between Continuous and Discrete Features')
plt.show()
