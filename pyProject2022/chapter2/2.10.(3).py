'''
encoding:utf-8
author:yh
date:2022/3/22 9:29
'''
fp=open('news.txt')
a=fp.read()
fp.close()
print(a)
n=input()
print(a.count(n))