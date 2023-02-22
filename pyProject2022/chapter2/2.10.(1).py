'''
encoding:utf-8
author:yh
date:2022/3/22 9:10
'''
def Fib(n):#递归算法
    if n==1 or n==2:
        return 1
    return Fib(n-1)+Fib(n-2)

print(Fib(4))