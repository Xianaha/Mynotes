# Hugging Face

## huggingface_hub

- 安装 huggingface_hub
```python
! conda install huggingface_hub
```

- 配置镜像地址
```python
! export HF_ENDPOINT=https://hf-mirror.com
! source ~/.profile # 使配置生效
```

- 通过huggingface_hub下载模型
```python
! huggingface-cli download --resume-download --local-dir-symlinks <model_name> --local-dir <model_dir>
```
其中，`<model_name>`为模型名称，`<model_dir>`为模型下载目录。
--resume-download：表示断点续传，即如果下载过程中出现错误，可以从上次下载的位置继续下载。
--local-dir-symlinks：表示下载后的模型文件会创建软链接到`<model_dir>`目录下。
