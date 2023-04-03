'''
encoding:utf-8
author:yh
date:2023/2/27 10:01
'''
import numpy as np
arr1 = np.array([2,3,4]) #通过*列表*创建一维矩阵
arr2 = np.array([(1.3,9,2.0),(7,6,1)]) #通过*元组*创建二行三列的二维矩阵
print(arr1)
print(arr2)
arr3 = np.zeros((2,3)) #通过元组(2, 3)生成全零二行三列的二维矩阵
print(arr3)
arr4 = np.identity(3) #生成三行三列的二维*单位矩阵*，对角线为1
print(arr4)
#生成每个元素都在[0,1]之间的二行三列随机矩阵
## 第一个random表示numpy中的子模块（类），第二个random表示类中的方法，size是方法中的参数‘size=（行，列）’，random()生成的是均匀的随机数
## 补充：random中还有个randn()生成服从标准的正态分布的随机数
arr5 = np.random.random(size = (2,3))
print(arr5)
arr6 = np.arange(5,20,3) #等距序列，参数为起点，终点，步长值。含起点值，不含终点值
print(arr6)
arr7 = np.linspace(0,2,5) #等距序列，参数为起点，终点，序列数。含起点值和终点值
print(arr7)
print(arr6) # [ 5 8 11 14 17]
print(arr1)
print(arr1.shape)
print(arr2)
print(arr2.shape) #返回矩阵的规格(2, 3)
print(arr1.ndim)
print(arr2.ndim) #返回矩阵的维度 2
print(arr2.size) #返回矩阵元素总数 6
# print(arr2.dtype.name) #返回矩阵元素的数据类型 float64
# print(type(arr2)) #查看整个数组对象的类型 <class 'numpy.ndarray'>

def f(x,y):
    return 10*x+y
arr8=np.fromfunction(f,(4,3),dtype=int)
print(arr8)
# 切片操作
print(arr8[1:3,1:])
print(arr8[:,1:]) #必须指定行列，不能为空
print(arr8[:,1:2]) #只要某一列
# arange
b= np.arange(12).reshape(3,4) #用 0 到 11 的整数生成三行四列的二维矩阵
print(b)

arr9 = np.array([[2,1],[3,1]])
arr10 = np.array([[1,2],[3,4]])
print(arr9,'\n',arr10)
# 矩阵相减
print(arr9-arr10)
# 乘法
## 对应位置相乘
print(arr9*arr10)
## 矩阵乘法
print(np.dot(arr9,arr10))
# 转置
print(arr10.T)
# 求逆矩阵
print(np.linalg.inv(arr10))
# 矩阵元素的求和、最大值、沿行（列）累计求和
print(np.sum(arr10))
print(np.max(arr10))
print(np.min(arr10))
print(arr10.cumsum(axis=0)) #axis=1 沿列累计
# 矩阵指数
print(np.exp(arr9))
# 矩阵的合并
arr11=np.vstack((arr9,arr10))#纵向合并数组，由于与堆栈类似，故命名为vstack
print(arr11)#按列合并，行不变
arr12=np.hstack((arr9,arr10))#横向合并数组
print(arr12)
print(np.hsplit(arr12,2))#将数组横向分为两部分，按列划分


# numpy补充
## dtype
## 用于描述与数组对应的内存区域是如何使用
### 使用标量类型定义数据类型
dt = np.dtype(np.int32)
print(dt)
### int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
dt = np.dtype('i4')
print(dt)
### 字节顺序标注定义数据类型
dt = np.dtype('<i4')
print(dt)
## 展示结构化数据类型的使用，类型字段和对应的实际类型将被创建。
# 首先创建结构化数据类型
import numpy as np
dt = np.dtype([('age',np.int8)]) # 即：第一列被命名为'age'列，且定义了数据类型为'int64'
print(dt)
# 将数据类型应用于 ndarray 对象
dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a)
## 再举一例
##定义一个结构化数据类型 student，包含字符串字段 name，整数字段 age，及浮点字段 marks，并将这个 dtype 应用到 ndarray 对象。
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print(a)
# 总结一下数组的属性
# ndarray.ndim	秩，即轴的数量或维度的数量
# ndarray.shape	数组的维度，对于矩阵，n 行 m 列
# ndarray.size	数组元素的总个数，相当于 .shape 中 n*m 的值
# ndarray.dtype	ndarray 对象的元素类型
# ndarray.itemsize	ndarray 对象中每个元素的大小，以字节为单位
# ndarray.flags	ndarray 对象的内存信息
# ndarray.real	ndarray元素的实部
# ndarray.imag	ndarray 元素的虚部
# ndarray.data	包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。

# 总结一下创建数组的方法
shape=[2,2]
x =  [1,2,3]
buffer =  b'Hello World'
list=range(5)
iterable = iter(list)
# 0. array函数创建数组
print(np.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0))
'''
object	数组或嵌套的数列
dtype	数组元素的数据类型，可选
copy	对象是否需要复制，可选
order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
subok	默认返回一个与基类类型一致的数组
ndmin	指定生成数组的最小维度
'''
# 1. 空数组（可指定形状）
print(np.empty(shape, dtype = float, order = 'C'))
## shape	数组形状
## dtype	数据类型，可选
## order	有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。
### 注意 − 数组元素为随机值，因为它们未初始化。
# 2. 全零数组
print(np.zeros(shape, dtype = float, order = 'C'))
# 3. 单位数组
print(np.ones(shape,dtype= None,order='C'))
# 4. 从已有的数组创建数组
print(np.asarray(x,dtype = None, order = None))
## x 任意形式的输入参数，可以是，列表, 列表的元组, 元组, 元组的元组, 元组的列表，多维数组。
# 5. 动态数组
print(np.frombuffer(buffer,dtype= 'S1', count = -1, offset = 0))
# 6. 从迭代对象中创建数组(什么是迭代器？)
print(np.fromiter(iterable, dtype=None, count=-1))
# 7. 从数值范围创建数组
start=0
stop=9
step=1
print(np.arange(start, stop, step, dtype=None))
## start	起始值，默认为0
## stop	终止值（不包含）
## step	步长，默认为1
## dtype	返回ndarray的数据类型，如果没有提供，则会使用输入数据的类型。
# 8. 创建一个一维数组，数组由等差序列构成。
print(np.linspace(start, stop, num=9, endpoint=True, retstep=False, dtype=None))
## start	序列的起始值
## stop	序列的终止值，如果endpoint为true，该值包含于数列中
## num	要生成的等步长的样本数量，默认为50
## endpoint	该值为 true 时，数列中包含stop值，反之不包含，默认是True。
## retstep	如果为 True 时，生成的数组中会显示间距，反之不显示。
## dtype	ndarray 的数据类型
# 9. 创建一个等比数列
print(np.logspace(start, stop, num=10, endpoint=True, base=2.0, dtype=None))
## start	序列的起始值为：base ** start
## stop	序列的终止值为：base ** stop。如果endpoint为true，该值包含于数列中
## num	要生成的等步长的样本数量，默认为50
## endpoint	该值为 true 时，数列中中包含stop值，反之不包含，默认是True。
## base	对数 log 的底数。
## dtype	ndarray 的数据类型


