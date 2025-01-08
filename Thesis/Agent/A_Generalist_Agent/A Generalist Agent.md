# A Generalist Agent

## Abstract
>The agent, which we refer to as Gato, works as a multi-modal, multi-task, multi-embodiment generalist policy.
>
我们所指的是Gato的代理，它作为一个多模态、多任务、多身体表现形式的通用策略工作。

## Introduction
>In this paper, we describe the current iteration of a general-purpose agent which we call Gato, instantiated as a single, large, transformer sequence model. With a single set of weights, Gato can engage in dialogue, caption images, stack blocks with a real robot arm, outperform humans at playing Atari games, navigate in
simulated 3D environments, follow instructions, and more.
>
在本文中，我们描述了当前迭代的一个通用代理，我们称之为Gato，其实例化为一个单一的大型Transformer序列模型。凭借一组权重，Gato可以进行对话、为图像添加标题、使用真实的机器人臂堆叠积木、在玩Atari游戏方面超越人类、在模拟的3D环境中导航、遵循指令等。

## Method

### Model
>The guiding design principle of Gato is to train on the widest variety of relevant data possible, including diverse modalities such as images, text, proprioception, joint torques, button presses, and other discrete and continuous observations and actions. To enable processing this multi-modal data, we serialize all data into a flat sequence of tokens. In this representation, Gato can be trained and sampled from akin to a standard large-scale language model. During deployment, sampled tokens are assembled into dialogue responses, captions, button presses, or other actions based on the context. In the following subsections, we describe Gato’s tokenization, network architecture, loss function, and deployment.
>
Gato的设计指导原则是在尽可能广泛的相关数据集上进行训练，包括各种模态的数据，如图像、文本、本体感觉、关节扭矩、按钮按下以及其他离散和连续的观察与动作。为了处理这种多模态数据，我们将所有数据序列化为一个扁平化的令牌序列。在这种表示中，Gato可以像标准的大规模语言模型一样进行训练和采样。在部署过程中，采样的令牌会根据上下文组装成对话响应、字幕、按钮按下或其他动作。在接下来的小节中，我们将描述Gato的令牌化方法、网络架构、损失函数及其部署方式。

### Tokenization
将数据转换成Tokens的方式：
- Text
    文本通过SentencePiece进行编码，将32000个子词单位转换成[0, 32000)的整数表示。
- Image
    图像首先被转换成非重叠的16x16的像素块序列，顺序为光栅顺序（参考ViT）。然后，图像块的每一个像素被归一化到区间[-1, 1]，并且除以块大小的平方根（即$\sqrt{16} = 4$）。
- Discrete values
    离散值，将所有可能的离散值映射成一个整数序列，按行（一个数据点作为一行）优先。（如性别、婚姻等，一个未婚男性被映射成(1, 0)）。Tokenization的结果是一个在区间[0, 1024)内的整数序列。
- Continuous values
    连续值，按行优先顺序展平为浮点值序列。如果这些值不在[-1, 1]范围内，则通过μ-law编码将其转换到此范围。然后将这些值均匀离散化到1024组中，最后这些离散整数被移动到[32000, 33024)的范围内。

### Embedding input tokens and setting output targets
通过处理后的Tokens和序列关系，把多模态信息转换成一个包含该信息的嵌入函数作为模型输入。
- 对于文本、离散或连续值或动作的Token，无论时序如何，都通过查表法找到对应的嵌入向量嵌入到向量空间中、对于这些向量，再通过他们的时序信息插入位置编码。
- 对于图像，通过单个ResNET模块对每一个patch进行嵌入以获得每一个patch的向量，然后再嵌入一个可学习的图像内部的位置信息编码。
模型使用自回归方式对数据进行建模。


## Conclusion

## Innovation

### Solved Problem

### Disvantages

## Links