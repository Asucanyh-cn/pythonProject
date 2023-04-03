'''
encoding:utf-8
author:yh
date:2023/3/1 10:00
'''
import pandas as pd #导入模块 pandas，定义别名 pd
import numpy as np
s=pd.Series([1,2,3,np.nan,5,6]) #列表生成 Series 对象
print(s) #索引在左边，值在右边
print(s[5])
s = pd.Series([9, 'zheng', 'beijing', 128, 'usa', 990], index=[1,2,3,'e','f','g']) #index 参数指定索引
print(s[3])

# 切片
print(s[1:-1]) # 数字索引
print(s['e':'g']) # 字符索引 (！！！包含了最后一个元素！！！)
print(s['e'])
# print(s[1:'g']) # 错误的引用！字符和数字索引不能混合使用
s = pd.Series([9, 'zheng', 'beijing', 128, 'usa', 990], index=['1','2','3','e','f','g']) #index 参数指定索引
print(s['1':'g'])
# 输入数据为字典类型
s = {"ton": 20, "mary": 18, "jack": 19, "car": None}
sa = pd.Series(s)
print(sa)  # 默认根据字典的键码字符串顺序排序
## 指定顺序
sa = pd.Series(s, index=['ton', 'mary', 'jack', 'car']) #指定顺序'ton', 'mary', 'jack', 'car'
print(sa)
# 通过 numpy 的 random.randn()随机数生成 Series 对象，
sa = pd.Series(np.random.randn(5))
## numpy 的 random.randn()和 random.rand()都是产生随机数的函数，前者产生的随机数服从正态分布，后者产生的随机样本服从[0,1)之间的均匀分布。

# Pandas数据框
data = {'id': ['Jack', 'Sarah', 'Mike'],
 'age': [18, 35, 20],
 'cash': [10.53, 500.7, 13.6]}
df = pd.DataFrame(data) #调用构造函数并将结果赋值给 df
print(df) # 默认根据字典的键码字符串顺序排序
## 指定顺序
df = pd.DataFrame(data,index=['id','age','cash'])
print(df)

df["rich"]=df["cash"]>200
print(df)
'''
      age    cash     id   rich
id     18   10.53   Jack  False
age    35  500.70  Sarah   True
cash   20   13.60   Mike  False
'''
## 指定列的顺序
df2=pd.DataFrame(data,columns=["id","age","cash"])
print(df2)
## 数据引用
### 引用列、切片、定位某个数据

print(df2["id"])
print(df2.iloc[0:1,0:2]) # 逗号左侧为行，右侧为列
# print(df2.iloc[0:1,'id':'id']) # 错误的用法
# print(df2.iloc[:,'id':'age'])
# ①iloc 主要使用数字来索引数据，而不能使用字符型的标签来索引数据。
# 而 loc 则刚好相反，只能使用字符型标签来索引数据，不能使用数字来索引数据。
# 注意：数字索引范围不包括结尾，而字符索引范围包括结尾。
print(df2.loc[:,'id':'id'])
#②ix 是一种混合索引，字符型标签和整型数据索引都可以。ix
print(df2.ix[0:0,'id':'id'])

# 数据清洗
# 部分处理见chapter7.p2_titanic.py
## 处理日期(字符转换为日期)
data={
  'Date':['2023/3/1','2022/1/1'],
   'age':[50,10]
}
df=pd.DataFrame(data,index=['day1','day2'])
print(df)
df['Date']=pd.to_datetime(df['Date'])
print(df)

## 处理重复值
person={
    "name":['google','runoob','runoob','taobao'],
    "age":['50','40','40','23']
}
df=pd.DataFrame(person)
print(df)
print(df.duplicated())
df.drop_duplicates(inplace=True)
print(df)


person={
    "name":['google','runoob','taobao','jd'],
    # "age":['50','40','233333']
    "age":[50,40,2333,125]
}
df=pd.DataFrame(person)
for x in df.index:
    # if int(df.loc[x,'age']) > 120:
    if df.loc[x, 'age'] > 120:
        ## 批量修改
        df.loc[x,'age']=120
        ## 删除错误数据行
        # df.drop(x,inplace= True)
print(df)
