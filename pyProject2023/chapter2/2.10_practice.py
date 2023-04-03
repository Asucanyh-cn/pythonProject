#斐波那契数列
# def Fib(n):
#     a=1
#     b=1
#     if(n==1):
#         print(a,end=' ')
#         print()
#     elif(n==2):
#         print(a,b,end=' ')
#         print()
#     else:
#         print(a, b, end=' ')
#         for i in range(n-2):
#             c=b
#             b=a+b
#             a=c
#             print(b,end=' ')
#         print()
# Fib(1)
# Fib(2)
# Fib(3)
# Fib(10)
#
# #
# # #筛选出奇数偶数数列
# list0=[2,5,8,12,35,56,9,4,12,55]
# list0.sort()
# print(list0)
# ##思路：遍历每一个元素，判断奇偶，放入对应列表中
# list1=[]
# list2=[]
# for e in list0:
#     if e % 2 ==0:
#         list2.append(e)
#     else:
#         list1.append(e)
# print("偶数列表：",list2,"奇数列表：",list1)

# #统计文件中的字符串词频
# file=open('news.txt','r',encoding='utf-8')
# content=file.read()
# print(content)
# str=input("需要统计的字符串：")
# n=0
# for word in content:
#     if word == str:
#         n+=1
# n=content.count(str)
# print(n)
# file.close()
# #
# # #加密：每位数字都加上 5，然后用除以 10 的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
# try:
#     num=int(input("请输入4位整数：\n"))
# except ValueError:
#     print("Please input integer only...")
# list=[]
# list.append(num%10)
# list.append(num%100/10)
# list.append(num%1000/100)
# list.append(num/1000)
# l=[]
# for i in range(4):
#     n=int((list[i]+5)%10)
#     l.insert(i,n)
# s=""
# for e in l:
#     s=s+str(e)
# print(s)

#游戏
class charactor:
    name=""
    sex=""
    age=0
    ce=0
    def __init__(self,name,sex,age,ce):
        self.name=name
        self.sex=sex
        self.age=age
        self.ce=ce
    def show(self):
        print(self.name,self.sex,self.age,"战斗力：",self.ce)
    def decrease(self):
        self.ce-=200
    def increase(self):
        self.ce+=200
    def attack(self,other):
        self.increase()
        other.decrease()
        print(self.name+"攻击了"+other.name)
    def practise(self):
        self.ce+=100
        print(self.name+"通过修炼增加100点攻击力！")
    def surrender(self,other):
        other.ce+=self.ce
        self.ce=0
        print(self.name+"向"+other.name+"投降")


c1=charactor("小赵","female",18,1000)
c2=charactor("小钱","male",20,1800)
c3=charactor("小孙","female",19,2500)
c1.show()
c2.show()
c3.show()
print("---分割线---")
c1.attack(c2)
# c1.show()
# c2.show()
# c3.show()

c1.practise()
c1.show()
print("---分割线---")
c2.show()
c3.show()
c2.surrender(c3)
c2.show()
c3.show()