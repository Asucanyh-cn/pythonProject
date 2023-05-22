'''
encoding:utf-8
author:yh
date:2023/4/12 11:15
'''
from snownlp import SnowNLP
s=SnowNLP('这个东西很赞')
#分词
print(s.words)
print(list(s.tags)) #词性标注
print(s.sentiments) #情感分析

text='''
自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。
它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。
自然语言处理是一门融语言学、计算机科学、数学于一体的科学。
因此，这一领域的研究将涉及自然语言，即人们日常使用的语言，
所以它与语言学的研究有着密切的联系，但又有重要的区别。
自然语言处理并不是一般地研究自然语言，
而在于研制能有效地实现自然语言通信的计算机系统，
特别是其中的软件系统。因而它是计算机科学的一部分。
'''
s=SnowNLP(text)
print(s.keywords(5)) #提取关键词
print(s.sentences)
for i in s.sentences:
    print(i)
print(s.summary())
s=SnowNLP([['这篇','文章'],['那篇','论文'],['文章'],['文章','这篇','这篇']])
print(s.tf) #词频
print(s.idf)
print(s.sim(['那篇']))

import pandas as pd
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel("./datafiles/mtpl.xls", 'Sheet1')
print(df.head())

df['score'] = df['评论'].apply(lambda x: SnowNLP(x).sentiments)
print(df.head())

def type_class(text):
    if text > 0.5:
        text = '好评'
    elif text > 0.2:
        text = '中评'
    else:
        text = "差评"
    return text
df['type'] = df['score'].apply(lambda x: type_class(x))
print(df.head())

text = ''
for line in df['评论']:
    line = line.strip() # 去除首位空格换行符
    text += line
print(text)
s=SnowNLP(text)
print(s.keywords(20))

# def handle(self, doc): #在 sentiment 中
#     words = seg.seg(doc) #seg 是 snownlp 的分词方法
#     words = normal.filter_stop(words) #过滤停用词
#     return words
# from snownlp import sentiment
# sent = sentiment.Sentiment()
# words_list=sentiment.Sentiment.handle(sent,text)
# text=' '.join(words_list)
# s=SnowNLP(text)
# print(s.keywords(20))

