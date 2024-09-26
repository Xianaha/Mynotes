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








## Pandas



## Matplotlib(Matlab的Python版本)

## PIL(Python Imaging Library)

## SciPy(Scientific Python)

## Scikit-learn

## CSV文件的读写

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