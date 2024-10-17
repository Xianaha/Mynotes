# How to use Git

## Install Git
[安装教程](https://blog.csdn.net/qq_45730223/article/details/131693287)
## Sign in Git Account
1. 打开Git Bash
2. 输入命令：`git config --global user.name "Xian"`
3. 输入命令：`git config --global user.email "1695165155@qq.com"`

## Create Local Private Key and Public Key
1. 打开Git Bash
2. 输入命令：`ssh-keygen`
3. 按回车键，默认保存到`C:\Users\Xian\.ssh`目录下
4. 输入命令：`cat ~/.ssh/id_rsa.pub`
5. 复制输出的公钥内容，并保存到GitHub或GitLab上，例如：`ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC6+...`输入到[Github](https://github.com/settings/keys)的SSH and GPG keys中，并添加描述信息。

## Instructions for using Git

`git clone <repository>` 克隆：克隆远程仓库到本地

`git add <file>` 暂存更改：添加文件到暂存区以便进行提交

`git status` 查看当前仓库状态：查看当前仓库状态，包括未跟踪的文件、修改的文件和暂存区的状态

`git commit -m "commit message"` 提交：提交暂存区的修改到本地仓库，并添加提交信息

`git push origin master` 推送：将本地仓库的修改推送到远程仓库的master分支，如果有冲突，需要先解决冲突。origin 是远程仓库的名称，master 是分支名称。`git push origin [branch_name] --force`会强制推送本地改动，即使有冲突也会覆盖远程仓库的修改。

`git pull origin master` 拉取：从远程仓库拉取最新代码并合并到本地仓库。

`git fetch origin master` 抓取：从远程仓库抓取最新代码，但不合并到本地仓库。

`git revert <commit-id>` 撤销提交：撤销指定提交。

`git reset HEAD <file>` 取消暂存：取消暂存文件。

`git reset --hard HEAD^` 回退版本：回退到上一个版本，并且会丢弃所有未提交的修改。其中`^`表示上一个版本，`--hard`表示强制回退。若想保留未提交的修改，则使用`--soft`选项。如果回退到指定版本，则使用`git reset --hard <commit-id>`，例如：`git reset --hard 8c7e1a1`。`git rest --hard HEAD~2`表示回退到上上个版本，`git reset --hard HEAD~100`表示回退到前100个版本。

`git merge <branch-name>` 合并分支：合并指定分支到当前分支。

`git stash` 暂存未提交的修改：暂存未提交的修改。

`git branch` 查看分支：查看本地仓库的分支。

`git branch <branch-name>` 创建分支：创建本地仓库的分支。

`git checkout <branch-name>` 切换分支：切换到指定分支。

`git branch -d <branch-name>` 删除分支：删除本地仓库的分支。

`git remote -v` 查看远程仓库：查看本地仓库的远程仓库。

`git remote add origin <repository>` 添加远程仓库：添加远程仓库到本地仓库。

`git remote remove origin` 删除远程仓库：删除本地仓库的远程仓库。

`git log` 查看提交历史：查看本地仓库的提交历史。

`git reset --hard <commit-id>` 回退版本：回退到指定提交版本。

`git stash` 暂存未提交的修改：暂存未提交的修改。

`git stash pop` 恢复暂存的修改：恢复暂存的修改。

`git diff` 查看修改内容：查看暂存区和工作区的差异。

`git diff --cached` 查看已暂存的修改内容：查看已暂存的修改内容。

`git rm <file>` 删除文件：从暂存区和工作区删除文件。

`git mv <file-original> <file-renamed>` 重命名文件：重命名文件，同时修改文件名。
