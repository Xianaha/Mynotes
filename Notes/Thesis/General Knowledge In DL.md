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