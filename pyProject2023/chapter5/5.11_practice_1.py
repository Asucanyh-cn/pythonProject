'''
encoding:utf-8
author:yh
date:2023/4/26 11:26
'''
'''
现有 17 个西瓜样本数据集 watermelon.csv，根据密度（demension），含糖率（sugar），
判断是否是好瓜，数据保存在 watermelon.csv 文件中，如表 5-3 所示，试建立逻辑回归分类
模型。
'''
import warnings
warnings.filterwarnings('ignore')
'''
1.加载数据
'''
import pandas as pd
data = pd.read_csv('watermelon.csv')
# print(data.head(50))
'''
2.特征处理
output 1 好瓜
output 0 坏瓜
'''
data_dum=pd.get_dummies(data,prefix='output',columns=['output'],drop_first=True)
'''
3.交叉验证
'''
from sklearn.model_selection import train_test_split
X=data_dum.ix[:,1:-1]
y=data_dum.ix[:,-1]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=500)
# print(X_train)
# print(X_test)
# print(y_train)
# print(y_test)

'''
4.建立模型
'''
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression(solver='liblinear')
lr.fit(X_train,y_train)
print(lr.intercept_)
print(lr.coef_)

'''
5.模型评估
'''
print('逻辑回归的准确率为：%.2f'%(lr.score(X_test, y_test) *100))

from sklearn.metrics import classification_report
y_true, y_pred = y_test, lr.predict(X_test)
print(classification_report(y_true, y_pred))