import requests
from lxml import etree
import time



area='nanjing'
url='https://'+area+'.qfang.com/newhouse/list/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41'}

# print(url)
# f=open(area+'.csv','a',encoding='utf-8')
f=open(area+'.csv','a',encoding='gbk')

f.write('名称,板块,均价\n')
# f=open(area+'.csv','r',encoding='utf-8')
# content=f.read()
# f.close()
# print(content)

##设置想要多少页的数据
print('——'*50)
while True:
    try:
        pages=int(input("请输入需要的页面数目："))
        if pages==0:
           pages=1
           print("默认抓取一页")
           break
        break
    except ValueError:
        print("请输入整数！")
for m in range(pages):
    htm=requests.get(url+'n'+str(m+1),headers=headers) #m+1表示从1开始
    time.sleep(1)
    print(htm.url)
    print('——' * 25)

    for i in range(20):
        selector=etree.HTML(htm.text)
        try:
            name=selector.xpath('//div['+str(i+1)+']/div/div[2]/div[1]/a/h3/text()')[0]
            plate=selector.xpath('//div['+str(i+1)+']/div/div[2]/div[2]/p[1]/text()')[0]
            #有些楼盘为待售，没有标注价格，所以爬取价格时可能出错
            try:
                 price = selector.xpath('//div[' + str(i + 1) + ']/div/div[3]/p[1]/span[1]/text()')[0]
            except:
                 price = 'null'

            s = str(name) + ',' + str(plate).strip() + ',' + str(price)  # 去除首尾的空格
            s = s.replace("\n", "")  # 去除末尾的换行符
            print("[Info]正在写入数据："+s)
            f.write(s + '\n')
        except:
            print("写入出错！")
print("[Info]爬取结束。")