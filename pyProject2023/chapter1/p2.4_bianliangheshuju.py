'''
encoding:utf-8
author:yh
date:2023/2/16 10:06
'''
x=3
print(x)
print(id(x)) # 查询x的内存地址

x=x*2 # 重新赋值，x的内存地址将被回收并重新分配
print(x)
print(id(x))