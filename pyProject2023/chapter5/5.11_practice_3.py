'''
encoding:utf-8
author:yh
date:2023/5/17 11:06
'''
import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_excel('air.xls', encoding='utf-8')
# print(data)
# print(data.iloc[:,1:])

X = data.iloc[:, 1:5]
print(X)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
data_scaled = scaler.fit_transform(X)

'''
1. K-means
'''
'''
1.1 使用手肘法调整k值
'''
import matplotlib.pyplot as plt
from sklearn import metrics

SSE = []  # 存放每次结果的误差平方和
for k in range(1, 10):
    estimator = KMeans(n_clusters=k)  # 构造聚类器
    estimator.fit(data_scaled)
    SSE.append(estimator.inertia_)
x = range(1, 10)
# plt.xlabel('k')
# plt.ylabel('SSE')
# plt.plot(x, SSE, 'o-')
# plt.show()
'''
1.2 最终建模
'''
y_pred = KMeans(n_clusters=6, random_state=9).fit_predict(data_scaled)
data['K-means聚类'] = y_pred
# print(data)
'''
1.3 聚类效果评价
'''
print(metrics.calinski_harabaz_score(X, y_pred))
'''
2. 层次聚类
'''
from sklearn.cluster import AgglomerativeClustering

y_pred = AgglomerativeClustering(affinity='euclidean', linkage='ward', n_clusters=3).fit_predict(data_scaled)
data['层次聚类'] = y_pred
# print(data)
'''
2.1 聚类效果评价
'''
print(metrics.calinski_harabaz_score(X, y_pred))

'''
3.DBSCAN 聚类
'''
from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=1, min_samples=2)
y_pred = dbscan.fit_predict(data_scaled)

data['DBSCAN聚类'] = y_pred
print(data)
