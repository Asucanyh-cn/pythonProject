'''
encoding:utf-8
author:yh
date:2023/2/27 10:47
'''
import pandas as pd
import matplotlib.pyplot as plt

stu = pd.read_csv('grade.csv')
print(stu)

# x = range(4)
x = range(9)
xm = []
km = []
cj = []

xm = stu.iloc[:, 0].values.tolist()
print(xm)

km = list(stu);
km.pop(0);
print(km)

for i in range(1, 5):
    cj.append(stu.iloc[:, i].values.tolist())
print(cj)

fig = plt.figure(figsize=(20, 20))

for i in range(4):
    fig.add_subplot(2, 2, i + 1)
    plt.bar(x, cj[i], width=0.5)
    plt.xticks(x, xm, rotation=15)
    plt.title(km[i])
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()
