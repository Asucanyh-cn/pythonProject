'''
encoding:utf-8
author:yh
date:2023/4/24 10:00
'''
# import warnings
# warnings.filterwarnings('ignore') #过滤警告信息，忽略版本问题

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('input_data.csv')
# print(data.head())

X=data[['square_feet']] #两个中括号，使数据类型从series变为dataframe
y=data[['price']]
# print(type(X))
# print(X)
'''
1.数据特征分析
'''
# fig,axes=plt.subplots(figsize=[3,3])
# axes.scatter(X,y)
# plt.show()
'''
2.建立模型，线性模型
'''
from sklearn.linear_model import LinearRegression
linreg=LinearRegression() #初始化
model=linreg.fit(X,y)
print(model) #copy_X是否复制数据，fit_intercept是否有截距，n_jobs调用内核数，normalize是否标准化
print(model.intercept_) #打印截距
print(model.coef_) #打印系数
'''
3.模型评估
模型得分用效果评估系数 R 的平方来衡量， R 平方越接近于 1，表示回归模型拟合效果越好
'''
print(model.score(X,y))
'''
4.拟合检验
将预测结果绘制线图和实际结果进行比较
'''
plt.subplots(figsize=[6,3])
plt.scatter(X,y,color='blue')
plt.plot(X,linreg.predict(X),color='red',linewidth=2)
plt.show()
'''
5.预测
将需要预测的面积变量 700、800 传入模型的预测参数
'''
y_pred = linreg.predict([[700], [800]]) #每一个输入 X 是一个列表，对应 y一个值
print(y_pred)