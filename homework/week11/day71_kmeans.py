# Day 71 · 聚类：没有标签时让数据自己分组
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans

folder = os.path.dirname(os.path.abspath(__file__))

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']   
plt.rcParams['axes.unicode_minus'] = False  

rng = np.random.default_rng(42)
n = 100

x1 = np.concatenate([rng.normal(-1,1,n), rng.normal(1,1,n)])
x2 = np.concatenate([rng.normal(-1,1,n), rng.normal(1,1,n)])

X = np.column_stack([x1,x2])

km = KMeans(n_clusters=2,n_init=10,random_state=0)
km.fit(X)
print(km.cluster_centers_)
print(km.inertia_)
print(km.labels_[:10])

plt.scatter(X[:,0],X[:,1],c=km.labels_,cmap="coolwarm",s=15)
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],
            marker="*",s=300,c="black",label="中心")
plt.legend()
plt.savefig(os.path.join(folder,"kmeans.png"))




