'''
encoding:utf-8
author:yh
date:2022/5/16 10:20
'''
import os, codecs
import jieba
from collections import Counter


def get_words(txt):
    seg_list = jieba.cut(txt)
    c = Counter()
    for x in seg_list:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1
    print('常用词频度统计结果')
    for (k, v) in c.most_common(5):
        # print('%s%s %s %d' % (' '*(5-len(k)), k, '*'*int(v/3), v))
        print('%s %d' % (k, v))


if __name__ == '__main__':
    with codecs.open('D:/spss kmeans/30.txt', 'r', 'utf8') as f:
        txt = f.read()
get_words(txt)
