'''
   字符串：用''或者""括起来的字符集合，比如'abc123'."xyzabc","xyz'123"
   注意的是单引号和双引号不能交叉！
'''
str1="I love Python"
print(str1)
print(str1[-1])
str2="e:\notebook" #\n代表换行,\t代表Tab键
print(str2)
print(r"e:\notebook")#r表示忽略所有的转义字符，保持字符串的原样
#字符串的切片操作
print(str1[2:-1])
#字符串的格式化(两种方法）
str3="there are %d apples %s the desk" #%d代表接受一个任意的整数，%s代表接受一个任意的字符串
print(str3%(10,'under'))
str4="there are {0} apples {1} the desk" #此方法不受数据类型限制
print(str4.format(3,'on'))
str5=str4.format(3,'on')

list1=str5.split()#将字符串根据空格分离出来
print(list1)

print(list1.count('apples'))#统计列表中的某个字符串出现的次数
str6=">6".join(list1)#将<list>中的元素用某字符串连接
print(str6)
str6=" ".join(list1)
print(str6)
str6="".join(list1)
print(str6)
str6="，".join(list1)
list2=str6.split("，")#将字符串根据逗号分离出来
print(list2)
