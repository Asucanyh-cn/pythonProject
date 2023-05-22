'''
encoding:utf-8
author:yh
date:2023/5/15 10:54
'''
'''
关联规则
'''
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

inputfile = 'menu_orders.xls'
data = pd.read_excel(inputfile, header=None)
print(data.head())

ct = lambda x: pd.Series(1, index=x[pd.notnull(x)])  # 转换 0-1 矩阵的过渡函数
b = map(ct, data.values)  # 用 map 方式执行矩阵转换
data = pd.DataFrame(list(b)).fillna(0)  # 实现矩阵转换，空值用 0 填充
print(data)

frequent_itemsets = apriori(data, min_support=0.2, use_colnames=True)
print(frequent_itemsets.head(5))

ct = lambda x: pd.Series(1, index=x[pd.notnull(x)])  # 转换 0-1 矩阵的过渡函数
b = map(ct, data.values)  # 用 map 方式执行矩阵转换
data = pd.DataFrame(list(b)).fillna(0)  # 实现矩阵转换，空值用 0 填充
print(data)

frequent_itemsets = apriori(data, min_support=0.2, use_colnames=True)
print(frequent_itemsets.head(5))

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)
print(rules)

print(rules.sort_values(by='confidence', axis=0, ascending=False).head(10))
