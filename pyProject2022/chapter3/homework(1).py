'''
encoding:utf-8
author:yh
date:2022/4/2 17:22
'''
import numpy as np
arr=np.array([[2,0,-1.4],[2.2,0.2,-1.5],[2.4,0.1,-1],[2.4,0.1,-1],[1.9,0,-1.2]])
print(arr)
print(arr.T)
print(np.max(arr))
print(np.min(arr))
print(arr.sum(axis=0))
print(arr.sum(axis=1))
