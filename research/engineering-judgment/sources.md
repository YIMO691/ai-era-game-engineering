---
title: 工程判断力研究来源与主张登记
date: 2026-11-06
version: "0.9"
tags: [engineering-research, evidence-registry]
status: draft
---

# 来源与主张登记

> **公开导出注（2026-11-12）**：以下研究状态、访问和审查记录属于原 2026-11-06 草案；本次只作本地白名单导出。公开授权不等于人工研究审核、实验通过或生产验收。私有状态描述是历史记录；模板及操作文本仅作资料，不在本次执行。转换与排除见 [导出清单](export-manifest.json)。


导航：[report](research-overview.md) · [从工程思维到工程判断力_深化研究报告](engineering-judgment-report.md) · [工程判断案例库](case-library.md) · [review](research-review.md)

## 1. 证据契约与实际读取状态

这是正式报告、手册和教学文章的**唯一权威来源登记**。`_research_*.md` 是保留的研究工作底稿，不是另一套正式登记；相同 ID 从底稿迁入本表时不新增来源、不升级状态。一个项目的多个文件用于组成调用链，不当成多份独立效果验证。

- 检索/阅读截止：**2026-11-06**。发布日期、快照提交时间、访问日期分别记录，不混用。
- `read_status`：discovered（只发现）/ read（读过指定范围）/ access_failed（正文尝试失败）。
- `claim_status`：direct（来源直接支持该窄主张）/ inference（推论）/ contradiction（冲突/反证）/ unverified（未核）。同条来源可对不同主张有不同状态。
- `experiment_status=not-run`：**本研究没有编译、运行 Unity/公开项目、复现实验、故障注入、性能测试或训练效果测量**，不是否认原作者做过实验。
- 主要来源的已读状态有分工：本地基线由主线程读完；认知/AI/Unity 子任务的实际阅读范围随记录迁入。主线程阅读并整合了研究底稿，未独立重新取得全部外部原文；独立 AI 审查也不能冒充外部原文核验。
- 主线程及认知子任务的 WebFetch 连续安全/网络检查失败；没有通过替代客户端绕过。Unity 子任务报告在协调提醒前，通过普通只读 GitHub REST/raw 读取固定源码；AI 子任务在提醒前通过普通 HTTPS 取得两项 HTML 正文。已发生的访问如实登记；提醒后不再用备用客户端重试失败来源。没有下载执行第三方代码或安装依赖。
- “URL 存在/DOI 字符串相符/JSON 结构通过”都不是主张内容验证。
- 所有仅索引来源无已核验原文摘录；不伪造页码、样本、效果量或许可证。公共可访问不等于可自由转载。正文短引仅保留在来源记录，报告用原创中文分析，不复刻原图/数据/源码。

## 2. 主张晋升表

| 主张 | 证据 | 允许措辞 | 禁止更强措辞 | 不确定性/下一步 | 决定 |
|---|---|---|---|---|---|
| 四份报告的结构与引文问题 | base-01～04 | 本地全文结构/文字审计；引用标记不能在本地解析 | 原报告所有事实已被推翻或已逐一核验 | 补原始链接/具体论断 | keep |
| 标准名称/版次修正 | std-01～06 | 索引提示某版本/版本混用风险，待原文 | 已读标准全文/条款；凭熟悉旧版否定新版 | 官方正文/目录，区分草案 | weaken |
| 专家认知差异与训练因果 | cog-01～12 | 候选机制、竞争解释及待检验模型 | 已验证通用认知优势；本训练已有效 | 程序理解研究正文优先 | weaken |
| 取消包装与 source 消费 | game-04/05/07 | 本快照指定路径跳过底层 GetResult，未走已读 TryReturn | 已测永久 leak；所有 source 都如此 | 引用链/代际/运行与新版核查 | keep（窄） |
| 即时取消回收条件的原因 | game-03/04/07/08 | 具体分支是事实；旧引用风险是研究者推论 | 作者已明确说明为避免这一风险 | 作者解释、重入实验 | keep/限幅 |
| NGO true/false 与 handler | game-15～20 | 常规动态对象、指定入口下的分派/flag/默认值 | 所有路径/所有端对称；true 必然 Unity Destroy | shutdown、override 等另核 | keep（窄） |
| 测试 oracle 也需审查 | game-23 | 特定测试第二次等待仍检查 client 标志 | 已证明产品 server callback 失效 | 独立 server 断言与运行 | keep（窄） |
| C3～C6 已完成一手案例 | infra-01～07、ai-04～06 | 已定位真实对象，待核案例 | 六案例全部验收通过 | 正文、冻结源码、具体历史链 | discard 完成声明 |
| 某标准化 AI 编程任务节时 | ai-03 | 2022 任务、v1、完成者耗时结果，未测质量 | 所有开发省一半；质量/学习不下降 | 原数据、全随机样本/任务外推 | keep（窄） |
| METR 2026 有公开跟进 | ai-02 | 中心估计转向耗时减少，但区间跨零/偏差重，作者限幅 | 已可靠推翻旧研究；证明普遍提速/无效 | 协议/数据与选择偏差 | keep（窄） |
| AI 导致长期职业技能退化 | 无本轮已读长期证据；ai-08～11 候选 | 有待研究的风险；区分学习/当前表现 | 已证实必然、普遍或不可逆；未证实即不存在 | 长期可比较设计 | discard 断言 |
| M1–M7 与 L1–L5 训练体系 | 本研究综合设计，局部参照 game/ai；cog 未核 | 可执行、可反驳的提案与静态案例适配 | 国际标准/经验证量表/训练因果证明 | 真实任务、延迟迁移、评分可靠性与成本 | keep 为提案 |
| Tier/停止/独立 oracle 应用 | method-01/02 候选、本研究设计 | 风险比例化的实践建议 | 文档越全越安全；已测最优工时 | 小规模使用与效果/负担评估 | keep 为建议 |

表内省略前缀均为 `ER-20261106-`。没有来源的方案、推演和练习以“研究设计/假设题”显著标注，不生成虚假的 evidence ID。

## 3. 本地输入：全文已读，不继承其外部引文可信度

### ER-20261106-input-01 — 第二阶段研究规格

- 来源/类型：用户提供的本地任务，私有研究任务规格（原文及文件定位不公开）。
- 版本/日期：本轮访问文件，无 Git 版本；读取日期 2026-11-06；774 行全文已读。文件创建/作者日期未核。
- 定位：研究范围与证据标准、七交付、七模型、三场景、十二问和验收；无外部公开 URL。
- 摘录：不摘录长段；本文件是需求依据，不是科学证据。
- 状态：read_status=read；claim_status=direct（任务要求）；experiment_status=not-run。
- 权利：用户输入，仅用于私有工作区处理，未发布。

### ER-20261106-base-01 — 工程思维

- 来源/类型：本地基线 `工程思维.md`；作者/外部原始出处未核；无可解析完整外部参考表。
- 读取日期/范围：2026-11-06，L1–240 全文；本地版本，无 SHA 冻结。
- 定位/支持：七层栈、系统/教育/验证视角；直接支持本研究对输入结构的描述，不证明训练效果。
- 摘录：无；原有 citation 标记不是本轮已核来源。
- 状态：read_status=read；claim_status=direct（输入文字）；experiment_status=not-run。
- 权利：用户提供研究材料，未修改、未公开，不推定第三方内容重用许可。

### ER-20261106-base-02 — 软件工程思维

- 来源/类型：本地基线 `软件工程思维.md`；外部出处未逐项核实。
- 读取日期/范围：2026-11-06，L1–320 全文；本地版本，无 SHA 冻结。
- 定位/支持：九机制、社会技术/演进；质量乘除表达只作比喻，不作测量。
- 摘录：无；不继承原有案例因果核验状态。
- 状态：read_status=read；claim_status=direct（输入文字）；experiment_status=not-run。
- 权利：同上，仅私有分析。

### ER-20261106-base-03 — 游戏工程

- 来源/类型：本地基线 `游戏工程.md`。
- 读取日期/范围：2026-11-06，L1–272 全文；本地版本，无 SHA 冻结。
- 定位/支持：五层游戏视角；70/30 比例无明确计量来源，AI 相互验证不等于独立 oracle。
- 摘录：无；外部数据/行业事实未全部复核。
- 状态：read_status=read；claim_status=direct（输入文字）；experiment_status=not-run。
- 权利：同上，仅私有分析。

### ER-20261106-base-04 — 工程-软件-游戏

- 来源/类型：本地基线 `工程-软件-游戏.md`。
- 读取日期/范围：2026-11-06，L1–606 全文；本地版本，无 SHA 冻结。
- 定位：L129–139 标准质量特性；L147–153 简化帧公式；L193–201 延迟；L533 本地引用可打开声明。
- 支持/限制：本地概念/表述审计；标准纠错须补原文，公式不能跨条件作为验收模型。
- 摘录：无。
- 状态：read_status=read；claim_status=direct（输入文字）；experiment_status=not-run。
- 权利：同上，仅私有分析。

## 4. 标准与方法候选：索引不等于已读条款

本节均由主线程检索；共同字段：访问日期 2026-11-06，read_scope=search excerpts，claim_status=unverified，experiment_status=not-run；无原文摘录，rights=not-verified，不复制标准全文。各条 read_status 另列，不能据索引推断强制适用性。

### ER-20261106-std-01 — ISO/IEC/IEEE 12207:2026

- 机构/标题/URL：[ISO/IEC/IEEE 12207:2026](https://www.iso.org/standard/90219.html)，ISO/IEC/IEEE。
- 版本/日期：索引指向第二版、2026-04，替代 2017；完整目录和条款未读。
- 定位/支持：恢复时核官方书目及生命周期过程正文；当前只允许“存在官方候选，不能凭熟悉 2017 版否定 2026”。
- read_status=access_failed；共同字段如上。

### ER-20261106-std-02 — SWEBOK V4 / V4.0a

- 机构/标题/URL：[IEEE Computer Society SWEBOK](https://www.computer.org/education/bodies-of-knowledge/software-engineering)；[v4 PDF 候选](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)。
- 版本/日期：索引指向 V4.0a 于 2025-09-25 公告及十八知识域，V4 与小修订关系待核。
- 定位/限制：未读指南正文；不能称读过十八知识域或把知识域清单当训练效果证据。
- read_status=access_failed；共同字段如上。

### ER-20261106-std-03 — ABET 2026–2027 Engineering Criteria

- 机构/URL：[ABET 当期工程认证准则](https://www.abet.org/accreditation/accreditation-criteria/criteria-for-accrediting-engineering-programs-2026-2027/)。
- 版本/定位：2026–2027；当期准则和同页拟议 2027–2028 修订需分开。具体条文未读。
- 支持/限制：认证目标属规范，不证明个人认知过程或本训练的因果效果。
- read_status=access_failed；共同字段如上。

### ER-20261106-std-04 — ISO/IEC 25010:2023

- 机构/URL：[ISO](https://www.iso.org/standard/78176.html)；[IEC 页面](https://webstore.iec.ch/en/publication/90024)。
- 版本/定位：2023 产品质量模型；索引列九特性、Interaction capability、Flexibility、Safety。
- 支持/限制：提示基线表可能混版；原文条款未读，不能把本研究重列的清单称标准原表。
- read_status=access_failed；共同字段如上。

### ER-20261106-std-05 — IEA GAPC

- 机构/URL：[IEA documents](https://www.internationalengineeringalliance.org/about/documents)；[2021.1 PDF 候选](https://www.ieagreements.org/assets/Uploads/IEA-Graduate-Attributes-and-Professional-Competencies-2021.1-Sept-2021.pdf)。
- 版本/日期：索引的 Version 4、2021.1 和发布日期标签待对读；不凭不同标签认定自相矛盾。
- 定位/限制：目录/文件首页/能力要求正文均待读取；规范不是培训实验。
- read_status=access_failed；共同字段如上。

### ER-20261106-std-06 — ISO/IEC/IEEE 15288:2023

- 机构/URL：[ISO 官方候选](https://www.iso.org/standard/81702.html)。
- 版本/日期：索引指向第二版、2023-05；未读系统生命周期条款。
- 定位/限制：用于后续基线标准版本核查，本版不据其证明七模型。
- read_status=discovered；共同字段如上。

### ER-20261106-method-01 — NASA Decision Analysis

- 机构/标题/URL：NASA，[*Systems Engineering Handbook*, §6.8 Decision Analysis](https://www.nasa.gov/reference/6-8-decision-analysis/)。
- 版本：候选 NASA/SP-2016-6105 Rev. 2；网页可能后续更新，未冻结。
- 定位/支持：检索指向标准、备选、不确定性、推荐与决策记录；未读正文，不能称 Tier 1–3/本研究停止规则来自 NASA 原标准。
- read_status=access_failed；共同字段如上。

### ER-20261106-method-02 — Documenting Architecture Decisions

- 作者/日期/URL：Michael Nygard，2011-11-15，[*Documenting Architecture Decisions*](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)。
- 版本/定位：网页未冻结；索引指向简短 context/status/decision/consequences，正文未读。
- 支持/限制：ADR 原作者实践文章候选，不是 ADR 提高质量的随机试验；本包扩展模板是研究者设计。
- read_status=discovered；共同字段如上。

### ER-20261106-unity-01 — Unity 2022.2 Profiling Applications

- 机构/URL：[Unity Manual 2022.2](https://docs.unity3d.com/2022.2/Documentation/Manual/profiler-profiling-applications.html)。
- 版本/范围：实际检索命中 2022.2，未核 6000.0；只读搜索片段。官方 Editor/目标设备测量区别为待核线索，不是本轮性能证据。
- 定位：target platform、Editor profiling 的相关正文待读；无本地 profile 数据。
- read_status=discovered；共同字段如上。

## 5. 基础设施候选：未完成四案的一手验收

本节共同字段：访问/检索 2026-11-06；read_scope=search excerpts；claim_status=unverified；experiment_status=not-run；原文摘录=无；rights=not-verified。没有源码冻结/编译/运行。页面中的历史目标不作为实际完成里程碑。

### ER-20261106-infra-01 — SQLite 测试与 TH3

- 机构/URL：SQLite 项目，[How SQLite Is Tested](https://www.sqlite.org/testing.html)、[TH3](https://www.sqlite.org/th3.html)。
- 版本/定位：浮动文档，未冻结；索引涉及故障/OOM/I/O/掉电与覆盖，正文未读。TH3 非完整公开体系；范围、覆盖定义、许可证和可复现部分待核。
- 允许/禁止：只能登记候选测试方法；不能称所有 SQLite/扩展均达到某覆盖标准，更不能“覆盖充分所以无 bug”。
- read_status=access_failed；共同字段如上。

### ER-20261106-infra-02 — SQLite WAL 与 checkpoint

- 机构/URL：[Write-Ahead Logging](https://sqlite.org/wal.html)；[wal_checkpoint_v2](https://www.sqlite.org/c3ref/wal_checkpoint_v2.html)。
- 版本/定位：浮动文档；索引提示并发、checkpoint、长读事务、同机共享内存/网络文件系统和 attached databases 限制。具体契约与 wal.c 未读，未固定 release。
- 允许/禁止：列必须核查的质量场景；不能声称已验证 WAL 在任何部署更快/安全。
- read_status=access_failed；共同字段如上。

### ER-20261106-infra-03 — Linux 6.6 Handling regressions

- 机构/URL：[Linux 6.6 process/handling-regressions](https://kernel.org/doc/html/v6.6/process/handling-regressions.html)。
- 版本/定位：v6.6 文档路径；回归责任、追踪/报告和修复线索仅来自索引。没有具体 regression/引入/修复链。
- 支持/限制：恢复时读相应版本，不能用 next 政策代替；本版只是待核流程案例。
- read_status=access_failed；共同字段如上。

### ER-20261106-infra-04 — Linux 6.6 Stable kernel rules

- 机构/URL：[Linux 6.6 stable-kernel-rules](https://docs.kernel.org/6.6/process/stable-kernel-rules.html)。
- 版本/定位：6.6；索引的 stable/backport 规则待正文核验；没有实际补丁接受/回归结果。
- 支持/限制：不能用流程文档证明某一局修/重构的效果。许可未读取，不转载。
- read_status=discovered；共同字段如上。

### ER-20261106-infra-05 — Kubernetes KEP 625 CSI Migration

- 机构/URL：[KEP 625](https://github.com/kubernetes/enhancements/blob/master/keps/sig-storage/625-csi-migration/README.md)；[2021 状态文章](https://kubernetes.io/blog/2021/12/10/storage-in-tree-to-csi-migration-status-update/)。
- 版本/定位：master **未冻结**；索引提示 API 转换、feature gates、upgrade/downgrade/upgrade 测试和观察；正文/实现/测试未读。
- 支持/限制：历史计划不等于实际里程碑；gate 关闭回退不保证后续版本仍可行。
- read_status=access_failed；共同字段如上。

### ER-20261106-infra-06 — Completing Cloud Provider Migration

- 机构/日期/URL：Kubernetes 官方，2024-05-20，[Completing Cloud Provider Migration](https://kubernetes.io/blog/2024/05/20/completing-cloud-provider-migration/)。
- 版本/定位：官方历史文章，未冻结正文；cloud-provider 迁移与 CSI 相关但不是同一变更。
- 支持/限制：仅索引线索；不能把该文日期当所有插件/功能退出旧路径的统一日期。
- read_status=access_failed；共同字段如上。

### ER-20261106-infra-07 — Kubernetes v1.31 Release

- 机构/日期/URL：Kubernetes 官方，2024-08-13，[v1.31 Release](https://kubernetes.io/blog/2024/08/13/kubernetes-v1-31-release/)。
- 版本/定位：1.31；发布说明候选，仅搜索片段，不证明已读每项 migration 实现/移除条件。
- 支持/限制：与 KEP 及当前实现需对读；不能把 roadmap 自动晋升为发布完成。
- read_status=discovered；共同字段如上。

## 6. 认知与学习候选登记

以下从认知子任务已交付记录迁入；12 项全部正文访问失败，状态保持不变，不作为已验证研究发现。

### ER-20261106-cog-01｜直觉有效的环境条件

- **来源**：Daniel Kahneman、Gary Klein（2009），*Conditions for Intuitive Expertise: A Failure to Disagree*。载体：*American Psychologist*；检索入口：PubMed、大学托管 PDF。
- **稳定链接**：[DOI 10.1037/a0016755](https://doi.org/10.1037/a0016755)；[PubMed](https://pubmed.ncbi.nlm.nih.gov/19739881/)；[尝试读取的 PDF](https://bear.warrington.ufl.edu/brenner/mar7588/Papers/kahneman-klein-2009.pdf)。访问日期：2026-11-06。
- **状态／范围**：`read_status=access_failed`；`read_scope=search excerpts`；`claim_status=unverified`；`experiment_status=not-run`。PDF 与 PubMed 页面均读取失败。
- **来源类型与原文定位**：候选理论综合／原作者观点对照，不应登记为新的随机实验。恢复位置为摘要及讨论环境有效性、学习机会、反馈与主观信心的正文；具体章节与页内定位未取得。检索书目信息给出期刊页码 515–526，不代表已读该页段。无已核验原文摘录。
- **拟支持的具体主张**：检索返回提示，可靠直觉与环境存在可学习的规律、获得学习机会有关；主观确信不自动保证准确。若正文核实，可用于提出“先审计任务环境与反馈，再谈直觉可靠性”，而不是“有经验者直觉总是好”。
- **不能支持**：成熟 Unity 工程师拥有跨业务、跨架构的通用直觉；快速回答优于审慎验证；本文已在软件工程中估计了直觉的效果。
- **反证／竞争解释**：优先寻找低有效性环境、错误或延迟反馈、领域内部专长不均的边界；同一人熟悉某类故障不能代表擅长长期架构收益预测。正文是否给出及如何限定这些例子均待核。
- **权利**：`rights=not-verified`；未取得版权／许可原文；只保留引用链接与原创中文候选主张。

### ER-20261106-cog-02｜专家问题表征，不是通用“看本质”能力

- **来源**：Michelene T. H. Chi、Paul J. Feltovich、Robert Glaser（1981），*Categorization and Representation of Physics Problems by Experts and Novices*。载体：*Cognitive Science*；候选正文由 Carnegie Mellon University 托管。
- **稳定链接**：[DOI 10.1207/s15516709cog0502_2](https://doi.org/10.1207/s15516709cog0502_2)；[尝试读取的 CMU PDF](https://www.cmu.edu/teaching/resources/Research/cognitive/Chi1981.pdf)。访问日期：2026-11-06。
- **状态／范围**：`read_status=access_failed`；`read_scope=search excerpts`；`claim_status=unverified`；`experiment_status=not-run`。
- **来源类型与原文定位**：候选原始物理问题分类／表征研究。恢复位置：摘要、各实验的方法与讨论；专家／新手的具体定义、任务操作与样本均未核验，不填数字。检索书目页码 121–152；无已读页内定位或原文摘录。
- **拟支持的具体主张**：索引提示，专家分类更依赖物理原理，新手更依赖表面特征。若核实，可提出“领域知识组织方式可能影响问题表征”；在工程训练中对照表面相似但机制不同、表面不同但机制相同的案例值得测试。
- **不能支持**：专家拥有与领域知识无关的本质洞察；物理实验已经证明软件架构训练有效；专家／新手组差异直接证明某一教学法造成差异。
- **反证／竞争解释**：领域知识量、被试选取、题目熟悉性和分类任务本身可能影响结果；组间比较不能直接确定能力形成的因果过程。工程师能背出“所有权”等标签，也不等于能预测实际故障。
- **权利**：`rights=not-verified`；未核对 Wiley／原出版版本的授权，不转载正文或图示。

### ER-20261106-cog-03｜刻意练习的原始论证

- **来源**：K. Anders Ericsson、Ralf Th. Krampe、Clemens Tesch-Römer（1993），*The Role of Deliberate Practice in the Acquisition of Expert Performance*。载体：*Psychological Review*；大学课程托管的原文 PDF 为候选入口。
- **稳定链接**：[DOI 10.1037/0033-295X.100.3.363](https://doi.org/10.1037/0033-295X.100.3.363)；[尝试读取的 Berkeley PDF](https://blogs.ischool.berkeley.edu/i225s14/files/2014/04/Ericsson-1993-article.pdf)。访问日期：2026-11-06。
- **状态／范围**：`read_status=access_failed`；`read_scope=search excerpts`；`claim_status=unverified`；`experiment_status=not-run`。
- **来源类型与原文定位**：候选理论论证加经验研究。恢复位置：刻意练习定义、与工作／游戏的区别、经验研究的方法及讨论；具体样本、回忆测量、设计与页内定位均未核验。检索书目页码 363–406；不提供原文摘录。
- **拟支持的具体主张**：检索返回将刻意练习描述为专为改进表现设计的努力活动，而不是所有重复劳动。若核实，可支持把“针对薄弱环节的任务、可检查的表现、反馈”与“累计写代码时长”区分开。
- **不能支持**：练满固定小时数必然成为专家；练习量解释全部差异；从回溯或组间关联直接推出训练因果；该定义已经在 Unity/C# 工程师上验证。
- **反证／竞争解释**：与 ER-20261106-cog-04、12 对读；需要检查练习定义是否一致、测量误差、选择效应及能力影响练习机会的反向路径。不把后续争议简单写成“原论文全错”。
- **权利**：`rights=not-verified`；公开课程副本不等于重用许可，未读取 APA 版权行。

### ER-20261106-cog-04｜刻意练习贡献的元分析争议

- **来源**：Brooke N. Macnamara、David Z. Hambrick、Frederick L. Oswald（2014），*Deliberate Practice and Performance in Music, Games, Sports, Education, and Professions: A Meta-Analysis*。载体：*Psychological Science*；Rice University 仓储为候选正文入口。
- **稳定链接**：[DOI 10.1177/0956797614535810](https://doi.org/10.1177/0956797614535810)；[PubMed 书目入口](https://pubmed.ncbi.nlm.nih.gov/24986855/)；[尝试读取的 Rice 仓储文件](https://repository.rice.edu/server/api/core/bitstreams/5c97be46-9886-4b8a-8010-91eb62914588/content)。访问日期：2026-11-06。
- **状态／范围**：`read_status=access_failed`；`read_scope=search excerpts`；`claim_status=unverified`；`experiment_status=not-run`。
- **来源类型与原文定位**：原创元分析／二次研究，不是新的训练随机试验。恢复位置：摘要、纳入标准、练习操作定义、异质性分析与讨论；研究数量、样本及效果量均未核验，因此不转录搜索结果中的百分比。
- **拟支持的具体主张**：索引提示，练习与表现的关系随领域而异，练习并非全部解释。若核实，可作为“不能把单一练习时长当完整能力模型”的反证来源。
- **不能支持**：“某百分比的个人能力由练习导致”；剩余方差等同天赋；职业领域汇总值就是软件工程效应；练习无用。相关性解释的方差不是个人能力的因果分解。
- **反证／竞争解释**：与 1993 年定义的符合程度、被纳入活动是否真正刻意练习、表现测量及范围限制都需阅读核对。不能只摘取最小领域数值，也不能把定义争议本身当作元分析已失效。
- **权利**：`rights=not-verified`；仓储版本是否为接受稿及其重用条款均未读取；不转载统计表。

### ER-20261106-cog-05｜真实软件相关候选：程序理解的心理表征

- **来源**：Nancy Pennington（1987），*Stimulus Structures and Mental Representations in Expert Comprehension of Computer Programs*。载体：*Cognitive Psychology*；Kent State University PDF 与 ScienceDirect 为候选入口。
- **稳定链接**：[DOI 10.1016/0010-0285(87)90007-7](https://doi.org/10.1016/0010-0285%2887%2990007-7)；[尝试读取的 Kent PDF](https://www.cs.kent.edu/~jmaletic/cs69995-PC/papers/pennington87.pdf)；[尝试读取的出版页](https://www.sciencedirect.com/science/article/pii/0010028587900077)。访问日期：2026-11-06。
- **状态／范围**：`read_status=access_failed`；`read_scope=search excerpts`；`claim_status=unverified`；`experiment_status=not-run`。
- **来源类型与原文定位**：候选原始程序理解研究。恢复位置：摘要、各研究方法、表征探测题及任务目标相关结果；检索书目页码 295–341。**方法与样本未从原文核验；不填人数、编程语言、经验年限或任务规模。** 无已核验原文摘录。
- **拟支持的具体主张**：索引提示，程序理解不应只用单一“功能目的”解释，控制关系、功能关系及阅读任务目标值得区分。若核实，可支持在评价中分别要求控制／状态解释和功能／目标解释，而不是用“能复述代码”代替理解。
- **不能支持**：所有程序员必然按固定阶段理解；1987 年的材料直接代表现代 Unity、C#、IDE 或大规模协作；纸面理解表现等于真实调试成功率。
- **反证／竞争解释**：任务需求、程序结构、熟悉性和探测方式可能塑造被测表征；这也可反驳“理解必然总是自顶向下”或“总是自底向上”的无条件说法，但须先读结果。
- **权利**：`rights=not-verified`；未读取 Elsevier 原版权行；不复制实验材料或图表。

### ER-20261106-cog-06｜真实软件工程候选：工作中的信息需求

- **来源**：A. J. Ko、Robert DeLine、Gina Venolia（2007），*Information Needs in Collocated Software Development Teams*。载体：ICSE；Microsoft Research 官方论文页及作者托管 PDF 是候选入口。使用作者缩写避免不同年代索引显示名不一致造成重复登记。
- **稳定链接**：[DOI 10.1109/ICSE.2007.45](https://doi.org/10.1109/ICSE.2007.45)；[MSR 论文页](https://www.microsoft.com/en-us/research/publication/information-needs-in-collocated-software-development-teams/)；[尝试读取的作者 PDF](https://faculty.washington.edu/ajko/papers/Ko2007InformationNeeds.pdf)；[尝试读取的 MSR PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2007/05/icse07_ko.pdf)。访问日期：2026-11-06。
- **状态／范围**：`read_status=access_failed`；`read_scope=search excerpts`；`claim_status=unverified`；`experiment_status=not-run`。两个 PDF 均失败；MSR 论文页只在搜索结果中出现，未成功打开。
- **来源类型与原文定位**：候选工作场所观察性软件开发研究，而不是教学干预。恢复位置：摘要、研究方法、需求分类、讨论／限制；具体章节名与表号未核验。**不转录搜索给出的人数、观察时长、问题类别数，也不填写未读的采样与编码方法。**
- **拟支持的具体主张**：检索返回提示，开发者存在对程序行为、设计理由、工件与同事知识的不同信息需求，一些问题会被延后。若核实，可支持把判断条件中的“信息可获得性、检索与协作成本”纳入模型，不能只归因个人脑力。
- **不能支持**：某种调试提问法已经提高正确率；观察到的信息需求直接说明专家胜过新手；同地团队结果无条件推广到远程、AI 辅助或 Unity 团队。
- **反证／竞争解释**：知识持有者不在、资料难找、组织分工等环境因素，可能解释看似“判断差”的表现；因此需区分“不会判断”与“缺少必要信息”。确切观察结论仍待原文复核。
- **权利**：`rights=not-verified`；作者公开 PDF 与机构发布不自动授予重用许可，未读取 IEEE 版权条款。

### ER-20261106-cog-07｜认知学徒制：原作者模型，不是工程培训效果试验

- **来源**：Allan Collins、John Seely Brown、Ann Holum（1991），*Cognitive Apprenticeship: Making Thinking Visible*。载体：*American Educator*；原刊机构 AFT 的网页是候选原文。
- **稳定链接**：[AFT 原刊网页](https://www.aft.org/ae/winter1991/collins_brown_holum)。DOI：未取得，不等于断言不存在。访问日期：2026-11-06。
- **状态／范围**：`read_status=access_failed`；`read_scope=search excerpts`；`claim_status=unverified`；`experiment_status=not-run`。
- **来源类型与原文定位**：原作者教学模型／说明文章候选；不标为原创随机试验。恢复位置：建模、指导、支架、表达、反思、探索等方法及迁移讨论；实际标题与段落定位未取得。搜索对卷期信息的呈现不稳定，故不填写未经核验的卷期页码。
- **拟支持的具体主张**：索引列出让思考可见、通过指导与逐步撤除支持学习的方法。若核实，可用来提出“导师展示提出假设、排除线索与改变判断的过程”，而不是只展示最终正确代码。
- **不能支持**：六种方法各自已在成熟工程师中证明有因果效果；旁观高手就会迁移；表达流利等于推理可靠。
- **反证／竞争解释**：学徒可能模仿导师说法而未掌握判断；若离开提示便失败，说明表现依赖支架。应把撤除提示后的新题作为检验，而不是拿模型文章本身当效果保证。
- **权利**：`rights=not-verified`；未取得 AFT 的具体授权，不复制文章段落。2020 年回顾文在搜索中出现，但未作为 1991 年原文替身使用。

### ER-20261106-cog-08｜提取学习与当下表现的分离

- **来源**：Henry L. Roediger III、Jeffrey D. Karpicke（2006），*Test-Enhanced Learning: Taking Memory Tests Improves Long-Term Retention*。载体：*Psychological Science*。
- **稳定链接**：[DOI 10.1111/j.1467-9280.2006.01693.x](https://doi.org/10.1111/j.1467-9280.2006.01693.x)；[尝试读取的出版全文页](https://journals.sagepub.com/doi/full/10.1111/j.1467-9280.2006.01693.x)；[PubMed 书目入口](https://pubmed.ncbi.nlm.nih.gov/16507066/)。访问日期：2026-11-06。
- **状态／范围**：`read_status=access_failed`；`read_scope=search excerpts`；`claim_status=unverified`；`experiment_status=not-run`。
- **来源类型与原文定位**：候选原始学习实验。恢复位置：各实验方法、即时与延迟测试、信心判断及讨论；分组、样本、材料、间隔数字均未核验。无原文摘录。
- **拟支持的具体主张**：索引提示，重学与测试的相对表现会随测试时间改变，学习者信心可能与延迟保持不一致。若核实，可支持把“当下做得顺”与“以后仍能独立提取”分开评价。
- **不能支持**：记忆实验等于复杂工程判断实验；背出模式名就能调试陌生系统；测试总在即时测验上占优；本研究已经识别了 Unity 工程师的最佳练习方案。
- **反证／竞争解释**：检索返回本身提示某些即时测试中重学有优势，这是对“测试任何时候都更好”的重要反例候选；保持效果也不自动等于跨任务迁移。
- **权利**：`rights=not-verified`；不复制实验材料或曲线；不把同年另一篇测试效应综述误当此实证文章。

### ER-20261106-cog-09｜间隔练习与保持窗口

- **来源**：Nicholas J. Cepeda、Harold Pashler、Edward Vul、John T. Wixted、Doug Rohrer（2006），*Distributed Practice in Verbal Recall Tasks: A Review and Quantitative Synthesis*。载体：*Psychological Bulletin*；作者 York University 页面为候选入口。
- **稳定链接**：[DOI 10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)；[尝试读取的作者页面](https://www.yorku.ca/ncepeda/publications/CPVWR2006.html)；[检索发现的作者实验室 PDF](https://www.evullab.org/pdf/CepedaPashlerVulWixtedRohrer-PB-2006.pdf)。访问日期：2026-11-06。
- **状态／范围**：`read_status=access_failed`；`read_scope=search excerpts`；`claim_status=unverified`；`experiment_status=not-run`。York 页面失败；实验室 PDF 仅发现、未尝试读取。
- **来源类型与原文定位**：元分析／二次研究；恢复位置：纳入任务、间隔与保持期的分析、讨论。纳入规模、效果量与具体最优间隔未核验，均不填写。
- **拟支持的具体主张**：检索返回提示，练习间隔的适宜性与希望保持多久有关。若核实，可支持“训练排期要与评价保持窗口一致”，而不是存在适用于所有技能的单一固定复习表。
- **不能支持**：口头记忆的结果已证明真实软件维护技能迁移；某套固定天数就是成熟工程师的最优排期；间隔本身保证正确的因果模型。
- **反证／竞争解释**：保持窗口、材料与任务改变可能改变相对优势；必须检查原文纳入边界，不能把所有形式的练习和所有间隔混为一类。
- **权利**：`rights=not-verified`；作者托管或仓储开放不等于确认版本与许可；不转载统计图表。

### ER-20261106-cog-10｜类比迁移需要检验，不是讲过就会

- **来源**：Mary L. Gick、Keith J. Holyoak（1983），*Schema Induction and Analogical Transfer*。载体：*Cognitive Psychology*；UCLA Reasoning Lab 原作者 PDF 为候选入口。
- **稳定链接**：[DOI 10.1016/0010-0285(83)90002-6](https://doi.org/10.1016/0010-0285%2883%2990002-6)；[尝试读取的 UCLA PDF](https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/Gick_Holyoak1983_SchemaInduction.pdf)。访问日期：2026-11-06。
- **状态／范围**：`read_status=access_failed`；`read_scope=search excerpts`；`claim_status=unverified`；`experiment_status=not-run`。
- **来源类型与原文定位**：候选原始类比问题解决实验。恢复位置：各实验中示例数量、比较／概括、提示操作与迁移结果；样本与任务细节未核验。检索书目页码 1–38；无原文摘录。
- **拟支持的具体主张**：检索返回提示，比较类比实例与图式形成、后续迁移有关。若核实，可支持设计成对工程案例，明确比较共享的因果关系，并单独测试无提示迁移。
- **不能支持**：讲一个架构故事就产生广泛迁移；实验中的图式质量关联足以证明它是唯一因果机制；训练了类比就自动获得通用判断力。
- **反证／竞争解释**：单个示例、显式原则和提示的作用可能取决于组合条件；应检查提示后表现是否被误写为自发迁移，以及关联变量是否受到共同任务因素影响。
- **权利**：`rights=not-verified`；不复制实验故事与示意图；原作者公开文件的重用条款未读取。

### ER-20261106-cog-11｜校准反馈及其迁移边界

- **来源**：Sarah Lichtenstein、Baruch Fischhoff（1980），*Training for Calibration*。载体：*Organizational Behavior and Human Performance*。
- **稳定链接**：[DOI 10.1016/0030-5073(80)90052-5](https://doi.org/10.1016/0030-5073%2880%2990052-5)；[尝试读取的出版页](https://www.sciencedirect.com/science/article/pii/0030507380900525)。访问日期：2026-11-06。
- **状态／范围**：`read_status=access_failed`；`read_scope=search excerpts`；`claim_status=unverified`；`experiment_status=not-run`。
- **来源类型与原文定位**：候选原始概率判断训练实验。恢复位置：摘要、训练／反馈设计、转移任务与讨论；不填写搜索给出的训练次数、题量或参与者比例。检索书目页码 149–171；无已核验摘录。
- **拟支持的具体主张**：检索返回提示，训练与反馈可能改善概率判断的校准，但向其他评估任务的迁移有限。若核实，可支持“具体任务上的预测—结果反馈值得训练，效果应在目标任务与迁移任务上分别评价”。
- **不能支持**：一张复盘表即可普遍消除过度自信；校准改善等同故障定位更准确；概率表达更保守就等于理解更深。
- **反证／竞争解释**：任务依赖与有限迁移本身是对“反馈带来通用校准”的候选反证；还须区分实际正确率、信心表达、校准与区分难易事件的能力。
- **权利**：`rights=not-verified`；未读取出版许可；不复制原任务、表格或训练材料。

### ER-20261106-cog-12｜对经典练习研究的复现与操作定义比较

- **来源**：Brooke N. Macnamara、Megha Maitra（2019），*The Role of Deliberate Practice in Expert Performance: Revisiting Ericsson, Krampe & Tesch-Römer (1993)*。载体：*Royal Society Open Science*；PMC 为候选公开正文入口。
- **稳定链接**：[DOI 10.1098/rsos.190327](https://doi.org/10.1098/rsos.190327)；[尝试读取的 PMC 文章](https://pmc.ncbi.nlm.nih.gov/articles/PMC6731745/)；[PubMed 书目入口](https://pubmed.ncbi.nlm.nih.gov/31598236/)。访问日期：2026-11-06。
- **状态／范围**：`read_status=access_failed`；`read_scope=search excerpts`；`claim_status=unverified`；`experiment_status=not-run`。
- **来源类型与原文定位**：候选原始复现研究。恢复位置：预定复现目标、盲法与练习定义、主要分析、局限；具体实施和数据未读取，不填样本数、效应或差异显著性。无原文摘录。
- **拟支持的具体主张**：索引将其描述为对 1993 年小提琴研究的复现，并提示未重现全部技能层级的累积练习差异。若核实，可用于要求能力模型面对复现、操作定义与反例，而不是把经典结果当免检前提。
- **不能支持**：完全推翻 1993 年全部论证；练习与表现无关；此音乐研究已给出软件工程训练的效应；“没有显著差异”即严格证明不存在任何差异。
- **反证／竞争解释**：复现材料、专家分组、练习定义与测量差异需逐一对照；原始研究和复现都不能仅因标题或立场被采信。与 ER-20261106-cog-04 共享作者，且 04 可能纳入 03，不得无差别计为多份独立确认。
- **权利**：`rights=not-verified`；虽然检索发现公开全文及数据集入口，但没有读取许可或数据；不因 PMC 或开放获取标签就代填具体 CC 版本。


## 7. AI 原始资料与工具案例

以下迁入 AI 子任务登记：仅 ai-02/03 已读正文；其余状态不得晋升。

### ER-20261106-ai-01 — METR 2025：熟悉真实仓库的 RCT

- **标题/作者/年**：*Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*；Joel Becker、Nate Rush、Elizabeth Barnes、David Rein；2025。作者信息由论文索引发现，未对读原文首页。
- **原始 URL**：[arXiv 2507.09089](https://arxiv.org/abs/2507.09089)；[METR 原始论文 PDF](https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf)。DOI：索引定位到 [10.48550/arXiv.2507.09089](https://doi.org/10.48550/arXiv.2507.09089)。
- **版本**：目标原始版本为 `2507.09089v1`；本轮请求其 HTML 失败。没有读取版本历史或核对后续修订；不把 METR 博客发布日期与 arXiv 上传日期混用。
- **方法/数字**：索引指向 16 名有经验的开源开发者、246 项真实任务、任务层面 AI 允许/禁止随机化；这些样本数字**未在 2025 原文中核实**。早期 +19%、区间 [+2%, +39%] 及 2025 年 2–6 月数据范围，已在 02 的官方跟进正文中读到，但不等于读过本论文。
- **实际读范围/定位**：仅检索结果；原文正文、附录、质量评估、排除规则、统计模型、任务熟悉度的精确定义均未读。待定位原文 Methods、Results、limitations；不伪造页码或摘录。
- **允许**：列为优先待读的熟悉真实仓库实验；早期时间结果暂以“2026 跟进回述”引用 02。
- **禁止**：声称已核对原论文的审核质量、任务计时、未完成任务处理；把小样本具体条件推广到所有职业开发者或 2026 最新工具。
- **独立性/利益相关**：METR 自己实施与报告的研究；与 02 是同一研究团队且部分参与者重叠，不算独立确认。资金、模型商合作与详细披露未读，不能写成无利益相关。
- **状态**：`read_status=access_failed`；`claim_status=unverified`；`experiment_status=not-run`；访问日期 2026-11-06。
- **版权**：原文许可页未核。仅登记书目和链接；无正文摘录、图表复用或再许可。

### ER-20261106-ai-02 — METR 2026 已公开跟进：设计与选择效应

- **标题/作者/年**：*We are Changing our Developer Productivity Experiment Design*；Joel Becker、Nate Rush、Tom Cunningham、David Rein、Khalid Mahamud；2026-02-24。页面正文及 BibTeX 均已读。
- **URL/DOI/版本**：[METR 官方文章](https://metr.org/blog/2026-02-24-uplift-update/)；网页文献，无已核 DOI。读的是 2026-11-06 当日取得的该日期页面，未取得网页快照 hash，不声称正文自发布后未变。
- **方法**：2025 年 8 月起的新实验，10 名原研究开发者加 47 名新招募者；仍让开发者预先提交任务，再随机分配 AI 允许/禁止，记录完成所用时间。文章末尾给出 **57 名开发者、143 个仓库、800+ 任务、经验中位数 10 年**。新仓库包括更小、更绿地、较不成熟项目，样本构成并非原样不变。
- **核验数字**：原参与者子集估计相对耗时 **−18%，区间 [−38%, +9%]**；新参与者 **−4%，[−15%, +9%]**；文章同时回述早期 **+19%，[+2%, +39%]**。新研究报酬由原研究 **$150/h 降为 $50/h**。调查中 **30%–50%** 的开发者称因不愿在禁 AI 条件下做某些任务而不提交它们。本文没有自行重算这些量。
- **关键限制，正文直接支持**：高预期受益者不愿参加；高预期受益任务被选择性漏报；禁 AI 任务更可能未完成，且有一人一个禁 AI 任务都未完成；同时开多个 agent 时难以归属时间；任务类型以及文档/测试等产物质量可能随条件变化。
- **判断限幅**：作者认为当前可能比早期更能提速，但也明确说数据对增加幅度只有很弱证据。作者对偏差方向及“可能低估”的判断不是数学上已识别的下界；不据此补算真实效应。区间跨零不能证明零效应，也不能证明普遍提速。
- **实际读范围/定位**：成功取得 HTML 全部文字；读了开头六段、`Wider adoption of AI has made it more difficult to measure task-level productivity`、`Selected developer quotes`、`Other means of measuring productivity`、`Details of the productivity study`。没有打开所链数据集、问卷、协议或重算结果；页尾推荐的其他研究只算线索。
- **短摘录**（少于 25 词）：（公开版省略第三方原句：未确认再分发许可；保留证据 ID、来源定位与中文分析）。定位：开头解释当前信号与早期差异的段落。
- **允许**：截至截止日确有公开 2026 跟进；公开了转向提速的中心估计，同时严重削弱其代表性与可解释性；需要修改实验设计。
- **禁止**：将它说成已完成可信的新一轮全面验证、撤回原研究、或当前 AI 普遍有确定提速。不能用开发者引语当实测十倍提速。
- **独立性/利益相关**：METR 官方研究团队报告自己的后续研究，与 01 部分样本及研究目标重叠；正文未完整核对资金来源，不能称独立第三方复现。
- **状态**：`read_status=read`；`claim_status=direct`，其中偏差大小与未来效应只能作为作者判断/推论；`experiment_status=not-run`；访问日期 2026-11-06。
- **版权**：页尾为 METR 版权所有。仅短引与中文事实概述，不转载全文、参与者引语集合、数据集或页面图表。

### ER-20261106-ai-03 — Peng 等：GitHub Copilot 受控编程题

- **标题/作者/年**：*The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*；Sida Peng、Eirini Kalliamvakou、Peter Cihon、Mert Demirer；2023。
- **URL/DOI/版本**：[原文 HTML v1](https://arxiv.org/html/2302.06590v1)；[书目页](https://arxiv.org/abs/2302.06590)；DOI [10.48550/arXiv.2302.06590](https://doi.org/10.48550/arXiv.2302.06590)。HTML 明示 **v1，2023-02-13**。只核此版本，不声称与后续版本逐字一致。
- **方法**：实验发生于 **2022-05-15 至 2022-06-20**，不是 2023 年工具的现场实验。Upwork 招募职业程序员；166 个邀请、95 个接受，随机 **45 人处理、50 人对照**。处理组获得 Copilot 及一分钟介绍；两组均可用互联网/Stack Overflow。统一任务为 JavaScript HTTP server。
- **测量边界**：GitHub Classroom 从个人仓库创建时间计到第一次提交通过 **12 项可见但不能修改的测试**。这是经过时间，不是精确的键盘操作时间、价值产出或端到端团队维护周期。标准化骨架项目不同于长期熟悉仓库的复杂维护。
- **核验数字**：正文报告两组各 35 人完成任务及问卷，时间结果明确**条件于完成任务**：处理组均值 **71.17 分钟**，对照 **160.89 分钟**；报告完成时间减少 **55.8%，95% CI [21%, 89%]，t 检验 p=0.0017**。四个超过 300 分钟的异常值都在对照组，作者称剔除后结论仍稳健，本轮未重算。
- **其他重要限制**：有 **5 名处理组参与者未完成 Copilot 注册**；任务成功率差正文称约 **+7 个百分点，95% CI [−0.11, 0.25]**，不显著。不能将完成者的时间差自动当作完整随机样本、所有任务成功与否都纳入的净效应。异质性 Table 1 中经验项 p=0.0629；“经验少者更受益”不是已确定的普遍规律。
- **实际读范围/定位**：成功取得 HTML 全部文字：Abstract、Introduction、Study Design、Results、Table 1、Discussion、参考文献及 Figures 1–8 图注。关键时间数字位于 Results 的 Figure 6 后段；质量限制在 Discussion。未读图片内文本、个体数据或补充仓库。
- **短摘录**（少于 25 词）：（公开版省略第三方原句：未确认再分发许可；保留证据 ID、来源定位与中文分析） 定位：Discussion 第一组限制段。
- **允许**：这个标准化任务、工具代际和完成者样本中有显著节时；这为 AI 可能提高某类任务表现提供实证。
- **禁止**：一般开发工作都省一半时间；成功率已经显著提高；证明安全性/维护性不变；少经验受益就等于技能学得更好；把 55.8% 较短耗时直接称作 55.8% 较高吞吐量。
- **独立性/利益相关**：原文列 Microsoft Research、GitHub、MIT 等机构；研究工具由相关企业提供，研究经 Microsoft Research Ethics Review Board 批准。它是产品相关作者参与的原始实验，不是独立于供应商的复现；不能因利益相关而自动否定，但需在引用时显露。
- **状态**：`read_status=read`；`claim_status=direct`，外推与因果机制另限幅；`experiment_status=not-run`；访问日期 2026-11-06。
- **版权**：HTML 明示 arXiv perpetual non-exclusive license，不等于开放再许可。只作短引和事实概述，不复刻图表/任务图片或论文全文。

### ER-20261106-ai-04 — SWE-bench：真实 issue 的测试型评估

- **标题/作者/年**：*SWE-bench: Can Language Models Resolve Real-World GitHub Issues?*；Carlos E. Jimenez 等；2023 预印本、ICLR 2024。完整作者顺序未对读原文，不补写未核名单。
- **URL/DOI/版本**：[arXiv 2310.06770](https://arxiv.org/abs/2310.06770)；[ICLR 原文](https://openreview.net/pdf?id=VTF8yNQM66)；[官方评估说明](https://www.swebench.com/SWE-bench/guides/evaluation/)；[官方 grading.py 候选入口](https://github.com/SWE-bench/SWE-bench/blob/main/swebench/harness/grading.py)。DOI 未核验。请求 v1 HTML 与官方评估页面失败；会议版、当前仓库均未读，源码未冻结。
- **方法/数字线索，未核**：原文索引指向 **2,294 项、12 个 Python 仓库**，从 issue 与对应 PR 建立任务；搜索结果指向论文 Table 9 的 `FAIL_TO_PASS`、`PASS_TO_PASS`、`test_patch` 定义。没有读取表格与实现，不能说已核验完整评分契约。原始 1.96% 等历史分数不作为当前能力证据。
- **实际读范围/定位**：仅发现论文/仓库与索引线索；正文、数据筛选、失败排除、隐藏测试、测试补丁处理、污染与许可证均未读。Table 9 和 `grading.py` 是恢复定位，不是本轮已核行号。
- **允许**：列为必须复核的“有限测试下 issue 修复”评估体系；提出核查测试是否既修复目标又保留原行为的问题。
- **禁止**：benchmark resolved 等于维护者接受、可长期维护、安全或自主完成整个软件工程流程；Python issue 成绩直接推广到 Unity/C#；把论文/仓库/榜单当三次独立确认。
- **独立性/利益相关**：benchmark 建设团队也参与 05 的 agent 研究，不能作为完全独立的双证据。具体资助与利益披露未读。
- **状态**：`read_status=access_failed`；`claim_status=unverified`；`experiment_status=not-run`；访问日期 2026-11-06。
- **版权**：论文、评估代码、任务仓库及 issue/PR 可能受不同许可约束；本轮未核 LICENSE，不转存数据/源码或复用图表。

### ER-20261106-ai-05 — SWE-agent 原始论文：ACI 的设计与实验

- **标题/作者/年**：*SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering*；John Yang、Carlos E. Jimenez、Alexander Wettig、Kilian Lieret、Shunyu Yao、Karthik Narasimhan、Ofir Press；NeurIPS 2024。名单来自书目检索，未对读首页。
- **URL/DOI/版本**：[arXiv 2405.15793](https://arxiv.org/abs/2405.15793)；[NeurIPS 原始发表 PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/5a7c947568c1b1328ccc5230172e1e7c-Paper-Conference.pdf)；DOI 索引定位到 [10.48550/arXiv.2405.15793](https://doi.org/10.48550/arXiv.2405.15793)。发现 arXiv v3 线索，但未读版本历史；不伪造论文与代码一一对应关系。
- **方法/数字线索，未核**：摘要索引描述 purpose-built ACI，服务仓库导航、文件编辑和程序/测试执行；索引报告过 **SWE-bench 12.5% pass@1、HumanEvalFix 87.7%**。这些只是待核的历史论文数字：模型版本、样本分母、预算、重试、是否完整集、表格与消融均未读，不能当本轮已核成功率。
- **实际读范围/定位**：原始 PDF 抓取失败；未读方法、ACI 命令规范、窗口与上下文策略、基线/消融、成本表、案例轨迹、附录和限制。不提供虚构章节号、页码、单任务账单或引语。
- **允许**：把 ACI 当成应研究的工程对象；据论文题目及摘要索引提出“工具/反馈设计可能影响任务表现”的待核假设。
- **禁止**：已证明某个具体窗口大小或 lint gate 是提升原因；性能提升完全由 harness 造成；上述历史分数是当前版本或本地复现结果；已核清每个实例成本。
- **独立性/利益相关**：系统作者自评，且与 04 的作者群重叠；论文、官网与仓库是同一项目家族，不是三个独立实证。资助与 API 支持披露待读。
- **状态**：`read_status=access_failed`；`claim_status=unverified`；`experiment_status=not-run`；访问日期 2026-11-06。
- **版权**：未核 PDF 许可和第三方模型条款；不复制图表、长段文字、轨迹或提示词。

### ER-20261106-ai-06 — SWE-agent 官方仓库/设计材料

- **来源/作者/年**：SWE-agent 项目维护者；公开仓库与项目背景文档；项目始于 2024，本轮检索截至 2026-11-06。
- **URL/DOI/版本**：[官方仓库](https://github.com/SWE-agent/SWE-agent)；[项目背景](https://swe-agent.com/latest/background/)；DOI 不适用。**发布/tag/SHA：未冻结。** 曾请求 `https://raw.githubusercontent.com/SWE-agent/SWE-agent/v0.7.0/run.py`，但抓取失败；这个候选 URL 不能证明 tag 存在，更不能证明其 commit。
- **代码入口线索，未核**：官方仓库的 issue 索引中可找到 `run.py`、`sweagent/agent/agents.py` 与 `Agent.run()` 的旧调用栈，如 [#309](https://github.com/SWE-agent/SWE-agent/issues/309)、[#312](https://github.com/SWE-agent/SWE-agent/issues/312)。它们只是历史入口候选，不是固定发布源码，也不是维护者确认的当前接口。环境实现文件、默认配置、命令定义、提交流程均未定位并逐行核查。
- **实际读范围/定位**：README、背景文档、源码、release/ref、LICENSE 均未成功打开；只读到搜索发现信息。不将错误调用栈推导成完整运行契约。
- **允许**：第 6 案例选择真实 SWE-agent 项目；将入口、环境、工具、测试、提交和资源清理列为恢复核查清单。
- **禁止**：写“已核验 v0.7.0/SHA”；宣称 main 与 2024 论文一致；把当前重写版本、旧版 Docker 环境和其他项目的工具实现混成一套已验证设计。
- **独立性/利益相关**：与 05 同源设计与实现材料；即便读到多个文件，也只能支持不同契约，不能凑成多份独立性能确认。
- **状态**：`read_status=access_failed`；`claim_status=unverified`；`experiment_status=not-run`；访问日期 2026-11-06。
- **版权**：仓库及其依赖的许可证未读；不凭印象标 MIT，不复制源码或将第三方材料重许可。

### ER-20261106-ai-07 — Perry 等：安全性与自信可能分离

- **标题/作者/年**：*Do Users Write More Insecure Code with AI Assistants?*；Neil Perry、Megha Srivastava、Deepak Kumar、Dan Boneh；CCS 2023；预印本始于 2022。
- **URL/DOI/版本**：[arXiv 2211.03622](https://arxiv.org/abs/2211.03622)；[作者页面候选](https://crypto.stanford.edu/~dabo/pubs/abstracts/ai-code.html)；[作者公开仓库](https://github.com/neilaperry/do-users-write-more-insecure-code-with-ai-assistants)；DOI 索引为 [10.1145/3576915.3623157](https://doi.org/10.1145/3576915.3623157)。会议版与预印本未对读，仓库未冻结。
- **方法/数字线索，未核**：索引描述 **47 名参与者、5 项安全相关任务、Python/JavaScript/C、codex-davinci-002**；其结论指向辅助组整体更不安全且更自信。但未读各任务判分、样本分组、显著性/多重比较、参与者经验和模型使用方式；不把“整体”解释成所有题都显著。
- **实际读范围/定位**：仅书目/索引；作者页抓取失败。正文、附录及数据未读，无可核验页码或原文摘录。
- **允许**：将其作为“正确性/安全性与主观自信需分别测量”的待核原始实验。
- **禁止**：所有 AI 辅助都会使代码不安全；该旧 Codex 结果直接等于当前 agent、完整真实仓库维护或长期退化；编造百分比作为实际漏洞增幅。
- **独立性/利益相关**：与 METR、SWE-agent 及 Copilot 实验不是同一实验；具体资助/行业合作披露未读，独立性不能只凭学术单位推定。
- **状态**：`read_status=access_failed`；`claim_status=unverified`；`experiment_status=not-run`；访问日期 2026-11-06。
- **版权**：未核 ACM/作者版及仓库许可；只提供书目链接与待核概述，无正文摘录或数据再分发。

### ER-20261106-ai-08 — Buçinca 等：非软件的过度依赖/认知强制

- **标题/作者/年**：*To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making*；Zana Buçinca、Maja Barbara Malaya、Krzysztof Z. Gajos；2021，PACM HCI / CSCW。
- **URL/DOI/版本**：[作者记录](https://www.eecs.harvard.edu/~kgajos/papers/2021/bucinca2021trust.shtml)；[作者版 PDF](https://www.eecs.harvard.edu/~kgajos/papers/2021/bucinca21trust.pdf)；[arXiv 2102.09692](https://arxiv.org/abs/2102.09692)；DOI 索引为 [10.1145/3449287](https://doi.org/10.1145/3449287)。正文/版本未核。
- **方法/数字线索，未核**：索引描述 **N=199**，比较认知强制、简单可解释 AI 和无 AI 条件；过度依赖可能下降，但满意度及整体团队表现不必同步改善。未读原任务细节、条件数量与统计，不能填入具体效应量。
- **实际读范围/定位**：仅索引；Harvard PDF 和作者记录均访问失败，无已核段落或摘录。
- **允许**：作为非软件的机制候选：让人先判断/主动调取帮助可能增加认知参与，但有时间、体验和人群差异成本；需要软件领域直接验证。
- **禁止**：**不能直接推出长期程序员技能退化或某种代码审查流程已有效**；不把降低错误建议采纳等同于提高整体生产率或长期能力。
- **独立性/利益相关**：独立于上述编程实验的研究团队与任务；具体资助/披露未读。跨领域独立不等于可直接迁移。
- **状态**：`read_status=access_failed`；`claim_status=unverified`；`experiment_status=not-run`；访问日期 2026-11-06。
- **版权**：作者版/ACM 许可未核；不复用图片、任务刺激、长摘录或实验材料。

### ER-20261106-ai-09 — Shen、Tamkin 2026：开发者学习新库

- **标题/作者/年**：*How AI Impacts Skill Formation*；Judy Hanwen Shen、Alex Tamkin；2026。相关官方文章 *How AI assistance impacts the formation of coding skills*，索引日期 2026-01-29。
- **URL/DOI/版本**：[arXiv 2601.20245](https://arxiv.org/abs/2601.20245)；[官方研究文章](https://www.anthropic.com/research/AI-assistance-coding-skills)。尝试 `2601.20245v1` HTML 失败；DOI 和修订历史未核，未对读网页与论文。
- **方法/数字线索，未核**：索引描述 **52 名以初级为主的软件工程师**学习 Python Trio，AI 条件在后测理解/调试等方面较差，平均速度提升不显著；网页索引的“17%”未核清是相对比例还是百分点，**不作为已核数字使用**。交互模式与学习结果的关联不能不经方法核查就升级为随机化机制效应。
- **实际读范围/定位**：只发现书目与网页索引；论文和官网正文均抓取失败。未读招募、随机化、排除、评分、统计、过程分类或延迟测验设计。
- **允许**：这是与职业技能学习直接相关、值得优先补读的近期原始研究；应分离“当下产出”和“离开辅助后的理解/调试”。
- **禁止**：已证明长期职业技能不可逆退化；所有 junior 必然学得更差；“问解释”与“完全委派”的差别已经由随机分组因果识别；将其变成 API 使用教程。
- **独立性/利益相关**：研究来自模型供应商 Anthropic；产品相关原始研究，不是独立于厂商的复现，也不能凭负面方向就忽略利益相关。
- **状态**：`read_status=access_failed`；`claim_status=unverified`；`experiment_status=not-run`；访问日期 2026-11-06。
- **版权**：网页与论文许可未读，未复用图表、测试题或长引文。

### ER-20261106-ai-10 — Sandoval 等：主动保留不同方向的安全结果

- **标题/作者/年**：*Lost at C: A User Study on the Security Implications of Large Language Model Code Assistants*；Gustavo Sandoval、Hammond Pearce、Teo Nys、Ramesh Karri、Siddharth Garg、Brendan Dolan-Gavitt；USENIX Security 2023。早期预印本标题为 *Security Implications of Large Language Model Code Assistants: A User Study*。
- **URL/DOI/版本**：[USENIX 官方发表页](https://www.usenix.org/conference/usenixsecurity23/presentation/sandoval)；[会议论文 PDF](https://www.usenix.org/system/files/usenixsecurity23-sandoval.pdf)；[arXiv 2208.09727](https://arxiv.org/abs/2208.09727)。会议版正文未读；DOI 未核，不把两个标题当两份独立实验。
- **方法/数字线索，未核**：索引描述 **58 名学生程序员**、C 语言链表购物清单任务、Codex 辅助与无辅助组；作者摘要对额外严重安全问题的评价较温和。索引中的关于不超过 10% 的说法（公开版省略英文原句，非新核验）没有读到分母、估计方式和区间，**不改写为安全等价界限或普遍漏洞率**。
- **实际读范围/定位**：索引发现；原始 PDF 抓取失败；具体缺陷分级、统计功效、组间差、任务限制和附录均待读。
- **允许**：保留作为对“安全影响一概负面”的竞争证据候选，补读后才能比较与 07 的任务、样本、工具与评分差异。
- **禁止**：没有显著差异就证明等价、无害或安全；学生单一 C 任务否定 Perry 的不同实验；将作者摘要中的上限语言解释为本轮重算的置信上界。
- **独立性/利益相关**：与 Perry 不是同一实验/同一作者组；具体资助与模型支持披露未读，不预先保证完全独立。
- **状态**：`read_status=access_failed`；`claim_status=unverified`；`experiment_status=not-run`；访问日期 2026-11-06。
- **版权**：会议/作者材料许可未核；不复用论文图、代码、参与者提交或数据集。

### ER-20261106-ai-11 — Kazemitabaar 等：青少年初学者学习，不等于职业开发

- **标题/作者/年**：*Studying the effect of AI Code Generators on Supporting Novice Learners in Introductory Programming*；Majeed Kazemitabaar、Justin Chow、Carl Ka To Ma、Barbara J. Ericson、David Weintrop、Tovi Grossman；CHI 2023。
- **URL/DOI/版本**：[arXiv 2302.07427](https://arxiv.org/abs/2302.07427)；[作者托管论文 PDF](https://terpconnect.umd.edu/~weintrop/papers/Kazemitabaar_et_al_CHI_2023.pdf)；DOI 索引为 [10.1145/3544548.3580919](https://doi.org/10.1145/3544548.3580919)。未对读会议版/预印本，未核修订历史。
- **方法/数字线索，未核**：索引描述 **69 名完成者、10–17 岁**，涉及 Python 代码编写、手动修改和一周后测；正文索引另出现 90 名开始者，流失与分析样本处理必须核查。索引报告编写表现改善、手动修改未下降、后测差异不显著，均未核表格与效应量。
- **实际读范围/定位**：仅索引；作者 PDF 抓取失败；完整设计、分配/流失、评分、练习与后测顺序、统计功效未读。不转引索引中的 1.15×/1.8× 等数作为正文核验。
- **允许**：主动保留可能有支持学习/表现收益的研究方向，反对只挑负面；它与 09 的人群、学习任务和评价时间尺度不同。
- **禁止**：学生做得更好就证明职业程序员学得更好；一周后无显著下降就证明没有长期损害；以当前未读线索宣布“AI 学习一定有益”。
- **独立性/利益相关**：与 09 不同作者和教育情境；具体资助/工具支持披露未读。学校样本与职业样本不能当直接相互复制。
- **状态**：`read_status=access_failed`；`claim_status=unverified`；`experiment_status=not-run`；访问日期 2026-11-06。
- **版权**：ACM/作者版许可未核；不复制教学任务、测验题、图片或参与者代码。

### ER-20261106-ai-12 — METR 2026 后续问卷线索：不是另一份 RCT

- **标题/作者/年**：*Measuring the Self-Reported Impact of Early-2026 AI on Technical Worker Productivity*；METR，具体作者名单待核；官方研究索引标示 2026-05-11。
- **URL/DOI/版本**：[METR 官方研究索引](https://metr.org/research/?page=2)。原文章正文未取到，DOI、作者与版本未核；不拿 02 的作者名单替代。
- **方法/数字线索**：02 已读页面的推荐区列出了本标题及 **349 名技术工作者、1.4–2× 自报工作价值变化**；搜索索引也指向该研究。只证明找到后续问卷线索，未核查问卷样本、题目、校正与数据，不能解释为客观实测产能。
- **实际读范围/定位**：02 页尾推荐卡片 + 搜索索引，不是本研究正文。因此按 `discovered` 而非 `read` 登记。
- **允许**：截至截止日检索还发现 2026 公开的问卷方向；优先确认正文、日期及是否有独立更新。
- **禁止**：用自报倍数填补 02 的选择偏差，或把它说成精确确认提速的第二轮 RCT；“没有找到更多 RCT”等于证明不存在。
- **独立性/利益相关**：仍为 METR 团队方向，非外部独立复现；具体作者、样本重叠与披露未知。
- **状态**：`read_status=discovered`；`claim_status=unverified`；`experiment_status=not-run`；发现日期 2026-11-06。
- **版权**：只登记书目与短卡片中的事实线索；未复制问卷、报告或图表，许可待核。

## 8. Unity/C# 固定源码与历史材料

以下迁入 Unity 子任务登记：25 项已读指定范围、1 项文档站访问失败；所有测试未运行。U/N 和来源内短编号的对应关系见共同字段。

### 共同字段与权利约定

- 所有项访问日期：**2026-11-06**；所有项 **`experiment_status=not-run`**，并在各条显式重复。没有实验数据、通过率、benchmark 或用户访谈。
- `U`：UniTask 2.5.10／`7c0f199fe0d3fc528024488ccd671e6c7b27745b`，快照提交日 2024-10-03。`N`：NGO 1.9.1／`7d27c5141123e3b9f31419ccca7768a640a45d56`，快照提交日 2024-04-18。各源码项的“日期”是这一快照日期，**不是宣称文件最后修改日或功能引入日**。
- `MIT-U`：Copyright (c) 2019 Yoshifumi Kawai / Cysharp, Inc.，见 02。`MIT-N`：Copyright (c) 2021 Unity Technologies，见 14。若日后复制实质源码，应附相应版权及 MIT 许可全文；本笔记只作少量短引与中文分析，没有把第三方源码重许可。
- GitHub REST 元数据公开可读，不把这件事等同额外再分发授权。Issue／PR 正文及评论不自动继承源码 MIT：作者保留文本权利，本研究仅短引、链接、不复制图片、不访问 PR 中的非公开 Jira。
- 每条仅有一个很短的“摘录”字段，同一原始来源的摘录合计不超过 25 个英文词；函数标识与行号用于定位，不以大段代码替代分析。文件行号来自实际读取内容，网页可能因显示方式不同需按函数名复核。
- `read_status=read` 表示下面列出的范围已实际读过，不表示通读仓库；源码通过固定 raw URL 或官方 REST contents 的 base64 正文读取，Issue／PR 通过官方 REST 读取 title／body 等字段。**没有把仅搜索到的候选当正文证据**。

### UniTask 来源

#### ER-20261106-game-01 — Cysharp／UniTask：tag、commit、manifest 版本锚

- 类型／机构：官方仓库 GitHub REST 元数据＋package manifest／Cysharp。
- URL 与标题：[git ref tags/2.5.10](https://api.github.com/repos/Cysharp/UniTask/git/ref/tags/2.5.10)；[release commit](https://github.com/Cysharp/UniTask/commit/7c0f199fe0d3fc528024488ccd671e6c7b27745b)（读取接口：[git/commits](https://api.github.com/repos/Cysharp/UniTask/git/commits/7c0f199fe0d3fc528024488ccd671e6c7b27745b)）；[package.json](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/src/UniTask/Assets/Plugins/UniTask/package.json)。
- 日期／版本／定位：提交 2024-10-03T00:42:37Z；U；ref.object、commit.sha/date/message、manifest version/unity/license。
- 摘录：`"version": "2.5.10"`。
- 读取范围：ref JSON；commit 的 SHA、作者／提交者日期、message 字段；manifest 全文。支持版本锚，不支持编译兼容性。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：API 元数据公开；manifest MIT-U。

#### ER-20261106-game-02 — UniTask：LICENSE

- URL／标题：[LICENSE](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/LICENSE)。机构：Cysharp。
- 日期／版本／定位：2024-10-03 快照；U；版权、许可条件与免责声明。
- 摘录：`Copyright (c) 2019 Yoshifumi Kawai / Cysharp, Inc.`
- 读取范围：许可全文；确认软件和随附文档的 MIT 条款，不推定覆盖独立 Issue 评论。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U，保留版权及许可要求。

#### ER-20261106-game-03 — UniTask：README 官方取消／PlayerLoop／池化契约

- URL／标题：[README.md](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/README.md)。机构：Cysharp。
- 日期／版本：2024-10-03 快照；U。
- 定位／重点读取范围：L143–159 基础／最低 Unity；L201–209 单次消费约束；L327–350 suppress 与即时取消成本；L478–602 PlayerLoop；L981–1004 测试和 Editor 限制；L1053–1066 Pooling Configuration。另读关键词相邻上下文，未通读 1159 行全文。
- 摘录：`heavier than checking CancellationToken on the player loop.`
- 支持：作者公开契约与理由；限制：README 中性能措辞不是本研究 benchmark。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U。

#### ER-20261106-game-04 — UniTask：UniTask.Delay.cs

- URL／标题：[Runtime/UniTask.Delay.cs](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/src/UniTask/Assets/Plugins/UniTask/Runtime/UniTask.Delay.cs)。机构：Cysharp。
- 日期／版本：2024-10-03 快照；U。
- 定位：L147–196 Delay 重载／类型分派；L698–828 `DelayPromise`，尤其 Create L722–755、GetResult L757–774、MoveNext L791–815、TryReturn L817–827。
- 摘录：`if (!(cancelImmediately && cancellationToken.IsCancellationRequested))`。
- 读取范围：L1–197、L691–890；其中上述 DelayPromise 全类已读。没有把 IgnoreTimeScale／Realtime 作为本案已完整分析的路径。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U。

#### ER-20261106-game-05 — UniTask：UniTask.cs 消费与取消包装

- URL／标题：[Runtime/UniTask.cs](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/src/UniTask/Assets/Plugins/UniTask/Runtime/UniTask.cs)。机构：Cysharp。
- 日期／版本：2024-10-03 快照；U。
- 定位／重点读取范围：L68–74 非泛型 suppress；L169–208 `IsCanceledSource`；L290–363 非泛型 Awaiter；L468–535 泛型 suppress／source；L625–708 泛型 Awaiter，另读检索上下文。
- 摘录：`if (source.GetStatus(token) == UniTaskStatus.Canceled)`。
- 支持：取消分支绕过底层 GetResult、普通 awaiter 的消费分派；不直接证明运行时对象持续存活。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U。

#### ER-20261106-game-06 — UniTask：PlayerLoopHelper.AddAction

- URL／标题：[Runtime/PlayerLoopHelper.cs](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/src/UniTask/Assets/Plugins/UniTask/Runtime/PlayerLoopHelper.cs#L492-L505)。机构：Cysharp。
- 日期／版本／定位：2024-10-03 快照；U；L492–505 AddAction／无 timing 异常。
- 摘录：`runner.AddAction(action);`
- 读取范围：L485–516；未通读所有 PlayerLoop 注入逻辑。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U。

#### ER-20261106-game-07 — UniTask：PlayerLoopRunner

- URL／标题：[Runtime/Internal/PlayerLoopRunner.cs](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/src/UniTask/Assets/Plugins/UniTask/Runtime/Internal/PlayerLoopRunner.cs)。机构：Cysharp。
- 日期／版本／定位：2024-10-03 快照；U；AddAction L29–49、RunCore L157–257。
- 摘录：`if (!action.MoveNext())`。
- 读取范围：全文 260 行；核对 running 时等待队列、false／异常时去引用、压缩与队尾补入。未由此声称所有跨线程复用安全。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U。

#### ER-20261106-game-08 — UniTask：completion core

- URL／标题：[Runtime/UniTaskCompletionSource.cs](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/src/UniTask/Assets/Plugins/UniTask/Runtime/UniTaskCompletionSource.cs)。机构：Cysharp。
- 日期／版本：2024-10-03 快照；U。
- 定位／重点读取范围：`UniTaskCompletionSourceCore<TResult>.Reset` L85–99；TrySetCanceled L176–192；Version／GetStatus／GetResult L194–251；OnCompleted 前半 L259–291；另读接口／相邻上下文与自动重置源 L385–440，未通读 944 行全文。
- 摘录：`continuation(continuationState);`
- 支持：完成时可直接调用 continuation、GetResult 抛取消、Reset 增代；不支持任意高层调用自动切回主线程。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U。

#### ER-20261106-game-09 — UniTask：TaskPool

- URL／标题：[Runtime/TaskPool.cs](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/src/UniTask/Assets/Plugins/UniTask/Runtime/TaskPool.cs)。机构：Cysharp。
- 日期／版本／定位：2024-10-03 快照；U；SetMaxPoolSize／GetCacheSizeInfo；TryPop L80–100、TryPush L103–121。
- 摘录：`if (size < TaskPool.MaxPoolSize)`。
- 读取范围：全文 123 行；支持回池可能失败、缓存大小不是唯一生命周期 oracle。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U。

#### ER-20261106-game-10 — UniTask：AsyncTest 取消测试

- URL／标题：[Assets/Tests/AsyncTest.cs](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/src/UniTask/Assets/Tests/AsyncTest.cs#L303-L335)。机构：Cysharp。
- 日期／版本／定位：2024-10-03 快照；U；ExceptionlessCancellation L303–316、ExceptionCancellation L318–335。
- 摘录：`canceled.Should().Be(true);`
- 读取范围：两个完整测试及 Cancel／Pool／Suppress 关键词命中的邻近上下文；不是整个测试套件。测试对象为 DelayFrame，断言功能结果／帧差，不检查本案 DelayPromise 回池。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U。

#### ER-20261106-game-11 — UniTask：DelayTest

- URL／标题：[Assets/Tests/DelayTest.cs](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/src/UniTask/Assets/Tests/DelayTest.cs)。机构：Cysharp。
- 日期／版本／定位：2024-10-03 快照；U；DelayFrame L22–39、DelayFrameZero L42–56、DelayRealtime L194–207。
- 摘录：`Time.frameCount.Should().Be(frameCount + 1);`
- 读取范围：全文 220 行；只把断言作为已写测试意图，不声称帧数或时间区间实际通过。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U。

#### ER-20261106-game-12 — UniTask Issue #661

- URL／标题：[DelayPromise Leaks when use SuppressCancellationThrow](https://github.com/Cysharp/UniTask/issues/661)；读取接口：[issue](https://api.github.com/repos/Cysharp/UniTask/issues/661)、[comments](https://api.github.com/repos/Cysharp/UniTask/issues/661/comments?per_page=100)。机构：Cysharp 官方仓库内公开用户报告，不是维护者设计声明。
- 日期／版本：2025-05-14T14:29:10Z 创建；2025-12-11T00:27:37Z 关闭／更新；报告未给精确包版本。2025-11-11 唯一已读评论来自 stale bot。
- 定位／摘录：正文 Problem；（公开版省略第三方原句：未确认再分发许可；保留证据 ID、来源定位与中文分析）
- 读取范围：REST title／body／日期／状态／closed_by／state_reason 与全部一条评论；未追踪全部事件历史。证实报告存在及机器人关闭，不证实运行 leak 或修复。
- 状态：`read_status=read`；`claim_status=direct`（报告／关闭记录），`unverified`（运行泄漏／修复）；`experiment_status=not-run`。许可：公开 Issue 作者文本，未推定 MIT，仅短引链接。

### Netcode for GameObjects 来源

#### ER-20261106-game-13 — Unity／NGO：tag、commit、manifest 版本锚

- URL／标题：[git ref ngo/1.9.1](https://api.github.com/repos/Unity-Technologies/com.unity.netcode.gameobjects/git/ref/tags/ngo/1.9.1)；[release commit](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/commit/7d27c5141123e3b9f31419ccca7768a640a45d56)（读取接口：[git/commits](https://api.github.com/repos/Unity-Technologies/com.unity.netcode.gameobjects/git/commits/7d27c5141123e3b9f31419ccca7768a640a45d56)）；[package.json](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/com.unity.netcode.gameobjects/package.json)。机构：Unity Technologies 官方仓库。
- 日期／版本／定位：提交 2024-04-18T16:34:14Z；N；ref.object、commit.sha/date/message、manifest version/unity/dependencies。
- 摘录：`"version": "1.9.1"`。
- 读取范围：ref JSON；commit 上述字段；manifest 全文；另读 tag 列表仅用于发现，不采用当前 tag 排序作版本依据。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：API 公开元数据；manifest MIT-N。

#### ER-20261106-game-14 — NGO：根目录与包内 LICENSE

- URL／标题：[根目录 LICENSE.md](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/LICENSE.md)；[包内 LICENSE.md](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/com.unity.netcode.gameobjects/LICENSE.md)。机构：Unity Technologies。
- 日期／版本／定位：2024-04-18 快照；N；版权、MIT 条款及免责声明。
- 摘录：`Copyright (c) 2021 Unity Technologies`。
- 读取范围：两份全文，文字同为 MIT；根目录许可用于核对 testproject 示例的仓库许可背景，不把示例冒充 package runtime。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-N；复制实质代码须保留声明与全文。

#### ER-20261106-game-15 — NGO：NetworkObject 公共入口

- URL／标题：[Runtime/Core/NetworkObject.cs](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/com.unity.netcode.gameobjects/Runtime/Core/NetworkObject.cs)。机构：Unity Technologies。
- 日期／版本：2024-04-18 快照；N。
- 定位／重点读取范围：SpawnInternal L761–782；Spawn／SpawnWithOwnership／Despawn L856–893；InvokeBehaviourNetworkDespawn L1387–1395；AddSceneObject L1857–1897，另读检索命中的相邻上下文与便利入口文档；未通读 2077 行全文。
- 摘录：`public void Despawn(bool destroy = true)`。
- 支持：真实默认值、server 权限、已有实例 Spawn、远端生成与生命周期通知。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-N。

#### ER-20261106-game-16 — NGO：NetworkSpawnManager

- URL／标题：[Runtime/Spawning/NetworkSpawnManager.cs](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/com.unity.netcode.gameobjects/Runtime/Spawning/NetworkSpawnManager.cs)。机构：Unity Technologies。
- 日期／版本：2024-04-18 快照；N。
- 定位：InstantiateAndSpawnNoParameterChecks L395–414；GetNetworkObjectToSpawn L420–484；CreateLocalNetworkObject 动态分支 L493–508；SpawnNetworkObjectLocallyCommon L648 起；SendSpawnCallForObject L756–770；DespawnObject L789–802；shutdown／场景释放 L840–929；OnDespawnObject L958–1075。
- 摘录：`DestroyGameObject = networkObject.IsSceneObject != false ? destroyGameObject : true`。
- 读取范围：以上核心分支、L614–732 的本地登记调用及检索上下文；L350–414、L740–774、L1038–1053 为证据缺口定点补读。未宣称通读整个 1135 行文件；已核读本案关键完整 OnDespawnObject。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-N。

#### ER-20261106-game-17 — NGO：NetworkPrefabHandler 与接口 XML 官方说明

- URL／标题：[Runtime/Spawning/NetworkPrefabHandler.cs](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/com.unity.netcode.gameobjects/Runtime/Spawning/NetworkPrefabHandler.cs)。机构：Unity Technologies。
- 日期／版本／定位：2024-04-18 快照；N；接口 Instantiate／Destroy XML L11–44；AddHandler L74–105；host hash 注册 L114–158；HandleNetworkPrefabSpawn L255–272、HandleNetworkPrefabDestroy L278–295。
- 摘录：`default destroy parameter (i.e. false)`。
- 读取范围：全文 425 行；摘录是本案指出的版本内文档冲突，不能作为公共默认值的正确契约。后备 source-hash handler 查找与物理释放委派有实际代码支持。
- 状态：`read_status=read`；`claim_status=direct`（实现／说明存在），`contradiction`（默认值文字）；`experiment_status=not-run`。许可：MIT-N。

#### ER-20261106-game-18 — NGO：CreateObjectMessage

- URL／标题：[Runtime/Messaging/Messages/CreateObjectMessage.cs](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/com.unity.netcode.gameobjects/Runtime/Messaging/Messages/CreateObjectMessage.cs)。机构：Unity Technologies。
- 日期／版本／定位：2024-04-18 快照；N；Deserialize L16–33、Handle L35–47、CreateObject L50–61。
- 摘录：`NetworkObject.AddSceneObject(sceneObject, networkVariableData, networkManager)`。
- 读取范围：全文 63 行；注意 prefab 未就绪／同步中的延迟处理，不把全部接收情况都化约为即时生成。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-N。

#### ER-20261106-game-19 — NGO：DestroyObjectMessage

- URL／标题：[Runtime/Messaging/Messages/DestroyObjectMessage.cs](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/com.unity.netcode.gameobjects/Runtime/Messaging/Messages/DestroyObjectMessage.cs)。机构：Unity Technologies。
- 日期／版本／定位：2024-04-18 快照；N；Deserialize L16–33；Handle L35–46。
- 摘录：`OnDespawnObject(networkObject, DestroyGameObject)`。
- 读取范围：全文 48 行；支持本地 flag 传播和未生成目标的 defer 分支，不是网络可靠性实验。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-N。

#### ER-20261106-game-20 — NGO 官方仓库：pool 示例

- URL／标题：[testproject/Assets/Samples/PrefabPool/NetworkPrefabHandlerObjectPool.cs](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/testproject/Assets/Samples/PrefabPool/NetworkPrefabHandlerObjectPool.cs)。机构：Unity Technologies；类型：官方仓库样例，**不是 package runtime 内建池**。
- 日期／版本／定位：2024-04-18 快照；N；OnNetworkSpawn L22–49；GetNextSpawnObject L57–68；Instantiate L70–77；Destroy L87–93；SpawnObjects L95–127。
- 摘录：`Host and Server spawn the objects`。
- 读取范围：全文 128 行；未打开其 Unity scene／prefab 配置，未验证运行，也未认为它实现了完整生产池协议。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-N（根目录许可见 14）。

#### ER-20261106-game-21 — NGO 官方样例：GenericPooledObjectBehaviour

- URL／标题：[testproject/Assets/Samples/PrefabPool/GenericPooledObjectBehaviour.cs](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/testproject/Assets/Samples/PrefabPool/GenericPooledObjectBehaviour.cs)。机构：Unity Technologies；类型：样例 companion。
- 日期／版本／定位：2024-04-18 快照；N；OnNetworkDespawn L35–57；OnNetworkSpawn L62–80；Update L133–165。
- 摘录：`NetworkObject.Despawn(HasHandler);`
- 读取范围：全文 186 行；只采用 HasHandler 条件分派与 false 时自行停用的源码事实，不推定实际场景中该字段赋值，也不把 0.12 秒可见性延迟当通用修复。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-N。

#### ER-20261106-game-22 — NGO：NetworkPrefabHandlerTests

- URL／标题：[Tests/Runtime/NetworkPrefabHandlerTests.cs](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/com.unity.netcode.gameobjects/Tests/Runtime/NetworkPrefabHandlerTests.cs)。机构：Unity Technologies。
- 日期／版本／定位：2024-04-18 快照；N；NetworkPrefabHandlerClass L88–174；测试 handler L206–239。
- 摘录：`Assert.False(networkPrefaInstanceHandler.StillHasInstances());`
- 读取范围：全文 240 行；其 handler 用 Unity Destroy，且直接调用内部 dispatch；不是“网络池借还跨端恰好一次”测试。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-N。

#### ER-20261106-game-23 — NGO：NetworkObjectOnNetworkDespawnTests

- URL／标题：[Tests/Runtime/NetworkObject/NetworkObjectOnNetworkDespawnTests.cs](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/com.unity.netcode.gameobjects/Tests/Runtime/NetworkObject/NetworkObjectOnNetworkDespawnTests.cs)。机构：Unity Technologies。
- 日期／版本／定位：2024-04-18 快照；N；Host／Server fixture L13–15；TestNetworkObjectDespawnOnShutdown L76–111，尤其 L102–110。
- 摘录：`() => OnNetworkDespawnTestComponent.OnClientNetworkDespawnCalled`。
- 读取范围：全文 113 行；第 109 行是本案 oracle 审核发现，不声称已运行测试或证明产品漏回调。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-N。

#### ER-20261106-game-24 — NGO Issue #990：历史 server handler 缺失

- URL／标题：[INetworkPrefabInstanceHandler not called on server](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/990)；读取接口：[issue](https://api.github.com/repos/Unity-Technologies/com.unity.netcode.gameobjects/issues/990)、[comments](https://api.github.com/repos/Unity-Technologies/com.unity.netcode.gameobjects/issues/990/comments?per_page=100)。机构：Unity 官方仓库；报告者 LukeStampfli，关联回复 NoelStephensUnity（REST 标为 MEMBER）。
- 日期／版本：创建 2021-07-28T11:22:16Z；关闭 2021-07-30T10:18:59Z；metadata 更新 2024-10-31；作者报告 MLAPI develop，**不是冻结 NGO 1.9.1 的实验**。
- 定位／摘录：[报告者关闭回复](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/990#issuecomment-889794522)；（公开版省略第三方原句：未确认再分发许可；保留证据 ID、来源定位与中文分析）。
- 读取范围：body／日期／状态与全部两条评论；正文中的截图未读。只把旧故障、hash 映射问题描述及关联修复记录作为历史证据。
- 状态：`read_status=read`；`claim_status=direct`（历史报告／回复），`unverified`（独立重现／修复实验）；`experiment_status=not-run`。许可：公开讨论作者文本，未推定 MIT，仅短引链接。

#### ER-20261106-game-25 — NGO PR #977：接口、host、XML 的公开设计说明

- URL／标题：[refactor!: NetworkPrefabHandler and INetworkPrefabInstanceHandler API & XmlDoc changes](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/pull/977)；读取接口：[pulls/977](https://api.github.com/repos/Unity-Technologies/com.unity.netcode.gameobjects/pulls/977)。机构：Unity Technologies 官方仓库。
- 日期／版本：2021-07-23T20:09:43Z 创建；2021-07-29T19:06:43Z merged。REST 实际返回 merge commit `d6b2a4864a79742c28afaaab02e46791dcb73270`，此处仅是历史元数据，不把它替代本案 N 快照。
- 定位／摘录：PR description 的接口命名理由；（公开版省略第三方原句：未确认再分发许可；保留证据 ID、来源定位与中文分析）
- 读取范围：title／body／created、updated、merged、merge_commit_sha、state 字段；未读全部 diff／review／提交链，不访问正文链接的 Jira。直接支持作者写过的目标，不证明完整方案比较或收益。
- 状态：`read_status=read`；`claim_status=direct`（设计文字）；`experiment_status=not-run`。许可：公开 PR 作者文本，未推定 MIT，仅短引链接。

### 访问失败，未用于证明正文

#### ER-20261106-game-26 — Unity Object-pooling 文档 URL（未读取正文）

- URL：[docs-multiplayer.unity3d.com/netcode/1.9.1/advanced-topics/object-pooling/](https://docs-multiplayer.unity3d.com/netcode/1.9.1/advanced-topics/object-pooling/)。机构：拟读取 Unity 官方文档站；类型：失败访问记录。
- 标题／日期／版本：仅按 URL 记为 object-pooling；页内标题、发布日期及实际正文版本均**未核验**。访问 2026-11-06；URL 带 1.9.1 不等于正文已冻结。
- 摘录：无。读取范围：无正文；WebFetch 返回无法验证域名安全。未换客户端重试或通过镜像取同页。
- 影响：不引用此页面内容；本案官方说明来自成功读取的固定源码 XML、官方仓库样例及公开 PR 描述。没有因访问失败降低其它已取得源码的 read_status，也没有假填文档证据。
- 状态：`read_status=access_failed`；`claim_status=unverified`；`experiment_status=not-run`。许可：正文未取得，未主张其转载授权。

## 公开导出附注：第三方短引的 MIT 许可

以下许可仅适用于本文件中已登记 MIT 的 UniTask / NGO 源码与随附文档短引，不适用于 Issue、PR、论文或网页。许可身份沿用原研究记录，本次未联网重新核验。

Copyright (c) 2019 Yoshifumi Kawai / Cysharp, Inc.

Copyright (c) 2021 Unity Technologies

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
