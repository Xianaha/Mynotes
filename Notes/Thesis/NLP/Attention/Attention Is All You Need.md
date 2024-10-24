# Title: Attention Is All You Need

## Abstract：

>The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. 
>
目前主流的序列转换模型都是基于复杂的循环或卷积神经网络，其中包含编码器和解码器。
>The best performing models also connect the encoder and decoder through an attention mechanism. 
>
最佳性能的模型还通过注意力机制连接编码器和解码器。
>We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.
>
我们提出了一个新的简单网络架构，即Transformer，仅使用注意力机制，完全抛弃了循环和卷积。 
>Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train.
>
在两个机器翻译任务上的实验表明，这些模型的质量优于现有最佳结果，并能更好地并行化，且训练时间更少。
>Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. 
>
我们的模型在WMT 2014英语-德语翻译任务上达到了28.4 BLEU，超过了现有最佳结果，包括集成模型，提高了2个BLEU。
>On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. 
>
在WMT 2014英语-法语翻译任务上，我们的模型建立了一个新的单模型的BLEU得分，即41.8，在8个GPU上训练3.5天，相比于文献中最佳模型的训练成本，少得多。
>We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.
>
我们表明，Transformer在其他任务上也能良好地泛化，通过将其成功应用于英语句法分析任务，无论是有限的训练数据还是大量的训练数据。

## Method：

![Transformer architecture](<Transformer%20architecture.png>)

![Transformer architecture with functions](<Transformer%20architecture%20with%20function.png>)

![concise transformer architecture](<concise%20Transformer.png>)

### Encoder and Decoder Stacks

![Encoder and Decoder](<Encoder-Decoder.png>)

![Encoder and Decoder Inside](<Encoder-Decoder%20Inside.png>)

>Here, the encoder maps an input sequence of symbol representations (x1, ..., xn) to a sequence of continuous representations z = (z1, ..., zn).
>
在这里，编码器将输入向量表示序列(x1, ..., xn)映射到连续表示序列z=(z1, ..., zn)中。

> Given z, the decoder then generates an output sequence (y1, ..., ym) of symbols one element at a time.
>
编码器给予解码器Z，解码器逐个生成输出向量序列(y1, ..., ym)。

> At each step the model is auto-regressive, consuming the previously generated symbols as additional input when generating the next.
>
在生成yt的每一步，模型是自回归的，在生成下一个输出时，会将之前生成的向量作为额外输入。即过去时刻的输出yt将作为下一个输出y(t+1)的输入。

#### Encoder

![Encoder Unit](<Encoder.png>)

>The encoder is composed of a stack of N = 6 identical layers. Each layer has two sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, position-wise fully connected feed-forward network.
>
编码器由N=6个相同层组成。每一层都有两个子层。第一个子层表达多头自注意力机制，第二个子层表达简单的、位置无关的全连接前馈网络（一个简单的感知机）。

数据经过self-attention模块后得到一个加权之后的特征向量Z，这个特征向量Z包含了输入序列的全部信息。Z由公式Attention(Q,K,V)得到：
$$Attention(Q,K,V)=softmax(\frac{QK^T}{\sqrt{d_k}})V$$  
其中Q,K,V分别是输入序列的特征向量，Q,K的维度都是d_k，V的维度是d_v。

得到的特征向量Z会被送入Feed-Forward Nerual Network中，该全连接神经网络有两层，第一层是激活函数ReLU，第二层是一个线性激活函数。该函数可以表达为：
$$FFN(x)=max(0,xW_1+b_1)W_2+b_2$$
其中x是输入向量，W_1,b_1,W_2,b_2是权重和偏置。

以上过程会重复N次，得到N个特征向量Z，然后将这些特征向量Z拼接起来，作为输出。同时该输出将会进入到Decoder中，作为Decoder的输入。

#### Decoder
>The decoder is also composed of a stack of N = 6 identical layers. In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack.
>
解码器也是由N=6个相同层组成。除了每个编码器层中的两个子层之外，解码器还插入了一个第三个子层，该子层对编码器堆栈的输出执行多头注意力。

>Similar to the encoder, we employ residual connections around each of the sub-layers, followed by layer normalization.
>
与编码器相似，我们在每个子层周围都插入残差连接，并进行层归一化。

>We also modify the self-attention sub-layer in the decoder stack to prevent positions from attending to subsequent positions. This masking, combined with fact that the output embeddings are offset by one position, ensures that the predictions for position i can depend only on the known outputs at positions less than i.
>
我们还修改了解码器堆栈中的自注意力子层，以防止当前位置的注意力依赖后续位置的信息。这种屏蔽机制与输出的嵌入向量是一个位置偏移的情况相结合，可以确保位置i的预测仅依赖于位置i之前的已知输出。

### Attention
>An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key.
>
注意力函数可以描述为将查询和一组键-值对映射到输出，其中查询、键、值和输出都是向量。输出是通过对值进行加权求和得到的，权重是通过查询与相应键的兼容性函数计算得到的。
#### Scaled Dot-Product Attention
![alt text](<Scaled Dot-Product Attention.png>)
>We call our particular attention "Scaled Dot-Product Attention". The input consists of queries and keys of dimension dk, and values of dimension dv. We compute the dot products of the query with all keys, divide each by $\sqrt{d_k}$, and apply a softmax function to obtain the weights on the values.
>
我们将特定的注意力机制命名为“缩放点积注意力”。输入由查询和键的维度dk和维度的值dv组成。我们对查询与所有键的点积进行除以$\sqrt{d_k}$，并应用softmax函数来获得值上的权重。
>In practice, we compute the attention function on a set of queries simultaneously, packed together into a matrix Q. The keys and values are also packed together into matrices K and V . We compute the matrix of outputs as:
$$Attention(Q,K,V)=softmax(\frac{QK^T}{\sqrt{d_k}})V$$
>
实际上，我们对一组查询同时进行注意力计算，将其打包成矩阵Q。键和值也被打包成矩阵K和V。我们计算输出矩阵如下：
$$Attention(Q,K,V)=softmax(\frac{QK^T}{\sqrt{d_k}})V$$
其中Q,K,V分别是输入序列的特征向量，Q,K的维度都是d_k，V的维度是d_v。
>The two most commonly used attention functions are additive attention , and dot-product (multi-plicative) attention. Dot-product attention is identical to our algorithm, except for the scaling factor
of √1dk. Additive attention computes the compatibility function using a feed-forward network with a single hidden layer. While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code.
>
两种最常用的注意力函数是加性注意力和点积注意力。点积注意力与我们的算法相同，只是除以了$\sqrt{d_k}$。加性注意力则使用一个单层隐藏的前馈网络来计算兼容函数。虽然两者在理论复杂度上类似，但点积注意力在实践中更快、更节省空间，因为它可以使用高度优化的矩阵乘法代码来实现。
>While for small values of dk the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of dk [3]. We suspect that for large values of dk, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients 4. To counteract this effect, we scale the dot products by √1dk
>
#### Multi-Head Attention
![alt text](<Multi-Head Attention.png>)
### Position-wise Feed-Forward Networks

### Embeddings and Softmax

### Positional Encoding

## Conclusion：

>In this work, we presented the Transformer, the first sequence transduction model based entirely on attention, replacing the recurrent layers most commonly  encoder-decoder architectures with multi-headed self-attention.
>
在这项工作中，我们介绍了Transformer，一种完全基于注意力的序列转换模型，它通过多头自注意力机制取代了大多数基于编码器-解码器架构的循环层。
>For translation tasks, the Transformer can be trained significantly faster than architectures basedon recurrent or convolutional layers.
>
对于翻译任务，Transformer的训练速度要快于基于循环或卷积层的架构。
>On both WMT 2014 English-to-German and WMT 2014 English-to-French translation tasks, we achieve a new state of the art. In the former task our best model outperforms even all previously reported ensembles. 
>
在WMT 2014英语-德语和WMT 2014英语-法语翻译任务上，我们达到了新的领先水平。在前者任务中，我们的最佳模型甚至超过了所有先前报道的集成模型。
>We are excited about the future of attention-based models and plan to apply them to other tasks. 
>
我们对基于注意力的模型的未来充满激情，并计划将其应用于其他任务。
>We plan to extend the Transformer to problems involving input and output modalities other than text and to investigate local, restricted attention mechanisms to efficiently handle large inputs and outputs such as images, audio and video. 
>
我们计划将Transformer扩展到涉及其他输入和输出模式的任务，如图像、音频和视频等大型输入和输出。
>Making generation less sequential is another research goals of ours. The code we used to train and evaluate our models is available at https://github.com/tensorflow/tensor2tensor.
>
我们计划研究生成式模型的非序列性。我们提供的代码用于训练和评估我们的模型，可在https://github.com/tensorflow/tensor2tensor找到。

## Innovation：

## Solve Problems：

## Disadvantage：

## Links

[原文链接](https://arxiv.org/pdf/1706.03762)

[Transformer原理图文讲解](https://jalammar.github.io/illustrated-transformer/)

[Transformer原理动画演示](https://www.bilibili.com/video/BV1tSHVeYEdW?vd_source=1e4713cfa8e350de3a5d5debd2321c1d)

[Transformer 原理讲解](https://blog.csdn.net/weixin_42475060/article/details/121101749?ops_request_misc=%257B%2522request%255Fid%2522%253A%252267B72B1C-98AD-4F50-822B-11F2374EC6CC%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=67B72B1C-98AD-4F50-822B-11F2374EC6CC&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-121101749-null-null.142^v100^pc_search_result_base6&utm_term=Transformer&spm=1018.2226.3001.4187)