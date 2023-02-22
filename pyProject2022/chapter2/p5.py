'''
encoding:utf-8
author:yh
date:2022/3/21 19:15
'''
fp = open('news.txt',encoding='gbk')
a = fp.read() #读取文件中的所有信息
fp.close()
print(a)
#
# x=input("请输入要查找的字符")
# print(a.count(x))
#打开文件，a表示追加方式打开，w表示覆盖方式打开，r表示只读方式
# with open('mykkk.txt','a') as f:
#     f.write("\nI love Python")
# with open('mykkk.txt','w') as f:
#     f.write("\nI love Python")
#由于是只读，无法运行
#with open('mykkk.txt','r') as f:
 #   f.write("\nI love Python")
with open('mykkk.txt','r') as f:
     print(f.read())
#错误！
# with open('mykkk.txt', 'r') as f:
#     print(f.readlines())
#     for line in f.readlines():
#         print(line.strip())   #strip(）去掉首尾空格和换行符
#         #w为什么后面的循环没有执行呢？
#         #打印完后，文件关闭数据没有了，所有后面的for循环没有执行
#正确！
#先将数据赋值给a再使用循环输出！
with open('mykkk.txt', 'r') as f:
    a=f.readlines()
for line in a:
    print(line.strip())  # strip(）去掉首尾空格和换行符
#无strip()
for line in a:
    print(line)
print('——'*90) #分割线
import json #json为数据字典文件
with open("jd.json",'r',encoding='utf-8') as f:
    jd=f.read()
dic=json.loads(jd)
print(dic)
for c in dic: #遍历dic，依次将元素赋值给c
    print(c.get('name'),c.get('age'),c.get('comment'))
print('——'*90) #分割线
import pandas as pd
###格式化列表文件
pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)
x = pd.read_excel('mtpl.xls','Sheet1')
print(x.head())#m默认显示前5行
print("——"*90)

pd.set_option('display.max_colwidth',50) #设置最大列宽
train = pd.read_csv("doubanpd.csv",encoding='gbk')
print(train.head())
print("——"*90)
print(train['reviews'].head(10))