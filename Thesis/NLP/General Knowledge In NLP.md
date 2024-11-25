# General Knowledge In NLP

To note down the general knowledge in NLP.

## BLEU Score (Bilingual Evaluation Understudy)

BLEU的计算公式可以表示为：

$$
BLEU = BP \times exp( \sum_{i=1}^{N} w_n\log P_i)
$$

BLEU 是一种用于评估机器翻译效果的自动化指标。他通过比较机器翻译输出与一个或多个参考翻译的相似性来评估翻译效果。BLEU分数的范围通常是从0到1，1表示完全匹配，0表示完全不匹配。
BLEU的主要特点和计算原理如下：

### n-gram 精度 (Pn-gram precision)

BLEU将被评估的翻译与参考翻译分成n-gram（即连续的n个word的序列），并计算每个n-gram的匹配程度。n-gram的数量可以是1到4，通常取2或3。然后，BLEU将计算机器翻译中与参考翻译中每个n-gram的匹配程度，并取平均值作为整个句子的匹配程度，即：Pn-gram。
其中n=1时，n-gram越高表达语句中单个word被翻译出来的准确性越高；当n>=2时，n-gram越高表达翻译出来的连续words越多，语句翻译出来的语句越流畅。
Pn的计算公式为：

$$
Pn = \frac{count(n-gram \in machine\ translation)}{count(n-gram \in reference\ translation)}
$$

### 召回率（Recall，Pavg）

原文：猫站在地上

机器译文：the the the the

人工译文：The cat is standing on the ground

在计算1-gram的时候，the 都出现在译文中，因此匹配度为4/4 ，但是很明显 the 在人工译文中最多出现的次数只有2次，因此BLEU算法修正了这个值的算法，首先会计算该n-gram在译文中可能出现的最大次数：

$$
Count(clip) = min(Count, Count(reference))
$$

Count是N-gram在机器翻译译文中的出现次数，Count(reference)是该N-gram在一个参考译文中最大的出现次数，最终统计结果取两者中的较小值。然后在把这个匹配结果除以机器翻译译文的N-gram个数。因此对于上面的例子来说，修正后的1-gram的统计结果就是2/4。
译文整体的准确率等于各n-gram 的加权平均：

$$
Pavg = exp( \sum_{i=1}^{N} w_n\log P_i)
$$

这里解释一下这个公式，N代表的总共的单词元组，例如，n=1时就是1-gram，一元组。wn是指当前单词元组下所占有的权重比，所有的权重比相加应当为1。从公式可以看出BLEU的取值范围是（0,1]，0最差，1最好。这里值得注意的是，当所有的权重值是均分的时候，这里所有元组的平均值就是算术平均值。

### 短句惩罚因子（short sentence penalty factor, BP）

短句惩罚因子是指当n-gram匹配度可能会随着句子长度的变短而变高，因此会存在这样一个问题：翻译引擎只翻译出句子中部分句子且翻译的比较准确，那么n-gram精度依旧很高，而短句惩罚因子则是用来抑制这种现象的。
为了避免这种评分的偏向性，BLEU在最后评分的结果中引入了BP。
BP 的计算公式为：

$$
BP = min(1, e^{-1 \times \frac{r}{c}})
$$

其中 c 是机器翻译的句子长度，r 是参考翻译的句子长度。
