'''
encoding:utf-8
author:yh
date:2023/4/19 13:16
'''
import re

import requests
from lxml import etree


def getUrlList(n, m=-1):
    # n=4
    # 用于存储所有文章的链接列表
    list = []
    # 存放返回结果
    res = []
    for i in range(n):
        href = 'http://opinion.people.com.cn/GB/223228/index' + str(i + 1) + '.html'
        # href='http://opinion.people.com.cn/GB/223228/index2.html' #第二页
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41'}
        html = requests.get(href, headers=headers)
        html.encoding = "utf-8"
        # print(html.text)
        selectors = etree.HTML(html.text)

        # 获取所有文章链接
        raw_hrefs = selectors.xpath('/html/body/div[6]/div[1]/div/ul/li/a/@href')
        # print(raw_hrefs)
        # 处理文章链接
        for href in raw_hrefs:
            href = "http://opinion.people.com.cn" + href
            # print(href)
            # 存入列表中
            list.append(href)
    # print(list)
    if m > len(list) or m == -1:
        m = len(list)
    for i in range(m):
        res.append(list[i])
    return res


def getCleanList(raw_list):
    res = []
    for item in raw_list:
        item = item.replace("\n", "").replace("\t", "").replace(" ", "").strip()
        res.append(item)
    return res


def list2String(list):
    res = ''
    for i in list:
        res += i
    return res


def washText(text):
    return re.sub('[^\u4e00-\u9fa5a-zA-Z0-9]', '', text)


'''
第一个参数为需要传入的字符串
第二个参数为停用词文件路径
'''

def removeStopWords(cuttedWords, stopWordsFilePath, others=[]):
    stopwords = [line.strip() for line in open(stopWordsFilePath, 'r', encoding='utf-8').readlines()]
    stopwords.extend(others)  # 设置额外的停用词
    return [word for word in cuttedWords if word not in stopwords]


def findNotStr(x):
    if isinstance(x, str):
        return 1
    else:
        return 0


from datetime import datetime


def removeHMS(dataTime, pattern):
    return dataTime.strftime(pattern)


def countWordFrequency(wordList, top=-1):
    result = []
    word_count = {}
    for word in set(wordList):  # 用set去除list中的重复项
        word_count[word] = wordList.count(word)
    sortedFrequencyList = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    if top == -1 or top > len(word_count):
        top = len(word_count)
    for i in range(top):
        result.append(sortedFrequencyList[i])
    return result
