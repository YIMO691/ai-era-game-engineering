---
title: 精益制造、产品开发与软件开发——证据受限的独立文献核查
created_at: 2026-11-11
version: "0.2.1"
topic_id: 20261111-code-aesthetics-batch01
status: evidence-reviewed-with-explicit-gaps
tags: [engineering-research, lean, quality, batch01]
---

# 精益思想迁移：核查记录与工程判断边界

> [!WARNING]
> 公开研究草案：Batch01-B仍为PARTIAL，人工研究审核pending，代码／参与者实验未执行。公开提交授权不等于研究通过。
> 本文件是历史记录，其中已读／通过／归档声明不代表当前独立核验。
> 文内“未发布”、本地文件名、行号和检查点属于原研究时点；本页已作公开目录与链接适配，不是字节保真档案。当前阅读顺序与发布边界见[课题入口](../README.md)。


> [!NOTE] v0.1 分支记录与 v0.2 补读状态
> 本文件开头记录的是 v0.1 当时的访问受限状态。Batch01-A 已合法读取 The Lean Gap 作者机构 PDF、Toyota TPS、Deming Institute PDSA 和 ASQ TQM 官方页面。当前状态以本文件末尾的补读记录和 [sources](../evidence/sources.md) 为准；Poppendieck 原书全文及部分近年综述仍未直接读取。
>
> 本文是给主线程合并的独立证据记录，不代替课题唯一登记表 `sources.md`，本轮未改其他文件。2013 年综述只描述其覆盖时期，不能当作 2026 年领域现状。

## 1. 问题、范围与停止条件

- **问题**：TPS、持续改进与精益产品开发中的哪些机制可以作为软件质量投入的设计假设？哪些不能凭概念对应就宣称有效？
- **类型**：exploratory / applied；不是验证精益必然有效，也不是写线性管理史。
- **竞争解释**：收益可能来自反馈加快、工作批次减少、团队经验或工具改善，而非“精益”标签本身；压缩人力也可能短期改善表观产出而损害质量。
- **支持条件**：在任务风险、质量标准和工作构成可比时，端到端交付、返工、缺陷及人员负荷联合改善；有可检验机制和边界。
- **推翻／弱化条件**：局部提速但测试队列增长；缺陷外溢；为减少 WIP 而牺牲必要探索；改进成本超过收益；无法区分精益与同期其他改造。
- **范围**：2003 年书籍、2013 年指定综述、官方／专业机构定义、2013 年后综述线索；软件一般工程语境。不是 Unity/C# 特定版本运行验证。
- **停止条件**：约 15 次定点检索／抓取，明确核心数字能确认到哪一级、有哪些缺口，并给出可证伪机制框架。正文受阻后不以搜索替代全文。
- **本地检查**：已读研究契约和已有 `plan.md`；目标目录原先只有计划文件，未发现 `topic.json`。`git -C "LOCAL_RESEARCH_WORKSPACE" status --short` 返回退出码 128，目录不是 Git 仓库。

## 2. 首要纠错与可允许措辞

### 2.1 Pernstål 等（2013）的四个数字

来源 **ER-20261111-CA-L01** 的出版商／机构检索索引同时给出 10,230、38、76%、42%，因此**不是本轮发现的明显误引，但尚未完成正文级核验**。

| 主张 | 本轮可支持到哪里 | 不应写成 |
|---|---|---|
| 数据库检索识别 10,230 篇／条 | 搜索结果将其表述为数据库检索得到的 papers；可暂记“10,230 个初始检索候选（是否去重未核验）” | 10,230 个独立实验、10,230 个企业，或已确认去重后样本 |
| 38 relevant papers | 筛选后相关文献数量，索引级支持 | 38 个相互独立的实证研究／项目；同项目多篇是否合并未知 |
| 76% non-empirical | 是作者对纳入文献的分类比例，不是干预失败率 | 76% 证明无效、76% 无科学价值，或 76% 的所有精益研究都非实证 |
| 42% clearly addressed large-scale development | 分母为这批相关文献；强调“明确涉及”大型开发 | 42% 成功率，或其余 58% 都是小团队；可能存在规模报告不足 |

**尚未核验的关键定义**：作者怎样操作化 empirical / non-empirical；大型是否按人数、团队数、代码规模、系统复杂性、组织边界或复合判据定义；未报告规模如何分类；检索截止时间、数据库名单、去重、质量评价和编码一致性。本轮不能补造统一的“大型＝多少人”阈值。

若以 38 为共同分母，29/38≈76%、16/38≈42% 只是数学上相容，**不是从原表核出的原始频数**，不应在主报告中当成已核事实。“非实证”“大型”也不是互斥类别，不能把百分比相加或推定交叉分布。

**建议用句**：

> Pernstål、Feldt 与 Gorschek（2013）的检索索引报告，数据库搜索识别了 10,230 个候选，最终纳入 38 篇相关文献，其中 76% 被分类为非实证，42% 明确涉及大型开发。本轮未取得正文，分类定义与筛选细节尚待复核；这些数字不能代表 2026 年研究现状。

### 2.2 2003 年著作不是效果元分析

**ER-20261111-CA-L02**：作者为 **Mary Poppendieck 和 Tom Poppendieck**，题名 *Lean Software Development: An Agile Toolkit*，Addison-Wesley Professional，2003 年，第一版。出版商索引给出出版日 2003-05-08、ISBN-13 9780321150783、240 页；没有核到 DOI，不填造 DOI。

- 出版商索引描述它把七项精益原则转用于软件，包含 22 项 thinking tools。这是实践／概念框架，不是证明跨领域平均效果的试验。
- 本轮定点搜索可定位第 2 章 **Amplify Learning**（书目索引 p.15）和第 6 章 **Build Integrity In**（p.125）。这些是定位线索，未核正文页。
- 搜索结果对第 2 章预览的总结明确区分“创造配方”与“照配方生产”，并提醒不能直接移植制造实践。因没有打开预览，本文不把这段比喻作为逐字原文引用。
- 不将后续版本的原则措辞混作 2003 年原章名。若主报告要列七项原则，需补读该版目录；当前已核到索引的两个章名不足以完成七项逐字版本校验。

### 2.3 官方概念不能充当因果效果证据

- **TPS**：丰田官方检索结果把 **jidoka（自働化）与 Just-in-Time（准时化）**列为两大支柱。Jidoka 指异常检测、停止与阻止缺陷流向后续过程，不等于“自动化越多越好”；JIT 关心在需要时按需要数量生产／供给，不等于机械“零库存”或让所有人满负荷。上述属 **L03 的索引级概念释义**，不是正文引用。
- **Kaizen（持续改进）**：本轮将其暂作人员参与、反复发现问题并修改过程的机制概念；未取得官方 kaizen 独立正文，不能补写其首创年代或某固定步骤为丰田唯一规范。
- **PDSA 与 PDCA**：Deming Institute 搜索结果强调 **Study，而不是 Check**；其 FAQ 索引说 Deming 没有接受／使用 PDCA。允许归属为“研究所的说明”，不可写成“Deming 发明 PDCA，后来升级成 PDSA”。Study 的关键是把预测与观察比较、学习并修正理论，不只是验收是否完成；本轮未读其原始通信或历史 PDF，不能宣称完成历史原件考证（L04）。
- **TQM**：ASQ 索引强调客户导向、所有成员参与、持续改进与组织文化。TQM 不是仅增加末端检验，也不等同于 TPS、JIT 或一个看板工具（L05）。

### 2.4 质量与生产力不是单向历史升级

不要写“先追求生产力，再升级到质量，再升级到精益／软件美学”。本轮来源不足以支持这种历史线性因果叙事，概念也在不同层级：TPS 是生产系统，TQM 是组织管理取向，PDSA 是学习循环，JIT/jidoka 是机制，而精益产品／软件开发是领域适配框架。

**综合推论（非历史实证）**：减少返工可能同时改善质量和有效产出；适当停止生产可能增加眼前等待但避免缺陷扩散；预防与学习也消耗资源且未必每次收益为正。应把二者视为受机制、时间尺度和边界条件影响的联合目标，而非固定的先后阶段。依据为 L03、L04、L05 的概念线索，强度不得升级为效果证明。

## 3. 重复制造、产品开发、软件开发的区别

来源线索：L02、L06、L09。下表是用于研究设计的**综合分析**，不是从已读原文复制的分类表。

| 维度 | 相对稳定的重复制造 | 产品／软件开发中的额外问题 | 迁移警戒 |
|---|---|---|---|
| 工作对象 | 按既定设计重复形成合格产品 | 同时发现需求、知识和设计；有时连合格标准也需学习 | 不能把所有试验、备选设计、迭代都当成废品 |
| 变异 | 部分变异应抑制，维持过程一致性 | 受控探索可能创造信息；也有应消除的失误变异 | 不把“消除变异”套到所有创造活动 |
| 库存／在制品 | 可见的零件、成品、工序队列 | 未验证决策、未集成代码、待审查变更和反馈欠账 | 用 WIP 约束降低拥塞，不主张知识储备或备选方案越少越好 |
| 质量反馈 | 可重复测量的规格与过程信号 | 测试覆盖有限，质量与真实使用、架构和演进关联 | 不能用通过现有测试替代产品价值与长期质量 |
| 计划与承诺 | 相对稳定节拍与需求拉动 | 不确定性、依赖、不可逆决策与学习时机 | 延迟承诺必须有信息获取计划和最晚负责时点，不能成为拖延 |
| 标准化 | 有助于稳定重复执行 | 更适合稳定接口、验证过程和可复用知识 | 不能把所有解决问题路径固化成统一动作 |

**核查意义**：L06 的 2011 年综述索引已经警告，直接把精益制造原则翻译为产品开发不一定有效；L09 提供 2011—2022 年产品开发综述线索，说明不能把精益产品开发误讲成重复装配的别名。两者本轮均未读全文，具体实践组合、样本与效果仍未知。

## 4. 转移机制、必要条件、失败模式、可测指标

> [!NOTE] 以下均为待验证的工程设计提案
> 对应关系不是因果证明；指标是建议收集的变量，不是本轮测得的结果。所有 `experiment_status: not-run`。须区分实施成本、价值结果与人员负荷，不以代码行、工单数或个人利用率单独代表生产力。

| 概念及来源线索 | 可迁移机制假设 | 必要条件 | 典型失败模式／反证信号 | 可测指标与平衡项 |
|---|---|---|---|---|
| Jidoka（L03） | 异常能被发现，阻止缺陷进入后续阶段；软件可用构建失败、契约检查、发布闸门触发响应 | 检查信号可靠；有人负责处置；有停止权限；定位与修复能力 | 测试盲区、误报疲劳；“红灯”常态化；停线后只责备个人；全靠门禁导致等待 | 发现至止损时间、逃逸缺陷率、返工小时、误报率、恢复时长；同时看检查成本与队列 |
| JIT / pull（L03） | 依据下游处理能力限制启动、缩小批次，减少等待与反馈延迟 | 工作单元可切分；依赖可见；下游容量和需求信号可信；缓冲策略明确 | 只裁缓冲、不解决波动；拆成无意义小票；开发快而审查积压；高风险任务被指标排挤 | 端到端 lead time 分位数、WIP、阻塞时间、吞吐和批次；同时看故障及需求满足 |
| Kaizen（L03，正文缺口） | 一线问题被记录，提出小规模变化并验证后保留／撤销 | 有改进时间、反馈、参与权和问题安全表达；有基线 | “持续改进”变持续加码；只统计建议数量；没有复测；局部优化损害整体 | 同类故障复发、实验完成及撤销比例、返工与认知负担；不以改善活动次数替代效果 |
| PDSA（L04） | 提出可证伪预测，小范围实施，研究偏差并修正认知，再决定行动 | 事前预测、可观察结果、重复循环、明确停止规则 | 事后讲故事；只做一次前后对比；把 Study 降为勾选验收 | 预测误差、按预设标准学习／改判的比例、结果稳定性；同时记录环境变化和负结果 |
| TQM（L05） | 把客户质量目标和跨职能责任纳入全流程，减少部门转嫁 | 共同质量定义、管理支持、数据质量、员工参与 | 质量部独占责任；文件／认证代替实际质量；指标激励造成隐瞒 | 用户故障／投诉、全生命周期质量成本、跨部门等待、人员负荷；区分预防／鉴定／内外失败成本，此成本分类本轮未另行核原典 |
| Lean Product Development（L06、L09） | 以知识生成、备选方案与整合学习降低错误承诺及晚期返工 | 不确定性明确；试验可比较；整合点及收敛规则存在 | 为去“浪费”取消探索；无限保留方案不做决定；把研究当稳定生产计件 | 决策前消除的关键不确定性、晚期设计变更、知识复用、试验成本、上市／交付时长 |
| Lean Software Development（L02、L01） | 围绕价值与学习控制未完成工作、强化集成质量和全局反馈 | 技术可验证、需求可反馈、跨职能协作及组织激励一致 | “精益”被简化成裁人、赶工或少文档；局部速度上升但维护风险外溢 | 从需求至可用结果的周期、变更失败率、缺陷修复成本、理解／变更时间、真实使用价值 |

最小检验建议：选择一个瓶颈而非整套标签同时上线；预先定义工作项边界和完成条件；保留基线与任务难度；记录改进与观测成本；同时监测质量、周期、价值及负荷；若可行使用分阶段／对照设计，并报告任务构成变化、人员变更与同期工具更新。简单前后比较仅能提供关联线索。

## 5. 来源登记（供主线程原样合并或去重）

**共同字段**：访问／检索日均为 2026-11-11；`experiment_status: not-run`。权利均为原作者／出版商／机构所有，未核开放许可，不推定可全文转载。`read_status: access_failed` 表示尝试正文失败但仍有索引线索；`discovered` 表示只发现索引未请求正文。以下“短摘录”若仅为标题／章名，会明确标识；**没有伪造正文引文**。搜索工具返回总结不保证逐字忠实，不能再加引号冒充原文。

### ER-20261111-CA-L01 — 指定 2013 年综述

- **Source**：Joakim Pernstål, Robert Feldt, Tony Gorschek. *The lean gap: A review of lean approaches to large-scale software systems development*. 2013. *Journal of Systems and Software*, 86(11), 2797–2821. DOI：[10.1016/j.jss.2013.06.035](https://doi.org/10.1016/j.jss.2013.06.035)。
- **机构／链接**：[Chalmers 书目](https://research.chalmers.se/publication/186358)；[Elsevier 记录](https://www.sciencedirect.com/science/article/pii/S0164121213001477)。
- **Source type / 状态**：论文的书目／摘要索引；`read_status: access_failed`；`claim_status: unverified`（有索引支持，未完成原文复核）。
- **实际阅读范围**：搜索工具针对以上记录的元数据与结果总结；未直接打开摘要页，未读正文。
- **定位／短摘录**：题名短语 “The lean gap”；数字定位仅能给出出版社摘要索引，无法给正文页码或表号。
- **Method / sample / findings**：索引报告数据库候选 10,230、纳入相关文献 38、非实证 76%、明确涉及大型开发 42%；研究设计、背景、限制报告不足；跨部门互动的证据有限。数据库／截止日期／筛选协议均未知。
- **Supports**：历史时点文献基础有限，需要谨慎跨领域迁移。
- **Contradicts / 不支持**：不支持“2013 已充分证明普适收益”；也不支持“2026 仍然只有这些文献”或“精益无效”。
- **Limitation / strength**：只能摘要索引级暂存，不能重建分类定义或效应量。
- **失败线索**：[175352.pdf](https://publications.lib.chalmers.se/records/fulltext/175352/175352.pdf) 抓取被安全检查阻止；搜索只把它列为潜在线索，**未确认此 PDF 就是该论文**，不可冒称它是作者稿。
- **Project relevance**：限制“制造方法可直接证明代码品质投资有效”的论断。

### ER-20261111-CA-L02 — Poppendieck 2003 原版书籍

- **Source**：Mary Poppendieck; Tom Poppendieck. *Lean Software Development: An Agile Toolkit*. 2003. Addison-Wesley Professional，第一版，ISBN 9780321150783；无已核 DOI。
- **URL**：[InformIT 出版商记录](https://www.informit.com/store/lean-software-development-an-agile-toolkit-9780321150783)；[O’Reilly 第 2 章预览线索](https://www.oreilly.com/library/view/lean-software-development/0321150783/ch02.html)。
- **状态／类型**：书籍出版商及目录索引；`read_status: access_failed`；`claim_status: unverified`。
- **实际范围**：出版商搜索元数据、七原则／22 工具简介及第 2 章搜索总结；未读全书或预览正文。
- **定位／短摘录**：目录章名 “Amplify Learning”（第 2 章，p.15 索引线索）、“Build Integrity In”（第 6 章，p.125 索引线索）。
- **Method / sample / findings**：实践工具与概念迁移著作；本轮没有获取系统抽样或因果评估方法。样本量不适用／未核，不写成 22 个实验。
- **Supports**：软件开发需要学习和质量内建；产品开发与重复生产应区分。
- **Contradicts**：不支持制造实践原样复制或“精益软件＝少做质量工作”。
- **Limitation / relevance / strength**：可作思想来源与版本线索，不能独立证明收益；七原则完整原版措辞尚待目录核验。

### ER-20261111-CA-L03 — 丰田官方 TPS

- **Source**：Toyota Motor Corporation. *Toyota Production System*. 无已核发布日期（n.d.），官网动态版本。
- **URL**：[Vision & Philosophy](https://global.toyota/en/company/vision-and-philosophy/production-system/)；同机构解释入口：[Plant Tour](https://global.toyota/en/company/plant-tours/production-system/)。两个入口同源，不算独立确认。
- **状态／类型**：官方机构概念说明的搜索索引；`read_status: access_failed`；`claim_status: unverified`。
- **实际范围／定位**：搜索结果对两支柱的总结；术语短摘录 “jidoka” / “Just-in-Time”，非段落原文。未直接阅读正文。
- **Method / sample / findings**：机构自述，无本轮已核实验样本；索引说明异常时停止、防止缺陷传递、必要时按必要数量生产，并指向拉动与看板。
- **Supports**：区分 TPS、JIT、jidoka；异常停止不等于简单自动化。
- **Contradicts**：不支持把看板或满负荷单独等同于 TPS。
- **Limitation / relevance / strength**：官方定义即使取得正文也只能直接支持其制度自述，不能证明软件绩效；Kaizen 的原文位置与精确措辞仍缺。

### ER-20261111-CA-L04 — Deming Institute 的 PDSA 说明

- **Source**：The W. Edwards Deming Institute. *PDSA Cycle*. n.d.；机构网页，不是 Deming 亲笔原件。
- **URL**：[PDSA](https://deming.org/explore/pdsa/)；[FAQ](https://deming.org/about-us/f-a-qs/)。
- **状态／类型**：官方机构说明索引；`read_status: access_failed`；`claim_status: unverified`。
- **实际范围／定位**：PDSA 网页与 FAQ 的搜索总结；仅已见术语 “Study” / “Check”，不冒充逐字完整句。
- **Method / sample / findings**：方法论解释，无效果样本；索引强调预测与实际结果比较、学习和修正理论，并区分 PDCA。
- **Supports**：PDSA 不应简化为完成度检查；应谨慎归属 PDCA。
- **Contradicts**：反对无保留写“Deming 使用／发明 PDCA”；注意这是研究所索引说法，不是本轮历史原件核验。
- **Limitation / relevance / strength**：理论说明不是随机试验；本轮不能给其历史信件原文引文。找到 Ron Moen 的历史 PDF 线索但未读，不独立登记为已核史料。

### ER-20261111-CA-L05 — ASQ 的 TQM 定义

- **Source**：American Society for Quality (ASQ). *Total Quality Management (TQM): What is TQM?* n.d.，专业机构网页。
- **URL**：[ASQ TQM](https://asq.org/quality-resources/total-quality-management)。
- **状态／实际范围**：`read_status: discovered`；`claim_status: unverified`；仅搜索结果定义总结，无正文访问。
- **定位／短摘录**：页面标题 “Total Quality Management (TQM)”；无正文短引文。
- **Method / sample / findings**：专业定义；无效果样本；索引概括客户导向、所有成员参与、持续改进、数据与沟通及组织文化。
- **Supports / Contradicts**：支持全组织质量取向；不支持把 TQM 缩为末端检验或一种软件工具。
- **Limitation / relevance / strength**：定义线索不构成绩效或历史演化证据；可帮助避免概念混同。

### ER-20261111-CA-L06 — 精益产品开发综述（2011）

- **Source**：Martínez León 与 Farris（搜索返回的作者形式；完整姓名本轮未核）. *Lean Product Development Research: Current State and Future Directions*. 2011. DOI：[10.1080/10429247.2011.11431885](https://doi.org/10.1080/10429247.2011.11431885)。刊物／卷期页码未在本轮返回中确认，不补填。
- **状态／类型**：综述发现记录；`read_status: discovered`；`claim_status: unverified`。
- **实际范围／定位**：一次搜索返回的综述摘要总结；标题为可定位短摘录，未读全文。
- **Method / sample / findings**：索引称覆盖 21 年研究、归纳七个知识领域；文章总数、检索截止和纳排标准未知。索引强调直接转译制造原则未必构成有效产品开发过程。
- **Supports / Contradicts**：支持领域适配需额外条件；反对把开发当重复制造。
- **Limitation / relevance / strength**：方法与效果未复核；仅作为边界线索，不据此宣布何种 LPD 方法已获因果验证。

### ER-20261111-CA-L07 — 2015 年度量综述

- **Source**：Eetu Kupiainen; Mika V. Mäntylä; Juha Itkonen. *Using metrics in Agile and Lean Software Development—A systematic literature review of industrial studies*. 2015. *Information and Software Technology*, 62, 143–163. DOI：[10.1016/j.infsof.2015.02.005](https://doi.org/10.1016/j.infsof.2015.02.005)。
- **URL**：[Aalto 书目记录](https://research.aalto.fi/en/publications/using-metrics-in-agile-and-lean-software-development-a-systematic/)。
- **状态／范围**：`read_status: discovered`；`claim_status: unverified`；只读搜索结果元数据及摘要总结。
- **定位／短摘录**：题名中的 “industrial studies”；无正文引文。
- **Method / sample / findings**：题名与索引指向工业研究的系统综述，考察 Agile/Lean 度量的使用原因和效果；纳入数及具体结果本轮未知。
- **Supports / Contradicts**：支持 2013 年后还有相关综述；不能把其敏捷与精益混合研究当成精益独立效果。
- **Limitation / relevance / strength**：不是 2013 年 large-scale lean 综述的同范围直接更新；仅用作补检和指标研究入口，不写“已弥合大型实证缺口”。

### ER-20261111-CA-L08 — 2022 年软件精益工具综述

- **Source**：Melanie Paz; Alonso Sasagawa; José Antonio Taquía Gutiérrez. *Systematic Literature Review of Lean Tools Applied to Software Development*. 2022. IEOM Society 会议论文；搜索入口指向 2022 Rome proceedings，正式会名、会议日期和页码本轮未核。DOI：[10.46254/EU05.20220448](https://doi.org/10.46254/EU05.20220448)。
- **URL**：[会议 PDF](https://ieomsociety.org/proceedings/2022rome/448.pdf)。
- **状态／范围**：`read_status: access_failed`；`claim_status: unverified`；仅搜索结果摘要总结，PDF 未取得。
- **定位／短摘录**：文章标题可定位；无法提供 PDF 页码与原文句子。
- **Method / sample / findings**：索引报告纳入 19 篇文章；等待是突出浪费、Kanban 最常应用、理解不足构成采用障碍。未核检索窗、数据库、质量评价、频数、效应量和大型项目比例。
- **Supports / Contradicts**：支持较晚研究存在及工具应用线索；不能据“最常用”推出“最有效”，不能用 19 与 38 作研究规模增长／下降比较，范围不同。
- **Limitation / relevance / strength**：会议综述且正文未读；不得认定其研究质量、效果方向或已解决早期缺口。

### ER-20261111-CA-L09 — 2023 年产品开发综述

- **Source**：Cukor Kirinić 与 Hegedić（搜索返回的作者形式；名字未核）. *Trends and Future Research Direction of Lean Product Development*. 2023. *Sustainability*, 15(24), article 16721（卷期与文章号来自返回 URL，待出版页复核）。
- **URL**：[出版商页面](https://www.mdpi.com/2071-1050/15/24/16721)。DOI 未在本轮结果中直接确认，不依据 URL 规律生成。
- **状态／范围**：`read_status: discovered`；`claim_status: unverified`；仅搜索结果摘要总结。
- **定位／短摘录**：题名 “Trends and Future Research Direction of Lean Product Development”；无正文引文。
- **Method / sample / findings**：索引称评述 2011—2022 年 85 篇论文，包括知识生成与可视化；纳排、质量评价和效果综合未核。
- **Supports / Contradicts**：支持产品开发领域存在较新的研究综合线索；不是软件大型开发现状的直接证据。
- **Limitation / relevance / strength**：不得用文献数量证明有效性，或冒充已读 85 项研究。

## 6. 主张晋升表

| Claim | Evidence | Allowed wording | Forbidden stronger wording | 不确定性／下一步／决定 |
|---|---|---|---|---|
| 2013 年综述报告四数字 | L01 | “索引报告……，分类定义待核” | “正文已核、2026 仍为 76%” | 补读方法与分类表；weaken |
| 软件开发不能机械照搬制造 | L02、L06、L09 | “来源线索提示需区分，作为迁移边界” | “任何制造方法都不适用于软件” | 读开发／生产差别与具体反例；keep 边界、weaken 效果 |
| TPS 两支柱与停止异常 | L03 | “官方搜索索引描述……” | “故 CI 必然提高生产力” | 取得官方正文，另找软件实证；weaken |
| PDSA 强调学习而非只检查 | L04 | “研究所索引强调 Study” | “Deming 发明 PDCA”“PDSA 比 PDCA 效果更好已证实” | 补正文及历史来源；revise |
| TQM 是组织层级质量取向 | L05 | “ASQ 索引定义……” | “质量史必然从产量演进至美学” | 补定义与独立历史研究；discard 线性叙事 |
| 2013 后研究仍在发展 | L07、L08、L09 | “找到 2015、2022、2023 综述线索” | “截至 2026 大型开发证据已充分／仍完全空白” | 更新检索并核同范围综述；keep 存在性、其余 unverified |
| 机制可改善软件质量／周期 | L02—L05、L06 及本轮推演 | “可检验的设计假设” | “对应关系证明因果收益” | 需要实证或项目实验；run experiment（本轮未运行） |

## 7. 真实检索式、抓取与失败记录

编号为本轮逻辑清单，平行调用的实际完成次序不代表顺序阅读。所有查询逐字列出；未把未执行的建议检索混入日志。

| # | 工具 | 真实查询／URL | 结果与影响 |
|---|---|---|---|
| 1 | WebSearch | `Pernstal Feldt Gorschek 2013 "lean gap" "10230"` | 无相关命中，返回无关网页；未采用，不据此判论文不存在 |
| 2 | WebFetch | `https://global.toyota/en/company/vision-and-philosophy/production-system/` | 安全验证失败；TPS 正文未读 |
| 3 | WebFetch | `https://deming.org/explore/pdsa/` | 同上；PDSA 原始说明正文未读 |
| 4 | WebSearch | `"The lean gap" Pernstål 2013` | 命中 Chalmers／ScienceDirect 书目、摘要索引和 PDF 线索 |
| 5 | WebSearch | `lean software development systematic literature review 2015 2024` | 命中 2015、2022 等较晚综述，满足后续检索要求；不等于全面更新至 2026 |
| 6 | WebSearch | `site.informit.com "Lean Software Development" "2003" Poppendieck` | 出版商元数据与样章线索 |
| 7 | WebSearch | `site.global.toyota "Toyota Production System" "jidoka" "Just-in-Time"` | 官方 TPS 与工厂导览索引 |
| 8 | WebSearch | `site.deming.org "PDSA" "PDCA" "Study"` | PDSA、FAQ 与历史说明 PDF 线索；PDF 未读 |
| 9 | WebFetch | `https://publications.lib.chalmers.se/records/fulltext/175352/175352.pdf` | 安全验证失败；无法确认文档身份、10,230 的去重口径及分类定义 |
| 10 | WebFetch | `https://www.informit.com/store/lean-software-development-an-agile-toolkit-9780321150783` | 安全验证失败；书籍正文与目录未直接阅读 |
| 11 | WebFetch | `https://ieomsociety.org/proceedings/2022rome/448.pdf` | 安全验证失败；2022 综述方法、19 篇与发现未作正文复核 |
| 12 | WebSearch | `lean product development manufacturing differences uncertainty knowledge creation Ward Sobek systematic review` | 命中 2011／2023 综述及知识工作线索；未取得 Ward–Sobek 原始出版物，不能归为已核原典 |
| 13 | WebSearch | `site.asq.org total quality management TQM customer focused all employees continual improvement` | 命中 ASQ TQM 定义索引 |
| 14 | WebSearch | `"The lean gap" "10,230" "large" "empirical"` | 命中指定四数字的摘要索引；仍未提供操作定义 |
| 15 | WebSearch | `"Lean Software Development" "2003" "Amplify Learning" "Build Integrity" "development" "manufacturing"` | 命中第 2／6 章名称、页码线索及生产／开发差异总结；未读章节正文 |

5 次 WebFetch 的共同错误文本：`Unable to verify if domain ... is safe to fetch. This may be due to network restrictions or enterprise security policies blocking claude.ai.` 这是**工具访问失败**，不等于网页不存在、404、付费墙或论文撤稿。未使用 curl 或其他路径绕过；已按协调提示把产物降为“证据受限范围研究”。

未采用 #1 的无关结果；#5 也发现 2023 卷期／2024 上线的技术债综述，但本轮未继续核验日期、方法，不把它写成已读证据或用来填补现状。后续可另查，但不增加本轮确认数量。

## 8. 下一步证据缺口与交接约束

1. **最高优先级**：由正常授权路径取得 L01 正文，核第一个检索数是否去重、最终 38 的单位，以及 empirical / large-scale 操作定义、截止时间、分类表和质量评价。未完成前不能将四数字写成“本轮全文核实”。
2. **原典核验**：L02 的 2003 年目录与第 2 章；丰田 TPS/Kaizen 正文；Deming Institute PDSA 与其引用的历史资料。不能用后来的七原则版本冒充原版。
3. **现状更新**：L07 与 L08 的范围都不是 L01 的严格同范围更新；需要大型、系统级、跨部门精益软件研究的较新综述和实证。已执行后续检索不等于已掌握 2026 现状。
4. **产品开发**：核 L06/L09 完整作者、刊物／DOI、方法与不利结果；若讲 set-based / 延迟承诺的具体收益，需专门原始研究，不凭术语推出收益。
5. **因果与测量**：当前只有索引支持和机制推演，没有可靠效应量、失败发生率、通用规模阈值或实际项目测量；不可宣称质量投资必然回本。
6. **主线程合并**：保留本文件来源 ID、状态及失败记录；同源多 URL 不拆成独立证据；不把本文机制表升级为已证实规律。未做 Obsidian UI 渲染验证，不宣称完成阅读视图验收。

## Sources（本轮实际使用的来源链接）

- [L01 Chalmers 2013 论文记录](https://research.chalmers.se/publication/186358)；[出版社记录](https://www.sciencedirect.com/science/article/pii/S0164121213001477)
- [L02 InformIT 2003 书籍记录](https://www.informit.com/store/lean-software-development-an-agile-toolkit-9780321150783)；[O’Reilly 第 2 章索引入口](https://www.oreilly.com/library/view/lean-software-development/0321150783/ch02.html)
- [L03 Toyota TPS](https://global.toyota/en/company/vision-and-philosophy/production-system/)；[官方导览](https://global.toyota/en/company/plant-tours/production-system/)
- [L04 Deming Institute PDSA](https://deming.org/explore/pdsa/)；[FAQ](https://deming.org/about-us/f-a-qs/)
- [L05 ASQ TQM](https://asq.org/quality-resources/total-quality-management)
- [L06 2011 LPD 综述 DOI](https://doi.org/10.1080/10429247.2011.11431885)
- [L07 2015 度量综述机构记录](https://research.aalto.fi/en/publications/using-metrics-in-agile-and-lean-software-development-a-systematic/)
- [L08 2022 软件精益工具综述 DOI](https://doi.org/10.46254/EU05.20220448)
- [L09 2023 LPD 综述](https://www.mdpi.com/2071-1050/15/24/16721)


## Batch01-A 原文补读更新（2026-11-11）

### L01 — The Lean Gap（2013）

已读取 Chalmers 作者机构公开 PDF 全文。原文方法部分 Table 2／§3.2 将发表年份窗口写为 1990–2010，结果段 §3.3 又写为 1990–2011，存在内部不一致；五个数据库检索日均为 2011-02-05。初始 13,984 条，去重 3,754 条后 10,230 条候选；标题／关键词／摘要筛选排除 10,176 条，余 54 条；再排除 16 条，最终纳入 38 篇。16/38 涉及大型软件开发，76% 为非实证研究，9/38 为 evaluation 或 validation research。

**修订：** 这组统计描述的是该论文所覆盖的历史研究范围，不代表 2026 年当前领域比例。它提示大型软件场景中的精益证据不足，但不证明精益实践无效。

### L03 — Toyota Production System

已读取 Toyota 官方页面。官方定义 TPS 的两个支柱为 Jidoka 与 Just-in-Time，并把日常 Kaizen 作为持续改善基础。Jidoka 强调发现异常即停止、防止缺陷流向下游并在过程中内建质量；JIT 强调同步连续流、只在需要时生产所需数量。Toyota 页面也说明会维持满足流程同步所需的最低部件库存，因此 JIT 不应被误读成“零缓冲”。

### L04 — PDSA

已读取 Deming Institute 官方页面。其明确强调 PDSA 的第三步是 Study，而不是简单的 Check：研究实际结果、与预测比较、修正理论。不能将 Deming 的 PDSA 与泛化的 PDCA 检查清单混为一谈。

### L05 — TQM

已读取 ASQ 官方说明。其将 TQM 描述为客户导向、全员参与、流程方法、系统整合、战略一致、持续改善、事实决策与沟通的组织质量管理方式；同时列出管理承诺不足、数据不可靠、短期利润导向和跨团队合作不足等常见困难。

### 迁移边界修订

制造业到软件工程应迁移“异常及时暴露、质量内建、价值流、持续学习、全局优化”等机制，而不是照搬生产线形态。软件需求探索、知识不确定性、复制成本和演进方式不同；迁移必须通过端到端周期、返工、缺陷、在制品、维护负担和用户结果联合验证。

详见 [07_Batch01-A核心文献原文核验与证据修订记录](batch01-a-verification.md) 与 [sources](../evidence/sources.md)。
