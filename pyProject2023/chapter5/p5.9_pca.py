'''
encoding:utf-8
author:yh
date:2023/5/17 10:03
'''
'''
PCA 降维在图像识别中的应用
'''
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_olivetti_faces

faces = fetch_olivetti_faces()
X = faces.data
y = faces.target

print(X)
print(X.shape)

from sklearn.decomposition import PCA

candidate_components = range(10, 300, 30)
explained_ratios = []
for c in candidate_components:
    pca = PCA(n_components=c)
    X_pca = pca.fit_transform(X)
    explained_ratios.append(np.sum(pca.explained_variance_ratio_))
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.figure(figsize=(8, 4))
plt.grid()
plt.plot(candidate_components, explained_ratios)
plt.xlabel('主成分个数')
plt.ylabel('成份的累积方差贡献率')
plt.title('成份-方差贡献率')
plt.yticks(np.arange(0.5, 1.05, .05))
plt.xticks(np.arange(0, 300, 20))
plt.show()
pca = PCA(n_components=140)
X_pca = pca.fit_transform(X)
print(X_pca.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=33)
from sklearn.svm import SVC

print(SVC().get_params())
param_grid = {'C': [1, 5, 10, 50, 100], 'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01]}
from sklearn.model_selection import GridSearchCV

clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)
clf = clf.fit(X_train, y_train)
print(clf.best_params_, clf.best_score_)

print(clf.best_estimator_.score(X_test, y_test))

