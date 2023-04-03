'''
encoding:utf-8
author:yh
date:2023/2/27 10:47
'''
import numpy as np
arr=np.array([[2,0,-1.4],[2.2,0.2,-1.5],[2.4,0.1,-1],[1.9,0,-1.2]])
print(arr)
print("矩阵的转置")
print(arr.T)
print("矩阵的最大值")
print(np.max(arr))
print("矩阵的最小值")
print(np.min(arr))
print("矩阵按行（列）累计求和")
print(arr.sum(axis=1))
print(arr.sum(axis=0))
