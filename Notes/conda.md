# Conda指令

## 常用指令

`conda info` 显示conda版本信息。

 `conda create -n env_name python=3.10` 创建一个名为env_name的环境，指定python版本为3.10。

 `conda activate env_name` 激活env_name环境。

 `conda deactivate` 退出当前环境。

 `conda install package_name` 安装package_name包。完整指令为：`conda install package_name=version`，其中version表示版本号，可选。

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