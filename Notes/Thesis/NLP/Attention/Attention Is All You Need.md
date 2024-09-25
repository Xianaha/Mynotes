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

![Transformer architecture](/Notes/Thesis/NLP/Attention/Transformer%20architecture.png "Transformer architecture")

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