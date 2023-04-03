'''
encoding:utf-8
author:yh
date:2023/3/20 10:41
'''
import requests
from lxml import etree
import time

url = "http://www.xiyi.edu.cn/gzcylist.jsp"
# url="http://www.xiyi.edu.cn/gzcylist.jsp?totalpage=101&PAGENUM=1&urltype=tree.TreeTempUrl&wbtreeid=1172"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41'}
pagenum = 1

params = {
    "totalpage": 101,
    "PAGENUM": pagenum,  # 设置分页
    "urltype": "tree.TreeTempUrl",
    "wbtreeid": 1172
}
# html = requests.get(url, headers=headers)
html = requests.get(url, headers=headers, params=params)
html.encoding = "utf-8"
# print(html.text)

selectors = etree.HTML(html.text)

# 浏览器会对html文本进行一定的规范化，所以会自动在路径中加入tbody，导致读取失败，在此处直接在路径中去除tbody即可。　
# trackingCode = selectors.xpath("//*[@class='content']/table[1]/tr[2]/td[2]/text()")[0]
# title = selectors.xpath("//tr[2]/td[3]/a/text()")[0]
# submitTime = selectors.xpath("//tr[2]/td[4]/text()")[0]
# resolveTime = selectors.xpath("//tr[2]/td[5]/text()")[0]
# s = str(trackingCode) + ',' + str(title) + ',' + str(submitTime) + ',' + str(resolveTime)
# s = s.replace(" ", "").strip().replace("\n", "")
# print(s)

f = open("XiaoZhangXinXiang.csv", "a", encoding="utf-8")
f.write("查询码,标题,提交时间,处理状态\n")
i = 2
while True:
    try:
        trackingCode = selectors.xpath("//*[@class='content']/table[1]/tr[" + str(i) + "]/td[2]/text()")[0]
        title = selectors.xpath("//tr[" + str(i) + "]/td[3]/a/text()")[0]
        submitTime = selectors.xpath("//tr[" + str(i) + "]/td[4]/text()")[0]
        resolveTime = selectors.xpath("//tr[" + str(i) + "]/td[5]/text()")[0]
    except:
        break

    s = str(trackingCode) + ',' + str(title) + ',' + str(submitTime) + ',' + str(resolveTime)
    s = s.replace(" ", "").strip().replace("\n", "")
    print(i - 1, s)
    i += 1
    f.write(s + "\n")

f.close()
