# import required libraries and packages
import pandas as pd
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn import mixture
from yellowbrick.cluster import KElbowVisualizer, SilhouetteVisualizer
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch

master_data = pd.read_csv(r"master data csv.csv", index_col=False) # modify file path for csv upload

# factorise the dataframe so that it can be read by a machine learning model
factorised_data = master_data.apply(lambda x: pd.factorize(x)[0])

# use TSNE to reduce dimensionality
tsne = TSNE(n_components=2, random_state=42)
Z = tsne.fit_transform(factorised_data)

# create a k-Means model an Elbow-Visualizer and show how many clusters it recommends
model = KMeans(random_state=42)
visualizer = KElbowVisualizer(model, k=(1, 8), timings=False)
visualizer.fit(Z)
visualizer.show()

# create a dendrogram to establish number of recommended clusters
plt.figure(figsize=(8, 8))
plt.title('Dendrogram to find Optimum Cluster Number')
Dendrogram = sch.dendrogram((sch.linkage(Z, method='ward')))
plt.show()

# create a silhouette score to check cluster quality
model_3clust = KMeans(n_clusters=2, random_state=42)
sil_visualizer = SilhouetteVisualizer(model_3clust)
sil_visualizer.fit(Z)
sil_visualizer.show()

# specify Gaussian Mixture Model
gmm = mixture.GaussianMixture(n_components=2, covariance_type='full')
# fit the model
gmm.fit(Z)
# extract the clusters predictions according to the highest probability
labels = gmm.predict(Z)
plt.scatter(x=Z[:, 0], y=Z[:, 1], c=labels, cmap='viridis')
plt.show()

# create a cluster map
cluster_map = pd.DataFrame()
cluster_map['data_index'] = factorised_data.index.values
cluster_map['cluster'] = labels

# join cluster map to main dataframe before factorisation so that clusters can be investigated further
df_final = cluster_map.join(master_data, how='right')
df_final.to_csv(r"clusters_labels.csv", index=False) # modify file path for csv download
