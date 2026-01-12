# SAGE：具有反思与记忆增强能力的自进化智能体

Xuechen Liang $^{1*}$ , Yangfan He $^{2*}$ , Yinghui Xia $^{3*}$ , Xinyuan Song $^{4}$ , Jianhui Wang $^{5}$ , Meiling Tao $^{6}$ , Li Sun $^{7}$ , Xinhang Yuan $^{8}$ , Jiayi Su $^{9}$ , Keqin Li $^{10}$ , Jiaqi Chen $^{10}$ , Jinsong Yang $^{3*}$ , Siyuan Chen $^{10}$ , Tianyu Shi $^{11\dagger}$

`<sup>`1`</sup>` 华东交通大学，`<sup>`2`</sup>` 明尼苏达大学双城分校，`<sup>`3`</sup>` AutoAgents.ai，`<sup>`4`</sup>` 埃默里大学，
`<sup>`5`</sup>` 电子科技大学，`<sup>`6`</sup>` 广东工业大学，
$^{7}$ 亚马逊，$^{8}$ 华盛顿大学，$^{9}$ 厦门大学，
$^{10}$ 独立研究员，$^{11}$ 布里斯托大学，$^{12}$ 多伦多大学
项目页面：https://jianhuiwemi.github.io/SAGE

# 摘要

大语言模型（LLMs）在自然语言处理领域取得了重大进展，但在动态环境中仍面临持续决策、缺乏长期记忆和上下文窗口有限等挑战。为解决这些问题，本文提出一个创新框架——具有反思与记忆增强能力的自进化智能体（SAGE）。SAGE框架包含三个智能体：用户、助手和检查器。通过集成迭代反馈、反思机制以及基于艾宾浩斯遗忘曲线的记忆优化机制，它显著增强了智能体处理多任务和长跨度信息的能力。智能体通过自进化能够自适应调整策略、优化信息存储与传输，并有效降低认知负荷。我们在多个基准测试和长文本任务上评估SAGE框架的性能。实验结果表明，SAGE显著提升了模型性能，在闭源模型上实现了2.26倍的改进，在开源模型上实现了 $57.7\%$ 到 $100\%$ 的改进，在较小模型上的效果尤为显著。

# 1 引言

近年来，大语言模型（LLMs）在自然语言处理领域取得了重大进展，在对话和文本生成等任务中展示了强大的性能 Brown et al. (2020); He et al. (2025; 2024)。最近，将LLMs作为自主智能体（LLM智能体）应用的兴趣日益增长，这些智能体不仅使用语言进行理解和生成，还在交互环境中用于规划和行动 Yao et al. (2023b); Shinn et al. (2023); Liang et al. (2024); Li et al. (2024); Zhou et al. (2024)。然而，这些模型仍面临若干挑战：（1）LLM智能体需要在变化的环境中持续做出决策，并适应新情境和任务。（2）LLM智能体缺乏长期记忆机制，这在需要与环境持续交互的情境中日益明显 Graves et al. (2016)。有限的上下文窗口也阻碍了模型处理长时间跨度信息的能力 Rae et al. (2019)。

为应对这些挑战，研究人员提出了元学习和多任务学习来增强LLM智能体的可迁移性和适应性。针对记忆限制，先前的工作如MemGPT Packer et al. (2024)使用FIFO队列来管理遗忘，而MemoryBank则采用基于插入时间的遗忘曲线。然而，这些方法通常是任务特定的，缺乏一个通用框架来系统性地改进复杂环境中的LLM智能体。最近的创新，如AutoGPT Yang et al. (2023)和BabyAGI Nakajima (2024)，利用LLMs作为核心控制器，旨在解决现实世界的挑战。然而，多智能体框架仍面临通信过载等问题，严重依赖记忆来维持上下文。随着交互历史的增长，资源需求和延迟增加，限制了在实际场景中的高效部署。

本文中，我们提出一个创新框架——具有反思与记忆增强能力的自进化智能体（SAGE）。通过反思增强智能体的自我调整能力，它们能更有效地利用历史信息，在面对复杂动态任务时做出高效决策。从自进化的角度，我们引入了一个基于艾宾浩斯遗忘曲线的记忆优化机制 Ebbinghaus (1885)。该机制帮助智能体选择性保留关键信息，优化信息存储与传输，减少不必要的认知负荷，并增强智能体在环境交互任务中的能力。实验结果表明，我们的方法在广泛的基准测试中持续提升了专有和开源LLMs的性能。改进在较小模型上尤为显著，增益更为明显。在多源问答和代码生成等任务上，我们的方法设立了新标准，超越了现有技术，并达到了领先的基准 Etezadi & Shamsfard (2023)，包括AgentBench Liu et al. (2023b)。

我们工作的主要贡献如下：

- 我们提出了一个新框架SAGE，它引入了反思机制以增强智能体的自我调整能力。无需任何额外训练，这使得智能体能更有效地利用历史信息，并在面对复杂动态任务时做出更好的决策。
- 我们引入了基于艾宾浩斯遗忘曲线的记忆优化机制。这帮助智能体选择性保留关键信息，减少多智能体系统中的信息过载问题。
- SAGE在多个具有挑战性的现实世界任务中实现了对强基线的改进，并在基准测试中达到了最先进的结果。该框架可应用于其他LLMs，在较小模型上的改进尤为强劲。

# 2 相关工作

# 2.1 推理与决策的自我改进

深度学习已经改变了包括NLP、时间序列分析和计算机视觉在内的多个领域 Qiu et al. (2025a;b; 2024)。许多研究专注于使大语言模型（LLMs）更好地自我改进。一些研究人员致力于使用精心设计的提示来帮助模型学习如何改进，尽管这通常仅适用于一次性任务。其他人在调整模型在任务中获得反馈的方式，这有助于它们更好地进行推理 Huang et al. (2022)。还有关于使用随机束搜索等策略来帮助模型做出更明智的决策并评估自身工作的工作。大多数当前方法依赖于快速、一次性的调整和需要大量资源和手动技术帮助的学习策略 Tian et al. (2024)。本文引入了自我反思机制，表明LLMs可以在不需要额外训练的情况下，在不同任务中持续改进并产生更高质量的工作。

# 2.2 LLM智能体的记忆机制

在基于LLM的智能体中，记忆模块存储、处理和检索与任务相关的信息，支持知识积累、经验处理和决策制定。为增强这些智能体的自进化能力，研究人员专注于设计和优化这些记忆模块 Raffel et al. (2020)。过去的研究涵盖了记忆模块的各种设计和实现。这包括整合来自不同试验的信息以提升推理能力，或以自然语言存储信息以增强模块的可解释性和用户友好性 Wada et al. (2019)。尽管有进展，自我调整和记忆管理仍需改进，以更有效地处理复杂的现实世界问题。

![](images/c04551aedcb0a07f85fa10fc8caad7d7ab95cc5cf7866818036aacc7694547b1.jpg)
图1：SAGE示意图：用户向具有短期记忆（STM）和长期记忆（LTM）的助手提供描述和实例。助手执行观察、行动、反思和输出，由检查器审查。右侧的保留率曲线说明了记忆随时间衰减，自进化循环指导持续更新。

# 3 方法

本节我们介绍SAGE框架，该框架旨在通过利用三个核心机制来提升智能体性能：迭代反馈、反思和MemorySyntax（如图1所示）。助手智能体 $A$ 根据检查器智能体 $C$ 提供的反馈 $f_{t}$ 迭代更新其策略 $\pi_{\theta}$，在连续迭代中优化以最大化期望奖励 $R$。反思机制允许 $A$ 整合历史观察 $\mathcal{O}_t$ 和行动 $\mathbf{a}_t$，形成自我反思 $r_t$，该反思存储在记忆 $\mathcal{M}_L$ 中供未来决策使用。最后，MemorySyntax将艾宾浩斯遗忘曲线与语言原则结合来管理记忆衰减，通过基于信息保留强度 $S(I_t)$ 优先处理信息，动态更新智能体的短期记忆 $\mathcal{M}_S$ 和长期记忆 $\mathcal{M}_L$，从而提升智能体保留关键信息同时丢弃较不相关数据的能力。后续小节详述这些组件。

# 3.1 迭代反馈

SAGE框架中的迭代反馈机制使助手智能体 $A$ 能够通过与检查器智能体 $C$ 的重复交互来优化其策略 $\pi_{\theta}$。在每次迭代 $t$，助手根据其当前输出 $\mathbf{o}_{t}$ 接收反馈 $f_{t}$，并相应调整其策略。此过程持续直到检查器验证输出或达到迭代上限 $N$，确保 $A$ 在连续迭代中逐步优化其决策以提升任务性能。

# 3.1.1 初始化阶段

角色分配。在SAGE框架中，引入了三个智能体：用户 $U$、助手 $A$ 和检查器 $C$。用户接收到提示 $P_U$ 后，承担任务提出者的角色，指定任务 $\mathcal{T}_U$ 和相关约束 $\mathcal{C}_U$。助手接收到提示 $P_A$ 后，基于观察 $\mathcal{O}_t$ 和环境 $\mathcal{E}$ 生成一系列行动 $\mathbf{a}_t$。检查器 $C$ 评估助手产生的输出 $\mathbf{o}_A$，基于 $\mathbf{o}_A$ 与期望结果之间的差异提供反馈 $f_C$，迭代更新其策略 $\pi_\theta$ 以最小化此差距。

任务分配。用户提供的任务 $\mathcal{T}_U$ 包括初始任务描述 $\mathbf{d}_U$ 和作为正确输出参考的实例 $\mathbf{i}_U$。这形成了助手的输入集 $\mathcal{I}_A = (\mathbf{d}_U, \mathbf{i}_U)$ 以启动其生成过程。助手随后在每个时间步 $t$ 选择行动 $\mathbf{a}_t$，由 $\pi_{\theta}$ 指导，目标是为完成 $\mathcal{T}_U$ 最大化奖励 $R_t$。

![](images/f21e9ad9efded782e22732e75ea10af1de8ccbeec9a7bae462bfb7b4dfc895df.jpg)
图2：助手迭代工作流程示例，包括检查器评估、反馈的提示模板以及整合短期和长期记忆的反思过程。

# 3.1.2 实际交互阶段

继初始化阶段中的角色分配和任务定义后，助手 $A$ 进入实际交互阶段，以生成旨在完成任务 $\mathcal{T}_U$ 的输出。在此阶段，$A$ 基于输入集 $\mathcal{I}_A = (\mathbf{d}_U, \mathbf{i}_U)$ 中提供的任务描述 $\mathbf{d}_U$ 和实例 $\mathbf{i}_U$，在每个时间步 $t$ 迭代产生输出 $\mathbf{o}_t$。在每个时间步 $t$，助手通过遵循其策略 $\pi_\theta$ 选择行动 $\mathbf{a}_t$，该策略以当前状态 $s_t$、奖励信号 $R_t$（任务性能的奖励分数）以及检查器 $C$ 的反馈 $f_t^i$ 为条件。此决策过程形式化为：

$$
\mathbf {o} _ {t} \sim \pi_ {\theta} \left(\mathbf {o} _ {t} \mid s _ {t}, R _ {t}, f _ {t} ^ {i}\right), \tag {1}
$$

其中 $\pi_{\theta}$ 代表助手的策略，$R_{t}$ 反映基于时间 $t$ 任务性能的奖励信号，$f_{t}^{i}$ 是检查器在第 $i$ 次迭代中提供的反馈。

随着交互进行，检查器 $C$ 评估 $A$ 生成的每个输出 $\mathbf{o}_t$，将其与从 $\mathbf{i}_U$ 导出的期望结果进行比较。基于此比较，检查器提供迭代反馈 $f_t^i$ 以指导 $A$ 优化其行动 $\mathbf{a}_t$ 和输出 $\mathbf{o}_t$。迭代优化持续直到检查器验证输出正确或达到迭代限制 $N$。

迭代反馈机制的理论最优性。在SAGE框架中，助手通过此检查器反馈反复更新其策略，使得输出能够逐步优化，直到结果被验证或达到指定的迭代限制。助手的效用 $R_{A}$ 反映任务性能，检查器的效用 $R_{C}$ 取决于其反馈。以下定理表明，这种迭代反馈机制在纳什均衡的意义上导致策略稳定性 Fudenberg & Tirole (1991)。

定理3.1（多智能体迭代反馈系统的理论）。令 $\mathcal{U},\mathcal{A},\mathcal{C}$ 分别表示用户 $(U)$、助手 $(A)$ 和检查器 $(C)$ 的紧致凸策略空间。假设效用函数

$$
R _ {U}: \mathcal {U} \times \mathcal {A} \times \mathcal {C} \rightarrow \mathbb {R}, \quad R _ {A}: \mathcal {U} \times \mathcal {A} \times \mathcal {C} \rightarrow \mathbb {R}, \quad a n d \quad R _ {C}: \mathcal {U} \times \mathcal {A} \times \mathcal {C} \rightarrow \mathbb {R} \tag {2}
$$

在每个参与者的策略中是连续的。那么，根据Debreu-Glicksberg-Fan不动点定理，存在一个纳什均衡

$$
\left(s _ {U} ^ {*}, s _ {A} ^ {*}, s _ {C} ^ {*}\right) \in \mathcal {U} \times \mathcal {A} \times \mathcal {C}. \tag {3}
$$

此外，假设助手的策略 $\pi_{\theta}$ 通过策略梯度方法更新，并且检查器的策略通过凸优化进行优化。那么，迭代更新过程产生序列

$$
\left\{\pi_ {\theta} ^ {(k)} \right\} _ {k \geq 0} \quad a n d \quad \left\{f ^ {(k)} \right\} _ {k \geq 0}, \tag {4}
$$

其收敛到一个稳定策略剖面 $(\pi_{\theta}^{*},f^{*})$，且有：

$$
R _ {A} \left(\pi_ {\theta} ^ {*}, f ^ {*}\right) \geq R _ {A} \left(\pi_ {\theta}, f ^ {*}\right), \quad R _ {C} \left(\pi_ {\theta} ^ {*}, f ^ {*}\right) \geq R _ {C} \left(\pi_ {\theta} ^ {*}, f\right). \tag {5}
$$

该结果表明，迭代反馈机制通过收敛到三参与者博弈中的纳什均衡来增强模型的策略稳定性。它为此三智能体系统相对于更简单的替代方案（如两智能体系统）提供了更强的理论依据。详细的理论解释和证明见附录A.2。

# 3.1.3 进化目标与方向

利用每次迭代 $t$ 获得的反馈 $f_{t}^{i}$，助手 $A$ 制定新的进化目标：

$$
\mathcal {G} ^ {t + 1} = \left(\mathcal {A} ^ {t + 1}, \mathcal {D} ^ {t + 1}\right), \quad \mathcal {D} ^ {t + 1} = \arg \min  _ {\mathcal {D} _ {t} \in \Delta} \sum_ {i \in I _ {t}} L _ {D} \left(\mathcal {D} _ {t}; f _ {t} ^ {i}, \pi_ {\theta} ^ {t}\right), \tag {6}
$$

其中 $\mathcal{A}^{t + 1}$ 代表更新的记忆优化机制，$\mathcal{D}^{t + 1} \in \Delta$ 指模型的自调整以使RL算法收敛。这些进化目标指导助手为后续迭代更新其策略 $\pi_{\theta}$。策略更新由函数 $\psi$ 控制，该函数整合了当前策略 $\pi_{\theta}^{t}$ 与新的进化目标 $\mathcal{G}^{t + 1}$：

$$
\theta^ {t + 1} = \phi (\theta^ {t}, \mathcal {G} ^ {t + 1}) = \theta^ {t} + \alpha \nabla_ {\theta} [ \lambda_ {A} L _ {A} (\theta^ {t}, \mathcal {A} ^ {t + 1}) + \lambda_ {D} L _ {D} (\theta^ {t}, \mathcal {D} ^ {t + 1}) ]. \tag {7}
$$

此处 $L_{A}(\theta, \mathcal{A})$ 和 $L_{D}(\theta, \mathcal{D})$ 分别是与记忆优化和自调整方面对应的MSE损失函数，$\lambda_{A}, \lambda_{D} \geq 0$ 是权重系数。迭代策略优化使助手 $A$ 能够基于累积反馈和不断变化的任务要求持续调整其策略，从而提升其在动态环境中的整体性能。

# 3.2 记忆管理

SAGE框架实现了一个双记忆系统，包括短期记忆（STM）和长期记忆（LTM），以管理与任务相关的信息并增强智能体的推理和决策能力（该过程的视觉表示见图2）。

短期记忆（STM）。STM负责存储有限的即时、任务特定数据。它随着新观察 $(\mathcal{O}_t)$ 和行动 $(\mathbf{a}_t)$ 快速更新，维持最近的轨迹历史 $\mathcal{T}_t = (\mathcal{O}_t,\mathbf{a}_t)$。这使得智能体能够实时决策并快速响应环境中的动态变化 Mnih et al. (2015)。

长期记忆（LTM）。LTM在较长时间内保留关键信息和自我反思 $(r_t)$，使智能体能够积累过去交互的知识并将其应用于未来任务。存储为 $\mathcal{M}_L = \{r_t \mid t \in T\}$，此记忆机制允许智能体利用先验经验来改进任务性能，特别是在需要长时间跨度信息的复杂环境中 Graves et al. (2016)。

通过整合STM和LTM，SAGE框架使智能体能够平衡即时任务需求与利用累积知识的能力，从而提升其整体决策效率。

# 3.2.1 反思

图4展示了应用于HotpotQA任务的反思机制示例 Yang et al. (2018b)。反思机制为助手 $A$ 提供稀疏奖励信号，如二元成功/失败状态、轨迹 $\mathcal{T}_t$ 及其存储的记忆 $\mathcal{M}_L$。助手处理这些输入，从过去表现中获取洞察，并为未来决策存储自我反思 $\mathbf{r}_t$。这些自我反思比标量奖励更丰富，增强了助手的学习能力，并被纳入长期记忆：

$$
\mathbf {r} _ {t} = \operatorname {r e f} \left(\mathbf {o} _ {1: t}, \mathbf {R} _ {1: t}\right), \tag {8}
$$

其中 $\operatorname{ref}(\cdot)$ 表示基于输出序列 $\mathbf{o}_{1:t}$ 和奖励 $\mathbf{R}_{1:t}$ 的反思函数。导出的反思 $\mathbf{r}_t$ 随后被添加到 $\mathcal{M}_L$：

$$
\mathcal {M} _ {L} \leftarrow \mathcal {M} _ {L} \cup \left\{\mathbf {r} _ {t} \right\}. \tag {9}
$$

该过程逐步增强智能体的决策能力，使其能够通过积累的经验有效适应。

# 3.2.2 MemorySyntax

基于反思机制，MemorySyntax方法将艾宾浩斯遗忘曲线与语言原则结合，以在智能体的记忆管理系统中模拟类人记忆过程。令 $I_{t}$ 表示时间 $t$ 接收的信息，$R(I_{t},\tau)$ 表示其在时间间隔 $\tau$ 后的保留率。根据艾宾浩斯遗忘曲线，保留率建模为：

$$
R \left(I _ {t}, \tau\right) = e ^ {- \frac {\tau}{S}}, \tag {10}
$$

其中 $S$ 是信息的强度，反映其重要性和复杂性。

为增强保留，MemorySyntax对 $I_{t}$ 应用语言优化，产生优化版本 $I_{t}^{*}$ 且强度 $S^{*} > S$。$I_{t}^{*}$ 的保留率定义为：

$$
R \left(I _ {t} ^ {*}, \tau\right) = \left\{ \begin{array}{l l} e ^ {- \frac {\tau}{S ^ {*}}}, & \text {i f} I _ {t} ^ {*} \in \mathcal {M} _ {S}, \\ e ^ {- \frac {\tau}{S}}, & \text {i f} I _ {t} ^ {*} \in \mathcal {M} _ {L}, \end{array} \right. \tag {11}
$$

其中 $\mathcal{M}_S$ 和 $\mathcal{M}_L$ 分别代表短期记忆和长期记忆。

智能体基于 $I_t^*$ 的保留率使用预定义阈值 $\theta_1$ 和 $\theta_2$（其中 $\theta_1 > \theta_2$）更新其记忆状态 $\mathcal{M}_t$。记忆更新规则形式化为：

$$
\mathcal {M} _ {t + 1} = \left\{ \begin{array}{l l} \mathcal {M} _ {t} \cup \left\{I _ {t} ^ {*} \right\}, & \text {i f} R \left(I _ {t} ^ {*}, \tau\right) \geq \theta_ {1}, \\ \mathcal {M} _ {t} \backslash \left\{I _ {t} ^ {*} \right\}, & \text {i f} R \left(I _ {t} ^ {*}, \tau\right) <   \theta_ {2}, \\ \mathcal {M} _ {t}, & \text {o t h e r w i s e .} \end{array} \right. \tag {12}
$$

此更新规则在以下条件下操作：

- 在短期记忆 $(\mathcal{M}_S)$ 中保留：如果 $R(I_t^*, \tau) \geq \theta_1$，信息 $I_t^*$ 保留在短期记忆 $\mathcal{M}_S$ 中。
- 丢弃信息：如果 $R(I_t^*, \tau) < \theta_2$，信息 $I_t^*$ 被视为不重要并被丢弃。
- 转移到长期记忆 $(\mathcal{M}_L)$：如果 $\theta_2 \leq R(I_t^*, \tau) < \theta_1$，信息 $I_t^*$ 转移到长期记忆 $\mathcal{M}_L$ 中。

上述MemorySyntax方法是最优的，并确保最大信息效用。理论背景和详细证明见附录A.1。

通过模拟人类记忆动态，MemorySyntax使智能体能够优先处理重要信息，在短期记忆 $\mathcal{M}_S$ 中保留关键数据，在长期记忆 $\mathcal{M}_L$ 中存储重要但不常用的信息，并丢弃不相关数据。该机制解决了记忆容量限制，并增强了智能体执行需要高效记忆管理的复杂任务的能力。

# 4 实验

为展示SAGE在协调自主智能体组共同完成任务方面的能力和性能，我们在基准任务上进行了广泛的定量实验。我们使用公共基准AgentBench Liu et al. (2023b)，这是一个多维进化基准，我们从中选择了六个任务。这些任务测试了在多轮开放式生成设置中作为智能体的LLMs的推理和决策能力。为进一步评估智能体的长上下文理解能力，我们选择了四个广泛采用的与长文本处理相关的任务。这些任务反映了智能体的编程能力（LCCGuo et al. (2023), RepoBench-P Liu et al. (2023a)）和推理能力（HotpotQA Yang et al. (2018b), TriviaQA Joshi et al. (2017b)）。

# 4.1 AgentBench评估

任务描述 AgentBench包括来自CODE（知识图谱、操作系统、数据库）、GAME（ALFWorld） Shridhar et al. (2021) 和WEB（WebShop Yao et al. (2023a), Mind2Web Deng et al. (2023)）的场景。有关数据集和基准的更多细节见附录B。

基线 我们评估商业模型GPT-3.5 Brown et al. (2020) 和GPT-4 OpenAI et al. (2024)，以及开源模型Llama2 Touvron et al. (2023), Codellama Roziere et al. (2024), Qwen Bai et al. (2023) 和ChatGLM2 GLM et al. (2024)。超过模型长度限制的对话历史被截断，使用贪婪解码。

结果 如表1所示，我们的方法显著提升了模型在AgentBench上的性能，尤其是对小模型。GPT-3.5和GPT-4尽管已有高分，但使用SAGE后也显示出显著改进，在数据库任务上高达 $2.26\mathrm{x}$。Llama2-7b得到显著增强，显示了该方法对较弱模型的影响。CodeLlama-7b和Qwen-1.8B也获得大幅提升。应用我们的方法后，Qwen-1.8B的性能接近GPT-3.5，突显了其作为通用智能体的潜力。Llama2先前容易出错，通过反馈和记忆优化显示出基本错误的显著减少，证明我们的方法不仅增强了智能体能力，还减少了复杂任务中的基本错误。

表1：AgentBench上的基线及SAGE框架性能

<table><tr><td rowspan="2">LLM类型</td><td rowspan="2">模型</td><td colspan="2">VER</td><td colspan="2">OS</td><td colspan="2">DB</td><td colspan="2">KG</td><td colspan="2">ALF</td><td colspan="2">WS</td><td colspan="2">M2W</td></tr><tr><td>基线</td><td>SAGE</td><td>基线</td><td>SAGE</td><td>基线</td><td>SAGE</td><td>基线</td><td>SAGE</td><td>基线</td><td>SAGE</td><td>基线</td><td>SAGE</td><td>基线</td><td>SAGE</td></tr><tr><td rowspan="2">API</td><td>GPT-4</td><td>42.4</td><td>49.7</td><td>32.0</td><td>39.8</td><td>57.4</td><td>63.1</td><td>78.0</td><td>82.0</td><td>67.1</td><td>67.8</td><td>27.0</td><td>32.0</td><td>27.0</td><td>32.0</td></tr><tr><td>GPT-3.5</td><td>31.6</td><td>38.3</td><td>15.7</td><td>35.6</td><td>25.9</td><td>37.6</td><td>17.0</td><td>23.0</td><td>64.1</td><td>72.1</td><td>16.0</td><td>28.0</td><td>16.0</td><td>28.0</td></tr><tr><td rowspan="5">OSS</td><td>Llama2-7B Chat</td><td>0.0</td><td>8.4</td><td>0.0</td><td>10.2</td><td>0.0</td><td>25.0</td><td>0.0</td><td>5.0</td><td>4.4</td><td>10.4</td><td>0.0</td><td>15.0</td><td>0.0</td><td>15.0</td></tr><tr><td>CodeLlama-7B Instruct</td><td>5.7</td><td>18.4</td><td>2.6</td><td>19.2</td><td>0.0</td><td>27.0</td><td>0.0</td><td>12.5</td><td>16.3</td><td>40.2</td><td>0.0</td><td>15.0</td><td>15.0</td><td>15.0</td></tr><tr><td>Qwen1.8B Chat</td><td>2.7</td><td>18.7</td><td>1.4</td><td>15.1</td><td>6.8</td><td>45.3</td><td>0.0</td><td>10.5</td><td>6.6</td><td>11.4</td><td>0.6</td><td>13.6</td><td>13.6</td><td>13.6</td></tr><tr><td>Qwen-7B Chat</td><td>5.6</td><td>22.2</td><td>4.8</td><td>18.0</td><td>0.0</td><td>48.0</td><td>34.0</td><td>38.5</td><td>0.0</td><td>13.6</td><td>0.0</td><td>15.0</td><td>15.0</td><td>15.0</td></tr><tr><td>ChatGLM2-6B v1.1</td><td>0.0</td><td>15.2</td><td>0.0</td><td>16.3</td><td>0.0</td><td>17.0</td><td>0.0</td><td>5.0</td><td>0.3</td><td>10.3</td><td>4.9</td><td>14.9</td><td>14.9</td><td>14.9</td></tr></table>

# 4.2 复杂问题解决任务评估

我们在三个任务上评估SAGE与基线模型：长形式QA Akash et al. (2023)、多轮对话 Cui et al. (2020) 和顺序任务完成 Stephens et al. (2012)。如表2所示，SAGE以显著增益优于所有基线，例如GPT-3.5在HotpotQA上的答案准确率提升 $20.8\%$ Yan+g et al. (2018b)，Mistral-7b在ALFWorld上的任务完成率提升 $17.3\%$ Shridhar et al. (2021)。在所有任务中，SAGE显著提升了答案准确率、对话连贯性和步骤完成度。

# 4.3 长上下文任务评估

我们在四个长文本任务上评估智能体的代码生成和推理能力：LCC数据集 Mohler et al. (2016) 专注于根据几行初始代码预测下一行代码，以精确率、召回率和F1作为指标。RepoBench-P Liu et al. (2024) 测试从跨文件和文件内上下文中检索相关代码片段以预测下一行，同样以精确率、召回率和F1进行评估。HotPotQA Yang et al. (2018a) 是一个基于维基百科的数据集，包含113k问答对，挑战智能体跨多个文档进行推理，通过答案F1进行评估。TriviaQA Joshi et al. (2017a) 是一个阅读理解数据集，包含问答对和证据段落（筛选为超过1,000词），同样使用答案F1进行评估。

我们比较了两种自我优化方法：束搜索 Kool et al. (2019)（通过随机束搜索整合自我评估）和Reflexion Shinn et al. (2023)（以语言形式使用过去试验经验）。

# 4.4 评估结果：

代码完成任务：在LCC数据集上（表3），SAGE在F1分数（79.29）上相比束搜索和Reflexion有轻微改进。其记忆机制有助于优化代码预测，但在代码完成等简单任务中性能差异不显著。

推理任务：SAGE在HotPotQA和TriviaQA上显著优于Reflexion和束搜索，F1分数分别为22.06和22.76（表3）。SAGE通过反思有效整合多文档信息的能力带来更好的推理准确率，而Reflexion和束搜索在处理复杂推理任务时面临挑战。

表3：不同方法性能对比

<table><tr><td rowspan="2">模型</td><td colspan="3">LCC</td><td colspan="3">RepoBench-P</td><td>HotpotQA</td><td>TriviaQA</td></tr><tr><td>精确率</td><td>召回率</td><td>F1</td><td>精确率</td><td>召回率</td><td>F1</td><td>F1</td><td>F1</td></tr><tr><td>Reflexion</td><td>77.72</td><td>81.00</td><td>79.28</td><td>78.73</td><td>81.86</td><td>80.25</td><td>11.26</td><td>11.23</td></tr><tr><td>Beam search</td><td>78.98</td><td>79.32</td><td>79.12</td><td>78.75</td><td>81.02</td><td>79.87</td><td>10.26</td><td>12.13</td></tr><tr><td>SAGE</td><td>78.76</td><td>79.88</td><td>79.29</td><td>79.27</td><td>83.28</td><td>81.22</td><td>22.06</td><td>22.76</td></tr></table>

# 4.5 RAG智能体评估

表4比较了经典词汇检索（使用BM25的RAG）Robertson & Zaragoza (2009)、密集段落检索（使用DPR的RAG）Reichman & Heck (2024)、商业检索解决方案（使用OpenAI Retrieval的RAG）OpenAI (2023)、TART序列到序列检索模型 Eisenschlos et al. (2022) 和FiD（解码器内融合）方法 Izacard & Grave (2021)，所有方法都在多文档和开放域QA任务（HotpotQA、Natural Questions Kwiatkowski et al. (2019) 和TriviaQA）上进行了测试。使用BM25的RAG依赖于基于术语的匹配，而使用DPR的RAG使用学习到的密集嵌入。TART采用基于Transformer的方法生成相关上下文，而FiD通过编码器-解码器设计融合多个检索到的段落。相比之下，ChatGPT-4（SAGE）采用结构化推理工作流进行检索和生成，这导致准确率稳定提升 $3.6\%$ 到 $4.7\%$，并在某些任务上减少近 $50\%$ 的内存消耗，且未增加延迟。

表4：不同任务和数据集上不同RAG智能体评估

<table><tr><td>智能体</td><td>准确率（QA）(%)</td><td>延迟（ms）</td><td>内存使用（MB）</td></tr><tr><td colspan="4">任务1：多文档QA（HotpotQA）</td></tr><tr><td>RAG (BM25)</td><td>60.8</td><td>121</td><td>613</td></tr><tr><td>RAG (DPR)</td><td>66.3</td><td>129</td><td>542</td></tr><tr><td>RAG (OpenAI Retrieval)</td><td>67.4</td><td>108</td><td>494</td></tr><tr><td>TART</td><td>63.2</td><td>144</td><td>477</td></tr><tr><td>FiD (Fusion-in-Decoder)</td><td>70.1</td><td>153</td><td>456</td></tr><tr><td>ChatGPT-4 - SAGE</td><td>74.8 (+4.7)</td><td>128</td><td>231 (-50%)</td></tr><tr><td colspan="4">任务2：上下文回答的文档检索（Natural Questions）</td></tr><tr><td>RAG (BM25)</td><td>59.9</td><td>125</td><td>605</td></tr><tr><td>RAG (DPR)</td><td>65.5</td><td>131</td><td>561</td></tr><tr><td>RAG (OpenAI Retrieval)</td><td>66.8</td><td>113</td><td>484</td></tr><tr><td>TART</td><td>62.4</td><td>146</td><td>455</td></tr><tr><td>FiD (Fusion-in-Decoder)</td><td>69.8</td><td>156</td><td>443</td></tr><tr><td>ChatGPT-4 - SAGE</td><td>73.6 (+3.8)</td><td>131</td><td>227 (-49%)</td></tr><tr><td colspan="4">任务3：多上下文开放域QA（TriviaQA）</td></tr><tr><td>RAG (BM25)</td><td>62.1</td><td>124</td><td>615</td></tr><tr><td>RAG (DPR)</td><td>67.8</td><td>129</td><td>530</td></tr><tr><td>RAG (OpenAI Retrieval)</td><td>68.9</td><td>117</td><td>494</td></tr><tr><td>TART</td><td>64.7</td><td>148</td><td>462</td></tr><tr><td>FiD (Fusion-in-Decoder)</td><td>71.9</td><td>155</td><td>456</td></tr><tr><td>ChatGPT-4 - SAGE</td><td>75.5 (+3.6)</td><td>134</td><td>243 (-47%)</td></tr></table>

# 4.6 错误分析

如图3所示，SAGE框架显著提升了智能体在各任务上的性能，特别是在AgentBench的WS任务中，这归因于其迭代反馈机制，通过持续的助手-检查器交互优化输出。在OS和DB任务中，上下文限制超出和无效格式错误几乎被消除，无效行动错误显著减少，这归功于反思机制帮助助手学习并减少逻辑错误。

![](images/9726eb0e462697a7dc3b1d7bd3be94219d7a30957ac0313cb1dc119fc294fb60.jpg)
图3：六个任务的执行结果（CLE：上下文限制超出，TLE：任务限制超出）。任务限制是任务未完成的主要原因，突显了LLM智能体在时间限制下的局限性。

# 4.7 消融研究

我们在Qwen-1.8B和CodeLlama-7B上进行了消融实验以评估记忆优化（表5）。无记忆优化时，两个模型表现较弱，尤其是Qwen-1.8B在KG任务中从6.8提升到48.0，在ALF任务中从0.0提升到10.5。类似地，CodeLlama-7B显示出大幅提升，特别是在DB任务中（2.7到41.3）和WS任务中（14.3到58.7）。总体而言，CodeLlama-7B表现优于Qwen-1.8B，突显了参数更多的模型在处理复杂任务时更强的适应性。

表5：AgentBench任务上记忆优化的消融研究

<table><tr><td>模型</td><td>OS</td><td>DB</td><td>KG</td><td>ALF</td><td>WS</td><td>M2W</td></tr><tr><td>Qwen-1.8B（无记忆优化）</td><td>10.4</td><td>22.6</td><td>6.8</td><td>0.0</td><td>26.6</td><td>5.0</td></tr><tr><td>Qwen-1.8B（有记忆优化）</td><td>18.7</td><td>28.3</td><td>45.3</td><td>10.5</td><td>31.4</td><td>25.1</td></tr><tr><td>Codellama-7B（无记忆优化）</td><td>9.7</td><td>2.7</td><td>0.0</td><td>0.0</td><td>14.3</td><td>5.0</td></tr><tr><td>Codellama-7B（有记忆优化）</td><td>23.4</td><td>41.3</td><td>48.0</td><td>12.5</td><td>58.7</td><td>15.0</td></tr></table>

# 5 结论

本文中，我们提出了SAGE框架，该框架通过反思机制和记忆优化增强了智能体在复杂任务中的自我调整和记忆管理能力。实验结果表明，在多个基准测试中性能显著提升，尤其是在较小模型上。在AgentBench测试中，SAGE提升了像GPT-3.5和GPT-4这样的强基线性能，同时也显著改进了开源模型。它有效地减少了基本错误和逻辑错误，特别是使较小模型能够处理复杂任务。

# 参考文献

Pritom Saha Akash, Kashob Kumar Roy, Lucian Popa, and Kevin Chen-Chuan Chang. Long-form question answering: An iterative planning-retrieval-generation approach, 2023. URL https://arxiv.org/abs/2311.09383.
Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin, Runji Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu, Keming Lu, Jianxin Ma, Rui Men, Xingzhang Ren, Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong Tu, Peng Wang, Shijie Wang, Wei Wang, Shengguang Wu, Benfeng Xu, Jin Xu, An Yang, Hao Yang, Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu, Hongyi Yuan, Zheng Yuan, Jianwei Zhang, Xingxuan Zhang, Yichang Zhang, Zhenru Zhang, Chang Zhou, Jingren Zhou, Xiaohuan Zhou, and Tianhang Zhu. Qwen technical report, 2023.
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners, 2020.
Thomas M. Cover and Joy A. Thomas. Elements of Information Theory (Wiley Series in Telecommunications and Signal Processing). Wiley-Interscience, USA, 2006. ISBN 0471241954.
Leyang Cui, Yu Wu, Shujie Liu, Yue Zhang, and Ming Zhou. MuTual: A dataset for multi-turn dialogue reasoning. In Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel Tetreault (eds.), Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pp. 1406-1416, Online, July 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.acl-main.130. URL https://aclanthology.org/2020.acl-main.130/.
Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Samuel Stevens, Boshi Wang, Huan Sun, and Yu Su. Mind2web: Towards a generalist agent for the web, 2023.
Hermann Ebbinghaus. Über das gedächtnis: untersuchungen zur experimentellen psychologie. Duncker & Humblot, 1885.
Julian Eisenschlos, Yury Zemlyanskiy, Jason Phang, Bhuwan Dhingra, and William W. Cohen. TART: Retrieval-augmented generation for task-oriented dialog. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL), pp. 1866-1881, 2022. URL https://aclanthology.org/2022.acl-long.131.
Romina Etezadi and Mehrnoush Shamsfard. The state of the art in open domain complex question answering: a survey. Applied Intelligence, 53(4):4124-4144, 2023.
Drew Fudenberg and Jean Tirole. Game Theory. MIT Press, Cambridge, MA, 1991.
Team GLM, Aohan Zeng, Bin Xu, Bowen Wang, Chenhui Zhang, Da Yin, Diego Rojas, Guanyu Feng, Hanlin Zhao, Hanyu Lai, Hao Yu, Hongning Wang, Jiadai Sun, Jiajie Zhang, Jiale Cheng, Jiayi Gui, Jie Tang, Jing Zhang, Juanzi Li, Lei Zhao, Lindong Wu, Lucen Zhong, Mingdao Liu, Minlie Huang, Peng Zhang, Qinkai Zheng, Rui Lu, Shuaiqi Duan, Shudan Zhang, Shulin Cao, Shuxun Yang, Weng Lam Tam, Wenyi Zhao, Xiao Liu, Xiao Xia, Xiaohan Zhang, Xiaotao Gu, Xin Lv, Xinghan Liu, Xinyi Liu, Xinyue Yang, Xixuan Song, Xunkai Zhang, Yifan An, Yifan Xu, Yilin Niu, Yuantao Yang, Yueyan Li, Yushi Bai, Yuxiao Dong, Zehan Qi, Zhaoyu Wang, Zhen Yang, Zhengxiao Du, Zhenyu Hou, and Zihan Wang. Chatglm: A family of large language models from glm-130b to glm-4 all tools, 2024.
Alex Graves, Greg Wayne, Malcolm Reynolds, Tim Harley, Ivo Danihelka, Agnieszka Grabska-Barwinska, Sergio Gomez Colmenarejo, Edward Grefenstette, Tiago Ramalho, John Agapiou, et al. Hybrid computing using a neural network with dynamic external memory. Nature, 538(7626):471-476, 2016.
Daya Guo, Canwen Xu, Nan Duan, Jian Yin, and Julian McAuley. Longcoder: A long-range pre-trained language model for code completion, 2023.
Yangfan He, Jianhui Wang, Kun Li, Yijin Wang, Li Sun, Jun Yin, Miao Zhang, and Xueqian Wang. Enhancing intent understanding for ambiguous prompt: A human-machine co-adaption strategy. Available at SSRN 5119629, 2024.
Yangfan He, Jianhui Wang, Kun Li, Yijin Wang, Li Sun, Jun Yin, Miao Zhang, and Xueqian Wang. Enhancing intent understanding for ambiguous prompts through human-machine co-adaptation. arXiv preprint arXiv:2501.15167, 2025.
Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu, and Jiawei Han. Large language models can self-improve, 2022.
Gautier Izacard and Edouard Grave. Leveraging passage retrieval with generative models for open domain question answering. In Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume (EACL), pp. 874-880, 2021. URL https://aclanthology.org/2021.eacl-main.24.
Mandar Joshi, Eunsol Choi, Daniel Weld, and Luke Zettlemoyer. TriviaQA: A large scale distantly supervised challenge dataset for reading comprehension. In Regina Barzilay and Min-Yen Kan (eds.), Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 1601-1611, Vancouver, Canada, July 2017a. Association for Computational Linguistics. doi: 10.18653/v1/P17-1147. URL https://aclanthology.org/P17-1147.
Mandar Joshi, Eunsol Choi, Daniel S. Weld, and Luke Zettlemoyer. Triviaqa: A large scale distantly supervised challenge dataset for reading comprehension, 2017b.
Wouter Kool, Herke van Hoof, and Max Welling. Stochastic beams and where to find them: The gumbel-top-k trick for sampling sequences without replacement, 2019. URL https://arxiv.org/abs/1903.06059.
Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Alberti, Danielle Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, Kristina Toutanova, Llion Jones, Matthew Kelcey, Ming-Wei Chang, Andrew M. Dai, Jakob Uszkoreit, Quoc Le, and Slav Petrov. Natural questions: A benchmark for question answering research. Transactions of the Association for Computational Linguistics, 7:452-466, 2019. doi: 10.1162/tacl_a_00276. URL https://aclanthology.org/Q19-1026/.

Zeyuan Li, Yangfan He, Lewei He, Jianhui Wang, Tianyu Shi, Bin Lei, Yuchen Li, and Qiuwu Chen. Falcon: Feedback-driven adaptive long/short-term memory reinforced coding optimization system. arXiv preprint arXiv:2410.21349, 2024.
Xuechen Liang, Meiling Tao, Yinghui Xia, Tianyu Shi, Jun Wang, and JingSong Yang. Cmat: A multi-agent collaboration tuning framework for enhancing small language models. arXiv preprint arXiv:2404.01663, 2024.
Tianyang Liu, Canwen Xu, and Julian McAuley. Repobench: Benchmarking repository-level code auto-completion systems, 2023a.
Tianyang Liu, Canwen Xu, and Julian McAuley. Repobench: Benchmarking repository-level code auto-completion systems. In The Twelfth International Conference on Learning Representations, 2024. URL https://openreview.net/forum?id=pPjZIouQuF.
Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang, Yuxiao Dong, and Jie Tang. Agentbench: Evaluating llms as agents. arXiv preprint arXiv: 2308.03688, 2023b.
Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A Rusu, Joel Veness, Marc G Bellemare, Alex Graves, Martin Riedmiller, Andreas K Fidjeland, Georg Ostrovski, et al. Human-level control through deep reinforcement learning. nature, 518(7540):529-533, 2015.
Michael Mohler, Mary Brunson, Bryan Rink, and Marc Tomlinson. Introducing the LCC metaphor datasets. In Nicoletta Calzolari, Khalid Choukri, Thierry Declerck, Sara Goggi, Marko Grobelnik, Bente Maegaard, Joseph Mariani, Helene Mazo, Asuncion Moreno, Jan Odijk, and Stelios Piperidis (eds.), Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC'16), pp. 4221-4227, Portoroz, Slovenia, May 2016. European Language Resources Association (ELRA). URL https://aclanthology.org/L16-1668.
Yohei Nakajima. Babyagi: An ai agent that can achieve goals and execute tasks, 2024.
OpenAI. Openai cookbook. https://github.com/openai/openai-cookbook, 2023. Accessed: 2025-03-27.
OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, Red Avila, Igor Babuschkin, Suchir Balaji, Valerie Balcom, Paul Baltescu, Haiming Bao, Mohammad Bavarian, Jeff Belgium, Irwan Bello, Jake Berdine, Gabriel Bernadett-Shapiro, Christopher Berner, Lenny Bogdonoff, Oleg Boiko, Madelaine Boyd, Anna-Luisa Brakman, Greg Brockman, Tim Brooks, Miles Brundage, Kevin Button, Trevor Cai, Rosie Campbell, Andrew Cann, Brittany Carey, Chelsea Carlson, Rory Carmichael, Brooke Chan, Che Chang, Fotis Chantzis, Derek Chen, Sully Chen, Ruby Chen, Jason Chen, Mark Chen, Ben Chess, Chester Cho, Casey Chu, Hyung Won Chung, Dave Cummings, Jeremiah Currier, Yunxing Dai, Cory Decareaux, Thomas Degry, Noah Deutsch, Damien Deville, Arka Dhar, David Dohan, Steve Dowling, Sheila Dunning, Adrien Ecoffet, Atty Eleti, Tyna Eloundou, David Farhi, Liam Fedus, Niko Felix, Simón Posada Fishman, Juston Forte, Isabella Fulford, Leo Gao, Elie Georges, Christian Gibson, Vik Goel, Tarun Gogineni, Gabriel Goh, Rapha Gontijo-Lopes, Jonathan Gordon, Morgan Grafstein, Scott Gray, Ryan Greene, Joshua Gross, Shixiang Shane Gu, Yufei Guo, Chris Hallacy, Jesse Han, Jeff Harris, Yuchen He, Mike Heating, Johannes Heidecke, Chris Hesse, Alan Hickey, Wade Hickey, Peter Hoeschele, Brandon Houghton, Kenny Hsu, Shengli Hu, Xin Hu, Joost Huizinga, Shantanu Jain, Shawn Jain, Joanne Jang, Angela Jiang, Roger Jiang, Haozhun Jin, Denny Jin, Shino Jomoto, Billie Jonn, Heewoo Jun, Tomer Kaftan, Lukasz Kaiser, Ali Kamali, Ingmar Kanitscheider, Nitish Shirish Keskar, Tabarak Khan, Logan Kilpatrick, Jong Wook Kim, Christina Kim, Yongjik Kim, Jan Hendrik Kirchner, Jamie Kiros, Matt Knight, Daniel Kokotajlo, Lukasz Kondraciuk, Andrew Kondrich, Aris Konstantinidis, Kyle Kosic, Gretchen Krueger, Vishal Kuo, Michael Lampe, Ikai Lan, Teddy Lee, Jan Leike

Jade Leung, Daniel Levy, Chak Ming Li, Rachel Lim, Molly Lin, Stephanie Lin, Mateusz Litwin, Theresa Lopez, Ryan Lowe, Patricia Lue, Anna Makanju, Kim Malfacini, Sam Manning, Todor Markov, Yaniv Markovski, Bianca Martin, Katie Mayer, Andrew Mayne, Bob McGrew, Scott Mayer McKinney, Christine McLeavey, Paul McMillan, Jake McNeil, David Medina, Aalok Mehta, Jacob Menick, Luke Metz, Andrey Mishchenko, Pamela Mishkin, Vinnie Monaco, Evan Morikawa, Daniel Mossing, Tong Mu, Mira Murati, Oleg Murk, David Mély, Ashvin Nair, Reiichiro Nakano, Rajeev Nayak, Arvind Neelakantan, Richard Ngo, Hyeonwoo Noh, Long Ouyang, Cullen O'Keefe, Jakub Pachocki, Alex Paino, Joe Palermo, Ashley Pantuliano, Giambattista Parascandolo, Joel Parish, Emy Parparita, Alex Passos, Mikhail Pavlov, Andrew Peng, Adam Perelman, Filipe de Avila Belbute Peres, Michael Petrov, Henrique Ponde de Oliveira Pinto, Michael, Pokorny, Michelle Pokrass, Vitchyr H. Pong, Tolly Powell, Alethea Power, Boris Power, Elizabeth Proehl, Raul Puri, Alec Radford, Jack Rae, Aditya Ramesh, Cameron Raymond, Francis Real, Kendra Rimbach, Carl Ross, Bob Rotsted, Henri Roussez, Nick Ryder, Mario Saltarelli, Ted Sanders, Shibani Santurkar, Girish Sastry, Heather Schmidt, David Schnurr, John Schulman, Daniel Selsam, Kyla Sheppard, Toki Sherbakov, Jessica Shieh, Sarah Shoker, Pranav Shyam, Szymon Sidor, Eric Sigler, Maddie Simens, Jordan Sitkin, Katarina Slama, Ian Sohl, Benjamin Sokolowsky, Yang Song, Natalie Staudacher, Felipe Petroski Such, Natalie Summers, Ilya Sutskever, Jie Tang, Nikolas Tezak, Madeleine B. Thompson, Phil Tillet, Amin Tootoonchian, Elizabeth Tseng, Preston Tuggle, Nick Turley, Jerry Tworek, Juan Felipe Cerón Uribe, Andrea Vallone, Arun Vijayvergiya, Chelsea Voss, Carroll Wainwright, Justin Jay Wang, Alvin Wang, Ben Wang, Jonathan Ward, Jason Wei CJ Weinmann Akila Welihinda Peter Welinder Jiayi Weng Lilian Weng Matt Wiethoff Dave Willner,Clemens Winter,Samuel Wolrich,Hannah WongLauren Workman Sherwin WuJeff WuMichael WuKai Xiao,Tao XuSarah YooKevin YuQiming Yuan Wojciech Zaremba Rowan ZellersChong Zhang Marvin Zhang Shengjia ZhaoTianhao Zheng,Juntang ZhuangWilliam Zhuk,and Barret Zoph.Gpt-4 technical report 2024. URL https://arxiv.org/abs/2303.08774.

Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, and Joseph E. Gonzalez. Memgpt: Towards llms as operating systems, 2024.
Xiangfei Qiu, Jilin Hu, Lekui Zhou, Xingjian Wu, Junyang Du, Buang Zhang, Chenjuan Guo, Aoying Zhou, Christian S. Jensen, Zhenli Sheng, and Bin Yang. Tfb: Towards comprehensive and fair benchmarking of time series forecasting methods. In Proc. VLDB Endow., pp. 2363-2377, 2024.
Xiangfei Qiu, Xiuwen Li, Ruiyang Pang, Zhicheng Pan, Xingjian Wu, Liu Yang, Jilin Hu, Yang Shu, Xuesong Lu, Chengcheng Yang, Chenjuan Guo, Aoying Zhou, Christian S. Jensen, and Bin Yang. Easytime: Time series forecasting made easy. In ICDE, 2025a.
Xiangfei Qiu, Xingjian Wu, Yan Lin, Chenjuan Guo, Jilin Hu, and Bin Yang. Duet: Dual clustering enhanced multivariate time series forecasting. In SIGKDD, pp. 1185-1196, 2025b.
Jack W Rae, Anna Potapenko, Siddhant M Jayakumar, and Timothy P Lillicrap. Compressive transformers for long-range sequence modelling. arXiv preprint arXiv:1911.05507, 2019.
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. Journal of machine learning research, 21(140):1-67, 2020.
Benjamin Reichman and Larry Heck. Dense passage retrieval: Is it retrieving?, 2024. URL https://arxiv.org/abs/2402.11035.
Stephen Robertson and Hugo Zaragoza. The probabilistic relevance framework: Bm25 and beyond. Foundations and Trends® in Information Retrieval, 3(4):333-389, 2009. ISSN 1554-0669. doi: 10.1561/1500000019. URL http://dx.doi.org/10.1561/1500000019.
Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaqing Ellen Tan, Yossi Adi, Jingyu Liu, Romain Sauvestre, Tal Remez, Jérémy Rapin, Artyom Kozhevnikov, Ivan Evtimov, Joanna Bitton, Manish Bhatt, Cristian Canton Ferrer, Aaron Grattaftori,

Wenhan Xiong, Alexandre Défossez, Jade Copet, Faisal Azhar, Hugo Touvron, Louis Martin, Nicolas Usunier, Thomas Scialom, and Gabriel Synnaeve. Code Llama：用于代码的开放基础模型，2024. URL https://arxiv.org/abs/2308.12950。
Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion：具有言语强化学习的语言智能体，2023。
Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Côté, Yonatan Bisk, Adam Trischler, and Matthew Hausknecht. ALFWorld：对齐文本与具身环境以进行交互式学习。 见于《国际学习表征会议（ICLR）论文集》，2021. URL https://arxiv.org/abs/2010.03768。
Keri K Stephens, Jaehee K Cho, and Dawnna I Ballard. 同时性、顺序性与速度：关于多任务完成度的组织信息。 人类传播研究，38(1):23-47, 2012。
Richard S. Sutton and Andrew G. Barto. 强化学习：导论。 MIT出版社，剑桥，马萨诸塞州，第2版，2018。
Ye Tian, Baolin Peng, Linfeng Song, Lifeng Jin, Dian Yu, Haitao Mi, and Dong Yu. 通过想象、搜索与批评实现LLMs的自我改进，2024。
Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami, Naman Goyal, Anthony Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian, Xiaqing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aurelien Rodriguez, Robert Stojnic, Sergey Edunov, and Thomas Scialom. Llama 2：开放基础与微调聊天模型，2023。
Takashi Wada, Tomoharu Iwata, and Yuji Matsumoto. 基于神经语言模型的有限资源无监督多语言词嵌入。 见于《计算语言学协会第57届年会论文集》，第3113-3124页，2019。
Hui Yang, Sifu Yue, and Yunzhong He. 用于在线决策的Auto‑GPT：基准与额外观点，2023. URL https://arxiv.org/abs/2306.02224。
Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William Cohen, Ruslan Salakhutdinov, and Christopher D. Manning. HotpotQA：一个用于多样化、可解释多跳问答的数据集。 见于Ellen Riloff、David Chiang、Julia Hockenmaier和Jun'ichi Tsujii（编辑），《2018年自然语言处理经验方法会议论文集》，第2369-2380页，布鲁塞尔，比利时，2018年10-11月。 计算语言学协会。 doi: 10.18653/v1/D18-1259。 URL https://aclanthology.org/D18-1259。
Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William W. Cohen, Ruslan Salakhutdinov, and Christopher D. Manning. HotpotQA：一个用于多样化、可解释多跳问答的数据集，2018b. URL https://arxiv.org/abs/1809.09600。
Shunyu Yao, Howard Chen, John Yang, and Karthik Narasimhan. WebShop：面向可扩展的真实世界网络交互与基于语言的智能体，2023a。
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. ReAct：在语言模型中协同推理与行动，2023b. URL https://arxiv.org/abs/2210.03629。

Ziqi Zhou, Jingyue Zhang, Jingyuan Zhang, Yangfan He, Boyue Wang, Tianyu Shi, and Alaa Khamis. 基于大语言模型的强化学习自动驾驶中人本奖励优化。 arXiv预印本 arXiv:2405.04135, 2024。

用户：基于给定的段落回答问题。只给我答案，不要输出任何其他词语。以下为给定段落：“信任制度”（有时被误称为“受托人制度”）是直到20世纪80年代在美国部分地区实施的一种监狱纪律与安全体系……

基于给定的段落回答问题。只给我答案，不要输出任何其他词语。

问题：哪个案件先被提交至法院，Miller v. California 还是 Gates v. Collier？

答案：

助手：Gates v. Collier

# 检查器：

错误答案：忽略了具体年份：助手没有准确确认每个案件的具体年份，导致对时间顺序的错误判断。

对问题理解不足：在回答问题时，助手可能没有充分理解或仔细分析所提供的信息，导致误判。

# 反思：

在回答关于哪个案件（Miller v. California 或 Gates v. Collier）先被提起的问题时，我错误地认为“Gates v. Collier”早于“Miller v. California”。实际上，“Miller v. California”在先。这表明我在判断事件的时间顺序上出现了错误。

改进措施：仔细核实信息：当回答涉及时间顺序的问题时，务必仔细检查每个事件的具体时间点，以确保准确性。

时间线工具：处理多个事件或案件时，使用时间线工具有助于理清先后顺序，避免疏忽。

复核机制：在提交最终答案前，建立自我复核机制，重新检查所有相关信息和细节，确保回答的准确性。

结论：这一错误提醒我在处理与时间和顺序相关的问题时需要更加细致和谨慎。通过反思和改进，我希望在未来能提供更准确、可靠的答案，避免类似错误的发生。

助手（使用SAGE）的回复：

Miller v. California

图4：带有SAGE的HotpotQA示例图示。

# 理论分析

# A.1 基于艾宾浩斯遗忘曲线的记忆优化的信息论视角

本研究提出的记忆优化机制基于艾宾浩斯遗忘曲线。它通过优先保留关键信息并丢弃无关数据来动态管理短期记忆（STM）和长期记忆（LTM）。该机制可视为根据每个信息单元的信息熵计算其保留强度 $S(I_{t})$。从理论上讲，可以将其解释为最大化信息熵，以表明该机制有效缓解了信息过载问题 Cover & Thomas (2006)。也就是说，通过优先保留高熵（即高不确定性）信息，模型提高了其信息处理效率。

首先，信息的保留强度定义为：

$$
S \left(I _ {t}\right) = \frac {H \left(I _ {t}\right)}{f (t)} \tag {13}
$$

其中分子 $H(I_{t})$ 表示时刻 $t$ 内容的信息熵，$f(t)$ 模拟遗忘曲线。

记忆优化的目标是在记忆容量约束下最大化所保留信息的效用：

$$
\max  \sum_ {t} M _ {t} \cdot S \left(I _ {t}\right), \quad \text {s . t .} \quad \sum_ {t} M _ {t} \leq C \tag {14}
$$

此处 $C$ 表示总记忆容量，$M_{t} \in \{0,1\}$ 表示时刻 $t$ 的信息是否被保留（1）或丢弃（0）。

使用拉格朗日乘子法，我们构造拉格朗日函数：

$$
\mathcal {L} \left(M _ {t}, \lambda\right) = \sum_ {t} M _ {t} \cdot S \left(I _ {t}\right) - \lambda \left(\sum_ {t} M _ {t} - C\right) \tag {15}
$$

对 $\mathcal{L}$（最优记忆保留）关于 $M_{t}$ 求导并设为零，得到最优条件：

$$
\frac {\partial \mathcal {L}}{\partial M _ {t}} = S \left(I _ {t}\right) - \lambda = 0 \quad \Rightarrow \quad \left\{ \begin{array}{l l} \text {保留} I _ {t} & \text {如果} S \left(I _ {t}\right) \geq \lambda \\ \text {丢弃} I _ {t} & \text {如果} S \left(I _ {t}\right) <   \lambda \end{array} \right. \tag {16}
$$

此规则与SAGE框架中使用的基于阈值的记忆保留策略一致。

# A.2 迭代反馈与博弈论模型

多智能体系统通常依赖于强化学习（RL）方法，因此其理论基础对于确保算法收敛到稳定解（如纳什均衡）至关重要 Fudenberg & Tirole (1991)。后续理论提供了收敛的形式化保证，表明我们提出的算法并非随机设计。相反，它通过建立稳健的标准，证实了其稳定性和性能优势，从而超越了标准方法。

# A.2.1 参与者及其策略空间设定

用户（U）：提供任务描述 $T_U$ 和约束 $C_U$。

助手（A）：选择行动 $a_{t} \sim \pi_{\theta}(\cdot \mid s_{t})$，其中 $\pi_{\theta}$ 为策略。(17)

检查器（C）：生成反馈 $f_{t}$，旨在减少误差 $\| o_{t} - o^{*}\|_{F}$，

其中 $o_t$ 是助手的输出，$o^*$ 是期望的（真实）输出，$\| \cdot \|_F$ 表示Frobenius范数。

对于效用函数，我们有：

助手的效用 $R_A$：衡量任务性能（例如BLEU分数、准确率）：$R_A =$  $a_t$ 的任务性能度量。

检查器的效用 $R_C$：通过误差减少量衡量反馈准确性：

$$
R _ {C} \propto \Delta \| o _ {t} - o ^ {*} \| _ {F}.
$$

(18)

整个交互可视为一个三参与者博弈，其中：助手（A）优化其策略 $\pi_{\theta}$ 以最大化 $R_{A}$，而检查器（C）旨在最小化 $\| o_t - o^*\|$（即最大化 $R_{C}$）。用户U设定任务和约束，指导助手和检查器的表现。接下来我们希望证明，在有限策略空间和连续效用函数的条件下，该多智能体博弈存在纳什均衡。

# A.2.2 定理3.1的证明设置

首先，我们列出此证明的路线图。

- 可以证明，在有限策略空间和连续效用函数的条件下，该多智能体博弈存在纳什均衡。
- 根据Debreu-Glicksberg-Fan定理（纳什存在定理的推广），若每个参与者的策略空间是紧致凸集，且效用函数在其自身策略上是连续且拟凹（或凹）的，则至少存在一个纳什均衡。
- 然后，助手的策略 $\pi_{\theta}$ 使用策略梯度方法更新。由于 $R_{A}$ 是 $\pi_{\theta}$ 的连续函数，助手的效用是连续的。
- 之后，检查器的反馈策略可通过凸优化（例如最小二乘回归）获得，因此 $R_{C}$ 是凸函数。
- 因此，存在纳什均衡 $(\pi_{\theta}^{*}, f^{*})$，在该均衡下助手和检查器的策略彼此稳定：

$$
\pi_ {\theta} ^ {*} = \arg \max  _ {\pi} R _ {A} (\pi , f ^ {*}), \quad f ^ {*} = \arg \max  _ {f} R _ {C} \left(\pi_ {\theta} ^ {*}, f\right) \tag {19}
$$

现在开始证明。

引理A.1. 令 $S_{1}, S_{2}, \ldots, S_{N}$ 为 $N$ 个参与者中每个参与者的有限策略集，且令 $u_{i}: S_{1} \times \dots \times S_{N} \to \mathbb{R}$ 对每个 $i$ 连续。则在该多智能体博弈中存在纳什均衡。

证明。 对于每个参与者 $i$，定义混合策略集为

$$
\Delta \left(\mathcal {S} _ {i}\right) = \left\{x _ {i} \in \mathbb {R} ^ {\left| \mathcal {S} _ {i} \right|} \mid x _ {i} (s) \geq 0 \text {对所有} s \in \mathcal {S} _ {i}, \sum_ {s \in \mathcal {S} _ {i}} x _ {i} (s) = 1 \right\}. \tag {20}
$$

每个集合 $\Delta(S_i)$ 是 $\mathbb{R}^{|S_i|}$ 中的一个单纯形，因而是非空、紧致且凸的。定义参与者 $i$ 的期望效用函数：

$$
U _ {i} \left(x _ {1}, \dots , x _ {N}\right) = \sum_ {\left(s _ {1}, \dots , s _ {N}\right) \in \mathcal {S} _ {1} \times \dots \times \mathcal {S} _ {N}} \left(\prod_ {j = 1} ^ {N} x _ {j} \left(s _ {j}\right)\right) u _ {i} \left(s _ {1}, \dots , s _ {N}\right). \tag {21}
$$

由于策略空间有限且 $u_{i}$ 连续（因此在有限集上有界），函数 $U_{i}$ 在乘积空间 $\prod_{j=1}^{N} \Delta(S_{j})$ 上连续。

对于每个参与者 $i$，定义最佳响应对应为：

$$
B R _ {i} \left(x _ {- i}\right) = \arg \max  _ {x _ {i} \in \Delta \left(\mathcal {S} _ {i}\right)} U _ {i} \left(x _ {i}, x _ {- i}\right), \tag {22}
$$

其中 $x_{-i}$ 表示除 $i$ 外所有参与者的混合策略。由于 $\Delta(S_i)$ 是紧致的且 $U_i$ 连续且关于 $x_i$ 线性（因此是凹的），最大值存在且 $BR_i(x_{-i})$ 非空、凸且紧致。现在定义整体最佳响应对应：

$$
B R (x) = B R _ {1} \left(x _ {- 1}\right) \times B R _ {2} \left(x _ {- 2}\right) \times \dots \times B R _ {N} \left(x _ {- N}\right), \tag {23}
$$

其中 $x = (x_{1}, x_{2}, \ldots, x_{N})$。乘积空间 $\prod_{i=1}^{N} \Delta(\mathcal{S}_{i})$ 是紧致凸的，且对应 $BR$ 具有非空、凸且紧致的值，并且是上半连续的（由于期望效用的连续性和线性）。因此，根据角谷不动点定理，存在一个不动点

$$
x ^ {*} = \left(x _ {1} ^ {*}, x _ {2} ^ {*}, \dots , x _ {N} ^ {*}\right) \in \prod_ {i = 1} ^ {N} \Delta \left(\mathcal {S} _ {i}\right) \tag {24}
$$

使得

$$
x ^ {*} \in B R \left(x ^ {*}\right). \tag {25}
$$

此不动点即为混合策略下的纳什均衡。

因此，在有限策略空间和连续效用函数的条件下，存在纳什均衡。根据Debreu-Glicksberg-Fan定理（纳什存在定理的推广），若每个参与者的策略空间是紧致凸集且效用函数在其自身策略上是连续且拟凹（或凹）的，则至少存在一个纳什均衡。

![](images/f5456e195737b2afed5afc4c417389813ed3f616047db35f8e8e056064ab4ec2.jpg)

引理A.2. 根据引理A.1，令 $I = \{1, 2, \dots, n\}$ 为参与者集合。对于每个参与者 $i$，令 $X_{i} \subset \mathbb{R}^{d_{i}}$ 为紧致凸策略集，并定义 $X = \prod_{i=1}^{n} X_{i}$。假设每个参与者的效用函数 $u_{i}: X \to \mathbb{R}$ 在 $X$ 上连续，且对于固定的 $x_{-i}$ 在其坐标 $x_{i}$ 上拟凹（或凹）。则根据Debreu-Glicksberg-Fan定理，存在至少一个纳什均衡 $x^{*} = (x_{1}^{*}, x_{2}^{*}, \ldots, x_{n}^{*}) \in X$。

证明. 对于每个参与者 $i$，定义最佳响应对应

$$
B R _ {i} \left(x _ {- i}\right) = \left\{x _ {i} \in X _ {i}: u _ {i} \left(x _ {i}, x _ {- i}\right) = \max  _ {y _ {i} \in X _ {i}} u _ {i} \left(y _ {i}, x _ {- i}\right) \right\}. \tag {26}
$$

由于 $u_{i}$ 连续且 $X_{i}$ 紧致，最大值可达；因此 $BR_{i}(x_{-i}) \neq \emptyset$。$u_{i}$ 在 $x_{i}$ 上的拟凹性（或凹性）确保集合

$$
\left\{x _ {i} \in X _ {i}: u _ {i} \left(x _ {i}, x _ {- i}\right) \geq \alpha \right\} \tag {27}
$$

对于任意 $\alpha \in \mathbb{R}$ 是凸的。特别地，对于每个固定的 $x_{-i}$，集合 $BR_{i}(x_{-i})$ 是凸的。

$u_{i}$ 的连续性意味着最佳响应对应 $BR_{i}$ 是上半连续的。这意味着对于任何收敛于 $x_{-i}$ 的序列 $\{x_{-i}^{(k)}\}$ 以及任何对应的满足 $x_{i}^{(k)} \in BR_{i}(x_{-i}^{(k)})$ 的序列 $\{x_{i}^{(k)}\}$，$\{x_{i}^{(k)}\}$ 的每个极限点 $x_{i}$ 都属于 $BR_{i}(x_{-i})$。

现在定义聚合最佳响应对应：

$$
B R (x) = B R _ {1} \left(x _ {- 1}\right) \times B R _ {2} \left(x _ {- 2}\right) \times \dots \times B R _ {n} \left(x _ {- n}\right), \tag {28}
$$

其中 $x = (x_{1}, x_{2}, \ldots, x_{n}) \in X$。注意：(1) $X$ 是 $\mathbb{R}^{d_1 + d_2 + \dots + d_n}$ 的非空、紧致凸子集。(2) 对于每个 $i$，$BR_{i}(x_{-i})$ 非空且凸。(3) 对应 $BR$ 是上半连续的。

根据Debreu-Glicksberg-Fan不动点定理，存在一个不动点 $x^{*} \in X$ 使得 $x^{*} \in BR(x^{*})$。即对于每个 $i \in I, x_{i}^{*} \in BR_{i}(x_{-i}^{*})$。这意味着没有参与者能通过单方面偏离 $x^{*}$ 来提高其效用，这正是纳什均衡的定义。

![](images/c04d857efa07606437105d205b050b08f4e04eb8808812ebd0b573083bcb24f2.jpg)

接下来，基于上述引理，我们希望证明助手的策略 $\pi_{\theta}$ 使用策略梯度方法 Sutton & Barto (2018) 更新。由于 $R_{A}$ 是 $\pi_{\theta}$ 的连续函数，助手的效用是连续的。

引理A.3. 令 $\Theta$ 表示助手策略 $\pi_{\theta}$ 的参数空间，且令助手的效用为

$$
R _ {A} \left(\pi_ {\theta}\right) = f \left(\pi_ {\theta}\right), \tag {29}
$$

其中 $f: \Pi \to \mathbb{R}$ 是策略空间 $\Pi$ 上的连续函数。假设映射 $\theta \mapsto \pi_{\theta}$ 是连续的。则复合函数

$$
F (\theta) = f \left(\pi_ {\theta}\right) \tag {30}
$$

在 $\theta$ 上连续。此外，由于助手的策略使用策略梯度方法更新，更新规则

$$
\theta_ {k + 1} = \theta_ {k} + \alpha_ {k} \nabla_ {\theta} F (\theta_ {k}) \tag {31}
$$

利用了连续函数的梯度。

证明。 我们将证明分为两部分：

步骤1：效用函数的连续性。 由于映射 $\theta \mapsto \pi_{\theta}$ 连续且函数 $f:\Pi \to \mathbb{R}$ 根据假设连续，它们的复合 $F(\theta) = f\bigl (\pi_{\theta}\bigr)$ 在 $\theta$ 上连续。形式上，对于任意 $\epsilon >0$，存在 $\delta >0$ 使得对于所有满足 $\| \theta -\theta^{\prime}\| < \delta$ 的 $\theta ,\theta^{\prime}\in \Theta$，

$$
\left| F (\theta) - F \left(\theta^ {\prime}\right) \right| = \left| f \left(\pi_ {\theta}\right) - f \left(\pi_ {\theta^ {\prime}\right) \right| <   \epsilon . \tag {32}
$$

步骤2：策略梯度更新。 在策略梯度框架中，助手根据以下规则更新其参数：

$$
\theta_ {k + 1} = \theta_ {k} + \alpha_ {k} \nabla_ {\theta} F (\theta_ {k}), \tag {33}
$$

其中 $\alpha_{k} > 0$ 是（可能递减的）步长，$\nabla_{\theta}F(\theta_k)$ 表示 $F$ 在 $\theta_{k}$ 处的梯度。由于 $F$ 连续（且在典型的平滑假设下，可微且梯度连续），梯度 $\nabla_{\theta}F$ 是良定义的。因此，策略梯度更新是从 $\theta_{k}$ 到 $\theta_{k + 1}$ 的连续映射。

由于每次迭代的更新基于助手效用 $F(\theta)$ 的梯度（该梯度连续），$\theta$ 中的微小扰动仅导致梯度和更新参数的小变化。这表明更新过程是稳定的，即助手的效用 $R_A(\pi_\theta) = F(\theta)$ 在策略梯度更新序列下连续变化 Sutton & Barto (2018)。

因此，由于 $R_A$ 是 $\pi_{\theta}$ 的连续函数且 $\pi_{\theta}$ 连续依赖于 $\theta$，助手的效用是连续的，且策略梯度更新是良定义的。

接下来我们希望证明，检查器的反馈策略可通过凸优化（例如最小二乘回归）获得，因此 $R_{C}$ 是凸函数。

引理A.4. 令 $\mathcal{F}$ 为向量空间的凸子集，并假设检查器的反馈策略由凸优化问题的解 $f\in \mathcal{F}$ 给出：

$$
\min  _ {f \in \mathcal {F}} J (f) = \sum_ {i = 1} ^ {n} \left(y _ {i} - f \left(x _ {i}\right)\right) ^ {2}, \tag {34}
$$

其中 $x_{i}$ 为给定输入，$y_{i}$ 为目标输出。定义检查器的效用函数

$$
R _ {C} (f) = J (f). \tag {35}
$$

则 $R_C$ 是 $\mathcal{F}$ 上的凸函数；即对于任意 $f_1, f_2 \in \mathcal{F}$ 和任意 $\lambda \in [0,1]$，有

$$
R _ {C} (\lambda f _ {1} + (1 - \lambda) f _ {2}) \leq \lambda R _ {C} (f _ {1}) + (1 - \lambda) R _ {C} (f _ {2}). \tag {36}
$$

证明. 我们通过验证平方误差损失是凸函数且凸组合保持凸性来证明 $R_C$ 的凸性。

对于每个数据点 $i$，考虑函数

$$
\ell_ {i} (f) = \left(y _ {i} - f \left(x _ {i}\right)\right) ^ {2}. \tag {37}
$$

由于对于任意实数 $t$，函数 $t^2$ 是凸的，且映射 $f \mapsto y_i - f(x_i)$ 是仿射的（因此是凸的），复合 $f \mapsto (y_i - f(x_i))^2$ 是凸的。特别地，对于任意 $f_1, f_2 \in \mathcal{F}$ 和 $\lambda \in [0,1]$，

$$
\ell_ {i} (\lambda f _ {1} + (1 - \lambda) f _ {2}) \leq \lambda \ell_ {i} (f _ {1}) + (1 - \lambda) \ell_ {i} (f _ {2}). \tag {38}
$$

由于检查器的总体损失（即效用函数）

$$
R _ {C} (f) = \sum_ {i = 1} ^ {n} \ell_ {i} (f) \tag {39}
$$

是有限个凸函数的和，因此 $R_C$ 在 $\mathcal{F}$ 上是凸的；即对于任意 $f_1, f_2 \in \mathcal{F}$ 和 $\lambda \in [0,1]$，

$$
\begin{array}{l} R _ {C} \left(\lambda f _ {1} + (1 - \lambda) f _ {2}\right) = \sum_ {i = 1} ^ {n} \ell_ {i} \left(\lambda f _ {1} + (1 - \lambda) f _ {2}\right) \\ \leq \lambda \sum_ {i = 1} ^ {n} \ell_ {i} \left(f _ {1}\right) + (1 - \lambda) \sum_ {i = 1} ^ {n} \ell_ {i} \left(f _ {2}\right) \tag {40} \\ = \lambda R _ {C} (f _ {1}) + (1 - \lambda) R _ {C} (f _ {2}). \\ \end{array}
$$

因此：

$$
R _ {C} (f) = \sum_ {i = 1} ^ {n} \left(y _ {i} - f \left(x _ {i}\right)\right) ^ {2} \text {在} \mathcal {F} \text {上是凸的。} \tag {41}
$$

□

因此，通过凸优化（例如最小二乘回归）导出的检查器反馈策略确保对应的效用函数 $R_{C}$ 是凸的。

# A.2.3 定理3.1的形式化证明

我们希望根据前述引理将定理3.1重述为如下引理：

引理A.5（定理3.1）。假设助手的策略空间 $\Pi$ 和检查器的策略空间 $\mathcal{F}$ 是非空、紧致且凸的集。并假设：$R_A:\Pi \times \mathcal{F}\to \mathbb{R}$ 对于固定的 $f$ 在 $\pi$ 上连续，$R_C:\Pi \times \mathcal{F}\rightarrow \mathbb{R}$ 对于固定的 $\pi$ 在 $f$ 上是凸的。则存在纳什均衡 $\pi_{\theta}^{*},f^{*}$，定义为

$$
\pi_ {\theta} ^ {*} = \underset {\pi \in \Pi} {\arg \max } R _ {A} (\pi , f ^ {*}) \quad \text {且} \quad f ^ {*} = \underset {f \in \mathcal {F}} {\arg \max } R _ {C} \left(\pi_ {\theta} ^ {*}, f\right). \tag {42}
$$

证明。 对于每个固定的 $f \in \mathcal{F}$，定义助手的最佳响应集：

$$
B R _ {A} (f) = \left\{\pi \in \Pi : R _ {A} (\pi , f) = \max  _ {\pi^ {\prime} \in \Pi} R _ {A} \left(\pi^ {\prime}, f\right) \right\}. \tag {43}
$$

根据假设（i）和 $\Pi$ 的紧致性，最大值可达且 $BR_{A}(f)$ 非空。（$R_{A}$ 的连续性保证了 $f$ 的微小变化会导致 $R_{A}(\cdot, f)$ 的微小变化。）

类似地，对于每个固定的 $\pi \in \Pi$，定义检查器的最佳响应集：

$$
B R _ {C} (\pi) = \left\{f \in \mathcal {F}: R _ {C} (\pi , f) = \max  _ {f ^ {\prime} \in \mathcal {F}} R _ {C} \left(\pi , f ^ {\prime}\right) \right\}. \tag {44}
$$

由于假设（ii）意味着 $R_C$ 在 $f$ 上是凸的且 $\mathcal{F}$ 是凸且紧致的，我们得出 $BR_C(\pi)$ 是非空、凸且闭的。

考虑对应关系

$$
H: \Pi \times \mathcal {F} \rightarrow \Pi \times \mathcal {F}, \quad H (\pi , f) = B R _ {A} (f) \times B R _ {C} (\pi). \tag {45}
$$

由上述论证可知：对于每个 $(\pi, f) \in \Pi \times \mathcal{F}$，集合 $H(\pi, f)$ 非空。$BR_A(f)$ 是闭的（由连续性和紧致性），$BR_C(\pi)$ 根据假设（ii）是凸的（且闭的）。因此，$H(\pi, f)$ 是凸且闭的。

由于定义域 $\Pi \times \mathcal{F}$ 是非空、紧致且凸的，且对应关系 $H$ 具有非空、凸且闭的值，并且是上半连续的（这源于 $R_{A}$ 在 $\pi$ 上的连续性和 $R_{C}$ 在 $f$ 上的凸性），角谷不动点定理保证了存在一个不动点

$$
\left(\pi^ {*}, f ^ {*}\right) \in \Pi \times \mathcal {F} \quad \text {使得} \quad \left(\pi^ {*}, f ^ {*}\right) \in H \left(\pi^ {*}, f ^ {*}\right). \tag {46}
$$

根据 $H$ 的定义，该不动点满足

$$
\pi^ {*} \in B R _ {A} \left(f ^ {*}\right) \quad \text {且} \quad f ^ {*} \in B R _ {C} \left(\pi^ {*}\right), \tag {47}
$$

这等价于

$$
\pi^ {*} = \underset {\pi \in \Pi} {\arg \max } R _ {A} (\pi , f ^ {*}) \quad \text {且} \quad f ^ {*} = \underset {f \in \mathcal {F}} {\arg \max } R _ {C} (\pi^ {*}, f). \tag {48}
$$

因此，助手或检查器的任何单方面偏离都不会提高各自的效用；换言之，策略对 $(\pi^{*},f^{*})$ 是一个纳什均衡。

# B 详细数据集信息

(1) 操作系统（OS） 将LLMs集成到操作系统中对于自动化和优化任务具有巨大潜力。这种集成需要一个安全、用户友好的界面来确保有效的LLM‑OS交互。LLMs必须准确理解操作系统上下文以进行明智的操作，并优先考虑安全性以防止滥用。此外，系统应有效处理错误并向用户提供清晰的反馈，从而增强整体交互和控制。解决这些方面可以改变各行各业中的计算机交互和效率。

(2) 数据库（DB） LLMs通过SQL操作真实数据库的能力至关重要，因为数据库分析在日常活动中具有重要性和复杂性。先前的研究强调了LLMs在自动化数据库访问方面的有效性，例如T5QL，一种新的SQL生成方法。此外，经过微调的LLMs（如GPT-3.5）已展现出从文本中提取和链接复杂科学信息的能力，从非结构化文本中获取结构化知识并构建广泛的数据库。
(3) WebShop（WS） WebShop是一个创新的电子商务网站环境模拟，包含118万种真实世界产品和12,087条众包文本指令。它挑战智能体根据给定指令导航各种类型的网页并执行多样化操作来查找、定制和购买产品。WebShop的挑战包括理解组合指令、查询（重新）表述、处理网页上的噪声文本以及战略性探索。
(4) 知识图谱（KG） LLMs在构建和与知识图谱（KG）交互方面的应用为增强语义理解和信息检索提供了有前景的机会。这涉及评估模型生成和解释数据内复杂相互关系的能力，从而促进更直观和上下文感知的响应。LLMs在这一领域的有效性能可以显著提高基于结构化知识的AI推理和决策能力。
(5) Mind2Web（M2W） Mind2Web（M2W）是一个为开发能够通过语言指令在真实网站上执行复杂任务的网络智能体而设计的数据集。它包含来自31个领域137个站点的2000多个任务。M2W的真实网络环境和多样化的用户交互使其成为推进AI导航能力的关键平台。
(6) ALFWorld（ALF） ALFWorld将交互式TextWorld环境与ALFRED数据集的具身任务连接起来，使智能体能够学习抽象策略并将其应用于真实世界任务。它支持抽象推理和具体执行，允许智能体在基于文本的模拟器中规划行动，并在视觉环境中执行这些任务。这种方法通过利用简化研究改进的模块化设计，增强了智能体在语言理解和视觉导航等各个领域的泛化和问题解决能力。

# C 与任务拆分智能体的比较

为了比较SAGE框架与现有智能体在不同任务类型和数据集上的表现，我们进行了全面评估。结果详见表6。SAGE在任务完成时间、答案准确率、对话连贯性和步骤完成准确率方面表现出优越性能，突显了其在管理复杂、多层面任务方面的有效性。

表6：不同任务类型和数据集上任务拆分SOTA智能体评估

<table><tr><td>智能体</td><td>任务完成时间（分钟）</td><td>答案准确率（QA）（%）</td><td>对话连贯性（%）</td><td>步骤完成准确率（%）</td></tr></table>

任务1：长形式问答（HotpotQA）

<table><tr><td>BabyAGI</td><td>7.8</td><td>74.1</td><td>-</td><td>-</td></tr><tr><td>AutoGPT</td><td>8.1</td><td>76.3</td><td>-</td><td>-</td></tr><tr><td>HuggingGPT</td><td>6.7</td><td>79.2</td><td>-</td><td>-</td></tr><tr><td>LangChain Agent</td><td>7.9</td><td>77.0</td><td>-</td><td>-</td></tr><tr><td>TaskMatrix.AI</td><td>6.5</td><td>80.3</td><td>-</td><td>-</td></tr><tr><td>SAGE - ChatGPT-4</td><td>10.6</td><td>82.5 (+6.0)</td><td>-</td><td>-</td></tr></table>

任务2：多轮对话完成（MultiWOZ）

<table><tr><td>BabyAGI</td><td>8.2</td><td>-</td><td>73.5</td><td>-</td></tr><tr><td>AutoGPT</td><td>8.5</td><td>-</td><td>75.6</td><td>-</td></tr><tr><td>HuggingGPT</td><td>7.1</td><td>-</td><td>78.1</td><td>-</td></tr><tr><td>LangChain Agent</td><td>8.3</td><td>-</td><td>76.5</td><td>-</td></tr><tr><td>TaskMatrix.AI</td><td>6.8</td><td>-</td><td>79.9</td><td>-</td></tr><tr><td>SAGE - ChatGPT-4</td><td>10.9</td><td>-</td><td>81.6 (+5.8)</td><td>-</td></tr></table>

任务3：具有依赖关系的顺序任务（ALFWorld）

<table><tr><td>BabyAGI</td><td>8.7</td><td>-</td><td>-</td><td>71.5</td></tr><tr><td>AutoGPT</td><td>8.3</td><td>-</td><td>-</td><td>73.1</td></tr><tr><td>HuggingGPT</td><td>7.5</td><td>-</td><td>-</td><td>75.2</td></tr><tr><td>LangChain Agent</td><td>7.8</td><td>-</td><td>-</td><td>72.8</td></tr><tr><td>TaskMatrix.AI</td><td>6.6</td><td>-</td><td>-</td><td>76.4</td></tr><tr><td>SAGE - ChatGPT-4</td><td>10.7</td><td>-</td><td>-</td><td>82.3 (+5.9)</td></tr></table>

# D 示例

# 在TriviaQA上使用GPT与SAGE的案例研究。

# 用户：

基于给定的段落回答问题。只给我答案，不要输出任何其他词语。以下为给定段落：

英国运河史 - 伦敦运河博物馆 英国运河史 首页 > 历史 > 英国运河 在运河史上，英国并非先驱。中国人可以声称中国大运河是最早的运河之一，建于十世纪……

基于给定的段落回答问题。只给我答案，不要输出任何其他词语。

问题：贝塞麦工艺生产哪种金属？

答案：

# 助手：

该文件内容似乎是一份关于土耳其行政区划的HTML文档，包含人口统计、图表和地图。该文件包含典型的网页脚本、元数据和结构化数据。

# 检查器：

明确目标：回答用户问题时，应专注于直接回答问题，而不引入无关信息。文档处理：在确认文档内容是否与问题相关之前，不应直接处理文档的细节。

# 反思：

问题描述：用户希望了解系统为何基于用户输入输出不相关的HTML文档内容，并寻求详细的反馈和反思。错误原因：输入误解：系统错误地假设用户上传了文件并试图读取其内容，而用户仅提供了文本输入。处理逻辑错误：在没有明确判断用户意图的情况下，系统直接解析并输出了文件内容。用户体验问题：无关输出：用户期望简洁、相关的答案，但系统提供了冗长且无关的HTML内容，影响了用户体验。沟通不畅：未能准确理解和响应用户真实需求，导致回答偏离主题。深度反思与改进建议：明确用户意图：准确解析用户输入：增强系统的自然语言处理能力，以准确区分用户是上传了文件还是仅提供了文本输入。用户反馈机制：实施用户反馈机制，及时调整对用户意图的理解。例如，通过确认问题来验证用户是否上传了文件。优化处理逻辑：分层处理流程：在系统设计中，将文件处理逻辑与文本响应逻辑分离，以避免误判。例如，当用户上传文件时，单独处理文件内容；当用户输入文本时，直接提供相关答案。预处理检查：在处理文件之前，进行预处理检查，确认文件内容是否符合预期。……

使用SAGE的LLMs响应：钢。

# 真实答案

钢。

# 在LCC上使用GPT与SAGE的案例研究。

# 用户：

import networkx as nx import pickle from Queue import PriorityQueue import copy
import random import string import sys class MultiDiGraphEdgeKey(nx.MultiDiGraph):

# 助手：

你将获得一个过去经验的记录，其中你被分配了一项任务但未能完成。反思所采取的策略和行动。制定一个简洁的新行动计划，该计划需考虑到你之前的错误。以下是两个示例：示例1：如果你忘记锁门，计划每次都要双重检查门锁。示例2：如果你错过了截止日期，计划提前设置提醒……

# 检查器：

给定代码是Camerini算法的一部分，该算法用于对有向图中的边进行排序。该算法特别适用于涉及在复杂网络中识别最优或接近最优子结构的问题，如树形图或生成树。该算法有两个主要阶段：

收缩阶段：此阶段识别并收缩图中的环，创建超节点。这种简化有助于更有效地处理环，并为扩展阶段做好准备。

扩展阶段：将环收缩为超节点后，此阶段将超节点扩展回其原始结构，从而得到一个排序后的树形图，其中边根据特定标准进行排序或优先排序。

# 使用SAGE的LLMs响应：

Z.addedge(eu, ev, **data.copy())) self.init/graph, Y, Z) A = best(root) self.init(graph) e, d = self.next(A, Y, Z) w = self.getgraphscore(A) - d if d != float('inf') else float('inf') P.put((-w, e, A, Y, Z)) solutions.append(A) return solutions
def bestbranching(self, root): return self.best(root)

def bestarborescencenorooted(self, root): return self.best(root)

def bestarborescencerooted(self, root): return self.best(root)

def getgraphscore(self, graph): return sum(data[self attr] for u, v, data in graphEdges(data=True))

def findroots(self, graph): roots = [node for node, degree in graph.indegree() if degree == 0] return roots .......

# 在Repobench‑P上使用GPT与SAGE的案例研究。

# 用户：

请完成以下代码。{src//kademlia//operation//KadRefreshOperation.java
public class KadRefreshOperation implements Operation
private final KadServer server;
private final KademliaNode localNode;
private final KademliaDHT dht;
private final KadConfiguration config;
public KadRefreshOperation.....

# 助手：

为了制定新的行动计划，让我们分析之前的错误并提出解决方案：错误1：在KadRefreshOperation类中，execute()方法调用了BucketRefreshOperation和ContentRefreshOperation，但没有任何错误处理或异常处理。这可能导致意外的错误和失败。解决方案：在KadRefreshOperation类的execute()方法中添加适当的错误处理和异常处理。这将确保任何错误或异常都能得到妥善处理，从而使执行能够顺利进行……

# 检查器：

在'KadRefreshOperation'类中，当'execute()'方法调用'BucketRefreshOperation'和'ContentRefreshOperation'时没有错误处理。分析：如果'BucketRefreshOperation'或'ContentRefreshOperation'抛出异常，整个'execute()'方法将失败，可能导致整个系统的刷新操作中断。在'StoreOperation'类中，'execute()'方法没有处理DHT中已存在内容的情况。分析：'execute()'方法总是返回1作为存储节点数量，这显然是错误的。正确的节点数量应根据内容是否已存在于DHT中返回。解决方案：在存储内容之前，检查其是否已存在。如果存在，返回0；否则，存储内容并返回实际的存储节点数量。

# 使用SAGE的LLMs响应：

private final transient KademliaRoutingTable routingTable; private final transient Kad-Configuration config; private final transient MessageFactory messageFactory;

/* 定时刷新操作 */ private final Timer refreshTimer;
/* * 初始化Kademlia系统 */ @param ownerId 该所有者的ID * @param nodeId 该节点的ID * @param InetAddress 该节点的地址 * @param port 该节点的端口 * @param config Kad系统的配置 */ @throws java.io.IOException */ public JKademliaNode(String ownerId, KademliaId nodeId, InetAddress InetAddress, int port, KadConfiguration config) throws IOException { this ownerId = ownerId; this.config = config;

/* 初始化节点 */ this.localNode = new Node(nodeId, InetAddress, port);
/* 初始化服务器 */ this.server = new KadServer(localNode.getNodeId(), config);
