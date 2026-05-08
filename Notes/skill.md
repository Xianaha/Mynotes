> **注意：** 本代码库包含 Anthropic 为 Claude 实现的skill。有关 Agent Skills 标准的信息，请访问 [agentskills.io](http://agentskills.io)。

# Skills

skill是包含指令、脚本和资源的文件夹，Claude 会动态加载这些内容以提升其在特定任务上的表现。skill教会 Claude 如何以可重复的方式完成特定任务——无论是依据公司品牌指南创建文档、使用组织特定的工作流分析数据，还是自动化处理个人事务。

更多信息，请查看：
- [什么是skill？](https://support.claude.com/en/articles/12512176-what-are-skills)
- [在 Claude 中使用skill](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [如何创建自定义skill](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [通过 Agent Skills 为现实世界装备智能体](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

# 关于本代码库

本代码库包含一些skill示例，用以展示 Claude skill系统的能力。这些skill涵盖创意应用（艺术、音乐、设计）、技术任务（测试 Web 应用、生成 MCP 服务器）以及企业工作流（沟通、品牌等）。

每个skill都独立存放在自己的文件夹中，并包含一个 `SKILL.md` 文件，里面提供了 Claude 所使用的指令和元数据。你可以浏览这些skill，为自己的skill获取灵感，或理解不同的模式与实现方法。

本代码库中的许多skill采用开源许可证（Apache 2.0）。我们也把驱动 [Claude 文档功能](https://www.anthropic.com/news/create-files) 背后的文档创建与编辑skill（位于 [`skills/docx`](./skills/docx)、[`skills/pdf`](./skills/pdf)、[`skills/pptx`](./skills/pptx) 和 [`skills/xlsx`](./skills/xlsx) 子文件夹中）包含在内。这些skill是源码可用（source-available）而非开源的，但我们希望将它们分享给开发者，作为在生产级 AI 应用中实际使用的复杂skill的参考。

## 免责声明

**这些skill仅供演示和教育目的。** 尽管其中部分能力可能在 Claude 中可用，但你实际使用 Claude 时所获得的实现和行为可能与这些skill中展示的不同。这些skill旨在说明模式和可能性。在将其用于关键任务之前，请始终在你自己的环境中充分测试skill。

# skill集合
- [./skills](./skills)：创意与设计、开发与技术、企业与沟通以及文档skill等示例
- [./spec](./spec)：Agent Skills 规范
- [./template](./template)：skill模板

# 在 Claude Code、Claude.ai 和 API 中尝试

## Claude Code
你可以通过运行以下命令，将此代码库注册为 Claude Code 插件市场：
```
/plugin marketplace add anthropics/skills
```

然后，要安装特定的skill集：
1. 选择 `Browse and install plugins`
2. 选择 `anthropic-agent-skills`
3. 选择 `document-skills` 或 `example-skills`
4. 选择 `Install now`

或者，直接通过以下命令安装任一插件：
```
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

安装插件后，只需提及skill即可使用。例如，如果你从市场安装了 `document-skills` 插件，你可以这样要求 Claude Code：“使用 PDF skill从 `path/to/some-file.pdf` 中提取表单字段”

## Claude.ai

这些示例skill在 Claude.ai 中都已对付费套餐用户开放。

要使用本代码库中的任何skill或上传自定义skill，请按照 [在 Claude 中使用skill](https://support.claude.com/en/articles/12512180-using-skills-in-claude#h_a4222fa77b) 中的说明操作。

## Claude API

你可以通过 Claude API 使用 Anthropic 预构建的skill，以及上传自定义skill。更多信息请参见 [Skills API 快速入门](https://docs.claude.com/en/api/skills-guide#creating-a-skill)。

# 创建一个基本skill

创建skill非常简单——只需一个包含 `SKILL.md` 文件的文件夹，文件内含有 YAML 前置元数据和指令。你可以使用本代码库中的 **template-skill** 作为起点：

```markdown
---
name: my-skill-name
description: 清晰描述此skill的功能及使用时机
---

# 我的skill名称

[在此添加当此skill激活时 Claude 需遵循的指令]

## 示例
- 示例用法 1
- 示例用法 2

## 指南
- 指南 1
- 指南 2
```

前置元数据只需要两个字段：
- `name` - skill的唯一标识符（小写，空格用连字符代替）
- `description` - 对skill功能和使用时机的完整描述

下面的 markdown 内容包含 Claude 需遵循的指令、示例和指南。更多详情请参见 [如何创建自定义skill](https://support.claude.com/en/articles/12512198-creating-custom-skills)。

# 合作伙伴skill

skill是教会 Claude 更好使用特定软件的好方法。当我们看到来自合作伙伴的优秀skill示例时，可能会在此处展示其中一些：

- **Notion** - [适用于 Claude 的 Notion skill](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0)