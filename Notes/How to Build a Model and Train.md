# How to Build a Model
不懂的地方可以查看[General Knowledge In DL](./General%20Knowledge%20In%20DL.md)，这个笔记只记载大值的流程套路。
## Building a Model

### Data Preparation

模型的上限取决于数据集的质量。

#### Data Cleaning

对于自己制作的数据集可能存在一些噪声或错误，需要进行数据清洗。
这一步可能使用到自动化脚本，对数据进行批处理，包括但不限于缺失值处理、异常值处理、重复值处理等。除此之外，对于数据文件报错、数据格式不一致等问题，也需要进行数据清洗。在[Script](./Script/)文件夹中提供了一些数据清洗脚本。

#### Data Transformation

数据预处理的另一个重要环节是数据转换。数据转换是指对数据进行特征工程，包括特征选择、特征缩放、特征编码等。常见的数据转换方式包括归一化、标准化、PCA、特征选择等。

在PyTorch中，常用的特征转换方式包括：

```python
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
])
```

- transforms.Resize()用于调整图像大小，也可以理解为H * W的像素值。
- transforms.ToTensor()用于将图像转换为Tensor格式，即[C, H, W]。其中C为通道数，H为高度，W为宽度。
- transforms.Normalize()用于归一化图像。对于黑白图像，一般使用(mean, std) = (0.5, 0.5)；对于彩色图像，一般使用(mean, std) = (0.485, 0.456, 0.406)和(0.229, 0.224, 0.225)。

#### Using public datasets

公共数据集往往已经经过了数据清洗和转换，可以直接使用。其次，调用时可以直接加载数据集处理好的训练集和测试集，不需要再次进行数据处理。

#### Definition of a custom dataset class

很多时候我们需要自己制作数据集，在完成数据清洗工作和转换后，我们需要定义一个自定义数据集类。该类的实例化对象能确保能够将数据集中的样本按照指定方式组织起来，并能够通过索引访问到样本。

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

#### Data Splitting

将数据集划分为训练集、验证集和测试集，是模型训练、评估和部署的重要环节。
公开数据集一般已经划分好了训练集、验证集和测试集，我们只需要按照比例将数据集划分到不同的子集中即可。
自己的数据集使用sklearn库中的 `train_test_split`函数可以很方便地将数据集划分为训练集和测试集。

```python
from sklearn.model_selection import train_test_split

train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=0.2, random_state=42)
# test_size表示测试集占总数据集的比例，random_state表示随机种子（一般使用42保证结果的一致性），用于保证划分的一致性。
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

#### Data loading

使用数据加载器（DataLoader）加载数据集，可以将数据集分批次加载到内存中，提高训练效率。数据加载器有以下几个优点：

- 批处理（Batching）：数据加载器可以将数据集分成多个小批次，这样可以有效地进行模型训练，提高训练效率和收敛速度。
- 随机打乱（Shuffling）：在训练过程中，随机打乱数据可以防止模型过拟合，提高模型的泛化能力。数据加载器可以在每个 epoch 开始前自动打乱数据。
- 并行加载（Parallel Loading）：数据加载器通常支持多线程或多进程的数据加载，这样可以加速数据读取过程，使得数据加载不会成为训练的瓶颈。
- 预处理（Preprocessing）：数据加载器可以在加载数据时进行必要的预处理，如数据增强、归一化等，从而简化训练代码，提高数据处理的效率。
- 内存管理（Memory Management）：通过数据加载器，可以按需加载数据，避免将整个数据集一次性加载到内存中，从而节省内存。

在Pytorch中使用数据加载器可以用 `torch.utils.data.DataLoader`类来实现。

```python
from torch.utils.data import DataLoader

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, num_workers=4)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False, num_workers=4)
```

这里的 `batch_size`参数表示每个批次的样本数量，`shuffle`参数表示是否打乱数据，`num_workers`参数表示加载数据时的线程数，默认为0，表示使用主线程加载数据。
每个批次的样本数量越大，训练效率越高，但是内存占用也会增大。
样本中的数据应包含图像矩阵和标签，以便训练时能够正常访问。

### Model Construction
这个部分主要介绍模型的构建过程，包括模型架构、损失函数、优化器等。

#### Model Architecture
定义一个模型架构，可以选择不同的模型结构，如卷积神经网络、循环神经网络、递归神经网络等。
模型架构细节可以参考[General Knowledge In DL](./General%20Knowledge%20In%20DL.md)中`torch.nn`模块的介绍。
```python
class simpleNet(nn.Module):
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
```


#### Loss Function

#### Optimizer

## Model Evaluation

## Model Deployment
