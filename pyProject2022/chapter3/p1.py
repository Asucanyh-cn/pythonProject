'''
encoding:utf-8
author:yh
date:2022/3/28 19:34
'''
'''
Numpy用来处理大型矩阵
一维数组[1,2,3,4,5],称为向量：["1001","zhangsan","男","21","math"],向量是对象的若干特征组合的集合
二维数组[["1001","男",21,"统计"],["1002","李四","女",21,"统计"],......],称为矩阵
三位数组[[[1,2,3],[2,3,4],[7,8,9]],...],三维空间，立体
'''
import matplotlib
import numpy as np #导入模块，取别名np
arr1=np.array([2,3,4])#通过列表创建数组[2,3,4]
print(arr1)#没有逗号，用空格分隔
print(arr1.ndim)#ndim表示返回当前数组的维度值！
arr2=np.array([(1.3,9,2.0),(7,6,1)])#通过元组创建数组(元素是个元组)
print(arr2)
print(arr2.ndim)
arr3=np.zeros((2,3))#通过元组(2,3)生成全零矩阵。两行三列。
print(arr3)
arr4=np.identity(3)#生成n行单位矩阵（单位矩阵一定是方阵）
print(arr4)
arr5=np.random.random((2,3))#产生每个元素都在[0,1]之间的随机矩阵
print(arr5)
arr51=np.random.randn(10)#randn产生的随机数服从标准正态分布
print(arr51)
arr6=np.arange(5,20,3)#生成等距序列，参数为：起点、终点、步长值。含起点值，不含终点值。
print(arr6)
arr7=np.linspace(0,2,5)#生成等距序列，参数为：起点、终点、序列数。含起点和终点值。
print(arr7)
print('——'*100)
print(arr2)
print(arr2.shape)#返回矩阵的规格(i,j)
print(arr2.ndim)#返回维数
print(arr4)
print(arr4.ndim)
print('——'*100)
arr20=np.array([(1,3,-4,1),(2,6,-8,2),(5,-2,3,10)])
print(arr20)
print(arr20.shape)
print(arr20.ndim)
print(arr20.size)#返回矩阵元素总数
print(arr20.dtype)#返回矩阵元素的数据类型
print(type(arr20))#查看整个数组对象的类型
print('——'*100)
def f(x,y):
    return 10*x+y
print(f(3,1))
arr8=np.fromfunction(f,(4,3),dtype=int)
###fromfunction()函数分别将(0,0),(0,1)...(3,2)代入,形成4行3列矩阵
print(arr8)
print('-'*100)
# # 切片，返回第二行到第三行的前2列（范围不包括末尾！）
print(arr8[1:3,:-1])# 1到2行，0到-1列   不写默认为0，-1表示最后一行
print('-'*5)
print(arr8[1:3])#1到2行
print('-'*5)
print(arr8[:,0:2])#0到1列
print('-'*5)
print(arr8[:,[1,2]])#1到2列。用区间可以显示头尾
###
print('-'*100)
b=np.arange(12).reshape(4,3)#arange生成0到11的数值再进行矩阵的再塑
print(b)
print(b.shape)
print(b.ndim)
###
print('-'*100)
arr9=np.array([[2,1],[3,1]])
arr10=np.array([[4,10],[20,8]])
print(arr9)
print('-'*6)
print(arr10)
###
print('——'*6)
print(arr9-arr10)#对应位置数相减
print('——'*6)
print(arr9*arr10)#矩阵元素对应位置数相乘
print(np.dot(arr9,arr10))#矩阵相乘,A矩阵第一行数与B矩阵第一列数相乘得到第一行第一列值，以此类推。
###
print("按行/列求和"+'-'*100)
print(arr10)
print(arr10.T)#矩阵的转置
print(arr10.sum(axis=0))#axis=0按行求和，axis=1按列求和
print(arr10.sum(axis=1))
print(arr10.sum(axis=1).T)#一维数组转置后不变
# print(arr10.sum(axis=1).shape)
print(np.array([arr10.sum(axis=1)]))
print(np.array([arr10.sum(axis=1)]).shape)
print(np.array([arr10.sum(axis=1)]).T)
print(np.array([arr10.sum(axis=1)]).T.shape)
###
print(np.linalg.inv(arr10))#返回逆矩阵A(mn)B(ns)=B(ns)A(mn)=E(m=n=s),方阵才有逆矩阵
print('-'*100)
print(arr9)
print(arr10)
arr11=np.vstack((arr9,arr10))#纵向合并数组，由于与堆栈类似，故命名为vstack
print(arr11)#按列合并，行不变
###
arr12=np.hstack((arr9,arr10))#横向合并数组
print(arr12)
print(np.hsplit(arr12,2))#将数组横向分为两部分，按列划分

