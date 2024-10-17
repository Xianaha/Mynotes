# Python语法

## 基本方法

```python

.format()
"{} {}".format("hello", "world") # 格式化字符串。
# 格式化字符串，用{}包裹的变量会被替换为format()函数的后续参数。

range(start, stop, step)
range(5) # 创建一个整数序列，从0开始，到4结束，步长为1。
range(1, 5) # 创建一个整数序列，从1开始，到4结束，步长为1。
range(1, 5, 2) # 创建一个整数序列，从1开始，到4结束，步长为2。
# 创建一个整数序列，从start开始，到stop结束，步长为step。

len()
len(str) # 计算字符串或列表的长度。
# 计算字符串或的长度。

.count()
str.count("o") # 计算字符串中某个字符出现的次数。
# 计算字符串中某个字符出现的次数。

.find()
str.find("o") # 查找字符串中某个字符的位置。
# 查找字符串中某个字符的位置。

.index()
str.index("o") # 查找字符串中某个字符的位置。
# 查找字符串中某个字符的位置。

map()
map(func, seq) # 将函数func作用在序列seq的每个元素上，并返回一个新的序列。
# 用于将一个函数作用在一个序列的每个元素上，并返回一个新的序列。

.mean()
lst.mean() # 计算列表的平均值。
# 计算列表的平均值。

sum()
sum(lst) # 计算列表元素的和。
# 计算列表元素的和。

.split()
str.split(",") # 按逗号分割字符串。
# 将字符串拆分成一个列表。默认情况下，它会根据空格进行拆分，但你也可以指定其他分隔符。

.strip()
# 去除字符串两端的空格。

.join()
lst.join(str) # 将列表中的元素用指定字符连接成一个字符串。
# 将列表中的元素用指定字符连接成一个字符串。

.replace()
str.replace("old", "new") # 将字符串中的old替换为new。
# 替换字符串中的指定子串。

.lower()
str.lower() # 将字符串转换为小写。
# 将字符串转换为小写。

.upper()
str.upper() # 将字符串转换为大写。
# 将字符串转换为大写。

.sort()
lst.sort() # 对列表进行排序。默认情况下，它会按升序排列；如果指定reverse=True，则按降序排列。
# 对列表进行排序。
```

## 条件语句

## 循环语句

## 函数

### 结构

```python
def 函数名(参数列表):
    函数体
    return 返回值
```

1. 函数名：函数的名称，可以自定义。
2. 参数列表：函数的参数，可以有多个参数，参数之间用逗号隔开。
3. 函数体：函数的主体，可以包含多个语句。
4. 返回值：函数的返回值，可以有多个返回值，返回值之间用逗号隔开。

### 性质
对于形参值或地址的传递，与C、C++类似。
实参与形参按照从左到右的位置顺序依次赋值。
为了避免位置参数赋值带来的混乱，Python 允许调用函数时通过关键字参数的形式指定形参与实参的对应关系。 调用者使用name=value的形式来指定函数中的哪个形参接受某个值。
在函数定义时，可以为参数指定值。这样当函数调用者没有提供对应参数值时，就可以使用指定的默认值。

Python 允许在定义函数时使用单星号*来收集位置参数，双星号**收集关键字参数。
单个星号将一组可变数量的位置参数组合成参数值的元组。在函数内部可以通过访问元组中的每个元素来使用参数。

```python
def m_value(*values):
    max_value = max(values)
    min_value = min(values)
    print(f'最大值: {max_value}, 最小值: {min_value}')
m_value(8, 6, 7, 4, 3, 9)
# 最大值: 9, 最小值: 3

#针对形参的关键字参数赋值形式， 利用 Python 定义函数时， 在形参前面加上双星号**来定义收集关键字参数的形参。此时形参是字典类型。
def f(**info):
    if 'name' not in info.keys():
        print('必须拥有名称信息。')
    else:
        print(info['name'] + '的诞生年份：' + info.get('time', '不详'))

f(name = 'C', time = '1972')
# C的诞生年份：1972
f(name = 'Python')
# Python的诞生年份：不详
```


## 数据结构

### 列表

#### 性质

类型为list。
元素类型可以不相同。
线性随机存取，通过下标访问。
支持切片。

```python
temp[-1]
--> 5 # 列表长度
```

#### 声明

```python
temp = [1, "qwe", 'c' 5, 6]
```

#### 列表推导式

列表推导是Python中的高级用法，其原理和for循环类似，但是写法上更加简洁，并且有返回值。
列表推导式也可以接外部函数。
#条件成功即将迭代对象赋给返回对象，所有返回对象组成一个列表。其中条件恒成立时可以省去if和条件
```python
temp = [返回对象 for 迭代对象 in 遍历对象  if 条件]
temp = [方法(返回对象) for 迭代对象 in 遍历对象 if 条件]
```

#### 常用方法

切片：
```python
temp[start:end:step] # start:end为切片的起止位置（左闭右开区间），step为步长，默认为1。
#例如：
temp[1:3] # 切片[1, 2]
temp[1:3:2] # 切片[1, 3]，步长为2
```

```python
# 运算符+会使两个列表前后拼接
temp1 = [1, 3, 5]
temp2 = [2, "qwa",  'c', 3]
temp3 = temp1 + temp2
temp3
-->[1, 3, 5, 2, 'qwa', 'c', 3]

# 运算符*会使该列表前后拼接n倍
n = 3
temp3 = temp2 * n
temp3
-->[2, 'qwa', 'c', 3, 2, 'qwa', 'c', 3, 2, 'qwa', 'c', 3]

list()
list(range(1, 11)) # 将range对象转换为列表
# 该函数可以将元组、字符串、字典转换为列表。

# append函数用于向列表末尾添加元素。该函数没有返回值，它只是修改了当前列表。
temp.append(元素值)

# clear函数用于将列表清空。
temp1.clear()

#删除该列表第四个元素，列表长度-1，后面的元素前移。
del temp[3]

# extend函数用于在列表的末尾添加另一个列表，与append函数相比，extend函数可以一次性添加多个元素。使用extend函数和列表加法的结果是一样的，但是extend函数会将另一个列表并入当前列表，而列表加法是返回新的列表，为节约内存空间，更推荐使用extend函数来实现大列表的连接操作。
temp1.extend(temp2)

# insert函数用于向列表中插入元素。该函数没有返回值，而是直接将元素插入当前列表, 原索引及其之后的元素将后移。insert函数的第一个参数是插入位置的索引，第二个参数是要插入的对象。
temp.insert(索引值, 元素值)

# remove函数用于从列表移除元素。该函数没有返回值，直接操作原列表。若列表中有重复元素，remove函数只会移除匹配到的第一个。
temp.remove(元素值)

# pop函数用于移除列表中指定位置的元素，并返回要移除的元素，移除之后，该索引之后的元素将前移。在默认情况下，移出列表中最后一个元素。
res = temp1.pop(索引值)
res = temp1.pop()

# reverse函数用于将列表反向排列。
temp1.reverse()

# sort函数用于将列表进行排序。如下，在默认情况下，sort函数会将列表进行升序排列。待排序的列表元素类型是字典，需要根据字典的键来排序，就要使用key参数。key参数后面是一个lambda表达式，这是一个函数对象，该函数对象返回了item[“price”]，那么sort函数就会使用item[“price”]来进行排序。
temp1.sort()     #升序
temp1.sort(reverse = True)     #降序
temp3 = [{"price":10.5},{"price":24},{"price":15}]
temp3.sort(key=lambda item:item["price"])
temp3
-->[{'price': 10.5}, {'price': 15}, {'price': 24}]

#copy函数用于创建列表的副本。创建副本和赋值是不一样的，创建副本会于new一个新对象，而赋值只是&。
temp3.copy(temp1)

#index函数用于返回所匹配的元素的索引。该函数的第一个参数是待查找的对象，第二个参数是查找的起始范围，第三个参数是查找的结束范围(左闭右开)。
res_index = temp.index(查找元素值, 查找起始索引值， 查找末尾索引值)

#count函数用于统计某个元素在列表中出现的次数。
res_count = temp.count(查找元素值)
```

### 元组

#### 性质
由一系列按特定顺序排序的元素组成。

元组和列表（list）的不同之处在于：

列表的元素是可以更改的，包括修改元素值，删除和插入元素，所以列表是可变序列；
而元组一旦被创建，它的元素就不可更改了，所以元组是不可变序列。
元组也可以看做是不可变的列表，通常情况下，元组用于保存无需修改的内容。

从形式上看，元组的所有元素都放在一对小括号( )中，相邻元素之间用逗号,分隔，如下所示：
(element1, element2, ... , elementn)

其中 element1~elementn 表示元组中的各个元素，个数没有限制，只要是 Python 支持的数据类型就可以。

从存储内容上看，元组可以存储整数、实数、字符串、列表、元组等任何类型的数据，并且在同一个元组中，元素的类型可以不同，例如：
("c.biancheng.net", 1, [2,'a'], ("abc",3.0))

在这个元组中，有多种类型的数据，包括整形、字符串、列表、元组。

另外，我们都知道，列表的数据类型是 list，那么元组的数据类型是什么呢？我们不妨通过 type() 函数来查看一下：
```python
type( ("c.biancheng.net",1,[2,'a'],("abc",3.0)) )
--> <class 'tuple'>
```

#### 声明
```python
# 使用 ( ) 直接创建
# 通过( )创建元组后，一般使用=将它赋值给某个变量，具体格式为：
tuplename = (element1, element2, ..., elementn)
#其中，tuplename 表示变量名，element1 ~ elementn 表示元组的元素。
num = (7, 14, 21, 28, 35)
course = ("Python教程", "http://c.biancheng.net/python/")
abc = ( "Python", 19, [1,2], ('c',2.0) )
# 在 Python 中，元组通常都是使用一对小括号将所有元素包围起来的，但小括号不是必须的，只要将各元素用逗号隔开，Python 就会将其视为元组，请看下面的例子：
course = "Python教程", "http://c.biancheng.net/python/"
#需要注意的一点是，当创建的元组中只有一个字符串类型的元素时，该元素后面必须要加一个逗号,，否则 Python 解释器会将它视为字符串。

# 使用tuple()函数创建元组
# 除了使用( )创建元组外，Python 还提供了一个内置的函数 tuple()，用来将其它数据类型转换为元组类型。
# tuple() 的语法格式如下：
tuple(data)
#其中，data 表示可以转化为元组的数据，包括字符串、元组、range 对象等。
```

#### 常用方法
```python
tuple1.count(元素值)
# 计算元组中某个元素出现的次数。

tuple1.index(元素值)
# 返回元组中某个元素的索引。
```

### 字典

#### 性质
字典是另一种可变容器模型,可存储任意类型对象。如字符串、数字、元组等其他容器模型
因为字典是无序的所以不支持索引和切片。
key不可以重复,否则只会保留第一个;
value值可以重复;
key可以是任意的数据类型,但不能出现可变的数据类型,保证key唯一;
key一般形式为字符串。

#### 声明
```python
dict = {"nane": "张三", "age": 20, "sex": "男"}
```

#### 常用方法
```python
# 向字典中加入新Key-Value对。
# 字典名[new key]=new value
dict["score"] = 100

# 删除字典中某对Key-Value。
del 字典名[key]
del dict["name"]

# 查找字典中某Key的Value。
value=字典名[key]
value=dict["sex"]

# 更改字典中某Key的Value
字典名[key]=new_value
dict["name"]="李四"

# 清空字典
dict.clear()

# len函数返回该字典的键值对个数。
dict.len()

# keys函数会返回一个列表包含这个字典的所有Key。
list1 = dict.keys()

# values函数会返回一个列表包含这个字典的所有Value。
list1 = dict.values()

# items函数返回包含每个键值对的元组的列表
dict = {"name": "张三", "age": 20, "sex": "男"}
list1 = dict.items()
list1
-->dict_items([('name', '张三'), ('age', 20), ('sex', '男')])

# 字典名[key]会返回该Key对应的Value值
value1 = dict["age"]

# setdefault函数
# 如果key值存在,那么返回对应字典的value,不会用到自己设置的value;
# 如果key值不存在.返回None,并且把新设置的key和value保存在字典中;
# 如果key值不存在,但设置了value,则返回设置的value;
dict.setdefault(key,value)

# get函数
# 如果key值存在,那么返回对应字典的value,不会用到自己设置的value;
# 如果key值不存在.返回None,但是不会把新设置的key和value保存在字典中;
# 如果key值不存在,但设置了value,则返回设置的value;
dict.get(k,value)

# enumerate函数
# 返回字典的Key，以Key的顺序为索引的元组形式返回。
enumerate(字典名)
for i in enumerate(dict):
    print(i)
-->(0, 'name')
(1, 'age')
(2, 'sex')

# 判断字典中是否存在某个Key
key_name in dict.keys()

# 判断字典中是否存在某个Value
value in dict.values()
```

### 集合

#### 性质

#### 声明

```python
s = {1,2,4,5}
```

#### 常用方法

```python
# set()类型转换，将其他数据结构转换为集合形式以达到去重效果
list1 = [1, 4, 5, 1, 4, 5]
s1 = set(list1)
s1
--> {1, 4, 5}

# 判断
des in 集合名

# update函数更新整个集合，把第二个集合插入第一个集合中
set1.update(set2)

# add函数可以向集合中插入一个值
set1.add(插入元素值)

# del 关键字用来删除集合，集合不存在。
del set1

# clear函数用来清空整个集合，集合还存在但不存在元素。
set1.clear()

# discard函数用来删除指定元素
set1.discard(待删除的元素值)

# remove函数用来移除指定元素
set1.remove(待移除的元素值)

# pop函数用来弹出最靠前的元素的值
value = set1.pop()

#集合存在以下运算符
`&`运算符表示交集运算  `set1 & set2`
`|`运算符表示并集运算  `set1 | set2`
`-`运算符表示差集运算  `set1 - set2`
`^`运算符表示对称差运算  `set1 ^ set2`
```