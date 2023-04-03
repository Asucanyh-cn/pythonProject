'''
encoding:utf-8
author:yh
date:2023/3/6 17:50
'''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# 鸢尾化数据集分为两部分，data和target，target为类别其中0代表‘setosa’，1代表‘versicolor’，2代表‘virginica’
iris_dataset = load_iris()
coln = ['SpealLength', 'Spealwidth', 'Petalwidth', 'PetalLength']
iris = pd.DataFrame(iris_dataset.data, columns=coln)

fType={0: "Setosa", 1: "Versicolour", 2: "Virginica"}

print(type(iris_dataset))
print(iris.head())
##查看数据的维度，以及种类的维度
print(iris_dataset.data.shape)
print(iris_dataset.target.shape)

print(iris_dataset.data)
print(iris_dataset.target)

## 方法一，使用条件分出各类别
fig, axes = plt.subplots(1,3,figsize=(12,4))
#单个图
# print(iris_dataset['data'][iris_dataset['target'] == 0])
# iris = iris_dataset['data'][iris_dataset['target'] == 0]
# iris_df = pd.DataFrame(iris, columns=coln)
# axes[0].set_xlabel("Length")
# axes[0].set_ylabel("Width")
# axes[0].scatter(iris_df.ix[:, 0], iris_df.ix[:, 1], c='b')
# axes[0].scatter(iris_df.ix[:, 3], iris_df.ix[:, 2], c='r')
# axes[0].legend(loc=0, ncol=2, frameon=False)
# plt.show()
##循环生成多个
for i in range(3):
    iris = iris_dataset['data'][iris_dataset['target'] == i]
    iris_df = pd.DataFrame(iris, columns=coln)
    print(iris_df.head())
    axes[i].set_xlabel("Length")
    axes[i].set_ylabel("Width")
    axes[i].scatter(iris_df.ix[:, 0], iris_df.ix[:, 1], c='b')
    axes[i].scatter(iris_df.ix[:, 3], iris_df.ix[:, 2], c='r')
    axes[i].legend(loc=0, ncol=1, frameon=True)
    axes[i].set_title(fType[i])
# plt.show()

# # 箱线图
## 单个
# iris = iris_dataset['data'][iris_dataset['target'] == 0]
# iris_df= pd.DataFrame(iris, columns=coln)
#
# fig, bp=plt.subplots()
# data_to_bp=[]
# for i in range(4):
#     data_to_bp.append(iris_df.iloc[:,i])
# plt.boxplot(data_to_bp)
# plt.xticks(range(1,5),coln,rotation=0)
# plt.show()
##多个子图

fig=plt.figure(figsize=(12,4))
for i in range(3):
    iris = iris_dataset['data'][iris_dataset['target'] == i]
    iris_df = pd.DataFrame(iris, columns=coln)

    ax=fig.add_subplot(1,3,i+1)
    plt.xticks(range(1,5),coln)
    data_to_bp=[]
    for n in range(4):
        data_to_bp.append(iris_df.iloc[:, n])
    plt.boxplot(data_to_bp)
    plt.title(fType[i])
plt.show()