'''
encoding:utf-8
author:yh
date:2023/4/3 9:59
'''
import nltk
# nltk.download() #安装方法之一
sen='I love python?'
token=nltk.word_tokenize(sen) #分词
print(token)

import re #正则表达式
list=re.sub("[^a-zA-Z]"," ",sen) # 去除标点符号
print(list)

list2=list.split()
print(list2)

sentence="What you say is very funny. And he is not a very nice person."
tokens=nltk.word_tokenize(sentence)
print(tokens)
list=re.sub("[^a-zA-Z]"," ",sentence) #去除标点符号
list_sen=list.split()
print(list_sen)
# 标注每个词的词性
tagged=nltk.pos_tag(tokens)
print(tagged)
# 词频统计
#1
fdist1 = nltk.FreqDist(tokens)
for key, val in fdist1.items():
    print(key, val)
#2 用两个列表，分别存放词和对应词频
list1=[]
list2=[]
for key,val in fdist1.items():
    list1.append(key)
    list2.append(val)
print(list1,list2)
