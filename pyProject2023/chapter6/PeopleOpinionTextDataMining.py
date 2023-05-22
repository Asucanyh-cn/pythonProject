'''
encoding:utf-8
author:yh
date:2023/4/19 11:25
'''
from lxml import etree
import requests


# 定义一个获取所有链接，返回一个列表的函数
# 第一个参数，设置爬取页数
# 第二个参数，设置爬取返回条数，默认全部
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


urlList = getUrlList(4, 1)
print(urlList)
# 开始爬取文本
# 计划使用数据框存储文本等相关数据
# import pandas as pd

for url in urlList:
    url = url
    header = headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41'}
    html=requests.get(url,headers=headers)
    html.encoding='gbk'

    selectors=etree.HTML(html.text)
    title=selectors.xpath('/html/body/div[1]/div[7]/div[1]/h1/text()')
    content=selectors.xpath('/html/body/div[1]/div[7]/div[1]/div[3]/p/text()')
    date=selectors.xpath('/html/body/div[1]/div[7]/div[1]/div[2]/div[1]/text()')
    print(title)
    print(content)
    print(date)
    #对数据进行初步清洗