'''
encoding:utf-8
author:yh
date:2023/4/19 10:57
'''
# import pandas as pd
# x = pd.read_csv('./datafiles/doubanpd.csv', encoding="gbk")
# print(x.head(10))
# newpage = x.dropna(axis=0)
# print(newpage.head(10))
#
# import jieba
# import jieba.analyse
# num_reviews = newpage["reviews"].size
# print(num_reviews)
#
# textreview=''
# for i in newpage["id"]:
#     textreview += newpage["reviews"][i]
#     textreview += ' '
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, STOPWORDS
# wc = WordCloud( background_color = 'white', # 设置背景颜色
#     max_words = 50, # 设置最大现实的字数
#     stopwords = STOPWORDS, # 设置停用词
#     font_path = 'C:/Windows/fonts/simsun.ttc', #设置字体格式，中文
#     max_font_size = 50, # 设置字体最大值
#     random_state = 30, # 设置随机生成状态，即配色方案
#  )
# wc.generate(textreview)
# #利用 matplotlib 库绘制词云
# import matplotlib.pyplot as plt
# plt.imshow(wc)
# plt.axis('off')
# plt.show()
#
# tags = jieba.analyse.extract_tags(textreview,topK=20,withWeight=True)
# print(tags)
#
# listkey = []
# listval = []
# for word, val in sorted(tags, key=lambda x:x[1], reverse=True):
#     listkey.append(word)
#     listval.append(val)
#     print(word, val)
# import numpy as np
# plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
# plt.bar(np.arange(20),listval,log=True)
# plt.xticks(np.arange(20),listkey,rotation=90)
# ax = plt.gca() #gca='get current axis'
# ax.set_ylabel('tfidf')
# plt.title('词频统计')
# plt.show()
#
# documents = newpage['reviews'].values.tolist()
# #print(documents)
# from nltk.tokenize import word_tokenize
# texts_tokenized = []
# for document in documents:
#     texts_tokenized_unit = []
# for word in word_tokenize(document):
#     texts_tokenized_unit += jieba.analyse.extract_tags(word, 5)
#     texts_tokenized.append(texts_tokenized_unit)
# print(texts_tokenized)
#
# #使用前需要导入 gensim 库
# #适合本环境的是 2.3 版本，命令：pip install genism==2.3 --no-deps
# import gensim
# #从 gensim 导入语料库
# from gensim import corpora
# #建立语料库中词的字典，每个唯一的词作为索引
# dictionary = corpora.Dictionary(texts_tokenized)
# #将语料库转换成文档词矩阵
# doc_term_matrix = [dictionary.doc2bow(doc) for doc in texts_tokenized]
# Lda = gensim.models.ldamodel.LdaModel
# ldamodel = Lda(doc_term_matrix, num_topics=6, id2word = dictionary, passes=50)
# print(ldamodel.print_topics(num_topics=3, num_words=10))


'''
LDA主题分析
'''
# import feedparser
#
# # 获取新闻RSS源
# rss_feeds = [
#     'http://news.baidu.com/n?cmd=1&class=civilnews&tn=rss',
#     'http://news.baidu.com/n?cmd=1&class=internews&tn=rss',
#     'http://news.baidu.com/n?cmd=1&class=finannews&tn=rss',
#     'http://news.baidu.com/n?cmd=1&class=shizheng&tn=rss',
#     'http://news.baidu.com/n?cmd=1&class=technews&tn=rss',
#     'http://news.baidu.com/n?cmd=1&class=sportnews&tn=rss',
#     'http://news.baidu.com/n?cmd=1&class=games&tn=rss',
#     'http://news.baidu.com/n?cmd=1&class=healthnews&tn=rss',
#     'http://news.baidu.com/n?cmd=1&class=socianews&tn=rss',
#     'http://news.baidu.com/n?cmd=1&class=envinews&tn=rss'
# ]
#
# # 获取新闻内容
# news_data = []
# for rss_feed in rss_feeds:
#     feed = feedparser.parse(rss_feed)
#     for entry in feed.entries:
#         news_data.append(entry.title + ' ' + entry.description)
#
# import jieba
# import re
# from collections import Counter
#
# # 加载停用词
# stopwords = []
# with open('./datafiles/stop_words.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         stopwords.append(line.strip())
#
# # 分词和预处理
# def preprocess(text):
#     # 去除标点符号和特殊字符
#     text = re.sub(r'[^\w\s]', '', text)
#     # 分词
#     words = jieba.cut(text)
#     # 去除停用词和低频词
#     words = [word for word in words if word not in stopwords and len(word) > 1]
#     word_counts = Counter(words)
#     words = [word for word in words if word_counts[word] > 1]
#     return words
#
# # 对新闻文本进行分词和预处理
# news_data_processed = []
# for news in news_data:
#     words = preprocess(news)
#     news_data_processed.append(words)
#
# from gensim import corpora, models
#
# # 构建词典
# dictionary = corpora.Dictionary(news_data_processed)
#
# # 构建文档-词频矩阵
# corpus = [dictionary.doc2bow(words) for words in news_data_processed]
#
# # 训练LDA模型
# lda_model = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=10, passes=10)
#
# # 输出每个主题的关键词
# for topic in lda_model.print_topics(num_topics=10, num_words=10):
#     print(topic)
#
# import pyLDAvis.gensim_models as gensimvis
# import pyLDAvis
#
# # 可视化LDA模型
# vis = gensimvis.prepare(lda_model, corpus, dictionary)
# pyLDAvis.display(vis)

'''
简单的案例
'''
import jieba
import pandas as pd
from gensim import corpora, models

# 创建测试用的新闻文本数据
news = pd.DataFrame({
    'title': ['中国队获得世界杯冠军', '美国总统访问中国', '中国发射卫星进入太空', '中国经济增长超过预期'],
    'content': ['中国队在世界杯足球赛中获得冠军，成为全球瞩目的焦点。',
                '美国总统访问中国，双方就贸易、安全等问题进行了磋商。',
                '中国成功发射一颗卫星进入太空，标志着中国航天事业又迈上了新的台阶。',
                '中国经济增长超过预期，为全球经济发展注入了新的动力。']
})

# 分词
news['content'] = news['content'].apply(lambda x: ' '.join(jieba.cut(x)))

# 构建词典
texts = [text.split() for text in news['content']]
print(texts)
dictionary = corpora.Dictionary(texts)

# 构建语料库
corpus = [dictionary.doc2bow(text) for text in texts]

# 训练LDA模型
lda_model = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=2, passes=10)

# 输出主题词
for topic in lda_model.print_topics(num_topics=2, num_words=3):
    print(topic)