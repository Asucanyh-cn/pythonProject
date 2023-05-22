'''
encoding:utf-8
author:yh
date:2023/3/1 11:01
'''
import pandas as pd
df = pd.read_csv('datafiles/titanic.csv')
print(df.head().to_string())
# print(df.describe().to_string())
# print(df.describe(include='all').to_string())
## 删除空值的行
print(df['age'])
print(df['age'].isnull())
new_df=df.dropna(subset=['age'])
print(new_df.describe().to_string())
print(new_df['age'].isnull().head())
## 将NaN值替换成均值
x=round(df['age'].mean(),2)
print(x)
df['age'].fillna(x,inplace=True)
print(df.head().to_string())