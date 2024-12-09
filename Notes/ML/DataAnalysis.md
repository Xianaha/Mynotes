# Data Analysis

## NumPy(Numerical Python)

Numpy 用于高效的数值计算，包括线性代数、随机数生成、统计计算等。其支持多维数组和矩阵运算等多种操作。
Numpy 的核心是ndarray(N-dimensional array)，它是一个功能强大的N维数组对象，封装了n维数组和矩阵运算的函数。
Numpy主要有以下特点：

1. **多维数组对象**：NumPy的核心数据结构是ndarray，它是一个多维数组，用于存储同质数据类型的元素。这些数组可以是一维、二维、三维等，非常适用于向量化操作和矩阵运算。
2. **广播功能**：NumPy允许在不同形状的数组之间执行操作，通过广播功能，它可以自动调整数组的形状，以使操作变得有效。
3. **索引和切片**：NumPy允许使用索引和切片操作来访问和修改数组中的元素，这使得数据的选择和处理非常灵活。
4. **高性能计算**：NumPy的底层实现是用C语言编写的，因此它在处理大规模数据时非常高效。此外，NumPy还与其他高性能计算库（如BLAS和LAPACK）集成，提供了快速的线性代数运算。
5. **互操作性**：NumPy可以与许多其他Python库和数据格式（例如Pandas、SciPy、Matplotlib）无缝集成，这使得数据科学工作流更加流畅。

使用方法：

```python
import numpy as np
```

常用方法：

### 自引用函数

`.shape`  
返回数组的形状。
```python
# 返回数组的形状
data = np.arange(1, 10)
data.shape
>>> (9,)
```

`.dim`  
返回数组的维度。
```python
# 返回数组的维度
data = np.arange(1, 10)
data.dim
>>> 1
```

`.dtype`  
返回数组元素的数据类型。
```python
# 返回数组元素的数据类型
data = np.arange(1, 10)
data.dtype
>>> dtype('int64')
```

`.size`  
返回数组元素的个数。
```python
# 返回数组元素的个数
data = np.arange(1, 10)
data.size
>>> 9
```

`.reshape(shape)`  
输出新形状的数组，不改变原数组的形状。若shape不符合数组元素个数，则会报错。
```python
# 不改变原数组的形状，返回一个新形状的数组
data = np.arange(1, 10)
data = data.reshape((3, 3))
data
>>> array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
```

`.resize(shape)`  
改变数组的形状，原数组元素会被覆盖。若shape不符合数组元素个数，则会用0填充。
```python
# 改变数组的形状，原数组元素会被覆盖，没有返回值
data = np.arange(1, 10)
data.resize((3, 3))
data
>>> array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
```

`.astype(dtype)`  
改变数组元素的数据类型。
```python
# 改变数组元素的数据类型
data = np.arange(1, 10)
data = data.astype(np.float32)
data
>>> array([1., 2., 3., 4., 5., 6., 7., 8., 9.])
```

`.swapaxes(axis1, axis2)`  
交换数组的两个维度。
```python
# 交换数组的两个轴
data = np.arange(1, 10).reshape((3, 3))
data = data.swapaxes(0, 1)
data
>>> array([[1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]])
```

`.T`  
返回数组的转置。
```python
# 返回数组的转置
data = np.arange(1, 10).reshape((3, 3))
data = data.T
data
>>> array([[1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]])
```

`.flatten()`  
返回数组的扁平化数组。即将数组展开成一维数组。
```python
# 返回数组的扁平化数组
data = np.arange(1, 10).reshape((3, 3))
data = data.flatten()
data
>>> array([1, 2, 3, 4, 5, 6, 7, 8, 9])
```

### 其他函数

`np.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)`  
将其他对象转换为ndarray，也可以创建数组。其中，object可以是列表、元组、元组列表、字典等。
```python
# 将其他对象转换为ndarray
lst = [1, 2, 3, 4, 5]
data = np.array(lst)
data
>>> array([1, 2, 3, 4, 5])

# 可以用np.array()创建数组
data = np.array([1, 2, 3, 4, 5])
data
>>> array([1, 2, 3, 4, 5])

data = np.array([[1, 2, 3], [4, 5, 6]])
data
>>> array([[1, 2, 3],
       [4, 5, 6]])
```

`np.eye(N, M=None, k=0, dtype=float)`  
创建N*N的单位矩阵。其中，N为矩阵的维度，M为矩阵的对角线元素个数，k为对角线元素的位置，dtype为数组元素的数据类型。
```python
# 创建N*N的单位矩阵
data = np.eye(3)
data
>>> array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
```

`np.zeros(shape, dtype=float, order='C')`  
创建指定形状和类型的全零数组。其中，shape为数组的形状，dtype为数组元素的数据类型，order为数组的存储顺序。
```python
# 创建指定形状和类型的全零数组
data = np.zeros((3, 4))
data
>>> array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
```

`np.ones(shape, dtype=None, order='C')`  
创建指定形状和类型的全一数组。其中，shape为数组的形状，dtype为数组元素的数据类型，order为数组的存储顺序。
```python
# 创建指定形状和类型的全一数组
data = np.ones((3, 4))
data
>>> array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
```

`np.full(shape, fill_value, dtype=None, order='C')`  
创建指定形状和类型的数组，数组元素的值都为fill_value。其中，shape为数组的形状，fill_value为数组元素的值，dtype为数组元素的数据类型，order为数组的存储顺序。
```python
# 创建指定形状和类型的数组，数组元素的值都为fill_value
data = np.full((3, 4), 3.14)
data
>>> array([[3.14, 3.14],
       [3.14, 3.14],
       [3.14, 3.14]])
```

`np.empty(shape, dtype=float, order='C')`  
创建指定形状和类型的未初始化数组。其中，shape为数组的形状，dtype为数组元素的数据类型，order为数组的存储顺序。
```python
# 创建指定形状和类型的未初始化数组，但由于是未初始化的，所以数据是随机的。
data = np.empty((3, 4))
data
>>> array([[1.70523023e-323, 1.70523023e-323, 1.70523023e-323, 1.70523023e-323],
       [1.70523023e-323, 1.70523023e-323, 1.70523023e-323, 1.70523023e-323],
       [1.70523023e-323, 1.70523023e-323, 1.70523023e-323, 1.70523023e-323]])
```

`np.arange(start, stop, step, dtype=None)`  
类似于Python内置函数range()，创建指定范围内的数组。其中，start为起始值，stop为终止值，step为步长，dtype为数组元素的数据类型。
```python
# 创建指定范围内的数组
data = np.arange(1, 10, 2)
data
>>> array([1, 3, 5, 7, 9])
```

`np.ones_like(a, dtype=None, order='K', subok=True)`  
创建与数组a相同形状和类型的全一数组。其中，a为数组，dtype为数组元素的数据类型，order为数组的存储顺序。
```python
# 创建与数组a相同形状和类型的全一数组
data = np.arange(1, 10)
data = np.ones_like(data)
data
>>> array([1, 1, 1, 1, 1])
```

`np.zeros_like(a, dtype=None, order='K', subok=True)`  
创建与数组a相同形状和类型的全零数组。其中，a为数组，dtype为数组元素的数据类型，order为数组的存储顺序。
```python
# 创建与数组a相同形状和类型的全零数组
data = np.arange(1, 10)
data = np.zeros_like(data)
data
>>> array([0, 0, 0, 0, 0])
```

`np.full_like(a, fill_value, dtype=None, order='K', subok=True)`  
创建与数组a相同形状和类型的数组，数组元素的值都为fill_value。其中，a为数组，fill_value为数组元素的值，dtype为数组元素的数据类型，order为数组的存储顺序。
```python
# 创建与数组a相同形状和类型的数组，数组元素的值都为fill_value
data = np.arange(1, 10)
data = np.full_like(data, 3.14)
data
>>> array([3.14, 3.14, 3.14])
```




`np.reshape(a, newshape, order='C')`  
改变数组的形状。其中，a为数组，newshape为新的形状，order为数组的存储顺序。
```python
# 改变数组的形状
data = np.arange(1, 10)
data = np.reshape(data, (3, 3))
data
>>> array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
```

`np.linspace(start, stop, num, endpoint=True, retstep=False, dtype=None)`  
创建指定范围内的等间隔数组。其中，start为起始值，stop为终止值，num为元素个数，endpoint为是否包含终止值，retstep为是否返回步长，dtype为数组元素的数据类型。
```python
# 创建指定范围内的等间隔数组
data = np.linspace(1, 10, 5)
data
>>> array([ 1.  ,  3.25,  5.5 ,  7.75, 10.   ])
```

`np.random.rand(d0, d1, ..., dn)`  
创建指定维度的随机数组，元素值在0~1之间。
```python
# 创建指定维度的随机数组
data = np.random.rand(3, 4)
data
>>> array([[0.5488135 , 0.71518937, 0.60276338, 0.54488318],
       [0.4236548 , 0.64589411, 0.43758721, 0.891773  ],
       [0.96366276, 0.38344152, 0.79172504, 0.52889492]])
```

`np.concatenate((a1, a2, ...), axis=0)`  
将多个数组连接起来。其中，a1, a2, ...为数组，axis为连接的轴。
```python
# 将多个数组连接起来，连接的轴为0
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.concatenate((a, b), axis=0)
c
>>> array([[1, 2],
       [3, 4],
       [5, 6],
       [7, 8]])

# 将多个数组连接起来，连接的轴为1
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.concatenate((a, b), axis=1)
c
>>> array([[1, 2, 5, 6],
       [3, 4, 7, 8]])
```

`np.vstack((a1, a2, ...))`  
将多个数组垂直堆叠起来。其中，a1, a2, ...为数组。
```python
# 将多个数组垂直堆叠起来
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.vstack((a, b))
c
>>> array([[1, 2],
       [3, 4],
       [5, 6],
       [7, 8]])
```

`np.hstack((a1, a2, ...))`  
将多个数组水平堆叠起来。其中，a1, a2, ...为数组。
```python
# 将多个数组水平堆叠起来
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.hstack((a, b))
c
>>> array([[1, 2, 5, 6],
       [3, 4, 7, 8]])
```

`np.where(condition, x, y)`  
根据条件选择数组元素。其中，condition为条件数组，x为选中元素，y为非选中元素。
```python
# 根据条件选择数组元素
a = np.array([[1, 2], [3, 4]])
b = np.where(a > 2, a, 0)
b
>>> array([[0, 0],
       [3, 4]])
```

### 切片
`arr[start:stop:step]`  
返回数组的切片，其中start为起始索引，stop为终止索引，step为步长。
```python
# 返回数组的切片
data = np.arange(1, 10)
data[1:5]
>>> array([2, 3, 4, 5])

# 步长为2
data[1:5:2]
>>> array([2, 4])
```

`arr[start:stop:step, start:stop:step, ...]`  
```python    
data = np.arange(1, 10).reshape((3, 3))
data[1:2, 1:2]
>>> array([[5]])
```

`arr[rows, cols]`  
rows为行索引，cols为列索引。
```python
data = np.arange(1, 10).reshape((3, 3))
data[[0, 1], [0, 1]]
>>> array([1, 4])
```

`arr[bool_arr]`  
根据布尔数组选择数组元素。其中，bool_arr为布尔数组。
```python
data = np.arange(1, 10).reshape((3, 3))
bool_arr = np.array([[True, False, True], [False, True, False], [True, False, True]])
data[bool_arr]
>>> array([1,3,5,7,9])
```

`arr[arr > 3]`  
```python
data = np.arange(1, 10).reshape((3, 3))
data[data > 3]
>>> array([4, 5, 6, 7, 8, 9])
```

### 运算

`+`  
计算两个数组对应位置元素的和。
```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = a + b
c
>>> array([[6, 8],
       [10, 12]])
```

`-`  
计算两个数组对应位置元素的差值。
```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = a - b
c
>>> array([[-4, -4],
       [-4, -4]])
```

`*`  
计算两个数组对应位置元素的乘积。
```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = a * b
c
>>> array([[5, 12],
       [21, 32]])
```

`/`  
计算两个数组对应位置元素的商。
```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = a / b
c
>>> array([[0.2, 0.33333333],
       [0.42857143, 0.5]])
```

`np.dot(a, b)`  
计算两个数组的点积。其中，a, b为数组。
```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.dot(a, b)
c
>>> array([[19, 22],
       [43, 50]])
```

`np.sum(arr, axis=None, dtype=None, out=None)`
返回数组的元素和（返回值是一个标量），其中axis为计算和的轴。
```python
a = np.array([[1, 2], [3, 4]])
b = np.sum(a)
b
>>> 10
```

`np.mean(arr, axis=None)`  
返回数组的均值。其中，axis为计算均值的轴。
```python
a = np.array([[1, 2], [3, 4]])
b = np.mean(a)
b
>>> 2.5
```

`np.max(a)`  
返回数组中最大值。
```python
a = np.array([[1, 2], [3, 4]])
b = np.max(a)
b
>>> 4
```

`np.min(a)`  
返回数组中最小值。
```python
a = np.array([[1, 2], [3, 4]])
b = np.min(a)
b
>>> 1
```

`np.argmax(a)`  
返回数组中最大值的索引。
```python
a = np.array([[1, 2], [3, 4]])
b = np.argmax(a)
b
>>> 3
```

`np.argmin(a)`  
返回数组中最小值的索引。
```python
a = np.array([[1, 2], [3, 4]])
b = np.argmin(a)
b
>>> 0
```

`np.sort(a)`  
返回数组排序后的副本。
```python
a = np.array([[1, 4], [3, 1]])
b = np.sort(a)
b
>>> array([[1, 4],
       [1, 3]])
```

`np.argsort(a)`  
返回数组排序后的索引。
```python
a = np.array([[1, 4], [3, 1]])
b = np.argsort(a)
b
>>> array([[1, 0],
       [0, 1]])
```

`np.std(a)`  
返回数组的标准差。
```python
a = np.array([[1, 2], [3, 4]])
b = np.std(a)
b
>>> 1.11803398875
```

`np.var(a)`  
返回数组的方差。
```python
a = np.array([[1, 2], [3, 4]])
b = np.var(a)
b
>>> 1.25
```

`np.prod(a)`  
返回数组所有元素的乘积。
```python
a = np.array([[1, 2], [3, 4]])
b = np.prod(a)
b
>>> 24
```

`np.cumsum(a, axis=None, dtype=None, out=None)`  
返回数组的累加和（是一个与原数组相同形状的数组，其中每个元素值都是从原数组的第一个元素开始到该元素的和）。其中，a为数组，axis为计算累加和的轴，dtype为数据类型，out为输出数组。
```python
a = np.array([[1, 2], [3, 4]])
b = np.cumsum(a)
b
>>> array([[1, 3],
       [4, 8]])
```

`np.cumprod(a, axis=None, dtype=None, out=None)`
返回数组的累乘积（是一个与原数组相同形状的数组，其中每个元素值都是从原数组的第一个元素开始到该元素的积）。其中，a为数组，axis为计算累乘积的轴，dtype为数据类型，out为输出数组。
```python
a = np.array([[1, 2], [3, 4]])
b = np.cumprod(a)
b
>>> array([[1, 2],
       [3, 8]])
```




### 数据的CSV文件读取
CSV文件是一种纯文本文件，其内容由纯文本数据组成，用逗号分隔，只能存储一维或二维数组。

`np.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ')`  
将数组X保存为CSV文件。其中，fname为文件名，X为数组，fmt为保存的格式，delimiter为分隔符，newline为换行符，header为文件头，footer为文件尾，comments为注释符。
```python
# 保存数组X为CSV文件
X = np.array([[1, 2], [3, 4]])
np.savetxt('data.csv', X, fmt='%d', delimiter=',', newline='\n', header='name,age,gender', footer='end')
```

`np.loadtxt(fname, dtype=float, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)`  
从CSV文件中读取数据。其中，fname为文件名，dtype为数据类型，comments为注释符，delimiter为分隔符，converters为转换器，skiprows为跳过的行数，usecols为读取的列索引，unpack为是否解包，ndmin为数组的最小维度。
```python
# 从CSV文件中读取数据
X = np.loadtxt('data.csv', dtype=int, delimiter=',', skiprows=1)
print(X)
```
### 多维数据的存取

`.tofile(fid, sep="", format="%s")`  
将数组保存为二进制文件。其中，fid为文件对象，sep为分隔符，如果是空串，写入文件为二进制，format为保存的格式。
```python
# 将数组保存为二进制文件
X = np.array([[1, 2], [3, 4]])
X.tofile('data.bin')
```

`.fromfile(fid, dtype=float, count=-1, sep="")`  
从二进制文件中读取数据。其中，fid为文件对象，dtype为数据类型，count为读取的元素个数，sep为分隔符。
```python
# 从二进制文件中读取数据
X = np.fromfile('data.bin', dtype=int)
print(X)
```

PS:a.tofile() 和np.fromfile（）要配合使用，要知道数据的类型和维度。

`np.save(file, arr, allow_pickle=True, fix_imports=True)`  
将数组保存为npy文件。其中，file为文件名，arr为数组，allow_pickle为是否允许pickle，fix_imports为是否修复导入。
```python
# 将数组保存为npy文件
X = np.array([[1, 2], [3, 4]])
np.save('data.npy', X)
```

`np.load(file, mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII')`  
从npy文件中读取数据。其中，file为文件名，mmap_mode为内存映射模式，allow_pickle为是否允许pickle，fix_imports为是否修复导入，encoding为编码。
```python
# 从npy文件中读取数据
X = np.load('data.npy')
print(X)
```

PS:np.save() 和np.load() 使用时，不用自己考虑数据类型和维度。








## Pandas(Panel Data)

### introduction

Pandas 是一个开源的第三方 Python 库，从 Numpy 和 Matplotlib 的基础上构建而来，享有数据分析“三剑客之一”的盛名（NumPy、Matplotlib、Pandas）。Pandas 已经成为 Python 数据分析的必备高级工具，它的目标是成为强大、灵活、可以支持任何编程语言的数据分析工具。

Pandas 这个名字来源于面板数据（Panel Data）与数据分析（data analysis）这两个名词的组合。在经济学中，Panel Data 是一个关于多维数据集的术语。Pandas 最初被应用于金融量化交易领域，现在它的应用领域更加广泛，涵盖了农业、工业、交通等许多行业。

Pandas 最初由 Wes McKinney（韦斯·麦金尼）于 2008 年开发，并于 2009 年实现开源。目前，Pandas 由 PyData 团队进行日常的开发和维护工作。在 2020 年 12 月，PyData 团队公布了最新的 Pandas 1.20 版本 。

在 Pandas 没有出现之前，Python 在数据分析任务中主要承担着数据采集和数据预处理的工作，但是这对数据分析的支持十分有限，并不能突出 Python 简单、易上手的特点。Pandas 的出现使得 Python 做数据分析的能力得到了大幅度提升，它主要实现了数据分析的五个重要环节：  
**加载数据**  
**整理数据**  
**操作数据**  
**构建数据模型**  
**分析数据**

我们知道，构建和处理二维、多维数组是一项繁琐的任务。Pandas 为解决这一问题， 在 ndarray 数组（NumPy 中的数组）的基础上构建出了两种不同的数据结构，分别是 Series（一维数据结构）DataFrame（二维数据结构）：  
Series 是带标签的一维数组，这里的标签可以理解为索引，但这个索引并不局限于整数，它也可以是字符类型，比如 a、b、c 等；  
DataFrame 是一种表格型数据结构，它既有行标签，又有列标签。

下面对上述数据结构做简单地的说明：

| 数据结构 |     维度     |     说明     |
| :----: |     :----:     |     :----:     |
|Series|	1	|该结构能够存储各种数据类型，比如字符数、整数、浮点数、Python 对象等，Series 用 name 和 index 属性来描述数据值。Series 是一维数据结构，因此其维数不可以改变。 |
|DataFrame|	2	|DataFrame 是一种二维表格型数据的结构，既有行索引，也有列索引。行索引是 index，列索引是 columns。在创建该结构时，可以指定相应的索引值。|

使用方法：
```python
import pandas as pd
```

### Series结构
Series 结构，也称 Series 序列，是 Pandas 常用的数据结构之一，它是一种类似于一维数组的结构，由一组数据值（value）和一组标签组成，其中标签与数据值之间是一一对应的关系。

Series 可以保存任何数据类型，比如整数、字符串、浮点数、Python 对象等，它的标签默认为整数，从 0 开始依次递增。Series 的结构图，如下所示：
![Series architecture](/Notes/ML/image/Series%20architecture.gif "Series architecture")  
通过标签我们可以更加直观地查看数据所在的索引位置。

`pd.Series(data=None, index=None, dtype=None, name=None, copy=False)`  
创建 Series 结构。其中，data 为数据列表，index 为索引列表，dtype 为数据类型，name 为 Series 名称，copy 为是否复制数据。
```python
# 创建Series结构
s = pd.Series()
s
>>> Series([], dtype: object)

s = pd.Series([1, 2, 3, 4, 5])
s
>>> 0    1
    1    2
    2    3
    3    4
    4    5
    dtype: int64

# 使用标量值创建Series结构，则必须提供索引，示例如下：
data = 10
index = ['A', 'B', 'C', 'D', 'E']
s = pd.Series(data, index=index)
s
>>> A    10
    B    10
    C    10
    D    10
    E    10
    dtype: int64

# ndarray 转换为 Series
a = np.array([1, 2, 3, 4, 5])
s = pd.Series(a)
s
>>> 0    1
    1    2
    2    3
    3    4
    4    5
    dtype: int64

# ndarray 是 NumPy 中的数组类型，当 data 是 ndarry 时，传递的索引必须具有与数组相同的长度。假如没有给 index 参数传参，在默认情况下，索引值将使用是 range(n) 生成，其中 n 代表数组长度，如下所示：
[0,1,2,3…. range(len(array))-1]

# 使用默认索引，创建 Series 序列对象：
data = np.array(['a','b','c','d'])
s = pd.Series(data)
s
>>> 0    a
    1    b
    2    c
    3    d
    dtype: object

# 给定索引值，创建 Series 序列对象：
# series 结构的索引可以是任意类型，比如字符串、日期等。

data = np.array(['a','b','c','d'])
index = ['A', 'B', 'C', 'D']
s = pd.Series(data, index=index)
s
>>> A    a
    B    b
    C    c
    D    d
    dtype: object

# dict创建Series对象
# 可以把 dict 作为输入数据。如果没有传入索引时会按照字典的键来构造索引；反之，当传递了索引时需要将索引标签与字典中的值一一对应。

data = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
s = pd.Series(data)
s
>>> A    1
    B    2
    C    3
    D    4
    dtype: int64

data = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
s = pd.Series(data, index=['A', 'B', 'C', 'D'])
s
>>> A    1
    B    2
    C    3
    D    4
    dtype: int64

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
s
>>> b    1.0
    c    2.0
    d    NaN
    a    0.0    
    dtype: float64
# pd.Series会按照index来构造索引寻找字典中的值，如果字典中有缺失值，则会用NaN填充。
```

### 访问Series数据

- 位置索引访问  
这种访问方式与 ndarray 和 list 相同，使用元素自身的下标进行访问。我们知道数组的索引计数从 0 开始，这表示第一个元素存储在第 0 个索引位置上，以此类推，就可以获得 Series 序列中的每个元素。下面看一组简单的示例：
```python
s = pd.Series([1, 2, 3, 4, 5], index=['A', 'B', 'C', 'D', 'E'])
s[0] # 位置下标访问
>>> 1

s['A'] # 标签下标访问
>>> 1

s[['A', 'C', 'E']] # 标签列表访问
>>> A    1
    C    3
    E    5
    dtype: int64

s[2:4] # 切片访问
>>> C    3
    D    4
    dtype: int64

s[s > 3] # 条件访问
>>> C    3
    D    4
    dtype: int64

#若索引不存在，则会报错：
s[10]
>>> KeyError: 10

s['F']
>>> KeyError: 'F'

```

`s.describe()`  
返回 Series 序列的描述性统计信息。其中，count 为非空值的个数，mean 为平均值，std 为标准差，min 为最小值，25% 为 25% 分位数，50% 为 50% 分位数，75% 为 75% 分位数，max 为最大值。
```python
s = pd.Series([1, 2, 3, 4, 5], index=['A', 'B', 'C', 'D', 'E'])
s.describe()
>>> count    5.000000
    mean     3.000000
    std      1.414214
    min      1.000000
    25%      2.000000
    50%      3.000000
    75%      4.000000
    max      5.000000
    dtype: float64
```

### Series常用属性和方法

下表列出了 Series 对象的常用属性。
| 名称 | 属性 |
| :---- | :---- |
| axes | 以列表的形式返回所有行索引标签。 |
| dtype | 返回 Series 序列的数据类型。 |
| empty | 返回 Series 序列是否为空。 |
| ndim | 返回 Series 序列的维数。 |
| shape | 返回 Series 序列的形状（元组）。 |
| size | 返回 Series 序列的元素个数（标量）。 |
| values | 返回 Series 序列的元素值。 |
| index | 返回 Series 序列的索引。 |

```python
s = pd.Series([1, 2, 3, 4, 5], index=['A', 'B', 'C', 'D', 'E'])
s.axes
>>> [RangeIndex(start=0, stop=5, step=1)] # 根据定义，Series 序列只有一维。

s.dtype
>>> dtype('int64')

s.empty
>>> False

s.ndim
>>> 1

s.shape
>>> (5,) # 根据定义，Series 序列只有一维。

5.size
>>> 5

5.values
>>> array([1, 2, 3, 4, 5])

s.index
>>> Index(['A', 'B', 'C', 'D', 'E'], dtype='object')
```

`s.head(n)`  
返回 Series 序列的前n行(前n个元素)。若不填写参数，则默认返回前5行;若n大于序列长度，则返回整个序列；若n为0，则返回空序列；若n为负数，则返回除了最后$|n|$个元素外的序列。
```python
s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
s.head()
>>> A    1
    B    2
    C    3
    D    4
    E    5
    dtype: int64
```

`s.tail()`  
返回 Series 序列的后几行。若不填写参数，则默认返回后5行;若n大于序列长度，则返回整个序列；若n为0，则返回空序列；若n为负数，则返回除了最前$|n|$个元素外的序列。
```python
s = pd.Series([1, 2, 3, 4, 5], index=['A', 'B', 'C', 'D', 'E'])
s.tail()
>>> A    1
    B    2
    C    3
    D    4
    E    5
    dtype: int64
```

`s.isnull()`  
用于检测 Series 序列中是否存在空值，返回布尔值序列。其中，True表示空值，False表示非空值。
```python
s = pd.Series([1, 2, 3, 4, None, 6, 7, 8, 9, 10], index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
s.isnull()
>>> A    False
    B    False
    C    False
    D    False
    E     True
    F    False
    G    False
    H    False
    I    False
    J    False
    dtype: bool
```

`s.notnull()`  
用于检测 Series 序列中是否存在非空值，返回布尔值序列。其中，True表示非空值，False表示空值。
```python
s = pd.Series([1, 2, 3, 4, None, 6, 7, 8, 9, 10], index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
s.notnull()
>>> A     True
    B     True
    C     True
    D     True
    E    False
    F     True
    G     True
    H     True
    I     True
    J     True
    dtype: bool
```
PS:其实不难理解，在实际的数据分析任物中，数据的收集往往要经历一个繁琐的过程。在这个过程中难免会因为一些不可抗力，或者人为因素导致数据丢失的现象。这时，我们可以使用相应的方法对缺失值进行处理，比如均值插值、数据补齐等方法。上述两个方法就是帮助我们检测是否存在缺失值。

### DataFrame结构
DataFrame 一个表格型的数据结构，既有行标签（index），又有列标签（columns），它也被称异构数据表，所谓异构，指的是表格中每列的数据类型可以不同，比如可以是字符串、整型或者浮点型等。其结构图示意图，如下所示：

![DataFrame architecture](/Notes/ML/image/Data%20Frame%20architecture.gif "DataFrame architecture")
表格中展示了某个销售团队个人信息和绩效评级（rating）的相关数据。数据以行和列形式来表示，其中每一列表示一个属性，而每一行表示一个条目的信息。

下表展示了上述表格中每一列标签所描述数据的数据类型，如下所示：
| 列标签 | 数据类型 |
| :---- | :---- |
| name | 字符串 |
| age | 整数 |
| gender | 字符串 |
| rating | 浮点数 |

DataFrame 的每一行数据都可以看成一个 Series 结构，只不过，DataFrame 为这些行中每个数据值增加了一个列标签。因此 DataFrame 其实是从 Series 的基础上演变而来。在数据分析任务中 DataFrame 的应用非常广泛，因为它描述数据的更为清晰、直观。

通过示例对  DataFrame 结构做进一步讲解。 下面展示了一张学生成绩表，如下所示：
![Student performance table](/Notes/ML/image/DataFrame%20Example.gif "Student performance table")

DataFrame 结构类似于 Execl 的表格型，表格中列标签的含义如下所示：
- Regd.No：表示登记的序列号
- Name：学生姓名
- Marks：学生分数

同 Series 一样，DataFrame 自带行标签索引，默认为“隐式索引”即从 0 开始依次递增，行标签与 DataFrame 中的数据项一一对应。上述表格的行标签从 0 到 5，共记录了 5 条数据（图中将行标签省略）。当然你也可以用“显式索引”的方式来设置行标签。

下面对 DataFrame 数据结构的特点做简单地总结，如下所示：
- DataFrame 每一列的标签值允许使用不同的数据类型；
- DataFrame 是表格型的数据结构，具有行和列；
- DataFrame 中的每个数据值都可以被修改。
- DataFrame 结构的行数、列数允许增加或者删除；
- DataFrame 有两个方向的标签轴，分别是行标签和列标签；
- DataFrame 可以对行和列执行算术运算。

使用Data Frame：

```python
import pandas as pd
```

### 创建DataFrame对象
创建 DataFrame 对象的语法格式如下：
```python
pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
```
- data：数据，可以是字典、列表、Numpy数组、Pandas的Series、或者其他DataFrame。
- index：行标签，可以是列表、Numpy数组、Pandas的Index，默认行标签是np.arange(n)生成的。
- columns：列标签，可以是列表、Numpy数组、Pandas的Index，默认列标签是np.arange(n)生成的。
- dtype：数据类型，可以是字符串、数据类型。
- copy：是否复制数据，默认为False。

`pd.DataFrame()`
```python
# 创建一个空的 DataFrame 对象。
df = pd.DataFrame()
>>> Empty DataFrame
    Columns: []
    Index: []

# 列表创建DataFame对象
data = [1,2,3,4,5]
df = pd.DataFrame(data)
df
>>> 0
0	1
1	2
2	3
3	4
4	5

# 使用嵌套列表创建 DataFrame 对象：
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
df
>>> Name  Age
0  Alex   10
1   Bob   12
2  Clarke  13

# 指定数值元素的数据类型为 float：
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
df
>>> Name  Age
0  Alex   10.0
1   Bob   12.0
2  Clarke  13.0

# 字典嵌套列表创建
# data 字典中，键对应的值的元素长度必须相同（也就是列表长度相同）。如果传递了索引，那么索引的长度应该等于数组的长度；如果没有传递索引，那么默认情况下，索引将是 range(n)，其中 n 代表数组长度。
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
df
>>> Name  Age
0   Tom   28
1  Jack   34
2  Steve  29
3  Ricky  42
# 这里使用了默认行标签，也就是 range(n)。它生成了 0,1,2,3，并分别对应了列表中的每个元素值。

# 现在给上述示例添加自定义的行标签：
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
df
>>>     Name  Age
rank1   Tom   28
rank2  Jack   34
rank3  Steve  29
rank4  Ricky  42
# index 参数为每行分配了一个索引。

# 列表嵌套字典创建DataFrame对象
# 列表嵌套字典可以作为输入数据传递给 DataFrame 构造函数。默认情况下，字典的键被用作列名。
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
df
>>>    a  b    c
0      1  2   NaN
1      5  10  20.0
# 这里，字典的键 a 和 b 被用作列名，键 c 被忽略。

# 给上述示例添加行标签索引：
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
df
>>>    a  b    c
first   1  2   NaN
second  5  10  20.0

# 使用字典嵌套列表以及行、列索引表创建一个 DataFrame 对象。
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
df1, df2
>>> (        a   b
     first   1   2
     second  5  10,
             a  b1
     first   1 NaN
     second  5 NaN)

# Series创建DataFrame对象
# 可以传递一个字典形式的 Series，从而创建一个 DataFrame 对象，其输出结果的行索引是所有 index 的合集。
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
df
>>>    one  two
    a   1.0   1
    b   2.0   2
    c   3.0   3
    d   NaN   4
# 对于 one 列而言，此处虽然显示了行索引 'd'，但由于没有与其对应的值，所以它的值为 NaN。
```

### 列索引操作DataFrame
DataFrame 可以使用列索（columns index）引来完成数据的选取、添加和删除操作。
```python
# 列索引选取数据列
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
df['one']
>>> a    1
    b    2
    c    3
    Name: one, dtype: int64

# 列索引添加数据列
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
df['three'] = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
df
>>>    one  two  three
    a   1.0   1   10.0
    b   2.0   2   20.0
    c   3.0   3   30.0
    d   NaN   4   40.0
# 这里可以通过列做相加运算：
df['sum'] = df['one'] + df['two'] + df['three']
df
>>>    one  two  three  sum
    a   1.0   1   10.0   12.0
    b   2.0   2   20.0   24.0
    c   3.0   3   30.0   36.0
    d   NaN   4   40.0   NaN

# 列索引删除数据列
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
   'three' : pd.Series([10,20,30], index=['a','b','c'])}
df = pd.DataFrame(d)
del df['two']
df
>>>    one  three
    a   1.0   10.0
    b   2.0   20.0
    c   3.0   30.0
# 这里删除了列 two。

```
### 行索引操作DataFrame
```python
# 标签索引选取
# 可以将行标签传递给 loc 函数，来选取数据。
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
df.loc['a']
>>> one    1
    two    1
    Name: a, dtype: int64
# loc 允许接两个参数分别是行和列，参数之间需要使用“逗号”隔开，但该函数只能接收标签索引。

# 整数索引选取
# 通过将数据行所在的索引位置传递给 iloc 函数，也可以实现数据行选取。
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
df.iloc[0]
>>> one    1
    two    1
    Name: a, dtype: int64
# iloc 允许传递整数索引，但该函数只能接收整数索引。

# 切片操作多行选取
# 也可以使用切片的方式同时选取多行。
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
df.loc['a':'c']
>>>    one  two
    a   1.0   1
    b   2.0   2
    c   3.0   3
# 这里使用了标签索引，选取了 a 到 c 之间的行。

df.iloc[0:2]
>>>    one  two
    a   1.0   1
    b   2.0   2
# 这里使用了整数索引，选取了 0 到 2 之间的行。
```

`df.drop(labels=None, axis=0, index=None, columns=None, inplace=False, errors='raise')`  
删除指定行或列的数据。其中，labels为行或列标签，axis为0表示删除行，为1表示删除列，index和columns分别表示行标签和列标签，inplace为True表示直接修改原数据，为False表示返回修改后的新数据, errors为'ignore'表示忽略错误、'raise'表示抛出错误。
```python
# 删除指定行或列的数据
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
df.drop('a', axis=0)
>>>    one  two
    b   2.0   2
    c   3.0   3
    d   NaN   4
# 这里删除了行标签为 'a' 的行。

df.drop('two', axis=1)
>>>    one
    a   1.0
    b   2.0
    c   3.0
    d   NaN
# 这里删除了列标签为 'two' 的列。

df.drop(['a', 'b'], axis=0)
>>>    one  two
    c   3.0   3
    d   NaN   4
# 这里删除了行标签为 'a' 和 'b' 的行。

df.drop(['one', 'two'], axis=1)
>>> Empty DataFrame
    Columns: []
    Index: [a, b, c, d]
# 这里删除了列标签为 'one' 和 'two' 的列。
```

### 常用属性和方法
| 名称 | 属性&方法 | 说明 |
| :---- | :---- | :---- |
| T | `df.T` | 转置，交换行列 |
| shape | `df.shape` | 返回一个元组（行数，列数） |
| index | `df.index` | 返回行标签（以Series形式） |
| columns | `df.columns` | 返回列标签（以Series形式） |
| values | `df.values` | 返回DataFrame中的数据（以Numpy数组形式） |
| dtypes | `df.dtypes` | 返回DataFrame中每列的数据类型 |
| ndim | `df.ndim` | 返回DataFrame的维度 |
| size | `df.size` | 返回DataFrame的大小 |
| empty | `df.empty` | 判断DataFrame是否为空 |
| info | `df.info()` | 打印DataFrame的概览信息 |
| describe | `df.describe()` | 打印DataFrame的汇总统计信息 |
| head | `df.head(n=5)` | 显示前n行数据 |
| tail | `df.tail(n=5)` | 显示后n行数据 |

`df.describe()`  
打印DataFrame的汇总统计信息。
```python
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
df.describe()
>>>        one    two
count  3.000000  4.000000
mean   2.000000  2.500000
std    1.000000  1.118034
min    1.000000  1.000000
25%    1.500000  1.750000
50%    2.000000  2.500000
75%    2.500000  3.250000
max    3.000000  4.000000
```

`df.info()`  
打印DataFrame的概览信息。
```python
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
df.info()
<class 'pandas.core.frame.DataFrame'>
Index: 4 entries, a to d
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   one     3 non-null      float64
 1   two     4 non-null      int64  
dtypes: float64(1), int64(1)
memory usage: 96.0+ bytes
```

`pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, copy=True)`  
将多个DataFrame对象合并为一个DataFrame。其中，objs为DataFrame对象列表，axis为合并的轴，join为合并方式，join_axes为合并轴，ignore_index为是否忽略原索引，keys为合并后的索引，levels为层次化索引，names为层次化索引的名称，verify_integrity为是否检查合并后数据的完整性，copy为是否复制数据。
```python
# 合并两个DataFrame对象
d1 = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df1 = pd.DataFrame(d1)

d2 = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df2 = pd.DataFrame(d2)

df3 = pd.concat([df1, df2])
df3
>>>    one  two
a       1.0   1
b       2.0   2
c       3.0   3
d       NaN   4
a       1.0   1
b       2.0   2
c       3.0   3
d       NaN   4

# 合并两个DataFrame对象，指定合并轴
df4 = pd.concat([df1, df2], axis=1)
df4
>>>    one	two	one	two
a	   1.0	1	1.0	1
b	   2.0	2	2.0	2
c	   3.0	3	3.0	3
d	   NaN	4	NaN	4
a	   1.0	1	1.0	1
b	   2.0	2	2.0	2
c	   3.0	3	3.0	3
d	   NaN	4	NaN	4

# 合并两个DataFrame对象，指定合并方式, 这里join='inner'表示只保留共同的行，其他的行将被删除，做交集。若join='outer'，则保留所有行，做并集。由参数axes指定合并轴。这里默认为0，表示合并行。
df5 = pd.concat([df1, df2], join='inner')
df5
>>>    one	two
a	    1.0	1
b	    2.0	2
c	    3.0	3
d	    NaN	4
a	    1.0	1
b	    2.0	2
c	    3.0	3
d	    NaN	4

# 合并两个DataFrame对象，指定合并轴和合并方式
df6 = pd.concat([df1, df2], axis=1, join='inner')
df6
>>>    	one	two	one	two
a	    1.0	1	1.0	1
b	    2.0	2	2.0	2
c	    3.0	3	3.0	3
d	    NaN	4	NaN	4

# 合并两个DataFrame对象，指定合并轴和合并方式
df7 = pd.concat([df1, df2], join='outer')
df7
>>>    one  two
a       1.0   1
b       2.0   2
c       3.0   3
d       NaN   4
a       1.0   1
b       2.0   2
c       3.0   3
d       NaN   4

# 合并两个DataFrame对象，指定合并轴和合并方式
df8 = pd.concat([df1, df2], join='outer', axis=1)
df8
>>>    one	two	one	two
a	   1.0	1	1.0	1
b	   2.0	2	2.0	2
c	   3.0	3	3.0	3
d	   NaN	4	NaN	4
a	   1.0	1	1.0	1
b	   2.0	2	2.0	2
c	   3.0	3	3.0	3
d	   NaN	4	NaN	4
```

`dp.shift(periods=1, freq=None, axis=0)`  
对DataFrame进行数据移动，返回新的DataFrame。其中，periods为移动的行数，freq为移动的频率，axis为移动的轴。
```python
# 对DataFrame进行数据移动
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
df.shift(periods=1)
>>>    one	two
a	    NaN	NaN
b	    1.0	1.0
c	    2.0	2.0
d	    3.0	3.0

df.shift(periods=-1)
>>>   one	two
a	2.0	2.0
b	3.0	3.0
c	NaN	4.0
d	NaN	NaN
```

`dp.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')`  
对DataFrame排序。其中，by为排序的列名，axis为排序的轴，ascending为是否升序，inplace为是否直接修改原数据，kind为排序算法，na_position为NaN值的位置。
```python
# 对DataFrame排序
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
df.sort_values(by='one')
>>>    one  two
a   1.0   1
b   2.0   2
c   3.0   3
d   NaN   4

df.sort_values(by='one', ascending=False)
>>>    one  two
d   NaN   4
c   3.0   3
b   2.0   2
a   1.0   1

df.sort_values(by=['one', 'two'], ascending=[True, False])
>>>    one  two
a   1.0   1
b   2.0   2
c   3.0   3
d   NaN   4
```

`df.sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last')`  
对DataFrame索引排序。其中，axis为排序的轴，level为层次化索引，ascending为是否升序，inplace为是否直接修改原数据，kind为排序算法，na_position为NaN值的位置。
```python
# 对DataFrame索引排序
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
df.sort_index()
>>>    one  two
a   1.0   1
b   2.0   2
c   3.0   3
d   NaN   4

df.sort_index(ascending=False)
>>>    one  two
d   NaN   4
c   3.0   3
b   2.0   2
a   1.0   1

df.sort_index(level=0, ascending=False)
>>>    one  two
a   1.0   1
b   2.0   2
c   3.0   3
d   NaN   4
```

`df.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, observed=False)`  
对DataFrame进行分组。其中，by为分组的列名，axis为分组的轴，level为层次化索引，as_index为是否保留原索引，sort为是否排序，group_keys为是否保留组名，squeeze为是否将分组后的结果压缩为Series，observed为是否观察组名。
```python
# 对DataFrame进行分组
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
df.groupby(by='one').sum()
>>>    one  two
a   1.0   1
b   2.0   2
c   3.0   3
d   NaN   4
```






### Pandas 读取文件
CSV 又称逗号分隔值文件，是一种简单的文件格式，以特定的结构来排列表格数据。 CSV 文件能够以纯文本形式存储表格数据，比如电子表格、数据库文件，并具有数据交换的通用格式。CSV 文件会在 Excel 文件中被打开，其行和列都定义了标准的数据格式。

将 CSV 中的数据转换为 DataFrame 对象是非常便捷的。和一般文件读写不一样，它不需要你做打开文件、读取文件、关闭文件等操作。相反，您只需要一行代码就可以完成上述所有步骤，并将数据存储在 DataFrame 中。

假如现在有一个 CSV 文件 data.csv，其内容如下：

```
Name,Hire Date,Salary,Leaves Remaining 
John Idle,08/15/14,50000.00,10 
Smith Gilliam,04/07/15,65000.00,6 
Parker Chapman,02/21/14,45000.00,7 
Jones Palin,10/14/13,70000.00,3 
Terry Gilliam,07/22/14,48000.00,9 
Michael Palin,06/28/13,66000.00,8  
```

`pd.read_csv(filepath_or_buffer，sep，header，names，index_col，encoding，skiprows，nrows，na_values，engine，usecols，parse_dates, low_memory)`  
其中，filepath_or_buffer为文件路径或文件对象，sep为分隔符（默认为逗号，也可以指定为其他字符，比如制表符（\t）或分号（;）），header为文件是否有标题行（指定行数作为列名，默认为0，表示没有标题行），names为列名列表（用于自定义列名，若header为None，则该参数必须指定），index_col为索引列，encoding为编码格式（指定文件的编码格式，默认为'utf-8'。在处理某些编码的文件时（如应为 latin1），可以设置为其他编码格式），skiprows为跳过的行数，nrows为读取的行数，na_values为缺失值列表，engine为引擎，usecols为读取的列名列表，parse_dates为日期列名列表，low_memory为内存优化参数（默认为True，表示在解析数据时使用分块的方法以节省内存。当处理大数据集时，可以设置为False来强制一次性读取整个文件）。
```python
# 读取CSV文件
df = pd.read_csv('data.csv')
print(df)
>>>    Name  Hire Date  Salary  Leaves Remaining
0  John Idle  08/15/14  50000.00                10
1  Smith Gilliam  04/07/15  65000.00                 6
2  Parker Chapman  02/21/14  45000.00                 7
3   Jones Palin  10/14/13  70000.00                 3
4  Terry Gilliam  07/22/14  48000.00                 9
5  Michael Palin  06/28/13  66000.00                 8

# 读取json文件
data = pd.read_json('data.json')
print(data)
>>>    Name  Hire Date  Salary  Leaves Remaining
0  John Idle  08/15/14  50000.00                10
1  Smith Gilliam  04/07/15  65000.00                 6
2  Parker Chapman  02/21/14  45000.00                 7
3   Jones Palin  10/14/13  70000.00                 3
4  Terry Gilliam  07/22/14  48000.00                 9
5  Michael Palin  06/28/13  66000.00                 8
```



### Pandas csv读写文件
文件的读写操作属于计算机的 IO 操作，Pandas IO 操作提供了一些读取器函数，比如 pd.read_csv()、pd.read_json 等，它们都返回一个 Pandas 对象。

在 Pandas 中用于读取文本的函数有两个，分别是： read_csv() 和 read_table() ，它们能够自动地将表格数据转换为 DataFrame 对象。

假如现在有一个 CSV 文件 C:/Users/Administrator/Desktop/person.csv，其内容如下：

```
ID,Name,Age,City,Salary
1,Jack,28,Beijing,22000
2,Lida,32,Shanghai,19000
3,John,43,Shenzhen,12000
4,Helen,38,Hengshui,3500
```

`pandas.read_csv(filepath_or_buffer, sep=',', skiprows=None, delimiter=None, header='infer',names=None, index_col=None, usecols=None)`
其中，filepath_or_buffer：文件路径或文件对象；sep：分隔符，默认为逗号；delimiter：分隔符，默认为 None；header：表头行数或列名列表，默认为 'infer'，表示自动检测；names：列名列表，默认为 None；index_col：索引列，默认为 None；usecols：读取的列名列表，默认为 None。
```python
# 读取CSV文件
df = pd.read_csv('C:/Users/Administrator/Desktop/person.csv')
print(df)
>>>    ID  Name  Age  City  Salary
0   1  Jack   28  Beijing   22000
1   2  Lida   32  Shanghai   19000
2   3  John   43  Shenzhen   12000
3   4  Helen   38  Hengshui    3500

# 自定义索引
# 在 CSV 文件中指定了一个列，然后使用index_col可以实现自定义索引。
df=pd.read_csv("C:/Users/Administrator/Desktop/person.csv",index_col=['ID'])
df
>>>    Name  Age  City  Salary
ID                               
1  Jack   28  Beijing   22000
2  Lida   32  Shanghai   19000
3  John   43  Shenzhen   12000
4  Helen   38  Hengshui    3500

# 查看每一列的dtype
df=pd.read_csv("C:/Users/Administrator/Desktop/person.csv",dtype={'Salary':np.float64})
df.dtypes
>>> ID           int64
Name         object
Age          int64
City         object
Salary    float64
dtype: object
# 默认情况下，Salary 列的 dtype 是 int 类型，但结果显示其为 float 类型，因为已经在上述代码中做了类型转换。

# 更改文件标头名
# 使用 names 参数可以指定头文件的名称。
df=pd.read_csv("C:/Users/Administrator/Desktop/person.csv",names=['a','b','c','d','e'])
df
>>>   a      b    c         d       e
0  ID   Name  Age      City  Salary
1   1   Jack   28   Beijing   22000
2   2   Lida   32  Shanghai   19000
3   3   John   43  Shenzhen   12000
4   4  Helen   38  Hengshui    3500
# 文件标头名是附加的自定义名称，但是您会发现，原来的标头名（列标签名）并没有被删除，此时您可以使用header参数来删除它。
df=pd.read_csv("C:/Users/Administrator/Desktop/person.csv",names=['a','b','c','d','e'],header=0)
df
>>>  a      b   c         d      e
0  1   Jack  28   Beijing  22000
1  2   Lida  32  Shanghai  19000
2  3   John  43  Shenzhen  12000
3  4  Helen  38  Hengshui   3500
# 现在，文件标头名已经被删除，只保留了自定义名称。假如原标头名并没有定义在第一行，您也可以传递相应的行号来删除它。

# 跳过指定的行数
# skiprows参数表示跳过指定的行数。
df=pd.read_csv("C:/Users/Administrator/Desktop/person.csv",skiprows=2)
df
>>>    ID  Name  Age  City  Salary
0   3  John   43  Shenzhen   12000
1   4  Helen   38  Hengshui    3500
# 跳过了前两行，只读取了后两行。

```

Pandas 提供的 to_csv() 函数用于将 DataFrame 转换为 CSV 数据。如果想要把 CSV 数据写入文件，只需向函数传递一个文件对象即可。否则，CSV 数据将以字符串格式返回。
`pd.to_csv(path_or_buf, sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, mode='w', encoding=None, compression=None, quoting=None, quotechar='"', line_terminator='\n', chunksize=None, date_format=None, doublequote=True, escapechar=None, decimal='.')`  
其中:
- `path_or_buf`：文件路径或文件对象；
- `sep`：分隔符，默认为逗号；
- `na_rep`：缺失值替换字符，默认为 ''；
- `header`：是否写入列名，默认为 True；
- `float_format`：浮点数格式，默认为 None；
- `columns`：列名列表，默认为 None；header：是否写入列名，默认为 True；
- `index`：是否写入索引，默认为 True；
- `index_label`：：索引标签，默认为 None；
- `mode`：写入模式，默认为 'w'；
- `encoding`：编码格式，默认为 None；
- `compression`：压缩格式，默认为 None；
- `quoting`：引号类型，默认为 None；
- `quotechar`：引号字符，默认为 '"'；
- `line_terminator`：行终止符，默认为 '\n'；
- `chunksize`：写入块大小，默认为 None；
- `date_format`：日期格式，默认为 None；
- `doublequote`：双引号类型，默认为 True；
- `escapechar`：转义字符，默认为 None；
- `decimal`：小数点符号，默认为 '.'。
```python
# 写入CSV文件
data = {'Name': ['Smith', 'Parker'], 'ID': [101, 102], 'Language': ['Python', 'JavaScript']} 
info = pd.DataFrame(data) 
info.to_csv('data.csv')
>>> data.csv:
    Name  ID  Language
0  Smith  101    Python
1  Parker  102  JavaScript

# 可以通过设定index=False参数，禁止写入索引。
info.to_csv('data.csv', index=False)
>>> data.csv:
Name  ID  Language
Smith  101    Python
Parker  102  JavaScript

# 也可以通过sep参数指定分隔符
info.to_csv('data.csv', sep='|')
>>> data.csv:
    Name|ID|Language
0  Smith|101|Python
1  Parker|102|JavaScript
```


`pd.read_table(filepath_or_buffer, sep='\t', delimiter=None, header='infer', names=None, index_col=None, usecols=None)`
其中，filepath_or_buffer：文件路径或文件对象；sep：分隔符，默认为制表符；delimiter：分隔符，默认为 None；header：表头行数或列名列表，默认为 'infer'，表示自动检测；names：列名列表，默认为 None；index_col：索引列，默认为 None；usecols：读取的列名列表，默认为 None。
```python
# 读取CSV文件
df = pd.read_table('C:/Users/Administrator/Desktop/person.csv', sep=',')
print(df)
>>>    ID  Name  Age  City  Salary
0   1  Jack   28  Beijing   22000
1   2  Lida   32  Shanghai   19000
2   3  John   43  Shenzhen   12000
3   4  Helen   38  Hengshui    3500
```

### Pandas Excel读写文件

假若现在有一个Excel文件data.xlsx，如下表所示：
| ID | Name | Age | City | Salary |
| --- | --- | --- | --- | --- |
| 1 | Jack | 28 | Beijing | 22000 |
| 2 | Lida | 32 | Shanghai | 19000 |
| 3 | John | 43 | Shenzhen | 12000 |
| 4 | Helen | 38 | Hengshui | 3500 |

`pd.read_excel(io, sheet_name=0, header=0, names=None, index_col=None,
              usecols=None, squeeze=False,dtype=None, engine=None,
              converters=None, true_values=None, false_values=None,
              skiprows=None, nrows=None, na_values=None, parse_dates=False,
              date_parser=None, thousands=None, comment=None, skipfooter=0,
              convert_float=True, **kwds)`
| 参数 | 说明 |
| --- | --- |
| io | 表示 Excel 文件的存储路径。 |
| sheet_name | 工作表名称或索引，默认为 0 |
| header | 指定作为列名的行，默认0，即取第一行的值为列名；若数据不包含列名，则设定 header = None。若将其设置为 header=2，则表示将前两行作为多重索引。 |
| names | 一般适用于Excel缺少列名，或者需要重新定义列名的情况；names的长度必须等于Excel表格列的长度，否则会报错。 |
| index_col | 用做行索引的列，可以是工作表的列名称，如 index_col = '列名'，也可以是整数或者列表。 |
| usecols | int或list类型，默认为None，表示需要读取所有列。 |
| squeeze | 是否将结果压缩为 Series，默认为 False |
| dtype | 数据类型字典，默认为 None |
| engine | 引擎，默认为 None |
| converters | 类型转换器字典，规定每一列的数据类型，默认为 None |
| true_values | 真值列表，默认为 None |
| false_values | 假值列表，默认为 None |
| skiprows | 接受一个列表，表示跳过指定行数的数据，从头部第一行开始，默认为 None |
| nrows | 需要读取的行数，默认为 None |
| na_values | 缺失值列表，默认为 None |
| parse_dates | 是否将日期列转换为日期类型，默认为 False |
| date_parser | 日期解析器，默认为 None |
| thousands | 千分位分隔符，默认为 None |
| comment | 注释行标记，默认为 None |
| skipfooter | 接受一个列表，省略指定行数的数据，从尾部最后一行开始，默认为 0 |
| convert_float | 是否将浮点数转换为科学计数法，默认为 True |
| **kwds | 其他关键字参数 |
```python
# 读取Excel文件
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
print(df)
>>>    ID  Name  Age  City  Salary
0   1  Jack   28  Beijing   22000
1   2  Lida   32  Shanghai   19000
2   3  John   43  Shenzhen   12000
3   4  Helen   38  Hengshui    3500
```

通过 to_excel() 函数可以将 Dataframe 中的数据写入到 Excel 文件。

如果想要把单个对象写入 Excel 文件，那么必须指定目标文件名；如果想要写入到多张工作表中，则需要创建一个带有目标文件名的ExcelWriter对象，并通过sheet_name参数依次指定工作表的名称。

因为版本问题，建议安装openpyxl库：`pip install openpyxl`或`conda install openpyxl`。  


`pd.to_excel(excel_writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf', verbose=True)`
| 参数 | 说明 |
| --- | --- |
| excel_writer | 目标Excel文件路径或ExcelWriter对象 |
| sheet_name | 指定要写入数据的工作表名称，默认为 'Sheet1' |
| na_rep | 缺失值替换字符，默认为 '' |
| float_format | 浮点数格式，默认为 None |
| columns | 列名列表，指要写入的列，默认为 None |
| header | 是否写入列名，写出每一列的名称，如果给出的是字符串列表，则表示列的别名，默认为 True |
| index | 是否写入索引，默认为 True |
| index_label | 引用索引列的列标签。如果未指定，并且 hearder 和 index 均为为 True，则使用索引名称。如果 DataFrame使用 MultiIndex，则需要给出一个序列，默认为 None |
| startrow | 起始行，初始写入的行位置，默认值0。表示引用左上角的行单元格来储存 DataFrame。 |
| startcol | 起始列，初始写入的列位置，默认值0。表示引用左上角的列单元格来储存 DataFrame。 |
| engine | 它是一个可选参数，用于指定要使用的引擎，可以是 openpyxl 或 xlsxwriter，默认为 None |
| merge_cells | 是否合并单元格，默认为 True |
| encoding | 编码格式，默认为 None |
| inf_rep | 无穷大值替换字符，默认为 'inf' |
| verbose | 是否显示进度条，默认为 True |
```python
df = pd.DataFrame({'ID': [1, 2, 3, 4], 'Name': ['Jack', 'Lida', 'John', 'Helen'], 'Age': [28, 32, 43, 38], 'City': ['Beijing', 'Shanghai', 'Shenzhen', 'Hengshui'], 'Salary': [22000, 19000, 12000, 3500]})
df.to_excel('data.xlsx', sheet_name='Sheet1', index=False)
```

### Pandas绘图

Pandas 在数据分析、数据可视化方面有着较为广泛的应用，Pandas 对 Matplotlib 绘图软件包的基础上单独封装了一个plot()接口，通过调用该接口可以实现常用的绘图操作。本节我们深入讲解一下 Pandas 的绘图操作。

Pandas 之所以能够实现了数据可视化，主要利用了 Matplotlib 库的 plot() 方法，它对 plot() 方法做了简单的封装，因此您可以直接调用该接口。

Pandas 的 plot() 方法可以实现常见的绘图操作，包括折线图、散点图、直方图、饼图等。

`df.plot(kind='line', x=None, y=None, ax=None, subplots=False, sharex=None, sharey=False, layout=None, figsize=None, use_index=True, title=None, grid=None, legend=False, style=None, logx=False, logy=False, loglog=False, xticks=None, yticks=None, xlim=None, ylim=None, rot=None, fontsize=None, colormap=None, table=False, yerr=None, xerr=None, secondary_y=False, sort_columns=False, **kwds)`
其中，kind：图表类型，默认为 'line'；x：x轴数据，默认为 None；y：y轴数据，默认为 None；ax：指定绘图区域，默认为 None；subplots：是否创建子图，默认为 False；sharex：是否共享x轴，默认为 None；sharey：是否共享y轴，默认为 False；layout：子图布局，默认为 None；figsize：图形尺寸，默认为 None；use_index：是否使用索引，默认为 True；title：图表标题，默认为 None；grid：是否显示网格，默认为 None；legend：是否显示图例，默认为 False；style：线条样式，默认为 None；logx：是否对x轴进行对数变换，默认为 False；logy：是否对y轴进行对数变换，默认为 False；loglog：是否对x轴和y轴同时进行对数变换，默认为 False；xticks：x轴刻度，默认为 None；yticks：y轴刻度，默认为 None；xlim：x轴范围，默认为 None；ylim：y轴范围，默认为 None；rot：x轴刻度旋转角度，默认为 None；fontsize：字体大小，默认为 None；colormap：颜色映射，默认为 None；table：是否显示数据表，默认为 False；yerr：y轴误差范围，默认为 None；xerr：x轴误差范围，默认为 None；secondary_y：是否创建副y轴，默认为 False；sort_columns：是否对列进行排序，默认为 False；**kwds：其他关键字参数。

```python
# 绘制折线图
df = pd.DataFrame({'ID': [1, 2, 3, 4], 'Salary': [22000, 19000, 12000, 3500]})
df.plot(kind='line', x='ID', y='Salary', title='Salary by ID')
```
![折线图](/Notes/ML/imgage/line.png)

```python
# 绘制散点图
df = pd.DataFrame({'ID': [1, 2, 3, 4], 'Salary': [22000, 19000, 12000, 3500]})
df.plot(kind='scatter', x='ID', y='Salary', title='Salary by ID')
```
![散点图](/Notes/ML/image/scatter.png)

```python
# 绘制直方图
df = pd.DataFrame({'ID': [1, 2, 3, 4], 'Salary': [22000, 19000, 12000, 3500]})
df.plot(kind='hist', x='Salary', title='Salary Histogram')
```
![直方图](/Notes/ML/imgae/hist.png)

```python
# 绘制饼图
df = pd.DataFrame({'ID': [1, 2, 3, 4], 'Salary': [22000, 19000, 12000, 3500]})
df.plot(kind='pie', y='Salary', title='Salary by ID')
```
![饼图](/Notes/ML/imgae/pie.png)

```python
# 绘制箱线图
df = pd.DataFrame({'ID': [1, 2, 3, 4], 'Salary': [22000, 19000, 12000, 3500]})
df.plot(kind='box', y='Salary', title='Salary by ID')
```
![箱线图](/Notes/ML/image/box.png)

```python

# 绘制密度图
df = pd.DataFrame({'ID': [1, 2, 3, 4], 'Salary': [22000, 19000, 12000, 3500]})
df.plot(kind='area', y='Salary', title='Salary Density')
```
![密度图](/Notes/ML/image/area.png)






## Matplotlib(Matlab的Python版本)

## PIL(Python Imaging Library)

## SciPy(Scientific Python)

## Scikit-learn

## CSV库对文件的读写

```python
import csv
```
`csv.reader(csvfile, dialect='excel', **fmtparams)`  
读取CSV文件。其中，csvfile为CSV文件对象，dialect为CSV文件的格式，fmtparams为格式参数。
```python
# 读取CSV文件
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

`csv.writer(csvfile, dialect='excel', **fmtparams)`  
写入CSV文件。其中，csvfile为CSV文件对象，dialect为CSV文件的格式，fmtparams为格式参数。
```python
# 写入CSV文件
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'gender'])
    writer.writerow(['Alice', 25, 'female'])
    writer.writerow(['Bob', 30, 'male'])
```

`csv.DictReader(csvfile, fieldnames=None, restkey=None, restval=None, dialect='excel', **fmtparams)`  
读取CSV文件，将每行数据转换为字典。其中，csvfile为CSV文件对象，fieldnames为字段名列表，restkey为剩余字段名，restval为剩余字段值，dialect为CSV文件的格式，fmtparams为格式参数。
```python
# 读取CSV文件，将每行数据转换为字典
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```

`csv.DictWriter(csvfile, fieldnames, restval='', extrasaction='raise', dialect='excel', **fmtparams)`  
写入CSV文件，将字典数据写入CSV文件。其中，csvfile为CSV文件对象，fieldnames为字段名列表，restval为剩余字段值，extrasaction为处理额外字段的行为，dialect为CSV文件的格式，fmtparams为格式参数。
```python
# 写入CSV文件，将字典数据写入CSV文件
with open('data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age', 'gender'])
    writer.writeheader()
    writer.writerow({'name': 'Alice', 'age': 25, 'gender': 'female'})
    writer.writerow({'name': 'Bob', 'age': 30, 'gender':'male'})
```

## Links

- [NumPy官网](https://numpy.org/)
- [NumPy详解](https://blog.csdn.net/m0_74344139/article/details/134842295?ops_request_misc=&request_id=&biz_id=102&utm_term=Numpy%E8%AF%A6%E8%A7%A3&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1-134842295.142^v100^pc_search_result_base6&spm=1018.2226.3001.4187)
- [Pandas教程](https://c.biancheng.net/pandas)