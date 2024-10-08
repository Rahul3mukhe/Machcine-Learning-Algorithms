# -*- coding: utf-8 -*-
"""Hierarichal clustering implementation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Le8wVSkB30H1FXLIbn_QowrfqZCn6s97
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets

#importing iris dataset
iris = datasets.load_iris()

iris_data=pd.DataFrame(iris.data)

iris_data.columns=iris.feature_names

iris_data

#standarsization
from sklearn.preprocessing import StandardScaler
scalar=StandardScaler()

x_scaled = scalar.fit_transform(iris_data)

x_scaled

x_scaled.shape

from sklearn.decomposition import PCA

pca= PCA(n_components=2)

pca

pca_scaled=pca.fit_transform(x_scaled)

pca_scaled

plt.scatter(pca_scaled[:,0],pca_scaled[:,1])

#agglometrive clustering
#to construct a dedogram
import scipy.cluster.hierarchy as sc
plt.figure(figsize=(10,7))
plt.title("dendogram")
sc.dendrogram(sch.linkage(pca_scaled,method='ward'))
plt.xlabel('samples')
plt.ylabel('euclidean distance')

from sklearn.cluster import AgglomerativeClustering
cluster=AgglomerativeClustering(n_clusters=3,affinity='euclidean',linkage='ward')
cluster.fit_predict(pca_scaled)

cluster.labels_

plt.scatter(pca_scaled[:,0],pca_scaled[:,1],c=cluster.labels_)

from sklearn.metrics import silhouette_score

silhouette_coefficients = []
for k in range(2,11):
  agglo = AgglomerativeClustering(n_clusters=k,affinity='euclidean',linkage='ward')
  agglo.fit(x_scaled)
  score = silhouette_score(x_scaled,agglo.labels_)
  silhouette_coefficients.append(score)

plt.plot(range(2,11),silhouette_coefficients)
plt.xlabel("number of clusters")
plt.ylabel("silhouette coefficient")
plt.xticks(range(2,11))
plt.show()

