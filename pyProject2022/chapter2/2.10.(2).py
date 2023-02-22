'''
encoding:utf-8
author:yh
date:2022/3/22 9:23
'''
List=[2,5,8,12,35,56,9,4,12,55]
odd=[]
even=[]
for a in List:
    if a%2==0:
        even.append(a)
    else:
        odd.append(a)
print(List)
print(odd)
print(even)