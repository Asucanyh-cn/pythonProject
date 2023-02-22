'''
encoding:utf-8
author:yh
date:2022/4/11 19:09
'''
'''
什么是网络爬虫？
如何高校的获取互联网上的海量数据，是大数据时代面临的重要问题
爬虫就是解决这些为而生的
'''
'''
requests是用python语言编写的HTTP库
导入:pip install requests
（出现SSL错误时）更新:pip install -U requests[security]
卸载:pip uninstall requests
'''
'''
准备：导入requests工具
第一步：对网络资源进行请求：requests.get方法或者post方法（可以通过查看目标网页以确定）
第二步：对网页进行解析，获取想要的信息
'''
import requests
# r=requests.get('https://www.qq.com')
# print(r.status_code)
# print(r.encoding)
# print(r.text)
res=requests.get('https://www.baidu.com')
# print(res.status_code)#输出状态码
# print(res.encoding)#输出网页采用的编码
print(res.text)#输出网页内容（源代码） Ctrl+F 搜索
res.encoding='utf-8'#修改编码形式
print(res.text)
print(res.content)#二进制形式输出内容，一般用在图片、视频。
print('——'*50)
url='https://www.douban.com'
r=requests.get(url)
print(r.status_code)
#出现418代码
'''
代码含义：
1开头的代码表示发出请求，但是未得到响应。
2开头表示请求发出且收到回应。
3开头表示重定向。
4开头表示客户端存在问题。5开头表示服务端存在问题。
'''
print(r.text)
#出现4开头的可以通过伪装浏览器解决
#如何获取伪装代码？
#任意打开一个网页后,F12,点击“网络”，刷新页面，任意选择一个加载出来的资源，滑到最后一行即可。
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36"
}#字典
r=requests.get(url,headers=headers)
print(r.status_code)
print('——'*50)
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36"
}#字典
res=requests.get('https://www.baidu.com',headers=headers)
# print(res.status_code)
# print(res.encoding)
# print(res.text)
res.encoding='utf-8'
print(res.text)
print('——'*50)
'''
xpath是一门在xml文档中查找信息的语言。
按照文档标签的嵌套关系（路径）遍历元素及其属性
//开始匹配标签
/匹配标签
@获取元素
@href获取文本的超级链接
@src获取图片
text()获取文本
*所有
''''''
lxml是一个网络解析库:pip install lxml --no-deps
'''
from lxml import etree #从lxml中导入etree工具
htm = '''
<html>
<div>
<ul>
<li class="item-0"><a href="src/1.html">第一个项目</a></li>
<li class="item-1"><a href="src/2.html">第二个项目</a></li>
<li class="item-2"><a href="src/3.html">第三个项目</a></li>
<li class="item-1"><a href="src/4.html">第四个项目</a></li>
<li class="else-0"><a href="src/5.html">其它项目</a></li>
ul 里的文本
</ul>
</div>
</html>
'''
selector=etree.HTML(htm)

li_1 = selector.xpath('//div/ul/li[1]/a/text()')
print(li_1)   #打印第一个列表中的文本
li_all = selector.xpath('//div/ul/li/a/text()')
print(li_all)  #打印所有列表的文本
li_3=selector.xpath('//*[@class="item-1"]/a/text()')#直接查找属性
'''
xpath可以通过浏览器自动生成
'''
print("——"*5)
all_text=''#空文本
all_li = selector.xpath('//div/ul/li')#获取了所有的li标签地址(对象所在内存地址)
#选择器的 xpath 对节点元素进行访问，返回列表
print(all_li)  #打印所有 li 元素对象列表
for c in all_li:#遍历all_li列表
    print(c.xpath('a/text()')[0])#注意将下标放在括号内！
    all_text=all_text+c.xpath('a/text()')[0]+" "
print("——"*5)
print(all_text)


