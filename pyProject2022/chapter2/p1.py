
list1=["python",3,True,4.5] #列表的定义
print(list1)#打印列表
#列表元素引用，通过下标来引用，从0开始，-1代表最后一个元素的索引
print(list1[0],list1[-1],list1[3])
#切片操作：取得连续的部分值，子集，用序号做索引，包括起始位置元素，但不包括结尾位置元素
print(list1[1:3],list1[1:-1])
print(list1[0:],list1[:])   #都表示取全部元素

list2=list1.append(10)      #等于号是赋值语句
print(list2)                #为什么是None? 因为list1.append(10)不会返回值

list1.append(10)
print(list1)
list2=list1
print(list2)

list1.insert(1,'really') #在指定位置插入一个元素
print(list1)

list1.remove('really') #删除列表中的元素
print(list1)

list1.reverse()#反序排列 ！注意列表内元素需要同类型，否则不可以反序！ 反序！=排序。排序使用<list>.sort()
print(list1)

list3=[2,5,1,10,7,4.5]
print(list3)
list3.reverse()#倒序排列 ！注意列表内元素需要同类型，否则不可以排序！
print(list3)
list3.sort(reverse=True)#降序排序
print(list3)
list3.sort(reverse=False)#升序排序
print(list3)