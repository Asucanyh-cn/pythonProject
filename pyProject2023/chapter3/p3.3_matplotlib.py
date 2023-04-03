'''
encoding:utf-8
author:yh
date:2023/3/6 10:02
'''
import numpy as np
import pandas as pd

data = pd.read_csv("csvTest.csv")
print(data.head())
# 查看数据的统计指标
print(data.describe())
# 相关系数

# 绘制散点图
import matplotlib.pyplot as plt

## 定义画布和坐标轴
# fig, axes=plt.subplots(1,2,figsize=(8,4))
# for i in range(2):
#     axes[i].scatter(data.ix[:,i],data.ix[:,2])
# plt.show()

# 绘制方程曲线
x = np.linspace(-5, 2, 100)  # 生成-5~2之间的100个数，它们是等差数列。
print(x)
y1 = x ** 3 + 5 * x ** 2 + 10
# plt.rcParams['font.sans-serif']=['SimHei']# 正确显示汉字
# plt.rcParams['axes.unicode_minus']=False # 正确显示负号
# plt.title('y1曲线') # 定义主标题
# plt.xlabel('x轴') # 设置x轴名字
# plt.ylabel('y轴')
# plt.plot(x,y1)
# plt.show()
y2 = 3 * x ** 2 + 10 * x
# plt.plot(x,y2)
# plt.show()
y3 = 6 * x + 10
# plt.plot(x,y3)
# plt.show()

# 将图形绘制在同一张画布
# fig, ax=plt.subplots()
# ax.plot(x,y3,c='b',label="y''(x)")
# ax.plot(x,y2,c='g',label="y'(x)")
# ax.plot(x,y1,c='r',label="y(x)")
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.legend()
# # plt.show()
# fig.savefig("figure-1.pdf")
## 进一步优化
# fig, ax=plt.subplots()
# ax.plot(x,y3,c='b',label="$y''(x)$",lw=0.5) # c参数=color参数 ，lw为lineweight设置粗细，ls为linestyle设置线类型
# ax.plot(x,y2,c='g',label="$y'(x)$",lw=0.5)
# ax.plot(x,y1,c='r',label="$y(x)=x^3+5x^2+10$",lw=0.5)
# ax.set_xlabel("$x$")
# ax.set_ylabel("$y$")
# ax.plot([0,0],[0,10],ls='--',lw=0.5,c='b') # 绘制线段
# ax.plot([0],[10],lw=0.5,marker='o',c='b') # 绘制点
# ax.legend(loc=0,ncol=3,frameon=False) # loc为0自动寻找最佳位置,ncol设置图例列数，frameon设置是否开启边框
# ax.plot(x,np.zeros_like(x),lw=0.5,c='black')
# plt.show()


# 线图、阶梯图、面积图
## 线图
x = np.linspace(-3, 3, 25)
# print(x)
# y1 = x ** 3 + 3 * x ** 2 + 10
# y2 = -1.5 * x ** 3 + 10 * x ** 2 - 15
# fig, ax = plt.subplots(figsize=(4, 3))
# ax.plot(x, y1, color='r', label='$y1$')
# ax.plot(x, y2, color='b', label='$y2$')
# ax.legend(loc=0, ncol=2, frameon=False)
# plt.show()
# ##阶梯图
# fig, ax=plt.subplots(figsize=(4,3))
# ax.step(x,y1)
# ax.step(x,y2)
# plt.show()
##面积图
# fig, ax=plt.subplots(figsize=(4,3))
# ax.fill_between(x,y1,y2) #将y1,y2之间的面积填起来
# plt.show()
# ## 子图
x = np.linspace(-3, 3, 25)
y1 = x ** 3 + 3 * x ** 2 + 10
y2 = -1.5 * x ** 3 + 10 * x ** 2 - 15
y3 = 4 * x + 5
y4 = 3 * x ** 2 + 2 * x + 2
# fig, axes = plt.subplots(1,4,figsize=(12,2))
# y=[y1,y2,y3,y4]
# for i in range(4):
#     axes[i].plot(x,y[i])
# plt.show()
# ## 设置子图布局
# fig, axes=plt.subplots(2,2,figsize=(8,4))
# axes[0,0].plot(x,y1)
# axes[0,1].plot(x,y2)
# axes[1,0].plot(x,y3)
# axes[1,1].plot(x,y4)
#
# plt.subplot(2,1,1)
# plt.plot(x,y1)
# plt.subplot(2,2,3)
# plt.plot(x,y2)
# plt.subplot(2,2,4)
# plt.plot(x,y3)
# plt.show()

# import matplotlib.pyplot as plot
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus']=False
# fig=plt.figure(figsize=(20,20))
# x=range(5)
# y=[2,2,5,2,4]
# s=['数量1','数量2','数量3','数量4','数量5']
# ax1=fig.add_subplot(2,2,1)
# plt.bar(x,y,width=0.5)
# plt.xticks(x,s,rotation=0)
# ax2=fig.add_subplot(2,2,2)
# plt.bar(range(4),[3,4,2,3],width=0.3)
# plt.xticks(x,s,rotation=0)
# ax3=fig.add_subplot(2,2,3)
# plt.bar(range(4),[3,4,2,3],width=0.3)
# plt.xticks(x,s,rotation=90)
# ax4=fig.add_subplot(2,2,4)
# plt.bar(range(4),[3,4,2,3],width=0.3)
# plt.xticks(x,s,rotation=90)
# plt.show()

# 从数据文件中读取，然后生成条形图
import pandas as pd
data=pd.read_csv('data.csv')
print(data)
data=pd.DataFrame(data)
fig=plt.figure(figsize=(20,20))
x=range(5)
s=list(data)
s.pop(0)
print(s)

y1=data.iloc[0,1:].tolist()
y2=data.iloc[1,1:].tolist()
y3=data.iloc[2,1:].tolist()
y4=data.iloc[3,1:].tolist()
y5=data.iloc[4,1:].values.tolist()
print(y1)

ax1=fig.add_subplot(2,3,1)
plt.bar(x,y1,width=0.5)
plt.xticks(x,s,rotation=0)

ax2=fig.add_subplot(2,3,2)
plt.bar(x,y2,width=0.5)
plt.xticks(x,s,rotation=0)

ax3=fig.add_subplot(2,3,3)
plt.bar(x,y3,width=0.5)
plt.xticks(x,s,rotation=0)

ax4=fig.add_subplot(2,3,4)
plt.bar(x,y4,width=0.5)
plt.xticks(x,s,rotation=0)

ax5=fig.add_subplot(2,3,5)
plt.bar(x,y5,width=0.5)
plt.xticks(x,s,rotation=0)

plt.show()