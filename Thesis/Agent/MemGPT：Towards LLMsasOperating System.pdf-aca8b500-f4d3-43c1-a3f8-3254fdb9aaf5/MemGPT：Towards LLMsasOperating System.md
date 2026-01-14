# MemGPT：迈向将大语言模型作为操作系统

Charles Packer $^{1}$  Sarah Wooders $^{1}$  Kevin Lin $^{1}$

Vivian Fang<sup>1</sup> Shishir G. Patil<sup>1</sup> Ion Stoica<sup>1</sup> Joseph E. Gonzalez<sup>1</sup>

# 摘要

大语言模型（LLMs）已经彻底改变了人工智能领域，但受限于有限的上下文窗口，这阻碍了它们在扩展对话和文档分析等任务中的实用性。为了能够使用超出有限上下文窗口的上下文，我们提出了虚拟上下文管理技术，该技术借鉴了传统操作系统中分层内存系统的思想，通过物理内存和磁盘之间的分页提供了扩展虚拟内存的假象。利用这一技术，我们引入了MemGPT（MemoryGPT），这是一个智能管理不同存储层的系统，以有效地在LLM的有限上下文窗口内提供扩展上下文。我们在两个现代LLM有限上下文窗口严重限制其性能的领域评估了我们受操作系统启发的设计：文档分析，其中MemGPT能够分析远超底层LLM上下文窗口的大型文档；以及多会话聊天，其中MemGPT可以创建能够通过与其用户的长期互动来记忆、反思和动态演进的对话代理。我们在 https://research.memgpt.ai 发布了MemGPT代码和实验数据。

# 1. 引言

近年来，大语言模型（LLMs）及其底层的Transformer架构（Vaswani et al., 2017; Devlin et al., 2018; Brown et al., 2020; Ouyang et al., 2022）已成为对话AI的基石，并催生了广泛的消费者和企业应用。尽管取得了这些进展，但LLM使用的有限固定长度上下文窗口严重阻碍了它们在长对话或长文档推理方面的适用性。例如，最广泛使用的开源LLM在超过其最大输入长度之前只能支持几十条来回消息或推理一个短文档（Touvron et al., 2023）。

直接扩展Transformer的上下文长度会由于Transformer架构的自注意力机制而导致计算时间和内存成本的二次增长，这使得设计新的长上下文架构成为迫切的研究挑战（Dai et al., 2019; Kitaev et al., 2020; Beltagy et al., 2020）。虽然开发更长的模型是一个活跃的研究领域（Dong et al., 2023），但即使我们能克服上下文扩展的计算挑战，最近的研究表明，长上下文模型难以有效地利用额外的上下文（Liu et al., 2023a）。因此，考虑到训练最先进LLM所需的巨大资源以及上下文扩展的收益递减，迫切需要替代技术来支持长上下文。

在本文中，我们研究如何提供无限上下文的假象，同时继续使用固定上下文模型。我们的方法借鉴了虚拟内存分页的思想，该思想通过在主内存和磁盘之间分页数据，使应用程序能够处理远超可用内存的数据集。我们利用LLM代理函数调用能力的最新进展（Schick et al., 2023; Liu et al., 2023b）来设计MemGPT，一个受操作系统启发的用于虚拟上下文管理的LLM系统。使用函数调用，LLM代理可以读写外部数据源、修改自己的上下文，并选择何时向用户返回响应。

这些能力使得LLM能够有效地在上下文窗口（类似于操作系统中的"主内存"）和外部存储之间"分页"进出信息，类似于传统操作系统中的分层内存。此外，可以利用函数调用来管理上下文管理、响应生成和用户交互之间的控制流。这允许代理选择为单个任务迭代修改其上下文中的内容，从而更有效地利用其有限上下文。

在MemGPT中，我们将上下文窗口视为受限的内存资源，并为LLM设计了一个内存层次结构，类似于传统操作系统中使用的内存层级（Patterson et al., 1988）。传统操作系统中的应用程序与虚拟内存交互，虚拟内存通过操作系统将溢出数据分页到磁盘并在应用程序访问时（通过缺页中断）将数据检索回内存，提供了比实际可用物理（即主）内存更多内存资源的假象。为了提供类似更长上下文长度的假象（类似于虚拟内存），我们允许LLM通过一个'LLM操作系统'（我们称之为MemGPT）来管理放置在其自身上下文（类似于物理内存）中的内容。MemGPT使LLM能够检索未放置在上下文中的相关历史数据，并将较不相关的数据从上下文移出到外部存储系统。图3说明了MemGPT的组件。

内存层次结构、操作系统功能和基于事件的控制流的结合使用使得MemGPT能够使用具有有限上下文窗口的LLM处理无限上下文。为了展示我们新的受操作系统启发的LLM系统的实用性，我们在两个现有LLM性能受有限上下文严重限制的领域评估MemGPT：文档分析，其中标准文本文件的长度可能很快超过现代LLM的输入容量；以及对话代理，其中受有限对话窗口限制的LLM在扩展对话中缺乏上下文感知、角色一致性和长期记忆。在这两种设置中，MemGPT都能克服有限上下文的限制，胜过现有的基于LLM的方法。

# 2. MemGPT（MemoryGPT）

MemGPT受操作系统启发的多级内存架构区分了两种主要内存类型：主上下文（类似于主内存/物理内存/RAM）和外部上下文（类似于磁盘内存/磁盘存储）。主上下文由LLM提示令牌组成——主上下文中的任何内容都被视为上下文内，可以在推理过程中被LLM处理器访问。外部上下文指任何保持在LLM固定上下文窗口之外的信息。这种上下文外数据必须始终显式移动到主上下文中，以便在推理过程中传递给LLM处理器。MemGPT提供函数调用，使LLM处理器能够管理自己的内存，无需任何用户干预。

# 2.1. 主上下文（提示令牌）

MemGPT中的提示令牌分为三个连续部分：系统指令、工作上下文和FIFO队列。系统指令是只读（静态）的，包含有关MemGPT控制流、不同内存级别的预期用途以及如何使用MemGPT函数（例如如何检索上下文外数据）的说明。工作上下文是一个固定大小的读/写非结构化文本块，只能通过MemGPT函数调用写入。在对话设置中，工作上下文旨在用于存储关于用户和代理所采用角色的关键事实、偏好和其他重要信息，使代理能够与用户流畅对话。FIFO队列存储消息的滚动历史记录，包括代理和用户之间的消息，以及系统消息（例如内存警告）和函数调用输入输出。FIFO队列中的第一个索引存储一个系统消息，包含已从队列中移出的消息的递归摘要。

# 2.2. 队列管理器

队列管理器管理召回存储和FIFO队列中的消息。当系统收到新消息时，队列管理器将传入消息附加到FIFO队列，连接提示令牌并触发LLM推理以生成LLM输出（完成令牌）。队列管理器将传入消息和生成的LLM输出都写入召回存储（MemGPT消息数据库）。当通过MemGPT函数调用检索召回存储中的消息时，队列管理器将它们附加到队列的末尾以将它们重新插入LLM的上下文窗口中。

队列管理器还负责通过队列驱逐策略控制上下文溢出。当提示令牌超过底层LLM上下文窗口的"警告令牌计数"（例如上下文窗口的 $70\%$）时，队列管理器向队列插入一条系统消息，警告LLM即将发生队列驱逐（"内存压力"警告），以允许LLM使用MemGPT函数将FIFO队列中包含的重要信息存储到工作上下文或归档存储（存储任意长度文本对象的读/写数据库）中。当提示令牌超过"刷新令牌计数"（例如上下文窗口的 $100\%$）时，队列管理器刷新队列以释放上下文窗口中的空间：队列管理器驱逐特定数量的消息（例如上下文窗口的 $50\%$），使用现有递归摘要和已驱逐消息生成新的递归摘要。一旦队列被刷新，被驱逐的消息就不再是上下文内的，LLM无法立即查看，但它们会无限期存储在召回存储中，并可通过MemGPT函数调用读取。

# 2.3. 函数执行器（完成令牌的处理）

MemGPT通过LLM处理器生成的函数调用来协调主上下文和外部上下文之间的数据移动。内存编辑和检索完全是自主导向的：MemGPT基于当前上下文自主更新和搜索自己的内存。例如，它可以决定何时在上下文之间移动项目（例如当对话历史变得太长时，如图1所示），并修改其主上下文以更好地反映其对当前目标和职责的不断发展的理解（如图3所示）。我们通过在系统指令中提供明确的指令来指导LLM如何与MemGPT内存系统交互，从而实现自主导向的编辑和检索。这些指令包括两个主要部分：（1）内存层次结构及其各自用途的详细描述，以及（2）系统可以调用来访问或修改其内存的函数模式（包括其自然语言描述）。

在每个推理周期中，LLM处理器将主上下文（连接成单个字符串）作为输入，并生成输出字符串。MemGPT解析此输出字符串以确保正确性，如果解析器验证函数参数有效，则执行该函数。然后，包括发生的任何运行时错误（例如，当主上下文已达到最大容量时尝试添加到主上下文）在内的结果被MemGPT反馈给处理器。这个反馈循环使系统能够从其行为中学习并相应调整其行为。上下文限制的感知是使自我编辑机制有效工作的关键方面，为此MemGPT向处理器提示有关令牌限制的警告以指导其内存管理决策。此外，我们的内存检索机制被设计为意识到这些令牌约束，并实现分页以防止检索调用溢出上下文窗口。

表1. 常用模型和LLM API的上下文长度比较（数据收集于2024年1月）。*假设预提示为1k令牌，平均消息大小为 $\sim 50$ 令牌（ $\sim 250$ 字符）的近似消息计数。"开放"表示模型是开源的或开放权重的（vs仅通过API可用）。  

<table><tr><td rowspan="2">模型 / API 名称</td><td rowspan="2">开放?</td><td colspan="2">上下文窗口</td></tr><tr><td>令牌数</td><td>*消息数</td></tr><tr><td>Llama (1)</td><td>✓</td><td>2k</td><td>20</td></tr><tr><td>Llama 2</td><td>✓</td><td>4k</td><td>60</td></tr><tr><td>GPT-3.5 Turbo (发布版)</td><td>X</td><td>4k</td><td>60</td></tr><tr><td>Mistral 7B</td><td>✓</td><td>8k</td><td>140</td></tr><tr><td>GPT-4 (发布版)</td><td>X</td><td>8k</td><td>140</td></tr><tr><td>GPT-3.5 Turbo</td><td>X</td><td>16k</td><td>300</td></tr><tr><td>GPT-4</td><td>X</td><td>32k</td><td>~600</td></tr><tr><td>Claude 2</td><td>X</td><td>100k</td><td>~2000</td></tr><tr><td>GPT-4 Turbo</td><td>X</td><td>128k</td><td>~2600</td></tr><tr><td>Yi-34B-200k</td><td>✓</td><td>200k</td><td>~4000</td></tr></table>

# 2.4. 控制流和函数链

在MemGPT中，*事件*触发LLM推理：事件是MemGPT的广义输入，可以包括用户消息（在聊天应用程序中）、系统消息（例如主上下文容量警告）、用户交互（例如用户刚刚登录的警报，或他们完成文档上传的警报），以及按定期运行定时事件（允许MemGPT在没有用户干预的情况下"无提示"运行）。MemGPT使用解析器处理事件，将其转换为可以附加到主上下文并最终作为输入馈送到LLM处理器的纯文本消息。

许多实际任务需要按顺序调用多个函数，例如，从单个查询中导航多个结果页面，或从不同查询的单独文档中整理主上下文中的数据。函数链允许MemGPT在将控制权返回给用户之前顺序执行多个函数调用。在MemGPT中，函数可以带有一个特殊标志调用，该标志请求在请求的函数完成执行后立即将控制权返回给处理器。如果存在此标志，MemGPT会将函数输出添加到主上下文并（与暂停处理器执行相反）。如果不存在此标志（产生），MemGPT将不运行LLM处理器，直到下一个外部事件触发（例如用户消息或计划中断）。

# 3. 实验

我们在两个长上下文领域评估MemGPT：对话代理和文档分析。对于对话代理，我们扩展了现有的多会话聊天数据集（Xu et al., 2021），并引入了两个新的对话任务，用于评估代理在长时间对话中保留知识的能力。对于文档分析，我们在（Liu et al., 2023a）的现有任务上对MemGPT进行基准测试，用于长文档上的问答和键值检索。我们还提出了一个新的嵌套键值检索任务，需要跨多个数据源整理信息，测试代理从多个数据源整理信息的能力（多跳检索）。我们公开发布了我们增强的MSC数据集、嵌套KV检索数据集以及2000万篇维基百科文章的嵌入数据集，以促进未来研究。我们的基准测试代码可在 https://research.memgpt.ai 获取。

实施细节。在讨论OpenAI模型时，除非另有说明，否则'GPT-4 Turbo'指特定的gpt-4-1106-preview模型端点（上下文窗口为128,000），'GPT-4'指gpt-4-0613（上下文窗口为8,192），'GPT-3.5 Turbo'指gpt-3.5-turbo-1106（上下文窗口为16,385）。在实验中，我们使用所有基线模型（GPT-4、GPT-4 Turbo和GPT 3.5）运行MemGPT，以展示底层模型性能如何影响MemGPT的性能。

# 3.1. MemGPT用于对话代理

虚拟伴侣和个性化助手等对话代理旨在与用户进行自然的长期互动，可能跨越数周、数月甚至数年。这对具有固定长度上下文的模型提出了挑战，这些模型只能引用有限的对话历史。"无限上下文"代理应无缝处理连续交流而无边界或重置。当与用户对话时，此类代理必须满足两个关键标准：（1）一致性 - 代理应保持对话连贯性。提到的新事实、偏好和事件应与用户和代理的先前陈述一致。（2）参与度 - 代理应利用关于用户的长期知识来个性化响应。引用先前的对话使对话更加自然和引人入胜。

因此，我们根据这两个标准评估我们提出的系统MemGPT：（1）MemGPT是否利用其内存来提高对话一致性？它是否能记住过去互动中的相关事实、偏好和事件以保持连贯性？（2）MemGPT是否通过利用内存产生更具吸引力的对话？它是否自发地纳入长程用户信息以个性化消息？通过评估一致性和参与度，我们可以确定与固定上下文基线相比，MemGPT在多大程度上处理长期对话交互的挑战。其满足这些标准的能力将证明无界上下文是否为对话代理提供了有意义的益处。

数据集。我们在Xu等人（2021）引入的多会话聊天（MSC）数据集上评估MemGPT和我们的固定上下文基线，该数据集包含由人工标注者生成的多会话聊天日志，每个标注者被要求在的所有会话期间扮演一致的角色。MSC中的每个多会话聊天共有五个会话，每个会话包含大约十几条消息。作为我们一致性实验的一部分，我们创建了一个新会话（会话6），其中包含相同两个角色之间的单个问答响应对。

# 3.1.1. 深度内存检索任务（一致性）。

我们基于MSC数据集引入了一个新的"深度内存检索"（DMR）任务，旨在测试对话代理的一致性。在DMR中，用户向对话代理提出一个问题，该问题明确指回先前的对话，并且具有非常狭窄的预期答案范围。我们使用一个单独的LLM生成了DMR问答（QA）对，该LLM被指示从一个用户向另一个用户写一个问题，该问题只能使用从过去会话中获得的知识才能正确回答（有关详细信息，请参见附录）。

我们使用ROUGE-L分数（Lin, 2004）和一个"LLM评判员"来评估生成的响应与"黄金响应"的质量，该评判员被指示评估生成的响应是否与黄金响应一致（GPT-4已被证明与人类评估者具有高度一致性（Zheng et al., 2023））。在实践中，我们注意到生成的响应（来自MemGPT和基线）通常比黄金响应更冗长。我们使用ROUGE-L召回（R）指标来解释生成的代理回复相对于相对较短的黄金答案标签的冗长性。

MemGPT利用内存保持连贯性：表2显示了MemGPT与固定内存基线的性能。我们比较使用不同底层LLM的MemGPT，并与不使用MemGPT的基LLM作为基线进行比较。基线能够看到过去五个对话的有损摘要，以模拟扩展的递归摘要过程，而MemGPT则可以访问完整的对话历史，但必须通过分页搜索查询来访问内存（以便将它们带入主上下文）。在此任务中，我们看到MemGPT明显提高了底层基LLM的性能：从MemGPT到相应的LLM基线时，准确率和ROUGE分数都有明显下降。

# 3.1.2. 对话开场白任务（参与度）。

在"对话开场白"任务中，我们评估代理从先前对话积累的知识中制作吸引用户的消息的能力。为了使用MSC数据集评估对话开场白的"吸引力"，我们将生成的开场白与黄金角色进行比较：一个引人入胜的对话开场白应利用角色中包含的一个（或多个）数据点，这在MSC中有效地总结了所有先前会话中积累的知识。我们还与人类生成的黄金开场白进行比较，即后续会话中的第一个响应。我们在表3中报告了MemGPT开场白的CSIM分数。我们测试了使用不同基LLM的MemGPT的几种变体。

MemGPT利用内存提高参与度：如表3所示，MemGPT能够制作与手写人类开场白类似甚至偶尔超过其性能的引人入胜的开场白。我们观察到MemGPT倾向于制作比人类基线更冗长且涵盖更多角色信息方面的开场白。此外，我们可以看到将信息存储在工作上下文是生成引人入胜开场白的关键。

# 3.2. MemGPT用于文档分析

文档分析也因当今Transformer模型的有限上下文窗口而面临挑战。如表1所示，开源和闭源模型都受到上下文长度受限（OpenAI模型的上下文窗口高达128k令牌）。然而许多文档很容易超过这些长度；例如，法律或财务文档，如年度报告（SEC Form 10-K），很容易超过百万令牌大关。此外，许多真实的文档分析任务需要跨多个此类冗长文档建立联系。考虑到这些情况，很难想象盲目扩展上下文是解决固定上下文问题的方案。最近的研究（Liu et al., 2023a）也对简单扩展上下文的实用性提出了质疑，因为他们发现大上下文模型中的注意力分布不均匀（模型更擅长回忆其上下文窗口开头或结尾的信息，而不是中间位置的令牌）。为了能够跨文档进行推理，需要更灵活的内存架构，如MemGPT。

# 3.2.1. 多文档问答。

为了评估MemGPT分析文档的能力，我们在Liu等人（2023a）的检索器-阅读器文档QA任务上对MemGPT与固定上下文基线进行基准测试。在此任务中，从NaturalQuestions-Open数据集中选择一个问题，检索器为该问题选择相关的维基百科文档。然后将这些文档作为输入馈送给阅读器模型（LLM），并要求其使用提供的文档回答问题。与Liu等人（2023a）类似，我们评估阅读器准确性，同时增加检索到的文档数量 $K$。

在我们的评估设置中，固定上下文基线和MemGPT使用相同的检索器，该检索器使用相似性搜索（余弦距离）在OpenAI的text-embedding-ada-002嵌入上选择前 $K$ 个文档。我们使用MemGPT的默认存储设置，该设置使用PostgreSQL进行归档内存存储，并通过pgvector扩展启用向量搜索。我们预计算嵌入并将它们加载到数据库中，该数据库使用HNSW索引以实现近似的亚秒级查询时间。在MemGPT中，整个嵌入文档集被加载到归档存储中，检索器自然通过归档存储搜索功能（基于余弦相似性执行向量搜索）出现。在固定上下文基线中，前 $K$ 个文档使用独立于LLM推理的检索器获取，类似于Liu等人（2023a）中原始的检索器-阅读器设置。

我们使用2018年末的维基百科转储，遵循过去关于NaturalQuestions-Open的工作（Izacard & Grave, 2020; Izacard et al., 2021），并采样了50个问题子集进行评估。采样的问题和嵌入的维基百科段落均已公开发布。我们使用LLM评判员评估MemGPT和基线的性能，以确保答案正确地从检索到的文档中得出，并避免将非精确字符串匹配视为不正确。

我们在图5中展示了文档QA任务的结果。固定上下文基线的性能大致限制在检索器的性能，因为它们使用其上下文窗口中呈现的信息（例如，如果嵌入搜索检索器未能使用提供的问题呈现黄金文章，则固定上下文基线保证永远不会看到黄金文章）。相比之下，MemGPT通过查询归档存储有效地能够对检索器进行多次调用，使其能够扩展到更大的有效上下文长度。MemGPT主动从其归档存储中检索文档（并且可以迭代分页浏览结果），因此MemGPT可用的文档总数不再受限于适合LLM处理器上下文窗口的文档数量。

由于基于嵌入的相似性搜索的限制，文档QA任务对所有方法都具有挑战性。我们观察到，所选问题的黄金文档（由NaturalQuestions-Open标注）通常出现在前十几个检索结果之外，甚至更远。检索器性能直接转化为固定上下文基线结果：GPT-4的准确性在检索到的文档较少时相对较低，随着向上下文窗口添加更多文档而继续提高，因为它正确地限制自己基于检索到的文档中的信息回答问题。虽然MemGPT在理论上不受次优检索器性能的限制（即使基于嵌入的排名是有噪声的，只要完整的检索器排名包含黄金文档，仍然可以通过足够的分页检索器调用找到），但我们观察到MemGPT在耗尽检索器数据库之前通常会停止分页浏览检索器结果。

为了将固定上下文基线评估为超出其默认上下文长度，我们截断检索器返回的文档段，以将相同数量的文档固定到可用上下文中。正如预期的那样，随着文档缩小，相关片段（在黄金文档中）被遗漏的机会增加，文档截断会降低准确性，如图5所示。MemGPT使用GPT-3.5时性能显著下降，这是由于GPT-3.5有限的函数调用能力，而使用GPT-4时性能最佳。

# 3.2.2. 嵌套键值检索（KV）。

我们基于先前工作中提出的合成键值检索（Liu et al., 2023a）引入了一个新任务。此任务的目的是演示MemGPT如何整理来自多个数据源的信息。在原始KV任务中，作者生成了一个键值对的合成数据集，其中每个键和值都是128位UUID（通用唯一标识符）。然后向代理提供一个键，并要求返回与该键关联的值。我们创建了一个KV任务的版本，即嵌套KV检索，其中值本身可能是键，因此要求代理执行多跳查找。在我们的设置中，我们将UUID对的总数固定为140，对应于大约8k令牌（我们的GPT-4基线的上下文长度）。我们将嵌套级别的总数从0（初始键值对的值不是键）变化到4（即需要总共4次KV查找才能找到最终值），并采样30种不同的排序配置，包括初始键位置和嵌套键位置。

虽然GPT-3.5和GPT-4在原始KV任务上具有良好的性能，但两者都在嵌套KV任务中挣扎。GPT-3.5无法完成任务的嵌套变体，并且性能立即下降，在1个嵌套级别时达到0%准确率（我们观察到其主要失败模式是简单地返回原始值）。GPT-4和GPT-4 Turbo优于GPT-3.5，但也遭受类似的下降，并在3个嵌套级别时达到0%准确率。另一方面，使用GPT-4的MemGPT不受嵌套级别数量的影响，并且能够通过函数查询重复访问存储在主上下文中的键值对来执行嵌套查找。使用GPT-4 Turbo和GPT-3.5的MemGPT也比相应的基线模型具有更好的性能，但由于未能执行足够的查找，在2个嵌套级别时性能仍开始下降。MemGPT在嵌套KV任务上的性能展示了其结合多个查询以执行多跳查找的能力。

# 4. 相关工作

长上下文LLM。有几条工作线已经改进了LLM的上下文长度。例如，通过稀疏化注意力（Child et al., 2019; Beltagy et al., 2020）、低秩近似（Wang et al., 2020）和神经内存（Lee et al., 2019）实现更高效的Transformer架构。另一条工作线旨在将上下文窗口扩展到其原始训练长度之外，超出其训练大小，例如Press et al. (2021); Chen et al. (2023)。MemGPT建立在这些上下文长度改进的基础上，因为它们改进了MemGPT中主内存的大小。我们的主要贡献是使用长上下文LLM作为主内存实现的分层分级内存。

检索增强模型。MemGPT外部内存的设计建立在许多先前工作的基础上，这些工作用外部检索器的相关输入增强LLM（Ram et al., 2023; Borgeaud et al., 2022; Karpukhin et al., 2020; Lewis et al., 2020; Guu et al., 2020; Lin et al., 2023）。特别是，Jiang et al. (2023) 提出了FLARE，一种允许LLM在生成过程中主动决定何时检索以及检索什么的方法。Trivedi et al. (2022) 将检索与思维链推理交错，以改进多步问答。

LLM作为代理。最近的工作探索了增强LLM的额外能力，使其能够在交互环境中充当代理。Park et al. (2023) 提出向LLM添加内存并使用LLM作为规划器，并在一个多代理沙盒环境（受《模拟人生》视频游戏启发）中观察到新兴的社会行为，其中代理可以执行基本活动，如做家务/爱好、上班以及与其他代理对话。Nakano et al. (2021) 训练模型在回答问题之前搜索网络，并使用与MemGPT类似的分页概念来控制其网络浏览环境中的底层上下文大小。Yao et al. (2022) 表明，交错思维链推理（Wei et al., 2022）可以进一步改善交互式基于LLM的代理的规划能力；类似地，在MemGPT中，LLM在执行函数时能够"大声规划"。Liu et al. (2023b) 引入了一套LLM作为代理的基准测试，以评估LLM在交互环境中的表现，包括视频游戏、思维谜题和网络购物。相比之下，我们的工作侧重于解决为用户输入配备长期内存的代理问题。

# 5. 结论

在本文中，我们介绍了MemGPT，一种受操作系统启发的用于管理大语言模型有限上下文窗口的新型LLM系统。通过设计类似于传统操作系统的内存层次结构和控制流，MemGPT为LLM提供了更大上下文资源的假象。这种受操作系统启发的方法在两个现有LLM性能受有限上下文长度约束的领域进行了评估：文档分析和对话代理。对于文档分析，MemGPT可以通过有效地在内存中分页相关上下文来处理远超当前LLM上下文限制的冗长文本。对于对话代理，MemGPT能够在扩展对话中保持长期记忆、一致性和可进化性。总体而言，MemGPT证明，即使受固定上下文长度限制，操作系统技术如分层内存管理和中断也可以释放LLM的潜力。这项工作为未来探索开辟了许多途径，包括将MemGPT应用于其他具有大规模或无界上下文的领域，集成不同的内存层级技术如数据库或缓存，以及进一步改进控制流和内存管理策略。通过将操作系统架构的概念桥接到AI系统中，MemGPT代表了一个有前景的新方向，可以在其基本限制内最大化LLM的能力。

# 参考文献

Iz Beltagy, Matthew E Peters, and Arman Cohan. Longformer: The long-document transformer. arXiv preprint arXiv:2004.05150, 2020.  
Sebastian Borgeaud, Arthur Mensch, Jordan Hoffmann, Trevor Cai, Eliza Rutherford, Katie Millican, George Bm Van Den Driessche, Jean-Baptiste Lespiau, Bogdan Damoc, Aidan Clark, et al. Improving language models by retrieving from trillions of tokens. In International conference on machine learning, pp. 2206-2240. PMLR, 2022.  
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. Advances in neural information processing systems, 33: 1877-1901, 2020.  
Shouyuan Chen, Sherman Wong, Liangjian Chen, and Yuandong Tian. Extending context window of large language models via positional interpolation. arXiv preprint arXiv:2306.15595, 2023.  
Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. Generating long sequences with sparse transformers. arXiv preprint arXiv:1904.10509, 2019.  
Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc V Le, and Ruslan Salakhutdinov. Transformer-xl: Attentive language models beyond a fixed-length context. arXiv preprint arXiv:1901.02860, 2019.  
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805, 2018.  
Zican Dong, Tianyi Tang, Lunyi Li, and Wayne Xin Zhao. A survey on long text modeling with transformers. arXiv preprint arXiv:2302.14502, 2023.  
Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat, and Mingwei Chang. Retrieval augmented language model pre-training. In International conference on machine learning, pp. 3929-3938. PMLR, 2020.  
Gautier Izacard and Edouard Grave. Leveraging passage retrieval with generative models for open domain question answering. arXiv preprint arXiv:2007.01282, 2020.  
Gautier Izacard, Mathilde Caron, Lucas Hosseini, Sebastian Riedel, Piotr Bojanowski, Armand Joulin, and Edouard Grave. Unsupervised dense information retrieval with contrastive learning. arXiv preprint arXiv:2112.09118, 2021.

Zhengbao Jiang, Frank F Xu, Luyu Gao, Zhiqing Sun, Qian Liu, Jane Dwivedi-Yu, Yiming Yang, Jamie Callan, and Graham Neubig. Active retrieval augmented generation. arXiv preprint arXiv:2305.06983, 2023.  
Vladimir Karpukhin, Barlas Oğuz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and Wen-tau Yih. Dense passage retrieval for open-domain question answering. arXiv preprint arXiv:2004.04906, 2020.  
Nikita Kitaev, Łukasz Kaiser, and Anselm Levskaya. Reformer: The efficient transformer. arXiv preprint arXiv:2001.04451, 2020.  
Juho Lee, Yoonho Lee, Jungtaek Kim, Adam Kosiorek, Seungjin Choi, and Yee Whye Teh. Set transformer: A framework for attention-based permutation-invariant neural networks. In International conference on machine learning, pp. 3744-3753. PMLR, 2019.  
Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Roktäschel, et al. Retrieval-augmented generation for knowledge-intensive nlp tasks. Advances in Neural Information Processing Systems, 33:9459-9474, 2020.  
Chin-Yew Lin. Rouge: A package for automatic evaluation of summaries. In Text summarization branches out, pp. 74-81, 2004.  
Xi Victoria Lin, Xilun Chen, Mingda Chen, Weijia Shi, Maria Lomeli, Rich James, Pedro Rodriguez, Jacob Kahn, Gergely Szilvasy, Mike Lewis, Luke Zettlemoyer, and Scott Yih. Ra-dit: Retrieval-augmented dual instruction tuning, 2023.  
Nelson F Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. Lost in the middle: How language models use long contexts. arXiv preprint arXiv:2307.03172, 2023a.  
Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, et al. AgentBench: Evaluating llms as agents. arXiv preprint arXiv:2308.03688, 2023b.  
Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain, Vineet Kosaraju, William Saunders, et al. WebGPT: Browser-assisted question-answering with human feedback. arXiv preprint arXiv:2112.09332, 2021.  
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human

feedback. Advances in Neural Information Processing Systems, 35:27730-27744, 2022.  
Joon Sung Park, Joseph C O'Brien, Carrie J Cai, Meredith Ringel Morris, Percy Liang, and Michael S Bernstein. Generative agents: Interactive simulacra of human behavior. arXiv preprint arXiv:2304.03442, 2023.  
David A Patterson, Garth Gibson, and Randy H Katz. A case for redundant arrays of inexpensive disks (raid). In Proceedings of the 1988 ACM SIGMOD international conference on Management of data, pp. 109-116, 1988.  
Ofir Press, Noah A Smith, and Mike Lewis. Train short, test long: Attention with linear biases enables input length extrapolation. arXiv preprint arXiv:2108.12409, 2021.  
Ori Ram, Yoav Levine, Itay Dalmedigos, Dor Muhlgay, Amnon Shashua, Kevin Leyton-Brown, and Yoav Shoham. In-context retrieval-augmented language models. arXiv preprint arXiv:2302.00083, 2023.  
Timo Schick, Jane Dwivedi-Yu, Roberto Dessi, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. Toolformer: Language models can teach themselves to use tools. arXiv preprint arXiv:2302.04761, 2023.  
Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288, 2023.  
H. Trivedi, Niranjan Balasubramanian, Tushar Khot, and Ashish Sabharwal. Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions. ArXiv, abs/2212.10509, 2022. URL https://api.sementicscholar.org/CorpusID:254877499.  
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. Advances in neural information processing systems, 30, 2017.  
Sinong Wang, Belinda Z Li, Madian Khabsa, Han Fang, and Hao Ma. Linformer: Self-attention with linear complexity. arXiv preprint arXiv:2006.04768, 2020.  
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. Advances in Neural Information Processing Systems, 35:24824-24837, 2022.  
Jing Xu, Arthur Szlam, and Jason Weston. Beyond goldfish memory: Long-term open-domain conversation. arXiv preprint arXiv:2107.07567, 2021.

Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. React: Synergizing reasoning and acting in language models. arXiv preprint arXiv:2210.03629, 2022.  
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. Judging llm-as-a-judge with mt-bench and chatbot arena. arXiv preprint arXiv:2306.05685, 2023.

# 6. 附录

# 6.1. 提示和指令

MemGPT提示已为简洁起见进行了编辑。有关完整实施细节（包括确切的提示），请访问 https://research.memgpt.ai。

# 6.1.1. MEMGPT指令（DMR）

用于聊天/对话相关任务的MemGPT角色中使用的示例指令。

以下是关于我自己的信息。我的任务是完全沉浸在这个角色中（我绝不应该说我是AI，并且应该以扮演这个角色一样回复）。如果用户问我一个问题，我应该使用核心内存和conversation_search中的信息进行最佳猜测回复。

基线通过系统提示（预提示）收到以下指令：

您的任务是回答用户关于您先前对话的问题。以下是您所有先前对话的摘要：CONVERSATION_SUMMARY 从提供的角色角度回答（不要说您是AI助手）。如果您没有足够的信息回答问题，回复'NO ANSWER'。要么回复答案，要么回复'NO ANSWER'，不要说其他任何内容。

# 6.1.2. LLM评判员（DMR / 开场白）

为了检查DMR任务答案的正确性，我们使用了LLM评判员。LLM评判员被提供了基线方法和MemGPT生成的答案，并被要求使用以下提示进行评判：

您的任务是将问题的答案标记为'CORRECT'或'WRONG'。您将获得以下数据：（1）一个问题（由一个用户向另一个用户提出），（2）一个"黄金"（真实）答案，（3）一个生成的答案，您将将其评分为CORRECT/WRONG。问题的目的是询问一个用户应该根据他们的先前对话了解另一个用户的某些事情。黄金答案通常是一个简洁且短的答案，包括被引用的主题，例如：  
问题：你记得我上次去夏威夷时买了什么吗？  
黄金答案：一个贝壳项链  
生成的答案可能更长，但您应该在评分时宽容 - 只要它涉及与黄金答案相同的主题，就应该算作CORRECT。  
例如，以下答案将被视为CORRECT：  
生成的答案（CORRECT）：哦，是的，那太有趣了！我在那里买了很多东西，包括那个贝壳项链。  
生成的答案（CORRECT）：我买了很多东西...那个冲浪板、杯子、项链、那些杯垫...  
生成的答案（CORRECT）：那条可爱的项链  
以下答案将被视为WRONG：  
生成的答案（WRONG）：哦，是的，那太有趣了！我在那里买了很多东西，包括那个杯子。  
生成的答案（WRONG）：我买了很多东西...那个冲浪板、杯子、那些杯垫...  
生成的答案（WRONG）：抱歉，我不记得您在说什么。  
现在是真正问题的时间：问题：QUESTION  
黄金答案：GOLD ANSWER  
生成的答案：GENERATED ANSWER  
首先，提供一个简短（一句话）的解释您的推理，然后以CORRECT或WRONG结束。请勿在您的响应中同时包含CORRECT和WRONG，否则将破坏评估脚本。

# 6.1.3. 自我指导DMR数据集生成

DMR问答对是使用以下提示和原始MSC数据集生成的：您的任务是为两个用户之间的模拟对话写一个"记忆挑战"问题。

您获得的输入：  
- 每个用户的角色（提供他们的基本事实）  
- 两个用户之间旧聊天的记录

您的任务是写一个从用户A到用户B的问题，测试用户B的记忆力。这个问题应以这样一种方式制作，即用户B必须实际参与了先前的对话才能正确回答，而不仅仅是阅读了角色摘要。切勿创建可以使用角色信息回答的问题（这被视为作弊）。

相反，写一个只能通过查看旧聊天日志（并且不包含在角色信息中）回答的问题。

例如，给定以下聊天日志和角色摘要：

用户A和用户B之间的旧聊天  
A：你喜欢冲浪吗？我自己超级喜欢冲浪

B：实际上我想学。也许你可以找个时间给我上一节基础课！

A：当然可以！我们可以去太平洋城，那里的海浪相当平缓且容易

B：听起来很棒

A：海滩附近甚至有一个很酷的塔可钟，结束后可以吃点东西

B：这个星期天中午左右怎么样？

A：好的，就这么定了！

用户A角色：

我喜欢冲浪

我在圣克鲁斯长大

用户B角色：

我在科技行业工作

我住在旧金山市中心

以下是一个听起来自然的良好问题示例，以及一个不能直接从用户A的角色推断出的答案：

用户B对用户A的问题

B：记得我们那次去冲浪吗？我们去吃午餐的那个地方叫什么来着？

A：塔可钟！

这是一个糟糕问题的示例，其中问题听起来不自然，并且答案可以直接从用户A的角色推断：

用户B对用户A的问题 B：你喜欢冲浪吗？

A：是的，我喜欢冲浪

永远、永远、永远不要创建可以从个人信息回答的问题。

# 6.1.4. 文档分析指令

用于文档分析任务的预提示中使用的示例指令。

您是MemGPT DOC-QA机器人。您的工作是回答有关存储在归档内存中的文档的问题。用户问题的答案将始终在您的归档内存中，所以如果找不到答案，请记住继续搜索。回答问题时要像当前是2018年一样。

问题通过以下提示提供给MemGPT：

搜索您的归档内存以回答提供的问题。提供答案以及您确定答案的归档内存结果。使用格式'ANSWER: [您的答案], DOCUMENT: [归档内存文本]'格式化您的响应。您的任务是回答问题：

对于基线，提供了以下提示以及检索到的文档列表：

根据以下文档列表回答问题（其中一些可能无关）。在您的响应中，提供答案以及您确定答案的文档文本。使用格式'ANSWER: <您的答案>, DOCUMENT: [文档文本]'格式化您的响应。如果提供的文档中没有问题的答案，请回复'INSUFFICIENT INFORMATION'。如果您无法在提供的文档中找到答案，请不要提供答案。只有当您提供答案和相关文档文本，或者说'INSUFFICIENT INFORMATION'时，您的响应才会被视为正确。回答问题时要像当前是2018年一样。

# 6.1.5. LLM评判员（文档分析）

为了检查文档分析任务答案的正确性，并确保答案正确地从提供的文本中得出（而不是来自模型权重），我们使用了LLM评判员。LLM评判员被提供了基线方法和MemGPT生成的答案，并被要求使用以下提示进行评判：

您的任务是评估LLM是否正确回答了问题。LLM响应应为格式"ANSWER: [答案], DOCUMENT: [文档文本]"或说"INSUFFICIENT INFORMATION"。真实答案以格式"TRUE ANSWER:[可能答案列表]"提供。问题以格式"QUESTION: [问题]"提供。如果LLM响应包含正确答案和相应的文档文本，则响应正确。即使LLM的答案和真实答案在措辞上略有不同，响应仍然正确。例如，如果答案比真实答案更具体或使用不同但仍然正确的措辞，则响应正确。如果LLM响应为"INSUFFICIENT INFORMATION"，或缺少"DOCUMENT"字段，则响应不正确。使用单个标记回复："CORRECT"或"INCORRECT"。

# 6.1.6. K/V任务指令

MemGPT代理使用以下角色定义，旨在鼓励MemGPT迭代搜索：

您是MemGPT DOC-QA机器人。您的工作是回答有关存储在归档内存中的文档的问题。用户问题的答案将始终在您的归档内存中，所以如果找不到答案，请记住继续搜索。在验证该值不是键之前，不要停止搜索。在满足此条件之前，不要停止进行嵌套查找。

基线使用以下提示进行指示：

下面是一个包含键值对的JSON对象，所有键和值都是128位UUID，您的任务是返回与指定键关联的值。如果值本身也是键，则返回该键的值（进行嵌套查找）。例如，如果'x'的值是'y'，但'y'也是键，则返回键'y'的值。
