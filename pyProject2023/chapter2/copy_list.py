'''
encoding:utf-8
author:yh
date:2023/2/22 11:20
'''
import copy
# 模块copy和内嵌copy函数的对比
list=['a','b',['1','2']]
list1=list.copy() ## list内嵌的copy函数为浅复制
list2=copy.copy(list)
print(list,list1,list2,sep='\n')
print("-"*10)
list.append('c')
list[2].append(3)
print(list,list1,list2,sep='\n')
print("-"*10)
list.append('c')
print(list,list1,list2,sep='\n')
print("-"*10)
# 使用copy模块的例子
list=['a','b',['1','2']]
list1=copy.copy(list)
list2=copy.deepcopy(list)
print(list,list1,list2,sep='\n')
print("-"*10)
list.append('c')
list[2].append(3)
print(list,list1,list2,sep='\n')