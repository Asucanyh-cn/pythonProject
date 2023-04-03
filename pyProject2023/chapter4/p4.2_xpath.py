from lxml import  etree
htm='''
 <html>
     <div>
        <ul>
           <li class="item-0"><a href="src/1.html">第一个项目</a></li>
           <li class="item-1"><a href="src/2.html">第二个项目</a></li>
           <li class="item-2"><a href="src/3.html">第三个项目</a></li>
           <li class="item-1"><a href="src/4.html">第四个项目</a></li>
           <li class="else-0"><a href="src/5.html">其它项目</a></li>
           ul里的文本
        </ul>
     </div>
  </html>
'''
selector = etree.HTML(htm)

print("【获取标签中的文本】")
li_1=selector.xpath("/html/body/div/ul/li[@class='item-0']/a/text()")
print(li_1)
all_li=selector.xpath("//ul/li/a/text()")
print(all_li)
print("【string()直接获取标签中的所有文本】")
all_text=selector.xpath("string(//ul)")
print(all_text)
print("【获取某个属性的属性值，使用@属性名，可以查找对应的属性值】")
link_1=selector.xpath("//div/ul/li/a/@href")
print(link_1)
class_1=selector.xpath("//li/@class")
print(class_1)


#################################
print("【输出文本】")
for i in all_li:
    print(i,end=' ')
print()
print("【输出文本，使用strip函数去除空格】")
all_text=selector.xpath("//ul/text()")
print(all_text)
all_li_clean=[]
for text in all_text:
    if text.strip():
        all_li_clean.append(text.strip())
print(all_li_clean)
print("【输出文本，去除首尾空格，以及换行符】")
all_text=selector.xpath("string(//ul)")
all_text=all_text.strip().replace(' ','').replace("\n",' ')
print(all_text)
#################################
print("【xpath的嵌套】")
all_li=selector.xpath("//ul/li")
# print(all_li)
for i in all_li:
    print(i.xpath('a/text()')[0],end=" ")
print()