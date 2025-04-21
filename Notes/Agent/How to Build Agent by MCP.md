# 示例客户端
来源：https://modelcontextprotocol.io/clients

支持MCP集成的应用程序列表

本页面概述了支持模型上下文协议(MCP)的应用程序。每个客户端可能支持不同的MCP功能，允许与MCP服务器进行不同级别的集成。

## 功能支持矩阵

| 客户端                               | [资源] | [提示] | [工具] | [采样] | 根节点 | 备注                                                                                           |
| ------------------------------------ | ----------- | --------- | ------- | ---------- | ----- | ----------------------------------------------------------------------------------------------- |
| [5ire][5ire]                         | ❌           | ❌         | ✅       | ❌          | ❌     | 支持工具                                                                                 |
| [Apify MCP测试器][Apify MCP Tester] | ❌           | ❌         | ✅       | ❌          | ❌     | 支持工具                                                                                  |
| [BeeAI框架][BeeAI Framework]   | ❌           | ❌         | ✅       | ❌          | ❌     | 在智能体工作流中支持工具                                                            |
| [Claude代码][Claude Code]           | ❌           | ✅         | ✅       | ❌          | ❌     | 支持提示和工具                                                                      |
| [Claude桌面应用][Claude Desktop] | ✅           | ✅         | ✅       | ❌          | ❌     | 支持工具、提示和资源                                                         |
| [Cline][Cline]                       | ✅           | ❌         | ✅       | ❌          | ❌     | 支持工具和资源                                                                   |
| [Continue][Continue]                 | ✅           | ✅         | ✅       | ❌          | ❌     | 支持工具、提示和资源                                                         |
| [Copilot-MCP][CopilotMCP]            | ✅           | ❌         | ✅       | ❌          | ❌     | 支持工具和资源                                                                   |
| [Cursor][Cursor]                     | ❌           | ❌         | ✅       | ❌          | ❌     | 支持工具                                                                                 |
| [Daydreams智能体][Daydreams]        | ✅           | ✅         | ✅       | ❌          | ❌     | 支持将服务器直接集成到Daydreams智能体中                                                 |
| [Emacs Mcp][Mcp.el]                  | ❌           | ❌         | ✅       | ❌          | ❌     | 在Emacs中支持工具                                                                        |
| [fast-agent][fast-agent]             | ✅           | ✅         | ✅       | ✅          | ✅     | 完整的多模态MCP支持，包含端到端测试                                              |
| [Genkit][Genkit]                     | ⚠️          | ✅         | ✅       | ❌          | ❌     | 通过工具支持资源列表和查找                                                |
| [GenAIScript][GenAIScript]           | ❌           | ❌         | ✅       | ❌          | ❌     | 支持工具                                                                                 |
| [Goose][Goose]                       | ❌           | ❌         | ✅       | ❌          | ❌     | 支持工具                                                                                 |
| [LibreChat][LibreChat]               | ❌           | ❌         | ✅       | ❌          | ❌     | 为智能体支持工具                                                                       |
| [mcp-agent][mcp-agent]               | ❌           | ❌         | ✅       | ⚠️         | ❌     | 支持工具、服务器连接管理和智能体工作流                              |
| [Microsoft Copilot Studio]           | ❌           | ❌         | ✅       | ❌          | ❌     | 支持工具                                                                                  |
| [OpenSumi][OpenSumi]                 | ❌           | ❌         | ✅       | ❌          | ❌     | 在OpenSumi中支持工具                                                                      |
| [oterm][oterm]                       | ❌           | ✅         | ✅       | ✅          | ❌     | 为Ollama支持工具、提示和采样                                                |
| [Roo Code][Roo Code]                 | ✅           | ❌         | ✅       | ❌          | ❌     | 支持工具和资源                                                                   |
| [Sourcegraph Cody][Cody]             | ✅           | ❌         | ❌       | ❌          | ❌     | 通过OpenCTX支持资源                                                              |
| [SpinAI][SpinAI]                     | ❌           | ❌         | ✅       | ❌          | ❌     | 为Typescript AI智能体支持工具                                                         |
| [Superinterface][Superinterface]     | ❌           | ❌         | ✅       | ❌          | ❌     | 支持工具                                                                                  |
| [TheiaAI/TheiaIDE][TheiaAI/TheiaIDE] | ❌           | ❌         | ✅       | ❌          | ❌     | 在Theia AI和AI驱动的Theia IDE中为智能体支持工具                              |
| [VS Code GitHub Copilot][VS Code]    | ❌           | ❌         | ✅       | ❌          | ✅     | 支持动态工具/根节点发现、安全密钥配置和显式工具提示 | 
| [Windsurf编辑器][Windsurf]          | ❌           | ❌         | ✅       | ❌          | ❌     | 通过AI Flow支持协作开发的工具                                      |
| [Witsy][Witsy]                       | ❌           | ❌         | ✅       | ❌          | ❌     | 在Witsy中支持工具                                                                        |
| [Zed][Zed]                           | ❌           | ✅         | ❌       | ❌          | ❌     | 提示显示为斜杠命令                                                                |

[5ire]: https://github.com/nanbingxyz/5ire

[Apify MCP测试器]: https://apify.com/jiri.spilka/tester-mcp-client

[BeeAI框架]: https://i-am-bee.github.io/beeai-framework

[Claude代码]: https://claude.ai/code

[Claude桌面应用]: https://claude.ai/download

[Cline]: https://github.com/cline/cline

[Continue]: https://github.com/continuedev/continue

[CopilotMCP]: https://github.com/VikashLoomba/copilot-mcp

[Cursor]: https://cursor.com

[Daydreams]: https://github.com/daydreamsai/daydreams

[Mcp.el]: https://github.com/lizqwerscott/mcp.el

[fast-agent]: https://github.com/evalstate/fast-agent

[Genkit]: https://github.com/firebase/genkit

[GenAIScript]: https://microsoft.github.io/genaiscript/reference/scripts/mcp-tools/

[Goose]: https://block.github.io/goose/docs/goose-architecture/#interoperability-with-extensions

[LibreChat]: https://github.com/danny-avila/LibreChat

[mcp-agent]: https://github.com/lastmile-ai/mcp-agent

[Microsoft Copilot Studio]: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp

[OpenSumi]: https://github.com/opensumi/core

[oterm]: https://github.com/ggozad/oterm

[Roo Code]: https://roocode.com

[Cody]: https://sourcegraph.com/cody

[SpinAI]: https://spinai.dev

[Superinterface]: https://superinterface.ai

[TheiaAI/TheiaIDE]: https://eclipsesource.com/blogs/2024/12/19/theia-ide-and-theia-ai-support-mcp/

[VS Code]: https://code.visualstudio.com/

[Windsurf]: https://codeium.com/windsurf

[Witsy]: https://github.com/nbonamy/witsy

[Zed]: https://zed.dev

[资源]: https://modelcontextprotocol.io/docs/concepts/resources

[提示]: https://modelcontextprotocol.io/docs/concepts/prompts

[工具]: https://modelcontextprotocol.io/docs/concepts/tools

[采样]: https://modelcontextprotocol.io/docs/concepts/sampling

## 客户端详情

### 5ire

[5ire](https://github.com/nanbingxyz/5ire) 是一个开源的跨平台桌面AI助手，通过MCP服务器支持工具。

**主要功能：**

* 内置MCP服务器可以快速启用和禁用
* 用户可以通过修改配置文件添加更多服务器
* 开源且用户友好，适合初学者
* 未来将持续改进对MCP的支持

### Apify MCP测试器

[Apify MCP测试器](https://github.com/apify/tester-mcp-client) 是一个开源客户端，使用服务器发送事件(SSE)连接到任何MCP服务器。
它是一个独立的Apify Actor，设计用于通过SSE测试MCP服务器，支持授权头。
它使用纯JavaScript(传统风格)并托管在Apify上，无需任何设置即可运行。

**主要功能：**

* 通过SSE连接到任何MCP服务器
* 与[Apify MCP服务器](https://apify.com/apify/actors-mcp-server)配合使用，与一个或多个Apify [Actors](https://apify.com/store)交互
* 根据上下文和用户查询动态使用工具(如果服务器支持)

### BeeAI框架

[BeeAI框架](https://i-am-bee.github.io/beeai-framework) 是一个开源框架，用于大规模构建、部署和服务强大的智能体工作流。该框架包含**MCP工具**，这是一个原生功能，可简化MCP服务器与智能体工作流的集成。

**主要功能：**

* 将MCP工具无缝集成到智能体工作流中
* 从连接的MCP客户端快速实例化框架原生工具
* 计划未来支持智能体MCP功能

**了解更多：**

* [在智能体工作流中使用MCP工具的示例](https://i-am-bee.github.io/beeai-framework/#/typescript/tools?id=using-the-mcptool-class)

### Claude代码

Claude代码是Anthropic的交互式智能编码工具，通过自然语言命令帮助您更快地编写代码。它支持MCP集成提示和工具，同时也作为MCP服务器与其他客户端集成。

**主要功能：**

* 支持MCP服务器的工具和提示
* 通过MCP服务器提供自己的工具，与其他MCP客户端集成

### Claude桌面应用

Claude桌面应用程序全面支持MCP，实现与本地工具和数据源的深度集成。

**主要功能：**

* 完全支持资源，允许附加本地文件和数据
* 支持提示模板
* 工具集成用于执行命令和脚本
* 本地服务器连接增强隐私和安全性

> ⓘ 注意：Claude.ai网页应用目前不支持MCP。MCP功能仅在桌面应用中可用。

### Cline

[Cline](https://github.com/cline/cline) 是VS Code中的自主编码智能体，可以编辑文件、运行命令、使用浏览器等 - 在每一步都需要您的许可。

**主要功能：**

* 通过自然语言创建和添加工具(例如"添加一个可以搜索网络的工具")
* 通过`~/Documents/Cline/MCP`目录与他人分享Cline创建的自定义MCP服务器
* 显示配置的MCP服务器及其工具、资源和任何错误日志

### Continue

[Continue](https://github.com/continuedev/continue) 是一个开源的AI代码助手，内置支持所有MCP功能。

**主要功能**

* 输入"@"提及MCP资源
* 提示模板显示为斜杠命令
* 直接在聊天中使用内置和MCP工具
* 支持VS Code和JetBrains IDE，可与任何LLM配合使用

### Copilot-MCP

[Copilot-MCP](https://github.com/VikashLoomba/copilot-mcp) 通过MCP提供AI编码辅助。

**主要功能：**

* 支持MCP工具和资源
* 与开发工作流集成
* 可扩展的AI能力

### Cursor

[Cursor](https://docs.cursor.com/advanced/model-context-protocol) 是一款AI代码编辑器。

**主要功能：**

* 在Cursor Composer中支持MCP工具
* 支持STDIO和SSE两种协议

### Daydreams

[Daydreams](https://github.com/daydreamsai/daydreams) 是一个用于在链上执行任何操作的生成式智能体框架

**主要功能：**

* 在配置中支持MCP服务器
* 提供MCP客户端接口

### Emacs Mcp

[Emacs Mcp](https://github.com/lizqwerscott/mcp.el) 是一个Emacs客户端，设计用于与MCP服务器交互，实现无缝连接和操作。它为AI插件如[gptel](https://github.com/karthink/gptel)和[llm](https://github.com/ahyatt/llm)提供MCP工具调用支持，遵循Emacs的标准工具调用格式。这种集成增强了Emacs生态系统中AI工具的功能。

**主要功能：**

* 为Emacs提供MCP工具支持

### fast-agent

[fast-agent](https://github.com/evalstate/fast-agent) 是一个Python智能体框架，支持通过简单声明式方法创建智能体和工作流，全面支持Anthropic和OpenAI模型的多模态功能。

**主要功能：**

* 基于MCP原生类型支持PDF和图像处理
* 提供交互式前端用于开发和诊断智能体应用，包括直通和回放模拟器
* 内置支持"构建高效智能体"工作流
* 可将智能体部署为MCP服务器

### Genkit

[Genkit](https://github.com/firebase/genkit) 是一个跨语言SDK，用于构建GenAI功能并集成到应用中。[genkitx-mcp](https://github.com/firebase/genkit/tree/main/js/plugins/mcp)插件支持作为客户端使用MCP服务器或从Genkit工具和提示创建MCP服务器。

**主要功能：**

* 支持工具和提示的客户端功能(资源部分支持)
* 在Genkit开发UI中提供丰富的发现功能
* 与Genkit现有工具和提示无缝互操作
* 支持多种主流GenAI模型提供商

### GenAIScript

使用[GenAIScript](https://microsoft.github.io/genaiscript/)(JavaScript)以编程方式组装LLM提示。在JavaScript中编排LLM、工具和数据。

**主要功能：**

* 用于处理提示的JavaScript工具箱
* 提供抽象层以提高易用性和生产力
* 与Visual Studio Code无缝集成

### Goose

[Goose](https://github.com/block/goose) 是一个开源AI智能体，通过自动化编码任务来增强您的软件开发能力。

**主要功能：**

* 通过工具向Goose暴露MCP功能
* 可通过[扩展目录](https://block.github.io/goose/v1/extensions/)、CLI或UI直接安装MCP
* 允许通过[构建自己的MCP服务器](https://block.github.io/goose/docs/tutorials/custom-extensions)扩展功能
* 包含开发、网页抓取、自动化、内存以及与JetBrains和Google Drive集成的内置工具

### LibreChat

[LibreChat](https://github.com/danny-avila/LibreChat) 是一个开源、可定制的AI聊天UI，支持多个AI提供商，现在包括MCP集成。

**主要功能：**

* 通过MCP服务器扩展当前工具生态系统，包括[代码解释器](https://www.librechat.ai/docs/features/code_interpreter)和图像生成工具
* 使用来自顶级提供商的各种LLM，向可定制的[智能体](https://www.librechat.ai/docs/features/agents)添加工具
* 开源且可自托管，支持安全的多用户功能
* 未来路线图包括扩展MCP功能支持

### mcp-agent

[mcp-agent] 是一个简单、可组合的框架，用于使用模型上下文协议构建智能体。

**主要功能：**

* MCP服务器的自动连接管理
* 向LLM暴露来自多个服务器的工具
* 实现[构建高效智能体](https://www.anthropic.com/research/building-effective-agents)中定义的每种模式
* 支持工作流暂停/恢复信号，如等待人工反馈

### Microsoft Copilot Studio

[Microsoft Copilot Studio] 是一个强大的SaaS平台，用于构建自定义AI驱动应用和智能智能体，使开发人员能够创建、部署和管理复杂的AI解决方案。

**主要功能：**

* 支持MCP工具
* 使用MCP服务器扩展Copilot Studio智能体
* 利用微软统一、治理和安全的API管理解决方案

### OpenSumi

[OpenSumi](https://github.com/opensumi/core) 是一个帮助您快速构建AI原生IDE产品的框架。

**主要功能：**

* 在OpenSumi中支持MCP工具
* 支持内置IDE MCP服务器和自定义MCP服务器

### oterm

[oterm] 是Ollama的终端客户端，允许用户创建聊天/智能体。

**主要功能：**

* 支持多个完全可定制的聊天会话，Ollama与工具连接
* 支持MCP工具

### Roo Code

[Roo Code](https://roocode.com) 通过MCP提供AI编码辅助。

**主要功能：**

* 支持MCP工具和资源
* 与开发工作流集成
* 可扩展的AI能力

### Sourcegraph Cody

[Cody](https://openctx.org/docs/providers/modelcontextprotocol) 是Sourcegraph的AI编码助手，通过OpenCTX实现MCP。

**主要功能：**

* 支持MCP资源
* 与Sourcegraph的代码智能集成
* 使用OpenCTX作为抽象层
* 计划未来支持更多MCP功能

### SpinAI

[SpinAI](https://spinai.dev) 是一个用于构建可观察AI智能体的开源TypeScript框架。该框架提供原生MCP兼容性，允许智能体与MCP服务器和工具无缝集成。

**主要功能：**

* AI智能体内置MCP兼容性
* 开源TypeScript框架
* 可观察的智能体架构
* 原生支持MCP工具集成

### Superinterface

[Superinterface](https://superinterface.ai) 是一个AI基础设施和开发者平台，用于构建应用内AI助手，支持MCP、交互组件、客户端函数调用等功能。

**主要功能：**

* 在通过React组件或脚本标签嵌入的助手中使用MCP服务器的工具
* 支持SSE传输协议
* 支持任何AI提供商的任何AI模型(OpenAI、Anthropic、Ollama等)

### TheiaAI/TheiaIDE

[Theia AI](https://eclipsesource.com/blogs/2024/10/07/introducing-theia-ai/) 是一个用于构建AI增强工具和IDE的框架。[AI驱动的Theia IDE](https://eclipsesource.com/blogs/2024/10/08/introducting-ai-theia-ide/) 是一个基于Theia AI构建的开放灵活的开发环境。

**主要功能：**

* **工具集成**：Theia AI使AI智能体(包括Theia IDE中的智能体)能够使用MCP服务器进行无缝工具交互
* **可定制提示**：Theia IDE允许用户定义和调整提示，动态集成MCP服务器以实现定制工作流
* **自定义智能体**：Theia IDE支持创建利用MCP功能的自定义智能体，使用户能够即时设计专用工作流

Theia AI和Theia IDE的MCP集成为用户提供了灵活性，使其成为探索和适应MCP的强大平台。

**了解更多：**
* [Theia IDE和Theia AI MCP公告](https://eclipsesource.com/blogs/2024/12/19/theia-ide-and-theia-ai-support-mcp/)
* [下载AI驱动的Theia IDE](https://theia-ide.org/)

### VS Code GitHub Copilot

[VS Code](https://code.visualstudio.com/) 通过[智能体模式](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)将MCP与GitHub Copilot集成，允许在您的智能编码工作流中直接与MCP提供的工具交互。在Claude Desktop、工作区或用户设置中配置服务器，提供引导式MCP安装和安全处理输入变量中的密钥，避免硬编码密钥泄露。

**主要功能：**

* 支持stdio和服务器发送事件(SSE)传输
* 每个会话可选择适合该智能体会话的工具以获得最佳性能
* 通过重启命令和输出日志轻松调试服务器
* 工具调用支持可编辑输入和始终允许切换
* 与现有VS Code扩展系统集成，从扩展注册MCP服务器

### Windsurf编辑器

[Windsurf编辑器](https://codeium.com/windsurf) 是一个将AI辅助与开发者工作流结合的智能IDE。它创新的AI Flow系统在保持开发者控制的同时，支持协作式和独立的AI交互。

**主要功能：**

* 革命性的人机协作AI Flow范式
* 智能代码生成和理解
* 支持多模型的丰富开发工具

### Witsy

[Witsy](https://github.com/nbonamy/witsy) 是一个AI桌面助手，支持Anthropic模型和作为LLM工具的MCP服务器。

**主要功能：**

* 支持多个MCP服务器
* 工具集成用于执行命令和脚本
* 本地服务器连接增强隐私和安全性
* 可从Smithery.ai轻松安装
* 开源，支持macOS、Windows和Linux

### Zed

[Zed](https://zed.dev/docs/assistant/model-context-protocol) 是一个内置MCP支持的高性能代码编辑器，专注于提示模板和工具集成。

**主要功能：**

* 提示模板在编辑器中显示为斜杠命令
* 工具集成增强编码工作流
* 与编辑器功能和工作区上下文紧密集成
* 不支持MCP资源

## 为您的应用添加MCP支持

如果您已为应用添加MCP支持，我们鼓励您提交pull request将其加入此列表。MCP集成可为用户提供强大的上下文AI能力，并使您的应用成为不断增长的MCP生态系统的一部分。

添加MCP支持的好处：

* 让用户能够自带上下文和工具
* 加入不断增长的可互操作AI应用生态系统
* 为用户提供灵活的集成选项
* 支持本地优先的AI工作流

要开始在应用中实现MCP，请查看我们的[Python](https://github.com/modelcontextprotocol/python-sdk)或[TypeScript SDK文档](https://github.com/modelcontextprotocol/typescript-sdk)

## 更新和更正

此列表由社区维护。如果您发现任何不准确之处或想更新关于MCP支持的信息，请提交pull request或在[我们的文档仓库中创建issue](https://github.com/modelcontextprotocol/modelcontextprotocol/issues)。


# 贡献
来源：https://modelcontextprotocol.io/development/contributing

如何参与模型上下文协议开发

我们欢迎社区贡献！请查看我们的[贡献指南](https://github.com/modelcontextprotocol/.github/blob/main/CONTRIBUTING.md)了解如何提交更改的详细信息。

所有贡献者必须遵守我们的[行为准则](https://github.com/modelcontextprotocol/.github/blob/main/CODE_OF_CONDUCT.md)。

如有问题和讨论，请使用[GitHub Discussions](https://github.com/orgs/modelcontextprotocol/discussions)。


# 路线图
来源：https://modelcontextprotocol.io/development/roadmap

我们对模型上下文协议发展的计划

<Info>最后更新：**2025-03-27**</Info>

模型上下文协议正在快速发展。本页面概述了我们当前对**未来六个月**关键优先事项和发展方向的思考，但随着项目发展这些可能会发生重大变化。要查看最近的变更，请查看**[规范变更日志](/specification/2025-03-26/changelog/)**。

<Note>此处提出的想法并非承诺——我们可能会以不同于描述的方式解决这些挑战，或者有些可能根本不会实现。这也不是一个*详尽*的列表；我们可能会加入未在此提及的工作。</Note>

我们重视社区参与！每个部分都链接到相关讨论，您可以在其中了解更多信息并贡献您的想法。

要了解我们标准化过程的技术视图，请访问GitHub上的[标准跟踪](https://github.com/orgs/modelcontextprotocol/projects/2/views/2)，它跟踪提案如何进展到被纳入官方[MCP规范](https://spec.modelcontextprotocol.io)中。

## 验证

为了培育强大的开发者生态系统，我们计划投资于：

* **参考客户端实现**：用高质量的AI应用展示协议功能
* **合规性测试套件**：自动验证客户端、服务器和SDK是否正确实现了规范

这些工具将帮助开发者自信地实现MCP，同时确保整个生态系统行为一致。

## 注册表

为了让MCP发挥其全部潜力，我们需要简化的方式来分发和发现MCP服务器。

我们计划开发一个[MCP注册表](https://github.com/orgs/modelcontextprotocol/discussions/159)，实现集中式服务器发现和元数据。该注册表主要作为API层，第三方市场和服务发现服务可以在此基础上构建。

## 智能体

随着MCP越来越多地成为智能体工作流的一部分，我们正在探索[改进](https://github.com/modelcontextprotocol/specification/discussions/111)，例如：

* **[智能体图](https://github.com/modelcontextprotocol/specification/discussions/94)**：通过命名空间和图感知通信模式实现复杂的智能体拓扑
* **交互式工作流**：通过细粒度权限、标准化交互模式和[与最终用户直接通信的方式](https://github.com/modelcontextprotocol/specification/issues/97)改进人在环中的体验

## 多模态

在MCP中支持完整的AI能力，包括：

* **额外模态**：视频和其他媒体类型
* **[流式处理](https://github.com/modelcontextprotocol/specification/issues/117)**：多部分、分块消息和双向通信以实现交互式体验

## 治理

我们正在实施优先考虑以下方面的治理结构：

* **社区主导的开发**：培育协作生态系统，社区成员和AI开发者都可以参与MCP的演进，确保其服务于多样化的应用和用例
* **透明的标准化**：建立明确的规范贡献流程，同时探索通过行业机构进行正式标准化

## 参与进来

我们欢迎您为MCP的未来做出贡献！加入我们的[GitHub Discussions](https://github.com/orgs/modelcontextprotocol/discussions)分享想法、提供反馈或参与开发过程。


# 最新动态
来源：https://modelcontextprotocol.io/development/updates

MCP的最新更新和改进

<Update label="2025-04-10" description="Java SDK 0.9.0发布">
  * MCP Java SDK [0.9.0](https://github.com/modelcontextprotocol/java-sdk/releases/tag/v0.9.0)版本已发布。
  * 重构日志系统以使用交换机制
  * 自定义上下文路径
  * 服务器指令
  * 调用工具结果增强
</Update>

<Update label="2025-03-26" description="Kotlin SDK 0.4.0发布">
  * 修复问题并清理API
  * 添加二进制兼容性跟踪以避免破坏性变更
  * 降低JDK要求至JDK8
  * 添加Claude Desktop集成与示例
  * 完整变更日志请见：[https://github.com/modelcontextprotocol/kotlin-sdk/releases/tag/0.4.0](https://github.com/modelcontextprotocol/kotlin-sdk/releases/tag/0.4.0)
</Update>

<Update label="2025-03-26" description="Java SDK 0.8.1发布">
  * MCP Java SDK [0.8.1](https://github.com/modelcontextprotocol/java-sdk/releases/tag/v0.8.1)版本已发布，
    提供了重要的错误修复。
</Update>

<Update label="2025-03-24" description="C# SDK发布">
  * 我们很高兴地宣布由
    [Peder Holdgaard Pedersen](http://github.com/PederHP)和微软开发的MCP
    [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk/)现已可用。这加入了我们不断增长的
    支持语言列表。C# SDK也可作为
    [NuGet包](https://www.nuget.org/packages/ModelContextProtocol)使用
  * Python SDK 1.5.0发布，包含多项修复和改进。
</Update>

<Update label="2025-03-21" description="Java SDK 0.8.0发布">
  * MCP Java SDK [0.8.0](https://github.com/modelcontextprotocol/java-sdk/releases/tag/v0.8.0)版本已发布，
    提供了重要的会话管理改进和错误修复。
</Update>

<Update label="2025-03-10" description="Typescript SDK发布">
  * Typescript SDK 1.7.0发布，包含多项修复和改进。
</Update>

<Update label="2025-02-14" description="Java SDK发布">
  * 我们很高兴地宣布，由VMware Tanzu的Spring AI团队开发的Java SDK现在
    是MCP的官方[Java SDK](https://github.com/modelcontextprotocol/java-sdk)。
    这加入了我们现有的Kotlin SDK，成为我们不断增长的支持语言列表的一部分。
    Spring AI团队将作为模型上下文协议组织的重要组成部分维护该SDK。
    我们非常高兴欢迎他们加入MCP社区！
</Update>

<Update label="2025-01-27" description="Python SDK 1.2.1">
* MCP Python SDK [1.2.1](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.2.1)版本已发布，
    提供了重要的稳定性改进和错误修复。
</Update>

<Update label="2025-01-18" description="SDK和服务器改进">
  * 在[TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)中简化了类似express的API
  * 在[客户端页面](https://modelcontextprotocol.io/clients)新增了8个客户端
</Update>

<Update label="2025-01-03" description="SDK和服务器改进">
  * 在[Python SDK](https://github.com/modelcontextprotocol/python-sdk)中增加了FastMCP API
  * 在[服务器仓库](https://github.com/modelcontextprotocol/servers)中提供了Docker化的MCP服务器
</Update>

<Update label="2024-12-21" description="Kotlin SDK发布">
  * Jetbrains发布了MCP的Kotlin SDK！
  * 查看[此仓库](https://github.com/modelcontextprotocol/kotlin-sdk/tree/main/samples/kotlin-mcp-server)获取MCP Kotlin服务器示例
</Update>


# 核心架构
来源：https://modelcontextprotocol.io/docs/concepts/architecture

了解MCP如何连接客户端、服务器和LLM

模型上下文协议(MCP)建立在灵活、可扩展的架构上，实现LLM应用与集成之间的无缝通信。本文档涵盖核心架构组件和概念。

## 概述

MCP遵循客户端-服务器架构，其中：

* **主机**是发起连接的LLM应用(如Claude Desktop或IDE)
* **客户端**与服务器保持1:1连接，位于主机应用内部
* **服务器**向客户端提供上下文、工具和提示

```mermaid
flowchart LR
    subgraph "主机"
        client1[MCP客户端]
        client2[MCP客户端]
    end
    subgraph "服务器进程"
        server1[MCP服务器]
    end
    subgraph "服务器进程"
        server2[MCP服务器]
    end

    client1 <-->|传输层| server1
    client2 <-->|传输层| server2
```

## 核心组件

### 协议层

协议层处理消息帧、请求/响应链接和高级通信模式。

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    class Protocol<Request, Notification, Result> {
        // 处理传入请求
        setRequestHandler<T>(schema: T, handler: (request: T, extra: RequestHandlerExtra) => Promise<Result>): void

        // 处理传入通知
        setNotificationHandler<T>(schema: T, handler: (notification: T) => Promise<void>): void

        // 发送请求并等待响应
        request<T>(request: Request, schema: T, options?: RequestOptions): Promise<T>

        // 发送单向通知
        notification(notification: Notification): Promise<void>
    }
    ```
  </Tab>

  <Tab title="Python">
    ```python
    class Session(BaseSession[RequestT, NotificationT, ResultT]):
        async def send_request(
            self,
            request: RequestT,
            result_type: type[Result]
        ) -> Result:
            """发送请求并等待响应。如果响应包含错误则抛出McpError"""
            # 请求处理实现

        async def send_notification(
            self,
            notification: NotificationT
        ) -> None:
            """发送不期待响应的单向通知"""
            # 通知处理实现

        async def _received_request(
            self,
            responder: RequestResponder[ReceiveRequestT, ResultT]
        ) -> None:
            """处理来自另一端的传入请求"""
            # 请求处理实现

        async def _received_notification(
            self,
            notification: ReceiveNotificationT
        ) -> None:
            """处理来自另一端的传入通知"""
            # 通知处理实现
    ```
  </Tab>
</Tabs>

关键类包括：

* `Protocol`
* `Client`
* `Server`

### 传输层

传输层处理客户端和服务器之间的实际通信。MCP支持多种传输机制：

1. **Stdio传输**
   * 使用标准输入/输出进行通信
   * 适合本地进程

2. **HTTP with SSE传输**
   * 使用服务器发送事件(SSE)进行服务器到客户端的消息
   * 使用HTTP POST进行客户端到服务器的消息

所有传输都使用[JSON-RPC](https://www.jsonrpc.org/) 2.0交换消息。有关模型上下文协议消息格式的详细信息，请参阅[规范](/specification/)。

### 消息类型

MCP有以下主要消息类型：

1. **请求**期待来自另一方的响应：
   ```typescript
   interface Request {
     method: string;
     params?: { ... };
   }
   ```

2. **结果**是对请求的成功响应：
   ```typescript
   interface Result {
     [key: string]: unknown;
   }
   ```

3. **错误**表示请求失败：
   ```typescript
   interface Error {
     code: number;
     message: string;
     data?: unknown;
   }
   ```

4. **通知**是不期待响应的单向消息：
   ```typescript
   interface Notification {
     method: string;
     params?: { ... };
   }
   ```

## 连接生命周期

### 1. 初始化

```mermaid
sequenceDiagram
    participant Client
    participant Server

    Client->>Server: 初始化请求
    Server->>Client: 初始化响应
    Client->>Server: 初始化完成通知

    Note over Client,Server: 连接准备就绪
```

1. 客户端发送带有协议版本和能力的`initialize`请求
2. 服务器响应其协议版本和能力
3. 客户端发送`initialized`通知作为确认
4. 正常消息交换开始

### 2. 消息交换

初始化后支持以下模式：

* **请求-响应**：客户端或服务器发送请求，另一方响应
* **通知**：任一方发送单向消息

### 3. 终止

任一方都可以终止连接：

* 通过`close()`进行干净关闭
* 传输断开
* 错误情况

## 错误处理

MCP定义了这些标准错误代码：

```typescript
enum ErrorCode {
  // 标准JSON-RPC错误代码
  ParseError = -32700,
  InvalidRequest = -32600,
  MethodNotFound = -32601,
  InvalidParams = -32602,
  InternalError = -32603
}
```

SDK和应用可以在-32000以上定义自己的错误代码。

错误通过以下方式传播：

* 对请求的错误响应
* 传输上的错误事件
* 协议级错误处理程序

## 实现示例

以下是实现MCP服务器的基本示例：

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    import { Server } from "@modelcontextprotocol/sdk/server/index.js";
    import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

    const server = new Server({
      name: "example-server",
      version: "1.0.0"
    }, {
      capabilities: {
        resources: {}
      }
    });

    // 处理请求
    server.setRequestHandler(ListResourcesRequestSchema, async () => {
      return {
        resources: [
          {
            uri: "example://resource",
            name: "示例资源"
          }
        ]
      };
    });

    // 连接传输
    const transport = new StdioServerTransport();
    await server.connect(transport);
    ```
  </Tab>

  <Tab title="Python">
    ```python
    import asyncio
    import mcp.types as types
    from mcp.server import Server
    from mcp.server.stdio import stdio_server

    app = Server("example-server")

    @app.list_resources()
    async def list_resources() -> list[types.Resource]:
        return [
            types.Resource(
                uri="example://resource",
                name="示例资源"
            )
        ]

    async def main():
        async with stdio_server() as streams:
            await app.run(
                streams[0],
                streams[1],
                app.create_initialization_options()
            )

    if __name__ == "__main__":
        asyncio.run(main())
    ```
  </Tab>
</Tabs>

## 最佳实践

### 传输选择

1. **本地通信**
   * 对本地进程使用stdio传输
   * 对同机通信高效
   * 简单的进程管理

2. **远程通信**
   * 需要HTTP兼容性的场景使用SSE
   * 考虑安全影响包括认证和授权

### 消息处理

1. **请求处理**
   * 彻底验证输入
   * 使用类型安全模式
   * 优雅处理错误
   * 实现超时

2. **进度报告**
   * 对长时间操作使用进度令牌
   * 增量报告进度
   * 已知时包含总进度

3. **错误管理**
   * 使用适当的错误代码
   * 包含有用的错误消息
   * 出错时清理资源

## 安全考虑

1. **传输安全**
   * 对远程连接使用TLS
   * 验证连接来源
   * 需要时实现认证

2. **消息验证**
   * 验证所有传入消息
   * 清理输入
   * 检查消息大小限制
   * 验证JSON-RPC格式

3. **资源保护**
   * 实现访问控制
   * 验证资源路径
   * 监控资源使用
   * 限速请求

4. **错误处理**
   * 不要泄露敏感信息
   * 记录安全相关错误
   * 实现适当的清理
   * 处理DoS场景

## 调试和监控

1. **日志记录**
   * 记录协议事件
   * 跟踪消息流
   * 监控性能
   * 记录错误

2. **诊断**
   * 实现健康检查
   * 监控连接状态
   * 跟踪资源使用
   * 性能分析

3. **测试**
   * 测试不同传输
   * 验证错误处理
   * 检查边界情况
   * 负载测试服务器


# 提示
来源：https://modelcontextprotocol.io/docs/concepts/prompts

创建可重用的提示模板和工作流

提示(prompt)使服务器能够定义可重用的提示模板和工作流，客户端可以轻松将其展示给用户和LLM。它们提供了一种标准化和共享常见LLM交互的强大方式。

<Note>
  提示设计为**用户控制**，意味着它们从服务器暴露给客户端时，目的是让用户能够明确选择使用它们。
</Note>

## 概述

MCP中的提示是预定义的模板，可以：

* 接受动态参数
* 包含来自资源的上下文
* 链接多个交互
* 引导特定工作流
* 作为UI元素展示(如斜杠命令)

## 提示结构

每个提示定义为：

```typescript
{
  name: string;              // 提示的唯一标识符
  description?: string;      // 人类可读的描述
  arguments?: [              // 可选的参数列表
    {
      name: string;          // 参数标识符
      description?: string;  // 参数描述
      required?: boolean;    // 参数是否必需
    }
  ]
}
```

## 发现提示

客户端可以通过`prompts/list`端点发现可用提示：

```typescript
// 请求
{
  method: "prompts/list"
}

// 响应
{
  prompts: [
    {
      name: "analyze-code",
      description: "分析代码寻找改进点",
      arguments: [
        {
          name: "language",
          description: "编程语言",
          required: true
        }
      ]
    }
  ]
}
```

## 使用提示

要使用提示，客户端发出`prompts/get`请求：

```typescript
// 请求
{
  method: "prompts/get",
  params: {
    name: "analyze-code",
    arguments: {
      language: "python"
    }
  }
}

// 响应
{
  description: "分析Python代码寻找改进点",
  messages: [
    {
      role: "user",
      content: {
        type: "text",
        text: "请分析以下Python代码寻找改进点：\n\n```python\ndef calculate_sum(numbers):\n    total = 0\n    for num in numbers:\n        total = total + num\n    return total\n\nresult = calculate_sum([1, 2, 3, 4, 5])\nprint(result)\n```"
      }
    }
  ]
}
```

## 动态提示

提示可以是动态的，并包含：

### 嵌入资源上下文

```json
{
  "name": "analyze-project",
  "description": "分析项目日志和代码",
  "arguments": [
    {
      "name": "timeframe",
      "description": "分析日志的时间范围",
      "required": true
    },
    {
      "name": "fileUri",
      "description": "要审查的代码文件URI",
      "required": true
    }
  ]
}
```

处理`prompts/get`请求时：

```json
{
  "messages": [
    {
      "role": "user",
      "content": {
        "type": "text",
        "text": "分析这些系统日志和代码文件中的问题："
      }
    },
    {
      "role": "user",
      "content": {
        "type": "resource",
        "resource": {
          "uri": "logs://recent?timeframe=1h",
          "text": "[2024-03-14 15:32:11] ERROR: Connection timeout in network.py:127\n[2024-03-14 15:32:15] WARN: Retrying connection (attempt 2/3)\n[2024-03-14 15:32:20] ERROR: Max retries exceeded",
          "mimeType": "text/plain"
        }
      }
    },
    {
      "role": "user",
      "content": {
        "type": "resource",
        "resource": {
          "uri": "file:///path/to/code.py",
          "text": "def connect_to_service(timeout=30):\n    retries = 3\n    for attempt in range(retries):\n        try:\n            return establish_connection(timeout)\n        except TimeoutError:\n            if attempt == retries - 1:\n                raise\n            time.sleep(5)\n\ndef establish_connection(timeout):\n    # 连接实现\n    pass",
          "mimeType": "text/x-python"
        }
      }
    }
  ]
}
```

### 多步骤工作流

```typescript
const debugWorkflow = {
  name: "debug-error",
  async getMessages(error: string) {
    return [
      {
        role: "user",
        content: {
          type: "text",
          text: `我看到的错误是：${error}`
        }
      },
      {
        role: "assistant",
        content: {
          type: "text",
          text: "我会帮助分析这个错误。您已经尝试过什么方法了？"
        }
      },
      {
        role: "user",
        content: {
          type: "text",
          text: "我尝试过重启服务，但错误仍然存在。"
        }
      }
}
    ];
  }
};
```

## 示例实现

以下是MCP服务器中实现提示的完整示例：

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    import { Server } from "@modelcontextprotocol/sdk/server";
    import {
      ListPromptsRequestSchema,
      GetPromptRequestSchema
    } from "@modelcontextprotocol/sdk/types";

    const PROMPTS = {
      "git-commit": {
        name: "git-commit",
        description: "生成Git提交信息",
        arguments: [
          {
            name: "changes",
            description: "Git差异或变更描述",
            required: true
          }
        ]
      },
      "explain-code": {
        name: "explain-code",
        description: "解释代码工作原理",
        arguments: [
          {
            name: "code",
            description: "要解释的代码",
            required: true
          },
          {
            name: "language",
            description: "编程语言",
            required: false
          }
        ]
      }
    };

    const server = new Server({
      name: "example-prompts-server",
      version: "1.0.0"
    }, {
      capabilities: {
        prompts: {}
      }
    });

    // 列出可用提示
    server.setRequestHandler(ListPromptsRequestSchema, async () => {
      return {
        prompts: Object.values(PROMPTS)
      };
    });

    // 获取特定提示
    server.setRequestHandler(GetPromptRequestSchema, async (request) => {
      const prompt = PROMPTS[request.params.name];
      if (!prompt) {
        throw new Error(`未找到提示: ${request.params.name}`);
      }

      if (request.params.name === "git-commit") {
        return {
          messages: [
            {
              role: "user",
              content: {
                type: "text",
                text: `为以下变更生成简洁但描述性的提交信息:\n\n${request.params.arguments?.changes}`
              }
            }
          ]
        };
      }

      if (request.params.name === "explain-code") {
        const language = request.params.arguments?.language || "未知";
        return {
          messages: [
            {
              role: "user",
              content: {
                type: "text",
                text: `解释这段${language}代码的工作原理:\n\n${request.params.arguments?.code}`
              }
            }
          ]
        };
      }

      throw new Error("未找到提示实现");
    });
    ```
  </Tab>

  <Tab title="Python">
    ```python
    from mcp.server import Server
    import mcp.types as types

    # 定义可用提示
    PROMPTS = {
        "git-commit": types.Prompt(
            name="git-commit",
            description="生成Git提交信息",
            arguments=[
                types.PromptArgument(
                    name="changes",
                    description="Git差异或变更描述",
                    required=True
                )
            ],
        ),
        "explain-code": types.Prompt(
            name="explain-code",
            description="解释代码工作原理",
            arguments=[
                types.PromptArgument(
                    name="code",
                    description="要解释的代码",
                    required=True
                ),
                types.PromptArgument(
                    name="language",
                    description="编程语言",
                    required=False
                )
            ],
        )
    }

    # 初始化服务器
    app = Server("example-prompts-server")

    @app.list_prompts()
    async def list_prompts() -> list[types.Prompt]:
        return list(PROMPTS.values())

    @app.get_prompt()
    async def get_prompt(
        name: str, arguments: dict[str, str] | None = None
    ) -> types.GetPromptResult:
        if name not in PROMPTS:
            raise ValueError(f"未找到提示: {name}")

        if name == "git-commit":
            changes = arguments.get("changes") if arguments else ""
            return types.GetPromptResult(
                messages=[
                    types.PromptMessage(
                        role="user",
                        content=types.TextContent(
                            type="text",
                            text=f"为以下变更生成简洁但描述性的提交信息:\n\n{changes}"
                        )
                    )
                ]
            )

        if name == "explain-code":
            code = arguments.get("code") if arguments else ""
            language = arguments.get("language", "未知") if arguments else "未知"
            return types.GetPromptResult(
                messages=[
                    types.PromptMessage(
                        role="user",
                        content=types.TextContent(
                            type="text",
                            text=f"解释这段{language}代码的工作原理:\n\n{code}"
                        )
                    )
                ]
            )

        raise ValueError("未找到提示实现")
    ```
  </Tab>
</Tabs>
</Tab>
</Tabs>

## 最佳实践

实现提示时：

1. 使用清晰、描述性的提示名称
2. 为提示和参数提供详细描述
3. 验证所有必需参数
4. 优雅处理缺失参数
5. 考虑提示模板的版本控制
6. 适当缓存动态内容
7. 实现错误处理
8. 记录预期的参数格式
9. 考虑提示的可组合性
10. 使用各种输入测试提示

## UI集成

提示可以在客户端UI中展示为：

* 斜杠命令
* 快速操作
* 上下文菜单项
* 命令面板条目
* 引导式工作流
* 交互式表单

## 更新和变更

服务器可以通知客户端关于提示的变更：

1. 服务器能力：`prompts.listChanged`
2. 通知：`notifications/prompts/list_changed`
3. 客户端重新获取提示列表

## 安全考虑

实现提示时：

* 验证所有参数
* 清理用户输入
* 考虑限速
* 实现访问控制
* 审计提示使用情况
* 适当处理敏感数据
* 验证生成的内容
* 实现超时
* 考虑提示注入风险
* 记录安全要求


# 资源
来源：https://modelcontextprotocol.io/docs/concepts/resources

将服务器数据暴露给LLM使用

资源是模型上下文协议(MCP)中的核心原语，允许服务器暴露可以被客户端读取并用作LLM交互上下文的数据和内容。

<Note>
  资源设计为**应用控制**，意味着客户端应用可以决定如何以及何时使用它们。
  不同的MCP客户端可能以不同方式处理资源。例如：

  * Claude Desktop当前要求用户在使用前明确选择资源
  * 其他客户端可能基于启发式自动选择资源
  * 某些实现甚至可能允许AI模型本身决定使用哪些资源

  服务器作者在实现资源支持时应准备好处理这些交互模式。为了自动向模型暴露数据，服务器作者应使用**模型控制**的原语，如[工具](./tools)。
</Note>

## 概述

资源代表MCP服务器希望提供给客户端的任何类型数据，包括：

* 文件内容
* 数据库记录
* API响应
* 实时系统数据
* 截图和图像
* 日志文件
* 等等

每个资源由唯一URI标识，可以包含文本或二进制数据。

## 资源URI

资源使用遵循以下格式的URI标识：

```
[protocol]://[host]/[path]
```

例如：

* `file:///home/user/documents/report.pdf`
* `postgres://database/customers/schema`
* `screen://localhost/display1`

协议和路径结构由MCP服务器实现定义。服务器可以定义自己的自定义URI方案。

## 资源类型

资源可以包含两种类型的内容：

### 文本资源

文本资源包含UTF-8编码的文本数据，适用于：

* 源代码
* 配置文件
* 日志文件
* JSON/XML数据
* 纯文本

### 二进制资源

二进制资源包含base64编码的原始二进制数据，适用于：

* 图像
* PDF
* 音频文件
* 视频文件
* 其他非文本格式

## 资源发现

客户端可以通过两种主要方法发现可用资源：

### 直接资源

服务器通过`resources/list`端点暴露具体资源列表。每个资源包括：

```typescript
{
  uri: string;           // 资源的唯一标识符
  name: string;          // 人类可读名称
  description?: string;  // 可选描述
  mimeType?: string;     // 可选MIME类型
}
```

### 资源模板

对于动态资源，服务器可以暴露[URI模板](https://datatracker.ietf.org/doc/html/rfc6570)，客户端可用其构造有效资源URI：

```typescript
{
  uriTemplate: string;   // 遵循RFC 6570的URI模板
  name: string;          // 此类资源的人类可读名称
  description?: string;  // 可选描述
  mimeType?: string;     // 所有匹配资源的可选MIME类型
}
```

## 读取资源

要读取资源，客户端使用资源URI发起`resources/read`请求。

服务器响应包含资源内容列表：

```typescript
{
  contents: [
    {
      uri: string;        // 资源URI
      mimeType?: string;  // 可选MIME类型

      // 以下二选一：
      text?: string;      // 文本资源
      blob?: string;      // 二进制资源(base64编码)
    }
  ]
}
```

<Tip>
  服务器可能在一个`resources/read`请求响应中返回多个资源。例如，当读取目录时，可以返回目录中的文件列表。
</Tip>

## 资源更新

MCP通过两种机制支持资源的实时更新：

### 列表变更
服务器可以通过`notifications/resources/list_changed`通知客户端可用资源列表的变化。

### 内容变更

客户端可以订阅特定资源的更新：

1. 客户端发送`resources/subscribe`并附带资源URI
2. 当资源变更时，服务器发送`notifications/resources/updated`
3. 客户端可以使用`resources/read`获取最新内容
4. 客户端可以使用`resources/unsubscribe`取消订阅

## 示例实现

以下是MCP服务器中实现资源支持的简单示例：

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    const server = new Server({
      name: "example-server",
      version: "1.0.0"
    }, {
      capabilities: {
        resources: {}
      }
    });

    // 列出可用资源
    server.setRequestHandler(ListResourcesRequestSchema, async () => {
      return {
        resources: [
          {
            uri: "file:///logs/app.log",
            name: "应用日志",
            mimeType: "text/plain"
          }
        ]
      };
    });

    // 读取资源内容
    server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
      const uri = request.params.uri;

      if (uri === "file:///logs/app.log") {
        const logContents = await readLogFile();
        return {
          contents: [
            {
              uri,
              mimeType: "text/plain",
              text: logContents
            }
          ]
        };
      }

      throw new Error("未找到资源");
    });
    ```
  </Tab>

  <Tab title="Python">
    ```python
    app = Server("example-server")

    @app.list_resources()
    async def list_resources() -> list[types.Resource]:
        return [
            types.Resource(
                uri="file:///logs/app.log",
                name="应用日志",
                mimeType="text/plain"
            )
        ]

    @app.read_resource()
    async def read_resource(uri: AnyUrl) -> str:
        if str(uri) == "file:///logs/app.log":
            log_contents = await read_log_file()
            return log_contents

        raise ValueError("未找到资源")

    # 启动服务器
    async with stdio_server() as streams:
        await app.run(
            streams[0],
            streams[1],
            app.create_initialization_options()
        )
    ```
  </Tab>
</Tabs>

## 最佳实践

实现资源支持时：

1. 使用清晰、描述性的资源名称和URI
2. 包含有用的描述以指导LLM理解
3. 已知时设置适当的MIME类型
4. 为动态内容实现资源模板
5. 对频繁变更的资源使用订阅
6. 使用清晰的错误消息优雅处理错误
7. 对大型资源列表考虑分页
8. 适当缓存资源内容
9. 处理前验证URI
10. 记录自定义URI方案

## 安全考虑

暴露资源时：

* 验证所有资源URI
* 实现适当的访问控制
* 清理文件路径防止目录遍历
* 谨慎处理二进制数据
* 考虑对资源读取进行限速
* 审计资源访问
* 传输中加密敏感数据
* 验证MIME类型
* 对长时间运行的读取实现超时
* 适当处理资源清理


# 根目录
来源：https://modelcontextprotocol.io/docs/concepts/roots

理解MCP中的根目录

根目录是MCP中的一个概念，定义了服务器可以操作的边界。它们提供了一种方式让客户端告知服务器相关资源及其位置。

## 什么是根目录？

根目录是客户端建议服务器应关注的URI。当客户端连接到服务器时，它会声明服务器应使用的根目录。虽然主要用于文件系统路径，但根目录可以是任何有效的URI，包括HTTP URL。

例如，根目录可以是：

```
file:///home/user/projects/myapp
https://api.example.com/v1
```

## 为什么使用根目录？

根目录有几个重要用途：

1. **指导**：告知服务器相关资源和位置
2. **清晰**：明确哪些资源属于工作区
3. **组织**：多个根目录允许同时处理不同资源

## 根目录如何工作

当客户端支持根目录时，它会：

1. 在连接期间声明`roots`能力
2. 向服务器提供建议的根目录列表
3. 根目录变更时通知服务器（如果支持）

虽然根目录是信息性的而非严格强制，但服务器应：

1. 尊重提供的根目录
2. 使用根目录URI定位和访问资源
3. 优先处理根目录边界内的操作

## 常见用例

根目录通常用于定义：

* 项目目录
* 仓库位置
* API端点
* 配置位置
* 资源边界

## 最佳实践

使用根目录时：

1. 仅建议必要的资源
2. 使用清晰、描述性的根目录名称
3. 监控根目录可访问性
4. 优雅处理根目录变更

## 示例
以下是典型MCP客户端如何暴露根目录的示例：

```json
{
  "roots": [
    {
      "uri": "file:///home/user/projects/frontend",
      "name": "前端仓库"
    },
    {
      "uri": "https://api.example.com/v1",
      "name": "API端点"
    }
  ]
}
```

这种配置建议服务器同时关注本地仓库和API端点，同时保持它们的逻辑分离。


# 采样
来源：https://modelcontextprotocol.io/docs/concepts/sampling

让您的服务器通过客户端请求LLM补全

采样是MCP的强大功能，允许服务器通过客户端请求LLM补全，在保持安全性和隐私性的同时实现复杂的代理行为。

<Info>
  Claude Desktop客户端目前不支持此MCP功能。
</Info>

## 采样工作原理

采样流程遵循以下步骤：

1. 服务器向客户端发送`sampling/createMessage`请求
2. 客户端审查并可修改请求
3. 客户端从LLM采样
4. 客户端审查补全结果
5. 客户端将结果返回给服务器

这种人机交互设计确保用户对LLM看到和生成的内容保持控制。

## 消息格式

采样请求使用标准化消息格式：

```typescript
{
  messages: [
    {
      role: "user" | "assistant",
      content: {
        type: "text" | "image",

        // 文本内容：
        text?: string,

        // 图像内容：
        data?: string,             // base64编码
        mimeType?: string
      }
    }
  ],
  modelPreferences?: {
    hints?: [{
      name?: string                // 建议的模型名称/系列
    }],
    costPriority?: number,         // 0-1，最小化成本的重要性
    speedPriority?: number,        // 0-1，低延迟的重要性
    intelligencePriority?: number  // 0-1，高级能力的重要性
  },
  systemPrompt?: string,
  includeContext?: "none" | "thisServer" | "allServers",
  temperature?: number,
  maxTokens: number,
  stopSequences?: string[],
  metadata?: Record<string, unknown>
}
```

## 请求参数

### 消息

`messages`数组包含发送给LLM的对话历史。每条消息包含：

* `role`："user"或"assistant"
* `content`：消息内容，可以是：
  * 带有`text`字段的文本内容
  * 带有`data`(base64)和`mimeType`字段的图像内容

### 模型偏好

`modelPreferences`对象允许服务器指定模型选择偏好：

* `hints`：模型名称建议数组，客户端可用于选择适当模型：
  * `name`：可匹配完整或部分模型名称的字符串(如"claude-3", "sonnet")
  * 客户端可将提示映射到不同提供商的等效模型
  * 多个提示按偏好顺序评估

* 优先级值(0-1标准化)：
  * `costPriority`：最小化成本的重要性
  * `speedPriority`：低延迟响应的重要性
  * `intelligencePriority`：高级模型能力的重要性

客户端根据这些偏好和可用模型做出最终模型选择。

### 系统提示

可选的`systemPrompt`字段允许服务器请求特定系统提示。客户端可以修改或忽略此提示。

### 上下文包含

`includeContext`参数指定要包含的MCP上下文：

* `"none"`：不包含额外上下文
* `"thisServer"`：包含请求服务器的上下文
* `"allServers"`：包含所有连接MCP服务器的上下文

客户端控制实际包含的上下文内容。

### 采样参数

使用以下参数微调LLM采样：

* `temperature`：控制随机性(0.0到1.0)
* `maxTokens`：生成的最大token数
* `stopSequences`：停止生成的序列数组
* `metadata`：额外的提供商特定参数

## 响应格式

客户端返回补全结果：

```typescript
{
  model: string,  // 使用的模型名称
  stopReason?: "endTurn" | "stopSequence" | "maxTokens" | string,
  role: "user" | "assistant",
  content: {
    type: "text" | "image",
    text?: string,
    data?: string,
    mimeType?: string
  }
}
```

## 示例请求

以下是向客户端请求采样的示例：

```json
{
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "当前目录中有哪些文件？"
        }
      }
    ],
    "systemPrompt": "你是一个有用的文件系统助手。",
    "includeContext": "thisServer",
    "maxTokens": 100
  }
}
```

## 最佳实践

实现采样时：

1. 始终提供清晰、结构良好的提示
2. 正确处理文本和图像内容
3. 设置合理的token限制
4. 通过`includeContext`包含相关上下文
5. 使用前验证响应
6. 优雅处理错误
7. 考虑对采样请求进行限速
8. 记录预期的采样行为
9. 使用各种模型参数进行测试
10. 监控采样成本
## 人工监督控制

采样设计考虑了人工监督：

### 对于提示

* 客户端应向用户显示建议的提示
* 用户应能修改或拒绝提示
* 系统提示可以被过滤或修改
* 上下文包含由客户端控制

### 对于补全

* 客户端应向用户显示补全结果
* 用户应能修改或拒绝补全
* 客户端可以过滤或修改补全
* 用户控制使用哪个模型

## 安全考虑

实现采样时：

* 验证所有消息内容
* 清理敏感信息
* 实施适当的速率限制
* 监控采样使用情况
* 传输中加密数据
* 处理用户数据隐私
* 审计采样请求
* 控制成本暴露
* 实现超时
* 优雅处理模型错误

## 常见模式

### 代理工作流

采样支持以下代理模式：

* 读取和分析资源
* 基于上下文做出决策
* 生成结构化数据
* 处理多步骤任务
* 提供交互式帮助

### 上下文管理

上下文的最佳实践：

* 请求最小必要上下文
* 清晰组织上下文结构
* 处理上下文大小限制
* 根据需要更新上下文
* 清理过时上下文

### 错误处理

健壮的错误处理应：

* 捕获采样失败
* 处理超时错误
* 管理速率限制
* 验证响应
* 提供回退行为
* 适当记录错误

## 限制

注意以下限制：

* 采样依赖客户端能力
* 用户控制采样行为
* 上下文大小有限制
* 可能应用速率限制
* 应考虑成本
* 模型可用性不同
* 响应时间不同
* 并非所有内容类型都受支持


# 工具
来源：https://modelcontextprotocol.io/docs/concepts/tools

让LLM通过您的服务器执行操作

工具是模型上下文协议(MCP)中的强大原语，允许服务器向客户端暴露可执行功能。通过工具，LLM可以与外部系统交互、执行计算并在现实世界中采取行动。

<Note>
  工具设计为**模型控制**，意味着工具从服务器暴露给客户端，目的是让AI模型能够自动调用它们(需要人工监督批准)。
</Note>

## 概述

MCP中的工具允许服务器暴露可执行函数，客户端可以调用这些函数，LLM可以使用它们执行操作。工具的关键方面包括：

* **发现**：客户端可以通过`tools/list`端点列出可用工具
* **调用**：使用`tools/call`端点调用工具，服务器执行请求的操作并返回结果
* **灵活性**：工具范围从简单计算到复杂API交互

与[资源](/docs/concepts/resources)类似，工具由唯一名称标识，可以包含描述以指导其使用。但与资源不同，工具代表可以修改状态或与外部系统交互的动态操作。

## 工具定义结构

每个工具定义具有以下结构：

```typescript
{
  name: string;          // 工具的唯一标识符
  description?: string;  // 人类可读描述
  inputSchema: {         // 工具参数的JSON Schema
    type: "object",
    properties: { ... }  // 工具特定参数
  },
  annotations?: {        // 工具行为的可选提示
    title?: string;      // 工具的人类可读标题
    readOnlyHint?: boolean;    // 如果为true，工具不会修改其环境
    destructiveHint?: boolean; // 如果为true，工具可能执行破坏性更新
    idempotentHint?: boolean;  // 如果为true，相同参数的重复调用没有额外效果
    openWorldHint?: boolean;   // 如果为true，工具与外部实体交互
  }
}
```

## 实现工具

以下是MCP服务器中实现基本工具的示例：

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    const server = new Server({
      name: "example-server",
      version: "1.0.0"
    }, {
      capabilities: {
        tools: {}
      }
    });

    // 定义可用工具
    server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
        tools: [{
          name: "calculate_sum",
          description: "将两个数字相加",
          inputSchema: {
            type: "object",
            properties: {
              a: { type: "number" },
              b: { type: "number" }
            },
            required: ["a", "b"]
          }
        }]
      };
    });

    // 处理工具执行
    server.setRequestHandler(CallToolRequestSchema, async (request) => {
      if (request.params.name === "calculate_sum") {
        const { a, b } = request.params.arguments;
        return {
          content: [
            {
              type: "text",
              text: String(a + b)
            }
          ]
        };
      }
      throw new Error("未找到工具");
    });
    ```
  </Tab>

  <Tab title="Python">
    ```python
    app = Server("example-server")

    @app.list_tools()
    async def list_tools() -> list[types.Tool]:
        return [
            types.Tool(
                name="calculate_sum",
                description="将两个数字相加",
                inputSchema={
"type": "object",
                    "properties": {
                        "a": {"type": "number"},
                        "b": {"type": "number"}
                    },
                    "required": ["a", "b"]
                }
            )
        ]

    @app.call_tool()
    async def call_tool(
        name: str,
        arguments: dict
    ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
        if name == "calculate_sum":
            a = arguments["a"]
            b = arguments["b"]
            result = a + b
            return [types.TextContent(type="text", text=str(result))]
        raise ValueError(f"未找到工具: {name}")
    ```
  </Tab>
</Tabs>

## 工具模式示例

以下是服务器可以提供的一些工具类型示例：

### 系统操作

与本地系统交互的工具：

```typescript
{
  name: "execute_command",
  description: "运行shell命令",
  inputSchema: {
    type: "object",
    properties: {
      command: { type: "string" },
      args: { type: "array", items: { type: "string" } }
    }
  }
}
```

### API集成

封装外部API的工具：

```typescript
{
  name: "github_create_issue",
  description: "创建GitHub issue",
  inputSchema: {
    type: "object",
    properties: {
      title: { type: "string" },
      body: { type: "string" },
      labels: { type: "array", items: { type: "string" } }
    }
  }
}
```

### 数据处理

转换或分析数据的工具：

```typescript
{
  name: "analyze_csv",
  description: "分析CSV文件",
  inputSchema: {
    type: "object",
    properties: {
      filepath: { type: "string" },
      operations: {
        type: "array",
        items: {
          enum: ["sum", "average", "count"]
        }
      }
    }
  }
}
```

## 最佳实践

实现工具时：

1. 提供清晰、描述性的名称和描述
2. 使用详细的JSON Schema定义参数
3. 在工具描述中包含示例，展示模型应如何使用它们
4. 实现适当的错误处理和验证
5. 对长时间操作使用进度报告
6. 保持工具操作专注和原子性
7. 记录预期的返回值结构
8. 实现适当的超时
9. 对资源密集型操作考虑限速
10. 记录工具使用情况以便调试和监控

## 安全考虑

暴露工具时：

### 输入验证

* 根据schema验证所有参数
* 清理文件路径和系统命令
* 验证URL和外部标识符
* 检查参数大小和范围
* 防止命令注入

### 访问控制

* 需要时实现身份验证
* 使用适当的授权检查
* 审计工具使用情况
* 限速请求
* 监控滥用行为

### 错误处理

* 不要向客户端暴露内部错误
* 记录与安全相关的错误
* 适当处理超时
* 错误后清理资源
* 验证返回值

## 工具发现和更新

MCP支持动态工具发现：

1. 客户端可以随时列出可用工具
2. 服务器可以使用`notifications/tools/list_changed`通知客户端工具变更
3. 工具可以在运行时添加或移除
4. 工具定义可以更新(但应谨慎操作)

## 错误处理

工具错误应在结果对象中报告，而不是作为MCP协议级错误。这允许LLM查看并可能处理错误。当工具遇到错误时：

1. 在结果中将`isError`设置为`true`
2. 在`content`数组中包含错误详情

以下是工具正确错误处理的示例：

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    try {
      // 工具操作
      const result = performOperation();
      return {
        content: [
          {
            type: "text",
            text: `操作成功: ${result}`
          }
        ]
      };
    } catch (error) {
      return {
        isError: true,
        content: [
          {
            type: "text",
            text: `错误: ${error.message}`
          }
        ]
      };
    }
    ```
  </Tab>

  <Tab title="Python">
    ```python
    try:
        # 工具操作
        result = perform_operation()
        return types.CallToolResult(
            content=[
                types.TextContent(
                    type="text",
text=f"操作成功: {result}"
                )
            ]
        )
    except Exception as error:
        return types.CallToolResult(
            isError=True,
            content=[
                types.TextContent(
                    type="text",
                    text=f"错误: {str(error)}"
                )
            ]
        )
    ```
  </Tab>
</Tabs>

这种方法允许LLM看到发生了错误，并可能采取纠正措施或请求人工干预。

## 工具注解

工具注解提供关于工具行为的额外元数据，帮助客户端理解如何展示和管理工具。这些注解是描述工具性质和影响的提示，但不应用于安全决策。

### 工具注解的目的

工具注解有几个关键用途：

1. 提供UX特定信息而不影响模型上下文
2. 帮助客户端适当分类和展示工具
3. 传达工具潜在副作用的信息
4. 协助开发直观的工具批准界面

### 可用的工具注解

MCP规范定义了以下工具注解：

| 注解             | 类型    | 默认值  | 描述                                                                                                                          |
| ---------------- | ------- | ------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `title`          | string  | -       | 工具的人类可读标题，用于UI展示                                                                                               |
| `readOnlyHint`   | boolean | false   | 如果为true，表示工具不会修改其环境                                                                                           |
| `destructiveHint`| boolean | true    | 如果为true，工具可能执行破坏性更新(仅在`readOnlyHint`为false时有意义)                                                       |
| `idempotentHint` | boolean | false   | 如果为true，使用相同参数重复调用工具没有额外效果(仅在`readOnlyHint`为false时有意义)                                         |
| `openWorldHint`  | boolean | true    | 如果为true，工具可能与"开放世界"的外部实体交互                                                                               |

### 示例用法

以下是不同场景下定义带注解的工具：

```typescript
// 只读搜索工具
{
  name: "web_search",
  description: "在网络上搜索信息",
  inputSchema: {
    type: "object",
    properties: {
      query: { type: "string" }
    },
    required: ["query"]
  },
  annotations: {
    title: "网络搜索",
    readOnlyHint: true,
    openWorldHint: true
  }
}

// 破坏性文件删除工具
{
  name: "delete_file",
  description: "从文件系统中删除文件",
  inputSchema: {
    type: "object",
    properties: {
      path: { type: "string" }
    },
    required: ["path"]
  },
  annotations: {
    title: "删除文件",
    readOnlyHint: false,
    destructiveHint: true,
    idempotentHint: true,
    openWorldHint: false
  }
}

// 非破坏性数据库记录创建工具
{
  name: "create_record",
  description: "在数据库中创建新记录",
  inputSchema: {
    type: "object",
    properties: {
      table: { type: "string" },
      data: { type: "object" }
    },
    required: ["table", "data"]
  },
  annotations: {
    title: "创建数据库记录",
    readOnlyHint: false,
    destructiveHint: false,
    idempotentHint: false,
    openWorldHint: false
  }
}
```

### 在服务器实现中集成注解

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
        tools: [{
          name: "calculate_sum",
          description: "将两个数字相加",
          inputSchema: {
            type: "object",
            properties: {
              a: { type: "number" },
              b: { type: "number" }
            },
            required: ["a", "b"]
          },
          annotations: {
            title: "计算总和",
            readOnlyHint: true,
            openWorldHint: false
          }
        }]
      };
    });
    ```
  </Tab>

  <Tab title="Python">
    ```python
    from mcp.server.fastmcp import FastMCP

    mcp = FastMCP("example-server")

    @mcp.tool(
        annotations={
            "title": "计算总和",
            "readOnlyHint": True,
            "openWorldHint": False
        }
    )
    async def calculate_sum(a: float, b: float) -> str:
        """将两个数字相加。
        
        参数:
            a: 要相加的第一个数字
            b: 要相加的第二个数字
        """
        result = a + b
        return str(result)
    ```
  </Tab>
</Tabs>

### 工具注解的最佳实践

1. **准确描述副作用**：明确指出工具是否会修改其环境以及这些修改是否具有破坏性。

2. **使用描述性标题**：提供清晰描述工具用途的人类友好标题。

3. **正确指示幂等性**：仅当使用相同参数重复调用确实没有额外效果时，才将工具标记为幂等。

4. **设置适当的开放/封闭世界提示**：指出工具是与封闭系统(如数据库)还是开放系统(如网络)交互。

5. **记住注解只是提示**：ToolAnnotations中的所有属性都是提示，不能保证准确描述工具行为。客户端绝不应仅基于注解做出安全关键决策。

## 测试工具

MCP工具的全面测试策略应涵盖：

* **功能测试**：验证工具在有效输入下正确执行，并适当处理无效输入
* **集成测试**：使用真实和模拟依赖项测试工具与外部系统的交互
* **安全测试**：验证身份验证、授权、输入清理和速率限制
* **性能测试**：检查负载下的行为、超时处理和资源清理
* **错误处理**：确保工具通过MCP协议正确报告错误并清理资源
# 传输协议
来源：https://modelcontextprotocol.io/docs/concepts/transports

了解MCP的通信机制

模型上下文协议(MCP)中的传输协议提供了客户端和服务器之间通信的基础。传输协议处理消息发送和接收的底层机制。

## 消息格式

MCP使用[JSON-RPC](https://www.jsonrpc.org/) 2.0作为其有线格式。传输层负责将MCP协议消息转换为JSON-RPC格式进行传输，并将接收到的JSON-RPC消息转换回MCP协议消息。

使用三种类型的JSON-RPC消息：

### 请求

```typescript
{
  jsonrpc: "2.0",
  id: number | string,
  method: string,
  params?: object
}
```

### 响应

```typescript
{
  jsonrpc: "2.0",
  id: number | string,
  result?: object,
  error?: {
    code: number,
    message: string,
    data?: unknown
  }
}
```

### 通知

```typescript
{
  jsonrpc: "2.0",
  method: string,
  params?: object
}
```

## 内置传输类型

MCP包含两种标准传输实现：

### 标准输入/输出(stdio)

stdio传输通过标准输入和输出流实现通信。这对于本地集成和命令行工具特别有用。

在以下情况下使用stdio：

* 构建命令行工具
* 实现本地集成
* 需要简单的进程通信
* 使用shell脚本

<Tabs>
  <Tab title="TypeScript (服务器)">
    ```typescript
    const server = new Server({
      name: "example-server",
      version: "1.0.0"
    }, {
      capabilities: {}
    });

    const transport = new StdioServerTransport();
    await server.connect(transport);
    ```
  </Tab>

  <Tab title="TypeScript (客户端)">
    ```typescript
    const client = new Client({
      name: "example-client",
      version: "1.0.0"
    }, {
      capabilities: {}
    });

    const transport = new StdioClientTransport({
      command: "./server",
      args: ["--option", "value"]
    });
    await client.connect(transport);
    ```
  </Tab>

  <Tab title="Python (服务器)">
    ```python
    app = Server("example-server")

    async with stdio_server() as streams:
        await app.run(
            streams[0],
            streams[1],
            app.create_initialization_options()
        )
    ```
  </Tab>

  <Tab title="Python (客户端)">
    ```python
    params = StdioServerParameters(
        command="./server",
        args=["--option", "value"]
    )

    async with stdio_client(params) as streams:
        async with ClientSession(streams[0], streams[1]) as session:
            await session.initialize()
    ```
  </Tab>
</Tabs>

### 服务器发送事件(SSE)

SSE传输通过HTTP POST请求实现服务器到客户端的流式传输和客户端到服务器的通信。

在以下情况下使用SSE：

* 只需要服务器到客户端的流式传输
* 在受限网络中工作
* 实现简单更新

#### 安全警告：DNS重绑定攻击

如果没有适当保护，SSE传输可能容易受到DNS重绑定攻击。为防止这种情况：

1. **始终验证Origin头**以确保传入的SSE连接来自预期来源
2. **避免将服务器绑定到所有网络接口**(0.0.0.0) - 改为仅绑定到localhost(127.0.0.1)
3. **为所有SSE连接实现适当的身份验证**

没有这些保护措施，攻击者可能使用DNS重绑定从远程网站与本地MCP服务器交互。

<Tabs>
  <Tab title="TypeScript (服务器)">
    ```typescript
    import express from "express";

    const app = express();

    const server = new Server({
      name: "example-server",
      version: "1.0.0"
    }, {
      capabilities: {}
    });

    let transport: SSEServerTransport | null = null;

    app.get("/sse", (req, res) => {
      transport = new SSEServerTransport("/messages", res);
      server.connect(transport);
    });

    app.post("/messages", (req, res) => {
      if (transport) {
        transport.handlePostMessage(req, res);
      }
    });

    app.listen(3000);
    ```
  </Tab>

  <Tab title="TypeScript (客户端)">
    ```typescript
    const client = new Client({
      name: "example-client",
      version: "1.0.0"
    }, {
      capabilities: {}
    });

    const transport = new SSEClientTransport(
      new URL("http://localhost:3000/sse")
    );
await client.connect(transport);
    ```
  </Tab>

  <Tab title="Python (服务器)">
    ```python
    from mcp.server.sse import SseServerTransport
    from starlette.applications import Starlette
    from starlette.routing import Route

    app = Server("example-server")
    sse = SseServerTransport("/messages")

    async def handle_sse(scope, receive, send):
        async with sse.connect_sse(scope, receive, send) as streams:
            await app.run(streams[0], streams[1], app.create_initialization_options())

    async def handle_messages(scope, receive, send):
        await sse.handle_post_message(scope, receive, send)

    starlette_app = Starlette(
        routes=[
            Route("/sse", endpoint=handle_sse),
            Route("/messages", endpoint=handle_messages, methods=["POST"]),
        ]
    )
    ```
  </Tab>

  <Tab title="Python (客户端)">
    ```python
    async with sse_client("http://localhost:8000/sse") as streams:
        async with ClientSession(streams[0], streams[1]) as session:
            await session.initialize()
    ```
  </Tab>
</Tabs>

## 自定义传输协议

MCP可以轻松实现满足特定需求的自定义传输协议。任何传输实现只需要符合Transport接口：

您可以实现自定义传输协议用于：

* 自定义网络协议
* 专用通信通道
* 与现有系统集成
* 性能优化

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    interface Transport {
      // 开始处理消息
      start(): Promise<void>;

      // 发送JSON-RPC消息
      send(message: JSONRPCMessage): Promise<void>;

      // 关闭连接
      close(): Promise<void>;

      // 回调函数
      onclose?: () => void;
      onerror?: (error: Error) => void;
      onmessage?: (message: JSONRPCMessage) => void;
    }
    ```
  </Tab>

  <Tab title="Python">
    虽然MCP服务器通常使用asyncio实现，但我们建议使用`anyio`实现低级接口(如传输协议)以获得更广泛的兼容性。

    ```python
    @contextmanager
    async def create_transport(
        read_stream: MemoryObjectReceiveStream[JSONRPCMessage | Exception],
        write_stream: MemoryObjectSendStream[JSONRPCMessage]
    ):
        """
        MCP的传输接口。

        参数:
            read_stream: 读取传入消息的流
            write_stream: 写入传出消息的流
        """
        async with anyio.create_task_group() as tg:
            try:
                # 开始处理消息
                tg.start_soon(lambda: process_messages(read_stream))

                # 发送消息
                async with write_stream:
                    yield write_stream

            except Exception as exc:
                # 处理错误
                raise exc
            finally:
                # 清理资源
                tg.cancel_scope.cancel()
                await write_stream.aclose()
                await read_stream.aclose()
    ```
  </Tab>
</Tabs>

## 错误处理

传输实现应处理各种错误场景：

1. 连接错误
2. 消息解析错误
3. 协议错误
4. 网络超时
5. 资源清理

错误处理示例：

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    class ExampleTransport implements Transport {
      async start() {
        try {
          // 连接逻辑
        } catch (error) {
          this.onerror?.(new Error(`连接失败: ${error}`));
          throw error;
        }
      }

      async send(message: JSONRPCMessage) {
        try {
          // 发送逻辑
        } catch (error) {
          this.onerror?.(new Error(`发送消息失败: ${error}`));
          throw error;
        }
      }
    }
    ```
  </Tab>

  <Tab title="Python">
    虽然MCP服务器通常使用asyncio实现，但我们建议使用`anyio`实现低级接口(如传输协议)以获得更广泛的兼容性。

    ```python
    @contextmanager
    async def example_transport(scope: Scope, receive: Receive, send: Send):
        try:
            # 创建双向通信流
            read_stream_writer, read_stream = anyio.create_memory_object_stream(0)
            write_stream, write_stream_reader = anyio.create_memory_object_stream(0)

            async def message_handler():
                try:
                    async with read_stream_writer:
                        # 消息处理逻辑
                        pass
                except Exception as exc:
                    logger.error(f"处理消息失败: {exc}")
                    raise exc

            async with anyio.create_task_group() as tg:
                tg.start_soon(message_handler)
                try:
                    # 生成通信流
                    yield read_stream, write_stream
                except Exception as exc:
                    logger.error(f"传输错误: {exc}")
                    raise exc
                finally:
                    tg.cancel_scope.cancel()
                    await write_stream.aclose()
                    await read_stream.aclose()
        except Exception as exc:
            logger.error(f"初始化传输失败: {exc}")
            raise exc
    ```
  </Tab>
</Tabs>

## 最佳实践
实现或使用MCP传输协议时：

1. 正确处理连接生命周期
2. 实现适当的错误处理
3. 连接关闭时清理资源
4. 使用适当的超时设置
5. 发送前验证消息
6. 记录传输事件以便调试
7. 在适当时实现重连逻辑
8. 处理消息队列中的背压
9. 监控连接健康状况
10. 实施适当的安全措施

## 安全考虑

实现传输协议时：

### 认证和授权

* 实现适当的认证机制
* 验证客户端凭证
* 使用安全的令牌处理
* 实现授权检查

### 数据安全

* 使用TLS进行网络传输
* 加密敏感数据
* 验证消息完整性
* 实现消息大小限制
* 清理输入数据

### 网络安全

* 实现速率限制
* 使用适当的超时设置
* 处理拒绝服务场景
* 监控异常模式
* 实现适当的防火墙规则
* 对于SSE传输，验证Origin头以防止DNS重绑定攻击
* 对于本地SSE服务器，仅绑定到localhost(127.0.0.1)而不是所有接口(0.0.0.0)

## 调试传输协议

调试传输问题的技巧：

1. 启用调试日志
2. 监控消息流
3. 检查连接状态
4. 验证消息格式
5. 测试错误场景
6. 使用网络分析工具
7. 实现健康检查
8. 监控资源使用情况
9. 测试边缘情况
10. 使用适当的错误跟踪


# 调试
来源：https://modelcontextprotocol.io/docs/tools/debugging

调试模型上下文协议(MCP)集成的全面指南

开发MCP服务器或将其与应用程序集成时，有效的调试至关重要。本指南介绍了MCP生态系统中可用的调试工具和方法。

<Info>
  本指南适用于macOS。其他平台的指南即将推出。
</Info>

## 调试工具概述

MCP提供了几个不同级别的调试工具：

1. **MCP检查器**
   * 交互式调试界面
   * 直接服务器测试
   * 详情请参阅[检查器指南](/docs/tools/inspector)

2. **Claude桌面开发者工具**
   * 集成测试
   * 日志收集
   * Chrome开发者工具集成

3. **服务器日志**
   * 自定义日志实现
   * 错误跟踪
   * 性能监控

## 在Claude桌面中调试

### 检查服务器状态

Claude.app界面提供基本的服务器状态信息：

1. 点击<img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/claude-desktop-mcp-plug-icon.svg" style={{display: 'inline', margin: 0, height: '1.3em'}} />图标查看：
   * 已连接的服务器
   * 可用的提示和资源

2. 点击<img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/claude-desktop-mcp-hammer-icon.svg" style={{display: 'inline', margin: 0, height: '1.3em'}} />图标查看：
   * 提供给模型的工具

### 查看日志

从Claude桌面查看详细的MCP日志：

```bash
# 实时跟踪日志
tail -n 20 -F ~/Library/Logs/Claude/mcp*.log
```

日志记录包括：

* 服务器连接事件
* 配置问题
* 运行时错误
* 消息交换

### 使用Chrome开发者工具

在Claude桌面中访问Chrome的开发者工具来调查客户端错误：

1. 创建一个`developer_settings.json`文件，设置`allowDevTools`为true：

```bash
echo '{"allowDevTools": true}' > ~/Library/Application\ Support/Claude/developer_settings.json
```

2. 打开开发者工具：`Command-Option-Shift-i`

注意：您会看到两个开发者工具窗口：

* 主内容窗口
* 应用标题栏窗口

使用控制台面板检查客户端错误。

使用网络面板检查：

* 消息负载
* 连接时间

## 常见问题

### 工作目录

在Claude桌面中使用MCP服务器时：

* 通过`claude_desktop_config.json`启动的服务器的当前工作目录可能未定义(如macOS上的`/`)，因为Claude桌面可以从任何位置启动
* 始终在配置和`.env`文件中使用绝对路径以确保可靠运行
* 通过命令行直接测试服务器时，当前工作目录将是运行命令的位置

例如在`claude_desktop_config.json`中，使用：

```json
{
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/username/data"]
}
```

而不是相对路径如`./data`

### 环境变量

MCP服务器自动继承的环境变量只有子集，如`USER`、`HOME`和`PATH`。

要覆盖默认变量或提供自己的变量，可以在`claude_desktop_config.json`中指定`env`键：

```json
{
  "myserver": {
    "command": "mcp-server-myapp",
    "env": {
      "MYAPP_API_KEY": "some_key",
    }
  }
}
```

### 服务器初始化

常见的初始化问题：

1. **路径问题**
   * 服务器可执行文件路径不正确
   * 缺少必需文件
   * 权限问题
* 尝试为`command`使用绝对路径

2. **配置错误**
   * 无效的JSON语法
   * 缺少必填字段
   * 类型不匹配

3. **环境问题**
   * 缺少环境变量
   * 变量值不正确
   * 权限限制

### 连接问题

当服务器连接失败时：

1. 检查Claude桌面日志
2. 验证服务器进程是否正在运行
3. 使用[检查器](/docs/tools/inspector)进行独立测试
4. 验证协议兼容性

## 实现日志记录

### 服务器端日志记录

当构建使用本地stdio[传输协议](/docs/concepts/transports)的服务器时，所有记录到stderr(标准错误)的消息将自动被宿主应用程序(如Claude桌面)捕获。

<Warning>
  本地MCP服务器不应将消息记录到stdout(标准输出)，这会干扰协议操作。
</Warning>

对于所有[传输协议](/docs/concepts/transports)，您也可以通过发送日志消息通知向客户端提供日志记录：

<Tabs>
  <Tab title="Python">
    ```python
    server.request_context.session.send_log_message(
      level="info",
      data="服务器启动成功",
    )
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript
    server.sendLoggingMessage({
      level: "info",
      data: "服务器启动成功",
    });
    ```
  </Tab>
</Tabs>

需要记录的重要事件：

* 初始化步骤
* 资源访问
* 工具执行
* 错误情况
* 性能指标

### 客户端日志记录

在客户端应用中：

1. 启用调试日志
2. 监控网络流量
3. 跟踪消息交换
4. 记录错误状态

## 调试工作流程

### 开发周期

1. 初始开发
   * 使用[检查器](/docs/tools/inspector)进行基本测试
   * 实现核心功能
   * 添加日志点

2. 集成测试
   * 在Claude桌面中测试
   * 监控日志
   * 检查错误处理

### 测试变更

高效测试变更：

* **配置变更**：重启Claude桌面
* **服务器代码变更**：使用Command-R重新加载
* **快速迭代**：开发过程中使用[检查器](/docs/tools/inspector)

## 最佳实践

### 日志策略

1. **结构化日志记录**
   * 使用一致的格式
   * 包含上下文
   * 添加时间戳
   * 跟踪请求ID

2. **错误处理**
   * 记录堆栈跟踪
   * 包含错误上下文
   * 跟踪错误模式
   * 监控恢复情况

3. **性能跟踪**
   * 记录操作时间
   * 监控资源使用情况
   * 跟踪消息大小
   * 测量延迟

### 安全考虑

调试时：

1. **敏感数据**
   * 清理日志
   * 保护凭据
   * 屏蔽个人信息

2. **访问控制**
   * 验证权限
   * 检查认证
   * 监控访问模式

## 获取帮助

遇到问题时：

1. **第一步**
   * 检查服务器日志
   * 使用[检查器](/docs/tools/inspector)测试
   * 检查配置
   * 验证环境

2. **支持渠道**
   * GitHub issues
   * GitHub讨论区

3. **提供信息**
   * 日志摘录
   * 配置文件
   * 重现步骤
   * 环境详情

## 下一步

<CardGroup cols={2}>
  <Card title="MCP检查器" icon="magnifying-glass" href="/docs/tools/inspector">
    学习使用MCP检查器
  </Card>
</CardGroup>


# 检查器
来源：https://modelcontextprotocol.io/docs/tools/inspector

使用MCP检查器测试和调试模型上下文协议服务器的深入指南

[MCP检查器](https://github.com/modelcontextprotocol/inspector)是一个用于测试和调试MCP服务器的交互式开发者工具。虽然[调试指南](/docs/tools/debugging)将检查器作为整体调试工具包的一部分进行了介绍，但本文档详细探讨了检查器的特性和功能。

## 入门

### 安装和基本用法

检查器可以直接通过`npx`运行而无需安装：

```bash
npx @modelcontextprotocol/inspector <command>
```

```bash
npx @modelcontextprotocol/inspector <command> <arg1> <arg2>
```

#### 检查来自NPM或PyPi的服务器

从[NPM](https://npmjs.com)或[PyPi](https://pypi.com)启动服务器包的常见方式。

<Tabs>
  <Tab title="NPM包">
    ```bash
    npx -y @modelcontextprotocol/inspector npx <package-name> <args>
    # 例如
npx -y @modelcontextprotocol/inspector npx server-postgres postgres://127.0.0.1/testdb
    ```
  </Tab>

  <Tab title="PyPi包">
    ```bash
    npx @modelcontextprotocol/inspector uvx <package-name> <args>
    # 例如
    npx @modelcontextprotocol/inspector uvx mcp-server-git --repository ~/code/mcp/servers.git
    ```
  </Tab>
</Tabs>

#### 检查本地开发的服务器

要检查本地开发或下载为仓库的服务器，最常见的方式是：

<Tabs>
  <Tab title="TypeScript">
    ```bash
    npx @modelcontextprotocol/inspector node path/to/server/index.js args...
    ```
  </Tab>

  <Tab title="Python">
    ```bash
    npx @modelcontextprotocol/inspector \
      uv \
      --directory path/to/server \
      run \
      package-name \
      args...
    ```
  </Tab>
</Tabs>

请仔细阅读附带的README以获取最准确的说明。

## 功能概述

<Frame caption="MCP检查器界面">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/mcp-inspector.png" />
</Frame>

检查器提供了与MCP服务器交互的多种功能：

### 服务器连接面板

* 允许选择用于连接服务器的[传输协议](/docs/concepts/transports)
* 对于本地服务器，支持自定义命令行参数和环境

### 资源选项卡

* 列出所有可用资源
* 显示资源元数据(MIME类型、描述)
* 允许检查资源内容
* 支持订阅测试

### 提示选项卡

* 显示可用的提示模板
* 展示提示参数和描述
* 支持使用自定义参数测试提示
* 预览生成的消息

### 工具选项卡

* 列出可用工具
* 显示工具模式和描述
* 支持使用自定义输入测试工具
* 展示工具执行结果

### 通知面板

* 呈现服务器记录的所有日志
* 显示从服务器接收的通知

## 最佳实践

### 开发工作流程

1. 开始开发
   * 使用您的服务器启动检查器
   * 验证基本连接性
   * 检查能力协商

2. 迭代测试
   * 进行服务器更改
   * 重新构建服务器
   * 重新连接检查器
   * 测试受影响的功能
   * 监控消息

3. 测试边缘情况
   * 无效输入
   * 缺少提示参数
   * 并发操作
   * 验证错误处理和错误响应

## 下一步

<CardGroup cols={2}>
  <Card title="检查器仓库" icon="github" href="https://github.com/modelcontextprotocol/inspector">
    查看MCP检查器源代码
  </Card>

  <Card title="调试指南" icon="bug" href="/docs/tools/debugging">
    了解更广泛的调试策略
  </Card>
</CardGroup>


# 示例服务器
来源：https://modelcontextprotocol.io/examples

示例服务器和实现的列表

本页面展示了各种模型上下文协议(MCP)服务器，展示了该协议的功能和多功能性。这些服务器使大型语言模型(LLM)能够安全地访问工具和数据源。

## 参考实现

这些官方参考服务器展示了核心MCP功能和SDK用法：

### 数据和文件系统

* **[文件系统](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)** - 具有可配置访问控制的安全文件操作
* **[PostgreSQL](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres)** - 具有模式检查功能的只读数据库访问
* **[SQLite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite)** - 数据库交互和商业智能功能
* **[Google Drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive)** - Google Drive的文件访问和搜索功能

### 开发工具

* **[Git](https://github.com/modelcontextprotocol/servers/tree/main/src/git)** - 读取、搜索和操作Git仓库的工具
* **[GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/github)** - 仓库管理、文件操作和GitHub API集成
* **[GitLab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab)** - 实现项目管理的GitLab API集成
* **[Sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry)** - 从Sentry.io检索和分析问题

### Web和浏览器自动化

* **[Brave搜索](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search)** - 使用Brave的搜索API进行Web和本地搜索
* **[Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)** - 为LLM使用优化的Web内容获取和转换
* **[Puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer)** - 浏览器自动化和网页抓取功能

### 生产力和通信

* **[Slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack)** - 频道管理和消息功能
* **[Google地图](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps)** - 位置服务、路线和地点详情
* **[Memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)** - 基于知识图的持久记忆系统

### AI和专用工具

* **[EverArt](https://github.com/modelcontextprotocol/servers/tree/main/src/everart)** - 使用各种模型的AI图像生成
* **[Sequential Thinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)** - 通过思维序列进行动态问题解决
* **[AWS KB Retrieval](https://github.com/modelcontextprotocol/servers/tree/main/src/aws-kb-retrieval-server)** - 使用Bedrock Agent Runtime从AWS知识库检索

## 官方集成

这些MCP服务器由公司为其平台维护：

* **[Axiom](https://github.com/axiomhq/mcp-server-axiom)** - 使用自然语言查询和分析日志、跟踪和事件数据
* **[Browserbase](https://github.com/browserbase/mcp-server-browserbase)** - 在云端自动化浏览器交互
* **[Cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** - 在Cloudflare开发者平台上部署和管理资源
* **[E2B](https://github.com/e2b-dev/mcp-server)** - 在安全的云沙箱中执行代码
* **[Neon](https://github.com/neondatabase/mcp-server-neon)** - 与Neon无服务器Postgres平台交互
* **[Obsidian Markdown Notes](https://github.com/calclavia/mcp-obsidian)** - 在Obsidian库中读取和搜索Markdown笔记
* **[Qdrant](https://github.com/qdrant/mcp-server-qdrant/)** - 使用Qdrant向量搜索引擎实现语义记忆
* **[Raygun](https://github.com/MindscapeHQ/mcp-server-raygun)** - 访问崩溃报告和监控数据
* **[Search1API](https://github.com/fatwang2/search1api-mcp)** - 搜索、爬取和站点地图的统一API
* **[Stripe](https://github.com/stripe/agent-toolkit)** - 与Stripe API交互
* **[Tinybird](https://github.com/tinybirdco/mcp-tinybird)** - 与Tinybird无服务器ClickHouse平台接口
* **[Weaviate](https://github.com/weaviate/mcp-server-weaviate)** - 通过您的Weaviate集合实现代理RAG

## 社区亮点

不断增长的社区开发服务器生态系统扩展了MCP的功能：

* **[Docker](https://github.com/ckreiling/mcp-server-docker)** - 管理容器、镜像、卷和网络
* **[Kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** - 管理Pod、部署和服务
* **[Linear](https://github.com/jerhadf/linear-mcp-server)** - 项目管理和问题跟踪
* **[Snowflake](https://github.com/datawiz168/mcp-snowflake-service)** - 与Snowflake数据库交互
* **[Spotify](https://github.com/varunneal/spotify-mcp)** - 控制Spotify播放和管理播放列表
* **[Todoist](https://github.com/abhiz123/todoist-mcp-server)** - 任务管理集成

> **注意：** 社区服务器未经测试，使用风险自负。它们与Anthropic无关，也不受其认可。

有关社区服务器的完整列表，请访问[MCP服务器仓库](https://github.com/modelcontextprotocol/servers)。
## 入门指南

### 使用参考服务器

基于TypeScript的服务器可以直接使用`npx`运行：

```bash
npx -y @modelcontextprotocol/server-memory
```

基于Python的服务器可以使用`uvx`(推荐)或`pip`运行：

```bash
# 使用uvx
uvx mcp-server-git

# 使用pip
pip install mcp-server-git
python -m mcp_server_git
```

### 配置Claude

要在Claude中使用MCP服务器，将其添加到配置中：

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/files"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_TOKEN>"
      }
    }
  }
}
```

## 其他资源

* [MCP服务器仓库](https://github.com/modelcontextprotocol/servers) - 参考实现和社区服务器的完整集合
* [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - 精选的MCP服务器列表
* [MCP CLI](https://github.com/wong2/mcp-cli) - 用于测试MCP服务器的命令行检查器
* [MCP Get](https://mcp-get.com) - 安装和管理MCP服务器的工具
* [Supergateway](https://github.com/supercorp-ai/supergateway) - 通过SSE运行MCP stdio服务器
* [Zapier MCP](https://zapier.com/mcp) - 支持7,000+应用和30,000+操作的MCP服务器

访问我们的[GitHub讨论区](https://github.com/orgs/modelcontextprotocol/discussions)与MCP社区互动。


# 常见问题
来源：https://modelcontextprotocol.io/faqs

用简单的术语解释MCP及其重要性

## 什么是MCP？

MCP(模型上下文协议)是一种标准方式，使AI应用程序和代理能够连接并与您的数据源(如本地文件、数据库或内容仓库)和工具(如GitHub、Google地图或Puppeteer)一起工作。

将MCP视为AI应用程序的通用适配器，类似于USB-C对于物理设备的作用。USB-C作为连接设备到各种外围设备和配件的通用适配器。同样，MCP提供了一种标准化方式来连接AI应用程序到不同的数据和工具。

在USB-C之前，您需要不同的线缆进行不同的连接。同样，在MCP之前，开发人员必须为他们希望AI应用程序使用的每个数据源或工具构建自定义连接——这是一个耗时的过程，通常导致功能有限。现在，有了MCP，开发人员可以轻松地将连接添加到他们的AI应用程序中，使应用程序从一开始就变得更强大。

## 为什么MCP很重要？

### 对于AI应用程序用户

MCP意味着您的AI应用程序可以访问您每天使用的信息和工具，使它们更有帮助。AI不再局限于它已经知道的内容，现在可以理解您的特定文档、数据和工作上下文。

例如，通过使用MCP服务器，应用程序可以从Google Drive访问您的个人文档或从GitHub获取关于您的代码库的数据，提供更个性化和上下文相关的帮助。

想象一下询问AI助手："总结上周的团队会议记录，并为每个人安排后续工作。"

通过使用由MCP提供支持的数据源连接，AI助手可以：

* 通过MCP服务器连接到您的Google Drive读取会议记录
* 根据记录理解谁需要后续跟进
* 通过另一个MCP服务器连接到您的日历自动安排会议

### 对于开发人员

MCP减少了构建需要访问各种数据源的AI应用程序时的开发时间和复杂性。有了MCP，开发人员可以专注于构建出色的AI体验，而不是重复创建自定义连接器。

传统上，将应用程序与数据源连接需要为每个数据源和每个应用程序构建自定义的一次性连接。这造成了大量的重复工作——每个希望将其AI应用程序连接到Google Drive或Slack的开发人员都需要构建自己的连接。

MCP通过使开发人员能够为数据源构建可被各种应用程序重用的MCP服务器来简化这一过程。例如，使用开源的Google Drive MCP服务器，许多不同的应用程序可以访问Google Drive的数据，而无需每个开发人员构建自定义连接。

这个开源的MCP服务器生态系统意味着开发人员可以利用现有的工作，而不是从头开始，从而更容易构建强大的AI应用程序，这些应用程序可以无缝集成用户已经依赖的工具和数据源。

## MCP如何工作？

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/mcp-simple-diagram.png" />
</Frame>

MCP通过一个简单的系统在您的AI应用程序和数据之间创建桥梁：

* **MCP服务器**连接到您的数据源和工具(如Google Drive或Slack)
* **MCP客户端**由AI应用程序(如Claude桌面)运行以连接到这些服务器
* 当您授予权限时，您的AI应用程序会发现可用的MCP服务器
* AI模型然后可以使用这些连接来读取信息并采取行动

这个模块化系统意味着可以添加新功能而无需更改AI应用程序本身——就像为计算机添加新配件而无需升级整个系统一样。

## 谁创建和维护MCP服务器？

MCP服务器由以下人员开发和维护：

* Anthropic的开发人员为常见工具和数据源构建服务器
* 开源贡献者为他们使用的工具创建服务器
* 企业开发团队为其内部系统构建服务器
* 软件提供商使其应用程序支持AI

一旦为数据源创建了开源的MCP服务器，任何兼容MCP的AI应用程序都可以使用它，从而创建一个不断增长的连接生态系统。查看我们的[示例服务器列表](https://modelcontextprotocol.io/examples)，或[开始构建您自己的服务器](https://modelcontextprotocol.io/quickstart/server)。


# 介绍
来源：https://modelcontextprotocol.io/introduction

开始使用模型上下文协议(MCP)

<Note>C# SDK已发布！查看[其他新功能](/development/updates)</Note>

MCP是一个开放协议，标准化了应用程序如何向LLM提供上下文。将MCP视为AI应用程序的USB-C端口。就像USB-C提供了一种标准化方式来连接您的设备到各种外围设备和配件一样，MCP提供了一种标准化方式来连接AI模型到不同的数据源和工具。

## 为什么选择MCP？

MCP帮助您在LLM之上构建代理和复杂工作流。LLM经常需要与数据和工具集成，MCP提供：

* 越来越多的预构建集成列表，您的LLM可以直接插入
* 在LLM提供商和供应商之间切换的灵活性
* 在基础设施内保护数据的最佳实践

### 通用架构

MCP的核心遵循客户端-服务器架构，其中主机应用程序可以连接到多个服务器：

```mermaid
flowchart LR
    subgraph "您的计算机"
        Host["带有MCP客户端的主机\n(Claude, IDEs, 工具)"]
        S1["MCP服务器A"]
        S2["MCP服务器B"]
        S3["MCP服务器C"]
        Host <-->|"MCP协议"| S1
        Host <-->|"MCP协议"| S2
        Host <-->|"MCP协议"| S3
        S1 <--> D1[("本地\n数据源A")]
        S2 <--> D2[("本地\n数据源B")]
    end
    subgraph "互联网"
        S3 <-->|"Web APIs"| D3[("远程\n服务C")]
    end
```

* **MCP主机**：如Claude桌面、IDE或希望通过MCP访问数据的AI工具等程序
* **MCP客户端**：与服务器保持1:1连接的协议客户端
* **MCP服务器**：轻量级程序，每个程序通过标准化的模型上下文协议公开特定功能
* **本地数据源**：MCP服务器可以安全访问的计算机文件、数据库和服务
* **远程服务**：可通过互联网(如通过API)访问的外部系统，MCP服务器可以连接到这些系统

## 开始使用

选择最适合您需求的路径：

#### 快速入门

<CardGroup cols={2}>
  <Card title="服务器开发者" icon="bolt" href="/quickstart/server">
    开始构建您自己的服务器以在Claude桌面和其他客户端中使用
  </Card>

  <Card title="客户端开发者" icon="bolt" href="/quickstart/client">
    开始构建您自己的客户端，可以与所有MCP服务器集成
  </Card>

  <Card title="Claude桌面用户" icon="bolt" href="/quickstart/user">
开始使用Claude桌面中的预构建服务器
  </Card>
</CardGroup>

#### 示例

<CardGroup cols={2}>
  <Card title="示例服务器" icon="grid" href="/examples">
    查看我们的官方MCP服务器和实现库
  </Card>

  <Card title="示例客户端" icon="cubes" href="/clients">
    查看支持MCP集成的客户端列表
  </Card>
</CardGroup>

## 教程

<CardGroup cols={2}>
  <Card title="使用LLM构建MCP" icon="comments" href="/tutorials/building-mcp-with-llms">
    学习如何使用Claude等LLM加速您的MCP开发
  </Card>

  <Card title="调试指南" icon="bug" href="/docs/tools/debugging">
    学习如何有效调试MCP服务器和集成
  </Card>

  <Card title="MCP检查器" icon="magnifying-glass" href="/docs/tools/inspector">
    使用我们的交互式调试工具测试和检查您的MCP服务器
  </Card>

  <Card title="MCP工作坊(视频,2小时)" icon="person-chalkboard" href="https://www.youtube.com/watch?v=kQmXtrmQ5Zg">
    <iframe src="https://www.youtube.com/embed/kQmXtrmQ5Zg" />
  </Card>
</CardGroup>

## 探索MCP

深入了解MCP的核心概念和功能：

<CardGroup cols={2}>
  <Card title="核心架构" icon="sitemap" href="/docs/concepts/architecture">
    了解MCP如何连接客户端、服务器和LLM
  </Card>

  <Card title="资源" icon="database" href="/docs/concepts/resources">
    将服务器中的数据内容暴露给LLM
  </Card>

  <Card title="提示" icon="message" href="/docs/concepts/prompts">
    创建可重用的提示模板和工作流
  </Card>

  <Card title="工具" icon="wrench" href="/docs/concepts/tools">
    使LLM能够通过您的服务器执行操作
  </Card>

  <Card title="采样" icon="robot" href="/docs/concepts/sampling">
    让您的服务器从LLM请求补全
  </Card>

  <Card title="传输协议" icon="network-wired" href="/docs/concepts/transports">
    了解MCP的通信机制
  </Card>
</CardGroup>

## 贡献

想要贡献？查看我们的[贡献指南](/development/contributing)了解如何帮助改进MCP。

## 支持和反馈

以下是获取帮助或提供反馈的方式：

* 对于MCP规范、SDK或文档(开源)相关的错误报告和功能请求，请[创建GitHub issue](https://github.com/modelcontextprotocol)
* 关于MCP规范的讨论或问答，使用[规范讨论区](https://github.com/modelcontextprotocol/specification/discussions)
* 关于其他MCP开源组件的讨论或问答，使用[组织讨论区](https://github.com/orgs/modelcontextprotocol/discussions)
* 对于Claude.app和claude.ai的MCP集成相关的错误报告、功能请求和问题，请参阅Anthropic的[如何获取支持](https://support.anthropic.com/en/articles/9015913-how-to-get-support)指南


# 客户端开发者指南
来源：https://modelcontextprotocol.io/quickstart/client

开始构建可以与所有MCP服务器集成的客户端。

在本教程中，您将学习如何构建一个连接到MCP服务器的LLM驱动的聊天机器人客户端。建议先完成[服务器快速入门](/quickstart/server)指南，该指南将引导您完成构建第一个服务器的基本知识。

<Tabs>
  <Tab title="Python">
    [您可以在此处找到本教程的完整代码。](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/mcp-client-python)

    ## 系统要求

    开始前，请确保您的系统满足以下要求：

    * Mac或Windows电脑
    * 已安装最新版Python
    * 已安装最新版`uv`

    ## 设置环境

    首先，使用`uv`创建一个新的Python项目：

    ```bash
    # 创建项目目录
    uv init mcp-client
    cd mcp-client

    # 创建虚拟环境
    uv venv

    # 激活虚拟环境
    # Windows:
    .venv\Scripts\activate
    # Unix或MacOS:
    source .venv/bin/activate

    # 安装所需包
    uv add mcp anthropic python-dotenv

    # 删除样板文件
    rm main.py

    # 创建主文件
    touch client.py
    ```

    ## 设置API密钥

    您需要从[Anthropic控制台](https://console.anthropic.com/settings/keys)获取Anthropic API密钥。

    创建`.env`文件来存储它：

    ```bash
    # 创建.env文件
    touch .env
    ```

    将密钥添加到`.env`文件：

    ```bash
    ANTHROPIC_API_KEY=<your key here>
    ```

    将`.env`添加到`.gitignore`：

    ```bash
    echo ".env" >> .gitignore
    ```

    <Warning>
      确保您的`ANTHROPIC_API_KEY`安全！
    </Warning>

    ## 创建客户端

    ### 基本客户端结构

    首先，设置导入并创建基本客户端类：

    ```python
    import asyncio
    from typing import Optional
    from contextlib import AsyncExitStack

    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client

    from anthropic import Anthropic
    from dotenv import load_dotenv

    load_dotenv()  # 从.env加载环境变量

    class MCPClient:
        def __init__(self):
            # 初始化会话和客户端对象
            self.session: Optional[ClientSession] = None
            self.exit_stack = AsyncExitStack()
            self.anthropic = Anthropic()
        # 方法将在这里定义
    ```

    ### 服务器连接管理

    接下来，我们将实现连接到MCP服务器的方法：

    ```python
async def connect_to_server(self, server_script_path: str):
        """连接到MCP服务器

        Args:
            server_script_path: 服务器脚本路径(.py或.js)
        """
        is_python = server_script_path.endswith('.py')
        is_js = server_script_path.endswith('.js')
        if not (is_python or is_js):
            raise ValueError("服务器脚本必须是.py或.js文件")

        command = "python" if is_python else "node"
        server_params = StdioServerParameters(
            command=command,
            args=[server_script_path],
            env=None
        )

        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        # 列出可用工具
        response = await self.session.list_tools()
        tools = response.tools
        print("\n已连接到服务器，可用工具:", [tool.name for tool in tools])
    ```

    ### 查询处理逻辑

    现在添加处理查询和工具调用的核心功能：

    ```python
    async def process_query(self, query: str) -> str:
        """使用Claude和可用工具处理查询"""
        messages = [
            {
                "role": "user",
                "content": query
            }
        ]

        response = await self.session.list_tools()
        available_tools = [{
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.inputSchema
        } for tool in response.tools]

        # 初始Claude API调用
        response = self.anthropic.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=messages,
            tools=available_tools
        )

        # 处理响应并处理工具调用
        final_text = []

        assistant_message_content = []
        for content in response.content:
            if content.type == 'text':
                final_text.append(content.text)
                assistant_message_content.append(content)
            elif content.type == 'tool_use':
                tool_name = content.name
                tool_args = content.input

                # 执行工具调用
                result = await self.session.call_tool(tool_name, tool_args)
                final_text.append(f"[调用工具 {tool_name} 参数 {tool_args}]")

                assistant_message_content.append(content)
                messages.append({
                    "role": "assistant",
                    "content": assistant_message_content
                })
                messages.append({
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": content.id,
                            "content": result.content
                        }
                    ]
                })

                # 从Claude获取下一个响应
                response = self.anthropic.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=1000,
                    messages=messages,
                    tools=available_tools
                )

                final_text.append(response.content[0].text)

        return "\n".join(final_text)
    ```

    ### 交互式聊天界面

    现在添加聊天循环和清理功能：

    ```python
    async def chat_loop(self):
        """运行交互式聊天循环"""
        print("\nMCP客户端已启动！")
        print("输入您的查询或'quit'退出。")

        while True:
            try:
                query = input("\n查询: ").strip()

                if query.lower() == 'quit':
                    break

                response = await self.process_query(query)
                print("\n" + response)

            except Exception as e:
                print(f"\n错误: {str(e)}")

    async def cleanup(self):
        """清理资源"""
        await self.exit_stack.aclose()
    ```

    ### 主入口点

    最后添加主执行逻辑：

    ```python
    async def main():
        if len(sys.argv) < 2:
            print("用法: python client.py <path_to_server_script>")
            sys.exit(1)

        client = MCPClient()
        try:
            await client.connect_to_server(sys.argv[1])
            await client.chat_loop()
        finally:
            await client.cleanup()

    if __name__ == "__main__":
        import sys
        asyncio.run(main())
    ```

    您可以在此处找到完整的`client.py`文件[这里。](https://gist.github.com/zckly/f3f28ea731e096e53b39b47bf0a2d4b1)

    ## 关键组件说明

    ### 1. 客户端初始化

    * `MCPClient`类初始化会话管理和API客户端
    * 使用`AsyncExitStack`进行正确的资源管理
    * 配置Anthropic客户端用于Claude交互

    ### 2. 服务器连接

    * 支持Python和Node.js服务器
    * 验证服务器脚本类型
    * 设置正确的通信通道
    * 初始化会话并列出可用工具

    ### 3. 查询处理

    * 维护对话上下文
    * 处理Claude的响应和工具调用
    * 管理Claude和工具之间的消息流
    * 将结果组合成连贯的响应

    ### 4. 交互式界面

    * 提供简单的命令行界面
    * 处理用户输入并显示响应
    * 包含基本错误处理
    * 允许优雅退出

    ### 5. 资源管理
* 正确清理资源
    * 连接问题的错误处理
    * 优雅的关闭流程

    ## 常见定制点

    1. **工具处理**
       * 修改`process_query()`以处理特定工具类型
       * 为工具调用添加自定义错误处理
       * 实现工具特定的响应格式化

    2. **响应处理**
       * 自定义工具结果的格式化方式
       * 添加响应过滤或转换
       * 实现自定义日志记录

    3. **用户界面**
       * 添加GUI或Web界面
       * 实现丰富的控制台输出
       * 添加命令历史记录或自动补全

    ## 运行客户端

    要使用任何MCP服务器运行您的客户端：

    ```bash
    uv run client.py path/to/server.py # python服务器
    uv run client.py path/to/build/index.js # node服务器
    ```

    <Note>
      如果您正在继续服务器快速入门中的天气教程，您的命令可能看起来像这样：`python client.py .../quickstart-resources/weather-server-python/weather.py`
    </Note>

    客户端将：
    
    1. 连接到指定的服务器
    2. 列出可用工具
    3. 启动交互式聊天会话，您可以：
       * 输入查询
       * 查看工具执行
       * 获取Claude的响应

    以下是连接到服务器快速入门中的天气服务器时的示例：

    <Frame>
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/client-claude-cli-python.png" />
    </Frame>

    ## 工作原理

    当您提交查询时：

    1. 客户端从服务器获取可用工具列表
    2. 您的查询与工具描述一起发送给Claude
    3. Claude决定使用哪些工具(如果有)
    4. 客户端通过服务器执行任何请求的工具调用
    5. 结果发送回Claude
    6. Claude提供自然语言响应
    7. 响应显示给您

    ## 最佳实践

    1. **错误处理**
       * 始终在try-catch块中包装工具调用
       * 提供有意义的错误消息
       * 优雅地处理连接问题

    2. **资源管理**
       * 使用`AsyncExitStack`进行正确清理
       * 完成后关闭连接
       * 处理服务器断开连接

    3. **安全性**
       * 将API密钥安全存储在`.env`中
       * 验证服务器响应
       * 谨慎处理工具权限

    ## 故障排除

    ### 服务器路径问题

    * 仔细检查服务器脚本路径是否正确
    * 如果相对路径不起作用，请使用绝对路径
    * Windows用户请确保在路径中使用正斜杠(/)或转义反斜杠(\\)
    * 验证服务器文件具有正确的扩展名(.py表示Python，.js表示Node.js)

    正确路径使用示例：

    ```bash
    # 相对路径
    uv run client.py ./server/weather.py

    # 绝对路径
    uv run client.py /Users/username/projects/mcp-server/weather.py

    # Windows路径(两种格式都可以)
    uv run client.py C:/projects/mcp-server/weather.py
    uv run client.py C:\\projects\\mcp-server\\weather.py
    ```

    ### 响应时间

    * 第一个响应可能需要长达30秒才能返回
    * 这是正常的，发生在：
      * 服务器初始化时
      * Claude处理查询时
      * 工具正在执行时
    * 后续响应通常更快
    * 在此初始等待期间不要中断进程

    ### 常见错误消息

    如果您看到：

    * `FileNotFoundError`：检查您的服务器路径
    * `Connection refused`：确保服务器正在运行且路径正确
    * `Tool execution failed`：验证工具所需的环境变量是否已设置
    * `Timeout error`：考虑增加客户端配置中的超时时间
  </Tab>

  <Tab title="Node">
    [您可以在此处找到本教程的完整代码。](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/mcp-client-typescript)

    ## 系统要求

    开始前，请确保您的系统满足以下要求：

    * Mac或Windows电脑
    * 已安装Node.js 17或更高版本
    * 已安装最新版`npm`
    * Anthropic API密钥(Claude)

    ## 设置环境

    首先，让我们创建并设置项目：

    <CodeGroup>
      ```bash MacOS/Linux
      # 创建项目目录
      mkdir mcp-client-typescript
      cd mcp-client-typescript

      # 初始化npm项目
      npm init -y

      # 安装依赖项
      npm install @anthropic-ai/sdk @modelcontextprotocol/sdk dotenv

      # 安装开发依赖项
      npm install -D @types/node typescript

      # 创建源文件
      touch index.ts
      ```

      ```powershell Windows
      # 创建项目目录
      md mcp-client-typescript
      cd mcp-client-typescript

      # 初始化npm项目
      npm init -y

      # 安装依赖项
      npm install @anthropic-ai/sdk @modelcontextprotocol/sdk dotenv

      # 安装开发依赖项
      npm install -D @types/node typescript

      # 创建源文件
      new-item index.ts
      ```
    </CodeGroup>

    更新您的`package.json`以设置`type: "module"`和构建脚本：

    ```json package.json
    {
      "type": "module",
      "scripts": {
        "build": "tsc && chmod 755 build/index.js"
      }
    }
    ```

    在项目根目录创建`tsconfig.json`：
{
      "compilerOptions": {
        "target": "ES2022",
        "module": "Node16",
        "moduleResolution": "Node16",
        "outDir": "./build",
        "rootDir": "./",
        "strict": true,
        "esModuleInterop": true,
        "skipLibCheck": true,
        "forceConsistentCasingInFileNames": true
      },
      "include": ["index.ts"],
      "exclude": ["node_modules"]
    }
    ```

    ## 设置API密钥

    您需要从[Anthropic控制台](https://console.anthropic.com/settings/keys)获取Anthropic API密钥。

    创建.env文件来存储它：

    ```bash
    echo "ANTHROPIC_API_KEY=<your key here>" > .env
    ```

    将.env添加到.gitignore：

    ```bash
    echo ".env" >> .gitignore
    ```

    <Warning>
      确保您的`ANTHROPIC_API_KEY`安全！
    </Warning>

    ## 创建客户端

    ### 基本客户端结构

    首先，在`index.ts`中设置导入并创建基本客户端类：

    ```typescript
    import { Anthropic } from "@anthropic-ai/sdk";
    import {
      MessageParam,
      Tool,
    } from "@anthropic-ai/sdk/resources/messages/messages.mjs";
    import { Client } from "@modelcontextprotocol/sdk/client/index.js";
    import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
    import readline from "readline/promises";
    import dotenv from "dotenv";

    dotenv.config();

    const ANTHROPIC_API_KEY = process.env.ANTHROPIC_API_KEY;
    if (!ANTHROPIC_API_KEY) {
      throw new Error("ANTHROPIC_API_KEY未设置");
    }

    class MCPClient {
      private mcp: Client;
      private anthropic: Anthropic;
      private transport: StdioClientTransport | null = null;
      private tools: Tool[] = [];

      constructor() {
        this.anthropic = new Anthropic({
          apiKey: ANTHROPIC_API_KEY,
        });
        this.mcp = new Client({ name: "mcp-client-cli", version: "1.0.0" });
      }
      // 方法将在这里定义
    }
    ```

    ### 服务器连接管理

    接下来，实现连接到MCP服务器的方法：

    ```typescript
    async connectToServer(serverScriptPath: string) {
      try {
        const isJs = serverScriptPath.endsWith(".js");
        const isPy = serverScriptPath.endsWith(".py");
        if (!isJs && !isPy) {
          throw new Error("服务器脚本必须是.js或.py文件");
        }
        const command = isPy
          ? process.platform === "win32"
            ? "python"
            : "python3"
          : process.execPath;
        
        this.transport = new StdioClientTransport({
          command,
          args: [serverScriptPath],
        });
        this.mcp.connect(this.transport);
        
        const toolsResult = await this.mcp.listTools();
        this.tools = toolsResult.tools.map((tool) => {
          return {
            name: tool.name,
            description: tool.description,
            input_schema: tool.inputSchema,
          };
        });
        console.log(
          "已连接到服务器，可用工具:",
          this.tools.map(({ name }) => name)
        );
      } catch (e) {
        console.log("连接到MCP服务器失败: ", e);
        throw e;
      }
    }
    ```

    ### 查询处理逻辑

    现在添加处理查询和工具调用的核心功能：

    ```typescript
    async processQuery(query: string) {
      const messages: MessageParam[] = [
        {
          role: "user",
          content: query,
        },
      ];

      const response = await this.anthropic.messages.create({
        model: "claude-3-5-sonnet-20241022",
        max_tokens: 1000,
        messages,
        tools: this.tools,
      });

      const finalText = [];
      const toolResults = [];

      for (const content of response.content) {
        if (content.type === "text") {
          finalText.push(content.text);
        } else if (content.type === "tool_use") {
          const toolName = content.name;
          const toolArgs = content.input as { [x: string]: unknown } | undefined;

          const result = await this.mcp.callTool({
            name: toolName,
            arguments: toolArgs,
          });
          toolResults.push(result);
          finalText.push(
            `[调用工具 ${toolName} 参数 ${JSON.stringify(toolArgs)}]`
          );

          messages.push({
            role: "user",
            content: result.content as string,
          });

          const response = await this.anthropic.messages.create({
            model: "claude-3-5-sonnet-20241022",
            max_tokens: 1000,
            messages,
          });

          finalText.push(
            response.content[0].type === "text" ? response.content[0].text : ""
          );
        }
      }

      return finalText.join("\n");
    }
    ```

    ### 交互式聊天界面

    现在添加聊天循环和清理功能：
async chatLoop() {
      const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
      });

      try {
        console.log("\nMCP客户端已启动！");
        console.log("输入您的查询或'quit'退出。");

        while (true) {
          const message = await rl.question("\n查询: ");
          if (message.toLowerCase() === "quit") {
            break;
          }
          const response = await this.processQuery(message);
          console.log("\n" + response);
        }
      } finally {
        rl.close();
      }
    }

    async cleanup() {
      await this.mcp.close();
    }
    ```

    ### 主入口点

    最后添加主执行逻辑：

    ```typescript
    async function main() {
      if (process.argv.length < 3) {
        console.log("用法: node index.ts <path_to_server_script>");
        return;
      }
      const mcpClient = new MCPClient();
      try {
        await mcpClient.connectToServer(process.argv[2]);
        await mcpClient.chatLoop();
      } finally {
        await mcpClient.cleanup();
        process.exit(0);
      }
    }

    main();
    ```

    ## 运行客户端

    要使用任何MCP服务器运行您的客户端：

    ```bash
    # 构建TypeScript
    npm run build

    # 运行客户端
    node build/index.js path/to/server.py # python服务器
    node build/index.js path/to/build/index.js # node服务器
    ```

    <Note>
      如果您正在继续服务器快速入门中的天气教程，您的命令可能看起来像这样：`node build/index.js .../quickstart-resources/weather-server-typescript/build/index.js`
    </Note>

    **客户端将：**

    1. 连接到指定的服务器
    2. 列出可用工具
    3. 启动交互式聊天会话，您可以：
       * 输入查询
       * 查看工具执行
       * 获取Claude的响应

    ## 工作原理

    当您提交查询时：

    1. 客户端从服务器获取可用工具列表
    2. 您的查询与工具描述一起发送给Claude
    3. Claude决定使用哪些工具(如果有)
    4. 客户端通过服务器执行任何请求的工具调用
    5. 结果发送回Claude
    6. Claude提供自然语言响应
    7. 响应显示给您

    ## 最佳实践

    1. **错误处理**
       * 使用TypeScript的类型系统进行更好的错误检测
       * 在try-catch块中包装工具调用
       * 提供有意义的错误消息
       * 优雅地处理连接问题

    2. **安全性**
       * 将API密钥安全存储在`.env`中
       * 验证服务器响应
       * 谨慎处理工具权限

    ## 故障排除

    ### 服务器路径问题

    * 仔细检查服务器脚本路径是否正确
    * 如果相对路径不起作用，请使用绝对路径
    * Windows用户请确保在路径中使用正斜杠(/)或转义反斜杠(\\)
    * 验证服务器文件具有正确的扩展名(.js表示Node.js或.py表示Python)

    正确路径使用示例：

    ```bash
    # 相对路径
    node build/index.js ./server/build/index.js

    # 绝对路径
    node build/index.js /Users/username/projects/mcp-server/build/index.js

    # Windows路径(两种格式都可以)
    node build/index.js C:/projects/mcp-server/build/index.js
    node build/index.js C:\\projects\\mcp-server\\build\\index.js
    ```

    ### 响应时间

    * 第一个响应可能需要长达30秒才能返回
    * 这是正常的，发生在：
      * 服务器初始化时
      * Claude处理查询时
      * 工具正在执行时
    * 后续响应通常更快
    * 在此初始等待期间不要中断进程

    ### 常见错误消息

    如果您看到：

    * `Error: Cannot find module`: 检查您的构建文件夹并确保TypeScript编译成功
    * `Connection refused`: 确保服务器正在运行且路径正确
    * `Tool execution failed`: 验证工具所需的环境变量是否已设置
    * `ANTHROPIC_API_KEY is not set`: 检查您的.env文件和环境变量
    * `TypeError`: 确保您为工具参数使用了正确的类型
  </Tab>

  <Tab title="Java">
    <Note>
      这是基于Spring AI MCP自动配置和boot starter的快速入门演示。
      要学习如何手动创建同步和异步MCP客户端，请查阅[Java SDK客户端](/sdk/java/mcp-client)文档
    </Note>

    此示例演示如何构建一个交互式聊天机器人，将Spring AI的Model Context Protocol (MCP)与[Brave Search MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search)结合使用。该应用程序创建了一个由Anthropic的Claude AI模型驱动的对话界面，可以通过Brave Search执行互联网搜索，实现与实时网络数据的自然语言交互。
    [您可以在此处找到本教程的完整代码。](https://github.com/spring-projects/spring-ai-examples/tree/main/model-context-protocol/web-search/brave-chatbot)

    ## 系统要求

    开始前，请确保您的系统满足以下要求：

    * Java 17或更高版本
    * Maven 3.6+
    * npx包管理器
    * Anthropic API密钥(Claude)
    * Brave Search API密钥

    ## 设置环境

    1. 安装npx(Node Package eXecute):
       首先确保安装[npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
       然后运行:
       ```bash
       npm install -g npx
       ```

    2. 克隆仓库:
       ```bash
       git clone https://github.com/spring-projects/spring-ai-examples.git
       cd model-context-protocol/brave-chatbot
       ```

    3. 设置API密钥:
       ```bash
       export ANTHROPIC_API_KEY='your-anthropic-api-key-here'
       export BRAVE_API_KEY='your-brave-api-key-here'
       ```

    4. 构建应用程序:
./mvnw clean install
       ```

    5. 使用Maven运行应用程序：
       ```bash
       ./mvnw spring-boot:run
       ```

    <Warning>
      确保您的`ANTHROPIC_API_KEY`和`BRAVE_API_KEY`密钥安全！
    </Warning>

    ## 工作原理

    该应用程序通过几个组件将Spring AI与Brave Search MCP服务器集成：

    ### MCP客户端配置

    1. pom.xml中的必需依赖：

    ```xml
    <dependency>
        <groupId>org.springframework.ai</groupId>
        <artifactId>spring-ai-starter-mcp-client</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.ai</groupId>
        <artifactId>spring-ai-starter-model-anthropic</artifactId>
    </dependency>
    ```

    2. 应用程序属性(application.yml)：

    ```yml
    spring:
      ai:
        mcp:
          client:
            enabled: true
            name: brave-search-client
            version: 1.0.0
            type: SYNC
            request-timeout: 20s
            stdio:
              root-change-notification: true
              servers-configuration: classpath:/mcp-servers-config.json
            toolcallback:
              enabled: true
        anthropic:
          api-key: ${ANTHROPIC_API_KEY}
    ```

    这会激活`spring-ai-starter-mcp-client`，根据提供的服务器配置创建一个或多个`McpClient`。
    `spring.ai.mcp.client.toolcallback.enabled=true`属性启用了工具回调机制，自动将所有MCP工具注册为spring ai工具。
    默认情况下它是禁用的。

    3. MCP服务器配置(`mcp-servers-config.json`)：

    ```json
    {
      "mcpServers": {
        "brave-search": {
          "command": "npx",
          "args": [
            "-y",
            "@modelcontextprotocol/server-brave-search"
          ],
          "env": {
            "BRAVE_API_KEY": "<PUT YOUR BRAVE API KEY>"
          }
        }
      }
    }
    ```

    ### 聊天实现

    聊天机器人使用Spring AI的ChatClient与MCP工具集成实现：

    ```java
    var chatClient = chatClientBuilder
        .defaultSystem("You are useful assistant, expert in AI and Java.")
        .defaultTools((Object[]) mcpToolAdapter.toolCallbacks())
        .defaultAdvisors(new MessageChatMemoryAdvisor(new InMemoryChatMemory()))
        .build();
    ```

    关键特性：

    * 使用Claude AI模型进行自然语言理解
    * 通过MCP集成Brave Search实现实时网络搜索能力
    * 使用InMemoryChatMemory维护对话记忆
    * 作为交互式命令行应用程序运行

    ### 构建和运行

    ```bash
    ./mvnw clean install
    java -jar ./target/ai-mcp-brave-chatbot-0.0.1-SNAPSHOT.jar
    ```

    或

    ```bash
    ./mvnw spring-boot:run
    ```

    应用程序将启动一个交互式聊天会话，您可以提问。当聊天机器人需要从互联网查找信息来回答您的问题时，它会使用Brave Search。

    聊天机器人可以：

    * 使用内置知识回答问题
    * 需要时使用Brave Search执行网络搜索
    * 记住之前对话中的上下文
    * 结合多个来源的信息提供全面的答案

    ### 高级配置

    MCP客户端支持额外的配置选项：

    * 通过`McpSyncClientCustomizer`或`McpAsyncClientCustomizer`自定义客户端
    * 多种客户端类型，支持多种传输类型：`STDIO`和`SSE`(Server-Sent Events)
    * 与Spring AI的工具执行框架集成
    * 自动客户端初始化和生命周期管理

    对于基于WebFlux的应用程序，您可以使用WebFlux starter替代：

    ```xml
    <dependency>
        <groupId>org.springframework.ai</groupId>
        <artifactId>spring-ai-mcp-client-webflux-spring-boot-starter</artifactId>
    </dependency>
    ```

    这提供了类似的功能，但使用了基于WebFlux的SSE传输实现，推荐用于生产部署。
  </Tab>

  <Tab title="Kotlin">
    [您可以在此处找到本教程的完整代码。](https://github.com/modelcontextprotocol/kotlin-sdk/tree/main/samples/kotlin-mcp-client)

    ## 系统要求

    开始前，请确保您的系统满足以下要求：

    * Java 17或更高版本
    * Anthropic API密钥(Claude)

    ## 设置环境

    首先，如果您还没有安装`java`和`gradle`，请先安装。
    您可以从[Oracle JDK官网](https://www.oracle.com/java/technologies/downloads/)下载`java`。
    验证您的`java`安装：

    ```bash
    java --version
    ```

    现在，让我们创建并设置您的项目：

    <CodeGroup>
      ```bash MacOS/Linux
      # 为我们的项目创建一个新目录
      mkdir kotlin-mcp-client
      cd kotlin-mcp-client

      # 初始化一个新的kotlin项目
      gradle init
      ```

      ```powershell Windows
      # 为我们的项目创建一个新目录
      md kotlin-mcp-client
      cd kotlin-mcp-client
      # 初始化一个新的kotlin项目
      gradle init
      ```
    </CodeGroup>

    运行`gradle init`后，您将看到创建项目的选项。
    选择**Application**作为项目类型，**Kotlin**作为编程语言，**Java 17**作为Java版本。

    或者，您可以使用[IntelliJ IDEA项目向导](https://kotlinlang.org/docs/jvm-get-started.html)创建Kotlin应用程序。

    创建项目后，添加以下依赖项：

    <CodeGroup>
val mcpVersion = "0.4.0"
      val slf4jVersion = "2.0.9"
      val anthropicVersion = "0.8.0"

      dependencies {
          implementation("io.modelcontextprotocol:kotlin-sdk:$mcpVersion")
          implementation("org.slf4j:slf4j-nop:$slf4jVersion")
          implementation("com.anthropic:anthropic-java:$anthropicVersion")
      }
      ```

      ```groovy build.gradle
      def mcpVersion = '0.3.0'
      def slf4jVersion = '2.0.9'
      def anthropicVersion = '0.8.0'
      dependencies {
          implementation "io.modelcontextprotocol:kotlin-sdk:$mcpVersion"
          implementation "org.slf4j:slf4j-nop:$slf4jVersion"
          implementation "com.anthropic:anthropic-java:$anthropicVersion"
      }
      ```
    </CodeGroup>

    同时，在构建脚本中添加以下插件：

    <CodeGroup>
      ```kotlin build.gradle.kts
      plugins {
          id("com.github.johnrengelman.shadow") version "8.1.1"
      }
      ```

      ```groovy build.gradle
      plugins {
          id 'com.github.johnrengelman.shadow' version '8.1.1'
      }
      ```
    </CodeGroup>

    ## 设置API密钥

    您需要从[Anthropic控制台](https://console.anthropic.com/settings/keys)获取Anthropic API密钥。

    设置您的API密钥：

    ```bash
    export ANTHROPIC_API_KEY='your-anthropic-api-key-here'
    ```

    <Warning>
      确保您的`ANTHROPIC_API_KEY`安全！
    </Warning>

    ## 创建客户端

    ### 基本客户端结构

    首先，创建基本客户端类：

    ```kotlin
    class MCPClient : AutoCloseable {
        private val anthropic = AnthropicOkHttpClient.fromEnv()
        private val mcp: Client = Client(clientInfo = Implementation(name = "mcp-client-cli", version = "1.0.0"))
        private lateinit var tools: List<ToolUnion>

        // 方法将在这里定义

        override fun close() {
            runBlocking {
                mcp.close()
                anthropic.close()
            }
        }
    ```

    ### 服务器连接管理

    接下来，实现连接到MCP服务器的方法：

    ```kotlin
    suspend fun connectToServer(serverScriptPath: String) {
        try {
            val command = buildList {
                when (serverScriptPath.substringAfterLast(".")) {
                    "js" -> add("node")
                    "py" -> add(if (System.getProperty("os.name").lowercase().contains("win")) "python" else "python3")
                    "jar" -> addAll(listOf("java", "-jar"))
                    else -> throw IllegalArgumentException("服务器脚本必须是.js、.py或.jar文件")
                }
                add(serverScriptPath)
            }

            val process = ProcessBuilder(command).start()
            val transport = StdioClientTransport(
                input = process.inputStream.asSource().buffered(),
                output = process.outputStream.asSink().buffered()
            )

            mcp.connect(transport)

            val toolsResult = mcp.listTools()
            tools = toolsResult?.tools?.map { tool ->
                ToolUnion.ofTool(
                    Tool.builder()
                        .name(tool.name)
                        .description(tool.description ?: "")
                        .inputSchema(
                            Tool.InputSchema.builder()
                                .type(JsonValue.from(tool.inputSchema.type))
                                .properties(tool.inputSchema.properties.toJsonValue())
                                .putAdditionalProperty("required", JsonValue.from(tool.inputSchema.required))
                                .build()
                        )
                        .build()
                )
            } ?: emptyList()
            println("已连接到服务器，可用工具: ${tools.joinToString(", ") { it.tool().get().name() }}")
        } catch (e: Exception) {
            println("连接到MCP服务器失败: $e")
            throw e
        }
    }
    ```

    同时创建一个辅助函数将`JsonObject`转换为Anthropic的`JsonValue`：

    ```kotlin
    private fun JsonObject.toJsonValue(): JsonValue {
        val mapper = ObjectMapper()
        val node = mapper.readTree(this.toString())
        return JsonValue.fromJsonNode(node)
    }
    ```

    ### 查询处理逻辑

    现在添加处理查询和工具调用的核心功能：

    ```kotlin
    private val messageParamsBuilder: MessageCreateParams.Builder = MessageCreateParams.builder()
        .model(Model.CLAUDE_3_5_SONNET_20241022)
        .maxTokens(1024)

    suspend fun processQuery(query: String): String {
        val messages = mutableListOf(
            MessageParam.builder()
                .role(MessageParam.Role.USER)
                .content(query)
                .build()
        )

        val response = anthropic.messages().create(
            messageParamsBuilder
                .messages(messages)
                .tools(tools)
                .build()
        )

        val finalText = mutableListOf<String>()
        response.content().forEach { content ->
            when {
                content.isText() -> finalText.add(content.text().getOrNull()?.text() ?: "")

                content.isToolUse() -> {
                    val toolName = content.toolUse().get().name()
                    val toolArgs =
                        content.toolUse().get()._input().convert(object : TypeReference<Map<String, JsonValue>>() {})

                    val result = mcp.callTool(
                        name = toolName,
                        arguments = toolArgs ?: emptyMap()
                    )
                    finalText.add("[调用工具 $toolName 参数 $toolArgs]")

                    messages.add(
                        MessageParam.builder()
                            .role(MessageParam.Role.USER)
                            .content(
                                """
                                    "type": "tool_result",
                                    "tool_name": $toolName,
                                    "result": ${result?.content?.joinToString("\n") { (it as TextContent).text ?: "" }}
                                """.trimIndent()
                            )
                            .build()
                    )
val aiResponse = anthropic.messages().create(
                        messageParamsBuilder
                            .messages(messages)
                            .build()
                    )

                    finalText.add(aiResponse.content().first().text().getOrNull()?.text() ?: "")
                }
            }
        }

        return finalText.joinToString("\n", prefix = "", postfix = "")
    }
    ```

    ### 交互式聊天

    添加聊天循环：

    ```kotlin
    suspend fun chatLoop() {
        println("\nMCP客户端已启动！")
        println("输入您的查询或'quit'退出。")

        while (true) {
            print("\n查询: ")
            val message = readLine() ?: break
            if (message.lowercase() == "quit") break
            val response = processQuery(message)
            println("\n$response")
        }
    }
    ```

    ### 主入口点

    最后添加主执行函数：

    ```kotlin
    fun main(args: Array<String>) = runBlocking {
        if (args.isEmpty()) throw IllegalArgumentException("用法: java -jar <your_path>/build/libs/kotlin-mcp-client-0.1.0-all.jar <path_to_server_script>")
        val serverPath = args.first()
        val client = MCPClient()
        client.use {
            client.connectToServer(serverPath)
            client.chatLoop()
        }
    }
    ```

    ## 运行客户端

    要使用任何MCP服务器运行您的客户端：

    ```bash
    ./gradlew build

    # 运行客户端
    java -jar build/libs/<your-jar-name>.jar path/to/server.jar # jvm服务器
    java -jar build/libs/<your-jar-name>.jar path/to/server.py # python服务器
    java -jar build/libs/<your-jar-name>.jar path/to/build/index.js # node服务器
    ```

    <Note>
      如果您正在继续服务器快速入门中的天气教程，您的命令可能看起来像这样：`java -jar build/libs/kotlin-mcp-client-0.1.0-all.jar .../samples/weather-stdio-server/build/libs/weather-stdio-server-0.1.0-all.jar`
    </Note>

    **客户端将：**

    1. 连接到指定的服务器
    2. 列出可用工具
    3. 启动交互式聊天会话，您可以：
       * 输入查询
       * 查看工具执行
       * 获取Claude的响应

    ## 工作原理

    以下是高级工作流程示意图：

    ```mermaid
    ---
    config:
        theme: neutral
    ---
    sequenceDiagram
        actor User
        participant Client
        participant Claude
        participant MCP_Server as MCP Server
        participant Tools

        User->>Client: 发送查询
        Client<<->>MCP_Server: 获取可用工具
        Client->>Claude: 发送带有工具描述的查询
        Claude-->>Client: 决定工具执行
        Client->>MCP_Server: 请求工具执行
        MCP_Server->>Tools: 执行选定的工具
        Tools-->>MCP_Server: 返回结果
        MCP_Server-->>Client: 发送结果
        Client->>Claude: 发送工具结果
        Claude-->>Client: 提供最终响应
        Client-->>User: 显示响应
    ```

    当您提交查询时：

    1. 客户端从服务器获取可用工具列表
    2. 您的查询与工具描述一起发送给Claude
    3. Claude决定使用哪些工具(如果有)
    4. 客户端通过服务器执行任何请求的工具调用
    5. 结果发送回Claude
    6. Claude提供自然语言响应
    7. 响应显示给您

    ## 最佳实践

    1. **错误处理**
       * 利用Kotlin的类型系统显式建模错误
       * 当可能出现异常时，在`try-catch`块中包装外部工具和API调用
       * 提供清晰且有意义的错误消息
       * 优雅地处理网络超时和连接问题

    2. **安全性**
       * 将API密钥和机密安全存储在`local.properties`、环境变量或密钥管理器中
       * 验证所有外部响应以避免意外或不安全的数据使用
       * 使用工具时谨慎处理权限和信任边界

    ## 故障排除

    ### 服务器路径问题

    * 仔细检查服务器脚本路径是否正确
    * 如果相对路径不起作用，请使用绝对路径
    * Windows用户请确保在路径中使用正斜杠(/)或转义反斜杠(\\)
    * 确保已安装所需的运行时(Java用于Java，npm用于Node.js，或uv用于Python)
    * 验证服务器文件具有正确的扩展名(.jar用于Java，.js用于Node.js或.py用于Python)

    正确路径使用示例：

    ```bash
    # 相对路径
    java -jar build/libs/client.jar ./server/build/libs/server.jar

    # 绝对路径
    java -jar build/libs/client.jar /Users/username/projects/mcp-server/build/libs/server.jar

    # Windows路径(两种格式都可以)
    java -jar build/libs/client.jar C:/projects/mcp-server/build/libs/server.jar
    java -jar build/libs/client.jar C:\\projects\\mcp-server\\build\\libs\\server.jar
    ```

    ### 响应时间

    * 第一个响应可能需要长达30秒才能返回
    * 这是正常的，发生在：
      * 服务器初始化时
      * Claude处理查询时
      * 工具正在执行时
    * 后续响应通常更快
    * 在此初始等待期间不要中断进程

    ### 常见错误消息

    如果您看到：

    * `Connection refused`: 确保服务器正在运行且路径正确
    * `Tool execution failed`: 验证工具所需的环境变量是否已设置
    * `ANTHROPIC_API_KEY is not set`: 检查您的环境变量
  </Tab>

  <Tab title="C#">
    [您可以在此处找到本教程的完整代码。](https://github.io/modelcontextprotocol/csharp-sdk/tree/main/samples/QuickstartClient)

    ## 系统要求

    开始前，请确保您的系统满足以下要求：

    * .NET 8.0或更高版本
    * Anthropic API密钥(Claude)
    * Windows、Linux或MacOS

    ## 设置环境

    首先，创建一个新的.NET项目：
dotnet new console -n QuickstartClient
    cd QuickstartClient
    ```

    然后，为项目添加所需依赖：

    ```bash
    dotnet add package ModelContextProtocol --prerelease
    dotnet add package Anthropic.SDK
    dotnet add package Microsoft.Extensions.Hosting
    ```

    ## 设置API密钥

    您需要从[Anthropic控制台](https://console.anthropic.com/settings/keys)获取Anthropic API密钥。

    ```bash
    dotnet user-secrets init
    dotnet user-secrets set "ANTHROPIC_API_KEY" "<your key here>"
    ```

    ## 创建客户端

    ### 基本客户端结构

    首先，设置基本客户端类：

    ```csharp
    using Microsoft.Extensions.Configuration;
    using Microsoft.Extensions.Hosting;

    var builder = Host.CreateEmptyApplicationBuilder(settings: null);

    builder.Configuration
        .AddUserSecrets<Program>();
    ```

    这创建了一个可以读取用户机密中API密钥的.NET控制台应用程序基础。

    接下来，设置MCP客户端：

    ```csharp
    var (command, arguments) = args switch
    {
        [var script] when script.EndsWith(".py") => ("python", script),
        [var script] when script.EndsWith(".js") => ("node", script),
        [var script] when Directory.Exists(script) || (File.Exists(script) && script.EndsWith(".csproj")) => ("dotnet", $"run --project {script} --no-build"),
        _ => throw new NotSupportedException("提供了不受支持的服务器脚本。支持的脚本为.py、.js或.csproj")
    };

    await using var mcpClient = await McpClientFactory.CreateAsync(new()
    {
        Id = "demo-server",
        Name = "Demo Server",
        TransportType = TransportTypes.StdIo,
        TransportOptions = new()
        {
            ["command"] = command,
            ["arguments"] = arguments,
        }
    });

    var tools = await mcpClient.ListToolsAsync();
    foreach (var tool in tools)
    {
        Console.WriteLine($"已连接到服务器，可用工具: {tool.Name}");
    }
    ```

    <Note>
      确保添加以下命名空间的using语句：

      ```csharp
      using ModelContextProtocol.Client;
      using ModelContextProtocol.Protocol.Transport;
      ```
    </Note>

    这配置了一个MCP客户端，将连接到作为命令行参数提供的服务器，然后列出连接服务器上的可用工具。

    ### 查询处理逻辑

    现在添加处理查询和工具调用的核心功能：

    ```csharp
    using IChatClient anthropicClient = new AnthropicClient(new APIAuthentication(builder.Configuration["ANTHROPIC_API_KEY"]))
        .Messages
        .AsBuilder()
        .UseFunctionInvocation()
        .Build();

    var options = new ChatOptions
    {
        MaxOutputTokens = 1000,
        ModelId = "claude-3-5-sonnet-20241022",
        Tools = [.. tools]
    };

    while (true)
    {
        Console.WriteLine("MCP客户端已启动！");
        Console.WriteLine("输入您的查询或'quit'退出。");

        string? query = Console.ReadLine();

        if (string.IsNullOrWhiteSpace(query))
        {
            continue;
        }
        if (string.Equals(query, "quit", StringComparison.OrdinalIgnoreCase))
        {
            break;
        }

        var response = anthropicClient.GetStreamingResponseAsync(query, options);

        await foreach (var message in response)
        {
            Console.Write(message.Text);
        }
        Console.WriteLine();
    }
    ```

    ## 关键组件说明

    ### 1. 客户端初始化

    * 使用`McpClientFactory.CreateAsync()`初始化客户端，设置传输类型和运行服务器的命令。

    ### 2. 服务器连接

    * 支持Python、Node.js和.NET服务器。
    * 使用参数中指定的命令启动服务器。
    * 配置使用stdio与服务器通信。
    * 初始化会话和可用工具。

    ### 3. 查询处理

    * 利用[Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/ai-extensions)作为聊天客户端。
    * 配置`IChatClient`使用自动工具(函数)调用。
    * 客户端读取用户输入并发送到服务器。
    * 服务器处理查询并返回响应。
    * 向用户显示响应。

    ### 运行客户端

    要使用任何MCP服务器运行您的客户端：

    ```bash
    dotnet run -- path/to/server.csproj # dotnet服务器
    dotnet run -- path/to/server.py # python服务器
    dotnet run -- path/to/server.js # node服务器
    ```

    <Note>
      如果您正在继续服务器快速入门中的天气教程，您的命令可能看起来像这样：`dotnet run -- path/to/QuickstartWeatherServer`。
    </Note>

    客户端将：

    1. 连接到指定的服务器
    2. 列出可用工具
    3. 启动交互式聊天会话，您可以：
       * 输入查询
       * 查看工具执行
       * 获取Claude的响应
    4. 完成后退出会话

    以下是连接到天气服务器快速入门时的示例：

    <Frame>
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-dotnet-client.png" />
    </Frame>
  </Tab>
</Tabs>

## 下一步

<CardGroup cols={2}>
  <Card title="示例服务器" icon="grid" href="/examples">
    查看我们的官方MCP服务器和实现库
  </Card>

  <Card title="客户端" icon="cubes" href="/clients">
    查看支持MCP集成的客户端列表
</Card>

  <Card title="使用LLM构建MCP" icon="comments" href="/tutorials/building-mcp-with-llms">
    学习如何使用Claude等LLM加速您的MCP开发
  </Card>

  <Card title="核心架构" icon="sitemap" href="/docs/concepts/architecture">
    了解MCP如何连接客户端、服务器和LLM
  </Card>
</CardGroup>


# 服务器开发者指南
来源: https://modelcontextprotocol.io/quickstart/server

开始构建您自己的服务器，用于Claude桌面版和其他客户端。

在本教程中，我们将构建一个简单的MCP天气服务器，并将其连接到主机(Claude桌面版)。我们将从基本设置开始，然后逐步过渡到更复杂的用例。

### 我们将构建什么

许多LLM目前无法获取天气预报和恶劣天气警报。让我们用MCP来解决这个问题！

我们将构建一个暴露两个工具的服务器：`get-alerts`和`get-forecast`。然后我们将服务器连接到MCP主机(本例中为Claude桌面版)：

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/weather-alerts.png" />
</Frame>

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/current-weather.png" />
</Frame>

<Note>
  服务器可以连接到任何客户端。我们在这里选择Claude桌面版是为了简单起见，但我们也有[构建您自己的客户端](/quickstart/client)指南以及[其他客户端列表](/clients)。
</Note>

<Accordion title="为什么选择Claude桌面版而不是Claude.ai？">
  因为服务器是本地运行的，MCP目前仅支持桌面主机。远程主机正在积极开发中。
</Accordion>

### MCP核心概念

MCP服务器可以提供三种主要类型的能力：

1. **资源**：客户端可读取的类文件数据(如API响应或文件内容)
2. **工具**：LLM可以调用的函数(需用户批准)
3. **提示**：帮助用户完成特定任务的预写模板

本教程将主要关注工具。

<Tabs>
  <Tab title="Python">
    让我们开始构建我们的天气服务器！[您可以在此处找到我们将构建的完整代码。](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/weather-server-python)

    ### 预备知识

    本快速入门假设您熟悉：

    * Python
    * Claude等LLM

    ### 系统要求

    * 已安装Python 3.10或更高版本
    * 必须使用Python MCP SDK 1.2.0或更高版本

    ### 设置环境

    首先，安装`uv`并设置我们的Python项目和环境：

    <CodeGroup>
      ```bash MacOS/Linux
      curl -LsSf https://astral.sh/uv/install.sh | sh
      ```

      ```powershell Windows
      powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
      ```
    </CodeGroup>

    确保之后重新启动终端，以确保`uv`命令被识别。

    现在，让我们创建并设置我们的项目：

    <CodeGroup>
      ```bash MacOS/Linux
      # 为我们的项目创建新目录
      uv init weather
      cd weather

      # 创建虚拟环境并激活
      uv venv
      source .venv/bin/activate

      # 安装依赖
      uv add "mcp[cli]" httpx

      # 创建服务器文件
      touch weather.py
      ```

      ```powershell Windows
      # 为我们的项目创建新目录
      uv init weather
      cd weather

      # 创建虚拟环境并激活
      uv venv
      .venv\Scripts\activate

      # 安装依赖
      uv add mcp[cli] httpx

      # 创建服务器文件
      new-item weather.py
      ```
    </CodeGroup>

    现在让我们深入构建您的服务器。

    ## 构建您的服务器

    ### 导入包并设置实例

    将这些添加到您的`weather.py`顶部：

    ```python
    from typing import Any
    import httpx
    from mcp.server.fastmcp import FastMCP

    # 初始化FastMCP服务器
    mcp = FastMCP("weather")

    # 常量
    NWS_API_BASE = "https://api.weather.gov"
    USER_AGENT = "weather-app/1.0"
    ```

    FastMCP类使用Python类型提示和文档字符串自动生成工具定义，使创建和维护MCP工具变得容易。

    ### 辅助函数

    接下来，添加我们的辅助函数，用于查询和格式化来自国家气象局API的数据：

    ```python
    async def make_nws_request(url: str) -> dict[str, Any] | None:
        """向NWS API发出请求并进行适当的错误处理。"""
        headers = {
            "User-Agent": USER_AGENT,
            "Accept": "application/geo+json"
        }
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, headers=headers, timeout=30.0)
                response.raise_for_status()
                return response.json()
            except Exception:
                return None

    def format_alert(feature: dict) -> str:
        """将警报特征格式化为可读字符串。"""
        props = feature["properties"]
        return f"""
    事件: {props.get('event', '未知')}
    区域: {props.get('areaDesc', '未知')}
    严重程度: {props.get('severity', '未知')}
    描述: {props.get('description', '无描述信息')}
    指示: {props.get('instruction', '未提供具体指示')}
    """
    ```

    ### 实现工具执行

    工具执行处理程序负责实际执行每个工具的逻辑。让我们添加它：

    ```python
    @mcp.tool()
    async def get_alerts(state: str) -> str:
        """获取美国州的天气警报。

        参数:
            state: 两字母美国州代码(如CA, NY)
        """
        url = f"{NWS_API_BASE}/alerts/active/area/{state}"
        data = await make_nws_request(url)
if not data or "features" not in data:
            return "无法获取警报或未找到警报。"

        if not data["features"]:
            return "该州没有活跃警报。"

        alerts = [format_alert(feature) for feature in data["features"]]
        return "\n---\n".join(alerts)

    @mcp.tool()
    async def get_forecast(latitude: float, longitude: float) -> str:
        """获取位置的天气预报。

        参数:
            latitude: 位置的纬度
            longitude: 位置的经度
        """
        # 首先获取预测网格端点
        points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
        points_data = await make_nws_request(points_url)

        if not points_data:
            return "无法获取该位置的预测数据。"

        # 从points响应中获取预测URL
        forecast_url = points_data["properties"]["forecast"]
        forecast_data = await make_nws_request(forecast_url)

        if not forecast_data:
            return "无法获取详细预测。"

        # 将时间段格式化为可读预测
        periods = forecast_data["properties"]["periods"]
        forecasts = []
        for period in periods[:5]:  # 只显示接下来的5个时间段
            forecast = f"""
    {period['name']}:
    温度: {period['temperature']}°{period['temperatureUnit']}
    风速: {period['windSpeed']} {period['windDirection']}
    预测: {period['detailedForecast']}
    """
            forecasts.append(forecast)

        return "\n---\n".join(forecasts)
    ```

    ### 运行服务器

    最后，初始化和运行服务器：

    ```python
    if __name__ == "__main__":
        # 初始化并运行服务器
        mcp.run(transport='stdio')
    ```

    您的服务器已完成！运行`uv run weather.py`确认一切正常。

    现在让我们从现有的MCP主机Claude桌面版测试您的服务器。

    ## 使用Claude桌面版测试您的服务器

    <Note>
      Claude桌面版尚未在Linux上可用。Linux用户可以继续[构建客户端](/quickstart/client)教程，构建连接到我们刚构建的服务器的MCP客户端。
    </Note>

    首先，确保您已安装Claude桌面版。[您可以在此处安装最新版本。](https://claude.ai/download)如果您已经安装了Claude桌面版，请确保它是最新版本。

    我们需要为要使用的MCP服务器配置Claude桌面版。为此，在文本编辑器中打开Claude桌面版应用配置`~/Library/Application Support/Claude/claude_desktop_config.json`。如果文件不存在，请创建它。

    例如，如果您安装了[VS Code](https://code.visualstudio.com/)：

    <Tabs>
      <Tab title="MacOS/Linux">
        ```bash
        code ~/Library/Application\ Support/Claude/claude_desktop_config.json
        ```
      </Tab>

      <Tab title="Windows">
        ```powershell
        code $env:AppData\Claude\claude_desktop_config.json
        ```
      </Tab>
    </Tabs>

    然后您将在`mcpServers`键中添加您的服务器。只有在至少正确配置了一个服务器时，MCP UI元素才会显示在Claude桌面版中。

    在本例中，我们将像这样添加我们的单个天气服务器：

    <Tabs>
      <Tab title="MacOS/Linux">
        ```json Python
        {
            "mcpServers": {
                "weather": {
                    "command": "uv",
                    "args": [
                        "--directory",
                        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather",
                        "run",
                        "weather.py"
                    ]
                }
            }
        }
        ```
      </Tab>

      <Tab title="Windows">
        ```json Python
        {
            "mcpServers": {
                "weather": {
                    "command": "uv",
                    "args": [
                        "--directory",
                        "C:\\ABSOLUTE\\PATH\\TO\\PARENT\\FOLDER\\weather",
                        "run",
                        "weather.py"
                    ]
                }
            }
        }
        ```
      </Tab>
    </Tabs>

    <Warning>
      您可能需要在`command`字段中提供`uv`可执行文件的完整路径。在MacOS/Linux上可以通过运行`which uv`或在Windows上运行`where uv`获取。
    </Warning>

    <Note>
      确保传入服务器的绝对路径。
    </Note>

    这告诉Claude桌面版：

    1. 有一个名为"weather"的MCP服务器
    2. 通过运行`uv --directory /ABSOLUTE/PATH/TO/PARENT/FOLDER/weather run weather.py`启动它

    保存文件，并重启Claude桌面版。
  </Tab>

  <Tab title="Node">
    让我们开始构建我们的天气服务器！[您可以在此处找到我们将构建的完整代码。](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/weather-server-typescript)

    ### 预备知识

    本快速入门假设您熟悉：

    * TypeScript
    * Claude等LLM

    ### 系统要求

    对于TypeScript，请确保您已安装最新版本的Node。

    ### 设置环境

    首先，如果您尚未安装Node.js和npm，请从[nodejs.org](https://nodejs.org/)下载它们。
    验证您的Node.js安装：

    ```bash
    node --version
    npm --version
    ```

    对于本教程，您需要Node.js 16或更高版本。

    现在，让我们创建并设置我们的项目：

    <CodeGroup>
      ```bash MacOS/Linux
      # 为我们的项目创建新目录
      mkdir weather
      cd weather

      # 初始化新的npm项目
      npm init -y

      # 安装依赖
      npm install @modelcontextprotocol/sdk zod
      npm install -D @types/node typescript
# 创建我们的文件
      mkdir src
      touch src/index.ts
      ```

      ```powershell Windows
      # 为我们的项目创建新目录
      md weather
      cd weather

      # 初始化新的npm项目
      npm init -y

      # 安装依赖
      npm install @modelcontextprotocol/sdk zod
      npm install -D @types/node typescript

      # 创建我们的文件
      md src
      new-item src\index.ts
      ```
    </CodeGroup>

    更新您的package.json，添加type: "module"和构建脚本：

    ```json package.json
    {
      "type": "module",
      "bin": {
        "weather": "./build/index.js"
      },
      "scripts": {
        "build": "tsc && chmod 755 build/index.js"
      },
      "files": [
        "build"
      ],
    }
    ```

    在项目根目录创建`tsconfig.json`：

    ```json tsconfig.json
    {
      "compilerOptions": {
        "target": "ES2022",
        "module": "Node16",
        "moduleResolution": "Node16",
        "outDir": "./build",
        "rootDir": "./src",
        "strict": true,
        "esModuleInterop": true,
        "skipLibCheck": true,
        "forceConsistentCasingInFileNames": true
      },
      "include": ["src/**/*"],
      "exclude": ["node_modules"]
    }
    ```

    现在让我们深入构建您的服务器。

    ## 构建您的服务器

    ### 导入包并设置实例

    将这些添加到您的`src/index.ts`顶部：

    ```typescript
    import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
    import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
    import { z } from "zod";

    const NWS_API_BASE = "https://api.weather.gov";
    const USER_AGENT = "weather-app/1.0";

    // 创建服务器实例
    const server = new McpServer({
      name: "weather",
      version: "1.0.0",
      capabilities: {
        resources: {},
        tools: {},
      },
    });
    ```

    ### 辅助函数

    接下来，添加我们的辅助函数，用于查询和格式化来自国家气象局API的数据：

    ```typescript
    // 用于向NWS API发出请求的辅助函数
    async function makeNWSRequest<T>(url: string): Promise<T | null> {
      const headers = {
        "User-Agent": USER_AGENT,
        Accept: "application/geo+json",
      };

      try {
        const response = await fetch(url, { headers });
        if (!response.ok) {
          throw new Error(`HTTP错误! 状态码: ${response.status}`);
        }
        return (await response.json()) as T;
      } catch (error) {
        console.error("NWS请求出错:", error);
        return null;
      }
    }

    interface AlertFeature {
      properties: {
        event?: string;
        areaDesc?: string;
        severity?: string;
        status?: string;
        headline?: string;
      };
    }

    // 格式化警报数据
    function formatAlert(feature: AlertFeature): string {
      const props = feature.properties;
      return [
        `事件: ${props.event || "未知"}`,
        `区域: ${props.areaDesc || "未知"}`,
        `严重程度: ${props.severity || "未知"}`,
        `状态: ${props.status || "未知"}`,
        `标题: ${props.headline || "无标题"}`,
        "---",
      ].join("\n");
    }

    interface ForecastPeriod {
      name?: string;
      temperature?: number;
      temperatureUnit?: string;
      windSpeed?: string;
      windDirection?: string;
      shortForecast?: string;
    }

    interface AlertsResponse {
      features: AlertFeature[];
    }

    interface PointsResponse {
      properties: {
        forecast?: string;
      };
    }

    interface ForecastResponse {
      properties: {
        periods: ForecastPeriod[];
      };
    }
    ```

    ### 实现工具执行

    工具执行处理程序负责实际执行每个工具的逻辑。让我们添加它：

    ```typescript
    // 注册天气工具
    server.tool(
      "get-alerts",
      "获取州的天气警报",
      {
        state: z.string().length(2).describe("两字母州代码(如CA, NY)"),
      },
      async ({ state }) => {
        const stateCode = state.toUpperCase();
        const alertsUrl = `${NWS_API_BASE}/alerts?area=${stateCode}`;
        const alertsData = await makeNWSRequest<AlertsResponse>(alertsUrl);

        if (!alertsData) {
          return {
            content: [
              {
                type: "text",
                text: "获取警报数据失败",
              },
            ],
          };
        }
const features = alertsData.features || [];
        if (features.length === 0) {
          return {
            content: [
              {
                type: "text",
                text: `${stateCode}没有活跃警报`,
              },
            ],
          };
        }

        const formattedAlerts = features.map(formatAlert);
        const alertsText = `${stateCode}的活跃警报:\n\n${formattedAlerts.join("\n")}`;

        return {
          content: [
            {
              type: "text",
              text: alertsText,
            },
          ],
        };
      },
    );

    server.tool(
      "get-forecast",
      "获取位置的天气预报",
      {
        latitude: z.number().min(-90).max(90).describe("位置的纬度"),
        longitude: z.number().min(-180).max(180).describe("位置的经度"),
      },
      async ({ latitude, longitude }) => {
        // 获取网格点数据
        const pointsUrl = `${NWS_API_BASE}/points/${latitude.toFixed(4)},${longitude.toFixed(4)}`;
        const pointsData = await makeNWSRequest<PointsResponse>(pointsUrl);

        if (!pointsData) {
          return {
            content: [
              {
                type: "text",
                text: `无法获取坐标${latitude}, ${longitude}的网格点数据。该位置可能不受NWS API支持(仅支持美国位置)。`,
              },
            ],
          };
        }

        const forecastUrl = pointsData.properties?.forecast;
        if (!forecastUrl) {
          return {
            content: [
              {
                type: "text",
                text: "无法从网格点数据获取预测URL",
              },
            ],
          };
        }

        // 获取预测数据
        const forecastData = await makeNWSRequest<ForecastResponse>(forecastUrl);
        if (!forecastData) {
          return {
            content: [
              {
                type: "text",
                text: "无法获取预测数据",
              },
            ],
          };
        }

        const periods = forecastData.properties?.periods || [];
        if (periods.length === 0) {
          return {
            content: [
              {
                type: "text",
                text: "没有可用的预测时间段",
              },
            ],
          };
        }

        // 格式化预测时间段
        const formattedForecast = periods.map((period: ForecastPeriod) =>
          [
            `${period.name || "未知"}:`,
            `温度: ${period.temperature || "未知"}°${period.temperatureUnit || "F"}`,
            `风速: ${period.windSpeed || "未知"} ${period.windDirection || ""}`,
            `${period.shortForecast || "无可用预测"}`,
            "---",
          ].join("\n"),
        );

        const forecastText = `${latitude}, ${longitude}的预测:\n\n${formattedForecast.join("\n")}`;

        return {
          content: [
            {
              type: "text",
              text: forecastText,
            },
          ],
        };
      },
    );
    ```

    ### 运行服务器

    最后，实现主函数来运行服务器：

    ```typescript
    async function main() {
      const transport = new StdioServerTransport();
      await server.connect(transport);
      console.error("天气MCP服务器正在stdio上运行");
    }

    main().catch((error) => {
      console.error("main()中的致命错误:", error);
      process.exit(1);
    });
    ```

    确保运行`npm run build`来构建您的服务器！这是让服务器连接的重要步骤。

    现在让我们从现有的MCP主机Claude桌面版测试您的服务器。

    ## 使用Claude桌面版测试您的服务器

    <Note>
      Claude桌面版尚未在Linux上可用。Linux用户可以继续[构建客户端](/quickstart/client)教程，构建连接到我们刚构建的服务器的MCP客户端。
    </Note>

    首先，确保您已安装Claude桌面版。[您可以在此处安装最新版本。](https://claude.ai/download)如果您已经安装了Claude桌面版，请确保它是最新版本。

    我们需要为要使用的MCP服务器配置Claude桌面版。为此，在文本编辑器中打开Claude桌面版应用配置`~/Library/Application Support/Claude/claude_desktop_config.json`。如果文件不存在，请创建它。

    例如，如果您安装了[VS Code](https://code.visualstudio.com/)：

    <Tabs>
      <Tab title="MacOS/Linux">
        ```bash
        code ~/Library/Application\ Support/Claude/claude_desktop_config.json
        ```
      </Tab>

      <Tab title="Windows">
        ```powershell
        code $env:AppData\Claude\claude_desktop_config.json
        ```
      </Tab>
    </Tabs>

    然后您将在`mcpServers`键中添加您的服务器。只有在至少正确配置了一个服务器时，MCP UI元素才会显示在Claude桌面版中。

    在本例中，我们将像这样添加我们的单个天气服务器：

    <Tabs>
      <Tab title="MacOS/Linux">
        <CodeGroup>
          ```json Node
          {
              "mcpServers": {
                  "weather": {
                      "command": "node",
                      "args": [
                          "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather/build/index.js"
                      ]
                  }
              }
          }
          ```
        </CodeGroup>
      </Tab>

      <Tab title="Windows">
        <CodeGroup>
          ```json Node
          {
              "mcpServers": {
"weather": {
                      "command": "node",
                      "args": [
                          "C:\\PATH\\TO\\PARENT\\FOLDER\\weather\\build\\index.js"
                      ]
                  }
              }
          }
          ```
        </CodeGroup>
      </Tab>
    </Tabs>

    这告诉Claude桌面版：

    1. 有一个名为"weather"的MCP服务器
    2. 通过运行`node /ABSOLUTE/PATH/TO/PARENT/FOLDER/weather/build/index.js`启动它

    保存文件，并重启Claude桌面版。
  </Tab>

  <Tab title="Java">
    <Note>
      这是一个基于Spring AI MCP自动配置和boot starter的快速入门演示。
      要了解如何手动创建同步和异步MCP服务器，请参阅[Java SDK服务器](/sdk/java/mcp-server)文档。
    </Note>

    让我们开始构建我们的天气服务器！
    [您可以在此处找到我们将构建的完整代码。](https://github.com/spring-projects/spring-ai-examples/tree/main/model-context-protocol/weather/starter-stdio-server)

    更多信息，请参阅[MCP服务器Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html)参考文档。
    如需手动实现MCP服务器，请参考[MCP服务器Java SDK文档](/sdk/java/mcp-server)。

    ### 系统要求

    * 已安装Java 17或更高版本
    * [Spring Boot 3.3.x](https://docs.spring.io/spring-boot/installing.html)或更高版本

    ### 设置环境

    使用[Spring Initializer](https://start.spring.io/)初始化项目。

    您需要添加以下依赖：

    <Tabs>
      <Tab title="Maven">
        ```xml
        <dependencies>
              <dependency>
                  <groupId>org.springframework.ai</groupId>
                  <artifactId>spring-ai-starter-mcp-server</artifactId>
              </dependency>

              <dependency>
                  <groupId>org.springframework</groupId>
                  <artifactId>spring-web</artifactId>
              </dependency>
        </dependencies>
        ```
      </Tab>

      <Tab title="Gradle">
        ```groovy
        dependencies {
          implementation platform("org.springframework.ai:spring-ai-starter-mcp-server")
          implementation platform("org.springframework:spring-web")   
        }
        ```
      </Tab>
    </Tabs>

    然后通过设置应用属性来配置您的应用：

    <CodeGroup>
      ```bash application.properties
      spring.main.bannerMode=off
      logging.pattern.console=
      ```

      ```yaml application.yml
      logging:
        pattern:
          console:
      spring:
        main:
          banner-mode: off
      ```
    </CodeGroup>

    [服务器配置属性](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html#_configuration_properties)文档列出了所有可用属性。

    现在让我们深入构建您的服务器。

    ## 构建您的服务器

    ### 天气服务

    让我们实现一个[WeatherService.java](https://github.com/spring-projects/spring-ai-examples/blob/main/model-context-protocol/weather/starter-stdio-server/src/main/java/org/springframework/ai/mcp/sample/server/WeatherService.java)，使用REST客户端从国家气象局API查询数据：

    ```java
    @Service
    public class WeatherService {

    	private final RestClient restClient;

    	public WeatherService() {
    		this.restClient = RestClient.builder()
    			.baseUrl("https://api.weather.gov")
    			.defaultHeader("Accept", "application/geo+json")
    			.defaultHeader("User-Agent", "WeatherApiClient/1.0 (your@email.com)")
    			.build();
    	}

      @Tool(description = "获取特定经纬度的天气预报")
      public String getWeatherForecastByLocation(
          double latitude,   // 纬度坐标
          double longitude   // 经度坐标
      ) {
          // 返回详细预测包括：
          // - 温度和单位
          // - 风速和方向
          // - 详细预测描述
      }
    	
      @Tool(description = "获取美国州的天气警报")
      public String getAlerts(
          @ToolParam(description = "两字母美国州代码(如CA, NY)" String state
      ) {
          // 返回活跃警报包括：
          // - 事件类型
          // - 受影响区域
          // - 严重程度
          // - 描述
          // - 安全指示
      }

      // ......
    }
    ```

    `@Service`注解会自动在应用上下文中注册服务。
    Spring AI的`@Tool`注解，使得创建和维护MCP工具变得容易。

    自动配置会自动将这些工具注册到MCP服务器。

    ### 创建Boot应用

    ```java
    @SpringBootApplication
    public class McpServerApplication {

    	public static void main(String[] args) {
    		SpringApplication.run(McpServerApplication.class, args);
    	}

    	@Bean
    	public ToolCallbackProvider weatherTools(WeatherService weatherService) {
    		return  MethodToolCallbackProvider.builder().toolObjects(weatherService).build();
    	}
    }
    ```

    使用`MethodToolCallbackProvider`工具将`@Tools`转换为MCP服务器使用的可操作回调。

    ### 运行服务器

    最后，构建服务器：

    ```bash
    ./mvnw clean install
    ```

    这将在`target`文件夹中生成一个`mcp-weather-stdio-server-0.0.1-SNAPSHOT.jar`文件。

    现在让我们从现有的MCP主机Claude桌面版测试您的服务器。

    ## 使用Claude桌面版测试您的服务器

    <Note>
      Claude桌面版尚未在Linux上可用。
    </Note>

    首先，确保您已安装Claude桌面版。
    [您可以在此处安装最新版本。](https://claude.ai/download)如果您已经安装了Claude桌面版，请确保它是最新版本。

    我们需要为要使用的MCP服务器配置Claude桌面版。
    为此，在文本编辑器中打开Claude桌面版应用配置`~/Library/Application Support/Claude/claude_desktop_config.json`。
如果文件不存在，请确保创建它。

    例如，如果您安装了[VS Code](https://code.visualstudio.com/)：

    <Tabs>
      <Tab title="MacOS/Linux">
        ```bash
        code ~/Library/Application\ Support/Claude/claude_desktop_config.json
        ```
      </Tab>

      <Tab title="Windows">
        ```powershell
        code $env:AppData\Claude\claude_desktop_config.json
        ```
      </Tab>
    </Tabs>

    然后您将在`mcpServers`键中添加您的服务器。
    只有在至少正确配置了一个服务器时，MCP UI元素才会显示在Claude桌面版中。

    在本例中，我们将像这样添加我们的单个天气服务器：

    <Tabs>
      <Tab title="MacOS/Linux">
        ```json java
        {
          "mcpServers": {
            "spring-ai-mcp-weather": {
              "command": "java",
              "args": [
                "-Dspring.ai.mcp.server.stdio=true",
                "-jar",
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/mcp-weather-stdio-server-0.0.1-SNAPSHOT.jar"
              ]
            }
          }
        }
        ```
      </Tab>

      <Tab title="Windows">
        ```json java
        {
          "mcpServers": {
            "spring-ai-mcp-weather": {
              "command": "java",
              "args": [
                "-Dspring.ai.mcp.server.transport=STDIO",
                "-jar",
                "C:\\ABSOLUTE\\PATH\\TO\\PARENT\\FOLDER\\weather\\mcp-weather-stdio-server-0.0.1-SNAPSHOT.jar"
              ]
            }
          }
        }
        ```
      </Tab>
    </Tabs>

    <Note>
      确保传入服务器的绝对路径。
    </Note>

    这告诉Claude桌面版：

    1. 有一个名为"my-weather-server"的MCP服务器
    2. 通过运行`java -jar /ABSOLUTE/PATH/TO/PARENT/FOLDER/mcp-weather-stdio-server-0.0.1-SNAPSHOT.jar`启动它

    保存文件，并重启Claude桌面版。

    ## 使用Java客户端测试您的服务器

    ### 手动创建MCP客户端

    使用`McpClient`连接到服务器：

    ```java
    var stdioParams = ServerParameters.builder("java")
      .args("-jar", "/ABSOLUTE/PATH/TO/PARENT/FOLDER/mcp-weather-stdio-server-0.0.1-SNAPSHOT.jar")
      .build();

    var stdioTransport = new StdioClientTransport(stdioParams);

    var mcpClient = McpClient.sync(stdioTransport).build();

    mcpClient.initialize();

    ListToolsResult toolsList = mcpClient.listTools();

    CallToolResult weather = mcpClient.callTool(
      new CallToolRequest("getWeatherForecastByLocation",
          Map.of("latitude", "47.6062", "longitude", "-122.3321")));

    CallToolResult alert = mcpClient.callTool(
      new CallToolRequest("getAlerts", Map.of("state", "NY")));

    mcpClient.closeGracefully();
    ```

    ### 使用MCP客户端Boot Starter

    使用`spring-ai-starter-mcp-client`依赖创建一个新的boot starter应用：

    ```xml
    <dependency>
        <groupId>org.springframework.ai</groupId>
        <artifactId>spring-ai-starter-mcp-client</artifactId>
    </dependency>
    ```

    并设置`spring.ai.mcp.client.stdio.servers-configuration`属性指向您的`claude_desktop_config.json`。
    您可以重用现有的Anthropic桌面配置：

    ```properties
    spring.ai.mcp.client.stdio.servers-configuration=file:PATH/TO/claude_desktop_config.json
    ```

    当您启动客户端应用时，自动配置将从claude_desktop_config.json自动创建MCP客户端。

    更多信息，请参阅[MCP客户端Boot Starters](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-client-docs.html)参考文档。

    ## 更多Java MCP服务器示例

    [starter-webflux-server](https://github.com/spring-projects/spring-ai-examples/tree/main/model-context-protocol/weather/starter-webflux-server)演示了如何使用SSE传输创建MCP服务器。
    它展示了如何利用Spring Boot的自动配置能力定义和注册MCP工具、资源和提示。
  </Tab>

  <Tab title="Kotlin">
    让我们开始构建我们的天气服务器！[您可以在此处找到我们将构建的完整代码。](https://github.com/modelcontextprotocol/kotlin-sdk/tree/main/samples/weather-stdio-server)

    ### 先决知识

    本快速入门假设您熟悉：

    * Kotlin
    * 像Claude这样的LLM

    ### 系统要求

    * 已安装Java 17或更高版本

    ### 设置环境

    首先，如果您还没有安装`java`和`gradle`，让我们安装它们。
    您可以从[官方Oracle JDK网站](https://www.oracle.com/java/technologies/downloads/)下载`java`。
    验证您的`java`安装：

    ```bash
    java --version
    ```

    现在，让我们创建并设置您的项目：

    <CodeGroup>
      ```bash MacOS/Linux
      # 为我们的项目创建新目录
      mkdir weather
      cd weather

      # 初始化新的kotlin项目
      gradle init
      ```

      ```powershell Windows
      # 为我们的项目创建新目录
      md weather
      cd weather

      # 初始化新的kotlin项目
      gradle init
      ```
    </CodeGroup>

    运行`gradle init`后，您将看到创建项目的选项。
    选择**Application**作为项目类型，**Kotlin**作为编程语言，**Java 17**作为Java版本。

    或者，您可以使用[IntelliJ IDEA项目向导](https://kotlinlang.org/docs/jvm-get-started.html)创建Kotlin应用。

    创建项目后，添加以下依赖：

    <CodeGroup>
      ```kotlin build.gradle.kts
      val mcpVersion = "0.4.0"
      val slf4jVersion = "2.0.9"
      val ktorVersion = "3.1.1"

      dependencies {
implementation("io.modelcontextprotocol:kotlin-sdk:$mcpVersion")
          implementation("org.slf4j:slf4j-nop:$slf4jVersion")
          implementation("io.ktor:ktor-client-content-negotiation:$ktorVersion")
          implementation("io.ktor:ktor-serialization-kotlinx-json:$ktorVersion")
      }
      ```

      ```groovy build.gradle
      def mcpVersion = '0.3.0'
      def slf4jVersion = '2.0.9'
      def ktorVersion = '3.1.1'

      dependencies {
          implementation "io.modelcontextprotocol:kotlin-sdk:$mcpVersion"
          implementation "org.slf4j:slf4j-nop:$slf4jVersion"
          implementation "io.ktor:ktor-client-content-negotiation:$ktorVersion"
          implementation "io.ktor:ktor-serialization-kotlinx-json:$ktorVersion"
      }
      ```
    </CodeGroup>

    同时，在构建脚本中添加以下插件：

    <CodeGroup>
      ```kotlin build.gradle.kts
      plugins {
          kotlin("plugin.serialization") version "your_version_of_kotlin"
          id("com.github.johnrengelman.shadow") version "8.1.1"
      }
      ```

      ```groovy build.gradle
      plugins {
          id 'org.jetbrains.kotlin.plugin.serialization' version 'your_version_of_kotlin'
          id 'com.github.johnrengelman.shadow' version '8.1.1'
      }
      ```
    </CodeGroup>

    现在让我们深入构建您的服务器。

    ## 构建您的服务器

    ### 设置实例

    添加服务器初始化函数：

    ```kotlin
    // 运行MCP服务器的主函数
    fun `run mcp server`() {
        // 创建带有基本实现的MCP服务器实例
        val server = Server(
            Implementation(
                name = "weather", // 工具名称为"weather"
                version = "1.0.0" // 实现版本
            ),
            ServerOptions(
                capabilities = ServerCapabilities(tools = ServerCapabilities.Tools(listChanged = true))
            )
        )

        // 使用标准IO创建服务器通信传输
        val transport = StdioServerTransport(
            System.`in`.asInput(),
            System.out.asSink().buffered()
        )

        runBlocking {
            server.connect(transport)
            val done = Job()
            server.onClose {
                done.complete()
            }
            done.join()
        }
    }
    ```

    ### 天气API辅助函数

    接下来，添加用于查询和转换国家气象局API响应的函数和数据类：

    ```kotlin
    // 扩展函数，获取给定经纬度的预测信息
    suspend fun HttpClient.getForecast(latitude: Double, longitude: Double): List<String> {
        val points = this.get("/points/$latitude,$longitude").body<Points>()
        val forecast = this.get(points.properties.forecast).body<Forecast>()
        return forecast.properties.periods.map { period ->
            """
                ${period.name}:
                温度: ${period.temperature} ${period.temperatureUnit}
                风速: ${period.windSpeed} ${period.windDirection}
                预测: ${period.detailedForecast}
            """.trimIndent()
        }
    }

    // 扩展函数，获取给定州的天气警报
    suspend fun HttpClient.getAlerts(state: String): List<String> {
        val alerts = this.get("/alerts/active/area/$state").body<Alert>()
        return alerts.features.map { feature ->
            """
                事件: ${feature.properties.event}
                区域: ${feature.properties.areaDesc}
                严重程度: ${feature.properties.severity}
                描述: ${feature.properties.description}
                指示: ${feature.properties.instruction}
            """.trimIndent()
        }
    }

    @Serializable
    data class Points(
        val properties: Properties
    ) {
        @Serializable
        data class Properties(val forecast: String)
    }

    @Serializable
    data class Forecast(
        val properties: Properties
    ) {
        @Serializable
        data class Properties(val periods: List<Period>)

        @Serializable
        data class Period(
            val number: Int, val name: String, val startTime: String, val endTime: String,
            val isDaytime: Boolean, val temperature: Int, val temperatureUnit: String,
            val temperatureTrend: String, val probabilityOfPrecipitation: JsonObject,
            val windSpeed: String, val windDirection: String,
            val shortForecast: String, val detailedForecast: String,
        )
    }

    @Serializable
    data class Alert(
        val features: List<Feature>
    ) {
        @Serializable
        data class Feature(
            val properties: Properties
        )

        @Serializable
        data class Properties(
            val event: String, val areaDesc: String, val severity: String,
            val description: String, val instruction: String?,
        )
    }
    ```

    ### 实现工具执行

    工具执行处理程序负责实际执行每个工具的逻辑。让我们添加它：

    ```kotlin
    // 创建带有默认请求配置和JSON内容协商的HTTP客户端
    val httpClient = HttpClient {
        defaultRequest {
            url("https://api.weather.gov")
            headers {
                append("Accept", "application/geo+json")
                append("User-Agent", "WeatherApiClient/1.0")
            }
            contentType(ContentType.Application.Json)
        }
        // 安装用于JSON序列化/反序列化的内容协商插件
        install(ContentNegotiation) { json(Json { ignoreUnknownKeys = true }) }
    }

    // 注册按州获取天气警报的工具
    server.addTool(
        name = "get_alerts",
        description = """
            获取美国州的天气警报。输入是两字母美国州代码(如CA, NY)
        """.trimIndent(),
        inputSchema = Tool.Input(
            properties = buildJsonObject {
                putJsonObject("state") {
                    put("type", "string")
                    put("description", "两字母美国州代码(如CA, NY)")
                }
            },
            required = listOf("state")
        )
) { request ->
        val state = request.arguments["state"]?.jsonPrimitive?.content
        if (state == null) {
            return@addTool CallToolResult(
                content = listOf(TextContent("必须提供'state'参数"))
            )
        }

        val alerts = httpClient.getAlerts(state)

        CallToolResult(content = alerts.map { TextContent(it) })
    }

    // 注册按经纬度获取天气预报的工具
    server.addTool(
        name = "get_forecast",
        description = """
            获取特定经纬度的天气预报
        """.trimIndent(),
        inputSchema = Tool.Input(
            properties = buildJsonObject {
                putJsonObject("latitude") { put("type", "number") }
                putJsonObject("longitude") { put("type", "number") }
            },
            required = listOf("latitude", "longitude")
        )
    ) { request ->
        val latitude = request.arguments["latitude"]?.jsonPrimitive?.doubleOrNull
        val longitude = request.arguments["longitude"]?.jsonPrimitive?.doubleOrNull
        if (latitude == null || longitude == null) {
            return@addTool CallToolResult(
                content = listOf(TextContent("必须提供'latitude'和'longitude'参数"))
            )
        }

        val forecast = httpClient.getForecast(latitude, longitude)

        CallToolResult(content = forecast.map { TextContent(it) })
    }
    ```

    ### 运行服务器

    最后，实现主函数来运行服务器：

    ```kotlin
    fun main() = `run mcp server`()
    ```

    确保运行`./gradlew build`来构建您的服务器。这是让服务器成功连接的重要步骤。

    现在让我们从现有的MCP主机Claude桌面版测试您的服务器。

    ## 使用Claude桌面版测试您的服务器

    <Note>
      Claude桌面版尚未在Linux上可用。Linux用户可以继续学习[构建客户端](/quickstart/client)教程，构建一个连接到我们刚创建的MCP服务器的客户端。
    </Note>

    首先，确保您已安装Claude桌面版。[您可以在此处安装最新版本](https://claude.ai/download)。如果您已经安装了Claude桌面版，请确保它是最新版本。

    我们需要为要使用的MCP服务器配置Claude桌面版。
    为此，在文本编辑器中打开Claude桌面版应用配置`~/Library/Application Support/Claude/claude_desktop_config.json`。
    如果文件不存在，请确保创建它。

    例如，如果您安装了[VS Code](https://code.visualstudio.com/)：

    <CodeGroup>
      ```bash MacOS/Linux
      code ~/Library/Application\ Support/Claude/claude_desktop_config.json
      ```

      ```powershell Windows
      code $env:AppData\Claude\claude_desktop_config.json
      ```
    </CodeGroup>

    然后您将在`mcpServers`键中添加您的服务器。
    只有在至少正确配置了一个服务器时，MCP UI元素才会显示在Claude桌面版中。

    在本例中，我们将像这样添加我们的单个天气服务器：

    <CodeGroup>
      ```json MacOS/Linux
      {
          "mcpServers": {
              "weather": {
                  "command": "java",
                  "args": [
                      "-jar",
                      "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather/build/libs/weather-0.1.0-all.jar"
                  ]
              }
          }
      }
      ```

      ```json Windows
      {
          "mcpServers": {
              "weather": {
                  "command": "java",
                  "args": [
                      "-jar",
                      "C:\\PATH\\TO\\PARENT\\FOLDER\\weather\\build\\libs\\weather-0.1.0-all.jar"
                  ]
              }
          }
      }
      ```
    </CodeGroup>

    这告诉Claude桌面版：

    1. 有一个名为"weather"的MCP服务器
    2. 通过运行`java -jar /ABSOLUTE/PATH/TO/PARENT/FOLDER/weather/build/libs/weather-0.1.0-all.jar`启动它

    保存文件，并重启Claude桌面版。
  </Tab>

  <Tab title="C#">
    让我们开始构建我们的天气服务器！[您可以在此处找到我们将构建的完整代码](https://github.com/modelcontextprotocol/csharp-sdk/tree/main/samples/QuickstartWeatherServer)

    ### 先决知识

    本快速入门假设您熟悉：

    * C#
    * 像Claude这样的LLM
    * .NET 8或更高版本

    ### 系统要求

    * 已安装[.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0)或更高版本

    ### 设置环境

    首先，如果您还没有安装`dotnet`，让我们安装它。您可以从[官方Microsoft .NET网站](https://dotnet.microsoft.com/download/)下载`dotnet`。验证您的`dotnet`安装：

    ```bash
    dotnet --version
    ```

    现在，让我们创建并设置您的项目：

    <CodeGroup>
      ```bash MacOS/Linux
      # 为我们的项目创建新目录
      mkdir weather
      cd weather
      # 初始化新的C#项目
      dotnet new console
      ```

      ```powershell Windows
      # 为我们的项目创建新目录
      mkdir weather
      cd weather
      # 初始化新的C#项目
      dotnet new console
      ```
    </CodeGroup>

    运行`dotnet new console`后，您将获得一个新的C#项目。
    您可以在您喜欢的IDE中打开项目，如[Visual Studio](https://visualstudio.microsoft.com/)或[Rider](https://www.jetbrains.com/rider/)。
    或者，您可以使用[Visual Studio项目向导](https://learn.microsoft.com/en-us/visualstudio/get-started/csharp/tutorial-console?view=vs-2022)创建C#应用。
    创建项目后，添加Model Context Protocol SDK和hosting的NuGet包：

    ```bash
    # 添加Model Context Protocol SDK NuGet包
    dotnet add package ModelContextProtocol --prerelease
    # 添加.NET Hosting NuGet包
    dotnet add package Microsoft.Extensions.Hosting
    ```

    现在让我们深入构建您的服务器。

    ## 构建您的服务器

    打开项目中的`Program.cs`文件，并将其内容替换为以下代码：

    ```csharp
    using Microsoft.Extensions.DependencyInjection;
    using Microsoft.Extensions.Hosting;
    using ModelContextProtocol;
    using System.Net.Http.Headers;
var builder = Host.CreateEmptyApplicationBuilder(settings: null);

    builder.Services.AddMcpServer()
        .WithStdioServerTransport()
        .WithToolsFromAssembly();

    builder.Services.AddSingleton(_ =>
    {
        var client = new HttpClient() { BaseAddress = new Uri("https://api.weather.gov") };
        client.DefaultRequestHeaders.UserAgent.Add(new ProductInfoHeaderValue("weather-tool", "1.0"));
        return client;
    });

    var app = builder.Build();

    await app.RunAsync();
    ```

    <Note>
      创建`ApplicationHostBuilder`时，确保使用`CreateEmptyApplicationBuilder`而不是`CreateDefaultBuilder`。这确保服务器不会向控制台写入任何额外消息。这仅适用于使用STDIO传输的服务器。
    </Note>

    这段代码设置了一个基本的控制台应用，使用Model Context Protocol SDK创建了一个带有标准I/O传输的MCP服务器。

    ### 天气API辅助函数

    接下来，定义一个包含工具执行处理程序的类，用于查询和转换国家气象局API的响应：

    ```csharp
    using ModelContextProtocol.Server;
    using System.ComponentModel;
    using System.Net.Http.Json;
    using System.Text.Json;

    namespace QuickstartWeatherServer.Tools;

    [McpServerToolType]
    public static class WeatherTools
    {
        [McpServerTool, Description("获取美国州的天气警报。")]
        public static async Task<string> GetAlerts(
            HttpClient client,
            [Description("要获取警报的美国州。")] string state)
        {
            var jsonElement = await client.GetFromJsonAsync<JsonElement>($"/alerts/active/area/{state}");
            var alerts = jsonElement.GetProperty("features").EnumerateArray();

            if (!alerts.Any())
            {
                return "该州没有活跃警报。";
            }

            return string.Join("\n--\n", alerts.Select(alert =>
            {
                JsonElement properties = alert.GetProperty("properties");
                return $"""
                        事件: {properties.GetProperty("event").GetString()}
                        区域: {properties.GetProperty("areaDesc").GetString()}
                        严重程度: {properties.GetProperty("severity").GetString()}
                        描述: {properties.GetProperty("description").GetString()}
                        指示: {properties.GetProperty("instruction").GetString()}
                        """;
            }));
        }

        [McpServerTool, Description("获取位置的天气预报。")]
        public static async Task<string> GetForecast(
            HttpClient client,
            [Description("位置的纬度。")] double latitude,
            [Description("位置的经度。")] double longitude)
        {
            var jsonElement = await client.GetFromJsonAsync<JsonElement>($"/points/{latitude},{longitude}");
            var periods = jsonElement.GetProperty("properties").GetProperty("periods").EnumerateArray();

            return string.Join("\n---\n", periods.Select(period => $"""
                    {period.GetProperty("name").GetString()}
                    温度: {period.GetProperty("temperature").GetInt32()}°F
                    风速: {period.GetProperty("windSpeed").GetString()} {period.GetProperty("windDirection").GetString()}
                    预测: {period.GetProperty("detailedForecast").GetString()}
                    """));
        }
    }
    ```

    ### 运行服务器

    最后，使用以下命令运行服务器：

    ```bash
    dotnet run
    ```

    这将启动服务器并在标准输入/输出上监听传入请求。

    ## 使用Claude桌面版测试您的服务器

    <Note>
      Claude桌面版尚未在Linux上可用。Linux用户可以继续学习[构建客户端](/quickstart/client)教程，构建一个连接到我们刚创建的MCP服务器的客户端。
    </Note>

    首先，确保您已安装Claude桌面版。[您可以在此处安装最新版本](https://claude.ai/download)。如果您已经安装了Claude桌面版，请确保它是最新版本。
    我们需要为要使用的MCP服务器配置Claude桌面版。为此，在文本编辑器中打开Claude桌面版应用配置`~/Library/Application Support/Claude/claude_desktop_config.json`。如果文件不存在，请确保创建它。
    例如，如果您安装了[VS Code](https://code.visualstudio.com/)：

    <Tabs>
      <Tab title="MacOS/Linux">
        ```bash
        code ~/Library/Application\ Support/Claude/claude_desktop_config.json
        ```
      </Tab>

      <Tab title="Windows">
        ```powershell
        code $env:AppData\Claude\claude_desktop_config.json
        ```
      </Tab>
    </Tabs>

    然后您将在`mcpServers`键中添加您的服务器。只有在至少正确配置了一个服务器时，MCP UI元素才会显示在Claude桌面版中。
    在本例中，我们将像这样添加我们的单个天气服务器：

    <Tabs>
      <Tab title="MacOS/Linux">
        ```json
        {
            "mcpServers": {
                "weather": {
                    "command": "dotnet",
                    "args": [
                        "run",
                        "--project",
                        "/ABSOLUTE/PATH/TO/PROJECT",
                        "--no-build"
                    ]
                }
            }
        }
        ```
      </Tab>

      <Tab title="Windows">
        ```json
        {
            "mcpServers": {
                "weather": {
                    "command": "dotnet",
                    "args": [
                        "run",
                        "--project",
                        "C:\\ABSOLUTE\\PATH\\TO\\PROJECT",
                        "--no-build"
                    ]
                }
            }
        }
        ```
      </Tab>
    </Tabs>

    这告诉Claude桌面版：

    1. 有一个名为"weather"的MCP服务器
    2. 通过运行`dotnet run /ABSOLUTE/PATH/TO/PROJECT`启动它
       保存文件，并重启Claude桌面版。
  </Tab>
</Tabs>

### 使用命令测试

让我们确保Claude桌面版能识别我们在`weather`服务器中暴露的两个工具。您可以通过查找锤子图标 <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/claude-desktop-mcp-hammer-icon.svg" style={{display: 'inline', margin: 0, height: '1.3em'}} /> 来确认：

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/visual-indicator-mcp-tools.png" />
</Frame>

点击锤子图标后，您应该看到列出的两个工具：

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/available-mcp-tools.png" />
</Frame>

如果您的服务器没有被Claude桌面版识别，请转到[故障排除](#troubleshooting)部分获取调试提示。

如果锤子图标已经显示，您现在可以通过在Claude桌面版中运行以下命令来测试您的服务器：
* 萨克拉门托的天气如何？
* 德克萨斯州有哪些活跃的天气警报？

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/current-weather.png" />
</Frame>

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/weather-alerts.png" />
</Frame>

<Note>
  由于这是美国国家气象局服务，查询仅适用于美国境内位置。
</Note>

## 底层工作原理

当您提问时：

1. 客户端将您的问题发送给Claude
2. Claude分析可用工具并决定使用哪个(些)工具
3. 客户端通过MCP服务器执行选定的工具
4. 结果返回给Claude
5. Claude组织自然语言响应
6. 响应显示给您！

## 故障排除

<AccordionGroup>
  <Accordion title="Claude桌面版集成问题">
    **获取Claude桌面版日志**

    Claude.app中与MCP相关的日志写入到`~/Library/Logs/Claude`中的日志文件：

    * `mcp.log`包含MCP连接和连接失败的一般日志
    * 名为`mcp-server-SERVERNAME.log`的文件将包含来自指定服务器的错误(stderr)日志

    您可以运行以下命令查看最近的日志并跟踪任何新日志：

    ```bash
    # 检查Claude日志中的错误
    tail -n 20 -f ~/Library/Logs/Claude/mcp*.log
    ```

    **服务器未在Claude中显示**

    1. 检查您的`claude_desktop_config.json`文件语法
    2. 确保项目路径是绝对路径而非相对路径
    3. 完全重启Claude桌面版

    **工具调用静默失败**

    如果Claude尝试使用工具但失败：

    1. 检查Claude日志中的错误
    2. 验证您的服务器构建和运行无错误
    3. 尝试重启Claude桌面版

    **这些都不起作用。我该怎么办？**

    请参考我们的[调试指南](/docs/tools/debugging)获取更好的调试工具和更详细的指导。
  </Accordion>

  <Accordion title="天气API问题">
    **错误：无法获取网格点数据**

    这通常意味着：

    1. 坐标在美国境外
    2. NWS API出现问题
    3. 您被限速

    解决方法：

    * 确认您使用的是美国坐标
    * 在请求之间添加小延迟
    * 检查NWS API状态页面

    **错误：[州]没有活跃警报**

    这不是错误 - 只是表示该州当前没有天气警报。尝试不同的州或在恶劣天气时检查。
  </Accordion>
</AccordionGroup>

<Note>
  如需更高级的故障排除，请查看我们的[调试MCP](/docs/tools/debugging)指南
</Note>

## 下一步

<CardGroup cols={2}>
  <Card title="构建客户端" icon="outlet" href="/quickstart/client">
    学习如何构建自己的MCP客户端连接到您的服务器
  </Card>

  <Card title="示例服务器" icon="grid" href="/examples">
    查看我们官方MCP服务器和实现的图库
  </Card>

  <Card title="调试指南" icon="bug" href="/docs/tools/debugging">
    学习如何有效调试MCP服务器和集成
  </Card>

  <Card title="使用LLM构建MCP" icon="comments" href="/tutorials/building-mcp-with-llms">
    学习如何使用Claude等LLM加速您的MCP开发
  </Card>
</CardGroup>


# 给Claude桌面版用户
来源：https://modelcontextprotocol.io/quickstart/user

开始使用预构建的服务器扩展Claude桌面版功能。

在本教程中，您将扩展[Claude桌面版](https://claude.ai/download)，使其能够读取计算机文件系统、写入新文件、移动文件甚至搜索文件。

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-filesystem.png" />
</Frame>

别担心 - 在执行这些操作前会征求您的许可！

## 1. 下载Claude桌面版

首先下载[Claude桌面版](https://claude.ai/download)，选择macOS或Windows版本。(Linux目前不支持Claude桌面版。)

按照安装说明操作。

如果您已经安装了Claude桌面版，请确保是最新版本 - 点击电脑上的Claude菜单并选择"检查更新..."

<Accordion title="为什么用Claude桌面版而不是Claude.ai？">
  因为服务器是本地运行的，MCP目前仅支持桌面主机。远程主机正在积极开发中。
</Accordion>

## 2. 添加文件系统MCP服务器

要添加此文件系统功能，我们将安装一个预构建的[文件系统MCP服务器](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)到Claude桌面版。这是Anthropic和社区创建的数十个[服务器](https://github.com/modelcontextprotocol/servers/tree/main)之一。

首先打开电脑上的Claude菜单并选择"设置..."请注意这不是应用窗口中的Claude账户设置。

在Mac上应该是这样的：

<Frame style={{ textAlign: 'center' }}>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-menu.png" width="400" />
</Frame>

点击设置面板左侧栏中的"开发者"，然后点击"编辑配置"：

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-developer.png" />
</Frame>

这将创建一个配置文件在：

* macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
* Windows: `%APPDATA%\Claude\claude_desktop_config.json`

如果文件不存在，并会在文件系统中显示该文件。

在任何文本编辑器中打开配置文件。将文件内容替换为：

<Tabs>
  <Tab title="MacOS/Linux">
    ```json
    {
      "mcpServers": {
        "filesystem": {
          "command": "npx",
          "args": [
            "-y",
            "@modelcontextprotocol/server-filesystem",
            "/Users/username/Desktop",
            "/Users/username/Downloads"
          ]
        }
      }
    }
    ```
  </Tab>

  <Tab title="Windows">
    ```json
    {
      "mcpServers": {
        "filesystem": {
          "command": "npx",
          "args": [
"-y",
            "@modelcontextprotocol/server-filesystem",
            "C:\\Users\\username\\Desktop",
            "C:\\Users\\username\\Downloads"
          ]
        }
      }
    }
    ```
  </Tab>
</Tabs>

请确保将`username`替换为您电脑的用户名。路径应指向您希望Claude能够访问和修改的有效目录。这里设置为桌面和下载目录，但您也可以添加更多路径。

您还需要在电脑上安装[Node.js](https://nodejs.org)才能正常运行。要验证是否安装了Node，请打开电脑上的命令行：

* 在macOS上，从应用程序文件夹打开终端
* 在Windows上，按Windows + R，输入"cmd"，然后按Enter

进入命令行后，输入以下命令验证是否安装了Node：

```bash
node --version
```

如果出现"command not found"或"node is not recognized"错误，请从[nodejs.org](https://nodejs.org/)下载Node。

<Tip>
  **配置文件如何工作？**

  此配置文件告诉Claude桌面版每次启动应用时要启动哪些MCP服务器。在本例中，我们添加了一个名为"filesystem"的服务器，它将使用Node的`npx`命令安装并运行`@modelcontextprotocol/server-filesystem`。这个服务器(描述见[此处](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem))将允许您在Claude桌面版中访问文件系统。
</Tip>

<Warning>
  **命令权限**

  Claude桌面版将以您用户账户的权限运行配置文件中的命令，并访问您的本地文件。只有在理解并信任来源时才添加命令。
</Warning>

## 3. 重启Claude

更新配置文件后，您需要重启Claude桌面版。

重启后，您应该会在输入框右下角看到一个锤子图标 <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/claude-desktop-mcp-hammer-icon.svg" style={{display: 'inline', margin: 0, height: '1.3em'}} />：

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-hammer.png" />
</Frame>

点击锤子图标后，您应该会看到文件系统MCP服务器附带的工具：

<Frame style={{ textAlign: 'center' }}>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-tools.png" width="400" />
</Frame>

如果您的服务器未被Claude桌面版识别，请转到[故障排除](#troubleshooting)部分获取调试提示。

## 4. 试试看！

您现在可以与Claude交谈并询问有关文件系统的问题。它应该知道何时调用相关工具。

您可以尝试询问Claude：

* 你能写一首诗并保存到我的桌面吗？
* 我的下载文件夹中有哪些与工作相关的文件？
* 你能把我桌面上的所有图片移动到一个名为"图片"的新文件夹吗？

根据需要，Claude将调用相关工具并在采取行动前征求您的同意：

<Frame style={{ textAlign: 'center' }}>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-approve.png" width="500" />
</Frame>

## 故障排除

<AccordionGroup>
  <Accordion title="服务器未在Claude中显示/锤子图标缺失">
    1. 完全重启Claude桌面版
    2. 检查您的`claude_desktop_config.json`文件语法
    3. 确保`claude_desktop_config.json`中包含的文件路径有效且为绝对路径而非相对路径
    4. 查看[日志](#getting-logs-from-claude-for-desktop)了解服务器为何无法连接
    5. 在命令行中尝试手动运行服务器(替换`username`如您在`claude_desktop_config.json`中所做)，查看是否有错误：

    <Tabs>
      <Tab title="MacOS/Linux">
        ```bash
        npx -y @modelcontextprotocol/server-filesystem /Users/username/Desktop /Users/username/Downloads
        ```
      </Tab>

      <Tab title="Windows">
        ```bash
        npx -y @modelcontextprotocol/server-filesystem C:\Users\username\Desktop C:\Users\username\Downloads
        ```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="获取Claude桌面版日志">
    Claude.app中与MCP相关的日志写入到：

    * macOS: `~/Library/Logs/Claude`

    * Windows: `%APPDATA%\Claude\logs`

    * `mcp.log`将包含关于MCP连接和连接失败的一般日志

    * 名为`mcp-server-SERVERNAME.log`的文件将包含来自指定服务器的错误(stderr)日志

    您可以运行以下命令查看最近的日志并跟踪任何新日志(在Windows上仅显示最近的日志)：

    <Tabs>
      <Tab title="MacOS/Linux">
        ```bash
        # 检查Claude日志中的错误
        tail -n 20 -f ~/Library/Logs/Claude/mcp*.log
        ```
      </Tab>

      <Tab title="Windows">
        ```bash
        type "%APPDATA%\Claude\logs\mcp*.log"
        ```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="工具调用静默失败">
    如果Claude尝试使用工具但失败：

    1. 检查Claude日志中的错误
    2. 验证您的服务器构建和运行无错误
    3. 尝试重启Claude桌面版
  </Accordion>

  <Accordion title="这些都不起作用。我该怎么办？">
    请参考我们的[调试指南](/docs/tools/debugging)获取更好的调试工具和更详细的指导。
  </Accordion>

  <Accordion title="Windows上出现ENOENT错误和路径中的`${APPDATA}`">
    如果配置的服务器加载失败，并且在其日志中看到路径中引用`${APPDATA}`的错误，您可能需要在`claude_desktop_config.json`的`env`键中添加`%APPDATA%`的扩展值：

    ```json
    {
      "brave-search": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-brave-search"],
        "env": {
          "APPDATA": "C:\\Users\\user\\AppData\\Roaming\\",
          "BRAVE_API_KEY": "..."
        }
      }
    }
    ```

    进行此更改后，再次启动Claude桌面版。

    <Warning>
      **NPM应全局安装**

      如果尚未全局安装NPM，`npx`命令可能会继续失败。如果NPM已全局安装，您将在系统上找到`%APPDATA%\npm`。如果没有，可以通过运行以下命令全局安装NPM：

      ```bash
      npm install -g npm
      ```
    </Warning>
  </Accordion>
</AccordionGroup>

## 下一步

<CardGroup cols={2}>
  <Card title="探索其他服务器" icon="grid" href="/examples">
    查看我们官方MCP服务器和实现的图库
  </Card>

  <Card title="构建自己的服务器" icon="code" href="/quickstart/server">
    现在构建您自己的自定义服务器以在Claude桌面版和其他客户端中使用
  </Card>
</CardGroup>


# MCP客户端
来源：https://modelcontextprotocol.io/sdk/java/mcp-client

学习如何使用Model Context Protocol(MCP)客户端与MCP服务器交互
# Model Context Protocol 客户端

MCP客户端是Model Context Protocol(MCP)架构中的关键组件，负责建立和管理与MCP服务器的连接。它实现了协议的客户端部分，处理：

* 协议版本协商以确保与服务器的兼容性
* 能力协商以确定可用功能
* 消息传输和JSON-RPC通信
* 工具发现和执行
* 资源访问和管理
* 提示系统交互
* 可选功能如roots管理和采样支持

<Tip>
  核心`io.modelcontextprotocol.sdk:mcp`模块提供了STDIO和SSE客户端传输实现，无需外部Web框架。

  Spring特定的传输实现作为**可选**依赖`io.modelcontextprotocol.sdk:mcp-spring-webflux`提供给[Spring Framework](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-client-boot-starter-docs.html)用户。
</Tip>

客户端提供同步和异步API以适应不同的应用场景。

<Tabs>
  <Tab title="同步API">
    ```java
    // 创建带有自定义配置的同步客户端
    McpSyncClient client = McpClient.sync(transport)
        .requestTimeout(Duration.ofSeconds(10))
        .capabilities(ClientCapabilities.builder()
            .roots(true)      // 启用roots能力
            .sampling()       // 启用采样能力
            .build())
        .sampling(request -> new CreateMessageResult(response))
        .build();

    // 初始化连接
    client.initialize();

    // 列出可用工具
    ListToolsResult tools = client.listTools();

    // 调用工具
    CallToolResult result = client.callTool(
        new CallToolRequest("calculator", 
            Map.of("operation", "add", "a", 2, "b", 3))
    );

    // 列出和读取资源
    ListResourcesResult resources = client.listResources();
    ReadResourceResult resource = client.readResource(
        new ReadResourceRequest("resource://uri")
    );

    // 列出和使用提示
    ListPromptsResult prompts = client.listPrompts();
    GetPromptResult prompt = client.getPrompt(
        new GetPromptRequest("greeting", Map.of("name", "Spring"))
    );

    // 添加/移除roots
    client.addRoot(new Root("file:///path", "description"));
    client.removeRoot("file:///path");

    // 关闭客户端
    client.closeGracefully();
    ```
  </Tab>

  <Tab title="异步API">
    ```java
    // 创建带有自定义配置的异步客户端
    McpAsyncClient client = McpClient.async(transport)
        .requestTimeout(Duration.ofSeconds(10))
        .capabilities(ClientCapabilities.builder()
            .roots(true)      // 启用roots能力
            .sampling()       // 启用采样能力
            .build())
        .sampling(request -> Mono.just(new CreateMessageResult(response)))
        .toolsChangeConsumer(tools -> Mono.fromRunnable(() -> {
            logger.info("工具更新: {}", tools);
        }))
        .resourcesChangeConsumer(resources -> Mono.fromRunnable(() -> {
            logger.info("资源更新: {}", resources);
        }))
        .promptsChangeConsumer(prompts -> Mono.fromRunnable(() -> {
            logger.info("提示更新: {}", prompts);
        }))
        .build();

    // 初始化连接并使用功能
    client.initialize()
        .flatMap(initResult -> client.listTools())
        .flatMap(tools -> {
            return client.callTool(new CallToolRequest(
                "calculator", 
                Map.of("operation", "add", "a", 2, "b", 3)
            ));
        })
        .flatMap(result -> {
            return client.listResources()
                .flatMap(resources -> 
                    client.readResource(new ReadResourceRequest("resource://uri"))
                );
        })
        .flatMap(resource -> {
            return client.listPrompts()
                .flatMap(prompts ->
                    client.getPrompt(new GetPromptRequest(
                        "greeting", 
                        Map.of("name", "Spring")
                    ))
                );
        })
        .flatMap(prompt -> {
            return client.addRoot(new Root("file:///path", "description"))
                .then(client.removeRoot("file:///path"));            
        })
        .doFinally(signalType -> {
            client.closeGracefully().subscribe();
        })
        .subscribe();
    ```
  </Tab>
</Tabs>

## 客户端传输

传输层处理MCP客户端和服务器之间的通信，为不同用例提供不同的实现。客户端传输管理消息序列化、连接建立和协议特定的通信模式。

<Tabs>
  <Tab title="STDIO">
    创建基于进程内通信的传输

    ```java
    ServerParameters params = ServerParameters.builder("npx")
        .args("-y", "@modelcontextprotocol/server-everything", "dir")
        .build();
    McpTransport transport = new StdioClientTransport(params);
    ```
  </Tab>

  <Tab title="SSE (HttpClient)">
    创建框架无关(纯Java API)的SSE客户端传输。包含在核心mcp模块中。

    ```java
    McpTransport transport = new HttpClientSseClientTransport("http://your-mcp-server");
    ```
  </Tab>

  <Tab title="SSE (WebFlux)">
    创建基于WebFlux的SSE客户端传输。需要mcp-webflux-sse-transport依赖。

    ```java
    WebClient.Builder webClientBuilder = WebClient.builder()
        .baseUrl("http://your-mcp-server");
    McpTransport transport = new WebFluxSseClientTransport(webClientBuilder);
    ```
  </Tab>
</Tabs>

## 客户端能力

客户端可以配置各种能力：

```java
var capabilities = ClientCapabilities.builder()
    .roots(true)      // 启用文件系统roots支持及列表变更通知
    .sampling()       // 启用LLM采样支持
    .build();
```

### Roots支持

Roots定义了服务器可以在文件系统中操作的边界：

```java
// 动态添加root
client.addRoot(new Root("file:///path", "description"));

// 移除root
client.removeRoot("file:///path");

// 通知服务器roots变更
client.rootsListChangedNotification();
```

roots能力允许服务器：

* 请求可访问的文件系统roots列表
* 接收roots列表变更通知
* 了解它们可以访问哪些目录和文件

### 采样支持

采样使服务器能够通过客户端请求LLM交互("补全"或"生成")：

```java
// 配置采样处理器
Function<CreateMessageRequest, CreateMessageResult> samplingHandler = request -> {
    // 与LLM交互的采样实现
    return new CreateMessageResult(response);
};

// 创建支持采样的客户端
var client = McpClient.sync(transport)
    .capabilities(ClientCapabilities.builder()
        .sampling()
        .build())
    .sampling(samplingHandler)
    .build();
```

此能力允许：

* 服务器无需API密钥即可利用AI能力
* 客户端保持对模型访问和权限的控制
* 支持基于文本和图像的交互
* 可选地在提示中包含MCP服务器上下文

### 日志支持

客户端可以注册日志消费者来接收来自服务器的日志消息，并设置最低日志级别来过滤消息：

```java
var mcpClient = McpClient.sync(transport)
        .loggingConsumer(notification -> {
            System.out.println("收到日志消息: " + notification.data());
        })
        .build();

mcpClient.initialize();

mcpClient.setLoggingLevel(McpSchema.LoggingLevel.INFO);

// 调用可以发送日志通知的工具
CallToolResult result = mcpClient.callTool(new McpSchema.CallToolRequest("logging-test", Map.of()));
```

客户端可以通过`mcpClient.setLoggingLevel(level)`请求控制接收的最低日志级别。低于设置级别的消息将被过滤掉。
支持的日志级别(按严重程度递增)：DEBUG (0), INFO (1), NOTICE (2), WARNING (3), ERROR (4), CRITICAL (5), ALERT (6), EMERGENCY (7)

## 使用MCP客户端

### 工具执行

工具是服务器端函数，客户端可以发现并执行它们。MCP客户端提供列出可用工具并使用特定参数执行它们的方法。每个工具都有唯一的名称并接受参数映射。

<Tabs>
  <Tab title="同步API">
    ```java
    // 列出可用工具及其名称
    var tools = client.listTools();
    tools.forEach(tool -> System.out.println(tool.getName()));

    // 使用参数执行工具
    var result = client.callTool("calculator", Map.of(
        "operation", "add",
        "a", 1,
        "b", 2
    ));
    ```
  </Tab>

  <Tab title="异步API">
    ```java
    // 异步列出可用工具
    client.listTools()
        .doOnNext(tools -> tools.forEach(tool -> 
            System.out.println(tool.getName())))
        .subscribe();

    // 异步执行工具
    client.callTool("calculator", Map.of(
            "operation", "add",
            "a", 1,
            "b", 2
        ))
        .subscribe();
    ```
  </Tab>
</Tabs>

### 资源访问

资源表示客户端可以使用URI模板访问的服务器端数据源。MCP客户端提供发现可用资源并通过标准化接口检索其内容的方法。

<Tabs>
  <Tab title="同步API">
    ```java
    // 列出可用资源及其名称
    var resources = client.listResources();
    resources.forEach(resource -> System.out.println(resource.getName()));

    // 使用URI模板检索资源内容
    var content = client.getResource("file", Map.of(
        "path", "/path/to/file.txt"
    ));
    ```
  </Tab>

  <Tab title="异步API">
    ```java
    // 异步列出可用资源
    client.listResources()
        .doOnNext(resources -> resources.forEach(resource -> 
            System.out.println(resource.getName())))
        .subscribe();

    // 异步检索资源内容
    client.getResource("file", Map.of(
            "path", "/path/to/file.txt"
        ))
        .subscribe();
    ```
  </Tab>
</Tabs>

### 提示系统

提示系统支持与服务器端提示模板交互。这些模板可以被发现并使用自定义参数执行，允许基于预定义模式的动态文本生成。

<Tabs>
  <Tab title="同步API">
    ```java
    // 列出可用提示模板
    var prompts = client.listPrompts();
    prompts.forEach(prompt -> System.out.println(prompt.getName()));

    // 使用参数执行提示模板
    var response = client.executePrompt("echo", Map.of(
        "text", "Hello, World!"
    ));
    ```
  </Tab>

  <Tab title="异步API">
    ```java
    // 异步列出可用提示模板
    client.listPrompts()
        .doOnNext(prompts -> prompts.forEach(prompt -> 
            System.out.println(prompt.getName())))
        .subscribe();

    // 异步执行提示模板
    client.executePrompt("echo", Map.of(
            "text", "Hello, World!"
        ))
        .subscribe();
    ```
  </Tab>
</Tabs>

### 使用补全

作为[补全能力](/specification/2025-03-26/server/utilities/completion)的一部分，MCP提供了一种标准化方式，让服务器为提示和资源URI提供参数自动补全建议。

查看[服务器补全能力](/sdk/java/mcp-server#completion-specification)了解如何在服务器端启用和配置补全。

在客户端，MCP客户端提供请求自动补全的方法：

<Tabs>
  <Tab title="同步API">
    ```java
    CompleteRequest request = new CompleteRequest(
            new PromptReference("code_review"),
            new CompleteRequest.CompleteArgument("language", "py"));

    CompleteResult result = syncMcpClient.completeCompletion(request);
    ```
  </Tab>

  <Tab title="异步API">
    ```java
CompleteRequest request = new CompleteRequest(
            new PromptReference("code_review"),
            new CompleteRequest.CompleteArgument("language", "py"));

    Mono<CompleteResult> result = mcpClient.completeCompletion(request);

    ```
  </Tab>
</Tabs>


# 概述
来源：https://modelcontextprotocol.io/sdk/java/mcp-overview

Model Context Protocol (MCP) Java SDK 介绍

[Model Context Protocol](https://modelcontextprotocol.org/docs/concepts/architecture)的Java SDK实现了AI模型和工具之间的标准化集成。

<Note>
  ### 0.8.x版本中的破坏性变更 ⚠️

  **注意：** 0.8.x版本引入了多项破坏性变更，包括新的基于会话的架构。
  如果您是从0.7.0升级，请参考[迁移指南](https://github.com/modelcontextprotocol/java-sdk/blob/main/migration-0.8.0.md)获取详细说明。
</Note>

## 功能特性

* MCP客户端和服务器实现支持：
  * 协议[版本兼容性协商](/specification/2024-11-05/basic/lifecycle/#initialization)
  * [工具](/specification/2024-11-05/server/tools/)发现、执行、列表变更通知
  * 使用URI模板的[资源](/specification/2024-11-05/server/resources/)管理
  * [Roots](/specification/2024-11-05/client/roots/)列表管理和通知
  * [提示](/specification/2024-11-05/server/prompts/)处理和管理
  * 用于AI模型交互的[采样](/specification/2024-11-05/client/sampling/)支持
* 多种传输实现：
  * 默认传输(包含在核心`mcp`模块中，无需外部Web框架)：
    * 基于Stdio的进程间通信传输
    * 基于Java HttpClient的SSE客户端传输，用于HTTP SSE客户端流
    * 基于Servlet的SSE服务器传输，用于HTTP SSE服务器流
  * 可选的Spring框架传输(使用Spring框架时更方便)：
    * WebFlux SSE客户端和服务器传输，用于响应式HTTP流
    * WebMVC SSE传输，用于基于Servlet的HTTP流
* 支持同步和异步编程范式

<Tip>
  核心`io.modelcontextprotocol.sdk:mcp`模块提供了默认的STDIO和SSE客户端及服务器传输实现，无需外部Web框架。

  Spring特定的传输实现作为可选依赖提供，方便使用[Spring Framework](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-client-boot-starter-docs.html)时使用。
</Tip>

## 架构

SDK采用分层架构，关注点分离清晰：

![MCP堆栈架构](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/java/mcp-stack.svg)

* **客户端/服务器层(McpClient/McpServer)**：两者都使用McpSession进行同步/异步操作，
  McpClient处理客户端协议操作，McpServer管理服务器端协议操作。
* **会话层(McpSession)**：使用DefaultMcpSession实现管理通信模式和状态。
* **传输层(McpTransport)**：通过以下方式处理JSON-RPC消息序列化/反序列化：
  * 核心模块中的StdioTransport(stdin/stdout)
  * 专用传输模块中的HTTP SSE传输(Java HttpClient、Spring WebFlux、Spring WebMVC)

MCP客户端是Model Context Protocol(MCP)架构中的关键组件，负责建立和管理与MCP服务器的连接。
它实现了协议的客户端部分。

![Java MCP客户端架构](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/java/java-mcp-client-architecture.jpg)

MCP服务器是Model Context Protocol(MCP)架构中的基础组件，向客户端提供工具、资源和能力。
它实现了协议的服务器端部分。

![Java MCP服务器架构](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/java/java-mcp-server-architecture.jpg)

关键交互：

* **客户端/服务器初始化**：传输设置、协议兼容性检查、能力协商和实现细节交换。
* **消息流**：JSON-RPC消息处理，包括验证、类型安全响应处理和错误处理。
* **资源管理**：资源发现、基于URI模板的访问、订阅系统和内容检索。

## 依赖项

在项目中添加以下Maven依赖：

<Tabs>
  <Tab title="Maven">
    核心MCP功能：

    ```xml
    <dependency>
        <groupId>io.modelcontextprotocol.sdk</groupId>
        <artifactId>mcp</artifactId>
    </dependency>
    ```

    核心`mcp`模块已包含默认STDIO和SSE传输实现，无需外部Web框架。

    如果使用Spring框架并希望使用Spring特定的传输实现，添加以下可选依赖之一：

    ```xml
    <!-- 可选：基于Spring WebFlux的SSE客户端和服务器传输 -->
    <dependency>
        <groupId>io.modelcontextprotocol.sdk</groupId>
        <artifactId>mcp-spring-webflux</artifactId>
    </dependency>

    <!-- 可选：基于Spring WebMVC的SSE服务器传输 -->
    <dependency>
        <groupId>io.modelcontextprotocol.sdk</groupId>
        <artifactId>mcp-spring-webmvc</artifactId>
    </dependency>
    ```
  </Tab>

  <Tab title="Gradle">
    核心MCP功能：

    ```groovy
    dependencies {
      implementation platform("io.modelcontextprotocol.sdk:mcp")
      //...
    }
    ```

    核心`mcp`模块已包含默认STDIO和SSE传输实现，无需外部Web框架。

    如果使用Spring框架并希望使用Spring特定的传输实现，添加以下可选依赖之一：

    ```groovy
    // 可选：基于Spring WebFlux的SSE客户端和服务器传输
    dependencies {
      implementation platform("io.modelcontextprotocol.sdk:mcp-spring-webflux")
    }

    // 可选：基于Spring WebMVC的SSE服务器传输
    dependencies {
      implementation platform("io.modelcontextprotocol.sdk:mcp-spring-webmvc")
    }
    ```
  </Tab>
</Tabs>

### 物料清单(BOM)

物料清单(BOM)声明了给定版本中所有依赖项的推荐版本。
在应用程序的构建脚本中使用BOM可以避免您自己指定和维护依赖项版本。
相反，您使用的BOM版本决定了所使用的依赖项版本。
它还确保默认情况下您使用的是受支持和测试过的依赖项版本，除非您选择覆盖它们。

将BOM添加到项目中：

<Tabs>
  <Tab title="Maven">
    ```xml
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>io.modelcontextprotocol.sdk</groupId>
                <artifactId>mcp-bom</artifactId>
                <version>0.9.0</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
    ```
  </Tab>

  <Tab title="Gradle">
    ```groovy
    dependencies {
      implementation platform("io.modelcontextprotocol.sdk:mcp-bom:0.9.0")
      //...
    }
    ```

    Gradle用户还可以通过利用Gradle(5.0+)对使用Maven BOM声明依赖约束的原生支持来使用Spring AI MCP BOM。
    这是通过在Gradle构建脚本的依赖项部分添加'platform'依赖处理程序方法实现的。
    如上面的代码片段所示，然后可以跟随着您希望使用的一个或多个spring-ai模块的无版本Starter依赖项声明，例如spring-ai-openai。
  </Tab>
</Tabs>

将版本号替换为您想要使用的BOM版本。

### 可用依赖项

以下依赖项可用并由BOM管理：
* 核心依赖项
  * `io.modelcontextprotocol.sdk:mcp` - 核心MCP库，提供Model Context Protocol实现的基础功能和API，包括默认的STDIO和SSE客户端及服务器传输实现。无需外部Web框架。
* 可选传输依赖项(使用Spring框架时更方便)
  * `io.modelcontextprotocol.sdk:mcp-spring-webflux` - 基于WebFlux的服务器发送事件(SSE)传输实现，用于响应式应用。
  * `io.modelcontextprotocol.sdk:mcp-spring-webmvc` - 基于WebMVC的服务器发送事件(SSE)传输实现，用于基于Servlet的应用。
* 测试依赖项
  * `io.modelcontextprotocol.sdk:mcp-test` - MCP应用的测试工具和支持。

# MCP服务器
来源：https://modelcontextprotocol.io/sdk/java/mcp-server

学习如何实现和配置Model Context Protocol(MCP)服务器

<Note>
  ### 0.8.x版本中的破坏性变更 ⚠️

  **注意：** 0.8.x版本引入了多项破坏性变更，包括新的基于会话的架构。
  如果您是从0.7.0升级，请参考[迁移指南](https://github.com/modelcontextprotocol/java-sdk/blob/main/migration-0.8.0.md)获取详细说明。
</Note>

## 概述

MCP服务器是Model Context Protocol(MCP)架构中的基础组件，向客户端提供工具、资源和能力。它实现了协议的服务器端部分，负责：

* 暴露客户端可以发现和执行的工具
* 使用基于URI的访问模式管理资源
* 提供提示模板和处理提示请求
* 支持与客户端的能力协商
* 实现服务器端协议操作
* 管理并发客户端连接
* 提供结构化日志和通知

<Tip>
  核心`io.modelcontextprotocol.sdk:mcp`模块提供了STDIO和SSE服务器传输实现，无需外部Web框架。

  Spring特定的传输实现作为**可选**依赖项`io.modelcontextprotocol.sdk:mcp-spring-webflux`、`io.modelcontextprotocol.sdk:mcp-spring-webmvc`提供给[Spring Framework](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-client-boot-starter-docs.html)用户。
</Tip>

服务器支持同步和异步API，允许在不同应用上下文中灵活集成。

<Tabs>
  <Tab title="同步API">
    ```java
    // 创建具有自定义配置的服务器
    McpSyncServer syncServer = McpServer.sync(transportProvider)
        .serverInfo("my-server", "1.0.0")
        .capabilities(ServerCapabilities.builder()
            .resources(true)     // 启用资源支持
            .tools(true)         // 启用工具支持
            .prompts(true)       // 启用提示支持
            .logging()           // 启用日志支持
            .completions()      // 启用补全支持
            .build())
        .build();

    // 注册工具、资源和提示
    syncServer.addTool(syncToolSpecification);
    syncServer.addResource(syncResourceSpecification);
    syncServer.addPrompt(syncPromptSpecification);

    // 完成后关闭服务器
    syncServer.close();
    ```
  </Tab>

  <Tab title="异步API">
    ```java
    // 创建具有自定义配置的异步服务器
    McpAsyncServer asyncServer = McpServer.async(transportProvider)
        .serverInfo("my-server", "1.0.0")
        .capabilities(ServerCapabilities.builder()
            .resources(true)     // 启用资源支持
            .tools(true)         // 启用工具支持
            .prompts(true)       // 启用提示支持
            .logging()           // 启用日志支持
            .build())
        .build();

    // 注册工具、资源和提示
    asyncServer.addTool(asyncToolSpecification)
        .doOnSuccess(v -> logger.info("工具已注册"))
        .subscribe();

    asyncServer.addResource(asyncResourceSpecification)
        .doOnSuccess(v -> logger.info("资源已注册"))
        .subscribe();

    asyncServer.addPrompt(asyncPromptSpecification)
        .doOnSuccess(v -> logger.info("提示已注册"))
        .subscribe();

    // 完成后关闭服务器
    asyncServer.close()
        .doOnSuccess(v -> logger.info("服务器已关闭"))
        .subscribe();
    ```
  </Tab>
</Tabs>

## 服务器传输提供者

MCP SDK中的传输层负责处理客户端和服务器之间的通信。
它提供了不同的实现来支持各种通信协议和模式。
SDK包含几个内置的传输提供者实现：

<Tabs>
  <Tab title="STDIO">
    <>
      创建基于进程内传输：

      ```java
      StdioServerTransportProvider transportProvider = new StdioServerTransportProvider(new ObjectMapper());
      ```

      通过标准输入/输出流提供双向JSON-RPC消息处理，具有非阻塞消息处理、序列化/反序列化和优雅关闭支持。

      关键特性：

      <ul>
        <li>通过stdin/stdout进行双向通信</li>
        <li>支持基于进程的集成</li>
        <li>简单的设置和配置</li>
        <li>轻量级实现</li>
      </ul>
    </>
  </Tab>

  <Tab title="SSE (WebFlux)">
    <>
      <p>创建基于WebFlux的SSE服务器传输。<br />需要<code>mcp-spring-webflux</code>依赖项。</p>

      ```java
      @Configuration
      class McpConfig {
          @Bean
          WebFluxSseServerTransportProvider webFluxSseServerTransportProvider(ObjectMapper mapper) {
              return new WebFluxSseServerTransportProvider(mapper, "/mcp/message");
          }

          @Bean
          RouterFunction<?> mcpRouterFunction(WebFluxSseServerTransportProvider transportProvider) {
              return transportProvider.getRouterFunction();
          }
      }
      ```

      <p>实现MCP HTTP与SSE传输规范，提供：</p>

      <ul>
        <li>使用WebFlux的响应式HTTP流</li>
        <li>通过SSE端点支持并发客户端连接</li>
        <li>消息路由和会话管理</li>
        <li>优雅关闭能力</li>
      </ul>
    </>
  </Tab>

  <Tab title="SSE (WebMvc)">
    <>
      <p>创建基于WebMvc的SSE服务器传输。<br />需要<code>mcp-spring-webmvc</code>依赖项。</p>

      ```java
      @Configuration
      @EnableWebMvc
      class McpConfig {
          @Bean
          WebMvcSseServerTransportProvider webMvcSseServerTransportProvider(ObjectMapper mapper) {
              return new WebMvcSseServerTransportProvider(mapper, "/mcp/message");
          }

          @Bean
          RouterFunction<ServerResponse> mcpRouterFunction(WebMvcSseServerTransportProvider transportProvider) {
              return transportProvider.getRouterFunction();
          }
      }
      ```

      <p>实现MCP HTTP与SSE传输规范，提供：</p>

      <ul>
        <li>服务器端事件流</li>
        <li>与Spring WebMVC集成</li>
        <li>支持传统Web应用</li>
        <li>同步操作处理</li>
      </ul>
</>
  </Tab>

  <Tab title="SSE (Servlet)">
    <>
      <p>
        创建基于Servlet的SSE服务器传输。它包含在核心<code>mcp</code>模块中。<br />
        <code>HttpServletSseServerTransport</code>可以与任何Servlet容器一起使用。<br />
        要在Spring Web应用中使用，可以将其注册为Servlet bean：
      </p>

      ```java
      @Configuration
      @EnableWebMvc
      public class McpServerConfig implements WebMvcConfigurer {

          @Bean
          public HttpServletSseServerTransportProvider servletSseServerTransportProvider() {
              return new HttpServletSseServerTransportProvider(new ObjectMapper(), "/mcp/message");
          }

          @Bean
          public ServletRegistrationBean customServletBean(HttpServletSseServerTransportProvider transportProvider) {
              return new ServletRegistrationBean(transportProvider);
          }
      }
      ```

      <p>
        使用传统的Servlet API实现MCP HTTP与SSE传输规范，提供：
      </p>

      <ul>
        <li>使用Servlet 6.0异步支持的异步消息处理</li>
        <li>多客户端连接的会话管理</li>

        <li>
          两种类型的端点：

          <ul>
            <li>SSE端点(<code>/sse</code>)用于服务器到客户端的事件</li>
            <li>可配置的消息端点用于客户端到服务器的请求</li>
          </ul>
        </li>

        <li>错误处理和响应格式化</li>
        <li>优雅关闭支持</li>
      </ul>
    </>
  </Tab>
</Tabs>

## 服务器能力

服务器可以配置多种能力：

```java
var capabilities = ServerCapabilities.builder()
    .resources(false, true)  // 资源支持，带列表变更通知
    .tools(true)            // 工具支持，带列表变更通知
    .prompts(true)          // 提示支持，带列表变更通知
    .logging()              // 启用日志支持(默认启用，日志级别为INFO)
    .build();
```

### 日志支持

服务器提供结构化日志能力，允许向客户端发送不同严重级别的日志消息：

```java
// 向客户端发送日志消息
server.loggingNotification(LoggingMessageNotification.builder()
    .level(LoggingLevel.INFO)
    .logger("custom-logger")
    .data("自定义日志消息")
    .build());
```

客户端可以通过`mcpClient.setLoggingLevel(level)`请求控制接收的最低日志级别。低于设置级别的消息将被过滤掉。
支持的日志级别(按严重程度递增)：DEBUG (0), INFO (1), NOTICE (2), WARNING (3), ERROR (4), CRITICAL (5), ALERT (6), EMERGENCY (7)

### 工具规范

Model Context Protocol允许服务器[暴露工具](/specification/2024-11-05/server/tools/)供语言模型调用。
Java SDK允许实现带有处理函数的工具规范。
工具使AI模型能够执行计算、访问外部API、查询数据库和操作文件：

<Tabs>
  <Tab title="同步">
    ```java
    // 同步工具规范
    var schema = """
                {
                  "type" : "object",
                  "id" : "urn:jsonschema:Operation",
                  "properties" : {
                    "operation" : {
                      "type" : "string"
                    },
                    "a" : {
                      "type" : "number"
                    },
                    "b" : {
                      "type" : "number"
                    }
                  }
                }
                """;
    var syncToolSpecification = new McpServerFeatures.SyncToolSpecification(
        new Tool("calculator", "基础计算器", schema),
        (exchange, arguments) -> {
            // 工具实现
            return new CallToolResult(result, false);
        }
    );
    ```
  </Tab>

  <Tab title="异步">
    ```java
    // 异步工具规范
    var schema = """
                {
                  "type" : "object",
                  "id" : "urn:jsonschema:Operation",
                  "properties" : {
                    "operation" : {
                      "type" : "string"
                    },
                    "a" : {
                      "type" : "number"
                    },
                    "b" : {
                      "type" : "number"
                    }
                  }
                }
                """;
    var asyncToolSpecification = new McpServerFeatures.AsyncToolSpecification(
        new Tool("calculator", "基础计算器", schema),
        (exchange, arguments) -> {
            // 工具实现
            return Mono.just(new CallToolResult(result, false));
        }
    );
    ```
  </Tab>
</Tabs>

工具规范包括带有`名称`、`描述`和`参数模式`的工具定义，以及实现工具逻辑的调用处理程序。
函数的第一个参数是用于客户端交互的`McpAsyncServerExchange`，第二个是工具参数的映射。

### 资源规范

带有处理函数的资源规范。
资源通过暴露以下数据为AI模型提供上下文：文件内容、数据库记录、API响应、系统信息、应用状态。
示例资源规范：

<Tabs>
  <Tab title="同步">
    ```java
    // 同步资源规范
    var syncResourceSpecification = new McpServerFeatures.SyncResourceSpecification(
        new Resource("custom://resource", "名称", "描述", "mime-type", null),
        (exchange, request) -> {
            // 资源读取实现
            return new ReadResourceResult(contents);
        }
    );
    ```
  </Tab>

  <Tab title="异步">
    ```java
    // 异步资源规范
    var asyncResourceSpecification = new McpServerFeatures.AsyncResourceSpecification(
        new Resource("custom://resource", "名称", "描述", "mime-type", null),
        (exchange, request) -> {
            // 资源读取实现
            return Mono.just(new ReadResourceResult(contents));
        }
    );
    ```
  </Tab>
</Tabs>

资源规范由资源定义和资源读取处理程序组成。
资源定义包括`名称`、`描述`和`MIME类型`。
处理资源读取请求的函数的第一个参数是`McpAsyncServerExchange`，服务器可以通过它与连接的客户端交互。
第二个参数是`McpSchema.ReadResourceRequest`。

### 提示规范

作为[提示能力](/specification/2024-11-05/server/prompts/)的一部分，MCP提供了一种标准化方式让服务器向客户端暴露提示模板。
提示规范是AI模型交互的结构化模板，支持一致的消息格式化、参数替换、上下文注入、响应格式化和指令模板化。

<Tabs>
  <Tab title="同步">
    ```java
    // 同步提示规范
    var syncPromptSpecification = new McpServerFeatures.SyncPromptSpecification(
        new Prompt("greeting", "描述", List.of(
            new PromptArgument("name", "描述", true)
        )),
        (exchange, request) -> {
            // 提示实现
            return new GetPromptResult(description, messages);
        }
    );
    ```
  </Tab>

  <Tab title="异步">
    ```java
    // 异步提示规范
    var asyncPromptSpecification = new McpServerFeatures.AsyncPromptSpecification(
        new Prompt("greeting", "描述", List.of(
            new PromptArgument("name", "描述", true)
        )),
        (exchange, request) -> {
            // 提示实现
            return Mono.just(new GetPromptResult(description, messages));
        }
    );
    ```
  </Tab>
</Tabs>

提示定义包括名称(提示的标识符)、描述(提示的目的)和参数列表(用于模板化的参数)。
处理函数处理请求并返回格式化模板。
第一个参数是用于客户端交互的`McpAsyncServerExchange`，第二个参数是`GetPromptRequest`实例。

### 补全规范

作为[补全能力](/specification/2025-03-26/server/utilities/completion)的一部分，MCP提供了一种标准化方式让服务器为提示和资源URI提供参数自动补全建议。

<Tabs>
  <Tab title="同步">
    ```java
    // 同步补全规范
    var syncCompletionSpecification = new McpServerFeatures.SyncCompletionSpecification(
    			new McpSchema.PromptReference("code_review"), (exchange, request) -> {
            
            // 补全实现...
            
            return new McpSchema.CompleteResult(
                new CompleteResult.CompleteCompletion(
                  List.of("python", "pytorch", "pyside"), 
                  10, // 总数
                  false // 是否有更多
                ));
          }
    );

    // 创建具有补全能力的同步服务器
    var mcpServer = McpServer.sync(mcpServerTransportProvider)
      .capabilities(ServerCapabilities.builder()
        .completions() // 启用补全支持
          // ...
        .build())
      // ...
      .completions(new McpServerFeatures.SyncCompletionSpecification( // 注册补全规范
          new McpSchema.PromptReference("code_review"), syncCompletionSpecification))
      .build();
    ```
  </Tab>

  <Tab title="异步">
    ```java
    // 异步提示规范
    var asyncCompletionSpecification = new McpServerFeatures.AsyncCompletionSpecification(
    			new McpSchema.PromptReference("code_review"), (exchange, request) -> {

            // 补全实现...

            return Mono.just(new McpSchema.CompleteResult(
                new CompleteResult.CompleteCompletion(
                  List.of("python", "pytorch", "pyside"), 
                  10, // 总数
                  false // 是否有更多
                )));
          }
    );

    // 创建具有补全能力的异步服务器
    var mcpServer = McpServer.async(mcpServerTransportProvider)
      .capabilities(ServerCapabilities.builder()
        .completions() // 启用补全支持
          // ...
        .build())
      // ...
      .completions(new McpServerFeatures.AsyncCompletionSpecification( // 注册补全规范
          new McpSchema.PromptReference("code_review"), asyncCompletionSpecification))
      .build();
    ```
  </Tab>
</Tabs>

`McpSchema.CompletionReference`定义定义了类型(`PromptRefernce`或`ResourceRefernce`)和补全规范的标识符(例如处理程序)。
处理函数处理请求并返回补全响应。
第一个参数是用于客户端交互的`McpAsyncServerExchange`，第二个参数是`CompleteRequest`实例。

查看[使用补全](/sdk/java/mcp-client#using-completion)了解如何在客户端使用补全能力。

### 使用服务器采样

要使用[采样能力](/specification/2024-11-05/client/sampling/)，请连接到支持采样的客户端。
不需要特殊的服务器配置，但在发出请求前验证客户端采样支持。
了解[客户端采样支持](./mcp-client#sampling-support)。

连接到兼容客户端后，服务器可以请求语言模型生成：

<Tabs>
  <Tab title="同步API">
    ```java
    // 创建服务器
    McpSyncServer server = McpServer.sync(transportProvider)
        .serverInfo("my-server", "1.0.0")
        .build();

    // 定义使用采样的工具
    var calculatorTool = new McpServerFeatures.SyncToolSpecification(
        new Tool("ai-calculator", "使用AI执行计算", schema),
        (exchange, arguments) -> {
            // 检查客户端是否支持采样
            if (exchange.getClientCapabilities().sampling() == null) {
                return new CallToolResult("客户端不支持AI能力", false);
            }
            
            // 创建采样请求
            McpSchema.CreateMessageRequest request = McpSchema.CreateMessageRequest.builder()
                .messages(List.of(new McpSchema.SamplingMessage(McpSchema.Role.USER,
                    new McpSchema.TextContent("计算: " + arguments.get("expression")))
                .modelPreferences(McpSchema.ModelPreferences.builder()
                    .hints(List.of(
                        McpSchema.ModelHint.of("claude-3-sonnet"),
                        McpSchema.ModelHint.of("claude")
                    ))
                    .intelligencePriority(0.8)  // 优先考虑智能
                    .speedPriority(0.5)         // 中等速度重要性
                    .build())
                .systemPrompt("你是一个有帮助的计算助手。只提供数字答案。")
                .maxTokens(100)
                .build();
            
            // 向客户端请求采样
            McpSchema.CreateMessageResult result = exchange.createMessage(request);
            
            // 处理结果
            String answer = result.content().text();
            return new CallToolResult(answer, false);
        }
    );

    // 将工具添加到服务器
    server.addTool(calculatorTool);
    ```
  </Tab>

  <Tab title="异步API">
    ```java
    // 创建服务器
    McpAsyncServer server = McpServer.async(transportProvider)
        .serverInfo("my-server", "1.0.0")
        .build();

    // 定义使用采样的工具
    var calculatorTool = new McpServerFeatures.AsyncToolSpecification(
        new Tool("ai-calculator", "使用AI执行计算", schema),
        (exchange, arguments) -> {
            // 检查客户端是否支持采样
if (exchange.getClientCapabilities().sampling() == null) {
                return Mono.just(new CallToolResult("客户端不支持AI能力", false));
            }
            
            // 创建采样请求
            McpSchema.CreateMessageRequest request = McpSchema.CreateMessageRequest.builder()
                .content(new McpSchema.TextContent("计算: " + arguments.get("expression")))
                .modelPreferences(McpSchema.ModelPreferences.builder()
                    .hints(List.of(
                        McpSchema.ModelHint.of("claude-3-sonnet"),
                        McpSchema.ModelHint.of("claude")
                    ))
                    .intelligencePriority(0.8)  // 优先考虑智能
                    .speedPriority(0.5)         // 中等速度重要性
                    .build())
                .systemPrompt("你是一个有帮助的计算助手。只提供数字答案。")
                .maxTokens(100)
                .build();
            
            // 向客户端请求采样
            return exchange.createMessage(request)
                .map(result -> {
                    // 处理结果
                    String answer = result.content().text();
                    return new CallToolResult(answer, false);
                });
        }
    );

    // 将工具添加到服务器
    server.addTool(calculatorTool)
        .subscribe();
    ```
  </Tab>
</Tabs>

`CreateMessageRequest`对象允许您指定：`Content` - 模型的输入文本或图像，
`Model Preferences` - 模型选择的提示和优先级，`System Prompt` - 模型行为的指令和
`Max Tokens` - 生成响应的最大长度。

### 日志支持

服务器提供结构化日志能力，允许向客户端发送不同严重级别的日志消息。
日志通知只能在现有客户端会话中发送，例如工具、资源和提示调用。

例如，我们可以从工具处理函数中发送日志消息。
在客户端，您可以注册日志消费者来接收来自服务器的日志消息，并设置最低日志级别来过滤消息。

```java
var mcpClient = McpClient.sync(transport)
        .loggingConsumer(notification -> {
            System.out.println("收到日志消息: " + notification.data());
        })
        .build();

mcpClient.initialize();

mcpClient.setLoggingLevel(McpSchema.LoggingLevel.INFO);

// 调用发送日志通知的工具
CallToolResult result = mcpClient.callTool(new McpSchema.CallToolRequest("logging-test", Map.of()));
```

服务器可以在工具/资源/提示处理函数中使用`McpAsyncServerExchange`/`McpSyncServerExchange`对象发送日志消息：

```java
var tool = new McpServerFeatures.AsyncToolSpecification(
    new McpSchema.Tool("logging-test", "测试日志通知", emptyJsonSchema),
    (exchange, request) -> {  

      exchange.loggingNotification( // 使用exchange发送日志消息
          McpSchema.LoggingMessageNotification.builder()
            .level(McpSchema.LoggingLevel.DEBUG)
            .logger("test-logger")
            .data("调试消息")
            .build())
        .block();

      return Mono.just(new CallToolResult("日志测试完成", false));
    });

var mcpServer = McpServer.async(mcpServerTransportProvider)
  .serverInfo("test-server", "1.0.0")
  .capabilities(
    ServerCapabilities.builder()
      .logging() // 启用日志支持
      .tools(true)
      .build())
  .tools(tool)
  .build();
```

客户端可以通过`mcpClient.setLoggingLevel(level)`请求控制接收的最低日志级别。低于设置级别的消息将被过滤掉。
支持的日志级别(按严重程度递增)：DEBUG (0), INFO (1), NOTICE (2), WARNING (3), ERROR (4), CRITICAL (5), ALERT (6), EMERGENCY (7)

## 错误处理

SDK通过McpError类提供全面的错误处理，涵盖协议兼容性、传输通信、JSON-RPC消息传递、工具执行、资源管理、提示处理、超时和连接问题。这种统一的错误处理方法确保在同步和异步操作中一致可靠地管理错误。


# 架构
来源：https://modelcontextprotocol.io/specification/2024-11-05/architecture/index


Model Context Protocol(MCP)遵循客户端-主机-服务器架构，其中每个
主机可以运行多个客户端实例。这种架构使用户能够跨应用程序集成AI
能力，同时保持清晰的安全边界和隔离关注点。基于JSON-RPC构建，MCP提供了
专注于客户端和服务器之间上下文交换和采样协调的有状态会话协议。

## 核心组件

```mermaid
graph LR
    subgraph "应用主机进程"
        H[主机]
        C1[客户端1]
        C2[客户端2]
        C3[客户端3]
        H --> C1
        H --> C2
        H --> C3
    end

    subgraph "本地机器"
        S1[服务器1<br>文件与Git]
        S2[服务器2<br>数据库]
        R1[("本地<br>资源A")]
        R2[("本地<br>资源B")]

        C1 --> S1
        C2 --> S2
        S1 <--> R1
        S2 <--> R2
    end

    subgraph "互联网"
        S3[服务器3<br>外部API]
        R3[("远程<br>资源C")]

        C3 --> S3
        S3 <--> R3
    end
```

### 主机

主机进程充当容器和协调器：

* 创建和管理多个客户端实例
* 控制客户端连接权限和生命周期
* 强制执行安全策略和同意要求
* 处理用户授权决策
* 协调AI/LLM集成和采样
* 管理跨客户端的上下文聚合

### 客户端

每个客户端由主机创建并维护与服务器的隔离连接：

* 每个服务器建立一个有状态会话
* 处理协议协商和能力交换
* 双向路由协议消息
* 管理订阅和通知
* 维护服务器之间的安全边界

主机应用程序创建并管理多个客户端，每个客户端与特定服务器保持1:1关系。

### 服务器

服务器提供专门的上下文和能力：

* 通过MCP原语暴露资源、工具和提示
* 独立运行，职责明确
* 通过客户端接口请求采样
* 必须遵守安全约束
* 可以是本地进程或远程服务

## 设计原则

MCP基于几个关键设计原则构建，这些原则指导其架构和实现：

1. **服务器应该非常容易构建**
* 主机应用程序处理复杂的编排职责
   * 服务器专注于特定、定义明确的能力
   * 简单接口最小化实现开销
   * 清晰的分离使代码可维护

2. **服务器应该高度可组合**

   * 每个服务器提供隔离的专注功能
   * 多个服务器可以无缝组合
   * 共享协议实现互操作性
   * 模块化设计支持可扩展性

3. **服务器不应该能够读取整个对话，也不能"窥视"其他服务器**

   * 服务器只接收必要的上下文信息
   * 完整对话历史保留在主机中
   * 每个服务器连接保持隔离
   * 跨服务器交互由主机控制
   * 主机进程强制执行安全边界

4. **功能可以逐步添加到服务器和客户端**
   * 核心协议提供最小必需功能
   * 额外能力可以根据需要协商
   * 服务器和客户端独立演进
   * 协议设计考虑未来可扩展性
   * 保持向后兼容性

## 消息类型

MCP基于[JSON-RPC 2.0](https://www.jsonrpc.org/specification)定义了三种核心消息类型：

* **请求**：带有方法和参数的期望响应的双向消息
* **响应**：匹配特定请求ID的成功结果或错误
* **通知**：不需要响应的单向消息

每种消息类型都遵循JSON-RPC 2.0规范的结构和传递语义。

## 能力协商

Model Context Protocol使用基于能力的协商系统，客户端和服务器在初始化时明确声明其支持的功能。能力决定会话期间可用的协议功能和原语。

* 服务器声明能力如资源订阅、工具支持和提示模板
* 客户端声明能力如采样支持和通知处理
* 双方必须在整个会话期间遵守声明的能力
* 可以通过协议扩展协商额外能力

```mermaid
sequenceDiagram
    participant 主机
    participant 客户端
    participant 服务器

    主机->>+客户端: 初始化客户端
    客户端->>+服务器: 使用能力初始化会话
    服务器-->>客户端: 响应支持的能力

    Note over 主机,服务器: 具有协商功能的活跃会话

    loop 客户端请求
        主机->>客户端: 用户或模型发起的操作
        客户端->>服务器: 请求(工具/资源)
        服务器-->>客户端: 响应
        客户端-->>主机: 更新UI或响应模型
    end

    loop 服务器请求
        服务器->>客户端: 请求(采样)
        客户端->>主机: 转发给AI
        主机-->>客户端: AI响应
        客户端-->>服务器: 响应
    end

    loop 通知
        服务器--)客户端: 资源更新
        客户端--)服务器: 状态变更
    end

    主机->>客户端: 终止
    客户端->>-服务器: 结束会话
    deactivate 服务器
```

每个能力在会话期间解锁特定的协议功能。例如：

* 实现的[服务器功能](/specification/2024-11-05/server)必须在服务器的能力中声明
* 发出资源订阅通知需要服务器声明订阅支持
* 工具调用需要服务器声明工具能力
* [采样](/specification/2024-11-05/client)需要客户端在其能力中声明支持

这种能力协商确保客户端和服务器对支持的功能有清晰理解，同时保持协议的可扩展性。


# 概述
来源：https://modelcontextprotocol.io/specification/2024-11-05/basic/index


<Info>**协议修订版**: 2024-11-05</Info>

MCP客户端和服务器之间的所有消息**必须**遵循[JSON-RPC 2.0](https://www.jsonrpc.org/specification)规范。协议定义了三种基本消息类型：

| 类型            | 描述                             | 要求                               |
| --------------- | -------------------------------- | ---------------------------------- |
| `请求`          | 发起操作的消息                   | 必须包含唯一ID和方法名             |
| `响应`          | 回复请求的消息                   | 必须包含与请求相同的ID             |
| `通知`          | 不需要回复的单向消息             | 不能包含ID                         |

**响应**进一步细分为**成功结果**或**错误**。结果可以遵循任何JSON对象结构，而错误必须至少包含错误代码和消息。

## 协议层

Model Context Protocol由几个关键组件组成：

* **基础协议**：核心JSON-RPC消息类型
* **生命周期管理**：连接初始化、能力协商和会话控制
* **服务器功能**：服务器暴露的资源、提示和工具
* **客户端功能**：客户端提供的采样和根目录列表
* **实用工具**：跨领域关注点如日志和参数补全

所有实现**必须**支持基础协议和生命周期管理组件。其他组件**可以**根据应用程序的特定需求实现。

这些协议层建立了清晰的关注点分离，同时支持客户端和服务器之间的丰富交互。模块化设计允许实现仅支持它们需要的功能。

查看以下页面获取不同组件的更多详情：

<CardGroup cols={3}>
  <Card title="生命周期" icon="arrows-rotate" href="/specification/2024-11-05/basic/lifecycle" />

  <Card title="资源" icon="file-lines" href="/specification/2024-11-05/server/resources" />

  <Card title="提示" icon="message" href="/specification/2024-11-05/server/prompts" />

  <Card title="工具" icon="wrench" href="/specification/2024-11-05/server/tools" />

  <Card title="日志" icon="rectangle-list" href="/specification/2024-11-05/server/utilities/logging" />

  <Card title="采样" icon="code" href="/specification/2024-11-05/client/sampling" />
</CardGroup>

## 认证

认证和授权目前不是核心MCP规范的一部分，但我们正在考虑在未来引入它们的方式。加入[GitHub Discussions](https://github.com/modelcontextprotocol/specification/discussions)帮助我们塑造协议的未来！

客户端和服务器**可以**协商自己的自定义认证和授权策略。

## 模式

协议的完整规范定义为[TypeScript模式](http://github.com/modelcontextprotocol/specification/tree/main/schema/2024-11-05/schema.ts)。这是所有协议消息和结构的真实来源。

还有一个[JSON模式](http://github.com/modelcontextprotocol/specification/tree/main/schema/2024-11-05/schema.json)，它是从TypeScript真实来源自动生成的，用于各种自动化工具。


# 生命周期
来源：https://modelcontextprotocol.io/specification/2024-11-05/basic/lifecycle


<Info>**协议修订版**: 2024-11-05</Info>
Model Context Protocol (MCP)定义了严格的客户端-服务器连接生命周期，确保正确的能力协商和状态管理。

1. **初始化**：能力协商和协议版本确认
2. **操作**：正常的协议通信
3. **关闭**：优雅地终止连接

```mermaid
sequenceDiagram
    participant 客户端
    participant 服务器

    Note over 客户端,服务器: 初始化阶段
    activate 客户端
    客户端->>+服务器: 初始化请求
    服务器-->>客户端: 初始化响应
    客户端--)服务器: 初始化完成通知

    Note over 客户端,服务器: 操作阶段
    rect rgb(200, 220, 250)
        note over 客户端,服务器: 正常协议操作
    end

    Note over 客户端,服务器: 关闭
    客户端--)-服务器: 断开连接
    deactivate 服务器
    Note over 客户端,服务器: 连接关闭
```

## 生命周期阶段

### 初始化

初始化阶段**必须**是客户端和服务器之间的第一次交互。在此阶段，客户端和服务器：

* 建立协议版本兼容性
* 交换和协商能力
* 共享实现细节

客户端**必须**通过发送包含以下内容的`initialize`请求来启动此阶段：

* 支持的协议版本
* 客户端能力
* 客户端实现信息

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "roots": {
        "listChanged": true
      },
      "sampling": {}
    },
    "clientInfo": {
      "name": "ExampleClient",
      "version": "1.0.0"
    }
  }
}
```

服务器**必须**响应其自身的能力和信息：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "logging": {},
      "prompts": {
        "listChanged": true
      },
      "resources": {
        "subscribe": true,
        "listChanged": true
      },
      "tools": {
        "listChanged": true
      }
    },
    "serverInfo": {
      "name": "ExampleServer",
      "version": "1.0.0"
    }
  }
}
```

成功初始化后，客户端**必须**发送`initialized`通知以表示已准备好开始正常操作：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/initialized"
}
```

* 客户端**不应**在服务器响应`initialize`请求之前发送除[ping](/specification/2024-11-05/basic/utilities/ping)之外的请求。
* 服务器**不应**在收到`initialized`通知之前发送除[ping](/specification/2024-11-05/basic/utilities/ping)和[日志](/specification/2024-11-05/server/utilities/logging)之外的请求。

#### 版本协商

在`initialize`请求中，客户端**必须**发送其支持的协议版本。这**应该**是客户端支持的*最新*版本。

如果服务器支持请求的协议版本，它**必须**响应相同的版本。否则，服务器**必须**响应其支持的另一个协议版本。这**应该**是服务器支持的*最新*版本。

如果客户端不支持服务器响应中的版本，它**应该**断开连接。

#### 能力协商

客户端和服务器能力确定了会话期间可用的可选协议功能。

关键能力包括：

| 类别     | 能力          | 描述                                                                         |
| -------- | ------------- | --------------------------------------------------------------------------- |
| 客户端   | `roots`       | 提供文件系统[根目录](/specification/2024-11-05/client/roots)的能力           |
| 客户端   | `sampling`    | 支持LLM[采样](/specification/2024-11-05/client/sampling)请求                 |
| 客户端   | `experimental`| 描述对非标准实验功能的支持                                                   |
| 服务器   | `prompts`     | 提供[提示模板](/specification/2024-11-05/server/prompts)                     |
| 服务器   | `resources`   | 提供可读[资源](/specification/2024-11-05/server/resources)                   |
| 服务器   | `tools`       | 暴露可调用[工具](/specification/2024-11-05/server/tools)                     |
| 服务器   | `logging`     | 发出结构化[日志消息](/specification/2024-11-05/server/utilities/logging)     |
| 服务器   | `experimental`| 描述对非标准实验功能的支持                                                   |

能力对象可以描述子能力，如：

* `listChanged`：支持列表变更通知(用于提示、资源和工具)
* `subscribe`：支持订阅单个项目的变更(仅资源)

### 操作

在操作阶段，客户端和服务器根据协商的能力交换消息。

双方**应该**：

* 遵守协商的协议版本
* 仅使用成功协商的能力

### 关闭

在关闭阶段，一方(通常是客户端)干净地终止协议连接。没有定义特定的关闭消息——相反，应该使用底层传输机制来发出连接终止信号：

#### stdio

对于stdio[传输](/specification/2024-11-05/basic/transports)，客户端**应该**通过以下方式启动关闭：

1. 首先关闭子进程(服务器)的输入流
2. 等待服务器退出，如果服务器在合理时间内未退出，则发送`SIGTERM`
3. 如果在`SIGTERM`后的合理时间内服务器仍未退出，则发送`SIGKILL`

服务器**可以**通过关闭其到客户端的输出流并退出来启动关闭。

#### HTTP

对于HTTP[传输](/specification/2024-11-05/basic/transports)，关闭是通过关闭相关的HTTP连接来指示的。

## 错误处理
实现**应该**准备好处理这些错误情况：

* 协议版本不匹配
* 未能协商所需能力
* 初始化请求超时
* 关闭超时

实现**应该**为所有请求实现适当的超时，以防止连接挂起和资源耗尽。

初始化错误示例：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32602,
    "message": "不支持的协议版本",
    "data": {
      "supported": ["2024-11-05"],
      "requested": "1.0.0"
    }
  }
}
```


# 消息
来源：https://modelcontextprotocol.io/specification/2024-11-05/basic/messages


<Info>**协议修订版**: 2024-11-05</Info>

MCP中的所有消息**必须**遵循[JSON-RPC 2.0](https://www.jsonrpc.org/specification)规范。协议定义了三种消息类型：

## 请求

请求从客户端发送到服务器或反之。

```typescript
{
  jsonrpc: "2.0";
  id: string | number;
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

* 请求**必须**包含字符串或整数ID。
* 与基础JSON-RPC不同，ID**不能**为`null`。
* 请求ID**不能**在同一会话中被请求者先前使用过。

## 响应

响应是对请求的回复。

```typescript
{
  jsonrpc: "2.0";
  id: string | number;
  result?: {
    [key: string]: unknown;
  }
  error?: {
    code: number;
    message: string;
    data?: unknown;
  }
}
```

* 响应**必须**包含与对应请求相同的ID。
* 必须设置`result`或`error`。响应**不能**同时设置两者。
* 错误代码**必须**是整数。

## 通知

通知从客户端发送到服务器或反之。它们不需要响应。

```typescript
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

* 通知**不能**包含ID。


# 传输
来源：https://modelcontextprotocol.io/specification/2024-11-05/basic/transports


<Info>**协议修订版**: 2024-11-05</Info>

MCP目前定义了两种标准的客户端-服务器通信传输机制：

1. [stdio](#stdio)，通过标准输入和标准输出通信
2. [HTTP with Server-Sent Events](#http-with-sse) (SSE)

客户端**应该**尽可能支持stdio。

客户端和服务器也可以以可插拔的方式实现[自定义传输](#custom-transports)。

## stdio

在**stdio**传输中：

* 客户端将MCP服务器作为子进程启动。
* 服务器在其标准输入(`stdin`)上接收JSON-RPC消息，并将响应写入其标准输出(`stdout`)。
* 消息由换行符分隔，并且**不能**包含嵌入的换行符。
* 服务器**可以**将UTF-8字符串写入其标准错误(`stderr`)用于日志记录。客户端**可以**捕获、转发或忽略此日志记录。
* 服务器**不能**向`stdout`写入任何非有效MCP消息的内容。
* 客户端**不能**向服务器的`stdin`写入任何非有效MCP消息的内容。

```mermaid
sequenceDiagram
    participant 客户端
    participant 服务器进程

    客户端->>+服务器进程: 启动子进程
    loop 消息交换
        客户端->>服务器进程: 写入stdin
        服务器进程->>客户端: 写入stdout
        服务器进程--)客户端: 在stderr上的可选日志
    end
    客户端->>服务器进程: 关闭stdin，终止子进程
    deactivate 服务器进程
```

## HTTP with SSE

在**SSE**传输中，服务器作为可以处理多个客户端连接的独立进程运行。

#### 安全警告

实现HTTP with SSE传输时：

1. 服务器**必须**验证所有传入连接的`Origin`头，以防止DNS重绑定攻击
2. 本地运行时，服务器**应该**仅绑定到localhost(127.0.0.1)而不是所有网络接口(0.0.0.0)
3. 服务器**应该**为所有连接实现适当的认证

没有这些保护措施，攻击者可能使用DNS重绑定从远程网站与本地MCP服务器交互。

服务器**必须**提供两个端点：

1. 一个SSE端点，供客户端建立连接并接收来自服务器的消息
2. 一个常规的HTTP POST端点，供客户端向服务器发送消息

当客户端连接时，服务器**必须**发送一个`endpoint`事件，包含客户端用于发送消息的URI。所有后续客户端消息**必须**作为HTTP POST请求发送到此端点。

服务器消息作为SSE `message`事件发送，消息内容编码为JSON在事件数据中。

```mermaid
sequenceDiagram
    participant 客户端
    participant 服务器

    客户端->>服务器: 打开SSE连接
    服务器->>客户端: endpoint事件
    loop 消息交换
        客户端->>服务器: HTTP POST消息
        服务器->>客户端: SSE message事件
    end
    客户端->>服务器: 关闭SSE连接
## 自定义传输

客户端和服务器**可以**实现额外的自定义传输机制以满足其特定需求。协议与传输无关，可以在任何支持双向消息交换的通信通道上实现。

选择支持自定义传输的实现者**必须**确保它们保留了MCP定义的JSON-RPC消息格式和生命周期要求。自定义传输**应该**记录其特定的连接建立和消息交换模式，以帮助互操作性。


# 取消
来源：https://modelcontextprotocol.io/specification/2024-11-05/basic/utilities/cancellation


<Info>**协议修订版**: 2024-11-05</Info>

Model Context Protocol (MCP)通过通知消息支持可选的在途请求取消功能。任一方都可以发送取消通知，表示应终止先前发出的请求。

## 取消流程

当一方想要取消进行中的请求时，它会发送一个`notifications/cancelled`通知，包含：

* 要取消的请求ID
* 可选的可以记录或显示的原因字符串

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/cancelled",
  "params": {
    "requestId": "123",
    "reason": "用户请求取消"
  }
}
```

## 行为要求

1. 取消通知**必须**仅引用：
   * 先前在同一方向发出的请求
   * 被认为仍在进行中的请求
2. `initialize`请求**不能**被客户端取消
3. 取消通知的接收者**应该**：
   * 停止处理被取消的请求
   * 释放相关资源
   * 不为被取消的请求发送响应
4. 接收者**可以**忽略取消通知，如果：
   * 引用的请求未知
   * 处理已完成
   * 请求无法取消
5. 取消通知的发送者**应该**忽略之后到达的请求响应

## 时间考虑

由于网络延迟，取消通知可能在请求处理完成后到达，甚至可能在响应已经发送后到达。

双方**必须**优雅处理这些竞态条件：

```mermaid
sequenceDiagram
   participant 客户端
   participant 服务器

   客户端->>服务器: 请求(ID: 123)
   Note over 服务器: 处理开始
   客户端--)服务器: notifications/cancelled(ID: 123)
   alt
      Note over 服务器: 处理可能在<br/>取消到达前<br/>已完成
   else 如果未完成
      Note over 服务器: 停止处理
   end
```

## 实现说明

* 双方**应该**记录取消原因以便调试
* 应用程序UI**应该**在请求取消时显示指示

## 错误处理

无效的取消通知**应该**被忽略：

* 未知请求ID
* 已完成的请求
* 格式错误的通知

这保持了通知的"发送后不管"特性，同时允许异步通信中的竞态条件。


# 心跳检测
来源：https://modelcontextprotocol.io/specification/2024-11-05/basic/utilities/ping


<Info>**协议修订版**: 2024-11-05</Info>

Model Context Protocol包含可选的心跳检测机制，允许任一方验证对方是否仍然响应且连接存活。

## 概述

心跳功能通过简单的请求/响应模式实现。客户端或服务器都可以通过发送`ping`请求来发起心跳检测。

## 消息格式

心跳检测请求是一个没有参数的标准JSON-RPC请求：

```json
{
  "jsonrpc": "2.0",
  "id": "123",
  "method": "ping"
}
```

## 行为要求

1. 接收者**必须**立即响应一个空响应：

```json
{
  "jsonrpc": "2.0",
  "id": "123",
  "result": {}
}
```

2. 如果在合理超时期限内未收到响应，发送者**可以**：
   * 认为连接已失效
   * 终止连接
   * 尝试重新连接过程

## 使用模式

```mermaid
sequenceDiagram
    participant 发送方
    participant 接收方

    发送方->>接收方: ping请求
    接收方->>发送方: 空响应
```

## 实现考虑

* 实现**应该**定期发出心跳检测以检查连接健康状态
* 心跳频率**应该**可配置
* 超时**应该**适合网络环境
* **应该**避免过度心跳检测以减少网络开销

## 错误处理

* 超时**应该**被视为连接失败
* 多次失败的心跳检测**可以**触发连接重置
* 实现**应该**记录心跳检测失败以便诊断


# 进度
来源：https://modelcontextprotocol.io/specification/2024-11-05/basic/utilities/progress


<Info>**协议修订版**: 2024-11-05</Info>

Model Context Protocol (MCP)通过通知消息支持可选的长时操作进度跟踪。任一方都可以发送进度通知以提供操作状态更新。

## 进度流程

当一方想要*接收*请求的进度更新时，它在请求元数据中包含一个`progressToken`。

* 进度令牌**必须**是字符串或整数值
* 进度令牌可以由发送方选择任何方式生成，但**必须**在所有活动请求中唯一
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "some_method",
  "params": {
    "_meta": {
      "progressToken": "abc123"
    }
  }
}
```

接收者**可以**发送包含以下内容的进度通知：

* 原始进度令牌
* 当前进度值
* 可选的"total"总值

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/progress",
  "params": {
    "progressToken": "abc123",
    "progress": 50,
    "total": 100
  }
}
```

* `progress`值**必须**随每个通知递增，即使总值未知
* `progress`和`total`值**可以**是浮点数

## 行为要求

1. 进度通知**必须**仅引用：
   * 在活动请求中提供的令牌
   * 与进行中操作关联的令牌

2. 进度请求的接收者**可以**：
   * 选择不发送任何进度通知
   * 以他们认为合适的频率发送通知
   * 如果未知则省略总值

```mermaid
sequenceDiagram
    participant 发送方
    participant 接收方

    Note over 发送方,接收方: 带进度令牌的请求
    发送方->>接收方: 带progressToken的方法请求

    Note over 发送方,接收方: 进度更新
    loop 进度更新
        接收方-->>发送方: 进度通知(0.2/1.0)
        接收方-->>发送方: 进度通知(0.6/1.0)
        接收方-->>发送方: 进度通知(1.0/1.0)
    end

    Note over 发送方,接收方: 操作完成
    接收方->>发送方: 方法响应
```

## 实现说明

* 发送方和接收方**应该**跟踪活动进度令牌
* 双方**应该**实现速率限制以防止泛滥
* 进度通知**必须**在完成后停止


# 根目录
来源：https://modelcontextprotocol.io/specification/2024-11-05/client/roots


<Info>**协议修订版**: 2024-11-05</Info>

Model Context Protocol (MCP)提供了一种标准化方式，让客户端可以向服务器暴露文件系统"根目录"。根目录定义了服务器可以在文件系统中操作的边界，让它们了解可以访问哪些目录和文件。服务器可以从支持此功能的客户端请求根目录列表，并在列表更改时接收通知。

## 用户交互模型

MCP中的根目录通常通过工作区或项目配置界面暴露。

例如，实现可以提供工作区/项目选择器，允许用户选择服务器应有权访问的目录和文件。这可以与版本控制系统或项目文件的自动工作区检测相结合。

但是，实现可以自由地通过任何适合其需求的界面模式暴露根目录——协议本身不强制要求任何特定的用户交互模型。

## 能力

支持根目录的客户端**必须**在[初始化](/specification/2024-11-05/basic/lifecycle#initialization)时声明`roots`能力：

```json
{
  "capabilities": {
    "roots": {
      "listChanged": true
    }
  }
}
```

`listChanged`表示客户端是否会在根目录列表更改时发出通知。

## 协议消息

### 列出根目录

要检索根目录，服务器发送`roots/list`请求：

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "roots/list"
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "roots": [
      {
        "uri": "file:///home/user/projects/myproject",
        "name": "我的项目"
      }
    ]
  }
}
```

### 根目录列表变更

当根目录变更时，支持`listChanged`的客户端**必须**发送通知：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/roots/list_changed"
}
```

## 消息流

```mermaid
sequenceDiagram
    participant 服务器
    participant 客户端

    Note over 服务器,客户端: 发现
    服务器->>客户端: roots/list
    客户端-->>服务器: 可用根目录

    Note over 服务器,客户端: 变更
    客户端--)服务器: notifications/roots/list_changed
    服务器->>客户端: roots/list
    客户端-->>服务器: 更新后的根目录
```

## 数据类型

### 根目录

根目录定义包括：

* `uri`: 根目录的唯一标识符。在当前规范中**必须**是`file://` URI
* `name`: 用于显示的可选人类可读名称
不同用例的根目录示例：

#### 项目目录

```json
{
  "uri": "file:///home/user/projects/myproject",
  "name": "我的项目"
}
```

#### 多个代码库

```json
[
  {
    "uri": "file:///home/user/repos/frontend",
    "name": "前端代码库"
  },
  {
    "uri": "file:///home/user/repos/backend",
    "name": "后端代码库"
  }
]
```

## 错误处理

客户端**应该**为常见失败情况返回标准JSON-RPC错误：

* 客户端不支持根目录：`-32601` (方法未找到)
* 内部错误：`-32603`

错误示例：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32601,
    "message": "不支持根目录",
    "data": {
      "reason": "客户端不具备根目录能力"
    }
  }
}
```

## 安全考虑

1. 客户端**必须**：
   * 仅暴露具有适当权限的根目录
   * 验证所有根目录URI以防止路径遍历
   * 实现适当的访问控制
   * 监控根目录可访问性

2. 服务器**应该**：
   * 处理根目录不可用的情况
   * 在操作中尊重根目录边界
   * 根据提供的根目录验证所有路径

## 实现指南

1. 客户端**应该**：
   * 在向服务器暴露根目录前获取用户同意
   * 提供清晰的根目录管理用户界面
   * 在暴露前验证根目录可访问性
   * 监控根目录变更

2. 服务器**应该**：
   * 使用前检查根目录能力
   * 优雅处理根目录列表变更
   * 在操作中尊重根目录边界
   * 适当缓存根目录信息


# 采样
来源：https://modelcontextprotocol.io/specification/2024-11-05/client/sampling


<Info>**协议修订版**: 2024-11-05</Info>

Model Context Protocol (MCP)提供了一种标准化方式，让服务器可以通过客户端请求LLM采样("补全"或"生成")。这种流程允许客户端保持对模型访问、选择和权限的控制，同时使服务器能够利用AI能力——无需服务器API密钥。服务器可以请求基于文本或图像的交互，并可选地在提示中包含来自MCP服务器的上下文。

## 用户交互模型

MCP中的采样允许服务器通过在其他MCP服务器功能中*嵌套*LLM调用来实现代理行为。

实现可以自由地通过任何适合其需求的界面模式暴露采样——协议本身不强制要求任何特定的用户交互模型。

<Warning>
  为了信任与安全，**应该**始终有人参与其中，并能够拒绝采样请求。

  应用程序**应该**：
  
  * 提供易于直观地审查采样请求的UI
  * 允许用户在发送前查看和编辑提示
  * 在交付前展示生成的响应以供审查
</Warning>

## 能力

支持采样的客户端**必须**在[初始化](/specification/2024-11-05/basic/lifecycle#initialization)时声明`sampling`能力：

```json
{
  "capabilities": {
    "sampling": {}
  }
}
```

## 协议消息

### 创建消息

要请求语言模型生成，服务器发送`sampling/createMessage`请求：

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "法国的首都是哪里？"
        }
      }
    ],
    "modelPreferences": {
      "hints": [
        {
          "name": "claude-3-sonnet"
        }
      ],
      "intelligencePriority": 0.8,
      "speedPriority": 0.5
    },
    "systemPrompt": "你是一个乐于助人的助手。",
    "maxTokens": 100
  }
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "role": "assistant",
    "content": {
      "type": "text",
      "text": "法国的首都是巴黎。"
    },
    "model": "claude-3-sonnet-20240307",
    "stopReason": "endTurn"
  }
}
```

## 消息流

```mermaid
sequenceDiagram
participant 服务器
    participant 客户端
    participant 用户
    participant LLM

    Note over 服务器,客户端: 服务器发起采样
    服务器->>客户端: sampling/createMessage

    Note over 客户端,用户: 人工审核环节
    客户端->>用户: 展示请求等待批准
    用户-->>客户端: 审核并批准/修改

    Note over 客户端,LLM: 模型交互
    客户端->>LLM: 转发批准的请求
    LLM-->>客户端: 返回生成结果

    Note over 客户端,用户: 响应审核
    客户端->>用户: 展示响应等待批准
    用户-->>客户端: 审核并批准/修改

    Note over 服务器,客户端: 完成请求
    客户端-->>服务器: 返回批准的响应
```

## 数据类型

### 消息

采样消息可以包含：

#### 文本内容

```json
{
  "type": "text",
  "text": "消息内容"
}
```

#### 图像内容

```json
{
  "type": "image",
  "data": "base64编码的图像数据",
  "mimeType": "image/jpeg"
}
```

### 模型偏好

MCP中的模型选择需要谨慎抽象，因为服务器和客户端可能使用不同的AI提供商和模型。服务器不能简单地按名称请求特定模型，因为客户端可能无法访问该模型或可能更喜欢使用不同提供商的等效模型。

为此，MCP实现了一个结合抽象能力优先级和可选模型提示的偏好系统：

#### 能力优先级

服务器通过三个标准化优先级值(0-1)表达需求：

* `costPriority`: 最小化成本的重要性？值越高偏好更便宜的模型
* `speedPriority`: 低延迟的重要性？值越高偏好更快的模型
* `intelligencePriority`: 高级能力的重要性？值越高偏好能力更强的模型

#### 模型提示

虽然优先级帮助基于特性选择模型，但`hints`允许服务器建议特定模型或模型系列：

* 提示被视为可以灵活匹配模型名称的子字符串
* 多个提示按偏好顺序评估
* 客户端**可以**将提示映射到不同提供商的等效模型
* 提示是建议性的——客户端做出最终模型选择

例如：

```json
{
  "hints": [
    { "name": "claude-3-sonnet" }, // 偏好Sonnet类模型
    { "name": "claude" } // 回退到任何Claude模型
  ],
  "costPriority": 0.3, // 成本不太重要
  "speedPriority": 0.8, // 速度非常重要
  "intelligencePriority": 0.5 // 中等能力需求
}
```

客户端处理这些偏好从其可用选项中选择合适的模型。例如，如果客户端无法访问Claude模型但有Gemini，它可能基于相似能力将sonnet提示映射到`gemini-1.5-pro`。

## 错误处理

客户端**应该**为常见失败情况返回错误：

错误示例：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -1,
    "message": "用户拒绝了采样请求"
  }
}
```

## 安全考虑

1. 客户端**应该**实现用户批准控制
2. 双方**应该**验证消息内容
3. 客户端**应该**尊重模型偏好提示
4. 客户端**应该**实现速率限制
5. 双方**必须**妥善处理敏感数据


# 规范
来源：https://modelcontextprotocol.io/specification/2024-11-05/index


[Model Context Protocol](https://modelcontextprotocol.io) (MCP)是一个开放协议，使LLM应用程序与外部数据源和工具之间能够无缝集成。无论您是在构建AI驱动的IDE、增强聊天界面还是创建自定义AI工作流，MCP都提供了一种标准化方式将LLM与它们所需的上下文连接起来。

本规范定义了权威的协议要求，基于TypeScript模式定义[schema.ts](https://github.com/modelcontextprotocol/specification/blob/main/schema/2024-11-05/schema.ts)。

有关实现指南和示例，请访问[modelcontextprotocol.io](https://modelcontextprotocol.io)。

本文件中的关键词"MUST"、"MUST NOT"、"REQUIRED"、"SHALL"、"SHALL NOT"、"SHOULD"、"SHOULD NOT"、"RECOMMENDED"、"NOT RECOMMENDED"、"MAY"和"OPTIONAL"应按照[BCP 14](https://datatracker.ietf.org/doc/html/bcp14) \[[RFC2119](https://datatracker.ietf.org/doc/html/rfc2119)] \[[RFC8174](https://datatracker.ietf.org/doc/html/rfc8174)]中描述的方式解释，当且仅当它们以全大写形式出现时，如本文所示。

## 概述

MCP为应用程序提供了一种标准化方式来：

* 与语言模型共享上下文信息
* 向AI系统暴露工具和能力
* 构建可组合的集成和工作流

该协议使用[JSON-RPC](https://www.jsonrpc.org/) 2.0消息在以下组件之间建立通信：

* **主机(Hosts)**: 发起连接的LLM应用程序
* **客户端(Clients)**: 主机应用程序内的连接器
* **服务器(Servers)**: 提供上下文和能力的服务

MCP部分灵感来自[语言服务器协议](https://microsoft.github.io/language-server-protocol/)，该协议标准化了如何在整个开发工具生态系统中添加编程语言支持。类似地，MCP标准化了如何将额外上下文和工具集成到AI应用程序生态系统中。

## 关键细节

### 基础协议

* [JSON-RPC](https://www.jsonrpc.org/)消息格式
* 有状态连接
* 服务器和客户端能力协商

### 功能

服务器向客户端提供以下任何功能：

* **资源(Resources)**: 供用户或AI模型使用的上下文和数据
* **提示(Prompts)**: 为用户提供的模板化消息和工作流
* **工具(Tools)**: 供AI模型执行的函数

客户端可以向服务器提供以下功能：

* **采样(Sampling)**: 服务器发起的代理行为和递归LLM交互
### 附加工具

* 配置
* 进度跟踪
* 取消操作
* 错误报告
* 日志记录

## 安全与信任保障

Model Context Protocol通过任意数据访问和代码执行路径实现了强大的能力。伴随着这种能力而来的是所有实现者必须仔细解决的重要安全和信任考虑。

### 关键原则

1. **用户同意与控制**
   * 用户必须明确同意并理解所有数据访问和操作
   * 用户必须保留对共享数据和执行操作的控制权
   * 实现者应提供清晰的UI用于审查和授权活动

2. **数据隐私**
   * 主机必须在向服务器暴露用户数据前获得明确同意
   * 主机不得未经用户同意将资源数据传输到其他地方
   * 用户数据应受到适当的访问控制保护

3. **工具安全**
   * 工具代表任意代码执行，必须谨慎对待
   * 主机必须在调用任何工具前获得明确用户同意
   * 用户应在授权使用前了解每个工具的功能

4. **LLM采样控制**
   * 用户必须明确批准任何LLM采样请求
   * 用户应控制：
     * 是否进行采样
     * 实际发送的提示内容
     * 服务器可以看到的结果
   * 协议有意限制服务器对提示的可见性

### 实现指南

虽然MCP本身无法在协议层面强制执行这些安全原则，但实现者**应该**：

1. 在应用中构建强大的同意和授权流程
2. 提供清晰的安全影响文档
3. 实施适当的访问控制和数据保护
4. 在集成中遵循安全最佳实践
5. 在功能设计中考虑隐私影响

## 了解更多

探索每个协议组件的详细规范：

<CardGroup cols={5}>
  <Card title="架构" icon="sitemap" href="architecture" />

  <Card title="基础协议" icon="code" href="basic" />

  <Card title="服务器功能" icon="server" href="server" />

  <Card title="客户端功能" icon="user" href="client" />

  <Card title="贡献指南" icon="pencil" href="contributing" />
</CardGroup>


# 概述
来源：https://modelcontextprotocol.io/specification/2024-11-05/server/index


<Info>**协议修订版**: 2024-11-05</Info>

服务器通过MCP为语言模型添加上下文提供了基本构建块。这些原语实现了客户端、服务器和语言模型之间的丰富交互：

* **提示(Prompts)**: 指导语言模型交互的预定义模板或指令
* **资源(Resources)**: 为模型提供额外上下文的结构化数据或内容
* **工具(Tools)**: 允许模型执行操作或检索信息的可执行函数

每个原语可以总结为以下控制层次结构：

| 原语     | 控制方式               | 描述                                         | 示例                          |
| -------- | ---------------------- | -------------------------------------------- | ----------------------------- |
| 提示     | 用户控制               | 通过用户选择调用的交互式模板                 | 斜杠命令、菜单选项            |
| 资源     | 应用控制               | 客户端附加和管理的上下文数据                 | 文件内容、git历史             |
| 工具     | 模型控制               | 暴露给LLM执行操作的函数                      | API POST请求、文件写入        |

深入了解这些关键原语：

<CardGroup cols={3}>
  <Card title="提示" icon="message" href="prompts" />

  <Card title="资源" icon="file-lines" href="resources" />

  <Card title="工具" icon="wrench" href="tools" />
</CardGroup>


# 提示
来源：https://modelcontextprotocol.io/specification/2024-11-05/server/prompts


<Info>**协议修订版**: 2024-11-05</Info>

Model Context Protocol (MCP)提供了一种标准化方式，让服务器可以向客户端暴露提示模板。提示允许服务器提供结构化消息和指令来与语言模型交互。客户端可以发现可用提示、检索其内容并提供参数来自定义它们。

## 用户交互模型

提示设计为**用户控制**，意味着它们从服务器暴露给客户端时，目的是让用户能够明确选择使用它们。

通常，提示会通过用户界面中用户发起的命令触发，这使用户能够自然地发现和调用可用提示。

例如，作为斜杠命令：

![作为斜杠命令暴露的提示示例](https://mintlify.s3.us-west-1.amazonaws.com/mcp/specification/2024-11-05/server/slash-command.png)

然而，实现者可以自由地通过任何适合其需求的界面模式暴露提示——协议本身不强制要求任何特定的用户交互模型。

## 能力

支持提示的服务器**必须**在[初始化](/specification/2024-11-05/basic/lifecycle#initialization)时声明`prompts`能力：

```json
{
  "capabilities": {
    "prompts": {
      "listChanged": true
    }
  }
}
```

`listChanged`表示服务器是否会在可用提示列表更改时发出通知。

## 协议消息

### 列出提示

要检索可用提示，客户端发送`prompts/list`请求。此操作支持[分页](/specification/2024-11-05/server/utilities/pagination)。

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "prompts/list",
  "params": {
    "cursor": "optional-cursor-value"
  }
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "prompts": [
      {
        "name": "code_review",
        "description": "要求LLM分析代码质量并提出改进建议",
        "arguments": [
{
            "name": "code",
            "description": "要审查的代码",
            "required": true
          }
        ]
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}
```

### 获取提示

要检索特定提示，客户端发送`prompts/get`请求。参数可以通过[补全API](/specification/2024-11-05/server/utilities/completion)自动完成。

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "prompts/get",
  "params": {
    "name": "code_review",
    "arguments": {
      "code": "def hello():\n    print('world')"
    }
  }
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "description": "代码审查提示",
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "请审查这段Python代码:\ndef hello():\n    print('world')"
        }
      }
    ]
  }
}
```

### 列表变更通知

当可用提示列表变更时，声明了`listChanged`能力的服务器**应该**发送通知：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/prompts/list_changed"
}
```

## 消息流

```mermaid
sequenceDiagram
    participant 客户端
    participant 服务器

    Note over 客户端,服务器: 发现
    客户端->>服务器: prompts/list
    服务器-->>客户端: 提示列表

    Note over 客户端,服务器: 使用
    客户端->>服务器: prompts/get
    服务器-->>客户端: 提示内容

    opt listChanged
      Note over 客户端,服务器: 变更
      服务器--)客户端: prompts/list_changed
      客户端->>服务器: prompts/list
      服务器-->>客户端: 更新后的提示
    end
```

## 数据类型

### 提示

提示定义包括：
* `name`: 提示的唯一标识符
* `description`: 可选的人类可读描述
* `arguments`: 可选的定制参数列表

### 提示消息

提示中的消息可以包含：
* `role`: "user"或"assistant"表示说话者
* `content`: 以下内容类型之一：

#### 文本内容

文本内容表示纯文本消息：

```json
{
  "type": "text",
  "text": "消息的文本内容"
}
```

这是用于自然语言交互的最常见内容类型。

#### 图像内容

图像内容允许在消息中包含视觉信息：

```json
{
  "type": "image",
  "data": "base64编码的图像数据",
  "mimeType": "image/png"
}
```

图像数据**必须**是base64编码并包含有效的MIME类型。这使得在视觉上下文重要时可以进行多模态交互。

#### 嵌入式资源

嵌入式资源允许在消息中直接引用服务器端资源：

```json
{
  "type": "resource",
  "resource": {
    "uri": "resource://example",
    "mimeType": "text/plain",
    "text": "资源内容"
  }
}
```

资源可以包含文本或二进制(blob)数据，并且**必须**包括：
* 有效的资源URI
* 适当的MIME类型
* 文本内容或base64编码的blob数据

嵌入式资源使提示能够无缝地将服务器管理的内容(如文档、代码示例或其他参考资料)直接整合到对话流程中。

## 错误处理

服务器**应该**为常见失败情况返回标准JSON-RPC错误：
* 无效提示名称：`-32602` (无效参数)
* 缺少必需参数：`-32602` (无效参数)
* 内部错误：`-32603` (内部错误)

## 实现考虑

1. 服务器**应该**在处理前验证提示参数
2. 客户端**应该**处理大型提示列表的分页
3. 双方**应该**尊重能力协商

## 安全

实现**必须**仔细验证所有提示输入和输出，以防止注入攻击或对资源的未授权访问。


# 资源
来源：https://modelcontextprotocol.io/specification/2024-11-05/server/resources


<Info>**协议修订版**: 2024-11-05</Info>
Model Context Protocol (MCP)提供了一种标准化方式，让服务器可以向客户端暴露资源。资源允许服务器共享为语言模型提供上下文的数据，如文件、数据库模式或应用特定信息。每个资源由[URI](https://datatracker.ietf.org/doc/html/rfc3986)唯一标识。

## 用户交互模型

MCP中的资源设计为**应用驱动**，由主机应用根据需求决定如何整合上下文。

例如，应用可以：
* 通过UI元素(树状或列表视图)暴露资源供显式选择
* 允许用户搜索和过滤可用资源
* 基于启发式或AI模型选择实现自动上下文包含

![资源选择器示例](https://mintlify.s3.us-west-1.amazonaws.com/mcp/specification/2024-11-05/server/resource-picker.png)

然而，实现可以自由地通过任何适合其需求的界面模式暴露资源——协议本身不强制要求任何特定的用户交互模型。

## 能力

支持资源的服务器**必须**声明`resources`能力：

```json
{
  "capabilities": {
    "resources": {
      "subscribe": true,
      "listChanged": true
    }
  }
}
```

该能力支持两个可选特性：
* `subscribe`: 客户端是否可以订阅接收单个资源变更通知
* `listChanged`: 服务器是否会在可用资源列表变更时发出通知

`subscribe`和`listChanged`都是可选的——服务器可以都不支持、支持其中一个或两者都支持：

```json
{
  "capabilities": {
    "resources": {} // 两个特性都不支持
  }
}
```

```json
{
  "capabilities": {
    "resources": {
      "subscribe": true // 仅支持订阅
    }
  }
}
```

```json
{
  "capabilities": {
    "resources": {
      "listChanged": true // 仅支持列表变更通知
    }
  }
}
```

## 协议消息

### 列出资源

要发现可用资源，客户端发送`resources/list`请求。此操作支持[分页](/specification/2024-11-05/server/utilities/pagination)。

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "resources/list",
  "params": {
    "cursor": "optional-cursor-value"
  }
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "resources": [
      {
        "uri": "file:///project/src/main.rs",
        "name": "main.rs",
        "description": "主要应用入口点",
        "mimeType": "text/x-rust"
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}
```

### 读取资源

要检索资源内容，客户端发送`resources/read`请求：

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "resources/read",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "contents": [
      {
        "uri": "file:///project/src/main.rs",
        "mimeType": "text/x-rust",
        "text": "fn main() {\n    println!(\"Hello world!\");\n}"
      }
    ]
  }
}
```

### 资源模板

资源模板允许服务器使用[URI模板](https://datatracker.ietf.org/doc/html/rfc6570)暴露参数化资源。参数可以通过[补全API](/specification/2024-11-05/server/utilities/completion)自动完成。

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "resources/templates/list"
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "resourceTemplates": [
      {
        "uriTemplate": "file:///{path}",
        "name": "项目文件",
        "description": "访问项目目录中的文件",
        "mimeType": "application/octet-stream"
      }
    ]
  }
}
### 列表变更通知

当可用资源列表变更时，声明了`listChanged`能力的服务器**应该**发送通知：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/list_changed"
}
```

### 订阅

协议支持可选的资源变更订阅。客户端可以订阅特定资源并在它们变更时接收通知：

**订阅请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "method": "resources/subscribe",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}
```

**更新通知：**

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/updated",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}
```

## 消息流

```mermaid
sequenceDiagram
    participant 客户端
    participant 服务器

    Note over 客户端,服务器: 资源发现
    客户端->>服务器: resources/list
    服务器-->>客户端: 资源列表

    Note over 客户端,服务器: 资源访问
    客户端->>服务器: resources/read
    服务器-->>客户端: 资源内容

    Note over 客户端,服务器: 订阅
    客户端->>服务器: resources/subscribe
    服务器-->>客户端: 订阅确认

    Note over 客户端,服务器: 更新
    服务器--)客户端: notifications/resources/updated
    客户端->>服务器: resources/read
    服务器-->>客户端: 更新后的内容
```

## 数据类型

### 资源

资源定义包括：
* `uri`: 资源的唯一标识符
* `name`: 人类可读名称
* `description`: 可选描述
* `mimeType`: 可选MIME类型

### 资源内容

资源可以包含文本或二进制数据：

#### 文本内容

```json
{
  "uri": "file:///example.txt",
  "mimeType": "text/plain",
  "text": "资源内容"
}
```

#### 二进制内容

```json
{
  "uri": "file:///example.png",
  "mimeType": "image/png",
  "blob": "base64编码数据"
}
```

## 常见URI方案

协议定义了几种标准URI方案。此列表并非详尽无遗——实现总是可以自由使用额外的自定义URI方案。

### https\://

用于表示网络上可用的资源。

服务器**应该**仅在客户端能够自行从网络获取和加载资源时使用此方案——即不需要通过MCP服务器读取资源。

对于其他用例，服务器**应该**优先使用另一个URI方案，或定义一个自定义方案，即使服务器本身将通过互联网下载资源内容。

### file://

用于标识行为类似文件系统的资源。然而，资源不需要映射到实际的物理文件系统。

MCP服务器**可以**使用[XDG MIME类型](https://specifications.freedesktop.org/shared-mime-info-spec/0.14/ar01s02.html#id-1.3.14)标识file://资源，如`inode/directory`，来表示没有标准MIME类型的非常规文件(如目录)。

### git://

Git版本控制集成。

## 错误处理

服务器**应该**为常见失败情况返回标准JSON-RPC错误：
* 资源未找到：`-32002`
* 内部错误：`-32603`

错误示例：

```json
{
  "jsonrpc": "2.0",
  "id": 5,
  "error": {
    "code": -32002,
    "message": "资源未找到",
    "data": {
      "uri": "file:///nonexistent.txt"
    }
  }
}
```

## 安全考虑

1. 服务器**必须**验证所有资源URI
2. **应该**为敏感资源实现访问控制
3. 二进制数据**必须**正确编码
4. **应该**在操作前检查资源权限


# 工具
来源：https://modelcontextprotocol.io/specification/2024-11-05/server/tools


<Info>**协议修订版**: 2024-11-05</Info>

Model Context Protocol (MCP)允许服务器暴露可由语言模型调用的工具。工具使模型能够与外部系统交互，如查询数据库、调用API或执行计算。每个工具由名称唯一标识，并包含描述其模式的元数据。

## 用户交互模型

MCP中的工具设计为**模型控制**，意味着语言模型可以根据其上下文理解力和用户提示自动发现和调用工具。

然而，实现可以自由地通过任何适合其需求的界面模式暴露工具——协议本身不强制要求任何特定的用户交互模型。

<Warning>
为了信任、安全和保障，**应该**始终有人参与工具调用过程，并保留拒绝调用的能力。

应用**应该**：
* 提供明确显示暴露给AI模型的工具的UI
* 在工具调用时插入清晰的视觉指示器
* 向用户展示操作确认提示，确保有人参与决策
</Warning>

## 能力

支持工具的服务器**必须**声明`tools`能力：

```json
{
  "capabilities": {
    "tools": {
      "listChanged": true
    }
  }
}
```

`listChanged`表示服务器是否会在可用工具列表变更时发出通知。

## 协议消息

### 列出工具

要发现可用工具，客户端发送`tools/list`请求。此操作支持[分页](/specification/2024-11-05/server/utilities/pagination)。

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {
    "cursor": "optional-cursor-value"
  }
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "get_weather",
        "description": "获取指定位置的当前天气信息",
        "inputSchema": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "城市名称或邮政编码"
            }
          },
          "required": ["location"]
        }
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}
```

### 调用工具

要调用工具，客户端发送`tools/call`请求：

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": {
      "location": "New York"
    }
  }
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "纽约当前天气：\n温度：72°F\n天气状况：局部多云"
      }
    ],
    "isError": false
  }
}
```

### 列表变更通知

当可用工具列表变更时，声明了`listChanged`能力的服务器**应该**发送通知：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/tools/list_changed"
}
```

## 消息流

```mermaid
sequenceDiagram
    participant LLM
    participant 客户端
    participant 服务器

    Note over 客户端,服务器: 发现
    客户端->>服务器: tools/list
    服务器-->>客户端: 工具列表

    Note over 客户端,LLM: 工具选择
    LLM->>客户端: 选择要使用的工具

    Note over 客户端,服务器: 调用
    客户端->>服务器: tools/call
    服务器-->>客户端: 工具结果
    客户端->>LLM: 处理结果

    Note over 客户端,服务器: 更新
    服务器--)客户端: tools/list_changed
    客户端->>服务器: tools/list
    服务器-->>客户端: 更新后的工具
```

## 数据类型

### 工具

工具定义包括：
* `name`: 工具的唯一标识符
* `description`: 功能的人类可读描述
* `inputSchema`: 定义预期参数的JSON模式

### 工具结果

工具结果可以包含多种类型的内容项：

#### 文本内容

```json
{
  "type": "text",
  "text": "工具结果文本"
}
```

#### 图像内容

```json
{
  "type": "image",
  "data": "base64编码数据",
  "mimeType": "image/png"
}
```

#### 嵌入式资源
[资源](/specification/2024-11-05/server/resources)**可以**被嵌入，以提供额外的上下文或数据，通过一个客户端可以稍后订阅或获取的URI：

```json
{
  "type": "resource",
  "resource": {
    "uri": "resource://example",
    "mimeType": "text/plain",
    "text": "资源内容"
  }
}
```

## 错误处理

工具使用两种错误报告机制：

1. **协议错误**：标准JSON-RPC错误，用于：
   * 未知工具
   * 无效参数
   * 服务器错误

2. **工具执行错误**：在工具结果中用`isError: true`报告：
   * API失败
   * 无效输入数据
   * 业务逻辑错误

协议错误示例：

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "error": {
    "code": -32602,
    "message": "未知工具：invalid_tool_name"
  }
}
```

工具执行错误示例：

```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "获取天气数据失败：API速率限制已超出"
      }
    ],
    "isError": true
  }
}
```

## 安全考虑

1. 服务器**必须**：
   * 验证所有工具输入
   * 实现适当的访问控制
   * 对工具调用进行速率限制
   * 对工具输出进行清理

2. 客户端**应该**：
   * 对敏感操作提示用户确认
   * 在调用服务器前向用户显示工具输入，避免恶意或意外数据泄露
   * 在传递给LLM前验证工具结果
   * 为工具调用实现超时
   * 记录工具使用情况用于审计


# 自动补全
来源：https://modelcontextprotocol.io/specification/2024-11-05/server/utilities/completion


<Info>**协议修订版**: 2024-11-05</Info>

Model Context Protocol (MCP)提供了一种标准化方式，让服务器可以为提示和资源URI提供参数自动补全建议。这实现了丰富的、类似IDE的体验，用户在输入参数值时可以获得上下文相关的建议。

## 用户交互模型

MCP中的自动补全设计用于支持类似IDE代码补全的交互式用户体验。

例如，应用可以在用户输入时以下拉菜单或弹出窗口显示补全建议，并能够过滤和选择可用选项。

然而，实现可以自由地通过任何适合其需求的界面模式暴露自动补全功能——协议本身不强制要求任何特定的用户交互模型。

## 协议消息

### 请求补全

要获取补全建议，客户端发送`completion/complete`请求，通过引用类型指定要补全的内容：

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "completion/complete",
  "params": {
    "ref": {
      "type": "ref/prompt",
      "name": "code_review"
    },
    "argument": {
      "name": "language",
      "value": "py"
    }
  }
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "completion": {
      "values": ["python", "pytorch", "pyside"],
      "total": 10,
      "hasMore": true
    }
  }
}
```

### 引用类型

协议支持两种补全引用类型：

| 类型           | 描述                 | 示例                                             |
| -------------- | ------------------- | ----------------------------------------------- |
| `ref/prompt`   | 按名称引用提示       | `{"type": "ref/prompt", "name": "code_review"}` |
| `ref/resource` | 引用资源URI          | `{"type": "ref/resource", "uri": "file:///{path}"}` |

### 补全结果

服务器返回按相关性排序的补全值数组，包含：
* 每个响应最多100项
* 可选的可用匹配总数
* 布尔值指示是否存在更多结果

## 消息流

```mermaid
sequenceDiagram
    participant 客户端
    participant 服务器

    Note over 客户端: 用户输入参数
    客户端->>服务器: completion/complete
    服务器-->>客户端: 补全建议

    Note over 客户端: 用户继续输入
    客户端->>服务器: completion/complete
    服务器-->>客户端: 精炼后的建议
```

## 数据类型

### CompleteRequest

* `ref`: `PromptReference`或`ResourceReference`
* `argument`: 包含以下字段的对象：
  * `name`: 参数名
  * `value`: 当前值
### CompleteResult

* `completion`: 包含以下字段的对象：
  * `values`: 建议值数组（最多100个）
  * `total`: 可选的匹配总数
  * `hasMore`: 是否有更多结果的标志

## 实现考虑

1. 服务器**应该**：
   * 按相关性排序返回建议
   * 在适当情况下实现模糊匹配
   * 对补全请求进行速率限制
   * 验证所有输入

2. 客户端**应该**：
   * 对快速补全请求进行防抖处理
   * 在适当情况下缓存补全结果
   * 优雅处理缺失或不完整的结果

## 安全

实现**必须**：
* 验证所有补全输入
* 实施适当的速率限制
* 控制对敏感建议的访问
* 防止基于补全的信息泄露


# 日志记录
来源：https://modelcontextprotocol.io/specification/2024-11-05/server/utilities/logging


<Info>**协议修订版**: 2024-11-05</Info>

Model Context Protocol (MCP)提供了一种标准化方式，让服务器可以向客户端发送结构化日志消息。客户端可以通过设置最低日志级别来控制日志详细程度，服务器发送包含严重级别、可选记录器名称和任意JSON可序列化数据的通知。

## 用户交互模型

实现可以自由地通过任何适合其需求的界面模式暴露日志功能——协议本身不强制要求任何特定的用户交互模型。

## 能力

发送日志消息通知的服务器**必须**声明`logging`能力：

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

## 日志级别

协议遵循[RFC 5424](https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1)中定义的标准syslog严重级别：

| 级别      | 描述                       | 示例用例                   |
| --------- | ------------------------- | ------------------------- |
| debug     | 详细的调试信息             | 函数入口/出口点            |
| info      | 一般信息性消息             | 操作进度更新               |
| notice    | 正常但重要的事件           | 配置变更                   |
| warning   | 警告条件                   | 已弃用功能使用             |
| error     | 错误条件                   | 操作失败                   |
| critical  | 严重条件                   | 系统组件故障               |
| alert     | 必须立即采取行动           | 检测到数据损坏             |
| emergency | 系统不可用                 | 完全系统故障               |

## 协议消息

### 设置日志级别

要配置最低日志级别，客户端**可以**发送`logging/setLevel`请求：

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "logging/setLevel",
  "params": {
    "level": "info"
  }
}
```

### 日志消息通知

服务器使用`notifications/message`通知发送日志消息：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/message",
  "params": {
    "level": "error",
    "logger": "database",
    "data": {
      "error": "连接失败",
      "details": {
        "host": "localhost",
        "port": 5432
      }
    }
  }
}
```

## 消息流

```mermaid
sequenceDiagram
    participant 客户端
    participant 服务器

    Note over 客户端,服务器: 配置日志
    客户端->>服务器: logging/setLevel (info)
    服务器-->>客户端: 空结果

    Note over 客户端,服务器: 服务器活动
    服务器--)客户端: notifications/message (info)
    服务器--)客户端: notifications/message (warning)
    服务器--)客户端: notifications/message (error)

    Note over 客户端,服务器: 级别变更
    客户端->>服务器: logging/setLevel (error)
    服务器-->>客户端: 空结果
    Note over 服务器: 仅发送错误级别<br/>及以上消息
```

## 错误处理

服务器**应该**为常见失败情况返回标准JSON-RPC错误：
* 无效日志级别：`-32602`（无效参数）
* 配置错误：`-32603`（内部错误）

## 实现考虑

1. 服务器**应该**：
   * 对日志消息进行速率限制
   * 在data字段中包含相关上下文
   * 使用一致的记录器名称
   * 移除敏感信息

2. 客户端**可以**：
   * 在UI中展示日志消息
   * 实现日志过滤/搜索
   * 可视化显示严重级别
   * 持久化日志消息

## 安全

1. 日志消息**不得**包含：
   * 凭据或密钥
   * 个人身份信息
   * 可能帮助攻击的内部系统详情

2. 实现**应该**：
   * 对消息进行速率限制
   * 验证所有数据字段
   * 控制日志访问
   * 监控敏感内容


# 分页
来源：https://modelcontextprotocol.io/specification/2024-11-05/server/utilities/pagination


<Info>**协议修订版**: 2024-11-05</Info>

Model Context Protocol (MCP)支持对可能返回大结果集的操作进行分页。分页允许服务器以较小的块返回结果，而不是一次性返回所有结果。
分页在通过互联网连接外部服务时特别重要，但对于本地集成也很有用，可以避免大数据集带来的性能问题。

## 分页模型

MCP中的分页使用不透明的基于游标的方法，而不是编号页面：

* **游标**是一个不透明的字符串令牌，表示结果集中的位置
* **页面大小**由服务器决定，客户端**不得**假设固定的页面大小

## 响应格式

当服务器发送包含以下内容的**响应**时，分页开始：
* 当前页面的结果
* 如果存在更多结果，可选的`nextCursor`字段

```json
{
  "jsonrpc": "2.0",
  "id": "123",
  "result": {
    "resources": [...],
    "nextCursor": "eyJwYWdlIjogM30="
  }
}
```

## 请求格式

收到游标后，客户端可以通过发出包含该游标的请求来*继续*分页：

```json
{
  "jsonrpc": "2.0",
  "method": "resources/list",
  "params": {
    "cursor": "eyJwYWdlIjogMn0="
  }
}
```

## 分页流程

```mermaid
sequenceDiagram
    participant 客户端
    participant 服务器

    客户端->>服务器: 列表请求(无游标)
    loop 分页循环
      服务器-->>客户端: 结果页 + nextCursor
      客户端->>服务器: 列表请求(带游标)
    end
```

## 支持分页的操作

以下MCP操作支持分页：
* `resources/list` - 列出可用资源
* `resources/templates/list` - 列出资源模板
* `prompts/list` - 列出可用提示
* `tools/list` - 列出可用工具

## 实现指南

1. 服务器**应该**：
   * 提供稳定的游标
   * 优雅处理无效游标

2. 客户端**应该**：
   * 将缺少`nextCursor`视为结果结束
   * 支持分页和非分页流程

3. 客户端**必须**将游标视为不透明令牌：
   * 不要对游标格式做假设
   * 不要尝试解析或修改游标
   * 不要跨会话持久化游标

## 错误处理

无效游标**应该**导致返回错误代码-32602（无效参数）。


# 架构
来源：https://modelcontextprotocol.io/specification/2025-03-26/architecture/index


Model Context Protocol (MCP)遵循客户端-主机-服务器架构，每个主机可以运行多个客户端实例。这种架构使用户能够在应用程序中集成AI功能，同时保持清晰的安全边界和隔离关注点。基于JSON-RPC构建，MCP提供了专注于客户端和服务器之间上下文交换和采样协调的有状态会话协议。

## 核心组件

```mermaid
graph LR
    subgraph "应用主机进程"
        H[主机]
        C1[客户端1]
        C2[客户端2]
        C3[客户端3]
        H --> C1
        H --> C2
        H --> C3
    end

    subgraph "本地机器"
        S1[服务器1<br>文件 & Git]
        S2[服务器2<br>数据库]
        R1[("本地<br>资源A")]
        R2[("本地<br>资源B")]

        C1 --> S1
        C2 --> S2
        S1 <--> R1
        S2 <--> R2
    end

    subgraph "互联网"
        S3[服务器3<br>外部API]
        R3[("远程<br>资源C")]

        C3 --> S3
        S3 <--> R3
    end
```

### 主机

主机进程充当容器和协调器：
* 创建和管理多个客户端实例
* 控制客户端连接权限和生命周期
* 强制执行安全策略和同意要求
* 处理用户授权决策
* 协调AI/LLM集成和采样
* 管理跨客户端的上下文聚合

### 客户端

每个客户端由主机创建并维护独立的服务器连接：
* 每个服务器建立一个有状态会话
* 处理协议协商和能力交换
* 双向路由协议消息
* 管理订阅和通知
* 维护服务器之间的安全边界

主机应用程序创建并管理多个客户端，每个客户端与特定服务器保持1:1关系。

### 服务器

服务器提供专门的上下文和能力：
* 通过MCP原语暴露资源、工具和提示
* 独立运行，职责明确
* 通过客户端接口请求采样
* 必须遵守安全约束
* 可以是本地进程或远程服务

## 设计原则

MCP基于几个关键设计原则构建，这些原则指导其架构和实现：

1. **服务器应该非常容易构建**
   * 主机应用程序处理复杂的编排责任
   * 服务器专注于特定的、定义明确的能力
   * 简单接口最小化实现开销
   * 清晰的分离使代码可维护

2. **服务器应该高度可组合**
   * 每个服务器提供隔离的专注功能
   * 多个服务器可以无缝组合
* 共享协议实现互操作性
   * 模块化设计支持可扩展性

3. **服务器不应该能够读取整个对话，也不能"窥探"其他服务器**
   * 服务器仅接收必要的上下文信息
   * 完整对话历史保留在主机中
   * 每个服务器连接保持隔离
   * 跨服务器交互由主机控制
   * 主机进程强制执行安全边界

4. **功能可以逐步添加到服务器和客户端**
   * 核心协议提供最小必需功能
   * 额外能力可以根据需要协商
   * 服务器和客户端独立演进
   * 协议设计考虑未来可扩展性
   * 保持向后兼容性

## 能力协商

Model Context Protocol使用基于能力的协商系统，客户端和服务器在初始化时明确声明其支持的功能。能力决定了会话期间可用的协议功能和原语。

* 服务器声明能力如资源订阅、工具支持和提示模板
* 客户端声明能力如采样支持和通知处理
* 双方必须在整个会话期间遵守声明的能力
* 额外的能力可以通过协议扩展进行协商

```mermaid
sequenceDiagram
    participant 主机
    participant 客户端
    participant 服务器

    主机->>+客户端: 初始化客户端
    客户端->>+服务器: 使用能力初始化会话
    服务器-->>客户端: 响应支持的能力

    Note over 主机,服务器: 具有协商功能的活跃会话

    loop 客户端请求
        主机->>客户端: 用户或模型发起的操作
        客户端->>服务器: 请求(工具/资源)
        服务器-->>客户端: 响应
        客户端-->>主机: 更新UI或响应模型
    end

    loop 服务器请求
        服务器->>客户端: 请求(采样)
        客户端->>主机: 转发给AI
        主机-->>客户端: AI响应
        客户端-->>服务器: 响应
    end

    loop 通知
        服务器--)客户端: 资源更新
        客户端--)服务器: 状态变更
    end

    主机->>客户端: 终止
    客户端->>-服务器: 结束会话
    deactivate 服务器
```

每个能力在会话期间解锁特定的协议功能。例如：
* 实现的[服务器功能](/specification/2025-03-26/server)必须在服务器的能力中声明
* 发出资源订阅通知需要服务器声明订阅支持
* 工具调用需要服务器声明工具能力
* [采样](/specification/2025-03-26/client)需要客户端在其能力中声明支持

这种能力协商确保客户端和服务器对支持的功能有清晰理解，同时保持协议的可扩展性。


# 授权
来源：https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization


<Info>**协议修订版**: 2025-03-26</Info>

## 1. 介绍

### 1.1 目的和范围

Model Context Protocol在传输层提供授权能力，使MCP客户端能够代表资源所有者向受限的MCP服务器发出请求。本规范定义了基于HTTP传输的授权流程。

### 1.2 协议要求

授权对MCP实现是**可选的**。当支持时：
* 使用基于HTTP传输的实现**应该**符合本规范
* 使用STDIO传输的实现**不应该**遵循本规范，而应从环境中获取凭据
* 使用替代传输的实现**必须**遵循其协议的安全最佳实践

### 1.3 标准合规性

此授权机制基于以下列出的已建立规范，但实现了其功能的选定子集，以确保安全性和互操作性，同时保持简单性：
* [OAuth 2.1 IETF草案](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12)
* OAuth 2.0授权服务器元数据([RFC8414](https://datatracker.ietf.org/doc/html/rfc8414))
* OAuth 2.0动态客户端注册协议([RFC7591](https://datatracker.ietf.org/doc/html/rfc7591))

## 2. 授权流程

### 2.1 概述

1. MCP授权实现**必须**实现OAuth 2.1，并为机密和公共客户端采取适当的安全措施
2. MCP授权实现**应该**支持OAuth 2.0动态客户端注册协议([RFC7591](https://datatracker.ietf.org/doc/html/rfc7591))
3. MCP服务器**应该**且MCP客户端**必须**实现OAuth 2.0授权服务器元数据([RFC8414](https://datatracker.ietf.org/doc/html/rfc8414))。不支持授权服务器元数据的服务器**必须**遵循默认URI模式

### 2.1.1 OAuth授权类型

OAuth指定了不同的流程或授权类型，这些是获取访问令牌的不同方式。每种类型针对不同的用例和场景。

MCP服务器**应该**支持最符合目标受众的OAuth授权类型。例如：
1. 授权码：当客户端代表(人类)最终用户操作时有用
   * 例如，代理调用由SaaS系统实现的MCP工具
2. 客户端凭据：客户端是另一个应用程序(不是人类)
   * 例如，代理调用安全的MCP工具检查特定商店的库存。不需要模拟最终用户

### 2.2 示例：授权码授权

这演示了用于用户认证的OAuth 2.1授权码授权类型流程。

**注意**：以下示例假设MCP服务器也作为授权服务器运行。然而，授权服务器可以作为独立的服务部署。

人类用户通过Web浏览器完成OAuth流程，获取标识其个人身份并允许客户端代表其操作的访问令牌。

当需要授权但客户端尚未证明时，服务器**必须**响应*HTTP 401 Unauthorized*。

客户端在收到*HTTP 401 Unauthorized*后启动[OAuth 2.1 IETF草案](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#name-authorization-code-grant)授权流程。

以下演示了使用PKCE的公共客户端的基本OAuth 2.1流程。

```mermaid
sequenceDiagram
    participant B as 用户代理(浏览器)
    participant C as 客户端
    participant M as MCP服务器

    C->>M: MCP请求
    M->>C: HTTP 401 Unauthorized
    Note over C: 生成code_verifier和code_challenge
    C->>B: 打开带有授权URL + code_challenge的浏览器
    B->>M: GET /authorize
    Note over M: 用户登录并授权
    M->>B: 重定向到带有授权码的回调URL
    B->>C: 回调带有授权码
    C->>M: 带有code + code_verifier的令牌请求
    M->>C: 访问令牌(+刷新令牌)
    C->>M: 带有访问令牌的MCP请求
    Note over C,M: 开始标准MCP消息交换
### 2.3 服务器元数据发现

对于服务器能力发现：
* MCP客户端*必须*遵循[RFC8414](https://datatracker.ietf.org/doc/html/rfc8414)定义的OAuth 2.0授权服务器元数据协议
* MCP服务器*应该*遵循OAuth 2.0授权服务器元数据协议
* 不支持OAuth 2.0授权服务器元数据协议的MCP服务器*必须*支持回退URL

发现流程如下所示：

```mermaid
sequenceDiagram
    participant C as 客户端
    participant S as 服务器

    C->>S: GET /.well-known/oauth-authorization-server
    alt 发现成功
        S->>C: 200 OK + 元数据文档
        Note over C: 使用元数据中的端点
    else 发现失败
        S->>C: 404 Not Found
        Note over C: 回退到默认端点
    end
    Note over C: 继续授权流程
```

#### 2.3.1 服务器元数据发现头部

MCP客户端*应该*在服务器元数据发现期间包含头部`MCP-Protocol-Version: <protocol-version>`，以允许MCP服务器根据MCP协议版本进行响应。

例如：`MCP-Protocol-Version: 2024-11-05`

#### 2.3.2 授权基础URL

授权基础URL*必须*通过丢弃MCP服务器URL中的任何现有`path`组件来确定。例如：

如果MCP服务器URL是`https://api.example.com/v1/mcp`，那么：
* 授权基础URL是`https://api.example.com`
* 元数据端点*必须*位于`https://api.example.com/.well-known/oauth-authorization-server`

这确保授权端点始终位于托管MCP服务器的域名的根级别，而不管MCP服务器URL中的任何路径组件。

#### 2.3.3 不支持元数据发现的回退方案

对于未实现OAuth 2.0授权服务器元数据的服务器，客户端*必须*使用以下默认端点路径（相对于[2.3.2节](#232-授权基础url)中定义的授权基础URL）：

| 端点               | 默认路径 | 描述                          |
| ------------------ | -------- | ----------------------------- |
| 授权端点 | /authorize   | 用于授权请求      |
| 令牌端点         | /token       | 用于令牌交换和刷新    |
| 注册端点  | /register    | 用于动态客户端注册 |

例如，托管在`https://api.example.com/v1/mcp`的MCP服务器，默认端点为：
* `https://api.example.com/authorize`
* `https://api.example.com/token`
* `https://api.example.com/register`

客户端*必须*首先尝试通过元数据文档发现端点，然后才回退到默认路径。使用默认路径时，所有其他协议要求保持不变。

### 2.4 动态客户端注册

MCP客户端和服务器*应该*支持[OAuth 2.0动态客户端注册协议](https://datatracker.ietf.org/doc/html/rfc7591)，以允许MCP客户端无需用户交互即可获取OAuth客户端ID。这为客户端提供了一种标准化的方式自动注册新服务器，这对MCP至关重要，因为：
* 客户端无法预先知道所有可能的服务器
* 手动注册会给用户带来摩擦
* 它实现了与新服务器的无缝连接
* 服务器可以实现自己的注册策略

任何*不支持*动态客户端注册的MCP服务器需要提供替代方法来获取客户端ID（以及适用的客户端密钥）。对于这些服务器之一，MCP客户端将不得不：
1. 硬编码专门针对该MCP服务器的客户端ID（以及适用的客户端密钥），或
2. 向用户呈现UI，允许他们在自行注册OAuth客户端后输入这些详细信息（例如，通过服务器托管的配置界面）。

### 2.5 授权流程步骤

完整的授权流程如下：

```mermaid
sequenceDiagram
    participant B as 用户代理(浏览器)
    participant C as 客户端
    participant M as MCP服务器

    C->>M: GET /.well-known/oauth-authorization-server
    alt 服务器支持发现
        M->>C: 授权服务器元数据
    else 无发现
        M->>C: 404 (使用默认端点)
    end

    alt 动态客户端注册
        C->>M: POST /register
        M->>C: 客户端凭据
    end

    Note over C: 生成PKCE参数
    C->>B: 打开带有授权URL + code_challenge的浏览器
    B->>M: 授权请求
    Note over M: 用户授权
    M->>B: 重定向到带有授权码的回调
    B->>C: 授权码回调
    C->>M: 令牌请求 + code_verifier
    M->>C: 访问令牌(+刷新令牌)
    C->>M: 带有访问令牌的API请求
```

#### 2.5.1 决策流程概述

```mermaid
flowchart TD
    A[开始授权流程] --> B{检查元数据发现}
    B -->|可用| C[使用元数据端点]
    B -->|不可用| D[使用默认端点]

    C --> G{检查注册端点}
    D --> G

    G -->|可用| H[执行动态注册]
    G -->|不可用| I[需要替代注册]

    H --> J[开始OAuth流程]
    I --> J

    J --> K[生成PKCE参数]
    K --> L[请求授权]
    L --> M[用户授权]
    M --> N[交换代码获取令牌]
    N --> O[使用访问令牌]
```

### 2.6 访问令牌使用

#### 2.6.1 令牌要求

访问令牌处理*必须*符合[OAuth 2.1第5节](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-5)对资源请求的要求。具体来说：

1. MCP客户端*必须*使用Authorization请求头字段[第5.1.1节](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-5.1.1)：

```
Authorization: Bearer <access-token>
```

注意授权*必须*包含在从客户端到服务器的每个HTTP请求中，即使它们是同一逻辑会话的一部分。

2. 访问令牌*不得*包含在URI查询字符串中

示例请求：

```http
GET /v1/contexts HTTP/1.1
Host: mcp.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

#### 2.6.2 令牌处理

资源服务器*必须*按照[第5.2节](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-5.2)所述验证访问令牌。
如果验证失败，服务器*必须*按照[第5.3节](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-5.3)的错误处理要求进行响应。无效或过期的令牌*必须*收到HTTP 401响应。

### 2.7 安全考虑

必须实现以下安全要求：
1. 客户端*必须*按照OAuth 2.0最佳实践安全存储令牌
2. 服务器*应该*强制执行令牌过期和轮换
3. 所有授权端点*必须*通过HTTPS提供服务
4. 服务器*必须*验证重定向URI以防止开放重定向漏洞
5. 重定向URI*必须*是localhost URL或HTTPS URL

### 2.8 错误处理

服务器*必须*为授权错误返回适当的HTTP状态码：

| 状态码 | 描述  | 用途                                      |
| ------ | ----- | ----------------------------------------- |
| 401    | 未授权 | 需要授权或令牌无效                       |
| 403    | 禁止  | 无效范围或权限不足                       |
| 400    | 错误请求 | 格式错误的授权请求                       |

### 2.9 实现要求

1. 实现*必须*遵循OAuth 2.1安全最佳实践
2. 所有客户端*必须*使用PKCE
3. *应该*实现令牌轮换以增强安全性
4. 令牌生命周期*应该*根据安全要求进行限制

### 2.10 第三方授权流程

#### 2.10.1 概述

MCP服务器*可以*支持通过第三方授权服务器进行委托授权。在此流程中，MCP服务器既充当OAuth客户端(对第三方授权服务器)又充当OAuth授权服务器(对MCP客户端)。

#### 2.10.2 流程描述

第三方授权流程包括以下步骤：
1. MCP客户端与MCP服务器启动标准OAuth流程
2. MCP服务器将用户重定向到第三方授权服务器
3. 用户向第三方服务器授权
4. 第三方服务器重定向回MCP服务器并携带授权码
5. MCP服务器用授权码交换第三方访问令牌
6. MCP服务器生成绑定到第三方会话的自有访问令牌
7. MCP服务器与MCP客户端完成原始OAuth流程

```mermaid
sequenceDiagram
    participant B as 用户代理(浏览器)
    participant C as MCP客户端
    participant M as MCP服务器
    participant T as 第三方授权服务器

    C->>M: 初始OAuth请求
    M->>B: 重定向到第三方/authorize
    B->>T: 授权请求
    Note over T: 用户授权
    T->>B: 重定向到MCP服务器回调
    B->>M: 授权码
    M->>T: 用授权码交换令牌
    T->>M: 第三方访问令牌
    Note over M: 生成绑定的MCP令牌
    M->>B: 重定向到MCP客户端回调
    B->>C: MCP授权码
    C->>M: 用授权码交换令牌
    M->>C: MCP访问令牌
```

#### 2.10.3 会话绑定要求

实现第三方授权的MCP服务器*必须*：
1. 维护第三方令牌与已颁发MCP令牌之间的安全映射
2. 在兑现MCP令牌前验证第三方令牌状态
3. 实现适当的令牌生命周期管理
4. 处理第三方令牌过期和续订

#### 2.10.4 安全考虑

实现第三方授权时，服务器*必须*：
1. 验证所有重定向URI
2. 安全存储第三方凭据
3. 实现适当的会话超时处理
4. 考虑令牌链的安全影响
5. 为第三方授权失败实现适当的错误处理

## 3. 最佳实践

#### 3.1 本地客户端作为公共OAuth 2.1客户端

我们强烈建议本地客户端作为公共客户端实现OAuth 2.1：
1. 使用代码挑战(PKCE)进行授权请求以防止拦截攻击
2. 实现适合本地系统的安全令牌存储
3. 遵循令牌刷新最佳实践以维护会话
4. 正确处理令牌过期和续订

#### 3.2 授权元数据发现

我们强烈建议所有客户端实现元数据发现。这减少了用户手动提供端点或客户端回退到定义默认值的需要。

#### 3.3 动态客户端注册

由于客户端无法预先知道MCP服务器集合，我们强烈建议实现动态客户端注册。这允许应用程序自动注册到MCP服务器，并消除了用户手动获取客户端ID的需要。


# 概述
来源：https://modelcontextprotocol.io/specification/2025-03-26/basic/index


<Info>**协议修订版**: 2025-03-26</Info>

Model Context Protocol由几个协同工作的关键组件组成：
* **基础协议**: 核心JSON-RPC消息类型
* **生命周期管理**: 连接初始化、能力协商和会话控制
* **服务器功能**: 服务器暴露的资源、提示和工具
* **客户端功能**: 客户端提供的采样和根目录列表
* **实用工具**: 跨领域关注点如日志记录和参数补全

所有实现*必须*支持基础协议和生命周期管理组件。其他组件*可以*根据应用程序的特定需求实现。

这些协议层建立了清晰的关注点分离，同时支持客户端和服务器之间的丰富交互。模块化设计允许实现仅支持它们需要的功能。

## 消息

MCP客户端和服务器之间的所有消息*必须*遵循[JSON-RPC 2.0](https://www.jsonrpc.org/specification)规范。协议定义了这些类型的消息：

### 请求

请求从客户端发送到服务器或反之，以启动操作。

```typescript
{
  jsonrpc: "2.0";
  id: string | number;
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

* 请求*必须*包含字符串或整数ID
* 与基础JSON-RPC不同，ID*不得*为`null`
* 请求ID*不得*在同一会话中由请求者先前使用过

### 响应

响应是对请求的回复，包含操作的结果或错误。

```typescript
{
  jsonrpc: "2.0";
  id: string | number;
  result?: {
    [key: string]: unknown;
  }
  error?: {
    code: number;
    message: string;
    data?: unknown;
  }
}
* 响应*必须*包含与对应请求相同的ID
* 响应进一步细分为**成功结果**或**错误**。必须设置`result`或`error`中的一个。响应*不得*同时设置两者
* 结果*可以*遵循任何JSON对象结构，而错误*必须*至少包含错误代码和消息
* 错误代码*必须*是整数

### 通知

通知是从客户端发送到服务器或反之的单向消息。接收方*不得*发送响应。

```typescript
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

* 通知*不得*包含ID

### 批量处理

JSON-RPC还定义了通过数组发送多个请求和通知来[批量处理](https://www.jsonrpc.org/specification#batch)的方法。MCP实现*可以*支持发送JSON-RPC批量请求，但*必须*支持接收JSON-RPC批量请求。

## 认证

MCP提供了用于HTTP的[授权](/specification/2025-03-26/basic/authorization)框架。使用基于HTTP传输的实现*应该*符合此规范，而使用STDIO传输的实现*不应该*遵循此规范，而应从环境中获取凭据。

此外，客户端和服务器*可以*协商自己的自定义认证和授权策略。

如需进一步讨论并为MCP认证机制的演进做出贡献，请加入[GitHub讨论](https://github.com/modelcontextprotocol/specification/discussions)帮助我们塑造协议的未来！

## 模式

协议的完整规范定义为[TypeScript模式](https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.ts)。这是所有协议消息和结构的真实来源。

还有一个[JSON模式](https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.json)，它是从TypeScript真实来源自动生成的，用于各种自动化工具。


# 生命周期
来源：https://modelcontextprotocol.io/specification/2025-03-26/basic/lifecycle


<Info>**协议修订版**: 2025-03-26</Info>

Model Context Protocol (MCP)为客户端-服务器连接定义了严格的生命周期，确保适当的能力协商和状态管理。

1. **初始化**: 能力协商和协议版本确认
2. **操作**: 正常协议通信
3. **关闭**: 优雅终止连接

```mermaid
sequenceDiagram
    participant Client as 客户端
    participant Server as 服务器

    Note over Client,Server: 初始化阶段
    activate Client
    Client->>+Server: 初始化请求
    Server-->>Client: 初始化响应
    Client--)Server: 初始化完成通知

    Note over Client,Server: 操作阶段
    rect rgb(200, 220, 250)
        note over Client,Server: 正常协议操作
    end

    Note over Client,Server: 关闭
    Client--)-Server: 断开连接
    deactivate Server
    Note over Client,Server: 连接关闭
```

## 生命周期阶段

### 初始化

初始化阶段*必须*是客户端和服务器之间的第一次交互。在此阶段，客户端和服务器：

* 建立协议版本兼容性
* 交换和协商能力
* 共享实现细节

客户端*必须*通过发送包含以下内容的`initialize`请求来启动此阶段：

* 支持的协议版本
* 客户端能力
* 客户端实现信息

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "roots": {
        "listChanged": true
      },
      "sampling": {}
    },
    "clientInfo": {
      "name": "ExampleClient",
      "version": "1.0.0"
    }
  }
}
```

初始化请求*不得*作为JSON-RPC[批量](https://www.jsonrpc.org/specification#batch)的一部分，因为在初始化完成之前不可能有其他请求和通知。这也允许与不支持JSON-RPC批处理的早期协议版本向后兼容。

服务器*必须*响应其自身的能力和信息：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "logging": {},
      "prompts": {
        "listChanged": true
      },
      "resources": {
        "subscribe": true,
        "listChanged": true
      },
      "tools": {
        "listChanged": true
      }
    },
    "serverInfo": {
      "name": "ExampleServer",
      "version": "1.0.0"
    },
    "instructions": "客户端的可选指令"
  }
}
```

成功初始化后，客户端*必须*发送`initialized`通知以表明已准备好开始正常操作：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/initialized"
}
```

* 在服务器响应`initialize`请求之前，客户端*不应该*发送除[ping](/specification/2025-03-26/basic/utilities/ping)之外的请求
* 在收到`initialized`通知之前，服务器*不应该*发送除[ping](/specification/2025-03-26/basic/utilities/ping)和[日志](/specification/2025-03-26/server/utilities/logging)之外的请求
#### 版本协商

在`initialize`请求中，客户端*必须*发送其支持的协议版本。这*应该*是客户端支持的*最新*版本。

如果服务器支持请求的协议版本，它*必须*响应相同的版本。否则，服务器*必须*响应它支持的另一个协议版本。这*应该*是服务器支持的*最新*版本。

如果客户端不支持服务器响应中的版本，它*应该*断开连接。

#### 能力协商

客户端和服务器能力确定了会话期间可用的可选协议功能。

关键能力包括：

| 类别   | 能力         | 描述                                                                         |
| ------ | ------------ | --------------------------------------------------------------------------- |
| 客户端 | `roots`      | 提供文件系统[根目录](/specification/2025-03-26/client/roots)的能力           |
| 客户端 | `sampling`   | 支持LLM[采样](/specification/2025-03-26/client/sampling)请求                 |
| 客户端 | `experimental` | 描述对非标准实验功能的支持                                                 |
| 服务器 | `prompts`    | 提供[提示模板](/specification/2025-03-26/server/prompts)                     |
| 服务器 | `resources`  | 提供可读[资源](/specification/2025-03-26/server/resources)                   |
| 服务器 | `tools`      | 暴露可调用[工具](/specification/2025-03-26/server/tools)                     |
| 服务器 | `logging`    | 发出结构化[日志消息](/specification/2025-03-26/server/utilities/logging)     |
| 服务器 | `experimental` | 描述对非标准实验功能的支持                                                 |

能力对象可以描述子能力，如：
* `listChanged`: 支持列表变更通知(用于提示、资源和工具)
* `subscribe`: 支持订阅单个项目的变更(仅资源)

### 操作阶段

在操作阶段，客户端和服务器根据协商的能力交换消息。

双方*应该*：
* 遵守协商的协议版本
* 仅使用成功协商的能力

### 关闭

在关闭阶段，一方(通常是客户端)干净地终止协议连接。没有定义特定的关闭消息——而是应该使用底层传输机制来发出连接终止信号：

#### stdio

对于stdio[传输](/specification/2025-03-26/basic/transports)，客户端*应该*通过以下方式启动关闭：
1. 首先关闭子进程(服务器)的输入流
2. 等待服务器退出，如果服务器在合理时间内未退出则发送`SIGTERM`
3. 如果在`SIGTERM`后的合理时间内服务器仍未退出，则发送`SIGKILL`

服务器*可以*通过关闭其到客户端的输出流并退出来启动关闭。

#### HTTP

对于HTTP[传输](/specification/2025-03-26/basic/transports)，关闭通过关闭相关的HTTP连接来指示。

## 超时

实现*应该*为所有发送的请求建立超时，以防止连接挂起和资源耗尽。当请求在超时期限内未收到成功或错误响应时，发送方*应该*为该请求发出[取消通知](/specification/2025-03-26/basic/utilities/cancellation)并停止等待响应。

SDK和其他中间件*应该*允许在每个请求的基础上配置这些超时。

实现*可以*选择在收到与请求对应的[进度通知](/specification/2025-03-26/basic/utilities/progress)时重置超时时钟，因为这暗示工作实际上正在进行。然而，实现*应该*始终强制执行最大超时，无论进度通知如何，以限制行为不当的客户端或服务器的影响。

## 错误处理

实现*应该*准备好处理这些错误情况：
* 协议版本不匹配
* 未能协商所需能力
* 请求[超时](#超时)

初始化错误示例：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32602,
    "message": "不支持的协议版本",
    "data": {
      "supported": ["2024-11-05"],
      "requested": "1.0.0"
    }
  }
}
```


# 传输
来源：https://modelcontextprotocol.io/specification/2025-03-26/basic/transports


<Info>**协议修订版**: 2025-03-26</Info>

MCP使用JSON-RPC编码消息。JSON-RPC消息*必须*使用UTF-8编码。

协议目前定义了两种标准的客户端-服务器通信传输机制：
1. [stdio](#stdio)，通过标准输入和标准输出通信
2. [可流式HTTP](#可流式http)

客户端*应该*尽可能支持stdio。

客户端和服务器也可以以可插拔的方式实现[自定义传输](#自定义传输)。

## stdio

在**stdio**传输中：
* 客户端将MCP服务器作为子进程启动
* 服务器从其标准输入(`stdin`)读取JSON-RPC消息，并将消息发送到其标准输出(`stdout`)
* 消息可以是JSON-RPC请求、通知、响应——或包含一个或多个请求和/或通知的JSON-RPC[批量](https://www.jsonrpc.org/specification#batch)
* 消息由换行符分隔，并且*不得*包含嵌入的换行符
* 服务器*可以*向其标准错误(`stderr`)写入UTF-8字符串用于日志记录。客户端*可以*捕获、转发或忽略此日志记录
* 服务器*不得*向`stdout`写入任何非有效MCP消息的内容
* 客户端*不得*向服务器的`stdin`写入任何非有效MCP消息的内容

```mermaid
sequenceDiagram
    participant Client as 客户端
    participant Server as 服务器进程

    Client->>+Server: 启动子进程
    loop 消息交换
        Client->>Server: 写入stdin
        Server->>Client: 写入stdout
        Server--)Client: 可选的stderr日志
    end
    Client->>Server: 关闭stdin，终止子进程
    deactivate Server
```

## 可流式HTTP

<Info>这取代了协议版本2024-11-05中的[HTTP+SSE传输](/specification/2024-11-05/basic/transports#http-with-sse)。请参阅下面的[向后兼容性](#向后兼容性)指南。</Info>

在**可流式HTTP**传输中，服务器作为可以处理多个客户端连接的独立进程运行。此传输使用HTTP POST和GET请求。服务器可以选择性地利用[服务器发送事件](https://en.wikipedia.org/wiki/Server-sent_events)(SSE)来流式传输多个服务器消息。这允许基本的MCP服务器，以及支持流式传输和服务器到客户端通知和请求的功能更丰富的服务器。

服务器*必须*提供支持POST和GET方法的单个HTTP端点路径(以下称为**MCP端点**)。例如，这可以是一个像`https://example.com/mcp`这样的URL。

#### 安全警告

实现可流式HTTP传输时：
1. 服务器*必须*验证所有传入连接的`Origin`头部，以防止DNS重绑定攻击
2. 在本地运行时，服务器*应该*仅绑定到localhost(127.0.0.1)而不是所有网络接口(0.0.0.0)
3. 服务器*应该*为所有连接实现适当的认证

没有这些保护措施，攻击者可能使用DNS重绑定从远程网站与本地MCP服务器交互。

### 向服务器发送消息

客户端发送的每个JSON-RPC消息*必须*是对MCP端点的新HTTP POST请求。

1. 客户端*必须*使用HTTP POST向MCP端点发送JSON-RPC消息
2. 客户端*必须*包含`Accept`头部，列出`application/json`和`text/event-stream`作为支持的内容类型
3. POST请求的主体*必须*是以下之一：
   * 单个JSON-RPC*请求*、*通知*或*响应*
   * 包含一个或多个*请求和/或通知*的数组[批量](https://www.jsonrpc.org/specification#batch)
   * 包含一个或多个*响应*的数组[批量](https://www.jsonrpc.org/specification#batch)
4. 如果输入仅包含(任意数量的)JSON-RPC*响应*或*通知*：
   * 如果服务器接受输入，服务器*必须*返回HTTP状态码202 Accepted且无主体
   * 如果服务器无法接受输入，它*必须*返回HTTP错误状态码(如400 Bad Request)。HTTP响应主体*可以*包含没有`id`的JSON-RPC*错误响应*
5. 如果输入包含任意数量的JSON-RPC*请求*，服务器*必须*返回`Content-Type: text/event-stream`以启动SSE流，或`Content-Type: application/json`以返回一个JSON对象。客户端*必须*支持这两种情况
6. 如果服务器启动SSE流：
   * SSE流*应该*最终包含每个POST主体中发送的JSON-RPC*请求*对应的一个JSON-RPC*响应*。这些*响应*可以[批量](https://www.jsonrpc.org/specification#batch)发送
   * 服务器*可以*在发送JSON-RPC*响应*之前发送JSON-RPC*请求*和*通知*。这些消息*应该*与原始客户端*请求*相关。这些*请求*和*通知*可以[批量](https://www.jsonrpc.org/specification#batch)发送
   * 服务器*不应该*在发送每个接收到的JSON-RPC*请求*对应的JSON-RPC*响应*之前关闭SSE流，除非[会话](#会话管理)过期
   * 发送完所有JSON-RPC*响应*后，服务器*应该*关闭SSE流
   * 断开连接*可能*随时发生(例如由于网络条件)。因此：
     * 断开连接*不应该*被解释为客户端取消其请求
     * 要取消，客户端*应该*显式发送MCP`CancelledNotification`
     * 为避免因断开连接导致消息丢失，服务器*可以*使流[可恢复](#可恢复性和重传)

### 监听来自服务器的消息

1. 客户端*可以*向MCP端点发出HTTP GET。这可用于打开SSE流，允许服务器与客户端通信，而无需客户端首先通过HTTP POST发送数据
2. 客户端*必须*包含`Accept`头部，列出`text/event-stream`作为支持的内容类型
3. 服务器*必须*返回`Content-Type: text/event-stream`响应此HTTP GET，或返回HTTP 405 Method Not Allowed，表示服务器在此端点不提供SSE流
4. 如果服务器启动SSE流：
   * 服务器*可以*在流上发送JSON-RPC*请求*和*通知*。这些*请求*和*通知*可以[批量](https://www.jsonrpc.org/specification#batch)发送
   * 这些消息*应该*与客户端同时运行的任何JSON-RPC*请求*无关
   * 服务器*不得*在流上发送JSON-RPC*响应*，*除非*[恢复](#可恢复性和重传)与先前客户端请求关联的流
   * 服务器*可以*随时关闭SSE流
   * 客户端*可以*随时关闭SSE流

### 多连接

1. 客户端*可以*同时保持连接到多个SSE流
2. 服务器*必须*仅在一个连接的流上发送其每个JSON-RPC消息；即它*不得*跨多个流广播相同消息
   * 可以通过使流[可恢复](#可恢复性和重传)来减轻消息丢失的风险

### 可恢复性和重传

为支持恢复中断的连接和重传可能丢失的消息：

1. 服务器*可以*向其SSE事件附加`id`字段，如[SSE标准](https://html.spec.whatwg.org/multipage/server-sent-events.html#event-stream-interpretation)所述
   * 如果存在，ID*必须*在该[会话](#会话管理)内的所有流中全局唯一——或者如果未使用会话管理，则在该特定客户端的全部流中全局唯一
2. 如果客户端希望在连接中断后恢复，它*应该*向MCP端点发出HTTP GET，并包含[`Last-Event-ID`](https://html.spec.whatwg.org/multipage/server-sent-events.html#the-last-event-id-header)头部以指示它接收到的最后一个事件ID
   * 服务器*可以*使用此头部重播在最后一个事件ID之后*在断开连接的流上*会发送的消息，并从该点恢复流
   * 服务器*不得*重播会在不同流上传递的消息

换句话说，这些事件ID应由服务器在*每个流*的基础上分配，作为该特定流中的游标。

### 会话管理

MCP"会话"由客户端和服务器之间逻辑相关的交互组成，从[初始化阶段](/specification/2025-03-26/basic/lifecycle)开始。为支持希望建立有状态会话的服务器：

1. 使用可流式HTTP传输的服务器*可以*在初始化时分配会话ID，通过在包含`InitializeResult`的HTTP响应中包含`Mcp-Session-Id`头部
   * 会话ID*应该*全局唯一且加密安全(例如安全生成的UUID、JWT或加密哈希)
   * 会话ID*必须*仅包含可见ASCII字符(范围从0x21到0x7E)
2. 如果服务器在初始化期间返回`Mcp-Session-Id`，使用可流式HTTP传输的客户端*必须*在其所有后续HTTP请求中包含`Mcp-Session-Id`头部
   * 需要会话ID的服务器*应该*对不包含`Mcp-Session-Id`头部的请求(初始化除外)响应HTTP 400 Bad Request
3. 服务器*可以*随时终止会话，之后它*必须*对包含该会话ID的请求响应HTTP 404 Not Found
4. 当客户端收到对包含`Mcp-Session-Id`的请求的HTTP 404响应时，它*必须*通过发送不带会话ID的新`InitializeRequest`来启动新会话
5. 不再需要特定会话的客户端(例如因为用户正在离开客户端应用程序)*应该*向MCP端点发送带有`Mcp-Session-Id`头部的HTTP DELETE，以显式终止会话
   * 服务器*可以*对此请求响应HTTP 405 Method Not Allowed，表示服务器不允许客户端终止会话

### 序列图

```mermaid
sequenceDiagram
    participant Client as 客户端
    participant Server as 服务器

    note over Client, Server: 初始化

    Client->>+Server: POST InitializeRequest
    Server->>-Client: InitializeResponse<br>Mcp-Session-Id: 1868a90c...
    
    Client->>+Server: POST InitializedNotification<br>Mcp-Session-Id: 1868a90c...
    Server->>-Client: 202 Accepted

    note over Client, Server: 客户端请求
    Client->>+Server: POST ... request ...<br>Mcp-Session-Id: 1868a90c...

    alt 单一HTTP响应
      Server->>Client: ... response ...
    else 服务器打开SSE流
      loop 当连接保持打开时
          Server-)Client: ... 来自服务器的SSE消息 ...
      end
      Server-)Client: SSE事件: ... response ...
    end
    deactivate Server

    note over Client, Server: 客户端通知/响应
    Client->>+Server: POST ... notification/response ...<br>Mcp-Session-Id: 1868a90c...
    Server->>-Client: 202 Accepted

    note over Client, Server: 服务器请求
    Client->>+Server: GET<br>Mcp-Session-Id: 1868a90c...
    loop 当连接保持打开时
        Server-)Client: ... 来自服务器的SSE消息 ...
    end
    deactivate Server
```

### 向后兼容性

客户端和服务器可以保持与已弃用的[HTTP+SSE传输](/specification/2024-11-05/basic/transports#http-with-sse)(来自协议版本2024-11-05)的向后兼容性，如下所示：

**服务器**希望支持旧客户端应该：

* 继续托管旧传输的SSE和POST端点，以及为可流式HTTP传输定义的新"MCP端点"
  * 也可以将旧的POST端点与新的MCP端点合并，但这可能引入不必要的复杂性
**客户端**希望支持旧服务器应该：

1. 接受来自用户的MCP服务器URL，该URL可能指向使用旧传输或新传输的服务器
2. 尝试向服务器URL POST一个`InitializeRequest`，并带有如上定义的`Accept`头部：
   * 如果成功，客户端可以假设这是支持新可流式HTTP传输的服务器
   * 如果失败并返回HTTP 4xx状态码(如405 Method Not Allowed或404 Not Found)：
     * 向服务器URL发出GET请求，期望这将打开SSE流并返回`endpoint`事件作为第一个事件
     * 当`endpoint`事件到达时，客户端可以假设这是运行旧HTTP+SSE传输的服务器，并应使用该传输进行所有后续通信

## 自定义传输

客户端和服务器*可以*实现额外的自定义传输机制以满足其特定需求。该协议与传输无关，可以在支持双向消息交换的任何通信通道上实现。

选择支持自定义传输的实现者*必须*确保它们保留了MCP定义的JSON-RPC消息格式和生命周期要求。自定义传输*应该*记录其特定的连接建立和消息交换模式以帮助互操作性。


# 取消
来源：https://modelcontextprotocol.io/specification/2025-03-26/basic/utilities/cancellation


<Info>**协议修订版**: 2025-03-26</Info>

模型上下文协议(MCP)通过通知消息支持可选地取消进行中的请求。任一方都可以发送取消通知以指示应终止先前发出的请求。

## 取消流程

当一方想要取消进行中的请求时，它发送包含以下内容的`notifications/cancelled`通知：
* 要取消的请求ID
* 可选的可以记录或显示的原因字符串

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/cancelled",
  "params": {
    "requestId": "123",
    "reason": "用户请求取消"
  }
}
```

## 行为要求

1. 取消通知*必须*仅引用：
   * 先前在同一方向发出的请求
   * 被认为仍在进行中的请求
2. `initialize`请求*不得*被客户端取消
3. 取消通知的接收者*应该*：
   * 停止处理被取消的请求
   * 释放相关资源
   * 不为被取消的请求发送响应
4. 接收者*可以*忽略取消通知如果：
   * 引用的请求未知
   * 处理已完成
   * 请求无法取消
5. 取消通知的发送者*应该*忽略之后到达的该请求的任何响应

## 时间考虑

由于网络延迟，取消通知可能在请求处理完成后到达，甚至可能在响应已经发送后到达。

双方*必须*优雅地处理这些竞态条件：

```mermaid
sequenceDiagram
   participant Client as 客户端
   participant Server as 服务器

   Client->>Server: 请求 (ID: 123)
   Note over Server: 处理开始
   Client--)Server: notifications/cancelled (ID: 123)
   alt
      Note over Server: 处理可能在<br/>取消到达前<br/>已完成
   else 如果未完成
      Note over Server: 停止处理
   end
```

## 实现说明

* 双方*应该*记录取消原因以便调试
* 应用程序UI*应该*在请求取消时显示指示

## 错误处理

无效的取消通知*应该*被忽略：
* 未知请求ID
* 已完成的请求
* 格式错误的通知

这保持了通知的"发送后不管"特性，同时允许异步通信中的竞态条件。


# Ping
来源：https://modelcontextprotocol.io/specification/2025-03-26/basic/utilities/ping


<Info>**协议修订版**: 2025-03-26</Info>

模型上下文协议包括一个可选的ping机制，允许任一方验证其对方是否仍然响应且连接是否存活。

## 概述

ping功能通过简单的请求/响应模式实现。客户端或服务器都可以通过发送`ping`请求来启动ping。

## 消息格式

ping请求是一个没有参数的标准JSON-RPC请求：

```json
{
  "jsonrpc": "2.0",
  "id": "123",
  "method": "ping"
}
```

## 行为要求

1. 接收者*必须*立即响应一个空响应：

```json
{
  "jsonrpc": "2.0",
  "id": "123",
  "result": {}
}
```

2. 如果在合理超时期限内未收到响应，发送者*可以*：
   * 认为连接已失效
   * 终止连接
   * 尝试重新连接过程

## 使用模式

```mermaid
sequenceDiagram
    participant Sender as 发送方
    participant Receiver as 接收方

    Sender->>Receiver: ping请求
    Receiver->>Sender: 空响应
```

## 实现考虑

* 实现*应该*定期发出ping以检测连接健康状态
* ping的频率*应该*可配置
* 超时*应该*适合网络环境
* *应该*避免过多的ping以减少网络开销

## 错误处理

* 超时*应该*被视为连接失败
* 多次失败的ping*可以*触发连接重置
* 实现*应该*记录ping失败以进行诊断


# 进度
来源：https://modelcontextprotocol.io/specification/2025-03-26/basic/utilities/progress
<Info>**协议修订版**: 2025-03-26</Info>

模型上下文协议(MCP)通过通知消息支持对长时间运行操作的可选进度跟踪。任一方都可以发送进度通知来提供操作状态更新。

## 进度流程

当一方想要*接收*请求的进度更新时，它在请求元数据中包含一个`progressToken`。

* 进度令牌*必须*是字符串或整数值
* 进度令牌可以由发送方使用任何方式选择，但*必须*在所有活动请求中唯一

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "some_method",
  "params": {
    "_meta": {
      "progressToken": "abc123"
    }
  }
}
```

接收方*可以*发送包含以下内容的进度通知：

* 原始进度令牌
* 当前进度值
* 可选的"total"总值
* 可选的"message"消息

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/progress",
  "params": {
    "progressToken": "abc123",
    "progress": 50,
    "total": 100,
    "message": "正在处理..."
  }
}
```

* `progress`值*必须*随每个通知增加，即使总值未知
* `progress`和`total`值*可以*是浮点数
* `message`字段*应该*提供相关的人类可读进度信息

## 行为要求

1. 进度通知*必须*仅引用：
   * 在活动请求中提供的令牌
   * 与进行中操作关联的令牌

2. 进度请求的接收者*可以*：
   * 选择不发送任何进度通知
   * 以他们认为合适的频率发送通知
   * 如果未知则省略总值

```mermaid
sequenceDiagram
    participant Sender as 发送方
    participant Receiver as 接收方

    Note over Sender,Receiver: 带有进度令牌的请求
    Sender->>Receiver: 带有progressToken的方法请求

    Note over Sender,Receiver: 进度更新
    loop 进度更新
        Receiver-->>Sender: 进度通知 (0.2/1.0)
        Receiver-->>Sender: 进度通知 (0.6/1.0)
        Receiver-->>Sender: 进度通知 (1.0/1.0)
    end

    Note over Sender,Receiver: 操作完成
    Receiver->>Sender: 方法响应
```

## 实现说明

* 发送方和接收方*应该*跟踪活动进度令牌
* 双方*应该*实现速率限制以防止泛滥
* 进度通知*必须*在完成后停止


# 关键变更
来源：https://modelcontextprotocol.io/specification/2025-03-26/changelog

本文档列出了自上一修订版[2024-11-05](/specification/2024-11-05)以来对模型上下文协议(MCP)规范的更改。

## 主要变更

1. 添加了基于OAuth 2.1的全面**[授权框架](/specification/2025-03-26/basic/authorization)**(PR
   [#133](https://github.com/modelcontextprotocol/specification/pull/133))
2. 用更灵活的**[可流式HTTP传输](/specification/2025-03-26/basic/transports#streamable-http)**替换了之前的HTTP+SSE传输(PR
   [#206](https://github.com/modelcontextprotocol/specification/pull/206))
3. 添加了对JSON-RPC**[批量处理](https://www.jsonrpc.org/specification#batch)**的支持(PR
   [#228](https://github.com/modelcontextprotocol/specification/pull/228))
4. 添加了全面的**工具注解**以更好地描述工具行为，例如它是只读的还是破坏性的(PR
   [#185](https://github.com/modelcontextprotocol/specification/pull/185))

## 其他架构变更

* 向`ProgressNotification`添加了`message`字段以提供描述性状态更新
* 添加了对音频数据的支持，加入了现有的文本和图像内容类型
* 添加了`completions`能力以明确指示对参数自动完成建议的支持

更多详情请参见[更新后的架构](http://github.com/modelcontextprotocol/specification/tree/main/schema/2025-03-26/schema.ts)。

## 完整变更日志

有关自上次协议修订以来所有更改的完整列表，请[参见GitHub](https://github.com/modelcontextprotocol/specification/compare/2024-11-05...2025-03-26)。


# 根目录
来源：https://modelcontextprotocol.io/specification/2025-03-26/client/roots


<Info>**协议修订版**: 2025-03-26</Info>

模型上下文协议(MCP)提供了一种标准化方式，让客户端向服务器暴露文件系统"根目录"。根目录定义了服务器可以在文件系统中操作的范围，让它们了解可以访问哪些目录和文件。服务器可以从支持客户端请求根目录列表，并在该列表更改时接收通知。

## 用户交互模型

MCP中的根目录通常通过工作区或项目配置界面暴露。

例如，实现可以提供工作区/项目选择器，允许用户选择服务器应有权访问的目录和文件。这可以与版本控制系统或项目文件的自动工作区检测相结合。

但是，实现可以自由地通过任何适合其需求的界面模式暴露根目录——协议本身不强制要求任何特定的用户交互模型。

## 能力

支持根目录的客户端*必须*在[初始化](/specification/2025-03-26/basic/lifecycle#initialization)期间声明`roots`能力：

```json
{
  "capabilities": {
    "roots": {
      "listChanged": true
    }
  }
}
```

`listChanged`指示客户端是否会在根目录列表更改时发出通知。

## 协议消息

### 列出根目录

要检索根目录，服务器发送`roots/list`请求：

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
"method": "roots/list"
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "roots": [
      {
        "uri": "file:///home/user/projects/myproject",
        "name": "我的项目"
      }
    ]
  }
}
```

### 根目录列表变更

当根目录变更时，支持`listChanged`的客户端*必须*发送通知：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/roots/list_changed"
}
```

## 消息流

```mermaid
sequenceDiagram
    participant Server as 服务器
    participant Client as 客户端

    Note over Server,Client: 发现
    Server->>Client: roots/list
    Client-->>Server: 可用根目录

    Note over Server,Client: 变更
    Client--)Server: notifications/roots/list_changed
    Server->>Client: roots/list
    Client-->>Server: 更新后的根目录
```

## 数据类型

### 根目录

根目录定义包括：
* `uri`: 根目录的唯一标识符。在当前规范中*必须*是`file://` URI
* `name`: 可选的人类可读名称，用于显示目的

不同用例的根目录示例：

#### 项目目录

```json
{
  "uri": "file:///home/user/projects/myproject",
  "name": "我的项目"
}
```

#### 多个仓库

```json
[
  {
    "uri": "file:///home/user/repos/frontend",
    "name": "前端仓库"
  },
  {
    "uri": "file:///home/user/repos/backend",
    "name": "后端仓库"
  }
]
```

## 错误处理

客户端*应该*为常见故障情况返回标准JSON-RPC错误：
* 客户端不支持根目录：`-32601`（方法未找到）
* 内部错误：`-32603`

错误示例：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32601,
    "message": "不支持根目录",
    "data": {
      "reason": "客户端不具备roots能力"
    }
  }
}
```

## 安全考虑

1. 客户端*必须*：
   * 仅暴露具有适当权限的根目录
   * 验证所有根目录URI以防止路径遍历
   * 实现适当的访问控制
   * 监控根目录可访问性

2. 服务器*应该*：
   * 处理根目录不可用的情况
   * 在操作中尊重根目录边界
   * 根据提供的根目录验证所有路径

## 实现指南

1. 客户端*应该*：
   * 在向服务器暴露根目录前提示用户同意
   * 提供清晰的根目录管理用户界面
   * 在暴露前验证根目录可访问性
   * 监控根目录变更

2. 服务器*应该*：
   * 在使用前检查roots能力
   * 优雅处理根目录列表变更
   * 在操作中尊重根目录边界
   * 适当缓存根目录信息


# 采样
来源：https://modelcontextprotocol.io/specification/2025-03-26/client/sampling


<Info>**协议修订版**: 2025-03-26</Info>

模型上下文协议(MCP)提供了一种标准化方式，让服务器通过客户端从语言模型请求LLM采样("补全"或"生成")。这种流程允许客户端保持对模型访问、选择和权限的控制，同时使服务器能够利用AI能力——无需服务器API密钥。服务器可以请求基于文本、音频或图像的交互，并可选地在提示中包含来自MCP服务器的上下文。

## 用户交互模型

MCP中的采样允许服务器通过在其他MCP服务器功能中*嵌套*LLM调用来实现代理行为。

实现可以自由地通过任何适合其需求的界面模式暴露采样——协议本身不强制要求任何特定的用户交互模型。

<Warning>
  为了信任与安全，*应该*始终有人参与其中，并能够拒绝采样请求。

  应用程序*应该*：
  * 提供易于直观地审查采样请求的UI
  * 允许用户在发送前查看和编辑提示
  * 在交付前展示生成的响应以供审查
</Warning>

## 能力

支持采样的客户端*必须*在[初始化](/specification/2025-03-26/basic/lifecycle#initialization)期间声明`sampling`能力：

```json
{
  "capabilities": {
    "sampling": {}
  }
}
```

## 协议消息
### 创建消息

要请求语言模型生成，服务器发送`sampling/createMessage`请求：

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "法国的首都是哪里？"
        }
      }
    ],
    "modelPreferences": {
      "hints": [
        {
          "name": "claude-3-sonnet"
        }
      ],
      "intelligencePriority": 0.8,
      "speedPriority": 0.5
    },
    "systemPrompt": "你是一个乐于助人的助手。",
    "maxTokens": 100
  }
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "role": "assistant",
    "content": {
      "type": "text",
      "text": "法国的首都是巴黎。"
    },
    "model": "claude-3-sonnet-20240307",
    "stopReason": "endTurn"
  }
}
```

## 消息流

```mermaid
sequenceDiagram
    participant Server as 服务器
    participant Client as 客户端
    participant User as 用户
    participant LLM as 语言模型

    Note over Server,Client: 服务器发起采样
    Server->>Client: sampling/createMessage

    Note over Client,User: 人工审核环节
    Client->>User: 展示请求等待批准
    User-->>Client: 审核并批准/修改

    Note over Client,LLM: 模型交互
    Client->>LLM: 转发批准的请求
    LLM-->>Client: 返回生成结果

    Note over Client,User: 响应审核
    Client->>User: 展示响应等待批准
    User-->>Client: 审核并批准/修改

    Note over Server,Client: 完成请求
    Client-->>Server: 返回批准的响应
```

## 数据类型

### 消息

采样消息可以包含：

#### 文本内容

```json
{
  "type": "text",
  "text": "消息内容"
}
```

#### 图像内容

```json
{
  "type": "image",
  "data": "base64编码的图像数据",
  "mimeType": "image/jpeg"
}
```

#### 音频内容

```json
{
  "type": "audio",
  "data": "base64编码的音频数据",
  "mimeType": "audio/wav"
}
```

### 模型偏好

MCP中的模型选择需要谨慎抽象，因为服务器和客户端可能使用不同的AI提供商和不同的模型产品。服务器不能简单地按名称请求特定模型，因为客户端可能无法访问该确切模型或可能更喜欢使用不同提供商的等效模型。

为了解决这个问题，MCP实现了一个结合抽象能力优先级和可选模型提示的偏好系统：

#### 能力优先级

服务器通过三个标准化优先级值(0-1)表达其需求：

* `costPriority`: 最小化成本有多重要？值越高越偏好更便宜的模型
* `speedPriority`: 低延迟有多重要？值越高越偏好更快的模型
* `intelligencePriority`: 高级能力有多重要？值越高越偏好更强大的模型

#### 模型提示

虽然优先级有助于根据特性选择模型，但`hints`允许服务器建议特定模型或模型系列：

* 提示被视为可以灵活匹配模型名称的子字符串
* 多个提示按偏好顺序评估
* 客户端*可以*将提示映射到不同提供商的等效模型
* 提示是建议性的——客户端做出最终模型选择

例如：

```json
{
  "hints": [
    { "name": "claude-3-sonnet" }, // 偏好Sonnet类模型
    { "name": "claude" } // 回退到任何Claude模型
  ],
  "costPriority": 0.3, // 成本不太重要
  "speedPriority": 0.8, // 速度非常重要
  "intelligencePriority": 0.5 // 中等能力需求
}
```

客户端处理这些偏好以从其可用选项中选择适当的模型。例如，如果客户端无法访问Claude模型但可以使用Gemini，它可能会根据类似能力将sonnet提示映射到`gemini-1.5-pro`。

## 错误处理

客户端*应该*为常见故障情况返回错误：

错误示例：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -1,
    "message": "用户拒绝了采样请求"
  }
}
```

## 安全考虑

1. 客户端*应该*实现用户批准控制
2. 双方*应该*验证消息内容
3. 客户端*应该*尊重模型偏好提示
4. 客户端*应该*实现速率限制
5. 双方*必须*妥善处理敏感数据


# 规范
来源：https://modelcontextprotocol.io/specification/2025-03-26/index


[模型上下文协议](https://modelcontextprotocol.io) (MCP) 是一个开放协议，使LLM应用程序与外部数据源和工具能够无缝集成。无论您是在构建AI驱动的IDE、增强聊天界面还是创建自定义AI工作流，MCP都提供了一种标准化方式来连接LLM及其所需的上下文。

本规范定义了权威的协议要求，基于TypeScript模式定义：
[schema.ts](https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.ts)。

有关实现指南和示例，请访问：
[modelcontextprotocol.io](https://modelcontextprotocol.io)。

本文档中的关键词"MUST"、"MUST NOT"、"REQUIRED"、"SHALL"、"SHALL NOT"、"SHOULD"、"SHOULD NOT"、"RECOMMENDED"、"NOT RECOMMENDED"、"MAY"和"OPTIONAL"应按照[BCP 14](https://datatracker.ietf.org/doc/html/bcp14) \[[RFC2119](https://datatracker.ietf.org/doc/html/rfc2119)] \[[RFC8174](https://datatracker.ietf.org/doc/html/rfc8174)]中的描述进行解释，且仅当它们以全大写字母出现时（如本文所示）才具有此含义。

## 概述

MCP为应用程序提供了一种标准化方式来：
* 与语言模型共享上下文信息
* 向AI系统暴露工具和能力
* 构建可组合的集成和工作流

该协议使用[JSON-RPC](https://www.jsonrpc.org/) 2.0消息在以下组件之间建立通信：
* **主机(Hosts)**：发起连接的LLM应用程序
* **客户端(Clients)**：主机应用程序中的连接器
* **服务器(Servers)**：提供上下文和能力的服务

MCP部分灵感来自[语言服务器协议](https://microsoft.github.io/language-server-protocol/)，该协议标准化了如何在整个开发工具生态系统中添加编程语言支持。类似地，MCP标准化了如何将额外的上下文和工具集成到AI应用程序生态系统中。

## 关键细节

### 基础协议
* [JSON-RPC](https://www.jsonrpc.org/)消息格式
* 有状态连接
* 服务器和客户端能力协商

### 功能
服务器向客户端提供以下任何功能：
* **资源(Resources)**：供用户或AI模型使用的上下文和数据
* **提示(Prompts)**：为用户提供的模板化消息和工作流
* **工具(Tools)**：供AI模型执行的函数

客户端可以向服务器提供以下功能：
* **采样(Sampling)**：服务器发起的代理行为和递归LLM交互

### 附加实用工具
* 配置
* 进度跟踪
* 取消
* 错误报告
* 日志记录

## 安全与信任保障

模型上下文协议通过任意数据访问和代码执行路径实现了强大的功能。伴随着这种能力而来的是所有实现者必须仔细解决的重要安全和信任考虑。

### 关键原则

1. **用户同意与控制**
   * 用户必须明确同意并理解所有数据访问和操作
   * 用户必须保留对共享数据和采取行动的控制权
   * 实现者应提供清晰的UI来审查和授权活动

2. **数据隐私**
   * 主机必须在向服务器暴露用户数据前获得明确用户同意
   * 主机不得在未经用户同意的情况下将资源数据传输到其他地方
   * 用户数据应受到适当的访问控制保护

3. **工具安全**
   * 工具代表任意代码执行，必须谨慎对待
     * 特别是，工具行为的描述（如注解）应被视为不可信的，除非来自可信服务器
   * 主机必须在调用任何工具前获得明确用户同意
   * 用户应在授权使用前了解每个工具的功能

4. **LLM采样控制**
   * 用户必须明确批准任何LLM采样请求
   * 用户应控制：
     * 是否进行采样
     * 实际发送的提示
     * 服务器可以看到的结果
   * 协议有意限制服务器对提示的可见性

### 实现指南

虽然MCP本身无法在协议层面强制执行这些安全原则，但实现者*应该*：
1. 在应用程序中构建强大的同意和授权流程
2. 提供清晰的安全影响文档
3. 实施适当的访问控制和数据保护
4. 在集成中遵循安全最佳实践
5. 在功能设计中考虑隐私影响

## 了解更多

探索每个协议组件的详细规范：

<CardGroup cols={5}>
  <Card title="架构" icon="sitemap" href="architecture" />

  <Card title="基础协议" icon="code" href="basic" />

  <Card title="服务器功能" icon="server" href="server" />

  <Card title="客户端功能" icon="user" href="client" />

  <Card title="贡献指南" icon="pencil" href="contributing" />
</CardGroup>


# 概述
来源：https://modelcontextprotocol.io/specification/2025-03-26/server/index


<Info>**协议修订版**: 2025-03-26</Info>

服务器通过MCP为语言模型添加上下文提供了基本构建块。这些原语实现了客户端、服务器和语言模型之间的丰富交互：

* **提示(Prompts)**：预定义的模板或指令，指导语言模型交互
* **资源(Resources)**：结构化数据或内容，为模型提供额外上下文
* **工具(Tools)**：可执行函数，允许模型执行操作或检索信息

每个原语可以总结为以下控制层次结构：

| 原语     | 控制方式               | 描述                                         | 示例                          |
| -------- | ---------------------- | -------------------------------------------- | ----------------------------- |
| 提示     | 用户控制               | 通过用户选择调用的交互式模板                 | 斜杠命令、菜单选项            |
| 资源     | 应用程序控制           | 由客户端附加和管理的上下文数据               | 文件内容、git历史             |
| 工具     | 模型控制               | 暴露给LLM以执行操作的函数                    | API POST请求、文件写入        |

在下面更详细地探索这些关键原语：

<CardGroup cols={3}>
  <Card title="提示" icon="message" href="prompts" />

  <Card title="资源" icon="file-lines" href="resources" />

  <Card title="工具" icon="wrench" href="tools" />
</CardGroup>


# 提示
来源：https://modelcontextprotocol.io/specification/2025-03-26/server/prompts


<Info>**协议修订版**: 2025-03-26</Info>

模型上下文协议(MCP)提供了一种标准化方式，让服务器向客户端暴露提示模板。提示允许服务器提供结构化消息和
与语言模型交互的指令。客户端可以发现可用的提示，检索其内容，并提供参数来自定义它们。

## 用户交互模型

提示设计为**用户控制**，意味着它们从服务器暴露给客户端时，目的是让用户能够明确选择使用它们。

通常，提示会通过用户界面中用户发起的命令触发，这允许用户自然地发现和调用可用的提示。

例如，作为斜杠命令：

![提示作为斜杠命令的示例](https://mintlify.s3.us-west-1.amazonaws.com/mcp/specification/2025-03-26/server/slash-command.png)

然而，实现者可以自由地通过任何适合其需求的界面模式暴露提示——协议本身不强制要求任何特定的用户交互模型。

## 能力

支持提示的服务器*必须*在[初始化](/specification/2025-03-26/basic/lifecycle#initialization)期间声明`prompts`能力：

```json
{
  "capabilities": {
    "prompts": {
      "listChanged": true
    }
  }
}
```

`listChanged`指示服务器是否会在可用提示列表更改时发出通知。

## 协议消息

### 列出提示

要检索可用提示，客户端发送`prompts/list`请求。此操作支持[分页](/specification/2025-03-26/server/utilities/pagination)。

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "prompts/list",
  "params": {
    "cursor": "optional-cursor-value"
  }
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "prompts": [
      {
        "name": "code_review",
        "description": "要求LLM分析代码质量并提出改进建议",
        "arguments": [
          {
            "name": "code",
            "description": "要审查的代码",
            "required": true
          }
        ]
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}
```

### 获取提示

要检索特定提示，客户端发送`prompts/get`请求。参数可以通过[补全API](/specification/2025-03-26/server/utilities/completion)自动完成。

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "prompts/get",
  "params": {
    "name": "code_review",
    "arguments": {
      "code": "def hello():\n    print('world')"
    }
  }
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "description": "代码审查提示",
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "请审查这段Python代码：\ndef hello():\n    print('world')"
        }
      }
    ]
  }
}
```

### 列表变更通知

当可用提示列表更改时，声明了`listChanged`能力的服务器*应该*发送通知：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/prompts/list_changed"
}
```

## 消息流

```mermaid
sequenceDiagram
    participant Client as 客户端
    participant Server as 服务器

    Note over Client,Server: 发现
    Client->>Server: prompts/list
    Server-->>Client: 提示列表

    Note over Client,Server: 使用
    Client->>Server: prompts/get
    Server-->>Client: 提示内容

    opt listChanged
      Note over Client,Server: 变更
      Server--)Client: prompts/list_changed
      Client->>Server: prompts/list
      Server-->>Client: 更新后的提示
    end
```

## 数据类型

### 提示

提示定义包括：
* `name`: 提示的唯一标识符
* `description`: 可选的人类可读描述
* `arguments`: 用于自定义的可选参数列表

### 提示消息

提示中的消息可以包含：
* `role`: "user"或"assistant"表示说话者
* `content`: 以下内容类型之一：

#### 文本内容

文本内容表示纯文本消息：

```json
{
  "type": "text",
  "text": "消息的文本内容"
}
这是用于自然语言交互的最常见内容类型。

#### 图像内容

图像内容允许在消息中包含视觉信息：

```json
{
  "type": "image",
  "data": "base64编码的图像数据",
  "mimeType": "image/png"
}
```

图像数据*必须*是base64编码的，并包含有效的MIME类型。这使得在视觉上下文重要时可以进行多模态交互。

#### 音频内容

音频内容允许在消息中包含音频信息：

```json
{
  "type": "audio",
  "data": "base64编码的音频数据",
  "mimeType": "audio/wav"
}
```

音频数据必须是base64编码的，并包含有效的MIME类型。这使得在音频上下文重要时可以进行多模态交互。

#### 嵌入式资源

嵌入式资源允许在消息中直接引用服务器端资源：

```json
{
  "type": "resource",
  "resource": {
    "uri": "resource://example",
    "mimeType": "text/plain",
    "text": "资源内容"
  }
}
```

资源可以包含文本或二进制(blob)数据，并且*必须*包括：
* 有效的资源URI
* 适当的MIME类型
* 文本内容或base64编码的blob数据

嵌入式资源使提示能够无缝地将服务器管理的内容（如文档、代码示例或其他参考资料）直接纳入对话流程。

## 错误处理

服务器*应该*为常见故障情况返回标准JSON-RPC错误：
* 无效提示名称：`-32602`（无效参数）
* 缺少必需参数：`-32602`（无效参数）
* 内部错误：`-32603`（内部错误）

## 实现考虑

1. 服务器*应该*在处理前验证提示参数
2. 客户端*应该*处理大型提示列表的分页
3. 双方*应该*尊重能力协商

## 安全

实现*必须*仔细验证所有提示输入和输出，以防止注入攻击或对资源的未授权访问。


# 资源
来源：https://modelcontextprotocol.io/specification/2025-03-26/server/resources


<Info>**协议修订版**: 2025-03-26</Info>

模型上下文协议(MCP)提供了一种标准化方式，让服务器向客户端暴露资源。资源允许服务器共享为语言模型提供上下文的数据，如文件、数据库模式或应用程序特定信息。每个资源由[URI](https://datatracker.ietf.org/doc/html/rfc3986)唯一标识。

## 用户交互模型

MCP中的资源设计为**应用程序驱动**，主机应用程序根据其需求决定如何合并上下文。

例如，应用程序可以：
* 通过UI元素（如树形或列表视图）暴露资源以供显式选择
* 允许用户搜索和过滤可用资源
* 基于启发式或AI模型的选择实现自动上下文包含

![资源上下文选择器示例](https://mintlify.s3.us-west-1.amazonaws.com/mcp/specification/2025-03-26/server/resource-picker.png)

然而，实现可以自由地通过任何适合其需求的界面模式暴露资源——协议本身不强制要求任何特定的用户交互模型。

## 能力

支持资源的服务器*必须*声明`resources`能力：

```json
{
  "capabilities": {
    "resources": {
      "subscribe": true,
      "listChanged": true
    }
  }
}
```

该能力支持两个可选功能：
* `subscribe`：客户端是否可以订阅以接收单个资源变更的通知
* `listChanged`：服务器是否会在可用资源列表更改时发出通知

`subscribe`和`listChanged`都是可选的——服务器可以都不支持、支持其中一个或两者都支持：

```json
{
  "capabilities": {
    "resources": {} // 两个功能都不支持
  }
}
```

```json
{
  "capabilities": {
    "resources": {
      "subscribe": true // 仅支持订阅
    }
  }
}
```

```json
{
  "capabilities": {
    "resources": {
      "listChanged": true // 仅支持列表变更通知
    }
  }
}
```

## 协议消息

### 列出资源

要发现可用资源，客户端发送`resources/list`请求。此操作支持[分页](/specification/2025-03-26/server/utilities/pagination)。

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "resources/list",
  "params": {
    "cursor": "optional-cursor-value"
  }
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
"resources": [
      {
        "uri": "file:///project/src/main.rs",
        "name": "main.rs",
        "description": "应用程序主要入口点",
        "mimeType": "text/x-rust"
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}
```

### 读取资源

要检索资源内容，客户端发送`resources/read`请求：

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "resources/read",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "contents": [
      {
        "uri": "file:///project/src/main.rs",
        "mimeType": "text/x-rust",
        "text": "fn main() {\n    println!(\"Hello world!\");\n}"
      }
    ]
  }
}
```

### 资源模板

资源模板允许服务器使用[URI模板](https://datatracker.ietf.org/doc/html/rfc6570)暴露参数化资源。参数可以通过[补全API](/specification/2025-03-26/server/utilities/completion)自动完成。

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "resources/templates/list"
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "resourceTemplates": [
      {
        "uriTemplate": "file:///{path}",
        "name": "项目文件",
        "description": "访问项目目录中的文件",
        "mimeType": "application/octet-stream"
      }
    ]
  }
}
```

### 列表变更通知

当可用资源列表更改时，声明了`listChanged`能力的服务器*应该*发送通知：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/list_changed"
}
```

### 订阅

协议支持可选的资源变更订阅。客户端可以订阅特定资源并在它们变更时接收通知：

**订阅请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "method": "resources/subscribe",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}
```

**更新通知：**

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/updated",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}
```

## 消息流

```mermaid
sequenceDiagram
    participant Client as 客户端
    participant Server as 服务器

    Note over Client,Server: 资源发现
    Client->>Server: resources/list
    Server-->>Client: 资源列表

    Note over Client,Server: 资源访问
    Client->>Server: resources/read
    Server-->>Client: 资源内容

    Note over Client,Server: 订阅
    Client->>Server: resources/subscribe
    Server-->>Client: 订阅确认

    Note over Client,Server: 更新
    Server--)Client: notifications/resources/updated
    Client->>Server: resources/read
    Server-->>Client: 更新后的内容
```

## 数据类型

### 资源

资源定义包括：
* `uri`: 资源的唯一标识符
* `name`: 人类可读名称
* `description`: 可选描述
* `mimeType`: 可选MIME类型
* `size`: 可选大小（字节）

### 资源内容

资源可以包含文本或二进制数据：

#### 文本内容

```json
{
  "uri": "file:///example.txt",
  "mimeType": "text/plain",
  "text": "资源内容"
}
```

#### 二进制内容

```json
{
  "uri": "file:///example.png",
  "mimeType": "image/png",
  "blob": "base64编码数据"
}
```

## 常见URI方案
协议定义了几种标准的URI方案。此列表并非详尽无遗——实现总是可以自由使用额外的自定义URI方案。

### https://

用于表示网络上可用的资源。

服务器*应该*仅在客户端能够自行从网络获取和加载资源时使用此方案——也就是说，它不需要通过MCP服务器读取资源。

对于其他用例，服务器*应该*优先使用另一个URI方案，或定义一个自定义方案，即使服务器本身将通过互联网下载资源内容。

### file://

用于标识行为类似文件系统的资源。然而，这些资源不需要映射到实际的物理文件系统。

MCP服务器*可以*使用[XDG MIME类型](https://specifications.freedesktop.org/shared-mime-info-spec/0.14/ar01s02.html#id-1.3.14)标识file://资源，如`inode/directory`，来表示没有标准MIME类型的非普通文件（如目录）。

### git://

Git版本控制集成。

## 错误处理

服务器*应该*为常见故障情况返回标准JSON-RPC错误：
* 资源未找到：`-32002`
* 内部错误：`-32603`

错误示例：

```json
{
  "jsonrpc": "2.0",
  "id": 5,
  "error": {
    "code": -32002,
    "message": "资源未找到",
    "data": {
      "uri": "file:///nonexistent.txt"
    }
  }
}
```

## 安全考虑

1. 服务器*必须*验证所有资源URI
2. *应该*为敏感资源实现访问控制
3. 二进制数据*必须*正确编码
4. *应该*在操作前检查资源权限


# 工具
来源：https://modelcontextprotocol.io/specification/2025-03-26/server/tools


<Info>**协议修订版**: 2025-03-26</Info>

模型上下文协议(MCP)允许服务器暴露可由语言模型调用的工具。工具使模型能够与外部系统交互，如查询数据库、调用API或执行计算。每个工具由名称唯一标识，并包含描述其模式的元数据。

## 用户交互模型

MCP中的工具设计为**模型控制**，意味着语言模型可以根据其上下文理解自动发现和调用工具。

然而，实现可以自由地通过任何适合其需求的界面模式暴露工具——协议本身不强制要求任何特定的用户交互模型。

<Warning>
  为了信任与安全，*应该*始终有人参与其中，并能够拒绝工具调用。
  
  应用程序*应该*：
  
  * 提供明确显示暴露给AI模型的工具的UI
  * 在调用工具时插入清晰的视觉指示器
  * 向用户呈现确认提示以确保有人参与
</Warning>

## 能力

支持工具的服务器*必须*声明`tools`能力：

```json
{
  "capabilities": {
    "tools": {
      "listChanged": true
    }
  }
}
```

`listChanged`指示服务器是否会在可用工具列表更改时发出通知。

## 协议消息

### 列出工具

要发现可用工具，客户端发送`tools/list`请求。此操作支持[分页](/specification/2025-03-26/server/utilities/pagination)。

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {
    "cursor": "optional-cursor-value"
  }
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "get_weather",
        "description": "获取某个位置的当前天气信息",
        "inputSchema": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "城市名称或邮政编码"
            }
          },
          "required": ["location"]
        }
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}
```

### 调用工具

要调用工具，客户端发送`tools/call`请求：

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": {
      "location": "New York"
    }
  }
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
"content": [
      {
        "type": "text",
        "text": "纽约当前天气:\n温度: 72°F\n天气状况: 局部多云"
      }
    ],
    "isError": false
  }
}
```

### 列表变更通知

当可用工具列表更改时，声明了`listChanged`能力的服务器*应该*发送通知：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/tools/list_changed"
}
```

## 消息流

```mermaid
sequenceDiagram
    participant LLM as 语言模型
    participant Client as 客户端
    participant Server as 服务器

    Note over Client,Server: 发现
    Client->>Server: tools/list
    Server-->>Client: 工具列表

    Note over Client,LLM: 工具选择
    LLM->>Client: 选择要使用的工具

    Note over Client,Server: 调用
    Client->>Server: tools/call
    Server-->>Client: 工具结果
    Client->>LLM: 处理结果

    Note over Client,Server: 更新
    Server--)Client: tools/list_changed
    Client->>Server: tools/list
    Server-->>Client: 更新后的工具
```

## 数据类型

### 工具

工具定义包括：
* `name`: 工具的唯一标识符
* `description`: 功能的人类可读描述
* `inputSchema`: 定义预期参数的JSON Schema
* `annotations`: 描述工具行为的可选属性

<Warning>为了信任与安全，客户端*必须*将工具注释视为不可信的，除非它们来自受信任的服务器。</Warning>

### 工具结果

工具结果可以包含不同类型的内容项：

#### 文本内容

```json
{
  "type": "text",
  "text": "工具结果文本"
}
```

#### 图像内容

```json
{
  "type": "image",
  "data": "base64编码数据",
  "mimeType": "image/png"
}
```

#### 音频内容

```json
{
  "type": "audio",
  "data": "base64编码音频数据",
  "mimeType": "audio/wav"
}
```

#### 嵌入式资源

[资源](/specification/2025-03-26/server/resources)*可以*被嵌入，以提供额外的上下文或数据，通过URI客户端可以稍后订阅或再次获取：

```json
{
  "type": "resource",
  "resource": {
    "uri": "resource://example",
    "mimeType": "text/plain",
    "text": "资源内容"
  }
}
```

## 错误处理

工具使用两种错误报告机制：

1. **协议错误**：标准JSON-RPC错误，用于：
   * 未知工具
   * 无效参数
   * 服务器错误

2. **工具执行错误**：在工具结果中用`isError: true`报告：
   * API失败
   * 无效输入数据
   * 业务逻辑错误

协议错误示例：

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "error": {
    "code": -32602,
    "message": "未知工具: invalid_tool_name"
  }
}
```

工具执行错误示例：

```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "获取天气数据失败: API速率限制已超出"
      }
    ],
    "isError": true
  }
}
```

## 安全考虑

1. 服务器*必须*：
   * 验证所有工具输入
   * 实现适当的访问控制
   * 限制工具调用速率
   * 清理工具输出

2. 客户端*应该*：
   * 对敏感操作提示用户确认
   * 在调用服务器前向用户显示工具输入，以避免恶意或意外数据泄露
   * 在传递给LLM前验证工具结果
   * 为工具调用实现超时
   * 记录工具使用情况以供审计


# 补全
来源：https://modelcontextprotocol.io/specification/2025-03-26/server/utilities/completion


<Info>**协议修订版**: 2025-03-26</Info>

模型上下文协议(MCP)提供了一种标准化方式，让服务器为提示和资源URI提供参数自动补全建议。这使得用户可以在输入参数值时获得丰富的、类似IDE的上下文建议体验。
## 用户交互模型

MCP中的补全设计用于支持类似IDE代码补全的交互式用户体验。

例如，应用程序可以在用户输入时以下拉菜单或弹出菜单显示补全建议，并能够从可用选项中进行筛选和选择。

然而，实现可以自由地通过任何适合其需求的界面模式暴露补全功能——协议本身不强制要求任何特定的用户交互模型。

## 能力

支持补全的服务器*必须*声明`completions`能力：

```json
{
  "capabilities": {
    "completions": {}
  }
}
```

## 协议消息

### 请求补全

要获取补全建议，客户端发送`completion/complete`请求，通过引用类型指定要补全的内容：

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "completion/complete",
  "params": {
    "ref": {
      "type": "ref/prompt",
      "name": "code_review"
    },
    "argument": {
      "name": "language",
      "value": "py"
    }
  }
}
```

**响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "completion": {
      "values": ["python", "pytorch", "pyside"],
      "total": 10,
      "hasMore": true
    }
  }
}
```

### 引用类型

协议支持两种补全引用类型：

| 类型           | 描述                 | 示例                                             |
| -------------- | ------------------- | ----------------------------------------------- |
| `ref/prompt`   | 按名称引用提示       | `{"type": "ref/prompt", "name": "code_review"}` |
| `ref/resource` | 引用资源URI          | `{"type": "ref/resource", "uri": "file:///{path}"}` |

### 补全结果

服务器返回按相关性排序的补全值数组，包含：
* 每个响应最多100个项目
* 可选的可用匹配总数
* 布尔值指示是否存在更多结果

## 消息流

```mermaid
sequenceDiagram
    participant Client as 客户端
    participant Server as 服务器

    Note over Client: 用户输入参数
    Client->>Server: completion/complete
    Server-->>Client: 补全建议

    Note over Client: 用户继续输入
    Client->>Server: completion/complete
    Server-->>Client: 精炼后的建议
```

## 数据类型

### CompleteRequest

* `ref`: `PromptReference`或`ResourceReference`
* `argument`: 包含以下内容的对象：
  * `name`: 参数名称
  * `value`: 当前值

### CompleteResult

* `completion`: 包含以下内容的对象：
  * `values`: 建议数组（最多100个）
  * `total`: 可选的总匹配数
  * `hasMore`: 附加结果标志

## 错误处理

服务器*应该*为常见故障情况返回标准JSON-RPC错误：
* 方法未找到：`-32601`（不支持的能力）
* 无效提示名称：`-32602`（无效参数）
* 缺少必需参数：`-32602`（无效参数）
* 内部错误：`-32603`（内部错误）

## 实现考虑

1. 服务器*应该*：
   * 按相关性排序返回建议
   * 在适当的地方实现模糊匹配
   * 限制补全请求速率
   * 验证所有输入

2. 客户端*应该*：
   * 对快速补全请求进行去抖动处理
   * 在适当的地方缓存补全结果
   * 优雅处理缺失或不完整的结果

## 安全

实现*必须*：
* 验证所有补全输入
* 实施适当的速率限制
* 控制对敏感建议的访问
* 防止基于补全的信息泄露


# 日志记录
来源：https://modelcontextprotocol.io/specification/2025-03-26/server/utilities/logging


<Info>**协议修订版**: 2025-03-26</Info>

模型上下文协议(MCP)提供了一种标准化方式，让服务器向客户端发送结构化日志消息。客户端可以通过设置最低日志级别来控制日志详细程度，服务器发送包含严重级别、可选记录器名称和任意JSON可序列化数据的通知。

## 用户交互模型

实现可以自由地通过任何适合其需求的界面模式暴露日志记录功能——协议本身不强制要求任何特定的用户交互模型。

## 能力

发出日志消息通知的服务器*必须*声明`logging`能力：

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

## 日志级别

协议遵循[RFC 5424](https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1)中规定的标准syslog严重级别：

| 级别     | 描述                      | 示例用例           |
| -------- | ------------------------ | ----------------- |
| debug    | 详细的调试信息            | 函数入口/出口点    |
| info      | 一般信息性消息          | 操作进度更新        |
| notice    | 正常但重要的事件        | 配置变更           |
| warning   | 警告条件                | 弃用功能使用       |
| error     | 错误条件                | 操作失败           |
| critical  | 严重条件                | 系统组件故障       |
| alert     | 必须立即采取行动        | 检测到数据损坏     |
| emergency | 系统不可用              | 完全系统故障       |

## 协议消息

### 设置日志级别

要配置最低日志级别，客户端*可以*发送`logging/setLevel`请求：

**请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "logging/setLevel",
  "params": {
    "level": "info"
  }
}
```

### 日志消息通知

服务器使用`notifications/message`通知发送日志消息：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/message",
  "params": {
    "level": "error",
    "logger": "database",
    "data": {
      "error": "连接失败",
      "details": {
        "host": "localhost",
        "port": 5432
      }
    }
  }
}
```

## 消息流

```mermaid
sequenceDiagram
    participant Client as 客户端
    participant Server as 服务器

    Note over Client,Server: 配置日志记录
    Client->>Server: logging/setLevel (info)
    Server-->>Client: 空结果

    Note over Client,Server: 服务器活动
    Server--)Client: notifications/message (info)
    Server--)Client: notifications/message (warning)
    Server--)Client: notifications/message (error)

    Note over Client,Server: 级别变更
    Client->>Server: logging/setLevel (error)
    Server-->>Client: 空结果
    Note over Server: 仅发送错误级别<br/>及以上消息
```

## 错误处理

服务器*应该*为常见故障情况返回标准JSON-RPC错误：
* 无效日志级别：`-32602`（无效参数）
* 配置错误：`-32603`（内部错误）

## 实现考虑

1. 服务器*应该*：
   * 限制日志消息速率
   * 在data字段中包含相关上下文
   * 使用一致的记录器名称
   * 移除敏感信息

2. 客户端*可以*：
   * 在UI中显示日志消息
   * 实现日志过滤/搜索
   * 可视化显示严重级别
   * 持久化日志消息

## 安全

1. 日志消息*不得*包含：
   * 凭据或密钥
   * 个人身份信息
   * 可能帮助攻击的内部系统详情

2. 实现*应该*：
   * 限制消息速率
   * 验证所有数据字段
   * 控制日志访问
   * 监控敏感内容


# 分页
来源：https://modelcontextprotocol.io/specification/2025-03-26/server/utilities/pagination


<Info>**协议修订版**: 2025-03-26</Info>

模型上下文协议(MCP)支持对可能返回大型结果集的操作进行分页。分页允许服务器以较小的块返回结果，而不是一次性返回所有结果。

分页在通过互联网连接到外部服务时特别重要，对于本地集成也很有用，可以避免大数据集的性能问题。

## 分页模型

MCP中的分页使用不透明的基于游标的方法，而不是编号页面。

* **游标**是一个不透明的字符串令牌，表示结果集中的位置
* **页面大小**由服务器决定，客户端*不得*假设固定页面大小

## 响应格式

当服务器发送包含以下内容的**响应**时，分页开始：
* 当前结果页面
* 如果存在更多结果，则包含可选的`nextCursor`字段

```json
{
  "jsonrpc": "2.0",
  "id": "123",
  "result": {
    "resources": [...],
    "nextCursor": "eyJwYWdlIjogM30="
  }
}
```

## 请求格式

收到游标后，客户端可以通过发出包含该游标的请求来*继续*分页：

```json
{
  "jsonrpc": "2.0",
  "method": "resources/list",
  "params": {
    "cursor": "eyJwYWdlIjogMn0="
  }
}
```

## 分页流程

```mermaid
sequenceDiagram
    participant Client as 客户端
    participant Server as 服务器

    Client->>Server: 列表请求(无游标)
    loop 分页循环
      Server-->>Client: 结果页面 + nextCursor
      Client->>Server: 列表请求(带游标)
    end
```

## 支持分页的操作

以下MCP操作支持分页：
* `resources/list` - 列出可用资源
* `resources/templates/list` - 列出资源模板
* `prompts/list` - 列出可用提示
* `tools/list` - 列出可用工具
## 实现指南

1. 服务器*应该*：
   * 提供稳定的游标
   * 优雅处理无效游标

2. 客户端*应该*：
   * 将缺少`nextCursor`视为结果结束
   * 同时支持分页和非分页流程

3. 客户端*必须*将游标视为不透明令牌：
   * 不要对游标格式做假设
   * 不要尝试解析或修改游标
   * 不要跨会话持久化游标

## 错误处理

无效游标*应该*导致代码为-32602（无效参数）的错误。


# 贡献
来源：https://modelcontextprotocol.io/specification/contributing


我们欢迎社区贡献！请查看我们的
[贡献指南](https://github.com/modelcontextprotocol/specification/blob/main/CONTRIBUTING.md)
了解如何提交变更的详细信息。

所有贡献者必须遵守我们的
[行为准则](https://github.com/modelcontextprotocol/specification/blob/main/CODE_OF_CONDUCT.md)。

如有问题和讨论，请使用
[GitHub讨论区](https://github.com/modelcontextprotocol/specification/discussions)。


# 版本控制
来源：https://modelcontextprotocol.io/specification/versioning


模型上下文协议使用基于字符串的版本标识符，格式为
`YYYY-MM-DD`，表示最后一次进行不兼容变更的日期。

<Info>只要变更保持向后兼容性，协议版本*不会*递增。这允许在保持互操作性的同时进行增量改进。</Info>

## 修订状态

修订可能标记为：

* **草案**：进行中的规范，尚未准备好使用
* **当前**：当前协议版本，已准备好使用并可能继续接收向后兼容的变更
* **最终**：过去的完整规范，将不再更改

**当前**协议版本是[**2025-03-26**](/specification/2025-03-26/)。

## 协商

版本协商发生在
[初始化](/specification/2025-03-26/basic/lifecycle#initialization)期间。客户端和服务器*可以*同时支持多个协议版本，但它们*必须*就会话使用的单一版本达成一致。

如果版本协商失败，协议会提供适当的错误处理，允许客户端在找不到与服务器兼容的版本时优雅地终止连接。


# 使用LLM构建MCP
来源：https://modelcontextprotocol.io/tutorials/building-mcp-with-llms

使用Claude等LLM加速您的MCP开发！

本指南将帮助您使用LLM构建自定义模型上下文协议(MCP)服务器和客户端。本教程将重点介绍Claude，但您可以使用任何前沿LLM完成此操作。

## 准备文档

开始前，收集必要的文档以帮助Claude理解MCP：

1. 访问[https://modelcontextprotocol.io/llms-full.txt](https://modelcontextprotocol.io/llms-full.txt)并复制完整文档文本
2. 导航到[MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)或[Python SDK仓库](https://github.com/modelcontextprotocol/python-sdk)
3. 复制README文件和其他相关文档
4. 将这些文档粘贴到您与Claude的对话中

## 描述您的服务器

提供文档后，向Claude清楚地描述您要构建的服务器类型。具体说明：

* 服务器将暴露哪些资源
* 提供哪些工具
* 应该提供哪些提示
* 需要与哪些外部系统交互

例如：

```
构建一个MCP服务器：
- 连接到公司的PostgreSQL数据库
- 将表模式暴露为资源
- 提供运行只读SQL查询的工具
- 包含常见数据分析任务的提示
```

## 与Claude合作

与Claude合作开发MCP服务器时：

1. 首先实现核心功能，然后迭代添加更多特性
2. 请Claude解释您不理解的任何代码部分
3. 根据需要请求修改或改进
4. 让Claude帮助您测试服务器并处理边缘情况

Claude可以帮助实现所有关键的MCP功能：

* 资源管理和暴露
* 工具定义和实现
* 提示模板和处理程序
* 错误处理和日志记录
* 连接和传输设置

## 最佳实践

使用Claude构建MCP服务器时：

* 将复杂服务器分解为较小的部分
* 在继续之前彻底测试每个组件
* 牢记安全性 - 验证输入并适当限制访问
* 为便于将来维护，良好记录代码
* 仔细遵循MCP协议规范

## 后续步骤

Claude帮助您构建服务器后：

1. 仔细检查生成的代码
2. 使用MCP检查器工具测试服务器
3. 将其连接到Claude.app或其他MCP客户端
4. 根据实际使用情况和反馈进行迭代

请记住，随着需求随时间变化，Claude可以帮助您修改和改进服务器。

需要更多指导？只需向Claude提出有关实现MCP功能或解决出现问题的具体问题。