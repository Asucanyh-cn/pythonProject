'''
encoding:utf-8
author:yh
date:2023/5/10 8:50
'''

'''
爬取微博的评论，特点：
需要登录
评论滚动换页
'''

'''
构造GET请求参数


flow: 0
is_reload: 1
id: 4899477671118918
is_show_bulletin: 2
is_mix: 0
max_id: 142715924818154
count: 20
uid: 2656274875
fetch_level: 0


flow: 0
is_reload: 1
id: 4899477671118918
is_show_bulletin: 2
is_mix: 0
max_id: 139554828940230
count: 20
uid: 2656274875
fetch_level: 0
'''
params = {
            'id': weibo_id,
            'mid': weibo_id,
            'max_id': max_id,
            'max_id_type': max_id_type
        }