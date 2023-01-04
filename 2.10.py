#斐波那契数列
def Fib(n):
    a=0
    b=1
    print(a,b,end=' ')
    for i in range(n-2):
        b=a+b
        a=b
        print(b,end=' ')
    print()
Fib(4)


#筛选出奇数偶数数列
list0=[2,5,8,12,35,56,9,4,12,55]
list0.sort()
print(list0)
##思路：遍历每一个元素，判断奇偶，放入对应列表中
list1=[]
list2=[]
for e in list0:
    if e % 2 ==0:
        list2.append(e)
    else:
        list1.append(e)
print("偶数列表：",list2,"奇数列表：",list1)

# #统计文件中的字符串词频
# file=open('res\\txt\\news.txt','r',encoding='utf-8')
# content=file.read()
# print(content)
# str=input("需要统计的字符串：")
# n=0
# # for word in content:
# #     if word == str:
# #         n+=1
# n=content.count(str)
# print(n)
# file.close()

#加密：每位数字都加上 5，然后用除以 10 的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
try:
    num=int(input("请输入4位整数：\n"))
except ValueError:
    print("Please input integer only...") 
list=[]
list.append(num%10)
list.append(num%100/10)
list.append(num%1000/100)
list.append(num/1000)
l=[]
for i in range(4):
    n=int((list[i]+5)%10)
    l.insert(i,n)
s=""
for e in l:
    s=s+str(e)
print(s)