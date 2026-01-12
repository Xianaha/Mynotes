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
- **Flat (1D)**：无拓扑结构
  - 对话历史：MemGPT, Mem0, MemoryBank
  - 用户画像：AI Persona, MPC, ChatHaruhi
  - 经验池：Reflexion, ExpeL, Voyager
  - 多模态：Ego-LLaVA, MovieChat, MA-LMM

- **Planar (2D)**：单图层结构化
  - 树结构：HAT, MemTree
  - 图结构：A-MEM, Zep, HippoRAG, D-SMART
  - 混合：Optimus-1, D-SMART

- **Hierarchical (3D)**：多图层跨层链接
  - 金字塔结构：HiAgent, GraphRAG, ILM-TR
  - 多层特化：H-Mem, HippoRAG 2, AriGraph, CAM
  - 多代理：G-Memory

#### 1.2 Parametric Memory（参数化记忆）
- **Internal**：注入模型权重
  - 预训练：LMLM, HierMemLM
  - 中训练：Agent-Founder, Early Experience
  - 后训练：Character-LM, SELF-PARAM, MEND, ROME

- **External**：外挂参数模块
  - Adapter：MLP-Memory, K-Adapter, WISE, ELDER
  - 辅助LM：MAC, Retroformer

#### 1.3 Latent Memory（潜空间记忆）
- **Generate**：生成新表示
  - 单模态：Gist, AutoCompressor, MemoryLLM, M+, Titans
  - 多模态：CoMem, Time-VLM, MemoryVLA

- **Reuse**：复用KV Cache
  - Memorizing Transformers, FOT, LONGMEM, SirLLM

- **Transform**：压缩/转换
  - Scissorhands, SnapKV, H2O, RazorAttention

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