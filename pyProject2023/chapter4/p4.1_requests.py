'''
encoding:utf-8
author:yh
date:2023/3/13 10:02
'''
import requests

# 百度
# r=requests.get("https://www.baidu.com/")
# 豆瓣
## https://www.douban.com/robots.txt
## robots.txt会说明哪些东西可以访问，哪些东西禁止访问。
url = "https://www.douban.com/search"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'}
# 传入参数
dict = {'q': 'python'}  # 字典键码 q 对应网址的参数 q
r = requests.get(url, params=dict, headers=headers)
# r = requests.get(url, headers=headers)
r.encoding = 'utf-8'
print(r.status_code)
print(r.url)
print("——" * 50)
url = "https://www.baidu.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'}
res = requests.get(url, headers)
print(res.encoding)
res.encoding = 'utf-8'
print(res.status_code)
# print(res.text)
print("——" * 50)
# 获取10页的数据
for i in range(2):
    i += 1
    url = 'https://shenzhen.qfang.com/newhouse/list/n' + str(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'}
    res = requests.get(url, headers)
    res.encoding='utf-8'
    print(res.status_code)
    print(res.url)
    print("——" * 25)
print("——" * 50)
