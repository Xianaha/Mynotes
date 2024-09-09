# Linux指令

## 与服务器相关

`scp` 命令是 `ssh` 协议的一部分，可以用来在本地和远程服务器之间安全地传输文件。

假设你有一个本地文件夹 `local_folder`，你想将其传到服务器的 `/remote/path/` 目录下，可以使用以下命令：
`scp -r local_folder username@server_ip:/remote/path/`
其中，`-r` 选项表示递归复制整个目录，`username` 是你的服务器用户名，`server_ip` 是你的服务器 IP 地址。

## 与文件相关

`ls` 命令用来列出当前目录的文件和目录。例如：`ls -l` 用来显示详细信息，`ls -a` 用来显示隐藏文件，`ls -h` 用来显示文件大小以方便查看。

`pwd` 命令用来显示当前目录的路径。例如：`pwd` 显示当前目录的路径。

`cd` 命令用来切换目录。例如：`cd /path/to/directory` 切换到 `/path/to/directory` 目录。完整语法为：`cd [目录]`，例如：`cd ..` 切换到上级目录；`cd ~` 切换到用户主目录；`cd -` 切换到上次所在目录；`cd` 切换到用户主目录；`cd /` 切换到根目录；`cd !$` 切换到上个命令的目录；`cd !n` 切换到第 n 个命令的目录。

`cp` 命令用来复制文件或目录。例如：`cp file1.txt file2.txt` 复制 `file1.txt` 到 `file2.txt`。

`file` 命令用来显示文件类型。例如：`file file1.txt` 显示 `file1.txt` 的类型。

`du` 命令用来显示目录或文件大小。例如：`du -sh /path/to/directory` 显示 `/path/to/directory` 的大小。

`cat` 命令用来显示文件内容。例如：`cat file1.txt` 显示 `file1.txt` 的内容。

`touch` 命令用来创建空文件。例如：`touch file1.txt` 创建名为 `file1.txt` 的空文件。

`mkdir` 命令用来创建目录。例如：`mkdir directory1` 创建名为 `directory1` 的目录。

`rmdir` 命令用来删除空目录。例如：`rmdir directory1` 删除名为 `directory1` 的空目录。

`rm` 命令用来删除文件或目录。例如：`rm file1.txt` 删除名为 `file1.txt` 的文件。完整语法为：`rm [选项] 文件或目录`，例如：`rm -d directory1` 删除名为 `directory1` 的目录，`-d` 选项表示删除空目录;`rm -r directory1` 删除名为 `directory1` 的目录及其内容。其中，`-r` 选项表示递归删除目录及其内容；`-f` 选项表示强制删除文件或目录，即使它们是只读的；`-i` 选项表示交互式删除，询问是否删除每个文件；`rf` 选项的组合表示递归强制删除。

`mv` 命令用来移动或重命名文件或目录。例如：`mv file1.txt file2.txt` 重命名 `file1.txt` 为 `file2.txt`。完整语法为：`mv [选项] 源文件 目标文件`，例如：`mv file1.txt /path/to/directory`。其中，`-i` 选项表示交互式移动，询问是否覆盖目标文件；`-f` 选项表示强制覆盖目标文件，即使目标文件是只读的。

`ln` 命令用来创建链接。例如：`ln -s /path/to/file link1.txt` 创建名为 `link1.txt` 的符号链接。

`chmod` 命令用来修改文件权限。例如：`chmod 777 file1.txt` 修改 `file1.txt` 的权限为 `rwxrwxrwx`，其中 `r` 表示可读，`w` 表示可写，`x` 表示可执行，第一个 `7` 表示拥有者的权限，第二个 `7` 表示组权限，第三个 `7` 表示其他用户权限。

`chown` 命令用来修改文件所有者。例如：`chown username file1.txt` 修改 `file1.txt` 的所有者为 `username`。

`df` 命令用来显示磁盘使用情况。例如：`df -h` 显示磁盘使用情况，以方便查看。

`tar` 命令用来打包和压缩文件。例如：`tar -cvf archive.tar /path/to/directory` 打包 `/path/to/directory` 目录到 `archive.tar` 文件。

`gzip` 命令用来压缩文件。例如：`gzip file1.txt` 压缩 `file1.txt`。完整语法为：`gzip [选项] 文件名`，例如：`gzip -9 file1.txt`。其中，`-9` 选项表示压缩级别为最高。

`gunzip` 命令用来解压文件。例如：`gunzip file1.txt.gz` 解压 `file1.txt.gz`。完整语法为：`gunzip [选项] 文件名`，例如：`gunzip -9 file1.txt.gz`。其中，`-9` 选项表示解压级别为最高。

`bzip2` 命令用来压缩文件。

`bunzip2` 命令用来解压文件。

`zip` 命令用来压缩文件。

`unzip` 命令用来解压文件。

`diff` 命令用来比较文件。

`patch` 命令用来打补丁。

`sort` 命令用来排序文件。

`uniq` 命令用来删除重复行。

`comm` 命令用来比较两个文件。

`wc` 命令用来统计文件行数、单词数、字符数。

`head` 命令用来显示文件开头内容。

`tail` 命令用来显示文件末尾内容。

`sed` 命令用来编辑文件。

`awk` 命令用来处理文本文件。

`grep` 命令用来搜索文件内容。

`cp` 命令用来复制文件或目录。例如：`cp file1.txt file2.txt` 复制 `file1.txt` 到 `file2.txt`。完整语法为：`cp [选项] 源文件 目标文件`，例如：`cp -r /path/to/directory /path/to/new/directory`。其中，`-r` 选项表示递归复制整个目录。

`grep` 命令用来搜索文件内容。

`find` 命令用来搜索文件。例如：`find /path/to/directory -name "file1.txt"` 搜索 `/path/to/directory` 目录下名为 `file1.txt` 的文件。完整语法为：`find [路径] [选项] [动作]`，例如：`find / -name "file1.txt"`。其中，`-name` 选项表示搜索文件名，`路径` 表示搜索路径，`动作` 表示执行的动作。

`head` 命令用来显示文件开头内容。

`tail` 命令用来显示文件末尾内容。

`less` 命令用来分页显示文件内容。

`more` 命令和 `less` 命令类似，但 `more` 命令只能向前翻页，而 `less` 命令可以向前和向后翻页。

`nano` 命令用来编辑文件。

`vim` 命令用来编辑文件。进入文件后，按 `i` 键进入编辑模式，按 `Esc` 键退出编辑模式；按 `:` 键进入命令模式，`:q!`指的是不保存退出，`:wq`指的是保存退出，`:q`指的是已经保存的情况下退出，输入命令并按 `Enter` 键执行命令，当然可以可以在正常模式直接输入`ZZ`直接进行保存并退出。按 `Ctrl+G` 键显示当前行号，按 `Ctrl+V` 键粘贴，按 `Ctrl+W` 键删除一个词，按 `Ctrl+U` 键删除一行，按 `Ctrl+K` 键删除到行尾，按 `Ctrl+H` 键删除一个字符，按 `Ctrl+R` 键搜索历史命令，按 `Ctrl+Y` 键粘贴上次删除的命令，按 `Ctrl+E` 键移动到行尾，按 `Ctrl+A` 键移动到行首，按 `Ctrl+F` 键向前移动一个字符，按 `Ctrl+B` 键向后移动一个字符。


`free` 命令用来显示内存使用情况。

`uptime` 命令用来显示系统运行时间。

`whoami` 命令用来显示当前用户。

`passwd` 命令用来修改当前用户密码。完整语法为：`passwd [选项] 用户名`，也可以用来锁定或解锁用户账户，例如：`passwd root`。其中，`-l` 选项表示锁定用户账户，`-u` 选项表示解锁用户账户。例如：`passwd -l root` 锁定 `root` 用户账户。

`shutdown` 命令用来关闭或重启系统。

`ping` 命令用来测试网络连接。

`ifconfig` 命令用来显示网络接口信息。

`route` 命令用来显示路由表。

`traceroute` 命令用来显示路由信息。

`nslookup` 命令用来查询域名信息。

`dig` 命令用来查询 DNS 记录。

`whois` 命令用来查询域名注册信息。

`last` 命令用来显示登录记录。

`ps` 命令用来显示进程信息。

`kill` 命令用来终止进程。

`killall` 命令用来终止所有进程。

`top` 命令用来实时显示系统信息。

`history` 命令用来显示命令历史。

`alias` 命令用来创建命令别名。

`unalias` 命令用来删除命令别名。

`su` 命令用来切换用户。

`sudo` 命令用来以超级用户权限运行命令。

`screen` 命令用来创建会话。

`tmux` 命令用来创建会话。

`htop` 命令用来实时显示系统信息。

`man` 命令用来显示命令帮助。

`apropos` 命令用来搜索命令帮助。

`whatis` 命令用来显示命令简介。

`whereis` 命令用来查找命令位置。

`which` 命令用来查找命令位置。

`locate` 命令用来查找文件。
