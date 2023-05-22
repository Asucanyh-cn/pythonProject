'''
encoding:utf-8
author:yh
date:2023/4/19 15:49
'''

'''
开始文本分析
1.文本数据预处理
  1.1 缺失值处理
  1.2 重复值处理（无重复值，跳过）
  1.3 文本内容清洗
  1.4 分词
  1.5 停用词处理
2.数据可视化分析
  2.1 数量分布
  2.2 词汇统计
  2.3 关键词可视化
3.主题挖掘
4.情感分析
'''
'''
读取数据
'''
import pandas as pd

data = pd.read_csv("./datafiles/PeopleOpinionTextData.csv", encoding='utf-8')
# print(data['内容'])
'''
1.1  缺失值处理
目标：去除空数据
'''
from FunctionUtils import findNotStr  # 用于查找所有非字符串的自定义函数

data['内容（findNotStr）'] = data['内容'].apply(findNotStr)
# print(data['内容（findNotStr）'].value_counts())  # 查看有多少非字符串数据 （即空数据 0表示空）
data = data.dropna()
# print(data[data['内容（findNotStr）']==0])
data_1_1 = data  # 将这一步的数据存个档
'''
1.3 文本内容清洗
目标：去除文本中存在对分析作用不大的标点符号与特殊字符
函数：washText()
'''
from FunctionUtils import washText

data['内容'] = data['内容'].apply(washText)
# print(data.head())
'''
1.4 分词
目标：使用jieba，将连续的文本，分割成语意合理的若干词汇序列
'''
import jieba

data['内容（分词后）'] = data['内容'].apply(jieba.cut)
# print(data['内容（分词后）'].head())
'''
1.5 停用词处理
目标：去除对对语义分析没有帮助的词。
方法：使用stopwords.txt设置的一些停用词，增加分析的准确性。自定义函数removeStopWords()
stopwords.txt：https://gitcode.net/mirrors/goto456/stopwords?utm_source=csdn_github_accelerator
'''
# from FunctionUtils import removeStopWords
#
# stopWordsFilePath = './datafiles/cn_stopwords.txt'
# others = ['更', '新', '党', '中']  # 根据后面的词频统计，发现了几个单字的频率高，将其设为停用词
# data['内容（分词后）'] = data['内容（分词后）'].apply(removeStopWords, args=(stopWordsFilePath, others,))
# print(data['内容（分词后）'].head())
'''
2.1 数量分布
目标：按年、月、日统计文章数量
方法：首先使用datatime处理一下日期格式，自定义函数removeHMS()去掉时分秒。
'''
# from datetime import datetime
# from FunctionUtils import removeHMS
#
# data['时间'] = data['时间'].apply(datetime.strptime, args=('%Y年%m月%d日%H:%M',))
# data['时间'] = data['时间'].apply(removeHMS, args=('%Y-%m-%d',))
# data['时间'] = data['时间'].apply(str)
#
# print(data['时间'].head())
#
# time_df = data['时间'].str.split('-', expand=True)
#
# print(time_df.head())
# print(time_df[0].value_counts().head())
# print(time_df[1].value_counts().head())
# print(time_df[2].value_counts().head())
#
# import matplotlib.pyplot as plt
#
# fig=plt.figure(figsize=(20,20))
# plt.rcParams['font.sans-serif']=['SimHei']# 正确显示汉字
# plt.rcParams['axes.unicode_minus']=False # 正确显示负号
#
# ax1=fig.add_subplot(1,3,1)
# plt.title("每年文章数")
# plt.xlabel("年份")
# plt.ylabel("文章数")
# time_df[0].value_counts().sort_index().plot(kind='bar')
#
# ax2=fig.add_subplot(1,3,2)
# plt.title("2022年每月文章数")
# plt.xlabel("月份")
# plt.ylabel("文章数")
# (time_df[time_df[0]=='2022'][1]).value_counts().sort_index().plot(kind='bar')
#
#
# ax3=fig.add_subplot(1,3,3)
# plt.title("2023年每月文章数")
# plt.xlabel("月份")
# plt.ylabel("文章数")
# (time_df[time_df[0]=='2023'][1]).value_counts().sort_index().plot(kind='bar')
# # plt.show()
#
# fig=plt.figure(figsize=(20,20))
#
# ax4=fig.add_subplot(1,2,1)
# plt.title("2022年每日文章数")
# plt.xlabel("日")
# plt.ylabel("文章数")
# (time_df[time_df[0]=='2022'][2]).value_counts().sort_index().plot(kind='bar')
#
#
# ax5=fig.add_subplot(1,2,2)
# plt.title("2023年每日文章数")
# plt.xlabel("日")
# plt.ylabel("文章数")
# (time_df[time_df[0]=='2023'][2]).value_counts().sort_index().plot(kind='bar')
# plt.show()

'''
2.2 词汇统计
目标：统计在所有文章中出现频数最多的n个词汇
方法：首先，将所有的分词放入同一个列表中，再使用自定义函数countWordFrequency()，
     第一个参数为列表，第二个参数为取前n（默认去全部），返回值为列表。
'''
# from FunctionUtils import countWordFrequency
#
# allWordlist = []  # 存放所有分词的列表
# n = 10
# for list in data['内容（分词后）']:
#     allWordlist += list
# resList = countWordFrequency(allWordlist, n)
# for word, freq in resList:
#     print(word, freq)

'''
2.3 关键词可视化
目的：①将出现最多的n个词汇的频数、频率做条形图。
'''
# wordList = []
# freqList = []
# for word, freq in resList:
#     wordList.append(word)
#     freqList.append(freq)
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.bar(np.arange(n), freqList, log=True)
# plt.xticks(np.arange(n), wordList, rotation=30)
# ax = plt.gca()  # gca='get current axis'
# ax.set_ylabel('词频')
# plt.title('词频统计')
# plt.show()
'''
2.4 生成词云图
目标：首先将所有分词连成一个文本,词间用空格分开，使用wordcloud生成词云图。
'''
# import numpy as np
# from PIL import Image
#
# text=''
# for word in allWordlist:
#     text+=word+" "
# print(text)
#
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, STOPWORDS
# image = np.array(Image.open('./datafiles/timg.jpg'))
# wc = WordCloud(
#     mask=image,
#     background_color="white", #设置背景颜色
#     max_words=50, #设置显示的最大词数
#     stopwords=STOPWORDS, #设置停用词
#     font_path = 'C:/Windows/fonts/simsun.ttc', #设置字体格式，中文
#     max_font_size=100, #设置字体最大值
#     random_state=30 #设置随机生成状态，即配色方案
# )
# wc.generate(text) #产生词云图
# plt.imshow(wc,interpolation='bilinear') #双线插值，显示图形
# plt.axis('off') #取消坐标，美化界面
# plt.show()
'''
3. 主题分析
'''
from gensim import corpora, models

# # 构建词典
# allWordlistByArticle = []
# for list in data['内容（分词后）']:
#     allWordlistByArticle.append(list)
# texts = allWordlistByArticle
# dictionary = corpora.Dictionary(texts)
# # 构建语料库
# corpus = [dictionary.doc2bow(text) for text in texts]
# # 训练LDA模型
# lda_model = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=3, passes=50)
# # 输出主题词
# for i, topic in lda_model.print_topics(num_topics=3, num_words=10):
#     print('Topic {}: {}'.format(i, topic))

'''
4.情感分析
'''
from snownlp import SnowNLP
# 输出情感分析结果，创建新的一列
data['score']=data['内容'].apply(lambda c:SnowNLP(c).sentiments)
print("积极 ",(data['score']>0.4).sum())
print("消极 ",(data['score']<=0.4).sum())
print(data[data['score']<=0.4])