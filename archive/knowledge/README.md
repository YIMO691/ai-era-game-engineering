# 知识地图

本页由 `python -I scripts/check_docs.py --write-index` 根据各专题的 `meta.json`、[命题登记](claims.json)与[受控词表](vocabulary.json)生成，请勿手工编辑；检查器会拒绝过期版本。架构与维护规则见[知识库架构](../docs/knowledge-architecture.md)。

## 专题

| 专题 | 核心问题 | 成熟度 | 编辑／审核／证据／实验 |
|---|---|---|---|
| [AI代码质量工作流](../research/ai-code-quality-workflow/README.md) | 怎样把项目约束、最小修改、可执行检查、定向审查与反馈接成可追溯的 AI 工作链？ | 成稿 | 草稿／待审／部分核验／未执行 |
| [AI-CQEP工程协议](../research/ai-cqep/README.md) | AI 参与研发时，用什么最小协议组织理解、方案、实现、验证、审查与反馈？ | 成稿 | 草稿／未知／部分核验／未执行 |
| [客户端代码质量](../research/client-code-quality/README.md) | 如何判断 Unity/C# 客户端代码的质量、开展审查，并把案例用于训练？ | 成稿 | 草稿／待审／部分核验／未执行 |
| [代码优美与工程品质](../research/code-aesthetics/README.md) | AI时代为什么仍要把代码写好；何时抽象、重构或停止？ | 成稿 | 定稿／待审／部分核验／未执行 |
| [工程判断与人机协作](../research/engineering-judgment/README.md) | 工程判断力能否拆解、训练与评价；AI 时代人应强化什么？ | 成稿 | 草稿／待审／部分核验／未执行 |
| [Unity异步任务生命周期](../research/unity-task-lifetime/README.md) | 场景退出或请求替换后，旧任务的结果由谁决定能否提交、由谁负责释放？ | 成稿 | 草稿／待审／部分核验／未执行 |

## 按领域

| 领域 | 专题 |
|---|---|
| 异步与生命周期 | [Unity异步任务生命周期](../research/unity-task-lifetime/README.md) |
| 资源归属与释放 | [Unity异步任务生命周期](../research/unity-task-lifetime/README.md) |
| 代码质量与表达 | [AI-CQEP工程协议](../research/ai-cqep/README.md)、[客户端代码质量](../research/client-code-quality/README.md)、[代码优美与工程品质](../research/code-aesthetics/README.md) |
| 审查与验证 | [AI代码质量工作流](../research/ai-code-quality-workflow/README.md)、[AI-CQEP工程协议](../research/ai-cqep/README.md)、[客户端代码质量](../research/client-code-quality/README.md) |
| AI 协作工作流 | [AI代码质量工作流](../research/ai-code-quality-workflow/README.md)、[AI-CQEP工程协议](../research/ai-cqep/README.md)、[代码优美与工程品质](../research/code-aesthetics/README.md)、[工程判断与人机协作](../research/engineering-judgment/README.md) |
| 工程判断 | [工程判断与人机协作](../research/engineering-judgment/README.md) |
| 学习、训练与评估 | [客户端代码质量](../research/client-code-quality/README.md)、[工程判断与人机协作](../research/engineering-judgment/README.md) |
| 品质动机与工程审美 | [代码优美与工程品质](../research/code-aesthetics/README.md) |

## 按读者

| 读者 | 专题 |
|---|---|
| 一线工程师 | [AI代码质量工作流](../research/ai-code-quality-workflow/README.md)、[AI-CQEP工程协议](../research/ai-cqep/README.md)、[客户端代码质量](../research/client-code-quality/README.md)、[代码优美与工程品质](../research/code-aesthetics/README.md)、[工程判断与人机协作](../research/engineering-judgment/README.md)、[Unity异步任务生命周期](../research/unity-task-lifetime/README.md) |
| 技术负责人与审查者 | [AI代码质量工作流](../research/ai-code-quality-workflow/README.md)、[AI-CQEP工程协议](../research/ai-cqep/README.md)、[客户端代码质量](../research/client-code-quality/README.md)、[代码优美与工程品质](../research/code-aesthetics/README.md)、[工程判断与人机协作](../research/engineering-judgment/README.md)、[Unity异步任务生命周期](../research/unity-task-lifetime/README.md) |
| 学习者与带教者 | [客户端代码质量](../research/client-code-quality/README.md)、[工程判断与人机协作](../research/engineering-judgment/README.md) |
| 研究者 | [代码优美与工程品质](../research/code-aesthetics/README.md)、[工程判断与人机协作](../research/engineering-judgment/README.md) |

## 命题：按责任—证据—限度

一条命题可以落在多条轴上，此处按第一条轴归类。类型与状态的含义见受控词表；“有支撑”只在所列证据范围内成立，不等于经过人工审核或实验。

### 责任

| 编号 | 命题 | 类型 | 状态 | 专题 | 实践规则 |
|---|---|---|---|---|---|
| K-001 | 异步、复用与生命周期中的“完成”可分解为执行位置、提交资格与资源归属等相互独立的问题；任一问题的肯定答案不能推出其他问题的答案。 | 综合推论 | 有支撑 | [Unity异步任务生命周期](../research/unity-task-lifetime/README.md)、[工程判断与人机协作](../research/engineering-judgment/README.md)、[客户端代码质量](../research/client-code-quality/README.md)、[代码优美与工程品质](../research/code-aesthetics/README.md) | G-12 |
| K-002 | 不再需要一个结果，不等于不再负责这个结果；取消只是请求减少工作，不证明工作已停止、不会返回资源或无需清理。 | 综合推论 | 有支撑 | [Unity异步任务生命周期](../research/unity-task-lifetime/README.md)、[客户端代码质量](../research/client-code-quality/README.md)、[AI-CQEP工程协议](../research/ai-cqep/README.md) | G-13、G-17、G-18 |
| K-003 | 提交资格应由业务 owner 管理的请求身份（代次或唯一标识）判断；对象仍有效不推出结果仍可提交。 | 逻辑论证 | 有支撑 | [Unity异步任务生命周期](../research/unity-task-lifetime/README.md)、[代码优美与工程品质](../research/code-aesthetics/README.md)、[AI-CQEP工程协议](../research/ai-cqep/README.md) | G-14、G-15、G-16 |
| K-004 | UniTask 2.5.10 的限定 DelayPromise 中途取消路径中，取消包装的 canceled 分支绕过底层 GetResult，未走到已读的 TryReturn 归池路径。 | 来源事实 | 有支撑 | [工程判断与人机协作](../research/engineering-judgment/README.md) | — |
| K-005 | NGO 1.9.1 中，业务 OnNetworkDespawn 之后旧网络流程仍有读取；收到生命周期通知不等于实例可立即复用。 | 来源事实 | 有支撑 | [工程判断与人机协作](../research/engineering-judgment/README.md) | G-21 |
| K-015 | AI 改变的是工程成本的分布，不改变谁接受风险、谁确认约束、谁决定发布与回滚。 | 价值或规范立场 | 有支撑 | [代码优美与工程品质](../research/code-aesthetics/README.md)、[工程判断与人机协作](../research/engineering-judgment/README.md)、[AI-CQEP工程协议](../research/ai-cqep/README.md) | G-50、G-51 |

### 证据

| 编号 | 命题 | 类型 | 状态 | 专题 | 实践规则 |
|---|---|---|---|---|---|
| K-006 | 主张什么，就需要什么类型的证据；证据的身份（官方、源码、论文）与它能否支持这一类主张要分开判断。 | 价值或规范立场 | 有支撑 | [工程判断与人机协作](../research/engineering-judgment/README.md)、[AI-CQEP工程协议](../research/ai-cqep/README.md)、[代码优美与工程品质](../research/code-aesthetics/README.md) | G-32 |
| K-007 | 编辑、人工审核、证据、实验与发布五种状态彼此正交，任一状态不能推出另一状态。 | 概念区分 | 有支撑 | [代码优美与工程品质](../research/code-aesthetics/README.md)、[工程判断与人机协作](../research/engineering-judgment/README.md) | G-33 |
| K-008 | 验证的独立性指错误来源不同，而不是审查者身份不同；多个模型或多次询问一致不构成独立验证。 | 逻辑论证 | 有支撑 | [工程判断与人机协作](../research/engineering-judgment/README.md)、[AI-CQEP工程协议](../research/ai-cqep/README.md)、[代码优美与工程品质](../research/code-aesthetics/README.md) | G-36、G-48 |
| K-009 | 样例、注释与测试本身也要被审查；测试通过只证明它检查的那部分成立。 | 特定案例 | 有支撑 | [工程判断与人机协作](../research/engineering-judgment/README.md) | G-34 |
| K-014 | AI 节省的时间转为品质收益需要三个条件同时成立：净节约确实存在、部分资源确实分配给品质、这次投入对具体问题有效。 | 逻辑论证 | 有支撑 | [代码优美与工程品质](../research/code-aesthetics/README.md) | G-52 |
| K-016 | Peng 等 v1 的标准化 JavaScript HTTP server 实验中，完成者耗时减少 55.8%（95% CI 21%–89%）；研究未测代码质量。 | 来源事实 | 有支撑 | [工程判断与人机协作](../research/engineering-judgment/README.md) | — |
| K-017 | METR 2026-02-24 跟进的两个子集中心估计显示耗时下降，但区间跨零，并披露了选择、完成、计时与产物差异。 | 来源事实 | 有支撑 | [工程判断与人机协作](../research/engineering-judgment/README.md) | — |
| K-018 | 项目宗旨所引的两项 AI 效率数字（约 26% 提升、约 19% 变慢）可以作为论据使用。 | 来源事实 | 受质疑 | （宗旨） | — |
| K-021 | 把项目约束、最小修改、可执行检查、定向审查和反馈接成工作链，比新增生成工具或全套插件更能改善 AI 参与的交付质量。 | 待验证假设 | 提出 | [AI代码质量工作流](../research/ai-code-quality-workflow/README.md)、[AI-CQEP工程协议](../research/ai-cqep/README.md) | G-41、G-48、G-49 |
| K-022 | 工程判断力可以通过“事前预测—外部反馈—新题迁移”的产物来训练与观察，而不是按工龄或阅读量评价。 | 待验证假设 | 提出 | [工程判断与人机协作](../research/engineering-judgment/README.md) | G-54、G-55 |

### 限度

| 编号 | 命题 | 类型 | 状态 | 专题 | 实践规则 |
|---|---|---|---|---|---|
| K-010 | 分析、审查与验证的深度应由后果、传播、未知与可检测/可恢复性决定，任一维度为高即升级，不取平均；代码行数不是风险指标。 | 综合推论 | 有支撑 | [工程判断与人机协作](../research/engineering-judgment/README.md)、[AI-CQEP工程协议](../research/ai-cqep/README.md)、[代码优美与工程品质](../research/code-aesthetics/README.md) | G-7、G-9、G-10、G-11 |
| K-011 | 可回滚的代码不等于可撤回的经济、数据或玩家损害；后者的风险不能用代码回滚能力来降级。 | 逻辑论证 | 有支撑 | [工程判断与人机协作](../research/engineering-judgment/README.md)、[AI-CQEP工程协议](../research/ai-cqep/README.md) | G-8、G-38 |
| K-012 | 工程判断的 Tier 1–3 与 AI-CQEP 的 L/M/H 在触发逻辑上可以对齐；差异在于 AI-CQEP 的常规功能无论风险都先审方案。 | 综合推论 | 提出 | [工程判断与人机协作](../research/engineering-judgment/README.md)、[AI-CQEP工程协议](../research/ai-cqep/README.md) | — |
| K-013 | 停止条件应在事前写下；“关键未知的合理变化不会改变选择”是判断能否停止的可回答问题。 | 综合推论 | 有支撑 | [工程判断与人机协作](../research/engineering-judgment/README.md)、[代码优美与工程品质](../research/code-aesthetics/README.md) | G-37、G-39 |
| K-019 | 追求品质有内在满足、对他人的责任、工具性收益三种理由；动机是否值得尊重、改动是否有效、投入是否适当需分别判断。 | 概念区分 | 有支撑 | [代码优美与工程品质](../research/code-aesthetics/README.md) | G-2 |
| K-020 | 判断重复与抽象应看是否因同一原因而变化、隐藏了什么知识，而不是出现次数或外观整洁。 | 综合推论 | 有支撑 | [代码优美与工程品质](../research/code-aesthetics/README.md)、[客户端代码质量](../research/client-code-quality/README.md)、[工程判断与人机协作](../research/engineering-judgment/README.md)、[AI-CQEP工程协议](../research/ai-cqep/README.md) | G-24、G-25 |

## 待处理：受质疑、仅提出或待验证的命题

| 编号 | 状态 | 推翻条件或缺口 |
|---|---|---|
| K-012 | 提出 | 对齐由阶段性综合提出，未经人工审核。 |
| K-018 | 受质疑 | 宗旨正文与来源登记的未核状态存在张力，见阶段性综合 7.5 节；待所有者决定如何处理宗旨正文。 |
| K-021 | 提出 | 尚无对照数据。 |
| K-022 | 提出 | 未验证效度与效果。 |

## 命题证据

| 编号 | 证据位置 |
|---|---|
| K-001 | [第 1–2 节：三个问题与固定源码的四条边界](../../book/part3-system/3-1-the-late-result.md)；[C1/C2 的反例结构](../../book/appendix-d-cases.md)；[命题一的跨专题对齐](../../book/part1-method/1-4-ownership-evidence-bound.md) |
| K-002 | [第 2.1、4 节：取消入口与资源交接协议](../../book/part3-system/3-1-the-late-result.md)；[8.3 超时要说清是哪一层停止](../../book/part7-craft/7-1-client-code-quality.md)；[Unity/C# 适配案例的契约](../../book/part8-ai-team/8-2-ai-cqep-protocol.md) |
| K-003 | [2.3、3 节：对象有效性不等于请求身份](../../book/part3-system/3-1-the-late-result.md)；[第五节贯穿案例](../../book/part1-method/1-2-why-write-good-code.md) |
| K-004 | [C1，固定 SHA 静态阅读，未运行](../../book/appendix-d-cases.md)；[5.1 节](../../book/part1-method/1-3-engineering-judgment.md) |
| K-005 | [C2，固定 SHA 静态阅读，未运行](../../book/appendix-d-cases.md)；[5.2 节](../../book/part1-method/1-3-engineering-judgment.md) |
| K-006 | [如何描述证据](../../book/appendix-h-research-method.md)；[命题二](../../book/part1-method/1-4-ownership-evidence-bound.md) |
| K-007 | [命题二与状态词表](../../book/part1-method/1-4-ownership-evidence-bound.md)；[状态词表](../../book/appendix-b-glossary.md) |
| K-008 | [人机职责与独立验证](../research/engineering-judgment/human-ai-collaboration-handbook.md)；[第六节：更多候选不等于更多独立证据](../../book/part1-method/1-2-why-write-good-code.md) |
| K-009 | [C2 中 XML 默认值与签名不一致、关服测试的 oracle 问题](../../book/appendix-d-cases.md) |
| K-010 | [第 3–4 节：分析深度与分级协议](../research/engineering-judgment/decision-handbook.md)；[4.1 风险裁剪](../../book/part8-ai-team/8-2-ai-cqep-protocol.md)；[命题三](../../book/part1-method/1-4-ownership-evidence-bound.md) |
| K-011 | [1 节关键修订第 5 条](../../book/part1-method/1-3-engineering-judgment.md)；[第 4 节：最小有效分级协议](../research/engineering-judgment/decision-handbook.md) |
| K-012 | [4.3 本文的对齐](../../book/part1-method/1-4-ownership-evidence-bound.md)；[变更风险分级](../../book/appendix-b-glossary.md) |
| K-013 | [第 5 节：S1–S6 停止规则](../research/engineering-judgment/decision-handbook.md)；[第七节停止信号](../../book/part1-method/1-2-why-write-good-code.md) |
| K-014 | [第六节：从生成收益到品质收益](../../book/part1-method/1-2-why-write-good-code.md) |
| K-015 | [第六节](../../book/part1-method/1-2-why-write-good-code.md)；[命题五](../../book/part1-method/1-4-ownership-evidence-bound.md) |
| K-016 | [第 8 节](../../book/part1-method/1-3-engineering-judgment.md)；[正文已读](../research/engineering-judgment/ai-evidence-notes.md) |
| K-017 | [第 8 节](../../book/part1-method/1-3-engineering-judgment.md)；[正文已读](../research/engineering-judgment/ai-evidence-notes.md) |
| K-018 | [正文引用](../../book/part1-method/1-1-from-code-to-responsibility.md)；[Q-01/Q-02 未核验，URL 未提供](../research/sources.md) |
| K-019 | [第二节](../../book/part1-method/1-2-why-write-good-code.md) |
| K-020 | [第三节](../../book/part1-method/1-2-why-write-good-code.md)；[第 6 节：抽象与必要复杂性](../../book/part7-craft/7-1-client-code-quality.md)；[第 6 节：抽象与复用](../research/engineering-judgment/decision-handbook.md)；[5.3 复用与新增抽象的闸门](../../book/part8-ai-team/8-2-ai-cqep-protocol.md) |
| K-021 | [结论](../../book/part8-ai-team/8-1-ai-quality-chain.md)；[11.2 如何检验](../../book/part8-ai-team/8-2-ai-cqep-protocol.md) |
| K-022 | [第 9 节](../../book/part1-method/1-3-engineering-judgment.md)；[十四域×五级与十二周设计](../research/engineering-judgment/training-and-assessment-handbook.md) |

返回[项目首页](../../README.md)。
