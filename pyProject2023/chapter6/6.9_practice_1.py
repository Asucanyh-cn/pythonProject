'''
encoding:utf-8
author:yh
date:2023/5/10 8:50
'''

'''
爬取微博的评论，特点：
需要登录✔
评论滚动换页
'''

'''
构造GET请求参数
'''
import requests

url='https://weibo.com/2656274875/MFJRR4H54'
headers = {
    'Cookie': 'UOR=www.baidu.com,weibo.com,www.baidu.com; SINAGLOBAL=4303165608149.7505.1671426953884; ULV=1683678615420:2:1:1:4313604179437.642.1683678615410:1671426953887; XSRF-TOKEN=yyeBKLq68vjyJDTm3GaKjw9W; SCF=Aoe87EbPxWUGyUqaX5ysbbbnqE_lJgNVjyXjQf5gi4hb36tbDgIEQy7W_G3dK7blLdooSojRRLslseOyXickT0Q.; SUB=_2A25JWD1ADeRhGeBP71EY8SnLyz2IHXVqLCmIrDV8PUNbmtANLUvmkW9NRU8FY6HNkDdatzsDOhuS2m7B8DQny7MD; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFiZ4gZLknXvs2O_1VxvoPY5JpX5KMhUgL.FoqpShe4eKMNeh22dJLoI7yWMNHoqg44I5tt; ALF=1686362639; SSOLoginState=1683770640; WBPSESS=QV2ndNa-2oEEqPgbtu_MhjJq2p5LgxqsQJTWBnwmL-YCw2qtcTl08U_YNHNXL6Sgy9rQg0DKxgmVvF0Wtfgmcj5j1v88aAHA5eULsOBC-CFL-7nVbyAl4JhDbn-NCQhsLn159OV8BHZ0pkm47TnpFg==',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
r = requests.get(url, headers=headers)
print(r.text)