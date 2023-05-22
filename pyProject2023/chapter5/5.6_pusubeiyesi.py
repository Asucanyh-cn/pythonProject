'''
encoding:utf-8
author:yh
date:2023/5/10 10:14
'''
'''
1.产生数据
'''
import sklearn.datasets

X, y = sklearn.datasets.make_moons(200, noise=0.20, random_state=0)
'''
2.样本划分，构建模型
'''
from sklearn.model_selection import train_test_split

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.20, random_state=1)
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(train_X, train_y)
'''
3.结果评估
'''
expected = test_y
predicted = model.predict(test_X)
print('byes 的准确率为：%.2f' % (model.score(train_X, train_y) * 100))
'''
性能指标预测模块
'''
from sklearn import metrics

print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))


'''
鸢尾花预测为例
'''
from sklearn.datasets import load_iris
iris_dataset=load_iris()
X=iris_dataset.data
y=iris_dataset.target

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)

from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(X_train,y_train)

expected=y_test
predicted=model.predict(X_test)

print("准确率为：%.2f"%(model.score(X_train,y_train)*100))

from sklearn import metrics
print(metrics.classification_report(expected,predicted))
print(metrics.confusion_matrix(expected,predicted))

print("%4d" % 5)
