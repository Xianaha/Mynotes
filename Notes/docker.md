# Docker 使用指南

## Docker 简介
Docker 是一个开源的应用容器引擎，允许开发者打包应用及其依赖包到一个可移植的容器中。

## 在VSCode中安装Docker

1. 安装Docker Desktop
   - Windows: 下载安装包 https://docs.docker.com/desktop/install/windows-install/
   - Mac: 下载安装包 https://docs.docker.com/desktop/install/mac-install/
   - Linux: 参考 https://docs.docker.com/engine/install/

2. 安装VSCode Docker扩展
   - 在VSCode扩展商店搜索"Docker"并安装
   - 或运行命令：
     ```bash
     code --install-extension ms-azuretools.vscode-docker
     ```

## 基础Docker命令

```bash
# 查看Docker版本信息
docker version

# 从Docker Hub拉取镜像
docker pull [镜像名]:[标签]  # 例如: docker pull nginx:latest

# 运行容器
docker run -d -p [主机端口]:[容器端口] --name [容器名] [镜像名]
# -d: 后台运行
# -p: 端口映射
# --name: 指定容器名称

# 查看运行中的容器
docker ps
# 查看所有容器(包括已停止的)
docker ps -a

# 停止容器
docker stop [容器ID/名称]

# 删除容器
docker rm [容器ID/名称]

# 查看镜像列表
docker images

# 删除镜像
docker rmi [镜像ID]
```

## Docker Compose 使用

1. 创建docker-compose.yml文件
```yaml
version: '3'
services:
  web:
    image: nginx
    ports:
      - "8080:80"
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: example
```

2. 启动服务
```bash
docker-compose up -d  # -d表示后台运行
```

3. 停止服务
```bash
docker-compose down
```

## VSCode中的Docker开发

1. 打开Docker面板(左侧活动栏Docker图标)
2. 右键镜像可进行pull/run等操作
3. 右键容器可查看日志、打开终端等
4. 使用Dev Containers扩展可直接在容器中开发

## 最佳实践

- 使用.dockerignore文件排除不需要的文件
- 多阶段构建减小镜像体积
- 使用官方镜像作为基础
- 为容器设置资源限制
