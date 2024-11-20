import matplotlib.pyplot as plt
import torch
from torchvision import transforms
from torch.utils.data import DataLoader, Dataset
from torch import nn
import torch.nn.functional as fct
import numpy as np
import os
from PIL import Image
from sklearn.model_selection import train_test_split

# 预处理数据
transform = transforms.Compose({
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
})

# 加载数据
class MyDataset(Dataset):
    def __init__(self, root, transform=None):
        self.root = root
        self.transform = transform
        self.imgs = []
        self.labels = []
        # 遍历目录，将图片路径和其对应类别标签添加到imgs和labels列表中
        for label, class_dir in enumerate(os.listdir(root)):
            class_path = os.path.join(root, class_dir)
            if os.path.isdir(class_path):
                for img_file in os.listdir(class_path):
                    self.imgs.append(os.path.join(class_path, img_file))
                    self.labels.append(label)
        
    def __len__(self):
        return len(self.imgs)
    
    def __getitem__(self, index):
        img = Image.open(self.imgs[index]).convert("RGB")
        label = self.labels[index]
        if self.transform:
            img = self.transform(img)
        return img, label

dataset = MyDataset(root="D:\Code\VScode_Python\datasets\Cats, Dogs, and Foxes", transform=transform)
data = dataset.imgs
labels = dataset.labels

# 划分训练集和测试集
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=0.2, random_state=42)

# 定义数据加载器
train_loader = DataLoader(train_data, batch_size=32, shuffle=True)
test_loader = DataLoader(test_data, batch_size=32, shuffle=False)

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
    
# 实例化模型
model = CNN()

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# GPU加速
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)

# 训练模型
epochs = 100
for epoch in range(epochs):
    running_loss = 0.0
    for images, labels in train_data:
        images, labels = images.to(device), labels.to(device)
        
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backwards()
        optimizer.step()
        
        running_loss += loss.item()
        
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {running_loss/len(train_loader):.4f}')