'''
encoding:utf-8
author:yh
date:2023/2/15 10:33
'''

import jieba
# s="我是中国人"
# list=jieba.cut(s)
# print(','.join(list))

seg_list1= jieba.cut("我是一名中国的大学生",cut_all=True)
seg_list2= jieba.cut("我是一名中国的大学生",cut_all=True,HMM=True)
print(u"全模式："+"/ ".join(seg_list1))
print(u"全模式 -HMM："+"/ ".join(seg_list2))