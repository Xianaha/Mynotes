# Python包管理工具

## Conda

### 常用指令

`conda info` 显示conda版本信息。
```
# conda environments:
#
base                   D:\Miniconda
pytorch              * D:\Miniconda\envs\pytorch
```
这里显示了当前conda环境的名称、路径、激活状态。其中`*`表示当前环境。

`conda create -n env_name python=3.10` 创建一个名为env_name的环境，指定python版本为3.10。

`conda activate env_name` 激活env_name环境。

`conda deactivate` 退出当前环境。

`conda install package_name` 安装package_name包。完整指令为：`conda install package_name=version`，其中version表示版本号，可选。`conda install -n env_name package_name` 安装package_name包到env_name环境。`conda install -r requirements.txt` 从requirements.txt文件安装依赖包。

`conda remove package_name` 卸载package_name包。

`conda list` 列出当前环境中的所有包。

`conda config --show` 显示当前配置。

`conda config --add envs_dirs envs_path` 添加虚拟环境路径。

`conda config --remove envs_dirs envs_path` 移除虚拟环境路径。

`conda config --set channel_priority strict` 设置channel优先级为strict。

`conda config --set always_yes yes` 自动确认所有包的安装。

`conda search package_name` 搜索package_name包。

`conda update package_name` 更新package_name包(更新至最新版本)。若需要更新到指定版本，则 `conda update numpy=1.21` 更新numpy包到1.21版本。

`conda update --all` 更新当前环境中的所有包。

`conda env export > environment.yml` 导出当前环境的依赖关系到environment.yml文件。完整指令为：`conda env export --from-history > environment.yml`，其中--from-history参数表示只导出当前环境的依赖关系，而不导出其他环境的依赖关系。

`conda env create -f environment.yml` 从environment.yml文件创建新的环境。完整指令为：`conda env create -f environment.yml`。

`conda env update -f environment.yml` 更新当前环境的依赖关系。完整指令为：`conda env update -f environment.yml`。

`conda env remove -n env_name` 删除名为env_name的环境。

`conda env list` 列出所有环境。

`conda clean -a` 清理无用的包和缓存。

## uv

uv是Rust实现的高性能Python包管理工具，由Astral公司开发(同pytest、ruff等工具同一团队)。

### 安装方法
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 常规用法

1. 创建虚拟环境：
```bash
uv venv  # 创建.venv目录作为虚拟环境
```

2. 激活虚拟环境：
- Windows:
```bash
.\.venv\Scripts\activate
```
- Unix/MacOS:
```bash
source .venv/bin/activate
```

3. 安装包：
```bash
uv pip install package_name
```

4. 从requirements.txt安装：
```bash
uv pip install -r requirements.txt
```

5. 生成requirements.txt：
```bash
uv pip freeze > requirements.txt
```

6. 快速安装(并行下载)：
```bash
uv pip install --parallel package_name
```

7. 升级所有包：
```bash
uv pip install --upgrade --all
```

### 项目初始化流程

1. 创建项目目录：
```bash
mkdir my_project
cd my_project
```

2. 初始化虚拟环境：
```bash
uv venv
```

3. 激活环境：
```bash
.\.venv\Scripts\activate
```

4. 初始化Python项目：
```bash
uv init
```

5. 安装依赖：
```bash
uv add "package[extra]"
```

6. 开发完成后冻结依赖：
```bash
uv pip freeze > requirements.txt
```

### 高级功能

1. 依赖解析缓存：
uv会缓存依赖解析结果，显著加快重复安装速度

2. 并行下载：
默认启用多线程下载，大幅提升包下载速度

3. 本地缓存：
所有下载的包会缓存在本地，避免重复下载

4. 快速依赖解析：
使用Rust实现的快速依赖解析算法

#### uv vs pip

| 特性        | uv          | pip         |
|------------|-------------|-------------|
| 实现语言    | Rust        | Python      |
| 下载速度    | 快(并行)    | 慢(串行)    |
| 依赖解析    | 快          | 慢          |
| 缓存机制    | 完善        | 有限        |
| 虚拟环境    | 内置支持    | 需venv模块 |

#### uv vs conda

| 特性        | uv          | conda       |
|------------|-------------|-------------|
| 包来源      | PyPI        | Conda仓库   |
| 跨平台      | 是          | 是          |
| 环境隔离    | 虚拟环境    | 独立环境    |
| 非Python包 | 不支持      | 支持        |
| 性能        | 快          | 慢          |

#### uv vs venv

1. uv内置虚拟环境功能，不需要额外安装venv模块
2. uv虚拟环境创建速度更快
3. uv提供更简洁的命令行接口
4. uv虚拟环境与pip兼容，可以混合使用
5. uv虚拟环境目录结构与传统venv一致

#### 性能对比

1. 创建虚拟环境：
- uv: ~100ms
- python -m venv: ~500ms

2. 安装numpy+pandas:
- uv: ~2s
- pip: ~10s

3. 重复安装(利用缓存):
- uv: ~0.5s
- pip: ~8s

#### 使用建议

1. 新项目推荐使用uv替代pip+venv组合
2. 已有项目可以逐步迁移到uv
3. 需要非Python依赖时仍需使用conda
4. 团队开发时统一包管理工具
