# General knoledge in Deep Learning

## Introduction

    这个笔记主要用来记录深度学习中的一些基础知识，包括但不限于基础理论和常用算法等等。

### Normalization(标准化)

标准化是指对数据进行变换，使其具有相同的量纲，即使数据分布在不同的范围内。常见的标准化方法有：

- 最小-最大标准化(Min-Max Normalization)：将数据缩放到[0,1]之间，使得数据具有相同的量纲。公式为：

$$x'=\frac{x-x_{min}}{x_{max}-x_{min}}$$

- Z-score标准化(Z-score Normalization)：将数据转换到标准正态分布，使得数据具有相同的方差和均值。公式为：

$$x'=\frac{x-mean(x)}{std(x)}$$

- 均方根标准化(Mean-Square Root Normalization)：将数据缩放到[0,1]之间，使得数据具有相同的方差。公式为：

$$x'=\frac{x}{\sqrt{\sum_{i=1}^{n}(x_i)^2}}$$

- 线性变换(Linear Transformation)：将数据线性变换到一个新的空间，使得数据具有相同的方差和均值。公式为：

$$x'=a_1x+a_2$$

其中，$a_1$和$a_2$是线性变换的系数。

### Sample and Feature in Matrix(样本和特征矩阵)

    样本矩阵：每一行代表一个样本，每一列代表一个特征(属性)。
    例如：
    ```
    [[1,2,3],
     [4,5,6],
     [7,8,9]]
    ```
    代表3个样本，每个样本有3个特征。其中，1,2,3,4,5,6,7,8,9是特征的值。`[[1,2,3],[4,5,6],[7,8,9]]`归属三个样本，`[1,2,3]`表示第一个样本的特征，`[4,5,6]`表示第二个样本的特征，`[7,8,9]`表示第三个样本的特征。而`[1,4,7]T,[2,5,8]T,[3,6,9]T`则是三种特征(属性)，其中`[1,4,7]T`表示第一种特征，`[2,5,8]T`表示第二种特征，`[3,6,9]T`表示第三种特征，其值分别属于三个样本对应该特征(属性)的值。
    
    特征矩阵：每一行代表一个特征，每一列代表一个样本。

### Activation Function(激活函数)

激活函数是神经网络的关键，它决定了神经网络的输出。常见的激活函数有：

- Sigmoid函数：$f(x)=\frac{1}{1+e^{-x}}$，输出范围为(0,1)。

- Tanh函数：$f(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}$，输出范围为(-1,1)。

- ReLU函数：$f(x)=max(0,x)$，输出范围为(0,∞)。

- Leaky ReLU函数：$f(x)=max(0.01x,x)$，输出范围为(0,∞)。

- ELU函数：$f(x)=\begin{cases}x, & x\geq0 \\ \alpha(e^x-1), & x<0 \end{cases}$，输出范围为(-∞,∞)。

- Softmax函数：$f(x_i)=\frac{e^{x_i}}{\sum_{j=1}^{n}e^{x_j}}$，输出范围为(0,1)，用于多分类问题。

## Common libraries 
记录一些常用的深度学习库。

### torch
`torch`是一个基于张量(tensor)的科学计算库，可以用来进行机器学习、深度学习等相关的计算。

使用：
```python
import torch
```
**模型保存和加载**：
`torch.save(obj, f)`，其中`obj`是要保存的对象，`f`是保存文件的路径。  
通常与`.state_dict()`一起使用，保存模型参数。
`model.state_dict()`方法返回一个字典，包含了模型的权重和偏置。
```python
torch.save(model.state_dict(), 'path/to/save/file.pth')
```

`torch.load(f)`，其中`f`是保存文件的路径。  
通常与`.load_state_dict()`一起使用，加载模型参数。
```python
model.load_state_dict(torch.load('path/to/save/file.pth'))
```

**文件格式**：

- `.pt`：保存的模型参数和优化器状态。
- `.pth`：保存的模型参数。
- `.onnx`：保存的神经网络结构和参数。  

其中，`.pt`和`.pth`这两种扩展名通常可以互换使用，都是用于保存模型的结构和权重。PTH更常见于保存完整模型，而PT则可能更多地用于脚本模型或者逻辑模型。

而`onnx`全称是Open Neural Network Exchange，是一种开放的神经网络交换格式。它的设计目的是为了实现不同深度学习框架之间的互操作性，例如可以将PyTorch模型导出为ONNX格式，然后在其他框架（如TensorFlow、MXNet等）中使用。


#### torch.nn
`torch.nn`是一个神经网络模块，用于构建和训练神经网络。

使用：
```python
import torch.nn as nn
#  from torch import nn
```

构建一个简单的神经网络：
```python
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        pass
        # 定义各种网络结构：
        # 需要保证各层的输入数据的维度和输出数据的维度一致
        # self.fc1 = nn.Linear(in_features, out_features)
        # self.conv1 = nn.Conv2d(in_channels = 1, out_channels = 6, kernel_size = 5, stride = 1, padding = 0)
        # self.pool = nn.MaxPool2d(kernel_size = 2, stride = 2)
        


    def forward(self, x):
        pass
        # 定义网络的前向传播过程
        # x = self.fc1(x)
        # x = self.conv1(x)
        # x = self.pool(x)
        # x = F.relu(x)
        # x = x.view(x.size(0), -1)
        # return x
```
这里可以使用torchsummary库来查看神经网络的结构：
```python
from torchsummary import summary
summary(Net, input_size=(3, 224, 224))
```

#### torch.nn.functional
`torch.nn.functional`是一个函数库，包含了神经网络的常用函数。

使用：
```python
import torch.nn.functional as F
```

#### torch.utils.data.DataLoader
`torch.utils.data.DataLoader`是一个数据加载器，用于加载和预处理数据集。它的作用包括：

- 批量加载数据：DataLoader 可以将数据集分成多个小批次，便于模型进行训练和评估。

- 随机打乱数据：它可以在每个 epoch 开始时打乱数据，帮助提高模型的泛化能力。

- 支持多线程加载：DataLoader 可以利用多线程来加速数据加载过程，尤其是在处理大型数据集时，这能够有效减少模型训练的时间。

- 自动处理数据集的迭代：使用 DataLoader 可以方便地迭代数据集，简化训练循环的编写。

- 集成数据预处理：可以直接在数据加载过程中进行必要的数据预处理操作，比如数据增强、归一化等

使用：
```python
from torch.utils.data import DataLoader
```
`DataLoader(dataset, batch_size=1, shuffle=False, sampler=None, batch_sampler=None, num_workers=0, collate_fn=None, pin_memory=False, drop_last=False, timeout=0, worker_init_fn=None)`其中：
- dataset（必填）：要加载的数据集对象，它必须是一个实现了`__len__`和`__getitem__`方法的类。

- batch_size（可选）：每个批次的样本数量，默认为 1。

- shuffle（可选）：是否在每个 epoch 开始时打乱数据，默认为 False。

- sampler（可选）：自定义数据抽样策略的对象。如果提供了 sampler，shuffle 参数将被忽略。

- num_workers（可选）：用于数据加载的子进程数量，默认为 0（表示不使用多线程）。

- collate_fn（可选）：用于将一批样本合并为一个小批量的函数，默认为 None。

- pin_memory（可选）：如果为 True，DataLoader 会将数据加载到 pinned memory 中，有助于提高 GPU 加载速度。

- drop_last（可选）：如果为 True，则在数据集大小不能被 batch_size 整除时丢弃最后一个小批量，默认为 False。

- timeout（可选）：加载数据的超时时间。
  
- worker_init_fn（可选）：用于初始化每个工作进程的函数。
例如：
```python
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
```



#### torch.utils.data.Dataset
`torch.utils.data.Dataset`是一个抽象类，用于定义数据集。通过继承`Dataset`类，可以自定义自己的数据集。

使用：
```python
from torch.utils.data import Dataset
```

在PyTorch中，自定义数据集类需要继承 `torch.utils.data.Dataset`类，并实现以下几个方法：

- `__init__(self, root, transform=None)`：构造函数，用于初始化数据集，包括数据集的根目录和数据转换方式。
- `__len__(self)`：返回数据集的样本数量。
- `__getitem__(self, index)`：返回指定索引的样本，包括图像和标签。

以下是一个自定义数据集类的例子：

```python
import os # 对文件和目录进行操作
from PIL import Image # 图像处理库
from torch.utils.data import Dataset # 自定义数据集类
class MyDataset(Dataset): # 继承Dataset类
    def __init__(self, root, transform=None):
        self.root = root # 数据集根目录
        self.transform = transform # 已经定义好的数据转换方式
        self.imgs = [] # 存放样本的特征矩阵
        self.labels = [] # 存放样本的标签列表
        # 遍历目录，将图片转化的特征矩阵和其对应类别标签添加到imgs和labels列表中
        for label, class_dir in enumerate(os.listdir(root)):
            class_path = os.path.join(root, class_dir)
            if os.path.isdir(class_path):
                for img_file in os.listdir(class_path):
                    img = Image.open(os.path.join(class_path, img_file)).convert("RGB") # 以RGB模式打开图片
                    if self.transform:
                        img = self.transform(img) # 将图像转换后再存放
                    self.imgs.append(img)
                    self.labels.append(label)
        self.labels = [x - 1 for x in self.labels]  # 标签从0开始，这里将标签从1开始。CrossEntropyLoss 要求目标标签在 [0, C-1] 范围内
      
    def __len__(self):
        return len(self.imgs)
  
    def __getitem__(self, index): # 使得数据集对象能够像列表一样使用索引访问到样本的特征矩阵和标签
        img = self.imgs[index]
        label = self.labels[index]
        # print(f"Fetching index {index}: Image {img}, Label {label}")  # 打印取出的样本和标签
        return img, label

# 实例化自定义数据集对象
dataset = MyDataset(root="D:\Code\VScode_Python\datasets\Cats, Dogs, and Foxes", transform=transform)
```

由于train_test_split函数会将训练集和测试集的数据和标签分开，所以通常还需要重新将将数据和标签绑定到一个对象中。
这里可以自定义一个类来封装数据和标签，并实现 `__getitem__`方法，使得数据集对象能够像列表一样使用索引访问到样本的特征矩阵和标签。
注意：这里组合前，样本已经经过了数据转换，所以不需要再次转换。

```python
class SubsetDataset(Dataset):
    def __init__(self, img_list, label_list):
        self.imgs = img_list
        self.labels = label_list

    def __len__(self):
        return len(self.imgs)

    def __getitem__(self, idx):
        return self.imgs[idx], self.labels[idx]

# 将数据和标签绑定到一个对象中，通过SubsetDataset类实例化训练集和测试集对象
train_dataset = SubsetDataset(train_data, train_labels)
test_dataset = SubsetDataset(test_data, test_labels)
```

### torchvision
`torchvision`是一个用于计算机视觉任务的库，它提供了常用的数据集、模型和图像变换。

安装：
```
pip install torchvision
```

使用：
```python
import torchvision
```

常用的数据集：
- CIFAR10：CIFAR-10 数据集，包含 60,000 张 32x32 像素的彩色图像，共 10 个类别。
- CIFAR100：CIFAR-100 数据集，包含 60,000 张 32x32 像素的彩色图像，共 100 个类别。
- MNIST：MNIST 数据集，包含 60,000 张 28x28 像素的灰度图像，共 10 个类别。
- FashionMNIST：FashionMNIST 数据集，包含 60,000 张 28x28 像素的灰度图像，共 10 个类别。
- ImageNet：ImageNet 数据集，包含 1,281,167 张 224x224 像素的彩色图像，共 1000 个类别。

常用的数据变换：

### torchsummary
`torchsummary`是一个用于打印神经网络模型结构的库。通过这个库，可以方便地查看模型的结构，包括每一层的输入输出维度、每一层的激活函数、每一层的参数数量等。

安装：
```
pip install torchsummary
```

使用：
```python
from torchsummary import summary
```

`summary(model, input_size)`，其中`model`是需要打印结构的神经网络模型，`input_size`是输入的图像大小。
`summary()`会打印出模型的结构，包括每一层的输入输出维度、每一层的激活函数、每一层的参数数量等。其依照的是`forward()`的定义运作，所以需要定义好`forward()`函数。
```python
# 定义CNN网络结构
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        # 第一层：卷积层 + 激活层 + 池化层
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)  # 输入3通道，输出16通道
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)   # 最大池化层，大小2x2
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1) # 输入16通道，输出32通道
        
        # 全连接层
        self.fc1 = nn.Linear(32 * 32 * 32, 128)   # 输入维度为32x32x32，输出维度为128
        self.fc2 = nn.Linear(128, 3)    # 输入维度为128，输出维度为3
        
    def forward(self, x):
        x = self.pool(fct.relu(self.conv1(x)))
        x = self.pool(fct.relu(self.conv2(x)))
        x = x.view(-1, 32 * 32 * 32)
        x = fct.relu(self.fc1(x))
        x = self.fc2(x)
        return x
summary(CNN(), (3, 128, 128))

>>>
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1         [-1, 16, 128, 128]             448
         MaxPool2d-2           [-1, 16, 64, 64]               0
            Conv2d-3           [-1, 32, 64, 64]           4,640
         MaxPool2d-4           [-1, 32, 32, 32]               0
            Linear-5                  [-1, 128]       4,194,432
            Linear-6                    [-1, 3]             387
================================================================
Total params: 4,199,907
Trainable params: 4,199,907
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.19
Forward/backward pass size (MB): 3.75
Params size (MB): 16.02
Estimated Total Size (MB): 19.96
----------------------------------------------------------------
```

