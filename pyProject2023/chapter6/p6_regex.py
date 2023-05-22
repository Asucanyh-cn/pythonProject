'''
encoding:utf-8
author:yh
date:2023/4/17 10:11
'''
###Re常用方法
#match
#search
#findall
#finditer
#sub
###贪婪模式和非贪婪模式
import re
# # pattern = '\d+(.*)' #模式：\d 匹配数字,+表示 1 或多个,()代表组,.代表任意字符,*表示 0 或多个
# # pattern = r'^[123abc(fff)]*'
# pattern=r'.+f'
# text='12334444fffffaf'
# title_text = re.match(pattern, text) #match从第一个字符开始，找不到就直接匹配失败
# print(title_text)
# print(title_text.group(0)) #group(0)返回模式匹配中的所有内容
# print(title_text.group(1)) #group(1)返回模式匹配中()里的内容


line="aha34h44h45h"
pattern="h.{2,3}h"
res_match=re.search(pattern,line) #search匹配整个字符串，从左往右，找到第一个匹配的内容
res_match=re.findall(pattern,line) #findall匹配整个字符串，以列表形式返回匹配的内容
print(res_match)

line="I want% to eat! fengmi,da-chang."
pattern="[^a-zA-Z-]+"
res_match=re.findall(pattern,line)
print(res_match)

pattern="[a-zA-Z-]+"
res_match=re.finditer(pattern,line)
for item in res_match:
    print(item.group(0),end=" ")
print()


s="I3 i love you very much!"
pattern="([a-zA-Z-])[a-zA-Z-]+"
# pattern="[a-zA-Z-][a-zA-Z-]+"
res_match=re.findall(pattern,s) #findall会优先返回()中的匹配内容
print(res_match)


#贪婪模式和非贪婪模式
#匹配IP地址
pattern=r"(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])"
res_match=re.search(pattern,"202.202.1.1")
print(res_match)

# [\u4e00-\u9fa5]匹配所有汉字
pattern="[\u4e00-\u9fa5]+"
text="I am 我是汉字 text."
res=re.findall(pattern,text)
print(res)
