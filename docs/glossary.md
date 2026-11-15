# 术语与分级对照

本页对齐各专题中名称不同、所指相近的概念，并区分名称相同、含义不同的概念。它是阅读索引，不是新的标准：每个术语的权威定义仍以所列来源文档为准；对齐关系是[阶段性综合](stage-review-2026-11.md)提出的综合推论，未经人工研究审核。

## 1. 所有权与生命周期

| 本页用语 | 各专题中的写法 | 含义 | 来源 |
|---|---|---|---|
| 执行位置 | 执行位置、owner线程、执行上下文 | 当前代码在哪个线程或调度上下文运行，能否调用目标API | [Unity任务生命周期](../research/unity-task-lifetime/report.md) |
| 提交资格 | 提交资格、写入资格、业务有效期、当前有效请求 | 一个结果此刻是否仍有权改变owner的状态 | [Unity任务生命周期](../research/unity-task-lifetime/report.md)、[代码优美论](../research/code-aesthetics/final/article.md) |
| 请求身份 | 请求代次、请求标识、展示代次、业务会话身份 | 用于判断提交资格的身份；同一实例重开、归池复用或切换目标时更新 | [AI-CQEP](../research/ai-cqep/AI-CQEP.md)、[工程判断](../research/engineering-judgment/engineering-judgment-report.md) |
| 资源归属 | 资源归属、ownership、释放责任 | 某份需要释放的结果此刻由producer、接收路径还是owner负责 | [Unity任务生命周期](../research/unity-task-lifetime/report.md)、[客户端代码质量](../research/client-code-quality/research-report.md) |
| 交接点 | 接管、Adopt、责任转移点 | 资源归属从接收路径转移到owner的唯一时刻；失败时保持原归属 | [Unity任务生命周期](../research/unity-task-lifetime/report.md) |
| 取消 | 请求取消、Cancel | 请求减少不再需要的工作；不证明工作已停止、不会返回资源或无需清理 | [Unity任务生命周期](../research/unity-task-lifetime/report.md) |
| 停止等待 | 超时、调用方不再等待 | 调用方不再等待结果；后台工作可能仍在进行，迟到结果仍需接收与清理 | [客户端代码质量](../research/client-code-quality/research-report.md) |
| 完成／消费／复用 | 终态、GetResult、TryReturn、归池 | 逻辑终态、带清理副作用的消费、物理复用是三件事 | [工程判断案例库](../research/engineering-judgment/case-library.md) |

贯穿原则：**不再需要不等于不再负责**；对象仍有效不等于请求仍有效。

## 2. 变更风险分级

三套分级的触发逻辑相近，但适用场景不同，不能互换名称。AI-CQEP的L/M/H是**变更风险**，与下一节能力等级中的L1–L5无关。

| 大致对应 | [工程判断Tier](../research/engineering-judgment/decision-handbook.md) | [AI-CQEP风险](../research/ai-cqep/QUICK-REFERENCE.md) | [代码优美论判断卡](../research/code-aesthetics/final/article.md) |
|---|---|---|---|
| 低 | Tier 1：已知路径、局部、低后果、可恢复；四问短卡 | L：局部、已知、可逆；自查；常规功能仍先审方案 | 几句话说明问题、约束、选择、依据、停止 |
| 中 | Tier 2：新状态、异步、配置或协议交互，多个owner；一页决策与验证矩阵 | M：重要协作、错误路径、异步或事件有效期；定向独立审阅 | 随风险与不可逆性增加记录与验证 |
| 高 | Tier 3：公共核心、持久化、兼容迁移、不可恢复风险；ADR、独立验收、恢复演练 | H：安全、资金、不可逆数据、公共协议、所有权或并发策略；独立审查 | 同上，不设固定档位 |

共同规则：按最高后果升级，不取平均；不按代码行数分级；诊断与实施可分别分级；可回滚代码不等于可撤回经济、数据或玩家损害。

主要差异：AI-CQEP面向“人审方案、AI实施”的工作流，常规功能无论风险高低都先经一次整体方案审核；工程判断Tier面向工程师自身的分析深度，Tier 1不要求方案审核。

原始报告的A/B/C是**AI委托类别**（按规格清晰度、验证自动化、失败代价划分），不是变更分级，见[原始深度研究报告](manifesto.md)。

## 3. 能力等级

以下三套均为待检验提案，不是行业标准或已验证量表。仓库不合并它们。

| 模型 | 结构 | 来源 | 当前角色 |
|---|---|---|---|
| L1–L4 | 实现者、模块负责人、系统工程师、技术负责人 | [原始深度研究报告](manifesto.md) | 保真导入的研究输入 |
| L1–L5 | 五级历史提案 | [历史草稿](historical/deep-research-draft.md) | 仅供追溯 |
| 十四域×五级 | 需求、项目、系统建模等十四个域，各自L1–L5行为锚点 | [工程判断训练手册](../research/engineering-judgment/training-and-assessment-handbook.md) | 未验证效度的训练设计 |

共同点：等级跃迁按责任范围与证据定义，不按工龄或代码难度；一个人在不同域可处于不同等级。

## 4. 停止条件

| 来源 | 写法 |
|---|---|
| [工程判断](../research/engineering-judgment/decision-handbook.md) | S1理解够用；S2决策稳定；S3风险可控；S4验证可反驳；S5边际收益下降；S6责任明确 |
| [代码优美论](../research/code-aesthetics/final/article.md) | 目标已达到；剩余收益无具体依据且成本超预算；新证据显示负担正转移到更重要处 |
| [AI-CQEP](../research/ai-cqep/QUICK-REFERENCE.md) | 开发验证完成、提测就绪、QA通过、发布许可是四个不同的“完成” |

## 5. 状态词表

一项产出可以同时处于多种状态，它们彼此独立，不能互相推出。下表记录各专题原文中出现的写法；今后专题元数据只使用[受控词表](../knowledge/vocabulary.json)中的规范取值，对应关系见[知识库架构](knowledge-architecture.md)。

| 维度 | 回答的问题 | 仓库中出现的值 |
|---|---|---|
| 编辑 | 写完了吗？ | final、draft、draft-for-owner-review |
| 人工审核 | 有权限的人审过吗？ | pending、awaiting_review、unknown（无状态文件，不推定已审） |
| 证据 | 承重来源核验到什么程度？ | PARTIAL、draft-with-evidence-gaps、source-grounded-draft-with-limitations |
| 实验 | 代码或参与者实验运行了吗？ | not-run |
| 发布 | 是否获授权公开？ | authorized-public-snapshot；原稿中的not-published为历史状态 |

审校结论另有PASS、PASS_WITH_LIMITATIONS、PARTIAL、FAIL四档，定义见[代码优美论审校结论](../research/code-aesthetics/audit/conclusion.md)。陈述类型（来源事实、特定案例、综合推论、待验证假设）见[研究方法](research-method.md)。

## 6. 独立验证

独立性指**错误来源尽可能不同**，不是人与AI的身份标签。第二个模型或新会话、人工源码审查、独立需求测试、性质与故障注入、目标运行观测、有权限的领域审查各自能增加什么、仍会遗漏什么，见[人机协作手册](../research/engineering-judgment/human-ai-collaboration-handbook.md)。

返回[项目首页](../README.md)。
