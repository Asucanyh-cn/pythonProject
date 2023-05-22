'''
encoding:utf-8
author:yh
date:2023/5/6 10:02
'''

import warnings
warnings.filterwarnings('ignore')
'''
k近邻
'''
import sklearn.datasets
import matplotlib.pyplot as plt
'''
make_moons 
产生200条数据，20%的干扰项，随机种子为0
'''
X, y = sklearn.datasets.make_moons(200, noise=0.20,random_state=0)
print(X,y)
plt.scatter(X[:,0], X[:,1], s=40, c=y) #s设置点的大小，c设置颜色
# plt.show()

print("——"*50)
'''
数据预处理
1. 数据标准化处理（归一化）
   处理数量级不一致
'''
from sklearn import preprocessing
normalized_X = preprocessing.minmax_scale(X)
'''
2. 规范化（正则化）
    处理数据差异较大
  2.1 L1正则公式
    L1正则化可以产生稀疏权值矩阵，即产生一个稀疏模型，可以用于特征选择
  2.2 L2正则公式
    L2正则化可以防止模型过拟合（overfitting）；一定程度上，L1也可以防止过拟合
::https://blog.csdn.net/jinping_shi/article/details/52433975

标准化处理和归一化处理都是数据预处理的方法，目的是将数据转换为统一的尺度，以便更好地进行数据分析和建模。
    标准化处理是将数据按照一定的比例缩放，使得数据的均值为0，标准差为1。
    标准化处理可以消除不同变量之间的量纲影响，使得不同变量之间可以进行比较和分析。常见的标准化方法有Z-score标准化和范围缩放标准化。
    
    归一化处理是将数据按照比例缩放到一个固定的范围内，通常是[0,1]或[-1,1]。
    归一化处理可以将数据映射到一个相同的尺度，避免不同变量之间的权重不一致。常见的归一化方法有最小-最大缩放和L2范数归一化。
'''
normalized_X = preprocessing.normalize(X)
print(normalized_X[0:5])

'''
随机森林
RandomForest
'''

from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier( n_estimators=100)
clf.fit(X,y)
print(clf.feature_importances_)

from sklearn.neighbors import  KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=15)
model.fit(X,y)
'''
模型评估
'''
from sklearn import metrics
from sklearn.metrics import classification_report
y_true,y_pred=y,model.predict(X)
print(classification_report(y_true,y_pred))

print(metrics.confusion_matrix(y_true,y_pred))
'''
鸢尾花预测
'''
from sklearn.datasets import load_iris
iris_dataset=load_iris()
print(iris_dataset.data.shape) # (150, 4)
print(iris_dataset.target.shape) #(150,)
print(iris_dataset['data'][:5])
'''
1.划分测试集和训练集
'''
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(iris_dataset['data'],iris_dataset['target'],test_size=0.25,random_state=0)
'''
2.建立k近邻分类器，并进行训练
'''
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
'''
3.分类器评估
'''
from sklearn import metrics
from sklearn.metrics import classification_report
y_true, y_pred = y_test, knn.predict(X_test)
print(classification_report(y_true, y_pred))

print(metrics.confusion_matrix(y_true, y_pred))

y1=knn.predict([[5,2.9,1,0.2]])
print(y1) #0