import requests
import requests as rq
from lxml import etree

url='https://www.baidu.com'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41'}
html=rq.get(url,headers=headers)
html.encoding='utf-8'
# print(html.text)
selectors=etree.HTML(html.text)
img=selectors.xpath('//*[@id="s_lg_img_new"]/@src')
img_url='https:'+str(img[0])
print(img_url)
img_rq=rq.get(img_url)
with open('baidu_logo.png','wb') as f:
    f.write(img_rq.content)