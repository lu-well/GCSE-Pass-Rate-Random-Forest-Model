# import required libraries and packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

gcse_clusters = pd.read_csv(r"gcse clusters csv.csv", index_col=False) # modify file path for csv upload

cluster_a = gcse_clusters["cluster 1"]
cluster_b = gcse_clusters["cluster 2"]
cluster_b = cluster_b[~np.isnan(cluster_b)]
without_special_schools = gcse_clusters["without special schools"]
without_special_schools = without_special_schools[~np.isnan(without_special_schools)]

# graph to compare cluster 1 and cluster 2
combined = np.concatenate([cluster_a, cluster_b])

# define mean and std below and above to include in graph
overall_mean = 69.32063
std_below = 51.52357
std_above = 87.1177

# plot histogram with density curve
plt.figure(figsize=(8, 5))

# add kernel density estimates
sns_kde1 = stats.gaussian_kde(cluster_a)
sns_kde2 = stats.gaussian_kde(cluster_b)
x_vals = np.linspace(min(combined), max(combined), 200)
plt.plot(x_vals, sns_kde1(x_vals), color="blue", lw=2, label="Cluster 1")
plt.plot(x_vals, sns_kde2(x_vals), color="orange", lw=2, label="Cluster 2")

# add vertical lines for mean, std above and std below
plt.axvline(std_below, color="grey", linestyle="--", label=f"1 Standard Deviation Below = {std_below:.2f}")
plt.axvline(std_above, color="grey", linestyle="--", label=f"1 Standard Deviation Above = {std_above:.2f}")
plt.axvline(overall_mean, color="black", linestyle="-", label=f"Mean = {overall_mean:.2f}")

plt.title("GCSE Pass Rate % Cluster Distribution Comparison")
plt.xlabel("GCSE Pass Rate %")
plt.ylabel("Density")
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()

# graph to compare cluster 1 and cluster 2 in the case that special schools are removed from the dataset
combined = np.concatenate([cluster_a, without_special_schools])

# define mean and std below and above to include in graph
overall_mean = 69.32063
std_below = 51.52357
std_above = 87.1177

# plot histogram with density curve
plt.figure(figsize=(8, 5))

# add kernel density estimates
sns_kde1 = stats.gaussian_kde(cluster_a)
sns_kde2 = stats.gaussian_kde(without_special_schools)
x_vals = np.linspace(min(combined), max(combined), 200)
plt.plot(x_vals, sns_kde1(x_vals), color="blue", lw=2, label="Cluster 1")
plt.plot(x_vals, sns_kde2(x_vals), color="orange", lw=2, label="Cluster 2 without Special Schools")

# add vertical lines for mean, std above and std below
plt.axvline(std_below, color="grey", linestyle="--", label=f"1 Standard Deviation Below = {std_below:.2f}")
plt.axvline(std_above, color="grey", linestyle="--", label=f"1 Standard Deviation Above = {std_above:.2f}")
plt.axvline(overall_mean, color="black", linestyle="-", label=f"Mean = {overall_mean:.2f}")

plt.title("GCSE Pass Rate % Cluster Distribution Comparison when Special Schools are Removed")
plt.xlabel("GCSE Pass Rate %")
plt.ylabel("Density")
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
