'''
encoding:utf-8
author:yh
date:2023/4/14 10:19
'''
import pandas as pd
#步骤
#
#导入数据  《保你平安》电影的豆瓣评论数据
data=pd.read_csv("./datafiles/douban.csv")

#删除未评论的行
data1=data.dropna()
data=data['comment']
data1=data1['comment']
# print(data)
# print(data1)

#写入评论数据
f=open("./datafiles/DoubanComment1.txt",'w',encoding='utf-8')
for comment in data1:
    f.write(str(comment)+'\n')
f.close()
#读取数据
def readTxt(path,encoding):
    data = []
    with open(path, encoding=encoding) as f:
        data = f.readlines()
    return data
#一.数据处理
#①去除指定无用的符号（1去除空格，2把省略号转换）
def process(content):     #定义函数
    content=content.replace(' ','').replace('...','。')  #去掉文本中的空格以及替换省略符号
    return content
#读取数据
data=readTxt("./datafiles/DoubanComment1.txt","utf-8")
#处理数据，写入新文件
f=open("./datafiles/DoubanComment2.txt",'w',encoding='utf-8')
for comment in data:
    f.write(process(comment))
f.close()
# ②让文本只保留汉字
def to_OnlyChinese(content):
    data=''
    for uchar in content:
        if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
            data=data+uchar
    return data + '\n' #使返回值保留换行符
#读取数据
data=readTxt("./datafiles/DoubanComment2.txt","utf-8")
# 写入新文件中
f=open("./datafiles/DoubanCommentOnlyChinese.txt",'w',encoding='utf-8')
for comment in data:
    f.write(to_OnlyChinese(comment))
f.close()

#③去除颜文字
#读取数据
data=readTxt("./datafiles/DoubanComment2.txt","utf-8")
# print(data)
import re
def clear_character(sentence):
    pattern = re.compile("[^\u4e00-\u9fa5^,^.^!^a-z^A-Z^0-9]")  # 只保留中英文、数字和符号，去掉其他东西
    # 若只保留中英文和数字，则替换为[^\u4e00-\u9fa5^a-z^A-Z^0-9]
    line = re.sub(pattern, '', sentence)  # 把文本中匹配到的字符替换成空字符
    new_sentence = ''.join(line.split())  # 去除空白
    return new_sentence+'\n'

with open("./datafiles/DoubanComment4.txt",'w',encoding="utf-8") as f:
    for comment in data:
        f.write(clear_character(comment))

#④繁体中文与简体中文转换
data=readTxt("./datafiles/DoubanComment4.txt","utf-8")
# print(data)
#安装 pip install openccpy
#OpenccPy。OpenccPy是一款 python 中文繁简体转换工具。
from opencc import OpenCC
def Simplified(sentence):
    new_sentence = OpenCC('t2s').convert(sentence)  # 繁体转为简体
    return new_sentence
def Traditional(sentence):
    new_sentence = OpenCC('s2t').convert(sentence)  # 简体转为繁体
    return new_sentence

with open("./datafiles/DoubanCommentSimplified.txt","w",encoding="utf-8") as f:
    for comment in data:
        f.write(Simplified(comment))
data=readTxt("./datafiles/DoubanCommentSimplified.txt","utf-8")
# print(data)

#二.使用jieba分词
import jieba
#读取数据
data=readTxt("./datafiles/DoubanCommentSimplified.txt","utf-8")
# print(data)
#对每行的评论进行分词
jiebaword = [] #用来存放所有分词
for comment in data:
    seg_list=jieba.cut(comment) #默认精确模式
    word="/".join(seg_list)
    jiebaword.append(word)
# print(jiebaword)
#三.去除停词
import jieba.analyse
#网友整理的停用词：https://gitcode.net/mirrors/goto456/stopwords?utm_source=csdn_github_accelerator
stopwords_filepath="./datafiles/cn_stopwords.txt"
jieba.analyse.set_stop_words(stopwords_filepath) #可以在stop_words.txt中设置额外的停用词
# 读取停用词
stopwords = [line.strip() for line in open(stopwords_filepath, 'r', encoding='utf-8').readlines()]
# stopwords.append() #添加额外的分词
stopwords.append('一个')
stopwords.append('一部')
stopwords.append('真的')

# 去停用词并保存结果到DoubanCommentClean.txt
with open("./datafiles/DoubanCommentClean.txt",'w',encoding="utf-8") as f:
    for words in jiebaword:
        words = words.split('/')
        for word in words:
            if word not in stopwords:
                f.write(word + '\t') #词之间用tab隔开
        f.write('\n')
#四.关键词提取
content = open('./datafiles/DoubanCommentClean.txt', 'rb').read() #以二进制形式读取文件
# tags = jieba.analyse.extract_tags(content, topK=10) #取 tfidf 权重前 10 的词
# print(','.join(tags))
tags = jieba.analyse.extract_tags(content, topK=10,withWeight=True)
# print(tags)
#①词频
#方法一，统计词频
import re
word_count = {} # 创建字典，用来存放词和其词频
word_all=[] #把所有的词放在一个列表中
for words in jiebaword:
    words=words.replace("\n","").split('/')
    for word in words:
        m = re.search("\d+", word) #匹配一个数字(0到9)
        n = re.search("\W+", word) #匹配一个或多个非字母进行切割，匹配到的非字母不缓存
        if word not in stopwords and not m and not n and word!="" and len(word)>1:
            word_all.append(word) #将每个词作为一个元素存入列表（用extend会导致词被拆开成单字）
# print(word_all)
for word in set(word_all):        #用set去除list中的重复项
    word_count[word]=word_all.count(word)
list_count = sorted(word_count.items(),key=lambda x:x[1],reverse=True)
for i in range(10):
    print(list_count[i])
#方法二，课本上的方法
listkey = []
listval = []
for word, val in sorted(tags, key=lambda x:x[1], reverse=True):
    listkey.append(word)
    listval.append(val)
    print(word, val)
#五.关键词可视化
# import matplotlib.pyplot as plt
# import numpy as np
# plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
# plt.bar(np.arange(10),listval,log=True)
# plt.xticks(np.arange(10),listkey,rotation=30)
# ax = plt.gca() #gca='get current axis'
# ax.set_ylabel('tfidf')
# plt.title('词频统计')
# plt.show()
#六.词云
#将清洗过的数据中，放在一个列表中
txt_list=readTxt('./datafiles/DoubanComment2.txt','utf-8')
text=""
for list in txt_list:
    text=text+list
    text=text.replace("\n","")
    # 处理一下停用词
print(text)
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
wc = WordCloud(
    background_color="yellow", #设置背景颜色
    max_words=50, #设置显示的最大词数
    stopwords=STOPWORDS, #设置停用词
    font_path = 'C:/Windows/fonts/simsun.ttc', #设置字体格式，中文
    max_font_size=100, #设置字体最大值
    random_state=30 #设置随机生成状态，即配色方案
)
wc.generate(text) #产生词云图
plt.imshow(wc) #显示词云图
plt.axis('off') #取消坐标，美化界面
plt.show()
#七.情感分析
'''
返回值为所分析评论的情绪为积极或消极的概率，其区间为[0,1]，
当分值大于0.5 时代表句子的情感极性偏向于积极，
当分值小于 0.5 时，情感极性偏向于消极。
'''
from snownlp import SnowNLP
txt_list=readTxt("./datafiles/DoubanCommentOnlyChinese.txt",'utf-8')
# print(txt_list)
# word_list=[]
# i=1
# for line in txt_list:
#     s=SnowNLP(line)
#     # print(s.words) #使用snownlp分词
#     # print(list(s.tags)) #词性标注
#     print(i,s.sentiments) #情感分析
#     i=i+1
#     word_list.extend(s.words)
# print(word_list)
with open("./datafiles/DoubanCommentScore.csv","w",encoding='utf-8') as f:
    f.write("id,score\n")
    i=1
    for line in txt_list:
        s = SnowNLP(line)
        f.write(str(i)+','+str(s.sentiments)+'\n')
        i=i+1
import pandas as pd
df=pd.read_csv("./datafiles/DoubanCommentScore.csv")
print(df.head())
def type_class(text):
    if text > 0.8:
        text = '优秀'
    elif text > 0.6:
        text=  '良好'
    elif text > 0.4:
        text = '一般'
    elif text > 0.2:
        text = '较差'
    else:
        text = "很差"
    return text
df['type'] = df['score'].apply(lambda x: type_class(x))
print(df.head(50))