'''
encoding:utf-8
author:yh
date:2022/4/18 19:30
'''
import requests
from lxml import etree
res=requests.get("https://www.huya.com/g/2752")
print(res.status_code)
html=etree.HTML(res.text)
pic_list=html.xpath("//img[@class='pic']")
print(pic_list)
####
for pic in pic_list:
    pic_src=pic.xpath("@data-original")[0]
    big_pic=big_src.split("?")[0]
