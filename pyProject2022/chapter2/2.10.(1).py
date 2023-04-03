'''
encoding:utf-8
author:yh
date:2022/3/22 9:10
'''
#递归算法
def Fib(n):
    if n==1 or n==2:
        return 1
    return Fib(n-1)+Fib(n-2)
for n in range(1,11):
    print(Fib(n),end=' ')