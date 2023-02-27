'''
encoding:utf-8
author:yh
date:2023/2/22 10:17
'''
fp=open("news.txt",encoding='utf-8')
a=fp.read()
fp.close()
print(a)
import json
with open("jsonData.txt",'r',encoding='utf-8') as f:
# with open("jd.json",'r',encoding='utf-8') as f:
    b=f.read()
dict=json.loads(b)
print(dict)
for c in dict:
    print(c.get('pageName'))
####
import json #json为数据字典文件
with open("jd.json",'r',encoding='utf-8') as f:
    jd=f.read()
dic=json.loads(jd)
print(dic)
for c in dic: #遍历dic，依次将元素赋值给c
    print(c.get('name'),c.get('age'),c.get('comment'))
print('——'*90) #分割线
import pandas as pd
# with open("mydata.txt",encoding='utf-8') as f:
#     f.write("I love python.")
# import pandas as pd
# pd.set_option('display.unicode.ambiguous_as_wide', True)
# pd.set_option('display.unicode.east_asian_width', True)
# df = pd.read_excel('mtpl.xls', 'Sheet1')
# print(df.head())
# #
# pd.set_option('display.max_colwidth',50) #设置最大列宽
# train = pd.read_csv("doubanpd.csv",encoding='gbk')
# print(train.head())
# print("——"*90)
# print(train['reviews'].head(10))