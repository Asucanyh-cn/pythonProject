'''
encoding:utf-8
author:yh
date:2023/3/27 15:41
'''
import requests
from lxml import etree

# 爬取ppt模板的预览图，将介绍作为文件名
url='http://www.pptmall.net/tag/free/page/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43'}
n=3 #第n页
url=url+str(n)

html=requests.get(url,headers=headers)
html.encoding='utf-8'
# print(html.text)

selectors=etree.HTML(html.text)

title=selectors.xpath("//article/div/a/text()")
img=selectors.xpath("//article/a/img/@src")

k=0
for imageUrl in img:
    t=title[k].replace("/","_").replace(":","比") #替换介绍中的非法字符，避免图片文件名报错
    print('正在写入... %s.jpg' %t )

    image=requests.get(imageUrl)
    with open("ppt素材预览图/%s.jpg"%t,'wb') as f:
        f.write(image.content)
    k=k+1
f.close()
print('Done')