'''
encoding:utf-8
author:yh
date:2023/5/3 16:08
'''
import pandas as pd
import numpy as np

raw=pd.read_csv("fatal-police-shootings-data.csv")
# print(raw.head())

print(raw.describe())

'''
threat_type 威胁类型
shoot           枪击 
threat          威胁
point           武器指向
attack          攻击
move             移动
undetermined     未定义
flee             逃亡
accident          事故
无序的分类变量
'''
print(raw['threat_type'].value_counts())
'''
flee_status 逃亡状态
not      无
car      开车
foot     步行
other     其它
无序的分类变量
'''
print(raw['flee_status'].value_counts())
'''
armed_with 装备
gun                          4873
knife                        1428
unarmed                       493
undetermined                  318
vehicle                       299
replica                       282
blunt_object                  207
unknown                       134
other                          86
gun;vehicle                    37
gun;knife                      34
vehicle;gun                    15
other;gun                       3
knife;vehicle                   3
blunt_object;knife              2
knife;blunt_object              2
blunt_object;blunt_object       2
replica;knife                   1
other;blunt_object;knife        1
vehicle;knife;other             1
replica;vehicle                 1
无序的分类变量
'''
print(raw['armed_with'].value_counts())
'''
location_precision
not_available    7145
block             165
address           100
intersection       85
poi_large           7
road                6  
poi_small           3
'''
print(raw['location_precision'].value_counts())

'''
gender
male          8017
female         369
无序的分类变量
'''
print(raw['gender'].value_counts())
'''
race
W      白
B      黑
H      西班牙裔
A       亚洲血统
N       美洲原住民
O        其他
B;H       1
选项：
- ： 白色
- ： 黑色
- ： 亚洲血统
- ： 美洲原住民
- ： 西班牙裔
- ： 其他

- ： 未知WBANHO--
'''
print(raw['race'].value_counts())
'''
was_mental_illness_related
False    6685
True     1747
'''
print(raw['was_mental_illness_related'].value_counts())
'''
body_camera
False    7190
True     1242
'''
print(raw['body_camera'].value_counts())
'''
agency_ids
'''
# print(raw['agency_ids'].value_counts())

'''
使用独热编码处理所需要的无序分类变量
threat_type
flee_status
armed_with
gender
race
was_mental_illness_related
body_camera
有序变量
age
date
'''
columns=['threat_type','flee_status','armed_with','gender','race','was_mental_illness_related','body_camera']
data_dum = pd.get_dummies(raw, prefix=columns, columns=columns, drop_first=True)
print(data_dum.head())
'''
生成新的csv文件
取500条就行了，太多了spss运行太慢
'''
data_dum.replace("",np.nan,inplace=True)
data_dum=data_dum.dropna(axis=0, how='any')
data_dum=data_dum.tail(500)
data_dum.to_csv("fatal-police-shootings-onehot.csv",index=False,sep=',')

'''
青少年：12岁至17岁之间的年轻人，正在上初中或高中，或没有完成高中学业。
大学生或年轻人：18岁至24岁之间的年轻人，正在大学就读或已经毕业。
中年人：25岁至64岁之间的中年人。
老年人：65岁及以上的人。
'''


bins=[0, 12, 18, 25,65,120]
data_dum['age_group'] = pd.cut(data_dum['age'], bins)
raw['age_group']= pd.cut(raw['age'], bins)

raw.replace("",np.nan,inplace=True)
raw=raw.dropna(axis=0, how='any')
raw=raw.tail(500)
raw.to_csv("fatal-police-shootings.csv",index=False,sep=',')
data_dum.to_csv("fatal-police-shootings-onehot.csv",index=False,sep=',')
