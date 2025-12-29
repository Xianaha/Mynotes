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
# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# 使用pip安装（不推荐，但可作为备选）
pip install uv
```

### 虚拟环境管理

#### 创建虚拟环境
```bash
# 创建默认的.venv目录
uv venv

# 指定环境名称和位置
uv venv myenv                # 创建myenv目录
uv venv --path ./envs/prod   # 指定完整路径

# 指定Python版本
uv venv --python 3.10        # 使用Python 3.10
uv venv --python 3.11        # 使用Python 3.11

# 创建不带pip的环境（最小化）
uv venv --without-pip

# 从pyproject.toml读取Python版本约束
uv venv --from pyproject.toml
```

#### 激活虚拟环境
```bash
# Windows
.\.venv\Scripts\activate
# 或使用完整路径
D:\path\to\.venv\Scripts\activate

# Unix/Linux/macOS
source .venv/bin/activate

# 使用uv直接运行命令（无需激活）
uv run python script.py      # 在虚拟环境中直接运行
uv run --with myenv python script.py  # 指定特定环境运行
```

#### 管理虚拟环境
```bash
# 列出所有虚拟环境
uv venv list

# 删除虚拟环境
uv venv remove myenv
uv venv remove --path ./envs/prod

# 复制虚拟环境
uv venv clone .venv --name .venv-backup

# 查看虚拟环境信息
uv venv info .venv
```

### 依赖管理

#### 安装依赖
```bash
# 基本安装
uv pip install package_name
uv pip install "package_name>=1.0,<2.0"  # 版本约束

# 从文件安装
uv pip install -r requirements.txt
uv pip install -r requirements-dev.txt

# 安装为可编辑模式（开发模式）
uv pip install -e .

# 安装额外依赖组
uv pip install "package[extra1,extra2]"

# 并行安装（默认启用）
uv pip install --parallel numpy pandas scikit-learn

# 仅下载不安装（用于离线环境）
uv pip download package_name --dest ./packages
```

#### 管理requirements文件
```bash
# 生成requirements.txt
uv pip freeze > requirements.txt

# 生成精确版本requirements.txt（推荐用于生产）
uv pip freeze --exact > requirements-exact.txt

# 生成仅包含直接依赖的requirements.txt
uv pip freeze --direct > requirements-direct.txt

# 从pyproject.toml生成requirements.txt
uv pip compile pyproject.toml -o requirements.txt

# 同步环境到requirements.txt
uv pip sync requirements.txt          # 完全匹配requirements.txt
uv pip sync --upgrade requirements.txt  # 更新到最新兼容版本

# 检查依赖冲突
uv pip check
```

#### 更新和卸载
```bash
# 更新单个包
uv pip install --upgrade package_name

# 更新所有包
uv pip install --upgrade --all

# 卸载包
uv pip uninstall package_name
uv pip uninstall -r requirements.txt  # 批量卸载

# 重新安装所有包
uv pip install --reinstall --all
```

### 项目配置与锁定文件

#### pyproject.toml管理
```bash
# 初始化pyproject.toml
uv init
uv init --name myproject --version 0.1.0

# 添加依赖到pyproject.toml
uv add numpy pandas                    # 添加直接依赖
uv add --dev pytest black              # 添加开发依赖
uv add --optional plotting matplotlib  # 添加可选依赖

# 从requirements.txt导入到pyproject.toml
uv add -r requirements.txt

# 更新pyproject.toml中的依赖
uv update numpy                       # 更新单个包
uv update --all                       # 更新所有包

# 移除依赖
uv remove numpy
```

#### 锁定文件
```bash
# 生成锁文件（精确版本）
uv lock                                # 生成uv.lock
uv lock --upgrade                     # 更新锁文件

# 从锁文件安装
uv pip install --locked               # 使用uv.lock安装
uv pip sync --locked                  # 同步到锁文件状态

# 检查锁文件状态
uv lock --check                       # 检查是否需要更新
```

### 环境迁移与复制

#### 导出环境
```bash
# 导出完整环境配置
uv export                            # 导出到requirements.txt
uv export --format json              # 导出为JSON格式
uv export --format toml              # 导出为TOML格式

# 导出可重现的环境
uv export --complete                 # 包含所有元数据
uv export --platform linux-64        # 指定平台

# 导出为部署包
uv pip freeze --all > requirements-deploy.txt
uv pip download -r requirements-deploy.txt --dest ./deploy-packages
```

#### 迁移环境
```bash
# 1. 从pip/conda迁移到uv
# 导出现有环境
pip freeze > old-requirements.txt
# 使用uv重新安装
uv pip install -r old-requirements.txt

# 2. 从conda迁移
conda env export --from-history > environment.yml
# 手动转换或使用工具转换后使用uv安装

# 3. 复制环境到其他机器
# 源机器：
uv export --complete > environment.uv.json
# 目标机器：
uv pip install --from-json environment.uv.json

# 4. 创建环境快照
uv venv snapshot .venv --output env-snapshot.tar.gz
uv venv restore env-snapshot.tar.gz --path restored-env
```

#### 离线环境管理
```bash
# 1. 在有网络的环境中准备包
uv pip download -r requirements.txt --dest ./offline-packages

# 2. 复制整个缓存目录
# uv缓存位置：~/.cache/uv (Unix) 或 %LOCALAPPDATA%\uv\cache (Windows)

# 3. 在离线环境中安装
uv pip install --no-index --find-links ./offline-packages -r requirements.txt

# 4. 配置离线缓存
uv config set cache-dir ./local-cache
uv config set download-mirror http://internal-mirror/pypi
```

### 与pip/conda互操作

#### 与pip兼容性
```bash
# uv可以直接使用pip格式的命令
uv pip install ...                   # 完全兼容pip命令
uv pip list --format=freeze         # pip风格的输出

# 混合使用uv和pip
# 1. 用uv创建环境，用pip安装特定包
uv venv
.\.venv\Scripts\activate
pip install some-package

# 2. 用pip生成requirements.txt，用uv安装
pip freeze > requirements.txt
uv pip install -r requirements.txt

# uv读取pip配置文件
# uv会自动读取 ~/.pip/pip.conf 和 pip.ini
```

#### 与conda配合使用
```bash
# 在conda环境中使用uv
conda create -n uv-env python=3.10
conda activate uv-env
pip install uv                      # 在conda环境中安装uv

# 使用uv管理conda环境中的Python包
uv pip install numpy                # 使用uv而非conda安装

# 导出conda环境供uv使用
conda list --export > conda-packages.txt
# 转换为requirements.txt格式后使用uv安装
```

### 实际工作流示例

#### 新项目开发流程
```bash
# 1. 创建项目
mkdir myproject && cd myproject

# 2. 初始化虚拟环境和项目配置
uv venv --python 3.11
.\.venv\Scripts\activate
uv init --name myproject --version 0.1.0

# 3. 添加依赖
uv add fastapi "uvicorn[standard]"
uv add --dev pytest black mypy
uv add --optional docs mkdocs

# 4. 开发过程中管理依赖
uv add new-package                 # 添加新依赖
uv update --all                    # 更新所有依赖
uv lock                            # 生成锁文件

# 5. 生成部署文件
uv export --exact > requirements.txt
uv lock > uv.lock
```

#### 团队协作流程
```bash
# 克隆项目后设置环境
git clone project-url
cd project

# 使用锁文件确保一致性
uv pip install --locked           # 安装精确版本

# 或从requirements.txt安装
uv pip install -r requirements.txt

# 添加新依赖后更新团队
uv add new-package
uv lock --upgrade
git add pyproject.toml uv.lock
git commit -m "Add new-package dependency"
```

#### CI/CD集成
```bash
# GitHub Actions示例
# .github/workflows/test.yml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
      - run: uv pip install --locked
      - run: uv run pytest
```

### 高级功能与性能优化

#### 缓存管理
```bash
# 查看缓存信息
uv cache dir                       # 显示缓存目录
uv cache info                      # 显示缓存统计

# 清理缓存
uv cache clean                     # 清理过期缓存
uv cache purge                     # 清理所有缓存

# 预热缓存（提前下载常用包）
uv cache warm numpy pandas scikit-learn
```

#### 配置管理
```bash
# 查看当前配置
uv config list

# 设置配置
uv config set cache-dir ./my-cache
uv config set network-timeout 30
uv config set install.timeout 60

# 配置文件位置
# Unix: ~/.config/uv/config.toml
# Windows: %APPDATA%\uv\config.toml
```

#### 性能优化技巧
1. **启用全局缓存**（团队共享）：
```bash
uv config set cache-dir /shared/cache
```

2. **使用镜像源加速**：
```bash
uv config set index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

3. **预下载依赖**（Docker构建优化）：
```dockerfile
# 先单独下载依赖，利用Docker缓存
COPY requirements.txt .
RUN uv pip install -r requirements.txt --target /deps
# 再复制代码
COPY . .
```

### 故障排除

#### 常见问题
1. **权限问题**：
```bash
# 使用--user标志
uv pip install --user package_name
# 或指定虚拟环境
uv venv --path ~/myenv
```

2. **网络问题**：
```bash
# 设置代理
uv config set proxy http://proxy:port
# 使用镜像源
uv config set index-url https://mirror.url
```

3. **依赖冲突**：
```bash
# 详细解析信息
uv pip install --verbose package_name
# 查看依赖树
uv pip show --tree package_name
```

#### 调试命令
```bash
# 详细输出
uv --verbose pip install package_name

# 模拟运行（不实际安装）
uv pip install --dry-run package_name

# 查看解析过程
uv pip install --no-cache package_name

# 强制重新解析
uv cache clean
uv pip install --reinstall package_name
```

#### uv vs pip vs conda 功能对比

| 特性 | uv | pip | conda |
|------|-----|-----|-------|
| **虚拟环境** | 内置 (`uv venv`) | 需venv模块 | 内置 (`conda create`) |
| **依赖解析** | 快速Rust解析器 | 较慢Python解析器 | 复杂但功能强 |
| **并行下载** | 默认启用 | 需`--parallel`标志 | 支持 |
| **锁定文件** | `uv.lock`支持 | 无原生支持 | `environment.yml` |
| **项目管理** | `pyproject.toml`集成 | 无 | `environment.yml` |
| **非Python包** | 不支持 | 不支持 | 支持 |
| **跨平台** | 优秀 | 优秀 | 优秀 |
| **缓存机制** | 智能全局缓存 | 简单缓存 | 仓库缓存 |
| **性能** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **易用性** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |

#### 使用建议总结

1. **新项目首选uv**：性能优异，功能全面，与现代Python工具链集成好
2. **科学计算场景**：仍可考虑conda（非Python依赖需求）
3. **迁移策略**：
   - 新项目直接使用uv
   - 现有pip项目逐步迁移：`pip freeze > req.txt && uv pip install -r req.txt`
   - conda项目评估需求，可混合使用
4. **团队协作**：统一使用uv.lock确保环境一致性
5. **生产部署**：使用`uv export --exact`生成精确requirements.txt

uv正在快速成为Python包管理的现代标准，特别适合需要快速迭代和团队协作的项目。
