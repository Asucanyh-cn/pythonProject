# -*- coding: utf-8 -*-
print("hello world")
# 关键词
import keyword
print(keyword.kwlist)

# 字符串
str='1234567890'

print(str)                 # 输出字符串
print(str[0:])             # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串

print('------------------------------')
print('hello\nworld')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nworld')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

print(type(str))

# 列表
list=['a','b','c']
slist='abc'
print(list[:-1],slist[:-1])

# 集合
value01,value02 = 1,2
parame1 = {value01,value02}
parame2 = set([value01,value02])
print(parame1,parame2)

# 字典
dict={'a':1,'b':2}
print(dict['a'])
print(dict.values())
print(dict.keys())

#f-string
var1="usage"
var2="f-string"
print(f'The {var1} of {var2}')
#%
var1="usage"
var2="f-string"
print('The %s of %s' %(var1,var2)) 

# List
list=['book','pen','rubber']
list.append('notebook')
print(list)

# del list element
del list[0]
print(list)

#Nested list
a=['A','1']
b=['B','2']
n=[a,b]
print(n)

# 导入 operator 模块
import operator

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))

#list function
print(list)
list.reverse()
print(list)

#tuple
tup1=('1','2','3')
tup2='1','2','3'
print(tup1,tup2)

tup0=()
print(tup0)
tup3=('1',)
tup4=('1')
print(type(tup3),type(tup4))

tup1=('1','2','3')
tup2='a','b','c'
tup3=tup1+tup2
print(tup3)

del tup3
# print(tup3)

print(id(tup1),id(tup2))

dict={'fruit':'apple','phone':'redmi'}
dict['fruit']='pear'
# dict[0]='pear'
print(dict)

del dict['phone']
print(dict)

# var = 1
# while var==1:
#     print("循环中")

# flag=1
# while (flag): print ('循环中')

list=[1,2,3,4]
it = iter(list) 
for x in it:
    print (x, end=" ")
print()
def example():
    x=1
    yield x
    yield x+1
ex=example()
for i in ex:
    print(i,end=" ")
print()
# print(next(ex),next(ex))

def f(a,*b,**c):
    print(a,end=" ")
    print(b,end=" ")
    print(c)
f(1)
# def f(a,b,*,c):
#     return a+b+c
# x=f(1,2,c=3,d=4)
# print(x)

import _module_custom_
# from _module_custom_ import helloworld
_module_custom_.helloworld()
# helloworld()
import sys
x=dir(sys)
# x=dir()
print(x)
# print(sys.ps1)
#按顺序传入
str='{} {} {}'
print(str.format('a','b','c'))
#在括号中的数字用于指向传入对象在 format() 中的位置
str='{0} {1} {2}'
print(str.format('a','b','c'))
str='{A} {B} {C}'
print(str.format(A='a',B='b',C='c'))

class MyClass:
    a=1
    b=2
    def sum(self):
        return a+b
    def helloworld(self):
        return 'helloworld'
myClass=MyClass()
print(myClass.a,myClass.helloworld())

class InitClass:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
# ic=InitClass(1,2)
# print(ic.r,ic.i)

# class MyClass:
#     def prt(self):
#         print(self)
#         print(self.__class__)
# x=MyClass()
# x.prt()

# class MyClass(InitClass):
#     def prt(self):
#         print(self)
#         print(self.__class__)
# ic=MyClass(1,2)
# print(ic.r,ic.i)
class school:
    student='100'
    teacher='200'
    def schprt(self):
        print("学校：学生"+self.student+"人,老师"+self.teacher+"人")
class student:
    def __init__(s,g,c):
        s.grade=g
        s._class=c

class DerivedClass(school,student):
    id=1

x=DerivedClass(1,2)
x.schprt()

class Vector:
    def __init__(self, a, b):
      self.a = a
      self.b = b
 
    def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
    def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
    def prt(self):
        print(self.a+self.b)

 
v1 = Vector(2,10)
v2 = Vector(5,-2)
# print (v1 + v2)
v3=v1+v2
v1.prt()
v2.prt()
v3.prt()
#7,8

x=1
def function():
    global x
    x=100
    print(x)
function()
print(x)