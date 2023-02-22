'''
encoding:utf-8
author:yh
date:2023/2/16 10:08
'''
import math
a = round(math.pi,3)
b = math.sqrt(16)
# 单分支if
if a>b:
    print(a)
else:
    print(b)
# 多分支if
weather = 'sunny'
if weather=='sunny':
    print("shopping")
elif weather=='cloudy':
    print("playing football")
else:
    print("learning python")
# while语句
a = 100
s = 0
while a:
    s=s+a
    a-=1
print("s=%d"%s)
print("s="+str(s))# 等价
## %的格式化作用
print("%s:%d"%("ab",34))
# for语句
for a in ['e','f','g']:
    print(a)
for a in 'string':
    print(a)
for a in range(2,10):
    print(a)
## 判断2~9是否为质数
for n in range(2,10):
    for x in range(2,n): # 将整个内循环for 看作一个if 语句
        if n%x==0:
            print(n,'equals',x,'*',n/x)
            break
    else:
        print(n,'是一个质数')

# continue语句
for i in range(1,10):
    if i%2==0:
        continue # 直接进入下一个循环
    print(i,end=" ")
# break命令
print("猜字游戏！")
import random
sec=random.randint(1,9)
# sec=1
guess=0
while guess!=sec:
    temp=input("请猜数字：")
    guess=int(temp)
    if guess==sec:
        print("你真是我肚子里的蛔虫啊！")
        break
    if guess>sec:
        print("大哥大！")
        continue
    if guess<sec:
        print("小了小了！")
        continue
print("游戏结束！")