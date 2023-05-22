'''
encoding:utf-8
author:yh
date:2023/4/19 11:25
'''
from lxml import etree
import requests
# 定义一个获取所有链接，返回一个列表的函数getUrlList()
# 第一个参数，设置爬取页数
# 第二个参数，设置爬取返回条数，默认全部
from FunctionUtils import getUrlList
urlList = getUrlList(4,-1)
# print(urlList)
# 开始爬取文本，并存入csv文件
with open('./datafiles/PeopleOpinionTextData.csv', 'w', encoding='utf-8') as f:
    f.write("标题,时间,内容\n")
for url in urlList:
    url = url
    header = headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41'}
    html = requests.get(url, headers=headers)
    html.encoding = 'gbk'

    selectors = etree.HTML(html.text)
    raw_title = selectors.xpath('/html/body/div[1]/div[7]/div[1]/h1/text()')
    raw_content = selectors.xpath('/html/body/div[1]/div[7]/div[1]/div[3]/p/text()')
    raw_date = selectors.xpath('/html/body/div[1]/div[7]/div[1]/div[2]/div[1]/text()')

    # print(raw_title)
    # print(raw_content)
    # print(raw_date)

    # 对数据进行初步清洗
    # ①去除换行符、制表符，空格：定义一个函数getCleanList()
    from FunctionUtils import getCleanList
    import re

    title, content, date = [], [], []
    title = getCleanList(raw_title)
    content = getCleanList(raw_content)
    date = getCleanList(raw_date)

    # print(title)
    # print(content)
    # print(date)
    # print("——" * 50)

    # ②将列表转换为纯字符串结构：定义一个函数list2String()
    from FunctionUtils import list2String

    # 人民网评：实施人才托举，丰满科普之翼
    # 用正则匹配处理标题，去掉"人民网："
    title = re.sub('人民网评：', '', list2String(title)).replace(",","，") #加上replace是因为发现有一篇文章的标题，错误的使用了英文逗号
    content = list2String(content)
    # 2023年04月19日11:01 | 来源：
    # 用正则匹配去除 “|”和其之后的内容
    date = re.sub('\|.*', '', list2String(date))

    # print(title)
    # print(content)
    # print(date)
    # 写入csv文件
    with open('./datafiles/PeopleOpinionTextData.csv', 'a', encoding='utf-8') as f:
        print("写入文章："+title+"......"+"完成")
        f.write(title + "," + date + "," + content + "\n")
print("共计"+str(len(urlList))+"条")
print("Done")