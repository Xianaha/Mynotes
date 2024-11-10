# Python语法

## 关键字

### pass
pass 是一个空操作语句，用于表示程序控制流中的“什么都不做”的情况。pass 通常用作占位符，以便在某些情况下保持代码结构的完整性。它没有任何效果，仅仅是为了让代码逻辑上完整，避免语法错误。

#### 作用
- 占位符  
在定义函数、类或条件语句时，pass 可以在计划实现某些功能时占位，以便后续填充逻辑。
```python
def my_function():
    pass  # 暂时不实现任何功能

class MyClass:
    pass  # 暂时不添加任何属性或方法
```

- 空循环或空条件  
在某些情况下，你可能需要一个空循环或空的条件语句，使用 pass 可以避免IndentationError。
```python
for i in range(10):
    pass  # 占位，暂时不处理每个元素

if condition:
    pass  # 占位，暂时不执行任何操作
```

- 在异常捕获中  
当捕获到某个异常时，可以选择不做任何处理，也可以用 pass 来空着该异常处理块。
```python
try:
    # 可能会抛出异常的代码
    result = 10 / 0
except ZeroDivisionError:
    pass  # 捕获异常而不做处理

```
### nonlocal
nonlocal关键字用于在嵌套函数中声明变量，指示该变量是来自外部函数的作用域，而不是全局作用域。简单来说，当我们在一个内部函数中想要修改外部函数（不是全局）的局部变量时，我们可以使用nonlocal。

#### 作用
- 声明在嵌套作用域中引用的变量  
在嵌套作用域中，nonlocal 关键字用于声明该变量是来自外部函数的作用域，并使得内部函数可以访问它。
```python
def outer():
    y = 20
    def inner():
        nonlocal y
        y += 10
        print(y)
    inner()
    print(y)

outer()
>>> 30
20
```

### global
global关键字用于在函数内部修改全局变量。

#### 作用
- 修改全局变量  
在函数内部，global 关键字用于修改全局变量。
```python
x = 10

def my_function():
    global x
    x += 10
    print(x)

my_function()
>>> 20
```


### del
del 关键字用于删除对象。

#### 作用
- 删除对象  
del 关键字用于删除对象，包括变量、列表、元组、字典等。
```python
x = 10
y = [1, 2, 3]

del x
del y[1]

print(x) # 输出结果为NameError: name 'x' is not defined
print(y) # 输出结果为[1, 3]
```

### is
is 关键字用于比较两个对象是否相同。is 是身份运算符，用于判断两个对象的身份（内存地址）是否相同。与 == 不同， 后者比较的是对象的值。

#### 作用
- 判断对象是否相同  
is 关键字用于判断两个对象是否相同。
```python
a = 10
b = 10
print(a is b) # 输出结果为True
c = b # 两个变量指向同一个对象,c 引用了 b
print(a is b) # 输出结果为True
print(c is b) # 输出结果为True

c = 20 # 重新赋值，b 与 c 不再指向同一个对象，c 指向了一个值为 20 的对象
print(c is b, b, c) # 输出结果为False 10 20

d = b # 再次赋值，d 引用了 b
print(d is b) # 输出结果为True
d += 10 # 对 d 进行操作，d 重新指向一个值为 b + 10 的对象
print(d is b, b, d) # 输出结果为False 10 20

e = a # 再次赋值，e 引用了 a
a += 10 # 对 a 进行操作，a 重新指向一个值为 a + 10 的对象
print(e is a, a, e) # 输出结果为False 20 10

```

### in
in 关键字用于判断某个对象是否存在于某个序列中，例如字符串、列表、元组、集合和字典等。
在使用 in 关键字时，如果对象存在于序列中，则返回 True，否则返回 False。
在使用 in 关键之前，需要确保序列中包含该对象的数据类型，否则会报错。例如，字符串中不包含数字，所以在字符串中使用 in 关键字时会报错。

#### 作用
- 判断对象是否存在于序列中  
in 关键字用于判断某个对象是否存在于某个序列中。
```python
a = 10
b = [1, 2, 3]
c = (1, 2, 3)
d = {1, 2, 3}
e = "hello world"

print(a in b) # 输出结果为False
print(a in c) # 输出结果为False
print(a in d) # 输出结果为False
print(a in e) # TypeError: 'in <string>' requires string as left operand, not int

1 in b # 输出结果为True
1 in c # 输出结果为True
1 in d # 输出结果为True
1 in e # TypeError: 'in <string>' requires string as left operand, not int

2 in b # 输出结果为True
2 in c # 输出结果为True
2 in d # 输出结果为True
2 in e # TypeError: 'in <string>' requires string as left operand, not int

"l" in e # 输出结果为True
"l" in b # 输出结果为False
"l" in c # 输出结果为False
"l" in d # 输出结果为False

```





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

all()
在Python中，`all()` 是一个内置函数，用于判断可迭代对象中的所有元素是否都是 `True`。只要可迭代对象中有一个元素为 `False`，`all()` 就会返回 `False`；如果可迭代对象为空，它会返回 `True`。

语法：all(iterable)
`iterable`：一个可迭代对象，例如列表、元组、集合、字典等。
返回 `True` 如果 `iterable` 中的所有元素为 `True`，否则返回 `False`。

基本用法：
print(all([True, True, True]))  # 输出: True
print(all([True, False, True]))  # 输出: False
print(all([]))  # 输出: True (空可迭代对象)

在 Python 中，0 被认为是 `False`，非零值被认为是 `True`。
print(all([1, 2, 3]))  # 输出: True
print(all([1, 0, 3]))  # 输出: False
print(all([0, 0, 0]))  # 输出: False

非空字符串被认为是 `True`。
print(all(['hello', 'world']))  # 输出: True
print(all(['hello', '']))        # 输出: False
print(all(['', '']))              # 输出: False

结合生成器表达式
可以与生成器表达式一起使用，检查某些条件是否都满足。
numbers = [1, 2, 3, 4]

检查所有数字是否都大于 0
print(all(n > 0 for n in numbers))  # 输出: True

检查是否所有数字都是偶数
print(all(n % 2 == 0 for n in numbers))  # 输出: False

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

chr()
chr(65) # 将整数转换为对应的ASCII字符。
# 将整数转换为对应的ASCII字符。

ord()
ord("A") # 将ASCII字符转换为对应的整数。
# 将ASCII字符转换为对应的整数。

hex()
hex(255) # 将整数转换为对应的十六进制字符串。
# 将整数转换为对应的十六进制字符串。

oct()
oct(255) # 将整数转换为对应的八进制字符串。
# 将整数转换为对应的八进制字符串。



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

## 位运算
### 与运算（&）
只有两个位都是1时，结果才是1。

```python
a = 0b1010
b = 0b1100
c = a & b
print(c) # 输出结果为1000
```

### 或运算（|）
只要两个位有一个是1，结果就是1。

```python
a = 0b1010
b = 0b1100
c = a | b
print(c) # 输出结果为1110
```

### 异或运算（^）
两个位都不同时，结果才是1；两个位相同时，结果就是0。

```python
a = 0b1010
b = 0b1100
c = a ^ b
print(c) # 输出结果为0110
```

### 取反运算（~）
对每个位取反，即0变1，1变0。

```python
a = 0b1010
b = ~a
print(b) # 输出结果为-1101
```

### 左移运算（<<）
将数字的二进制形式向左移动指定的位数。

```python
a = 0b1010
b = a << 2
print(b) # 输出结果为0b101000
```

### 右移运算（>>）
将数字的二进制形式向右移动指定的位数。

```python
a = 0b1010
b = a >> 2
print(b) # 输出结果为0b0010
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

   ```python
   # 可以指定参数的类型。：后面跟着参数类型，->后面跟着返回值类型。
   def add(x: int, y: int) -> int:
       return x + y

   # 可以在在参数列表中指定默认值。如果不对参数赋值，则使用默认值。
   def add(x, y=1):
       return x + y

   # 可以在参数列表中指定可变参数。单个星号将一组可变数量的位置参数组合成参数值的元组。在函数内部可以通过访问元组中的每个元素来使用参数。
   def add(*args):
       return sum(args)

   def m_value(*values):
       max_value = max(values)
       min_value = min(values)
       print(f'最大值: {max_value}, 最小值: {min_value}')
   m_value(8, 6, 7, 4, 3, 9)
   >>> 最大值: 9, 最小值: 3


   # 可以在参数列表中指定关键字参数。针对形参的关键字参数赋值形式， 利用 Python 定义函数时， 在形参前面加上双星号**来定义收集关键字参数的形参。此时形参是字典类型。
   def add(**kwargs):
       return sum(kwargs.values())

   def f(**info):
   if 'name' not in info.keys():
       print('必须拥有名称信息。')
   else:
       print(info['name'] + '的诞生年份：' + info.get('time', '不详'))

   f(name = 'C', time = '1972')
   >>> C的诞生年份：1972
   f(name = 'Python')
   >>> Python的诞生年份：不详


   # Python函数传入的都是引用，因此可以修改函数内部的变量值。
   def change_value(x):
       x = 2
       print(x)
   a = 1
   change_value(a)
   print(a) # 输出结果为2，函数内部的变量值被修改。

   ```
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
>>>  5 # 列表长度
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
>>> [1, 3, 5, 2, 'qwa', 'c', 3]

# 运算符*会使该列表前后拼接n倍
n = 3
temp3 = temp2 * n
temp3
>>> [2, 'qwa', 'c', 3, 2, 'qwa', 'c', 3, 2, 'qwa', 'c', 3]

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
>>> [{'price': 10.5}, {'price': 15}, {'price': 24}]

#copy函数用于创建列表的副本。创建副本和赋值是不一样的，创建副本会于new一个新对象，而赋值只是&。
temp3.copy(temp1)

#index函数用于返回所匹配的元素的索引。该函数的第一个参数是待查找的对象，第二个参数是查找的起始范围，第三个参数是查找的结束范围(左闭右开)。
res_index = temp.index(查找元素值, 查找起始索引值， 查找末尾索引值)

#count函数用于统计某个元素在列表中出现的次数。
res_count = temp.count(查找元素值)
```

### 字符串

#### 性质

类型为str。
线性存储，通过下标访问，但不可修改！
可以对字符串进行重新构建以达成修改的目的：
```python
s = "hello world"
s = s + "!"
s
>>> "hello world!"
# 这里通过重新赋值或拼接的方式生成了新的字符串s。
```
支持切片。

```python
str(object=) # 将对象转换为字符串。
str(['a', 'b', 'c']) # 将列表转换为字符串
>>> "['a', 'b', 'c']"

str(3.1415926) # 将浮点数转换为字符串。
>>> "3.1415926"

str(100) # 将整数转换为字符串。
>>> "100"
```

#### 声明

```python
# 单引号和双引号都可以用来声明字符串。
str1 = 'hello world'
str2 = "hello world"
```

#### 常用方法

切片：

```python
str0[start:end:step] # start:end为切片的起止位置（左闭右开区间），step为步长，默认为1。
#例如：
str0 = "hello world"
str0[1:3] # 切片"el"
str0[1:3:2] # 切片"e"，步长为2

# 反转字符串
str0[::-1] # 切片[::-1]，步长为-1，即反转字符串。

str0[: : -1]
>>> "dlrow olleh"
```

```python
# 运算符+会使两个字符串前后拼接
str1 = "hello"
str2 = "world"
str3 = str1 + " " + str2
str3
>>> "hello world"

# 运算符*会使该字符串前后拼接n倍
n = 3
str3 = str3 * n
str3
>>> "hello worldhello worldhello world"

str.lower()
# 将字符串转换为小写，返回新的字符串。

str.upper()
# 将字符串转换为大写，返回新的字符串。

str.strip()
# 去除字符串两端的空格，返回新的字符串。

str.lstrip()
# 去除字符串左边的空格，返回新的字符串。

str.rstrip()
# 去除字符串右边的空格，返回新的字符串。

str.capitalize()
# 首字母大写，其他字母小写，返回新的字符串。

str.title()
# 单词首字母大写，其他字母小写，返回新的字符串。

str.isalnum()
# 检查字符串是否由字母和数字组成。返回True或False。

str.isalpha()
# 检查字符串是否只由字母组成。返回True或False。

str.isdigit()
# 检查字符串是否只由数字组成。返回True或False。

str.find(sub, start=0, end=len(str))
# 其中sub表示需要查找的字符串，start表示查找的起始位置，end表示查找的结束位置。
# 返回子串的第一个位置，如果没有找到，则返回-1。
text = "hello world"
position = text.find("world")
position
>>> 6

str.rfind(sub, start=0, end=len(str))
# 与find函数类似，但从右边开始查找。

str.count(sub, start=0, end=len(str))
# 计算子串在字符串中出现的次数。

str.startswith(prefix, start=0, end=len(str))
# 检查字符串是否以指定子串开头。返回True或False。

str.endswith(suffix, start=0, end=len(str))
# 检查字符串是否以指定子串结尾。返回True或False。

str.split(sep=None, maxsplit=-1)
# 按照指定分隔符将字符串分割成多个子串，返回一个列表。
# sep表示分隔符，默认为None，表示不指定分隔符。
# maxsplit表示最大分割次数，默认为-1，表示分割所有。

str.join(iterable)
# 将序列iterable中的元素以当前字符串为分隔符，连接成一个新的字符串。
lst = ["hello", "world"]
str1 = ",".join(lst)
str1
>>> "hello,world"

str.replace(old, new, count=-1)
# 将字符串中的old替换为new，返回替换后的字符串。
# count表示替换次数，默认为-1，表示全部替换。
str0 = "hello world"
str1 = str0.replace("l", "L")
str1
>>> "heLLo world"

str.splitlines()
# 按照换行符将字符串分割成多个子串，返回一个列表。
# 如果没有找到换行符，则返回一个包含整个字符串的列表。
str0 = "hello\nworld"
str1 = str0.splitlines()
str1
>>> ['hello', 'world']

join()
# 与split()函数相反，join()函数用于将序列iterable中的元素以当前字符串为分隔符，连接成一个新的字符串。
lst = ["hello", "world"]
str1 = "-".join(lst)
str1
>>> "hello-world"

partition()
# 按照子串出现的位置将字符串分割成三部分，返回一个元组。
# 元组的第一个元素是分割出的第一个子串，第二个元素是分割出的第二个子串，第三个元素是分割出的第三个子串。
# 如果没有找到子串，则返回一个空元组。
str0 = "hello world"
str1 = str0.partition("l")
str1
>>> ('he', 'l', 'lo world')


# 字符串的格式化
# 字符串的格式化可以用%运算符实现，其语法格式如下：
"%[format_code] [argument]...".
# 其中，format_code表示格式代码，argument表示要格式化的对象。
# 常见的格式代码有：
# %s 字符串（字符串对象）
# %d 整数（整数对象）
# %f 浮点数（浮点数对象）
# %x 十六进制整数（整数对象）
# %o 八进制整数（整数对象）
# %e 指数（浮点数对象）
# %g 通用浮点数（浮点数对象）
# %c 单个字符（字符串对象）
# %r 任意对象（任意对象）

# 字符串的格式化还可以指定格式化符号，如：
# 1. 字符串宽度
# 2. 字符串精度
# 3. 字符串对齐方式
# 4. 字符串填充字符
# 5. 数字的进制表示
# 6. 数字的千位分隔符
# 7. 数字的显示方式
# 8. 日期和时间的格式化
# 9. 字符串的编码方式
# 10. 字符串的转义字符

# 字符串的格式化示例：
age = 20
name = "张三"
print("我的名字是%s，今年%d岁了。" % (name, age))
# 输出结果：我的名字是张三，今年20岁了。

# 字符串的格式化还可以指定填充字符、对齐方式、宽度等。
# 填充字符：
print("%05d" % 123)
# 输出结果：000123

# 对齐方式：
print("%-5d" % 123)
# 输出结果：123  
print("%5d" % 123)
# 输出结果：  123

# 宽度：
print("%5d" % 123)
# 输出结果：  123
print("%05d" % 123)
# 输出结果：000123

# 格式化字符串的使用示例：
name = "张三"
age = 20
score = 80
print("我的名字是%s，今年%d岁了，成绩是%.2f分。" % (name, age, score))
# 输出结果：我的名字是张三，今年20岁了，成绩是80.00分。




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
>>>  <class 'tuple'>
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
key可以是任意的数据类型,但不能出现可变的数据类型,保证key唯一。字典的key可以是数字、字符串、元组等任意不可变类型，但不能是可变类型，如列表、字典等。
key一般形式为字符串。

#### 声明

```python
dict = {"nane": "张三", "age": 20, "sex": "男"}

# 嵌套字典形成多层字典结构

persons = {
    'person1': {'name': 'Alice', 'age': 25},
    'person2': {'name': 'Bob', 'age': 30}
}


students = {
    "ZhangSan" : {
        "name": "张三",
        "age": 20,
        "sex": "男"
        "courses" : {
            "Python": {
                "teacher": "老师A",
                "score": 90
            },
            "Java": {
                "teacher": "老师B",
                "score": 85
            }
        }
    },
    "LiSisi" : {
        "name" : "李思思",
        "age": 21,
        "sex": "女"
        "courses" : {
            "C++": {
                "teacher": "老师C",
                "score": 80
            },
            "C": {
                "teacher": "老师D",
                "score": 75
            }
        }
    }
}

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
>>> dict_items([('name', '张三'), ('age', 20), ('sex', '男')])

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
>>> (0, 'name')
(1, 'age')
(2, 'sex')

# 判断字典中是否存在某个Key
key_name in dict.keys()

# 判断字典中是否存在某个Value
value in dict.values()
```

### 集合

#### 性质
- 无序：集合中的元素没有固定顺序。  
- 不重复：集合中的元素不能重复，添加重复元素时，集合只会保留一个。
#### 声明

```python
# 使用花括号创建集合
my_set = {1, 2, 3, 4}

# 使用set()函数创建集合
my_set2 = set([1, 2, 3, 4])

```

#### 常用方法

```python
# set()类型转换，将其他数据结构转换为集合形式以达到去重效果
list1 = [1, 4, 5, 1, 4, 5]
s1 = set(list1)
s1
>>> {1, 4, 5}

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
