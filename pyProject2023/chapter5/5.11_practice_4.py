'''
encoding:utf-8
author:yh
date:2023/5/17 17:52
'''
import pandas as pd

data = pd.read_csv('wine.data', header=-1)
print(data.head())
Y = data[0]
X = data.iloc[:, 1:15]
'''
标准化处理
'''
from sklearn.preprocessing import StandardScaler
import pandas as pd

X = pd.DataFrame(StandardScaler().fit_transform(X), columns=X.columns)
# print(X.head())

'''
PCA
'''
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

X = np.array(X)
print(X)
candidate_components = range(1, 13, 1)
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
plt.xticks(np.arange(0, 13, 1))
plt.show()
pca = PCA(n_components=5)
X_pca = pca.fit_transform(X)
print(X_pca.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_pca, Y, test_size=0.2, random_state=33)
from sklearn.svm import SVC

print(SVC().get_params())
param_grid = {'C': [1, 5, 10, 50, 100], 'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01]}

from sklearn.model_selection import GridSearchCV

clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)
clf = clf.fit(X_train, y_train)
print(clf.best_params_, clf.best_score_)

print(clf.best_estimator_.score(X_test, y_test))
