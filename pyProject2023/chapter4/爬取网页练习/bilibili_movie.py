'''
encoding:utf-8
author:yh
date:2023/3/27 16:31
'''
#爬取bilibili中的电影关数据
#解决ajax动态页面爬取（在浏览器中利用抓包工具进行全局搜索，找到目标url）
import requests
import json
url='https://api.bilibili.com/pgc/season/index/result?' \
    'st=2' \
    '&style_id=-1' \
    '&area=-1' \
    '&release_date=-1' \
    '&season_status=-1' \
    '&order=2' \
    '&sort=0' \
    '&page=1' \
    '&season_type=2' \
    '&type=1'\
    # '&pagesize=25'
params={
    'pagesize':100 #设置爬取总条数
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54'
}


data=requests.get(url,headers=headers,params=params)
data.encoding='utf-8'
# print(data)

jdata=json.loads(data.text) #以json格式读取接口返回的数据
# print(jdata)
f=open('bilibili_movie.csv',"w",encoding="utf-8")
f.write("title,subTitle,order,score,badge,link,\n")
for i in range(params['pagesize']):
    # print(i)
    item = jdata['data']['list'][i]
    # print(item['subTitle'])
    temp = {
        'title': item['title'],
        'subTitle': item['subTitle'],
        'order': item['order'],
        'score': item['score'],
        'badge': item['badge'],
        'link': item['link']
    }
    # print(temp)
    s='{title},{subTitle},{order},{score},{badge},{link}\n'.format(**temp)
    print('正在写入... '+s)
    f.write(s)
f.close()
print('Done')