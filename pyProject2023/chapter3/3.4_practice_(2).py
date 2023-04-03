'''
encoding:utf-8
author:yh
date:2023/2/27 10:47
'''
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('titanic.csv')
print("——" * 50)
print("前5行数据\n" + titanic.head().to_string())
print("——" * 50)
desc = titanic.describe(include='all').round(1).to_string()
print("描述性统计\n" + desc)
print("——" * 50)
# 使用pandas进行数据清洗
print("将age列的NaN值替换成均值\n")
x = round(titanic['age'].mean(), 2)
titanic['age'].fillna(x, inplace=True)
print(titanic.head().to_string())

print("——" * 50)
print("age、fare最大最小值差异大，可绘制箱线图\n")

# print(titanic['age'].dropna())
# print(titanic['fare'].dropna())
fig = plt.figure(figsize=(10, 5))

# age = []
# age.append(titanic['age'].dropna())
# print(age)
# print(titanic['age'].dropna())
ax1 = fig.add_subplot(1, 2, 1)
plt.boxplot(titanic['age'].dropna().reset_index(drop=True))
plt.xticks(range(1, 2), ['age'])

ax2 = fig.add_subplot(1, 2, 2)
plt.boxplot(titanic['fare'].dropna().reset_index(drop=True))
plt.xticks(range(1, 2), ['fare'])

# plt.show()
print("——" * 50)
print("分类汇总：按性别对幸存人数汇总\n")
print("查看各状态的元素个数\n")
print(titanic.groupby(['sex','survived']).size().to_string())
print("分组以后，汇总计算的若干组数据\n")
print(titanic.groupby(['sex','survived']).count().to_string())
print("——" * 50)
print("对仓位（pclass）进行聚合计算")
print(titanic.groupby("pclass").aggregate("count").to_string())
print("——" * 50)
print("筛选登船地点、家乡")
print(titanic.filter(items=['embarked','home.dest']).head(20).to_string())
print("——" * 50)

