'''
encoding:utf-8
author:yh
date:2023/4/27 11:02
'''
import pandas as pd

data = pd.read_csv('bankloan.csv')
# print(data.head(50))

'''
对各个特征进行统计描述，data.describe()默认只统计数值列，include='all'，表示所有特征列，
以观察各个特征的统计描述、类型、是否有缺失值等
'''
# print(data.describe(include='all'))
print(data.describe())
'''
1.1数据处理
指标分组
1.1.1 年龄分组
年轻人：18岁至24岁之间的年轻人，正在大学就读或已经毕业。
中年人：25岁至64岁之间的中年人。
老年人：65岁及以上的人。
'''
data.loc[data['age'] <= 25, 'age'] = 0
data.loc[(data['age'] <= 64) & (data['age']>25), 'age'] = 1
data.loc[data['age']>64, 'age'] = 2

'''
1.1.2 雇员年限分组
0-3 短
3-7 中
7-10 较长
10+ 长
'''
data.loc[data['employ']<=3,'employ']=0
data.loc[(data['employ']<=7)&(data['employ']>3),'employ']=1
data.loc[(data['employ']<=10)&(data['employ']>7),'employ']=2
data.loc[data['employ']>10,'employ']=3

'''
1.1.3 居住年限分组
0-3 短
3-7 中
7-10 较长
10+ 长
'''
data.loc[data['address']<=3,'address']=0
data.loc[(data['address']<=7)&(data['address']>3),'address']=1
data.loc[(data['address']<=10)&(data['address']>7),'address']=2
data.loc[data['address']>10,'address']=3

'''
1.1.4 收入分组
0-15 低 
15-30 中
30+ 高
'''
data.loc[data['income']<=15,'income']=0
data.loc[(data['income']<=30)&(data['income']>3),'income']=1
data.loc[data['income']>30,'income']=2

'''
1.1.5 收入债务比分组
0-5 优 
5-10 良
10-15 中
15+ 差
'''
data.loc[data['debtinc']<=5,'debtinc']=0
data.loc[(data['debtinc']<=10)&(data['debtinc']>5),'debtinc']=1
data.loc[(data['debtinc']<=15)&(data['debtinc']>10),'debtinc']=2
data.loc[data['debtinc']>15,'debtinc']=3

'''
1.1.5 信用卡债务比分组
0-0.5 优 
0.5-1 良
1-1.5 中
1.5+ 差
'''
data.loc[data['creddebt']<=0.5,'creddebt']=0
data.loc[(data['creddebt']<=1)&(data['creddebt']>0.5),'creddebt']=1
data.loc[(data['creddebt']<=1.5)&(data['creddebt']>1),'creddebt']=2
data.loc[data['creddebt']>1.5,'creddebt']=3

'''
1.1.5 其它债务比分组
0-1 优 
1-2 良
2-3 中
3+ 差
'''
data.loc[data['othdebt']<=1,'othdebt']=0
data.loc[(data['othdebt']<=2)&(data['othdebt']>1),'othdebt']=1
data.loc[(data['othdebt']<=3)&(data['othdebt']>2),'othdebt']=2
data.loc[data['othdebt']>3,'othdebt']=3
'''
1.1.6 教育程度分组
0-3 0
3-5 1
'''
data.loc[data['ed']<=3,'ed']=0
data.loc[data['ed']>3,'ed']=1

'''
①自变量和因变量的提取
'''

# X=data.iloc[:700,4:-3] #用收入相关指标作为自变量
# y=data.iloc[:700,-1]
# X=data.iloc[:700,5:-1] #用负债相关指标作为自变量
# y=data.iloc[:700,-1]
X = data.iloc[:700, 0:-1]  #使用所有指标
y = data.iloc[:700, -1]

'''
②交叉验证, 将数据随机分成训练集和测试集
'''
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3, random_state=1)

print(X_train.tail(5))
print(y_train.tail(5))
print(X_test.tail(5))
print(y_test.tail(5))

from sklearn.tree import DecisionTreeClassifier

'''
默认的是基于 Gini 不纯度分类，基尼系数是一种评估数据集分割点优劣的成本函数
'''
clf = DecisionTreeClassifier(random_state=1)  # 设置随机种子，使决策树结果一致
clf = clf.fit(X_train, y_train)
# print(clf.feature_importances_)
#
'''
③模型评估，将训练集带入模型
输出模型的预测得分和混淆矩阵统计报告
'''
pre_labels = clf.predict(X_test)
print(pre_labels)
print('决策树的准确率为：%.2f' % (clf.score(X_test, y_test) * 100))

from sklearn.metrics import classification_report
#召回率
print(classification_report(y_test, pre_labels))

from sklearn.tree import export_graphviz
from pydotplus import graph_from_dot_data
features_2=['income', 'debtinc']
features_3=['debtinc', 'creddebt', 'othdebt']
features_4=['income', 'debtinc', 'creddebt', 'othdebt']
features_8 = ['age', 'ed', 'employ', 'address', 'income', 'debtinc', 'creddebt', 'othdebt']
features=features_8
dot_data = export_graphviz(clf, out_file=None, feature_names=features, filled=True, rounded=True)
graph = graph_from_dot_data(dot_data)
graph.write_png("tree_credit_practice_2.png")

import matplotlib.pyplot as plt

img = plt.imread('tree_credit_practice_2.png')
fig = plt.figure(figsize=(16, 8))
plt.imshow(img)
plt.axis('off')
# plt.show()

'''
④预测结果
预测700条数据后的数据
'''
X_pre=data.iloc[701:,0:-1]
# print(X_pre)
pre_labels = clf.predict(X_pre)

print(type(pre_labels))
for i in range(len(pre_labels)):
    print('第',i+701,'条记录的预测结果:',pre_labels[i])