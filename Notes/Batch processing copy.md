# Batch processing
批处理是指将一系列的操作自动化地执行，并将结果输出到文件中，以便后续处理。批处理的优点是可以节省人力，提高工作效率。批处理的实现方法有很多，常见的有命令行、脚本、任务计划程序、服务器任务、应用程序等。
## os
Python 提供了一个 os 模块，可以用来处理文件和目录。
```python
import os
```

### 列出目录中的文件

`os.listdir(path)` 
可以列出指定目录中的文件和目录。返回值是一个列表，包含目录中所有的文件和目录的名称。
```python
files = os.listdir(path)
```

### 对文件路径进行操作

`os.path.split(path, sep=None)` 
可以将文件名分割成目录名和文件名。其中，path 是文件路径，sep 是分隔符，默认为 os.sep。
```python
file = "D:\Code\VScode_Python\Test\K-NN.py"
dirname, filename = os.path.split(file)
dirname, filename
>>> ('D:\\Code\\VScode_Python\\Test', 'K-NN.py')
```

`os.path.splitext(path, sep=None)` 
可以分割文件名和扩展名。其中，path 是文件路径。
```python
file = "D:\Code\VScode_Python\Test\K-NN.py"
filename, ext = os.path.splitext(file)
filename, ext
>>> ('D:\\Code\\VScode_Python\\Test\\K-NN', '.py')

file = "K-NN.ipynb"
filename, file_extension = os.path.splitext(file)
filename, file_extension
>>> ('K-NN', '.ipynb')
```

`os.path.join(path, *paths)` 
可以将多个路径组合成一个路径。其中，path 是第一个路径，paths 是其他路径。
```python
path = os.path.join('D:\Code\VScode_Python\Test', 'K-NN.py')
path
>>> 'D:\\Code\\VScode_Python\\Test\\K-NN.py'
```

`os.path.exists(path)` 
可以判断文件或目录是否存在。
```python
if os.path.exists(path):
    # 文件或目录存在
else:
    # 文件或目录不存在
```

`os.path.isfile(path)` 
可以判断是否为文件。
```python
if os.path.isfile(path):
    # 是文件
else:
    # 不是文件
```

`os.path.isdir(path)` 
可以判断是否为目录。
```python
if os.path.isdir(path):
    # 是目录
else:
    # 不是目录
```

`os.path.getsize(path)` 
可以获取文件大小（以字节为单位）。
```python
size = os.path.getsize(path)
>>> 123456
```

### 对文本进行操作

`with` 语句可以自动关闭文件。其有以下功能：
- **自动管理资源**：使用`with`语句可以确保在代码块执行完毕后，相关的资源（如文件）会自动关闭，而不需要显式调用close()方法。这避免了因忘记关闭资源而导致的内存泄漏或文件占用问题。
- **异常处理**：如果with语句中的代码块发生异常，with语句能够保证资源的正确释放，即使发生错误也能够执行相应的清理操作。
- **简化代码**：with语句的使用使得代码更简洁、可读性更高，避免了冗长的try...finally结构。    

`open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)` 
可以打开一个文件，并返回一个文件对象。其中，file 是文件路径，mode 是打开模式（包括读、写、追加等，分别用'r'、'w'、'a'表示），buffering 是缓冲区大小，encoding 是编码格式，errors 是错误处理方式，newline 是换行符，closefd 是一个布尔值，如果为 True，则关闭文件描述符，opener 是一个可选参数，用于指定打开文件的函数。

```python
with open(file, mode) as f:
    # 对文件进行操作
```

### 读取文件内容

`file.endswith(suffix)` 
可以判断文件名是否以指定后缀结尾。
```python
if file.endswith('.txt'):
    # 对文本文件进行操作
```

`file.startswith(prefix)` 
可以判断文件名是否以指定前缀开头。
```python
if file.startswith('abc_'):
    # 对以 abc_ 开头的文件进行操作
```


`f.read()` 
读取文件中所有内容。返回值是一个字符串。
```python
with open(file, mode) as f:
    content = f.read()
```

`f.readlines()` 
可以读取文件内容，并按行分割。返回值是一个列表，包含文件中的每一行(在列表中以字符串的形式存储)。
```python
with open(file, mode) as f:
    lines = f.readlines()
```

### 写入文件内容

`f.write(string)` 
可以向文件写入内容。其中，string 是要写入的字符串。
```python
with open(file, mode) as f:
    f.write(string)
```


### 获取目录及其目录下的文件

`os.walk(top, topdown=True, onerror=None, followlinks=False)` 
可以遍历目录及其子目录。返回值是一个生成器，每个元素是一个三元组，包含当前目录路径、目录列表、文件列表。会递归所有子目录及其文件直至遍历完整个目录树。其中root 是当前目录的路径，dirs 是当前目录中的子目录列表，files 是当前目录中的文件列表。
```python
for root, dirs, files in os.walk(top):
    # 对目录及其子目录进行操作
```

### 创建目录

`os.mkdir(path)` 
可以创建目录。
```python
os.mkdir(path)
```

### 删除目录

`os.rmdir(path, ignore_errors=False)` 
只能删除空目录。其中，path 是要删除的目录的路径，ignore_errors 是一个可选参数，默认为 False。如果 ignore_errors 为 False，并且目录中有文件或者子目录，则抛出 OSError 异常。如果 ignore_errors 为 True，则忽略异常。
```python
os.rmdir(path)
```

`os.removedirs(path, ignore_errors=False)`
可以递归删除指定路径及其所有父目录（如果他们为空），以便清理文件系统中不必要的目录。
```python
os.removedirs(path)
```

### 删除文件

`os.remove(path, dir_fd)` 
可以删除文件。其中，path 是要删除的文件的路径，dir_fd 是一个文件描述符（整型），这个参数用于指定一个目录的文件描述符，path参数将被视为相对于这个目录的路径。通常情况下，dir_fd 可以省略。只有在需要使用文件描述符时，才需要指定这个参数。
```python
os.remove(path)
```

### 重命名文件或目录

`os.rename(src, dst)` 
可以重命名文件或目录。其中，src 是源文件或目录的路径，dst 是目标文件或目录的路径。
```python
os.rename(src, dst)
```

### 复制文件或目录
`shutil.copy(src, dst)` 
可以复制文件或目录。其中，src 是源文件或目录的路径，dst 是目标文件或目录的路径。
```python
import shutil
shutil.copy(src, dst)
```

## subprocess
subprocess 模块可以用来执行子进程。
```python
import subprocess
```

### 执行命令

`subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False)` 
可以执行命令。其中，args 是命令的列表，stdin、input、stdout、stderr 是标准输入、输入、标准输出、错误输出的管道，capture_output 是一个布尔值，如果为 True，则捕获标准输出和错误输出，并返回一个 CompletedProcess 实例。shell 是一个布尔值，如果为 True，则使用 shell 执行命令，否则使用子进程执行。cwd 是当前工作目录，timeout 是命令的超时时间，check 是一个布尔值，如果为 True，并且命令执行失败，则抛出 CalledProcessError 异常。
```python
result = subprocess.run(['ls', '-l'], capture_output=True)
print(result.stdout.decode())
```

