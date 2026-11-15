---
title: 认知科学与程序理解证据备忘录
created_at: 2026-11-11
version: "0.2.1"
status: targeted-evidence-review
topic_id: 20261111-code-aesthetics-batch01
tags: [program-comprehension, cognitive-science, code-aesthetics]
---

# 认知科学与程序理解证据备忘录

> [!WARNING]
> 公开研究草案：Batch01-B仍为PARTIAL，人工研究审核pending，代码／参与者实验未执行。公开提交授权不等于研究通过。
> 本文件是历史记录，其中已读／通过／归档声明不代表当前独立核验。
> 文内“未发布”、本地文件名、行号和检查点属于原研究时点；本页已作公开目录与链接适配，不是字节保真档案。当前阅读顺序与发布边界见[课题入口](../README.md)。


本文件补充代码美学与软件工艺之间的认知机制。它不主张“代码优美”已被认知科学定义，也不提供通用评分量表。

## 核心来源

| ID | 来源 | 读取状态 | 核心贡献 | 主要边界 |
|---|---|---|---|---|
| K01 | Soloway & Ehrlich (1984), *Empirical Studies of Programming Knowledge* | IEEE PDF 全文 | 程序计划和表达惯例影响程序理解 | 旧语言、受控代码片段，不等于大型生产维护 |
| K02 | Green (1989), *Cognitive Dimensions of Notations* | 作者 PDF 全文 | 可见性、黏滞性、隐藏依赖、角色表达性等分析维度 | 概念框架，不是经验证的代码评分量表 |
| K03 | Pennington (1987), *Comprehension Strategies in Programming* | SEI 二手注释摘要 | 程序模型与领域模型交叉参照 | 原始章节未取得，只能作线索 |

## 关键发现与修订

1. 代码阅读者会调用既有程序计划和表达惯例。违反预期的写法可能使理解更难，即使程序仍然可以运行。
2. 记法和环境会改变认知工作：隐藏依赖、信息不可见、修改黏滞和困难心智操作，都会影响理解与设计。
3. 领域代码需要让维护者把程序模型与业务模型联系起来；仅懂调用链不等于懂业务行为。
4. 审美偏好、主观可读性、理解正确率、修改正确率和维护成本是不同变量，必须分别测量。

## 研究建议

Batch02 应先定义行为等价的材料，测量行为预测、领域解释、依赖定位、修改正确性、时间、查找次数和回归情况。主观美感仅作为一个独立结果变量，不应替代实际任务表现。

完整分析见 [08_认知科学与程序理解补充研究](../batch01/cognition.md)；来源账本见 [sources](../evidence/sources.md)。
