'''
encoding:utf-8
author:yh
date:2023/4/3 10:58
'''
import re
import pandas as pd
train = pd.read_csv("datafiles\movieReviews.tsv", header=0, delimiter='\t', quoting=3)
print(train.head(), type(train))

print(train.shape)  # 查看 train 数据的维度大小
print(train.columns.values)  # 查看三个特征
print(train["review"][0])  # 查看第一条评论数据
# 文本预处理
# Anaconda 自带 BeautifulSoup4，导入即可使用，通过 html.parser 对文本进行 HTML 解析
# 利用 BeautifulSoup 的 get_text()方法，获取解析对象的内容。
# 1. 去除文本中的html标签
# 2. 去除文本中的字符
# 3. 将大写字母转换为小写字母
# 4. 分词
# 5. 去除停用词，获得有意义的词
# 6. 将有意义的词拼接成文本
from bs4 import BeautifulSoup

example1 = BeautifulSoup(train["review"][0], "html.parser")  # 1. 去除文本中的html标签
print(example1.get_text())
print("——" * 50)
letter_only = re.sub("[^a-zA-Z]", " ", example1.get_text())  # 2. 去除文本中的字符
print(letter_only)
print("——" * 50)
lower_case = letter_only.lower()  # 3. 将大写字母转换为小写字母
print(lower_case)
print("——" * 50)
words = lower_case.split()  # 4. 分词
print(words)
print("——" * 50)
from nltk.corpus import stopwords

print(stopwords.words("english"))  # 查看停用词
print("——" * 50)
stops = stopwords.words("english")
meaningful_words = [w for w in words if not w in stops]  # 5. 去除停用词
print(meaningful_words)
print("——" * 50)


# 使用函数来实现所有评论的处理
def review_to_words(raw_review):
    # 1.去 HTML 标签
    review_text = BeautifulSoup(raw_review, 'html.parser').get_text()
    # 2.去非字母符号
    letters_only = re.sub("[^a-zA-Z]", " ", review_text)
    # 3.分词并小写化
    words = letters_only.lower().split()
    # 4.去停止词
    stops = set(stopwords.words("english"))
    meaningful_words = [w for w in words if not w in stops]
    # 5.将有意义的词拼接成文本
    return (" ".join(meaningful_words))

clean_review = review_to_words(train["review"][1])
print(clean_review)
