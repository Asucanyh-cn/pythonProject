'''
encoding:utf-8
author:yh
date:2023/5/6 11:17
'''
'''
支持向量机
支持向量指边界点
找到最优的边界点，用以划分
'''
'''
1.产生数据
'''
import sklearn.datasets
import matplotlib.pyplot as plt

X, y = sklearn.datasets.make_moons(200, noise=0.20, random_state=0)
# print(X, y)
'''
2.数据集划分
'''
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

'''
3.模型构建
'''
from sklearn import metrics
from sklearn.svm import SVC

model = SVC(gamma='auto')
model.fit(X_train, y_train)
'''
4.模型评估
'''
print('SVC 的准确率为：%.2f'%(model.score(X_train, y_train) *100))
expected = y_test
predicted = model.predict(X_test)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
'''
5.超参数调优
其中，C 是惩罚系数，即对误差的宽容度。C 越高，说明越不能容忍出现误差，容易过拟合；C 越小，容易欠拟合。
'''
print(model.get_params())
'''
将备选参数定义为字典，传入 GridSearchCV 进行 KFold 交叉验证，得出各个参数的平
均性能指标和排序，从而选择最优参数
'''
param_grid = {'C': [0.1,1,10,100]}
import pandas as pd
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
kf = KFold(n_splits=3, shuffle=True, random_state=123)
gs = GridSearchCV(model, param_grid, 'accuracy', cv = kf, return_train_score=True)
gs.fit(X_train, y_train)
cv_results = pd.DataFrame(gs.cv_results_)
print(cv_results[['param_C','mean_score_time','mean_test_score','rank_test_score']])

print(gs.best_estimator_)
'''
6.构建模型
'''
model=gs.best_estimator_
model.fit(X_train, y_train)
'''
7.结果评估
'''
print('SVC 的准确率为：%.2f'%(model.score(X_train, y_train) *100))
expected = y_test
predicted = model.predict(X_test)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))