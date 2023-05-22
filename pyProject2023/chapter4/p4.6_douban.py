'''
encoding:utf-8
author:yh
date:2023/3/16 11:28
'''
import csv

import requests
from lxml import etree


url='https://movie.douban.com/subject/35457272/comments?status=P'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43'}


# html=requests.get(url,headers=headers)
# html.encoding='utf-8'
# # print(html.url)
# # print(html.text)
# selector=etree.HTML(html.text)



# pages=int(input("输入需要爬取的评论数："))
totals=120
url= url+'&limit='+str(totals)
print(url)

htm=requests.get(url,headers=headers)
htm.encodings='utf-8'
selector=etree.HTML(htm.text)

f=open('douban.csv', 'w', encoding='utf-8',newline='')
f.write('name,status,comment,rate,zan\n')
# f.write('status,comment,rate,zan\n')
# writer = csv.DictWriter(f, fieldnames=['name','status','comments','rate','zan'])
# writer.writeheader()


for i in range(totals):
    num=str(i+1)
    try:
        name=selector.xpath('//*[@id="comments"]/div['+num+']/div[2]/h3/span[2]/a/text()')[0]
        status=selector.xpath('//*[@id="comments"]/div['+num+']/div[2]/h3/span[2]/span[1]/text()')[0]
        comments=selector.xpath('//*[@id="comments"]/div['+num+']/div[2]/p/span/text()')[0]
        rate=selector.xpath('//*[@id="comments"]/div['+num+']/div[2]/h3/span[2]/span[2]/@title')[0]
        zan=selector.xpath('//*[@id="comments"]/div['+num+']/div[2]/h3/span[1]/span/text()')[0]
    except:
        print('[Warning]写入行('+num+')失败！')
        continue
    # s=str(name)+','+str(status)+','+str(comments)+','+str(rate)+','+str(zan)+'\n'
    temp={
        'name':name.replace(" ","").replace(",","，").replace('"',"“").replace("\n",""),
        'status':status.replace(" ","").replace(",","，").replace('"',"“").replace("\n",""),
        'comments':comments.replace(" ","").replace(",","，").replace('"',"“").replace("\n",""),
        'rate':rate.replace(" ","").replace(",","，").replace('"',"“").replace("\n",""),
        'zan':zan.replace(" ","").replace(",","，").replace('"',"“").replace("\n",""),
    }

    print('[Info]正在写入行...('+num+')')
    # f.write(s)
    f.write("{name},{status},{comments},{rate},{zan}\n".format(**temp))
    # f.write('{status},{comments},{rate},{zan}\n'.format(**temp))
    # writer.writerow(temp)
f.close()