'''
encoding:utf-8
author:yh
date:2023/5/15 10:20
'''
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

X, y = make_blobs(n_samples=1000, n_features=2, centers=[[-1, -1], [0, 0], [1, 1], [2, 2]],
                  cluster_std=[0.4, 0.2, 0.2, 0.2], random_state=9)
# plt.scatter(X[:, 0], X[:, 1], marker='o')
# plt.show()

print(X)

'''
k-means聚类
'''

from sklearn.cluster import KMeans

y_pred = KMeans(n_clusters=2, random_state=1).fit_predict(X)
# plt.scatter(X[:, 0], X[:, 1], c=y_pred)
# plt.show()

'''
使用Calinski-Harabasz分数评估
'''
from sklearn import metrics
print(metrics.calinski_harabaz_score(X,y_pred))

'''
手肘法确定最佳K值
'''
from sklearn.cluster import KMeans
SSE = [] # 存放每次结果的误差平方和
for k in range(1,10):
    estimator = KMeans(n_clusters=k) # 构造聚类器
    estimator.fit(X)
    SSE.append(estimator.inertia_)
x = range(1,10)
plt.xlabel('k')
plt.ylabel('SSE')
# plt.plot(x,SSE,'o-')
# plt.show()

'''
层次聚类
'''
from sklearn.cluster import AgglomerativeClustering
y_pred = AgglomerativeClustering(affinity='euclidean',linkage='ward',n_clusters=4).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
print(metrics.calinski_harabaz_score(X, y_pred)) # 5666.92902528
'''
基于密度的聚类
'''
from sklearn.cluster import DBSCAN
y_pred =DBSCAN(eps=0.4,min_samples=110).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
print(metrics.calinski_harabaz_score(X, y_pred)) # 5879.65178153

