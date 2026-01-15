# Agent

# Agent Memory
![agent memory](./Image/Agent%20memory%20with%20other%20memory.jpg)

## 一、核心动机
- **为什么需要新分类体系？**
  - 传统长/短期记忆分类过时
  - 2025年方法爆炸：工具记忆、测试时扩展、多模态记忆
  - 术语混乱：declarative/episodic/semantic/parametric等概念模糊
  - 研究碎片化：动机、实现、假设、评估标准差异巨大

## 二、概念辨析（Section 2）
- **Agent Memory vs LLM Memory**
  - LLM Memory：内部KV Cache、长上下文机制、架构修改（Mamba）
  - Agent Memory：外部持久化、环境驱动、跨任务演化
  - 重叠：Few-shot提示、自反思、KV压缩可视为Agent Memory的短期机制
  
- **Agent Memory vs RAG**
    - 核心区别概述

        **RAG（检索增强生成）**：本质是**静态外部知识注入**，专注于为单次LLM调用补充事实性知识。它像一个**开卷考试助手**，允许模型带着《百科全书》进场，考察的是"翻书速度"和"定位精度"，典型场景是知识密集型问答（如HotpotQA）。其核心是"检索即服务"，检索流水线（索引→召回→重排→生成）相对固定，不随时间演化。

        **Agent Memory**：本质是**动态认知演化**，是智能体与环境持续交互的**自传式记录**。它像一个**长期管家**，需要记住用户半年来的偏好变更、任务进度、失败教训，并主动更新知识体系。核心在于"记忆即身份"，支持跨会话、跨任务自我进化（如GAIA深度研究、SWE-bench代码修复）。

    - 灰色地带：为什么两者边界模糊？

        实践中存在大量**概念重叠**，导致标题、方法论和评估经常混淆：

            1. **评估任务重叠**：许多自称"Agent Memory"的系统却在RAG的短程QA任务（如HotpotQA）上测试，而有些"RAG系统"实际上实现了持续自我改进，不断蒸馏知识。

            2. **技术栈共享**：两者共享向量索引、语义搜索、图检索等基础组件，但**设计哲学不同**：
            - RAG：检索是**工具**，用完即弃
            - Agent Memory：记忆是**状态**，持续生长

            3. **HippoRAG现象**：该系统被两个社区同时视为各自领域的突破，说明跨任务、长程检索的需求正在融合两种范式。

    - 深入辨析：基于Mei et al. (2025)的RAG分类法

        1. 模块化RAG (Modular RAG)

            **定义**：检索流水线被分解为索引、检索、重排、过滤、上下文组装等**静态模块**，像一条**装配线**。

            **Agent Memory中的对应**：这些技术出现在**检索阶段**，但记忆本身是可读写的：
            - **相同点**：都用向量搜索（FAISS）、语义匹配、规则过滤
            - **不同点**：Agent Memory的检索结果会**反馈**给记忆库（如Mem0, MemOS），形成闭环
            - **本质区别**：模块化RAG是**只读数据库**，Agent Memory是**可读写文件系统**

        2. 图RAG (Graph RAG)

            **定义**：知识库被构建为**知识图谱/概念图**，利用**图遍历**进行多跳推理。

            **Agent Memory中的对应**：当智能体积累关系洞察时，图结构**自然涌现**：
            - **动态性**：Agent Memory的图不是静态的（如HippoRAG），而是**活的经验图谱**：
            - 节点：概念、任务、实体（可新增/合并/删除）
            - 边：因果关系、时序依赖、发现路径（随交互演化）
            - **代表性系统**：Mem0g, A-MEM, Zep, G-Memory
            - **本质区别**：图RAG是**预制地图**，Agent Memory是**探索中绘制的动态地图**

        3. Agentic RAG (智能体RAG)

            **定义**：检索被集成到**自主决策循环**中，LLM主动控制**何时、如何、检索什么**（如PlanRAG, Self-RAG）。

            **与Agent Memory的关系**：**概念最接近，但知识归属不同**：
            - **Agentic RAG**：检索外部**任务特定数据库**（如临时搜索Web）
            - **Agent Memory**：维护**内部持久化记忆基座**，跨任务累积**自我经验**
            - **协同场景**：Agentic RAG决定"现在需要查什么"，Agent Memory提供"我过去学到了什么"

    - 关键区别总结表  
        | 维度 | 模块化RAG | 图RAG | Agentic RAG |
        | :--- | :--- | :--- | :--- |
        | 知识来源 | 外部静态库 | 外部静态图 | 外部动态源 |
        | 记忆归属 | 无 | 无 | 内部经验库 |
        | 时间维度 | 单时刻 | 单时刻 | 跨任务时间轴 |
        | Agent Memory 中的角色 | 仅检索机制 | 结构灵感源 | 概念近亲 |
        | | 可用 | 需动态化 | 需内化 |
  
- **Agent Memory vs Context Engineering**

    **总体定位**：两者的关系是**交集而非层级包含**，是两种不同操作范式的协同，而非谁包含谁。

    - **Context Engineering**：**资源管理范式**
        - 将上下文窗口视为**受限的计算资源**
        - 核心目标：优化信息负载（指令、知识、状态、memory），缓解**输入容量与生成能力的不对称**
        - 视角：Agent Memory只是其**上下文组装函数中的一个变量**，需要高效调度以最大化推理效能

    - **Agent Memory**：**认知建模范式**
        - 侧重于具有**演化身份的持久实体**的认知建模
        - 视角：Context Engineering是其**实现层**，确保认知连续性在模型物理限制内运作

    **重叠（Overlap）**：在**工作内存技术实现**上显著趋同

    - **共享机制**：两者都采用相同的**信息压缩、组织、选择**技术
    - Token修剪与基于重要性的选择（如H2O, SnapKV）
    - 滚动摘要（Rolling Summary）作为**缓冲区管理策略**和**瞬态情景记忆机制**
    - 动态信息检索与递归状态更新
    - **实践效果**：在长时程交互中，两者的边界实际消失，因为都依赖相同的**摘要、检索、状态更新**原语

    **区别（Distinctions）**：在**长生命周期Agent**场景中最为明显

    - **Context Engineering的核心关注点**：
        - **接口组织**：优化LLM与环境的交互接口结构
        - **工具集成**：工具调用流水线、通信协议（如MCP）的标准化
        - **约束**：确保指令、工具调用、中间状态在上下文窗口内**可格式化、可调度、可执行**
        - **层级**：在**资源分配和接口正确性**层面运作，强调**句法有效性**和**执行效率**

    - **Agent Memory的核心关注点**：
        - **知识持久化**：事实性知识的长期存储（如MemoryBank）
        - **经验演化**：从成功/失败中抽象程序性知识（如ReasoningBank, Voyager）
        - **身份维持**：跨任务/情节的一致性行为和自我呈现
        - **参数内化**：将外部记忆整合进模型参数（如SELF-PARAM, WISE）
        - **层级**：在**学习、适应、自主性**的认知层面运作

    **本质比喻**：
    - **Context Engineering** = **操作系统的内存管理器**：决定哪些数据驻留内存、哪些换出，优化资源利用率
    - **Agent Memory** = **应用层的数据库系统**：决定存储什么知识、如何索引、何时更新，支撑业务逻辑

    **总结**：Context Engineering构建**外部支架**优化瞬时接口，Agent Memory构成**内部基础**维持持久状态。前者确保"现在能算得动"，后者确保"长期能学得会"。

## 三、三维分类体系（核心框架）

### 维度1：形式（Forms）- 记忆存储在哪？

#### 1.1 Token-level Memory（符号化记忆）
**核心思想**：记忆以**离散符号（文本/标记）**形式存储在外部系统中，类似于人类的笔记或日记。这种方式**可解释性强**、**易于编辑**，支持复杂的查询与推理，但存储开销较大，检索效率高度依赖索引质量。

- **Flat (1D)**：无拓扑结构
  - **比喻**：按时间顺序写的日记本，一页接一页。
  - **特点**：所有记忆条目**线性排列**，无结构化关联。适合存储**时序性强**但结构简单的数据。
  - **典型系统与实例**：
    - **对话历史**：MemGPT 将整个对话视为一个长序列，通过“分页”机制管理；Mem0 使用向量数据库存储每条消息。
    - **用户画像**：AI Persona 将用户偏好（如“喜欢咖啡”“怕冷”）以键值对形式线性存储。
    - **经验池**：Voyager 在探索 Minecraft 时，将成功的行动序列（如“如何挖钻石”）以文本形式存入经验库。
    - **多模态记忆**：Ego-LLaVA 将视觉观察与文本描述按时间戳拼接，形成跨模态的线性记录。

  - **进一步分类与演进**：随着研究的深入，Flat Memory 在对话、偏好、配置文件、经验和多模态等特定领域发展出更精细的设计：

    #### 对话记忆 (Conversation Memory)
    专注于存储和管理对话内容，防止遗忘：
    - **早期方法**：存储原始对话历史或生成递归摘要（Wang et al., 2025a; Lu et al., 2023; Wang et al., 2025h; Yuan et al., 2025b）
    - **MemGPT突破**：引入操作系统隐喻和分层管理，将活跃上下文与外部存储解耦（Packer et al., 2023a）
    - **后续工作**：Li et al., 2025k; Kang et al., 2025a 等在此基础上实现无限上下文管理
    - **精度提升**：memory单元的粒度与结构多样化，与认知对齐：
      - **紧凑表示**：COMEDY（Chen et al., 2025c）、Memory Sharing（Gao and Zhang, 2024a）、MemGuide（Du et al., 2025b）将信息压缩为语义表示或查询-响应对
      - **混合结构**：Alonso et al., 2024; MIRIX（Wang and Chen, 2025）采用向量-表组合等多功能memory类型
      - **认知边界**：基于句法元组（Chatterjee and Agarwal, 2025）或贝叶斯惊喜和段落结构的事件分割（Fountas et al., 2025; Pan et al., 2025）组织信息
    - **高级认知存储**：存储思维过程和叙事复杂性：
      - **思维记忆**：Think-in-Memory（Liu et al., 2023a）、RMM（Tan et al., 2025c）存储归纳思维和回顾性反思
      - **复杂场景**：ComoRAG（Wang et al., 2025f）、MOOM（Chen et al., 2025d）将memory分解为事实、情节、角色层面组件
    - **自主优化**：从静态存储转变为自适应系统：
      - **标准化操作**：Mem0（Chhikara et al., 2025）建立memory维护标准
      - **强化学习优化**：Yan et al., 2025b; Wang et al., 2025o 引入RL优化memory构建
      - **动态校准**：预测缺失信息（Nan et al., 2025）、管理token预算（Liu et al., 2025c）、减少冗余（Fang et al., 2025b）

    #### 偏好记忆 (Preference Memory)
    专注于建模用户不断演化的品味、兴趣和决策模式，尤其在推荐场景中：
    - **早期系统**：RecMind（Wang et al., 2024h）分离用户属性与领域知识
    - **工作流集成**：InteRecAgent（Huang et al., 2025d）将memory折叠到推荐工作流，保留用户配置和活动项目池
    - **结构化索引**：MR.Rec（Huang et al., 2025b）构建memory索引，归档完整交互过程，存储原始项目信息和类别偏好摘要
    - **对话设置**：Memocrs（Xi et al., 2024a）采用结构化设计：用户特定memory（跟踪实体和态度）+ 通用memory（聚合跨用户知识）

    #### 配置文件记忆 (Profile Memory)
    专注于存储和维护稳定的用户配置文件、角色属性或长期身份信息：
    - **早期框架**：MemoryBank（Zhong et al., 2024）按时间戳组织对话历史和事件摘要，逐步构建用户配置文件
    - **多维度扩展**：AI Persona（Wang et al., 2024f）处理多维人机交互信息
    - **实时一致性**：MPC（Lee et al., 2023）存储实时人设信息和对话摘要，确保长时间交互中行为一致
    - **综合机制**：Westhäuser et al., 2025 结合长期/短期memory与自动生成摘要，形成中期上下文，允许配置文件演化
    - **角色扮演**：
      - ChatHarui（Li et al., 2023a）从小说/剧本文本提取对话，保持角色一致
      - RoleLLM（Wang et al., 2024d）通过问答对捕获角色特定知识

    #### 经验记忆 (Experiential Memory)
    存储agent在交互任务中动态积累的经验，包括观察、思维链、行动轨迹和环境反馈：
    - **原始轨迹归档**：直接存储历史行为轨迹，通过检索重用成功/失败案例（Zhou et al., 2025a; Wang et al., 2025p）
    - **高级抽象**：将特定交互抽象为通用经验：
      - **反思模型**：Reflexion（Shinn et al., 2023b）区分短期轨迹历史和长期自我反思反馈
      - **思维模板**：将复杂历史压缩为工作流、规则模板或高级"思维模板"（Wang et al., 2024l; Kim et al., 2025a; Yang et al., 2024b）
    - **结构化组织**：
      - 构建领域特定知识库
      - 采用分层规划-执行memory架构
      - 结合类人遗忘和反思机制（Tang et al., 2025c,d; Ouyang et al., 2025; Ye et al., 2025b; Zhao et al., 2024; Liang et al., 2025）
    - **可执行技能**：在编程/工具使用环境中演变为代码仓库、程序脚本或工具使用条目：
      - 整合探索经验，迭代改进代码质量，动态修改底层逻辑（Wang et al., 2024a; Yin et al., 2025; Fang et al., 2025d; Xiao et al., 2025b）
      - 针对操作系统等复杂环境，将成功执行记录提炼为可重用示例或向量化表示（Zhang et al., 2025a; Han et al., 2025a）

    #### 多模态记忆 (Multimodal Memory)
    以离散token-level单元形式存储从原始多模态数据（图像、视频帧、音频段、文本）中提取的信息：
    - **可穿戴/以自我为中心**：
      - Ego-LLaVA（Shen et al., 2024）捕获第一人称视频并转换为语言描述
      - Memoro（Zulfikar et al., 2024）使用语音到文本形成基于嵌入的memory块
      - Livia（Xi and Wang, 2025）将长期用户memory整合到情感感知AR系统，应用遗忘曲线和修剪策略
    - **视频理解**：
      - MovieChat（Song et al., 2024）采用短期/长期分割，存储最近帧特征
      - MA-LMM（He et al., 2024）双库设计：原始视觉特征库 + 查询嵌入库
      - VideoAgent（Wang et al., 2024g）维护文本片段描述的时间memory + 跨帧实体追踪的对象级memory
      - Context-as-Memory（Yu et al., 2025b）在交互式视频生成中，仅将先前生成的帧存储为memory
    - **具身场景**：
      - KARMA（Wang et al., 2025q）双层memory：长期memory在3D场景图中存储静态对象；短期memory追踪对象位置和状态变化
      - Embodied VideoAgent（Fan et al., 2025）构建持久对象memory，与第一人称视频和传感器融合
      - Mem2Ego（Zhang et al., 2025l）分离三个memory存储：全局地图、地标描述、访问历史
      - MEMENTO（Kwon et al., 2025）提供评估框架，将多模态交互历史视为agent的memory

  - **优缺点总结**：
    - **优势**：简单性、可扩展性；memory可以以最小成本追加或修剪；相似性搜索等检索方法允许灵活访问，无需预定义结构；适合广泛回忆、情景积累和快速变化的交互历史
    - **局限**：缺乏显式的关系组织，连贯性和相关性高度依赖检索质量；随着memory增长，冗余和噪声累积；可能检索相关单元而不理解它们之间的关系，限制组合推理、长时程规划和抽象形成；在需要结构化推理或稳定知识组织的任务中受限

- **Planar (2D)**：单图层结构化
  - **定义**：Planar Memory 在 memory 单元之间引入了显式的组织拓扑，但仅在**单个结构层内**（无分层级别或跨层引用）。拓扑可以是图、树、表、隐式连接结构等，其中邻接、父子顺序或语义分组等关系在一个平面内编码。其核心在于通过建立显式关联机制突破单一存储池，实现了从单纯的"存储"到"组织"的跨越。
  - **比喻**：一张思维导图或知识网络，节点间有明确的连接关系。
  - **特点**：记忆被组织成**图（Graph）**或**树（Tree）**结构，支持**多跳推理**与**关系查询**，能够利用节点间的链接产生集体协同效应，编码更全面的上下文知识。
  - **典型系统与实例**：

    #### 树结构 (Tree)
    分层组织信息，处理不同级别的抽象：
    - **HAT**（Hierarchical Attention Tree, A et al., 2024）通过分割长交互并逐步聚合，构建分层聚合树，支持从粗到细的检索，在长上下文问答中表现优于平面向量索引。
    - **MemTree**（Rezazadeh et al., 2025c）引入动态表示，从孤立的对话日志推断分层模式，将具体事件总结为更高级别的概念，允许 agent 同时使用详细 memory 和抽象知识。

    #### 图结构 (Graph)
    由于能够捕捉复杂关联、因果关系和时间动态，图结构在 2D memory 中占主导地位：
    - **基础框架**：Ret-LLM（Modarressi et al., 2023）将外部存储抽象为可寻址的基于三元组的单元，使 LLM 能够与类似轻量级知识图谱的关系中心表交互。
    - **领域专用**：
      - **医学**：HuaTuo（Wang et al., 2023a）整合中文医学知识图谱和临床文本的结构化语料库，注入专业知识以微调基础模型。
      - **个性化**：KGT（Sun et al., 2024）实时编码用户偏好和反馈为用户特定知识图谱中的节点和边。
      - **推理密集型**：PREMem（Kim et al., 2025b）将部分推理负担转移到 memory 构建阶段，从原始对话推导结构化 memory 项及其演化关系。
      - **查询优化**：Memory-augmented Query Reconstruction（Xu et al., 2025b）维护专门的查询 memory，记录过去的 KG 查询和推理步骤，使用检索到的记录重建更准确的查询。
    - **时序组织**：TeaFarm（iunn Ong et al., 2025）沿着分段时间线组织对话历史，应用结构化压缩管理终身上下文。
    - **对话增强**：
      - **COMET**（Kim et al., 2024b）使用外部常识库解析对话，动态更新具有推断隐藏属性的上下文感知人设图。
      - **A-MEM**（Xu et al., 2025c）将知识标准化为卡片式单元，通过相关性组织（相关 memory 放入同一"盒子"），构建完整的 memory 网络。
    - **多 agent 协作**：Intrinsic Memory Agents（Yuen et al., 2025）采用分区架构，子 agent 维护角色特定私有 memory，同时协作读写共享 memory。
    - **多模态统一**：M3-Agent（Long et al., 2025）将图像、音频和文本统一到以实体为中心的 memory 图中。
    - **导航与规划**：SALI（Pan et al., 2024）构建现实-想象混合 memory，将真实观察和想象的未来场景统一到一致的导航图中。

    #### 混合结构 (Hybrid)
    复杂任务需要混合架构，分离不同认知功能的同时共享公共 memory 基板：
    - **Optimus-1**（Li et al., 2024d）明确分离静态知识（用于规划的分层有向知识图谱）和动态交互（用于反思和自我改进的抽象多模态经验池）。
    - **D-SMART**（Lei et al., 2025）结合结构化事实 memory（持续更新的知识图谱）和基于遍历的推理树。

  - **优缺点总结**：
    - **优势**：
      1. **关联能力**：通过显式链接建立 memory 单元间的关系，支持超越简单迭代的检索机制（如结构化键值查找、图遍历）。
      2. **知识编码**：能够捕捉复杂关联、因果关系和时间动态，编码更全面的上下文知识。
      3. **推理支持**：适用于多跳推理、关系查询和需要结构化组织的任务。
    - **局限**：
      1. **单层限制**：没有分层存储机制，所有 memory 必须合并到单一整体模块中，难以处理高度复杂和多样化的任务场景。
      2. **构建成本**：高构建和搜索成本，可能阻碍实际部署。
      3. **可扩展性**：随着 memory 规模增长，扁平化设计可能导致冗余和性能下降。

- **Hierarchical (3D)**：多图层跨层链接
  - **定义**：分层 memory 跨层组织信息，使用层间连接将 memory 塑造成体积结构化空间。这种层次支持不同抽象程度的表示——从原始观察到紧凑的事件摘要，再到更高级别的主题模式。跨层连接进一步产生一个体积 memory 空间，系统不仅可以在单元间横向导航，还可以跨抽象级别纵向导航。分层 memory 超越了简单分层，旨在构建具有深度抽象能力和动态演化机制的复杂系统。这些工作通常采用多层次图结构或受神经科学启发的机制，构建一个更类人的体积 memory 空间，其中信息更丰富，memory 单元之间的连接更清晰、更明确。
  - **比喻**：多层图书馆，每层是一个大类（如历史、科学），层内再分书架，且层间有“电梯”可快速跳转。
  - **特点**：**多层次抽象** + **跨层链接**，既能高层概览，又能钻取细节，适合**长周期、复杂演化**的记忆需求。通过将 memory 节点放置在层次和关系维度的交叉点上，分层 memory 允许不同的 memory 相互作用并形成多维协同效应，有助于系统编码更全面、更深层次语境化的知识。
  - **典型系统与实例**：

    #### 金字塔结构 (Pyramid)
    将 memory 构建为多层次金字塔，信息逐步组织到更高层的抽象中，并以从粗到细的方式进行查询：
    - **HiAgent**（Hu et al., 2025a）通过以子目标为中心的分层工作 memory 管理长时程任务，为当前活动的子目标保留详细轨迹，同时将完成的子目标压缩为更高级别的摘要，可在需要时选择性检索。
    - **GraphRAG**（Edge et al., 2025）通过社区检测构建多层次图索引，递归地将实体级子图聚合为社区级摘要。
    - **Zep**（Rasmussen et al., 2025）将 agent memory 形式化为时序知识图谱，并类似地执行社区划分。
    - **ILM-TR**（Tang et al., 2024）采用树状金字塔索引，结合内循环机制，反复查询不同抽象级别的摘要并更新短期 memory 缓冲区，直到检索到的证据和生成的答案稳定。
    - **EMG-RAG**（Wang et al., 2024k）将可编辑 memory 图组织为三层，其中树状类型和子类索引（L1, L2）位于实体级 memory 图（L3）之上，确保可控的个性化。
    - **G-Memory**（Zhang et al., 2025c）使用三层图层次结构（洞察、查询和交互图）构建共享经验，使以查询为中心的遍历能够在跨试验的高层洞察和具体协作的紧凑轨迹之间垂直移动。

    #### 多层结构 (Multi-layer)
    强调分层专业化，将 memory 组织成专注于特定信息类型或功能的独立模块或级别：
    - **Lyfe Agents**（Kaiya et al., 2023）将突出的长期记录与低价值的瞬态细节分开，使系统能够维护一个紧凑的、行为重要的 memory 层。
    - **H-Mem**（Sun and Zeng, 2025）明确将长期对话 memory 排列为按语义抽象排序的多层层次结构，其中较低层存储细粒度的交互片段，较高层存储越来越压缩的摘要。
    - **HippoRAG**（Gutierrez et al., 2024）将 memory 分解为关联索引组件（实现为开放知识图谱）和底层段落存储，使用图谱层协调存储内容的多跳检索。
    - **HippoRAG 2**（Gutierrez et al., 2025）将此设计扩展到非参数持续学习设置，通过更深的段落集成和在线 LLM 过滤丰富了索引层。
    - **AriGraph**（Anokhin et al., 2024）在统一图内按信息类型分离 memory，结合编码环境结构的语义知识图谱世界模型，以及将具体观察链接回语义主干的事件级组件。
    - **SGMem**（Wu et al., 2025h）在原始对话之上添加了一个句子图 memory 层，将历史表示为分块单元内的句子级图。
    - **CAM**（Li et al., 2025f）通过将重叠的语义图逐步聚类成分层模式结构，对阅读过程本身进行分层。

  - **优缺点总结**：
    - **优势**：
      1. **多维协同**：通过层次和关系维度的交叉，允许 memory 节点相互作用形成多维协同效应。
      2. **深度语境化**：支持不同抽象级别的表示，能够编码更全面、更深层次语境化的知识。
      3. **强大检索**：支持复杂的多路径查询，可在每层内的关系网络之间以及层间的抽象级别之间移动，实现高精度的相关 memory 检索。
      4. **任务性能**：强大的检索能力使其在复杂任务中表现优异。
    - **局限**：
      1. **结构复杂性**：三维结构的复杂性及其密集的信息组织对检索效率和整体有效性带来挑战。
      2. **语义保持**：确保所有存储的 memory 保持语义意义是困难而关键的问题。
      3. **布局设计**：设计系统的最佳三维布局（层次和关系的组合）是一个具有挑战性的优化问题。
      4. **构建成本**：与平面结构相比，构建和维护分层 memory 的成本更高。

#### 1.2 Parametric Memory（参数化记忆）
**核心思想**：将记忆**编码到模型参数**中，使记忆成为模型“本能”的一部分。与将信息存储为可见且可编辑的离散单元的 token-level memory 不同，参数化 memory 将信息直接存储在模型的参数中，允许模型内部化和回忆信息而无需参考外部存储。这种方式**推理速度快**、无需外部检索，但更新困难、容量有限，且可解释性较弱。

基于 memory 相对于核心模型参数的存储位置，参数化 memory 可分为两种主要形式：
1. **内部参数化 memory**：memory 编码在模型的原始参数内（如权重、偏置），直接调整基础模型以纳入新知识或行为。
2. **外部参数化 memory**：memory 存储在额外的参数集中（如适配器、LoRA 模块、轻量级代理模型），模块化地附加在旁边而不修改原始模型权重。

- **Internal（内部参数化）**：注入模型权重
  - **比喻**：将知识内化为大脑的长期记忆，形成条件反射般的技能。
  - **特点**：直接修改主模型的权重，使知识“固化”在模型中；不会增加额外参数或附加模块；结构简单，无额外推理开销，但更新困难。
  - **训练阶段与典型系统**：
    - **预训练阶段**：在预训练阶段引入 memory 机制，解决长尾世界知识压缩问题：
      - **知识检索增强**：LMLM（Zhao et al., 2025b）、HierMemLM（Pouransari et al., 2025）存储用于知识检索的 memory，将知识本身存储于外部知识库。
      - **长窗口优化**：TNL（Qin et al., 2024b）、StreamingLLM（Xiao et al., 2024）优化注意力计算效率以增强长窗口 memory 能力。
    - **中期训练阶段**：在持续预训练阶段纳入来自下游任务的可泛化经验：
      - **Agent 经验整合**：Agent-Founder（Su et al., 2025）、Early Experience（Zhang et al., 2025j）整合 agent 经验，提高工具调用、具身模拟、推理等能力。
      - **长窗口性能提升**：Chen et al., 2024a 等方法提高 LLMs 的长窗口性能或效率，使模型能以更长窗口维护更多短期 memory。
    - **训练后阶段**：在训练后阶段纳入 memory 以适应下游任务：
      - **个性化与角色扮演**：Character-LM（Shao et al., 2023）、CharacterGLM（Zhou et al., 2024a）将 LLM 微调为不同特征或人格。
      - **知识编辑与模型更新**：
        - **蒸馏注入**：SELF-PARAM（Wang et al., 2025n）通过 KL 散度蒸馏注入额外知识，无需额外参数。
        - **外部存储+内部经验**：Room（Kim et al., 2023b）在外部存储知识，在内部保存经验。
        - **精准编辑**：KnowledgeEditor（Cao et al., 2021）、MEND（Mitchell et al., 2022）修改内部参数以实现快速知识编辑，仅更改需要编辑的知识。
        - **人格编辑**：PersonalityEdit（Mao et al., 2024）基于心理学人格理论提出 LLM 人格编辑数据集。
        - **抗干扰编辑**：APP（Ma et al., 2024）采用多训练目标，确保知识编辑期间相邻知识受最小干扰。
        - **安全编辑**：DINM（Wang et al., 2024c）使模型能学习拒绝危险请求而不影响正常功能。
        - **其他编辑方法**：AlphaEdit（Fang et al., 2025c）等进一步扩展模型编辑能力。
  - **优缺点总结**：
    - **优势**：结构简单，不给原始模型增加额外推理开销或部署成本；memory 完全内化，推理效率高。
    - **局限**：更新困难，需要重新训练，成本高昂且容易忘记旧 memory；更适合大规模存储领域知识或任务先验，而非短段的个性化 memory 或工作 memory。

- **External（外部参数化）**：外挂参数模块
  - **比喻**：为电脑加装外置硬盘或扩展卡，在不改动主系统的情况下增加存储容量。
  - **特点**：通过额外的参数模块（如 Adapter、LoRA、辅助 LM）扩展模型容量，每个模块可对应特定用户、领域或任务；memory 被编码到额外参数模块中，可添加、移除或替换而不干扰基础模型预训练表示空间。
  - **形式与典型系统**：
    - **基于适配器的模块**：附加到冻结基础模型的适配器模块，以模块化和可逆的方式存储和检索 memory：
      - **MLP-Memory**（Wei et al., 2025d）：通过 MLP 将 RAG 知识与 Transformer 解码器集成。
      - **K-Adapter**（Wang et al., 2021）：训练特定任务适配器注入新知识，保持原始骨干不变，实现持续知识扩展而不干扰预训练表示。
      - **WISE**（Wang et al., 2024e）：双参数 memory 设置——分离预训练知识和编辑知识，路由机制动态选择使用哪个参数 memory，减轻终身编辑期间的冲突。
      - **ELDER**（Li et al., 2025d）：维护多个 LoRA 模块，学习根据输入语义自适应选择或混合它们的路由函数，提高长期编辑场景中的鲁棒性和可扩展性。
      - **T-Patcher**（Huang et al., 2023）、Lin et al., 2025 等进一步扩展适配器方法。
    - **基于辅助 LM 的模块**：采用架构解耦的外部参数化 memory 形式，memory 存储在单独的模型或外部知识模块中：
      - **MAC**（Tack et al., 2024）：通过摊销网络将新文档信息压缩为紧凑调制，存储在 memory 库中。
      - **Retroformer**（Yao et al., 2024a）：提出记忆过去任务执行成功或失败经验的学习范式。
  - **优缺点总结**：
    - **优势**：在适应性和模型稳定性之间提供平衡；支持模块化更新、特定任务个性化、受控回滚；避免全模型微调可能导致的灾难性遗忘或全局权重失真。
    - **局限**：外部参数模块必须与模型内部表示流集成，memory 注入的有效性取决于外部参数与内部参数知识的接口能力；间接影响可能限制 memory 效用的充分发挥。

#### 1.3 Latent Memory（潜空间记忆）
**核心思想**：将记忆**压缩为连续向量表示（潜变量）**，在效率与表达能力之间取得平衡。潜空间 memory 将信息编码为连续向量表示，允许模型在不需要外部存储的情况下内部化和回忆信息。其核心是将信息压缩到连续向量空间中，通常通过生成新表示、复用现有中间状态或转换/压缩输入来实现。这种方式**存储紧凑**、支持相似性检索，但存在信息损失，且可解释性较弱。

- **Generate（生成新表示）**
  - **比喻**：将一篇长文章总结成一段精华摘要，只保留核心信息。
  - **特点**：训练模型将长输入（如多轮对话）**生成**一个固定长度的向量表示，作为后续推理的上下文。这些向量表示可以视为输入内容的语义摘要，能够捕获关键信息并忽略冗余细节。
  - **典型系统与实例**：
    - **单模态文本压缩**：
      - **Gist**（Mu et al., 2023）为长输入生成一个“要点”向量，将长上下文压缩为固定长度的表示。
      - **AutoCompressor**（Chevalier et al., 2023）训练模型自动压缩历史对话，生成上下文向量以供后续生成使用。
      - **MemoryLLM**（Xu et al., 2024a）将多轮交互压缩为单个记忆向量，并支持增量更新，实现长期对话记忆。
    - **多模态联合编码**：
      - **CoMem**（Yang et al., 2024a）将图像序列与文本描述共同编码到一个联合潜空间中，支持跨模态记忆检索。
      - **Time-VLM**（Zhao et al., 2024b）为视频片段生成时序记忆向量，捕获视频中的动态变化。
    - **其他生成方法**：MemGPT 的压缩机制、Mem0 的向量存储等也可视为生成潜表示的例子。

- **Reuse（复用中间状态）**
  - **比喻**：重复使用草稿纸上已计算好的中间结果，避免重复劳动。
  - **特点**：将 Transformer 在历史上下文中计算的 **Key-Value（KV）Cache** 存储起来，在遇到相似上下文时直接复用，极大提升推理效率。这种方法避免了重复计算，特别适合具有重复模式的输入。
  - **典型系统与实例**：
    - **Memorizing Transformers**（Wu et al., 2022）将历史 KV Cache 存储为外部记忆，通过注意力机制进行检索与复用。
    - **Fast-Overlap Transformers (FOT)**（Zhang et al., 2023b）识别输入中的重复模式，直接复用之前计算的注意力结果，显著加速推理。
    - **LongMem**（Wang et al., 2023b）设计分层机制存储 KV Cache，支持跨会话的记忆共享。
    - **其他复用方法**：H2O、SnapKV、Scissorhands、RazorAttention 等系统也涉及 KV Cache 的复用，但更侧重于选择重要部分，因此也属于 Transform 类别。

- **Transform（转换/压缩输入）**
  - **比喻**：将杂乱的书桌整理成井井有条的抽屉，丢弃无用物品，分类存放重要物品。
  - **特点**：对已有的表示（如原始标记序列或 KV Cache）进行**压缩、转换或重组织**，以降低计算开销。这些方法通常基于重要性评分或学习到的策略，选择信息量最大的部分，丢弃冗余信息。
  - **典型系统与实例**：
    - **基于重要性选择**：
      - **Scissorhands**（Xiao et al., 2023）根据重要性分数动态裁剪输入序列，保留关键标记。
      - **SnapKV**（Li et al., 2023c）学习选择最重要的 KV 对，丢弃冗余信息，优化注意力计算。
      - **H2O**（Zhang et al., 2023c）基于注意力分数选择关键标记，显著减少上下文长度。
      - **RazorAttention**（Li et al., 2024b）训练轻量级模型预测重要标记，实现智能剪枝。
    - **其他转换方法**：LLMLingua、CompAct 等硬压缩方法，以及 Gist、ICAE、AutoCompressor 等软压缩方法，虽然常用于工作记忆，但本质上也是将输入转换为更紧凑的潜表示。

  - **优缺点总结**：
    - **优势**：
      1. **高效存储**：潜表示通常比原始 token 序列更紧凑，节省存储空间。
      2. **快速检索**：支持相似性搜索，能够快速找到相关记忆。
      3. **计算效率**：复用 KV Cache 或压缩输入可以减少计算开销，加速推理。
      4. **可扩展性**：适合处理长上下文，避免上下文窗口限制。
    - **局限**：
      1. **信息损失**：压缩过程可能导致细节丢失，影响记忆的准确性。
      2. **可解释性差**：连续向量表示难以理解和编辑，不如符号化记忆直观。
      3. **训练需求**：许多方法需要额外的训练或微调，增加复杂性。
      4. **检索依赖**：检索效果依赖于表示质量和相似度度量，可能产生无关结果。

  - **讨论**：潜空间 memory 在效率与表达能力之间提供了良好的平衡，特别适合需要快速检索和紧凑存储的场景。然而，其“黑盒”性质使得调试和可控性成为挑战。未来的工作可能会探索更可解释的潜表示，以及更好地集成符号化和参数化 memory 的混合方法。

### 维度2：功能（Functions）- 为什么需要记忆？

#### 2.1 Factual Memory（事实记忆）
- **User Factual**：维持人机交互一致性
  - 对话连贯：MemGPT, Livia, RMM, Mem0
  - 目标一致：RecurrentGPT, Memolet, MemGuide
  - 具身场景：M3-Agent, MEMENTO

- **Environment Factual**：维持与外部世界一致性
  - 知识持久：HippoRAG, MemoryLLM, WISE, LMLM
  - 共享访问：Memory Sharing, MetaGPT, G-Memory, OASIS

#### 2.2 Experiential Memory（经验记忆）
- **Case-based**：存储原始轨迹
  - 轨迹：Memento, JARVIS-1, Continuous Memory
  - 解决方案：ExpeL, Synapse, MapCoder, FinCon

- **Strategy-based**：抽象为策略/工作流
  - 洞察：H2R, R2D2, BrowserAgent
  - 工作流：AWM, AgentKB
  - 模式：Buffer of Thoughts, ReasoningBank, PRINCIPLES

- **Skill-based**：编译为可执行能力
  - 代码片段：Voyager, Darwin Gödel Machine
  - 函数/脚本：CREATOR, SkillWeaver, LEGOMem
  - API：Gorilla, COLT, ToolLLM
  - MCP：Alita, MemTool

- **Hybrid**：混合表示
  - ExpeL, AgentKB, ChemAgent, G-Memory, MemVerse

#### 2.3 Working Memory（工作记忆）
- **Single-turn**：输入压缩
  - 硬压缩：LLMLingua, CompAct
  - 软压缩：Gist, ICAE, AutoCompressor
  - 混合：HyCo2, MELODI
  - 观察抽象：Synapse, VideoAgent, MA-LMM

- **Multi-turn**：状态维护
  - 状态折叠：MEM1, ReSum, MemSearcher
  - 层次折叠：HiAgent, Context-Folding, AgentFold, DeepAgent
  - 认知规划：SayPlan, KARMA, PRIME

### 维度3：动态（Dynamics）- 记忆如何运作？

#### 3.1 Memory Formation（形成）
- **Semantic Summarization**：语义摘要
  - 增量：MemGPT → Mem0 → Mem1 (PPO) → MemAgent (GRPO)
  - 分区：MemoryBank, COMEDY → ReadAgent, LightMem

- **Knowledge Distillation**：知识提取
  - 事实：TiM, RMM, MemGuide, M3-Agent
  - 经验：AWM, Memp, ExpeL, H2R → Memory-R1, Mem-α

- **Structured Construction**：结构化构建
  - 实体级：KGT, Mem0g → D-SMART → GraphRAG → AriGraph, Zep
  - 块级：HAT, RAPTOR → MemTree, H-MEM → CAM, G-Memory

- **Latent Representation**：潜表示
  - 文本：MemoryLLM, M+, MemGen
  - 多模态：CoMem, Mem2Ego, KARMA

- **Parametric Internalization**：参数内化
  - 知识：MEND → ROME → MEMIT → CoLoR
  - 能力：SFT, DPO, GRPO

#### 3.2 Memory Evolution（演化）
- **Consolidation**（整合）
  - 局部：RMM, VLN
  - 聚类：PREMem, TiM, CAM
  - 全局：MOOM, Matrix, AgentFold

- **Updating**（更新）
  - 外部更新：MemGPT → Zep → MOOM/LightMem → Mem-α
  - 模型编辑：ROME, MEMIT, MEMORYLLM, M+

- **Forgetting**（遗忘）
  - 基于时间：MemGPT, MAICC
  - 基于频率：XMem, KARMA, MemOS
  - 基于重要性：Zhong et al., VLN → TiM, MemTool

#### 3.3 Memory Retrieval（检索）
- **Timing & Intent**：检索时机与意图
  - 自动时机：MemGPT, MemTool → ComoRAG, MemGen
  - 自动意图：AgentRR → MemOS → H-MEM

- **Query Construction**：查询构建
  - 分解：Visconde, ChemAgent → PRIME, MA-RAG → AgentKB
  - 重写：HyDE → MemoRAG, MemGuide → Rewrite-Retrieve-Read

- **Retrieval Strategies**：检索策略
  - Lexical：TF-IDF, BM25
  - Semantic：Sentence-BERT, CLIP
  - Graph：AriGraph, HippoRAG, CAM
  - Hybrid：AgentKB, Semantic Anchoring, MemoriesDB

- **Post-Retrieval Processing**：后处理
  - 重排过滤：Semantic Anchoring → learn-to-memorize → Memory-R1
  - 聚合压缩：ComoRAG, MA-RAG → G-Memory

## 四、资源与框架（Section 6）

### 4.1 Benchmarks
- **记忆专用**：LoCoMo, LongMemEval, MemBench, StreamBench
- **通用代理**：GAIA, SWE-bench, ALFWorld, WebArena
- **长上下文**：LongBench, RULER, BABILong, MM-Needle

### 4.2 开源框架
- **Agent-centric**：MemGPT, Mem0, MemOS, Zep, MemoryOS
- **通用存储**：Pinecone, Chroma, Weaviate
- **新兴**：Memary, Cognee, SuperMemory, Second Me

## 五、前沿方向（Section 7）

### 5.1 生成式记忆（Memory Generation）
- 从检索到生成：检索→生成（ComoRAG） vs 直接生成（MemGen）
- 未来特性：上下文自适应、跨模态融合、学习式优化

### 5.2 自动化管理（Automated Management）
- 现状：手工规则 → RL辅助（Mem-α, Memory-R1）
- 未来：LLM自主工具调用 + 自优化记忆结构

### 5.3 RL驱动记忆（RL-Enabled Memory）
- 演进路径：RL-free → RL-assisted → Fully RL-driven
- 未来：消除手工先验 + 端到端记忆控制

### 5.4 多模态记忆（Multimodal Memory）
- 现状：视觉/视频记忆为主（Ego-LLaVA, VideoAgent）
- 未来：全模态统一表示 + 跨模态对齐

### 5.5 共享记忆（Shared Memory in MAS）
- 现状：孤立记忆 → 中心化共享（MetaGPT）
- 未来：Agent-aware访问 + 学习式同步 + 多模态一致性

### 5.6 世界模型记忆（World Model Memory）
- 现状：帧采样/滑动窗口 → 显式记忆库（UniWM, WorldMem）
- 未来：双系统架构（System 1/2）+ 主动记忆管理

### 5.7 可信记忆（Trustworthy Memory）
- 挑战：隐私泄露、可解释性差、幻觉传播
- 未来：权限控制 + 可审计更新 + 差分隐私 + 因果追溯

## 六、核心洞察

1. **记忆是认知过程，非存储容器**：动态演化 > 静态存储
2. **三维互补**：形式 × 功能 × 动态缺一不可
3. **RL是终极驱动**：从手工规则到自优化系统
4. **评估需考"长期驾驶"**：非"倒车入库"
5. **可信是部署前提**：隐私/可解释/抗幻觉

## 七、实践建议

- **研究者**：聚焦Section 5（Dynamics）+ Section 7（Frontiers）
- **工程师**：精读Section 3（Forms）+ 跑通MemGPT/Mem0
- **架构师**：从Section 4（Functions）出发设计系统
