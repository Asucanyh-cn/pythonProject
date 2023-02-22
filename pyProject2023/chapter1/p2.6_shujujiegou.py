'''
encoding:utf-8
author:yh
date:2023/2/16 10:37
'''
# 列表
List1 = ['Python',5,0.2]
print(List1[0])
print(List1[0:-1],List1[0:2])
print(List1[-1])
List2 = ['I','love','python']
print(List2[1],List2[-1])
print(List2[:],List2[0:2])
print(List1.index(5),List1.count(5)) #值为 5 的下标 1，5 出现的次数 1

List2.extend(List1)
#在 list2 末尾添加 list1
print(List2) #['I', 'really', 'love', 'python', 'Python', 5, 0.2]
List2.reverse()
#对列表的元素进行倒序排列
print(List2)
#[0.2, 5, 'Python', 'python', 'love', 'really', 'I']
List3=[1,3,2]
List3.sort() #对列表按值进行排序
print(List3) #[1, 2, 3]

# 字符串
str1 = 'learn Python'
print(str1,str1[0],str1[-1]) #输出整个字符串 learn Python,第一个字符 l，最后一个字符 n
print(str1[:8]) #切片 learn Py
# \n作为换行符，\t作为tab分隔符
print('E:\note\Python.doc')

# 字符串连接
str4 = 'String\t'
str5 = 'is powerful'
str4 = str4+str5
print(str4)
# 字符串格式化
format_str1 = 'There are %d apples %s the desk.'
a_tuple = (2,'on')
print(format_str1 % a_tuple) # There are 2 apples on the desk.
format_str2 = 'There are {0} apples {1} the desk.'.format(3,'on')
print(format_str2) # There are 3 apples on the desk.
format_str3 = 'There are %d apples %s the desk.'%(2,"on")
print(format_str3) # There are 2 apples on the desk.

