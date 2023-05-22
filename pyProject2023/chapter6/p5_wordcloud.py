'''
encoding:utf-8
author:yh
date:2023/4/14 16:05
'''
import re

# import jieba
# text = ''
# with open('./datafiles/news.txt') as fileIn:
#      for line in fileIn.readlines():
#          line = line.strip('\n') #去除换行符
#          text += ''.join(jieba.cut(line))
#          text += ''
# print("jieba = "+text)
#
# import re
# text=re.sub('[^\u4e00-\u9fa5]',' ',text)
# print("Only Chinese = "+text)
#
# import numpy as np
# from wordcloud import WordCloud, STOPWORDS
# from PIL import Image #图像处理库，若PIL导入报错，使用 pip install --upgrade pillow 更新图像界面库 pillow
# image = np.array(Image.open('./datafiles/timg.jpg')) #将图片转换为二维矩阵
# wc = WordCloud( background_color = 'white', #设置背景颜色
#     mask=image, #设置背景图片
#     max_words = 50, #设置最大现实的字数
#     stopwords = STOPWORDS, #设置停用词
#     font_path = 'C:/Windows/fonts/simsun.ttc', #设置字体格式，中文
#     max_font_size = 50, #设置字体最大值
#     random_state = 30, #设置随机生成状态，即配色方案
# )
# wc.generate(text)
#
# import matplotlib.pyplot as plt
# plt.imshow(wc)
# plt.axis('off') #off取消坐标显示，美化界面
# plt.show()

#英文的词云

import matplotlib.pyplot as plt
#利用wordcloud制作词云
from wordcloud import WordCloud, STOPWORDS
#将需要制作的文本打开
text = open('./datafiles/ironman.txt').read()
print(text)
#可以使用nltk对英文进行分词以及去除停用词
text=re.sub("[^a-zA-Z]"," ",text)
words=text.split()
# print(list)

from nltk.corpus import stopwords
stops = set(stopwords.words("english"))
list = [w for w in words if not w in stops]
for i in list:
    text+=i+" "
print(text)

from PIL import Image  #PIL 图像处理库
import numpy as np
image = np.array(Image.open('./datafiles/timg.jpg'))

wc = WordCloud(background_color="white",    #设置背景颜色
               mask=image,                     #设置背景图片
               max_words=50,                   #设置显示的最大词数
               stopwords=STOPWORDS,           #设置停用词
               max_font_size=100,             #设置字体最大值
               random_state=30                # 设置随机生成状态，即配色方案
              )
#产生词云
wc.generate(text)
plt.imshow(wc,interpolation='bilinear')     #双线插值，显示图形
plt.axis("off")
plt.show()