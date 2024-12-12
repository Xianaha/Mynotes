# ResNet

## Abstract
>Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions. We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. On the ImageNet dataset we evaluate residual nets with a depth of up to 152 layers—8× deeper than VGG nets but still having lower complexity. An ensemble of these residual nets achieves 3.57% error on the ImageNet test set. This result won the 1st place on the ILSVRC 2015 classification task. We also present analysis
on CIFAR-10 with 100 and 1000 layers.
The depth of representations is of central importance for many visual recognition tasks. Solely due to our extremely deep representations, we obtain a 28% relative improvement on the COCO object detection dataset. Deep residual nets are foundations of our submissions to ILSVRC & COCO 2015 competitions1, where we also won the 1st places on the tasks of ImageNet detection, ImageNet localization, COCO detection, and COCO segmentation.
>
我们提出了一种残差学习框架来简化比以前更深的神经网络的训练。我们明确地将这些更深的层重新表述为相对于输入层来学习的残差函数，而不是成为学习无参照的函数。
残差网络在...比赛...数据集上取得了...样的优异成绩。
## Method

1. **Batch Normalization(BN)**：

## Conclusion

## Innovation

### Solved Problems
1. **梯度消失和梯度爆炸**
梯度消失：若每一层的误差梯度小于1，反向传播时，网络越深，梯度越趋近于0。
梯度爆炸：若每一层的误差梯度大于1，反向传播时，网络越深，梯度越来越大。

2. **模型退化**
随着层数的增加，模型的预测效果越来越差。

### Disadvantages

## Links
论文链接：
[Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)
图文讲解链接：
[ResNet网络讲解](https://blog.csdn.net/weixin_44001371/article/details/134192776?ops_request_misc=%257B%2522request%255Fid%2522%253A%25221ce17e86978d3d640ba02d56ec6f49c3%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=1ce17e86978d3d640ba02d56ec6f49c3&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-134192776-null-null.142^v100^pc_search_result_base6&utm_term=ResNET&spm=1018.2226.3001.4187)