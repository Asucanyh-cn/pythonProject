'''
encoding:utf-8
author:yh
date:2023/3/27 10:31
'''
import re
import json
from bs4 import BeautifulSoup

with open("taobao.txt", "r", encoding="gbk") as f:
    data = f.read()
data = data.strip(' \n')
data = json.loads(data)
data = data['mods']['itemlist']['data']['auctions']
print(len(data))
f=open('python商品信息.csv',"w",encoding="gbk")
f.write("标题,价格,购买人数,邮费,是否天猫,地区\n")
for item in data:
    temp={
        'title':BeautifulSoup(item['title'],"html.parser").get_text(),
        'view_price':item['view_price'],
        'view_sales':re.sub('[^0-9]]',"",item['view_sales']),
        'view_fee':'是' if item['view_fee']=='0.00' else '否',
        'isTmall':'是' if item['shopcard']['isTmall']=='true' else '否',
        'item_loc':item['item_loc']
    }
    s='{title},{view_price},{view_sales},{view_fee},{isTmall},{item_loc}\n'.format(**temp)
    f.write(s)
    print(s)
f.close()