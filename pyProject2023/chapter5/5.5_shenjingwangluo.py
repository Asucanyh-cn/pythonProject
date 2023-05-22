'''
encoding:utf-8
author:yh
date:2023/5/8 10:06
'''
'''
1.1加载数据
'''
import sklearn.datasets

'''
使用sklearn.datasets中的make_moons方法，生成月形数据。
::https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html
其它的类型的数据还有：
make_circles 同心圆样本点
make_classification 模拟分类数据集 
'''
X, y = sklearn.datasets.make_moons(200, noise=0.20, random_state=0)
'''
1.2首先使用逻辑回归，并评估模型的性能
'''
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

from sklearn.linear_model import LogisticRegression

'''
LogisticRegression参数
    solver: 逻辑回归损失函数的优化方法。有如下五个可选值：
        liblinear：使用开源的liblinear库实现，使用`坐标轴下降法`来迭代优化损失函数。
        lbfgs：拟牛顿法的一种，利用`损失函数二阶导数`也即海森矩阵来迭代优化损失函数。
        newton-cg：利用`损失函数二阶导数`也即海森矩阵来迭代优化损失函数。
        sag：随机平均梯度下降，与普通梯度下降法的区别时每次迭代仅仅用一部分的样本来计算梯度，适合于样本数据多的时候。
        saga：线性收敛的随机优化算法的的变种。
    其它参数: 
        https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
'''
clf = LogisticRegression(solver='lbfgs')

clf.fit(X_train, y_train)
#
print('逻辑回归的准确率为：%.2f' % (clf.score(X_train, y_train) * 100))
#
from sklearn.metrics import classification_report
#
y_true, y_pred = y_test, clf.predict(X_test)
print(classification_report(y_true, y_pred))
#
'''
2.1 使用MLP神经网络模型
MLPClassifier参数介绍
    solver： 权重优化器，可选值有如下三种 (默认adam)
        lbfgs：拟牛顿法的一种，利用损失函数二阶导数也即海森矩阵来迭代优化损失函数。
        sgd：随机梯度下降
        adam：机遇随机梯度的优化器
        *默认solver使用的‘adam’在相对较大的数据集上效果比较好（几千个样本或者更多），对小数据集来说，lbfgs收敛更快效果也更好。
    hidden_layer_sizes=(5) 表示 hidden_layer 建立 5 个一层神经元，
    hidden_layer_sizes=(5,8) 表示建立两层分别为5和8的神经元。
'''
from sklearn.neural_network import MLPClassifier  # MLP（Multi-layer Perceptron）

clf = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(12), random_state=0)
'''
2.2 模型训练
'''
clf.fit(X_train, y_train)
print('神经网络的准确率为：%.2f' % (clf.score(X_train, y_train) * 100))

from sklearn.metrics import classification_report

y_true, y_pred = y_test, clf.predict(X_test)
print(classification_report(y_true, y_pred))

'''
2.3参数调优
'''
from sklearn import metrics

print(metrics.confusion_matrix(y_true, y_pred))
'''
MLPClassifier中的参数补充
    activation：激活函数的类型。可以是“identity”、“logistic”、“tanh”或者“relu”。默认值是“relu”。
    alpha：L2正则化系数。默认值是0.0001。防止模型过拟合。
    batch_size：随机优化的minibatches的大小。在SGD算法中，每个批次中包含的样本数量。默认值是“auto”。
    ::https://www.shuzhiduo.com/A/A7zgpw6VJ4/
'''
print(clf.get_params())

param_grid = {'hidden_layer_sizes': [3, 5, 10, 12, 15]}
#
import pandas as pd
from sklearn.model_selection import KFold, GridSearchCV

kf = KFold(n_splits=3, shuffle=True, random_state=123)
gs = GridSearchCV(clf, param_grid, 'accuracy', cv=kf, return_train_score=True)
gs.fit(X, y)
cv_results = pd.DataFrame(gs.cv_results_)
print(cv_results)
print(gs.best_estimator_)

clf = gs.best_estimator_
# '''
# 2.4模型训练，评估性能
# '''
clf.fit(X_train, y_train)
print('神经网络的准确率为：%.2f' % (clf.score(X_train, y_train) * 100))
from sklearn.metrics import classification_report

y_true, y_pred = y_test, clf.predict(X_test)
print(classification_report(y_true, y_pred))
'''
2.5预测结果
'''
from sklearn import metrics

print(metrics.confusion_matrix(y_true, y_pred))

X1 = [[1.445, 0.344]]
print(clf.predict(X1))

'''
3.1 BP 神经网络
'''
import sklearn.datasets

X, y = sklearn.datasets.make_moons(200, noise=0.20, random_state=0)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
from sklearn.neural_network import BernoulliRBM

# rbm = BernoulliRBM(n_components=3, learning_rate=0.1, batch_size=10, n_iter=10, random_state=9)
# rbm.fit(X, y)
# '''
# BernoulliRBM没有提供predict方法，下方代码无法使用:
#
# from sklearn.metrics import classification_report
# y_true, y_pred = y, rbm.predict(X)
# print(classification_report(y_true, y_pred))
# '''
from sklearn import linear_model, metrics
from sklearn.neural_network import BernoulliRBM

from sklearn.pipeline import Pipeline

logistic = linear_model.LogisticRegression(solver='lbfgs', max_iter=3000)
rbm = BernoulliRBM(random_state=0, verbose=True)
'''
通过 Pipeline 建立管道，将 BP 神经网络和逻辑回归模型相结合
'''
classifier = Pipeline(steps=[('rbm', rbm), ('logistic', logistic)])
rbm.learning_rate = 0.08  # 学习力
rbm.n_iter = 50  # 迭代次数
rbm.n_components = 10  # n_components 值越大，性能越好，但计算量也越大
logistic.C = 50000
classifier.fit(X_train, y_train)
print('BP 神经网络的准确率为：%.2f' % (classifier.score(X_train, y_train) * 100))
print("Logistic regression using RBM features:\n%s\n" %
      (metrics.classification_report(y_test, classifier.predict(X_test))))
print(metrics.confusion_matrix(y_test, classifier.predict(X_test)))
