'''
encoding:utf-8
author:yh
date:2023/2/16 10:02
'''
def s(x):
    if x==1:
        return  "yes"
    else:
        return "no"
print(s(1))
print(s(2))
# lambda匿名定义
s = lambda x:"yes" if x==1 else "no"
print(s(1))
print(s(2))
