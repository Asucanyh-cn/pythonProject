'''
encoding:utf-8
author:yh
date:2022/4/4 19:04
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
test = pd.read_csv("csvTest.csv")#用pandas处理数据.将数据交给text变量
print(test.head(5))#输出前5行数据
#输出所有基本统计指标#mean 均值，std 标准差
print(test.describe().round(2))#.round(2)表示保留两位小数
# #输出部分
print(test.describe().loc[['count','mean','std']].round(2))#.loc[['',...,'']]用来引用部分行，单引号内为索引
print("——"*50)
print(test.ix[:,0])
#.ix用来部分输出列。逗号左边为“哪些行”，右边为“哪些列”，“：”为全部的意思。0表示第一列。
print("——"*5)
print(test.ix[0:5,0:2])#（0到4）行 （0到1）列
# print("——"*50)
print(test.ix[:,0].corr(test.ix[:,2]).round(2))#相关系数绝对值0~1之间，0代表完全不相关，1代表完全相关。
print(test.ix[:,1].corr(test.ix[:,2]).round(2))
print("——"*5)
print(range(2))
# for i in range(2):
#     print(i)
#结果：0,1

for i in range(2):
    print(test.ix[:,i].corr(test.ix[:,2]).round(2))

print("——"*50)
fig, axes = plt.subplots(1,2, figsize=(8, 4))
for n in range(2):#画1,2两个子图，大小分别为8，4.
    axes[n].scatter(test.ix[:,n],test.ix[:,2])
    #scatter表示画散点图.绘制第 1 列和第 3 列、第 2 列和第 3 列之间散点图
# plt.show()#显示图形
# print("——"*50)
x = np.linspace(-5,2,100)#用numpy创建-5到2，100个等距数列


# print(x)
# y1 = x**3 + 5*x**2 + 10
# plt.rcParams['font.sans-serif']=['SimHei']#正确显示汉字
# plt.rcParams['axes.unicode_minus']=False #正确显示负号
# plt.plot(x,y1)#绘制曲线
# plt.title("y1曲线")#设置标题
# plt.xlabel("x")
# plt.ylabbel("y")
# plt.show()
# print("——"*5)
# y2 = 3*x**2 +10*x
# y3 = 6*x +10
# # plt.plot(x,y2)
# # plt.show()
# # plt.plot(x,y3)
# # plt.show()
# # 如何让图形显示在一张图上？
# fig, ax=plt.subplots()
# ax.plot(x,y1,color='b',label="y(x)")
# ax.plot(x,y2,color='g',label="y'(x)")
# ax.plot(x,y3,color='r',label="y''(x)")
# plt.set_xlabel("x")#设置坐标轴名字
# plt.set_ylabbel("y")
# ax.legend(loc=0,ncol=3,frameon=False)#加图例标签
# plt.show()
# fig.savefig("figure-1.pdf")#保存图片为pdf
# print("——"*50)
# fig, axes = plt.subplots(figsize=(6,3))#用figsize定义图的大小（当图片保存到磁盘时具有一定的大小和纵横比
# ax.plot(x,y1,lw=1.5,c="blue",label="$y(x)$")#lw线粗
# ax.plot(x,y2,lw=1.5,color="r",label="$y'(x)$")
# ax.plot(x,y3,lw=1.5,color="green",label="$y(x)$")
# ax.plot(x,np.zeros_like(x),lw=0.5,color="black")
# ax.plot([-3.33,-3.33],[0,(-3.33)**3 + 5*(-3.33)**2 + 10],ls='--',lw=1,color="black")
# ax.plot([0,0],[0,10],ls='--',lw=1,color="black")
# ax.plot([0],[10],lw=0.5,marker='o',color="blue")
# ax.plot([-3.33,-3.33],[0,(-3.33)**3 + 5*(-3.33)**2 + 10],ls='--',lw=1,marker='o',color="black")#画点，o要小写
# ax.set_ylim(-15,40)#显示y轴的上下限
# ax.set_yticks([-10,0,10,20,30])#画y轴的刻度和x轴的刻度
# ax.set_yticks([-5,-3,-1,0,1,3])
# ax.set_xticks(['第一个','第二个','第三个','第四个'])
# ax.set_xlabel("$x$",fontsize=18)
# ax.set_ylabel("$y$",fontsize=18)
