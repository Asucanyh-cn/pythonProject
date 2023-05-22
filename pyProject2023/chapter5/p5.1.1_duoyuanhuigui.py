'''
encoding:utf-8
author:yh
date:2023/4/24 10:57
'''
import pandas as pd
data = pd.read_csv('Advertising.csv')
print(data.head())
'''
1.数据特征分析
'''
import matplotlib.pyplot as plt
# fig, axes = plt.subplots(1,3, figsize=(9, 3))
# for n in range(3):
#     axes[n].scatter(data.ix[:,n+1],data.ix[:,4])
# plt.show()
'''
2.提取 TV、Radio、Newspaper 作为 X 变量
'''
feature_cols = ['TV', 'Radio', 'Newspaper'] #指定特征列表
X = data[feature_cols] #提取特征列表数据
print(X.head())

print(type(X)) # <class 'pandas.core.frame.DataFrame'>
print(X.shape) # (200, 3) X 是 200 行 3 列的二维数组
y = data['Sales'] #等价 y = data.Sales
print(y.head())
print(type(y))
print(y.shape)
'''
3.使用交叉验证
交叉验证是划分样本为训练集和测试集的一种有效方法。
如果将所有样本代入模型，可能会导致过拟合，因此用训练集训练模型，在测试集中评估模型。
'''
#训练集和测试集样本划分，默认测试集比例 25%
from sklearn.model_selection import train_test_split
X_train,X_test, y_train, y_test = train_test_split(X, y, random_state=1)
#random_state 参数设定随机种子，以保证每次实验的一致性
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
'''
4.建立模型
将训练集数据代入线性回归模型进行拟合
'''
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
model=linreg.fit(X_train, y_train)
print(model)
print(linreg.intercept_)
print(linreg.coef_)
'''
5.模型评估
将训练集数据代入回归模型得到模型得分，即效果评估系数 R 的平方
'''
print(model.score(X_train,y_train))
#将测试集数据代入模型
y_pred = linreg.predict(X_test)
print(y_pred.round(2))
#将预测结果与实际结果进行比较
plt.plot(range(len(y_pred)),y_pred,'-',label="predict") #预测结果用实线表示
plt.plot(range(len(y_pred)),y_test,'--',label="test") #实际结果用虚线表示
plt.legend(loc="upper right") #显示图中的标签
plt.xlabel("the number of sales")
plt.ylabel('value of sales')
plt.show()