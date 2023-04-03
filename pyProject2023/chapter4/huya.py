'''
encoding:utf-8
author:yh
date:2023/3/27 10:00
'''
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
print(len(pic_list))
####
for pic in pic_list:
    pic_src=pic.xpath("@data-original")[0]
    # print(pic_src)
    big_pic=pic_src.split("?")[0] #以问号为分隔符分为两个部分，取左边的部分
    # print(big_pic)

    urlR=big_pic.split("//")[1]
    urlL="https://"
    url=urlL+urlR

    name=pic.xpath("@alt")[0]
    image=requests.get(url)
    image.encoding="utf-8"
    # print(url)
    with open("HuyaPictures/%s.jpg"%name,"wb") as f:
        f.write(image.content)
    print("[图片]%s"%name+".jpg 保存成功")
