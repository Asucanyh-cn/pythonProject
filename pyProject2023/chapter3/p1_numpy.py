'''
encoding:utf-8
author:yh
date:2023/2/27 10:01
'''
import numpy as np
arr1 = np.array([2,3,4]) #通过*列表*创建一维矩阵
arr2 = np.array([(1.3,9,2.0),(7,6,1)]) #通过*元组*创建二行三列的二维矩阵
print(arr1)
print(arr2)
arr3 = np.zeros((2,3)) #通过元组(2, 3)生成全零二行三列的二维矩阵
print(arr3)
arr4 = np.identity(3) #生成三行三列的二维*单位矩阵*，对角线为1
print(arr4)
#生成每个元素都在[0,1]之间的二行三列随机矩阵
## 第一个random表示numpy中的子模块（类），第二个random表示类中的方法，size是方法中的参数‘size=（行，列）’，random()生成的是均匀的随机数
## 补充：random中还有个randn()生成服从标准的正态分布的随机数
arr5 = np.random.random(size = (2,3))
print(arr5)
arr6 = np.arange(5,20,3) #等距序列，参数为起点，终点，步长值。含起点值，不含终点值
print(arr6)
arr7 = np.linspace(0,2,5) #等距序列，参数为起点，终点，序列数。含起点值和终点值
print(arr7)
print(arr6) # [ 5 8 11 14 17]
print(arr1)
print(arr1.shape)
print(arr2)
print(arr2.shape) #返回矩阵的规格(2, 3)
print(arr1.ndim)
print(arr2.ndim) #返回矩阵的维度 2
print(arr2.size) #返回矩阵元素总数 6
# print(arr2.dtype.name) #返回矩阵元素的数据类型 float64
# print(type(arr2)) #查看整个数组对象的类型 <class 'numpy.ndarray'>

def f(x,y):
    return 10*x+y
arr8=np.fromfunction(f,(4,3),dtype=int)
print(arr8)
# 切片操作
print(arr8[1:3,1:])
print(arr8[:,1:]) #必须指定行列，不能为空
print(arr8[:,1:2]) #只要某一列
# arange
b= np.arange(12).reshape(3,4) #用 0 到 11 的整数生成三行四列的二维矩阵
print(b)

arr9 = np.array([[2,1],[3,1]])
arr10 = np.array([[1,2],[3,4]])
print(arr9,'\n',arr10)
# 矩阵相减
print(arr9-arr10)
# 乘法
## 对应位置相乘
print(arr9*arr10)
## 矩阵乘法
print(np.dot(arr9,arr10))
# 转置
print(arr10.T)
# 求逆矩阵
print(np.linalg.inv(arr10))
# 矩阵元素的求和、最大值、沿行（列）累计求和
print(np.sum(arr10))
print(np.max(arr10))
print(np.min(arr10))
print(arr10.cumsum(axis=0)) #axis=1 沿列累计
# 矩阵指数
print(np.exp(arr9))