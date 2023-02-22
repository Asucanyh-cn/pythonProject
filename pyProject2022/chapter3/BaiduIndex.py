'''
encoding:utf-8
author:yh
date:2022/4/19 20:01
'''
import requests
headers={'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML, likeGecko) Chrome/83.0.4103.106Safari/537.36'}
res=requests.get("https://www.baidu.com/",headers=headers)
res.encoding="utf-8"
print(res.status_code)
# print(res.text)

from lxml import  etree
selector=etree.HTML(res.text)

H_title=selector.xpath('//*[@id="hotsearch-content-wrapper"]/li/a/span[2]/text()')
print(H_title)

logo=selector.xpath('//*[@id="s_lg_img"]/@src')
print(logo)
logo_url='http:'+logo[0]
print(logo_url)
v=requests.get(logo_url)
with open('baidu_logo.jpg','wb') as f:
    f.write(v.content)
    print('图片已爬取')
