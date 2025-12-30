# Python包管理工具

## Conda

Conda是一个开源的包管理系统和环境管理系统，支持多种语言（主要是Python），可以管理非Python依赖（如C库、CUDA等）。由Anaconda公司开发，有Miniconda（最小安装）和Anaconda（完整发行版）两种发行版。

### 安装方法

#### Miniconda（推荐）
```bash
# Linux/macOS
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

# Windows
# 从 https://docs.conda.io/en/latest/miniconda.html 下载.exe安装程序
```

#### Anaconda（完整版）
```bash
# Linux/macOS
curl -O https://repo.anaconda.com/archive/Anaconda3-latest-Linux-x86_64.sh
bash Anaconda3-latest-Linux-x86_64.sh

# Windows
# 从 https://www.anaconda.com/products/distribution 下载安装程序
```

#### 配置conda（安装后）
```bash
# 初始化shell（首次安装后运行）
conda init

# 更新conda到最新版本
conda update -n base -c defaults conda
```

### 虚拟环境管理

#### 创建虚拟环境
```bash
# 基本创建
conda create -n myenv                     # 创建名为myenv的环境
conda create -n myenv python=3.10        # 指定Python版本
conda create -n myenv python=3.10 numpy pandas  # 创建时安装包

# 指定环境位置
conda create -p ./myenv                  # 在当前目录创建
conda create -p /path/to/env             # 指定完整路径

# 克隆环境
conda create --clone myenv --name myenv-clone  # 克隆环境
conda create --clone ./env1 --name env2        # 从路径克隆

# 从environment.yml创建
conda env create -f environment.yml
conda env create -f environment.yml --name newname
```

#### 激活与退出环境
```bash
# 激活环境
conda activate myenv                     # 激活名为myenv的环境
conda activate ./myenv                   # 激活路径环境

# 退出环境
conda deactivate

# 查看当前环境
conda info --envs                        # 查看所有环境
conda info                               # 查看conda信息（含当前环境）
```

#### 管理虚拟环境
```bash
# 列出所有环境
conda env list
conda info --envs

# 删除环境
conda remove -n myenv --all              # 删除整个环境
conda env remove -n myenv                # 同上
conda remove -p ./myenv --all           # 删除路径环境

# 重命名环境（通过克隆+删除）
conda create --clone oldenv --name newenv
conda remove --name oldenv --all

# 环境信息
conda list -n myenv                      # 查看环境中的包
conda env export -n myenv               # 导出环境配置
```

### 依赖管理

#### 安装包
```bash
# 基本安装
conda install numpy                      # 安装最新版本
conda install numpy=1.21                 # 安装指定版本
conda install "numpy>=1.20,<1.22"       # 版本范围

# 指定环境安装
conda install -n myenv numpy            # 安装到指定环境
conda install -p ./myenv numpy          # 安装到路径环境

# 从特定通道安装
conda install -c conda-forge numpy      # 从conda-forge通道
conda install -c pytorch pytorch        # 从pytorch通道

# 安装多个包
conda install numpy pandas matplotlib scikit-learn

# 安装pip包（在conda环境中使用pip）
conda install pip                       # 先安装pip
pip install some-package                # 然后使用pip安装
```

#### 更新包
```bash
# 更新单个包
conda update numpy
conda update -n myenv numpy            # 更新指定环境中的包

# 更新所有包
conda update --all
conda update -n myenv --all            # 更新指定环境所有包

# 更新conda本身
conda update conda
conda update -n base conda             # 更新base环境中的conda
```

#### 卸载包
```bash
# 卸载单个包
conda remove numpy
conda remove -n myenv numpy            # 从指定环境卸载

# 卸载多个包
conda remove numpy pandas matplotlib

# 查看包依赖关系（卸载前）
conda remove numpy --dry-run           # 模拟卸载，显示影响
```

#### 搜索和查看包
```bash
# 搜索包
conda search numpy                     # 搜索包
conda search "numpy[version='1.21.*']" # 搜索特定版本
conda search -c conda-forge numpy      # 从特定通道搜索

# 查看包信息
conda list                             # 查看当前环境所有包
conda list -n myenv                    # 查看指定环境包
conda list --export                    # 导出包列表（精确版本）

# 包详细信息
conda info numpy                       # 查看包详细信息
conda show numpy                       # 显示包元数据
```

### 环境配置文件管理

#### environment.yml文件
```yaml
# environment.yml示例
name: myproject-env
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
  - numpy=1.21
  - pandas>=1.3
  - pip
  - pip:
    - torch==1.12.0
    - -r requirements.txt
```

#### 导出和导入环境
```bash
# 导出当前环境
conda env export > environment.yml                  # 导出完整环境（含所有依赖）
conda env export --from-history > environment.yml   # 仅导出显式安装的包（推荐）

# 导出指定环境
conda env export -n myenv > environment.yml

# 导出为requirements.txt风格（用于pip）
conda list --export > requirements.txt             # 精确版本
conda list -e > requirements.txt                   # 同上

# 从文件创建环境
conda env create -f environment.yml                # 从environment.yml创建
conda env create -f environment.yml -n newname     # 指定新名称

# 更新现有环境
conda env update -f environment.yml                # 更新当前环境
conda env update -n myenv -f environment.yml       # 更新指定环境
```

#### 共享环境最佳实践
```bash
# 1. 创建最小化environment.yml（推荐）
conda env export --from-history > environment.yml

# 2. 创建精确复现environment.yml（用于生产）
conda env export --no-builds > environment-exact.yml

# 3. 创建跨平台environment.yml
conda env export --from-history | grep -v "^prefix" > environment.yml
```

### 通道和配置管理

#### 通道管理
```bash
# 添加通道
conda config --add channels conda-forge           # 添加conda-forge通道
conda config --add channels pytorch               # 添加pytorch通道

# 设置通道优先级
conda config --set channel_priority strict        # 严格优先级（推荐）
conda config --set channel_priority flexible      # 灵活优先级

# 查看通道配置
conda config --show channels                     # 显示通道列表
conda config --get channels                      # 获取通道

# 移除通道
conda config --remove channels conda-forge       # 移除通道

# 临时使用通道（不修改配置）
conda install -c conda-forge numpy
```

#### 配置管理
```bash
# 查看所有配置
conda config --show
conda config --show-sources                     # 显示配置源

# 常用配置设置
conda config --set always_yes yes               # 自动确认
conda config --set auto_activate_base false     # 不自动激活base环境
conda config --set changeps1 false              # 不在提示符显示环境名

# 代理设置
conda config --set proxy_servers.http http://proxy:port
conda config --set proxy_servers.https https://proxy:port

# 镜像源配置（中国用户）
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
conda config --set show_channel_urls yes
```

### 缓存和清理

#### 包缓存管理
```bash
# 查看缓存信息
conda info                                      # 包含缓存路径信息
conda config --show pkgs_dirs                  # 显示包目录

# 清理缓存
conda clean --all                              # 清理所有（包括索引、包、临时文件）
conda clean --packages                         # 清理未使用的包
conda clean --tarballs                         # 清理下载的tar包
conda clean --index-cache                      # 清理索引缓存

# 设置缓存大小限制
conda config --set pkgs_dirs /path/to/cache    # 设置缓存目录
```

### 实际工作流示例

#### 新项目开发流程
```bash
# 1. 创建项目目录
mkdir myproject && cd myproject

# 2. 创建conda环境
conda create -n myproject python=3.10
conda activate myproject

# 3. 安装项目依赖
conda install numpy pandas matplotlib
conda install -c conda-forge jupyterlab
conda install -c pytorch pytorch torchvision

# 4. 导出环境配置
conda env export --from-history > environment.yml

# 5. 开发过程中添加新依赖
conda install seaborn
conda env export --from-history > environment.yml  # 更新配置文件
```

#### 团队协作流程
```bash
# 克隆项目后
git clone project-url
cd project

# 从environment.yml创建环境
conda env create -f environment.yml
conda activate project-env

# 开发后更新环境配置
conda env export --from-history > environment.yml
git add environment.yml
git commit -m "Update environment dependencies"
```

#### 数据科学工作流
```bash
# 创建数据科学环境
conda create -n datascience python=3.10
conda activate datascience

# 安装数据科学堆栈
conda install numpy pandas matplotlib seaborn
conda install scikit-learn scipy statsmodels
conda install -c conda-forge jupyterlab jupyter_contrib_nbextensions

# 安装深度学习框架
conda install -c pytorch pytorch torchvision torchaudio
conda install -c conda-forge tensorflow

# 导出环境
conda env export --from-history > datascience-environment.yml
```

### 故障排除

#### 常见问题
```bash
# 1. 环境激活失败
# 解决方法：重新初始化conda
conda init --reverse  # 先反向初始化
conda init            # 再重新初始化

# 2. 依赖冲突
# 查看冲突信息
conda install package_name --dry-run  # 模拟安装
conda list --show-channel-urls        # 查看包来源

# 创建新环境解决冲突
conda create -n cleanenv python=3.10
conda activate cleanenv
conda install package_name

# 3. 下载速度慢
# 使用国内镜像源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
conda config --set show_channel_urls yes

# 4. 环境损坏
# 重新创建环境
conda env export --from-history > backup.yml
conda remove -n brokenenv --all
conda env create -f backup.yml -n newenv
```

#### 调试命令
```bash
# 详细输出
conda install -v numpy                    # 详细模式
conda install -vv numpy                   # 更详细

# 检查conda安装
conda doctor                              # 检查conda安装（如可用）
conda info -a                            # 所有信息

# 清理并重试
conda clean --all
conda update --all
```

### 与pip/uv互操作

#### 在conda环境中使用pip
```bash
# 最佳实践：先conda后pip
conda create -n myenv python=3.10
conda activate myenv
conda install numpy pandas              # 先用conda安装
conda install pip                       # 安装pip
pip install some-package                # 再用pip安装conda没有的包

# 注意事项：避免混合使用导致的依赖冲突
# 尽量使用conda安装，pip仅作补充
```

#### 从conda迁移到uv
```bash
# 1. 导出conda环境
conda list --export > conda-packages.txt

# 2. 转换为requirements.txt格式
# 需要手动转换或使用工具，因为conda和pip包名可能不同

# 3. 使用uv安装
uv venv
uv pip install -r requirements.txt

# 4. 对于特定conda包（如cudatoolkit），需要单独处理
```

#### conda与uv混合使用
```bash
# 方案1：在conda环境中安装uv
conda create -n uv-env python=3.10
conda activate uv-env
pip install uv                          # 在conda环境中安装uv
uv pip install numpy                    # 使用uv管理Python包

# 方案2：使用conda安装系统依赖，uv管理Python包
conda create -n myenv python=3.10 cudatoolkit=11.3
conda activate myenv
uv pip install torch torchvision        # 使用uv安装PyTorch
```

### 使用建议总结

1. **选择conda的场景**：
   - 需要非Python依赖（CUDA、MKL、特定C库等）
   - 科学计算、数据科学项目
   - 需要严格的环境复现
   - Windows平台（conda对Windows支持更好）

2. **环境管理最佳实践**：
   - 每个项目使用独立环境
   - 使用`environment.yml`记录环境配置
   - 使用`--from-history`导出最小化配置
   - 定期清理缓存

3. **性能优化**：
   - 使用国内镜像源加速下载
   - 合理设置通道优先级
   - 定期清理未使用的包

4. **团队协作**：
   - 共享`environment.yml`文件
   - 统一conda版本和配置
   - 文档化环境设置步骤

Conda在科学计算和机器学习领域仍然是重要工具，特别是在需要管理复杂依赖和跨平台兼容性的场景中。

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

### 新项目与环境创建

#### 从零创建新项目（完整流程）
```bash
# 1. 创建项目目录
mkdir my-project && cd my-project

# 2. 初始化虚拟环境（指定Python版本）
uv venv --python 3.11

# 3. 激活虚拟环境
# Windows:
.\.venv\Scripts\activate
# Unix/Linux/macOS:
source .venv/bin/activate

# 4. 初始化项目配置（创建pyproject.toml）
uv init --name my-project --version 0.1.0

# 5. 添加项目依赖
uv add fastapi uvicorn[standard]  # 添加生产依赖
uv add --dev pytest black mypy   # 添加开发依赖
uv add --optional docs mkdocs    # 添加可选依赖

# 6. 生成锁定文件（确保环境一致性）
uv lock

# 7. 安装所有依赖
uv pip install --locked

# 8. 验证环境
uv run python -c "import fastapi; print('环境配置成功！')"
```

#### 使用现有项目模板
```bash
# 从GitHub模板创建项目
git clone https://github.com/example/python-template my-project
cd my-project

# 使用uv创建环境并安装依赖
uv venv
.\.venv\Scripts\activate  # 或 source .venv/bin/activate
uv pip install -r requirements.txt

# 或从pyproject.toml安装
uv pip install .
```

#### 项目结构生成
uv可以自动生成标准的Python项目结构：
```bash
# 生成完整项目结构
uv init --name myapp --version 1.0.0 --package

# 生成的项目结构示例：
# myapp/
# ├── pyproject.toml      # 项目配置
# ├── README.md           # 项目说明
# ├── src/                # 源代码目录
# │   └── myapp/          # 包目录
# │       ├── __init__.py
# │       └── __main__.py
# ├── tests/              # 测试目录
# └── .gitignore          # Git忽略文件
```

#### 环境与项目配置一体化
```bash
# 一步完成环境创建和项目初始化
uv venv && .\.venv\Scripts\activate && uv init

# 指定Python版本和项目名称
uv venv --python 3.11 && .\.venv\Scripts\activate && uv init --name myproject --version 0.1.0

# 创建环境并安装常用开发工具
uv venv --python 3.11
.\.venv\Scripts\activate
uv add --dev pytest black ruff mypy pre-commit
```

#### 多环境项目配置
对于需要多个环境（开发、测试、生产）的项目：
```bash
# 创建开发环境
uv venv --python 3.11 --path ./envs/dev
uv pip install -r requirements-dev.txt

# 创建生产环境
uv venv --python 3.11 --path ./envs/prod
uv pip install -r requirements.txt

# 创建测试环境
uv venv --python 3.11 --path ./envs/test
uv pip install -r requirements-test.txt
```

#### 项目依赖管理最佳实践
```bash
# 1. 使用pyproject.toml管理依赖（推荐）
# pyproject.toml示例：
[project]
name = "my-project"
version = "0.1.0"
dependencies = [
    "fastapi>=0.100.0",
    "uvicorn[standard]>=0.23.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "black>=23.0.0",
    "mypy>=1.5.0",
]
docs = [
    "mkdocs>=1.5.0",
    "mkdocs-material>=9.0.0",
]

# 2. 从pyproject.toml安装
uv pip install .                    # 安装核心依赖
uv pip install ".[dev]"             # 安装核心+开发依赖
uv pip install ".[dev,docs]"        # 安装所有依赖

# 3. 更新依赖
uv update --all                     # 更新所有包
uv update fastapi                   # 更新特定包

# 4. 生成requirements.txt（用于兼容性）
uv export --exact > requirements.txt
uv export --exact --with dev > requirements-dev.txt
```

### 环境与项目移除

#### 移除虚拟环境
```bash
# 基本移除命令
uv venv remove .venv                     # 移除当前目录的.venv环境
uv venv remove myenv                     # 移除名为myenv的环境
uv venv remove --path ./envs/prod        # 移除指定路径的环境

# 移除前检查（安全操作）
uv venv list                             # 先查看所有环境
uv venv info .venv                       # 查看要移除的环境信息

# 强制移除（跳过确认）
uv venv remove .venv --force

# 批量移除（结合其他工具）
# Linux/macOS: 移除所有以test-开头的环境
for env in $(uv venv list | grep "^test-" | cut -d' ' -f1); do
    uv venv remove $env
done

# Windows PowerShell: 移除所有以test-开头的环境
uv venv list | Select-String "^test-" | ForEach-Object {
    $envName = $_ -split '\s+' | Select-Object -First 1
    uv venv remove $envName
}
```

#### 移除整个项目
```bash
# 1. 安全移除流程（推荐）
# a. 退出当前环境（如果在激活状态）
deactivate
# 或（Windows）
.\.venv\Scripts\deactivate.bat

# b. 移除虚拟环境
uv venv remove .venv

# c. 移除项目生成的配置文件
rm -f pyproject.toml uv.lock requirements*.txt  # Linux/macOS
# 或 Windows:
del pyproject.toml uv.lock requirements*.txt

# d. 移除项目目录（谨慎操作！）
# 先确认目录内容
ls -la my-project/
# 再删除（需手动执行）
# rm -rf my-project/  # Linux/macOS
# 或 rmdir /s /q my-project  # Windows

# 2. 使用uv init创建的项目移除
# uv init --package创建的项目包含标准结构：
# myapp/
# ├── pyproject.toml
# ├── README.md
# ├── src/
# ├── tests/
# └── .gitignore

# 移除完整项目结构：
uv venv remove .venv
rm -rf src/ tests/  # 移除源码和测试目录
rm -f pyproject.toml README.md .gitignore

# 3. 从Git模板创建的项目移除
# 如果项目是从git clone创建的：
uv venv remove .venv
# 保留.git目录用于版本控制，或完全删除：
# rm -rf .git my-project/
```

#### 清理项目相关缓存
```bash
# 1. 清理uv缓存
uv cache clean                     # 清理过期缓存
uv cache purge                     # 清理所有缓存

# 2. 清理pip缓存（如果在环境中使用过pip）
# 先激活环境（如果存在）
.\.venv\Scripts\activate
pip cache purge
deactivate

# 3. 清理构建缓存
rm -rf build/ dist/ *.egg-info/    # 清理Python构建产物
rm -rf __pycache__/ *.pyc          # 清理Python字节码

# 4. 清理测试和覆盖率文件
rm -rf .pytest_cache/ .coverage htmlcov/
```

#### 移除最佳实践与安全建议
```bash
# 1. 删除前备份重要文件
cp pyproject.toml pyproject.toml.backup
cp requirements.txt requirements.txt.backup
uv export --exact > environment-backup.txt

# 2. 使用dry-run先检查
# 查看移除环境的影响
uv venv remove .venv --dry-run

# 3. 分阶段删除（避免误删）
# 第一阶段：只删除环境
uv venv remove .venv
# 第二阶段：删除配置文件
rm -f pyproject.toml uv.lock
# 第三阶段：删除源码（最后进行）

# 4. 版本控制集成
# 如果使用git，先提交更改再删除
git add .
git commit -m "备份当前状态"
# 然后进行移除操作

# 5. 项目依赖树分析（删除前了解影响）
uv pip show --tree                 # 显示依赖树
uv pip check                       # 检查依赖冲突
```

#### 特殊场景处理
```bash
# 1. 多环境项目移除
# 开发、测试、生产环境分别移除
uv venv remove --path ./envs/dev
uv venv remove --path ./envs/test
uv venv remove --path ./envs/prod

# 2. 可编辑模式安装的包
# 如果使用 uv pip install -e . 安装
uv pip uninstall -e .              # 卸载可编辑包
uv venv remove .venv               # 再移除环境

# 3. 有全局缓存的包
# 查看缓存中的项目相关包
uv cache info | grep my-project
# 清理特定包的缓存
uv cache clean --pattern "my-project*"

# 4. 容器化环境（Docker）
# Dockerfile中可能需要额外清理
# RUN uv venv remove .venv && \
#     rm -rf /root/.cache/uv /root/.cache/pip

# 5. CI/CD环境清理
# GitHub Actions等CI系统中的清理
# - name: Clean up
#   run: |
#     uv venv remove .venv || true
#     uv cache clean
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
