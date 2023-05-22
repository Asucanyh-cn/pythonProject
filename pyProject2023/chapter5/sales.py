'''
encoding:utf-8
author:yh
date:2023/5/22 10:05
'''
'''
1. 加载数据
'''
import pandas as pd

data = pd.read_csv('sales.csv')
print(data)
'''
2. 数据探索
'''
print(data.describe(include='all'))
print(data.shape)
'''
2.1 面积分布情况
'''
import matplotlib.pyplot as plt

plt.hist(data['mj'].dropna(), bins=60)  # bins 制定直方图中条形的个数
# plt.show()
'''
2.2 面积异常值探索
'''
plt.boxplot(data['mj'].dropna())
# plt.show()
'''
3. 数据集划分
'''
X = data[['qy', 'fx', 'mj', 'jg']]
y = data['lb']
from sklearn.model_selection import train_test_split

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=1)
print(train_X.shape, train_y.shape)
print(test_X.shape, test_y.shape)
print("——" * 50)

mj_train_na = pd.isnull(train_X['mj'])
mj_test_na = pd.isnull(test_X['mj'])
print(mj_train_na)
print(mj_test_na)
print("——" * 50)

train_X = train_X.values
test_X = test_X.values
train_X_copy = train_X.copy()
'''
4. 数据填充
'''
from sklearn.preprocessing import Imputer

imp = Imputer(strategy='mean')
imp.fit(train_X[:, [2]])

train_X[:, [2]] = imp.transform(train_X[:, [2]])
print(train_X[:])
print("——" * 50)
print(test_X[:5])
print("——" * 50)
test_X[:, [2]] = imp.transform(test_X[:, [2]])
print(test_X[:5])
'''
5. 类别变量处理
'''
from sklearn.preprocessing import LabelEncoder

print(train_X[:5, 0])
print(train_X[:5, 1])
print("——" * 50)

le_qy = LabelEncoder()
le_qy.fit(train_X[:, 0])
train_X[:, 0] = le_qy.transform(train_X[:, 0])
le_fx = LabelEncoder()
le_fx.fit(train_X[:, 1])
train_X[:, 1] = le_fx.transform(train_X[:, 1])

print(train_X[:5])
print("——" * 50)
'''
6. 数据特征选择
'''
# ①图形观察法
qy = train_X[:, 0]
fx = train_X[:, 1]
mj = train_X[:, 2]
jg = train_X[:, 3]
lb = train_y
fig, axes = plt.subplots(1, 4, figsize=[12, 3])
axes[0].scatter(qy, lb)
axes[1].scatter(fx, lb)
axes[2].scatter(mj, lb)
axes[3].scatter(jg, lb)
# plt.show()
# ②方差分析统计方法
from sklearn.feature_selection import SelectKBest, chi2

skb = SelectKBest(chi2, k=3)
skb.fit(train_X, train_y)
train_X_3 = skb.transform(train_X)
print(train_X_3[:5])

import numpy as np

features = ['qy', 'fx', 'mj', 'jg']
scores = pd.DataFrame({'feature': np.array(features), 'score': skb.scores_})
scores.sort_values('score', ascending=False, inplace=True)
print(scores)

plt.bar(np.arange(4), scores['score'], log=True)
plt.xticks(np.arange(4), scores['feature'], rotation=30)
# plt.show()
# ③机器学习方法
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier()
sfm = SelectFromModel(clf, threshold=0.2)  # 设定阈值 0.2
sfm.fit(train_X, train_y)
train_X_clf = sfm.transform(train_X)
print(train_X_clf[:5])

scores = pd.DataFrame({'feature': np.array(features),
                       'score': sfm.estimator_.feature_importances_})
scores.sort_values('score', ascending=False, inplace=True)
print(scores)

plt.bar(np.arange(4), scores['score'], log=True)
plt.xticks(np.arange(4), scores['feature'], rotation=30)
# plt.show()

'''
7. 建模与调优
'''
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(random_state=1)
print(clf.get_params())
param_grid = {'max_depth': [3, 4, 5, 6, 7, 8, 9, 10], 'min_impurity_decrease': [0.01, 0.02, 0.03]}
from sklearn.model_selection import KFold

kf = KFold(n_splits=3, shuffle=True, random_state=123)
from sklearn.model_selection import GridSearchCV

gs = GridSearchCV(clf, param_grid, 'accuracy', cv=kf)

gs.fit(train_X_3, train_y)
cv_results = pd.DataFrame(gs.cv_results_)
print(cv_results[['param_max_depth', 'param_min_impurity_decrease', 'mean_test_score']])
print(gs.best_estimator_)
fig, ax = plt.subplots()
grouped = cv_results.groupby('param_min_impurity_decrease')
for key, group in grouped:
    group.plot(ax=ax, x='param_max_depth', y='mean_test_score', label=key)
plt.show()
