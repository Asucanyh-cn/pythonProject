import requests as rq
from lxml import etree
url='https://www.yhdmp.me/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'}
r=rq.get(url=url,headers=headers)
print(r.status_code,r)
r.encoding='utf-8'
selector=etree.HTML(r.text)

for i in range(7):
    weeklist=selector.xpath('/html/body/div[8]/div[2]/div[1]/div[2]/span/text()')[i]
    print(weeklist)
    animelist=selector.xpath('/html/body/div[8]/div[2]/div[1]/div[3]/ul')[i]
    print(animelist.xpath('li/a/text()'))