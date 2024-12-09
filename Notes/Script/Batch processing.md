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
可以判断文件或目录是否存在，也可以判断文件是否可读、可写、可执行（是否损坏）。
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

`


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

## Crawl

### 抓包分析
- 打开开发者工具
    - `F12`/右键点击检查选择`Network`标签页
- 刷新页面/点击下一页/下滑页面/点击数据加载
    - 让网页的数据加载出来
- 通过关键字搜索找到对应的数据位置
    - 关键字
        - 采集评论（以评论内容搜索）
        - 采集用户信息（以用户昵称搜索）
        - 采集商品信息（以商品名称搜索）
        - 采集订单信息（以订单号搜索）

### 代码实现
- 发送请求
    - 使用`requests`模块发送请求，获取响应内容
        - 模拟浏览器，找到分析的`url`和`header`信息（请求标头）
        - 使用`requests.get(url, headers=headers)`发送请求，返回响应内容`response`
- 获取数据
    - 使用`BeautifulSoup`模块解析响应内容，获取数据
- 解析数据
    - 解析数据，提取需要的数据
- 保存数据
    - 将数据保存到文件中，以便后续处理

### json
json 模块可以用来处理 JSON 数据。
```python
import json
```

`json.dumps(obj)` 
可以将 Python 对象编码为 JSON 字符串。
```python
json_str = json.dumps(obj)
```

`json.loads(s)` 
可以将 JSON 字符串解码为 Python 对象。
```python
obj = json.loads(s)
```

`json.load(fp)` 
可以从文件中读取 JSON 数据，并解码为 Python 对象。
```python
with open(file, 'r') as f:
    obj = json.load(f)
```

`json.dump(obj, fp)` 
可以将 Python 对象编码为 JSON 字符串，并写入文件。
```python
with open(file, 'w') as f:
    json.dump(obj, f)
```

`json.dumps(obj, indent=4)` 
可以格式化 JSON 字符串。
```python
json_str = json.dumps(obj, indent=4)
```

### requests
requests 模块可以用来发送 HTTP 请求。适合静态页面的爬取，动态页面的爬取需要用到`selenium`模块。
```python
import requests
```

- `url`，通常是一个字符串，表示请求的 URL。

- `params`，是一个字典，表示请求的查询参数。`params` 参数用于向服务器发送查询字符串参数。这些参数通常是在 URL 中以键值对的形式传递的，主要用于过滤或指定要获取的数据。

例如，如果你想请求一个 API，并且希望根据某些条件（如页面编号、搜索关键字等）来过滤结果，你可以使用 params 来构建查询参数。

- `data`，是一个字典或字符串，表示请求的请求体。

- `headers`，是一个字典，表示请求的头部信息。
在大多数现代浏览器中，可以通过打开开发者工具获取 User-Agent。一般可以按下 `F12` 键，切换到 `Network`（网络）标签页，然后刷新页面。选中任意请求，查看其
请求标头的内容可以获取headers。一般需要`cookie` 和 `User-Agent`信息。
- `cookies`，是一个字典，表示请求的 Cookie。主要用于身份验证，检测是否登录账号。

- `User-Agent`，用户代理，表示浏览器/设备基本信息

- `auth`，是一个元组，表示 HTTP 认证的用户名和密码。

- `timeout`，是一个浮点数，表示请求的超时时间（单位：秒）。

- `verify`，是一个布尔值或字符串，表示是否验证 SSL 证书。

- `stream`，是一个布尔值，表示是否以流的形式接收响应内容。

- `cert`，是一个字符串，表示客户端 SSL 证书的路径。

- `json`，是一个字典或列表，表示请求的 JSON 数据。

- `method`，是一个字符串，表示 HTTP 请求的方法。

`requests.get(url, params=None, **kwargs)` 
获取指定 URL 的内容。其中：
- `url`，表示请求的 URL。
- `params`，表示请求的查询参数。
- `kwargs`，表示其他的请求参数。
- 返回值是一个 Response 对象，包含响应内容、状态码、头部信息等。

```python
url = 'https://www.csdn.net/'
response = requests.get(url)
response.text
>>> <html><body><script language="javascript"> window.onload=setTimeout("iw(20)", 200); function iw(OI) {var qo, mo="", no="", oo = [0x67,0x4d,0xdd......................
```


`requests.post(url, data=None, json=None, **kwargs)` 
发送 POST 请求。其中：
- `url`，表示请求的 URL。
- `data`，表示请求的请求体。
- `json`，表示请求的 JSON 数据。
- `kwargs`，表示其他的请求参数。
- 返回值是一个 Response 对象，包含响应内容、状态码、头部信息等。
```python
url = 'https://httpbin.org/post'
data = {'name': 'Alice', 'age': 25}
response = requests.post(url, data=data)
response.json()
>>> {'args': {}, 'data': '{"name": "Alice", "age": 25}', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'Content-Length': '22', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.1', 'X-Amzn-Trace-Id': 'Root=1-60a1d9a0-7d5d1d5d5a0d5d5a4a0a5a5a'}, 'json': None, 'origin': '172.16.58.3', 'url': 'https://httpbin.org/post'}
```

`requests.put(url, data=None, **kwargs)` 
发送 PUT 请求。其中：
- `url`，表示请求的 URL。
- `data`，表示请求的请求体。
- `kwargs`，表示其他的请求参数。
- 返回值是一个 Response 对象，包含响应内容、状态码、头部信息等。
```python
url = 'https://httpbin.org/put'
data = {'name': 'Alice', 'age': 25}
response = requests.put(url, data=data)
response.json()
>>> {'args': {}, 'data': '{"name": "Alice", "age": 25}', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'Content-Length': '22', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.1', 'X-Amzn-Trace-Id': 'Root=1-60a1d9a0-7d5d1d5d5a0d5d5a4a0a5a5a'}, 'json': None, 'origin': '172.16.58.3', 'url': 'https://httpbin.org/put'}
```

`requests.delete(url, **kwargs)` 
发送 DELETE 请求。其中：
- `url`，表示请求的 URL。
- `kwargs`，表示其他的请求参数。
- 返回值是一个 Response 对象，包含响应内容、状态码、头部信息等。
```python
url = 'https://httpbin.org/delete'
response = requests.delete(url)
response.json()
>>> {'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'Content-Length': '0', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.1', 'X-Amzn-Trace-Id': 'Root=1-60a1d9a0-7d5d1d5d5a0d5d5a4a0a5a5a'}, 'json': None, 'origin': '172.16.58.3', 'url': 'https://httpbin.org/delete'}
```

`requests.head(url, **kwargs)` 
发送 HEAD 请求。其中：
- `url`，表示请求的 URL。
- `kwargs`，表示其他的请求参数。
- 返回值是一个 Response 对象，包含响应内容、状态码、头部信息等。
```python
url = 'https://httpbin.org/get'
response = requests.head(url)
response.headers
>>> {'Server': 'nginx', 'Date': 'Thu, 16 Sep 2021 07:56:22 GMT', 'Content-Type': 'application/json', 'Content-Length': '270', 'Connection': 'keep-alive', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
```

`requests.options(url, **kwargs)` 
发送 OPTIONS 请求。其中：
- `url`，表示请求的 URL。
- `kwargs`，表示其他的请求参数。
- 返回值是一个 Response 对象，包含响应内容、状态码、头部信息等。
```python
url = 'https://httpbin.org/get'
response = requests.options(url)
response.headers
>>> {'Server': 'nginx', 'Date': 'Thu, 16 Sep 2021 07:56:22 GMT', 'Content-Type': 'application/json', 'Content-Length': '270', 'Connection': 'keep-alive', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true', 'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS', 'Access-Control-Allow-Headers': 'DNT, X-CustomHeader, Keep-Alive, User-Agent, X-Requested-With, If-Modified-Since, Cache-Control, Content-Type, Authorization', 'Access-Control-Max-Age': '604800'}
```

`requests.request(method, url, **kwargs)` 
发送自定义请求。其中，method 是 HTTP 请求的方法，url 是请求的 URL。其中：
- `url`，表示请求的 URL。
- `kwargs`，表示其他的请求参数。
- 返回值是一个 Response 对象，包含响应内容、状态码、头部信息等。
```python
url = 'https://httpbin.org/get'
response = requests.request('GET', url)
response.json()
>>> {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.1'}, 'origin': '172.16.58.3', 'url': 'https://httpbin.org/get'}
```

`response.text` 
表示响应的文本内容。

`response.json()` 
表示响应的 JSON 数据。

`response.url` 
表示响应的 URL。

`response.encoding` 
表示响应的编码格式。
```python
# 转码
response.encoding = 'utf-8'
```

`response.status_code` 
表示响应的状态码。

`response.headers` 
表示响应的头部信息。

`response.content` 
表示响应的字节内容。

`response.raise_for_status()`
如果响应的状态码不是 2xx，则抛出 HTTPError 异常。出现该情况时，可以考虑以下原因：
- 检查URL：确保您请求的URL是正确的并且在正常运作。您可以在浏览器中尝试直接访问该URL，看是否能正常打开。

- 检查目标网站的可用性：目标网站可能正在进行维护，您可以稍后再试。

- 请求头与其他参数：有些网站会拒绝没有正确请求头的请求，您可以考虑增加或修改User-Agent或其他请求头，以模仿真实的浏览器请求。
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}
```
- IP封禁或限制：某些网站可能会在短时间内限制同一个IP的请求次数，从而造成访问失败。您可以通过更改网络环境或在请求之间增加延迟来解决。

- 使用代理：如果您的请求频繁地被拒绝，可以考虑使用代理服务器来减小被封禁的风险。

- 调试信息：为了更好地Debug，可以打印response.status_code和response.text来获取更多的错误信息。
```python
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
except requests.HTTPError as e:
    print(f"HTTP error occurred: {e}")
    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")
```

```python
response = requests.get('https://httpbin.org/status/404')
response.raise_for_status()
>>> requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://httpbin.org/status/404
```

### webdriver-manager
webdriver-manager 可以用来自动下载浏览器驱动。

安装：
```python
pip install webdriver-manager
```
```python
from webdriver_manager.chrome import ChromeDriverManager
```

`ChromeDriverManager().install()` 
可以下载 Chrome 浏览器的驱动。
```python
from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()
```

### selenium
`Selenium` 是一个用于自动化浏览器操作的工具，常用于 Web 应用的测试和网页内容的抓取。它支持多种浏览器，包括 Chrome、Firefox、Safari 等。适合动态网页的自动化测试、爬虫、自动化运维等领域。但因为selenium要模仿浏览器行为，在速度上会慢于requests。
[Selenium 教程网站](https://www.runoob.com/python3/python-selenium.html)
安装：
```python
pip install selenium
```

**常用方法**：
`webriver` 
表示浏览器驱动，可以用来控制浏览器。
```python
from selenium import webdriver

# 使用 Chrome 浏览器
driver = webdriver.Chrome()

# 使用 Firefox 浏览器
driver = webdriver.Firefox()

# 使用 Edge 浏览器
driver = webdriver.Edge()

# 关闭浏览器(通常配套使用)
driver.quit()
```
在打开网页后，系统会自动加载网页窗口实例。若不希望系统自动加载，可以设置`headless`参数为`True`。
```python
from selenium.webdriver.edge.options import Options # 如果使用chrome则将edge换成chrome
options = webdriver.Options()
options.add_argument('headless')
driver = webdriver.Edeg(options=options)
```

`driver.get(url)` 
可以打开指定 URL 的页面。通常和driver.quit()配合使用。
```python
driver.get('https://www.baidu.com')
```

`driver.back()`
可以返回上一页。

`driver.forward()`
可以前进到下一页。

`driver.refresh()`
可以刷新当前页面。

`element.click()`
可以点击元素。

`element.send_keys(text)`
可以输入文本。

`element.clear()`
可以清空输入框。

`element.text`
可以获取元素的文本。

`element.get_attribute(name)`
可以获取元素的属性。

`element.location`
可以获取元素的位置。

`element.size`
可以获取元素的大小。

`element.screenshot(filename)`
可以截取元素的屏幕快照。

`element.is_displayed()`
可以判断元素是否可见。

`element.is_enabled()`
可以判断元素是否可用。

`element.is_selected()`
可以判断元素是否被选中。

`driver.find_element(by, value)`
查找第一个匹配的元素。其中：
- `by`，表示查找元素的类型。
- `value`，表示查找元素的属性。
- 返回值是一个 WebElement 对象，表示找到的元素。
```python
element = driver.find_element(By.ID, 'kw')

```

`driver.find_elements(by, value)`
查找所有匹配的元素。其中：
- `by`，表示查找元素的类型。
- `value`，表示查找元素的属性。
- 返回值是一个列表，包含所有找到的元素。
```python
elements = driver.find_elements(By.CLASS_NAME, 'class-name')
```

`driver.execute_script(script, *args)`
执行 JavaScript 代码。其中：
- `script`，表示 JavaScript 代码。
- `args`，表示参数。
- 返回值是执行 JavaScript 代码的返回值。
```python
result = driver.execute_script("return 1 + 2;")
```

`driver.add_cookie(cookie_dict)`
添加 Cookie。其中：
- `cookie_dict`，表示 Cookie 的字典。
```python
cookie_dict = {
    'name': 'value',
    'name2': 'value2'
}
driver.add_cookie(cookie_dict)
```

`driver.get_cookies()`
获取所有 Cookie。

`driver.delete_all_cookies()`
删除所有 Cookie。

`driver.delete_cookie(name)`
删除指定名称的 Cookie。

`driver.maximize_window()`
最大化浏览器窗口。

`driver.minimize_window()`
最小化浏览器窗口。


`driver.implicitly_wait(time)`
设置隐式等待时间。

`driver.WebDriverWait(timeout, poll_frequency, ignored_exceptions)`
设置显式等待时间。

`driver.set_page_load_timeout(time)`
设置页面加载超时时间。

`driver.set_script_timeout(time)`
设置脚本超时时间。



#### selenium.webdriver.common.by
`By` 类提供了一系列常用的查找元素的策略。
```python
from selenium.webdriver.common.by import By

# 查找 ID 为 id-value 的元素
element = driver.find_element(By.ID, 'id-value')

# 查找 NAME 为 name-value 的元素
element = driver.find_element(By.NAME, 'name-value')

# 查找 XPATH 为 xpath-value 的元素
element = driver.find_element(By.XPATH, 'xpath-value')

# 查找 CSS 选择器为 css-selector 的元素
element = driver.find_element(By.CSS_SELECTOR, 'css-selector')

# 查找 TAG NAME 为 tag-name 的元素
element = driver.find_element(By.TAG_NAME, 'tag-name')

# 查找 CLASS NAME 为 class-name 的元素
element = driver.find_element(By.CLASS_NAME, 'class-name')

# 查找 LINK TEXT 为 link-text 的元素
element = driver.find_element(By.LINK_TEXT, 'link-text')




### BeautifulSoup
BeautifulSoup 模块可以用来解析 HTML 文档。
```python
from bs4 import BeautifulSoup
```

`BeautifulSoup(markup, features=None, **kwargs)` 
可以解析 HTML 文档。其中：
- `markup`，表示要解析的 HTML 文档。
- `features`，表示解析器的特性。
- `kwargs`，表示其他的解析参数。
- 返回值是一个 BeautifulSoup 对象，包含解析后的文档。
```python
html = '''
<html>
<head>
    <title>Example</title>
</head>
<body>
    <p>Hello, world!</p>
</body>
</html>
'''
soup = BeautifulSoup(html, 'html.parser')
print(soup.title.string)
>>> Example
```

`soup.prettify()` 
可以格式化 HTML 文档。
```python
html = '''
<html>
<head>
    <title>Example</title>
</head>
<body>
    <p>Hello, world!</p>
</body>
</html>
'''
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())
```

`soup.title.string` 
可以获取文档的标题。

`soup.find_all(name, attrs, recursive, string, **kwargs)` 
可以查找文档中所有符合条件的元素。其中：
- `name`，表示元素的名称。
- `attrs`，表示元素的属性。
- `recursive`，表示是否递归查找。
- `string`，表示是否查找字符串。
- `kwargs`，表示其他的查找参数。
- 返回值是一个列表，包含所有符合条件的元素。
```python
html = '''
<html>
<head>
    <title>Example</title>
</head>
<body>
    <p>Hello, world!</p>
</body>
</html>
'''
soup = BeautifulSoup(html, 'html.parser')
print(soup.find_all('p'))
```

`soup.find(name, attrs, recursive, string, **kwargs)` 
可以查找文档中第一个符合条件的元素。其中：
- `name`，表示元素的名称。
- `attrs`，表示元素的属性。
- `recursive`，表示是否递归查找。
- `string`，表示是否查找字符串。
- `kwargs`，表示其他的查找参数。
- 返回值是一个 Tag 对象，表示第一个符合条件的元素。
```python
html = '''
<html>
<head>
    <title>Example</title>
</head>
<body>
    <p>Hello, world!</p>
</body>
</html>
'''
soup = BeautifulSoup(html, 'html.parser')
print(soup.find('p'))
```

`soup.select(selector)` 
可以查找文档中所有符合 CSS 选择器的元素。其中：
- `selector`，表示 CSS 选择器。
- 返回值是一个列表，包含所有符合条件的元素。
```python
html = '''
<html>
<head>
    <title>Example</title>
</head>
<body>
    <p>Hello, world!</p>
</body>
</html>
'''
soup = BeautifulSoup(html, 'html.parser')
print(soup.select('p'))
```



### re
re 模块可以用来处理正则表达式。
```python
import re
```

**正则表达式**：
正则表达式（Regular Expression，简称 regex）是一种用于匹配字符串的模式，它可以用来检索、替换和验证文本数据。正则表达式通过特定的语法规则描述字符串的结构，从而实现对文本的灵活操作。  
正则表达式通常用于以下几个主要场景：
- 搜索：查找符合特定模式的字符串。
- 替换：将符合特定模式的字符串替换成另一个字符串。
- 验证：检查字符串是否符合特定格式，如电子邮件地址、电话号码等。

正则表达式的语法包括字符集、量词、锚点和分组等，可以用于创建非常复杂的匹配规则。例如：
- `\d` 匹配任何数字。
- `\w` 匹配任何字母数字字符（包括下划线）。
- `.` 匹配除换行符外的任何单个字符。
- `*` 表示前面的元素可以出现零次或多次。
- `+` 表示前面的元素可以出现一次或多次。
- `?` 表示前面的元素可以出现零次或一次。
- `()` 表示创建分组，可以用于提取子串，表示需要的子串。
- `|` 表示或，可以匹配多个选项。
- `^` 表示行首，`$` 表示行尾。
- `\` 表示转义字符，可以用于匹配特殊字符。
- `[]` 表示字符集，可以匹配指定范围内的字符。
- `{}` 表示数量词，可以用于指定出现次数。
- `*` 表示零次或多次，`+` 表示一次或多次，`?` 表示零次或一次。
- `^` 表示非，`|` 表示或，`.` 表示任意字符，`(` 表示分组，`)` 表示结束分组。

详细可以看[正则表达式教程](https://www.runoob.com/regexp/regexp-intro.html)。



通过组合这些基本元素，可以构建出强大的文本处理功能。


**匹配模式**：
匹配模式是指在正则表达式中用于定义如何查找和匹配字符串的规则或方法。匹配模式决定了正则表达式如何解析和应用在目标文本上，以找到特定的字符串或模式。
常见的匹配模式包括以下几种：  
- 贪婪模式：这是默认的匹配模式，它会尽可能多地匹配字符。例如，正则表达式 `.*` 会尝试匹配尽可能多的字符，直到找到满足条件的最后一个字符串。  
- 非贪婪模式（懒惰模式）：使用 `?` 修饰符，可以使匹配尽量少地匹配字符，直到找到满足条件的第一个字符串。例如，正则表达式 `.*?` 会尽可能少地匹配字符。  
区分大小写：默认情况下，大多数正则表达式匹配是区分大小写的，但可以通过特定的标志（如 `i`）来进行不区分大小写的匹配。  
- 多行模式：在多行文本中使用时，可以通过特定的标志（如 `m`）来改变 ^ 和 $ 的行为，使它们匹配每一行的开头和结尾，而不仅仅是整个字符串的开头和结尾。  
- 单行模式：使用 `s` 标志可以使 . 匹配包括换行符在内的任何字符。

不同的匹配模式可以通过设置正则表达式的标志（如 /pattern/flags）来实现。选择合适的匹配模式可以提高正则表达式的灵活性和准确性。  


`re.findall(pattern, string, flags=0)` 
可以查找字符串中所有匹配正则表达式的子串。其中：
- `pattern`，表示正则表达式。
- `string`，表示要搜索的字符串，通常是数据源、数据集合、字符序列等。
- `flags`，表示匹配模式。
- 返回值是一个列表，包含所有匹配的子串。
```python
pattern = r'\d+'
string = 'The price is $10.50, the quantity is 20, the total is $20.00.'
re.findall(pattern, string)
>>> ['10', '50', '20', '20', '00']
```

`re.search(pattern, string, flags=0)` 
可以搜索字符串中第一个匹配正则表达式的子串。其中：
- `pattern`，表示正则表达式。
- `string`，表示要搜索的字符串。
- `flags`，表示匹配模式。
- 返回值是一个 Match 对象，包含第一个匹配的子串。
```python
pattern = r'\d+'
string = 'The price is $10.50, the quantity is 20, the total is $20.00.'
match = re.search(pattern, string)
match.group()
>>> '10'
```

`re.match(pattern, string, flags=0)` 
可以从字符串开头匹配正则表达式。其中：
- `pattern`，表示正则表达式。
- `string`，表示要搜索的字符串。
- `flags`，表示匹配模式。
- 返回值是一个 Match 对象，包含第一个匹配的子串。
```python
pattern = r'\d+'
string = 'The price is $10.50, the quantity is 20, the total is $20.00.'
match = re.match(pattern, string)
match.group()
>>> '10'
```

`re.sub(pattern, repl, string, count=0, flags=0)` 
可以替换字符串中所有匹配正则表达式的子串。其中：
- `pattern`，表示正则表达式。
- `repl`，表示替换字符串。
- `string`，表示要搜索的字符串。
- `count`，表示替换的次数。
- `flags`，表示匹配模式。
- 返回值是一个字符串，表示替换后的字符串。
```python
pattern = r'\d+'
repl = 'X'
string = 'The price is $10.50, the quantity is 20, the total is $20.00.'
re.sub(pattern, repl, string)
>>> 'The price is $X.X, the quantity is X, the total is X.X.'
```

`re.split(pattern, string, maxsplit=0, flags=0)` 
可以分割字符串。其中：
- `pattern`，表示分隔符。
- `string`，表示要分割的字符串。
- `maxsplit`，表示分割的次数。
- `flags`，表示匹配模式。
- 返回值是一个列表，包含分割后的子串。
```python
pattern = r'\s+'
string = 'The price is $10.50, the quantity is 20, the total is $20.00.'
re.split(pattern, string)
>>> ['The', 'price', 'is', '$10.50,', 'the', 'quantity', 'is', '20,', 'the', 'total', 'is', '$20.00.']
```




#### Link
[requests 官方教材](https://requests.readthedocs.io/projects/cn/zh-cn/latest/user/quickstart.html#)

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

