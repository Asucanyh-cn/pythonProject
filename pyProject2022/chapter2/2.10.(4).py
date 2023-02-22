'''
encoding:utf-8
author:yh
date:2022/3/22 9:32
'''
tel=''
tel2=[]
while len(tel)!=4:
    tel=input("四位整数：")
for j in range(4):
    tel2.append((int(tel[j])+5)%10)
tel2.reverse()
print(tel2)
tel=''
for i in tel2:
    tel=tel+str(i)
print("加密后为：{0}".format(tel))