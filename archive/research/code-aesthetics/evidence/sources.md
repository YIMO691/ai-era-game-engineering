---
title: Batch 01 唯一来源登记与主张账本

created_at: 2026-11-11
tags: [engineering-research, code-aesthetics, evidence]
---

> [!WARNING] Batch01-B 当前状态优先于下文历史声明
> 下文条目中的read_status与阅读日志保留为Batch01-A历史自述，不是本轮独立阅读证明。本轮没有取得任何目标全文、作者稿、直接摘要或外部元数据页面；搜索索引单列SEARCH_INDEX_ONLY，不升级阅读。正文事实均待核，不能由访问失败反推论文错误或前轮未读。审校结论PARTIAL，完整矩阵见 [12_Batch01-B核心论断证据审校](../audit/claim-evidence-matrix.md)。

## Batch02设计用途登记（2026-11-11）

16—18为本项目自行构造的定义、伪代码、题面与评分提案，不是新增外部实证来源。未新增阅读或网络请求，外部来源仍36项；本轮重点来源状态不升级。A01/A02及K01—K03只用作提出问题的入口，不借其未核效应、百分数或术语全集设量表／样本量；A03/L01/Q01/Q02/I02—I04不作为首组效果的已证依据。具体依赖见 [16_Batch02构念与测量草案](../batch02/constructs.md)。验收表是预期值，experiment_status仍not-run；本地文件检查不改变该状态。

## Batch01-B 独立状态表（2026-11-11）

ID均沿用ER-20261111-CA-前缀，不新增或重复登记论文。此表是当前审校层：全部read_status=access_failed、外部事实claim_status=unverified、experiment_status=not-run。逻辑／算术判断另列于矩阵，不冒充原文direct证据。未列24项不在本轮重点复核范围，状态仅历史继承，不授予新核验。

| Source ID | audit_evidence_status | 关键未决／允许措辞 | 日志 |
|---|---|---|---|
| A01 | NOT_ACCESSIBLE | 26次访谈与26人不可直接互换；not ugly为待核组织解释，非普遍准入制度 | [audit-aesthetics-craft](../audit/aesthetics-craft.md) |
| A02 | NOT_ACCESSIBLE | 0.33与0.0961口径未闭合；0.33²=0.1089，不据此改论文数字；秩相关不证明构念独立 | [audit-aesthetics-craft](../audit/aesthetics-craft.md) |
| A03 | NOT_ACCESSIBLE | 155为来包Git身份口径，自然人去重待核；6为所报受访者；分类非完整理论验证 | [audit-aesthetics-craft](../audit/aesthetics-craft.md) |
| L01 | NOT_ACCESSIBLE | 日期、筛选、10230/38/76%/42%/9均待正文；两年份冲突不擅自裁决，比例不是成功率 | [audit-lean](../audit/lean.md) |
| Q01 | NOT_ACCESSIBLE | 样本、两模型N、Time-in-Development定义、R²尺度待核；关联不等于干预ROI | [audit-quality-ai](../audit/quality-ai.md) |
| Q02 | NOT_ACCESSIBLE | 九术语及采用版身份待核；产品模型不是源代码美学量表；译名暂用 | [audit-quality-ai](../audit/quality-ai.md) |
| I02 | NOT_ACCESSIBLE | 16/246、时间效应和区间、ITT方法与署名差异待核；时间+19%不等于生产率−19% | [audit-quality-ai](../audit/quality-ai.md) |
| I03 | NOT_ACCESSIBLE | 选择方向与幅度未确认；不把方法更新当稳健普遍提速率 | [audit-quality-ai](../audit/quality-ai.md) |
| I04 | NOT_ACCESSIBLE | 26.08%的ITT/IV/LATE、采用定义、分母、权重及版本待核；SE原写法不裁定所有百分点表述错误 | [audit-quality-ai](../audit/quality-ai.md) |
| K01 | NOT_ACCESSIBLE | 两研究百分数分母、子组、材料和轮次待核；94/45不是实验条件分组的证据 | [audit-cognition](../audit/cognition.md) |
| K02 | NOT_ACCESSIBLE | 六维1989归属待核；候选分析词汇不是经验证量表 | [audit-cognition](../audit/cognition.md) |
| K03 | NOT_ACCESSIBLE | 原章／SEI均不可达，不能继承SECONDARY_SOURCE_ONLY；摘要作者与术语待核 | [audit-cognition](../audit/cognition.md) |

本轮实际调用：WebFetch 17次，全部安全检查失败；WebSearch 24次，仅发现线索。访问日志分载以上四份memo，均由本账本链接，不作为新增来源登记。失败不是404、撤稿或内容错误，不绕过拒绝。来源权利仍属原作者／出版者。

> [!NOTE] 历史：v0.2 状态更新（2026-11-11）
> v0.1 的“全部来源仍为 discovered / access_failed”是当时的状态，已被 Batch01-A 的定点原文核验更新。当前状态必须以各条目的 `read_status` 为准：部分论文全文已读，部分仅读取作者稿／工作论文，ISO 原版全文与若干书籍仍未直接读取。未完成的来源不得因本轮补读而自动升级。


# 来源、检索与主张账本

> [!WARNING]
> 公开研究草案：Batch01-B仍为PARTIAL，人工研究审核pending，代码／参与者实验未执行。公开提交授权不等于研究通过。
> 文内“未发布”、本地文件名、行号和检查点属于原研究时点；本页已作公开目录与链接适配，不是字节保真档案。当前阅读顺序与发布边界见[课题入口](../README.md)。


> [!NOTE] 当前证据状态与读取纪律
> 本账本保留 v0.1 的检索过程记录，并在 Batch01-A 中更新了部分来源的实际读取范围。`read_status` 必须逐条解释：`fulltext_read`、`fulltext_read_author_copy`、`official_page_read`、`targeted_read`、`secondary_summary_only` 等状态不可混用。搜索摘要不能替代全文；作者稿不能自动等同最终出版版；官方标准元数据不能等同标准全文。`claim_status=unverified` 表示该条具体主张尚未完成原文核验，不表示来源不存在或结论为假。

## 统一字段与权利

- 检索日期：2026-11-11。无自运行实验，所有条目 `experiment_status=not-run`。
- 索引提供的引文、章节位置只是**待回查定位**；不得包装成研究者逐字核对过的引文。
- 未下载或打包第三方全文，来源版权归原作者／出版社；本包仅保存短摘录、书目信息与研究者释义；开放访问不自动表示可重分发。
- DOI 是身份线索而非内容正确性的保证；同一论文的预印本、大学库、会议页合并为同一 ID，不算独立重复研究。
- 本文件是唯一权威来源登记；注释书目是按问题组织的阅读说明。工作备忘录保留过程，不作为第二套独立证据。
- 以下 main 编号 Q 为质量及经典、I 为 AI、C 为中文；A/L 为独立分支合并记录。

## 主线程来源

### ER-20261111-CA-Q01 — Increasing, not Diminishing：质量收益模型

- **Source**：Markus Borg, Ilyana Pruvost, Enys Mones, Adam Tornhill (2024). “Increasing, not Diminishing: Investigating the Returns of Highly Maintainable Code.” *Proceedings of the 7th ACM/IEEE International Conference on Technical Debt (TechDebt 2024)*, 21–30.
- **DOI / URL**：最终出版 DOI：https://doi.org/10.1145/3644384.3644471 ；全文预印本：https://arxiv.org/html/2401.13407 ；PDF：https://arxiv.org/pdf/2401.13407
- **Type / status**：同行评审会议论文；读取 arXiv 全文并交叉核对 ACM 最终出版元数据。`read_status=fulltext_read_preprint; claim_status=method_model_and_limits_checked`。
- **Method / sample**：两个工业数据集，合计 79 个专有软件项目、46,211 个源文件、25 种语言；以文件为单位，使用 Code Health 等代理指标分析缺陷数量和实现时间。
- **Findings**：作者提出质量健康度与缺陷、实现时间之间可能存在非线性关系，并建立价值模型讨论高维护健康度的潜在收益。回归模型的 R² 分别约为 0.038（缺陷）与 0.006（实现时间）。
- **Limits**：观察性数据，不是随机重构实验；低 R² 表明模型对结果的解释力有限；指标与样本具有工具／客户选择性；价值模型含假设，不是实际测得的重构 ROI。不能把相关性写成质量投入的因果回报。
- **Metadata note**：arXiv HTML 版本含旧 DOI 字符串；本登记以 ACM 最终出版 DOI `10.1145/3644384.3644471` 为准。
- **Relevance**：支持将代码健康与生命周期成本作为研究对象，不支持“越精致越赚钱”或“所有重构都值得做”。

### ER-20261111-CA-Q02 — ISO/IEC 25010:2023 产品质量标准

- **Source**：ISO/IEC 25010:2023, *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*, Edition 2, 2023-11-15.
- **URL**：ISO 官方页面：https://www.iso.org/standard/78176.html ；GSO 对 ISO/IEC 25010:2023 的采用版公开预览：https://gso-sims-preview-doc-aws.s3-eu-west-1.amazonaws.com/gso-iso-iec-25010-2025-en.html
- **Type / status**：国际标准；读取 ISO 官方元数据页及 GSO 采用版公开文本，未取得 ISO 官方付费原版全文。`read_status=official_metadata_plus_adoption_text; claim_status=nine_characteristics_checked`。
- **Nine characteristics**：Functional suitability；Performance efficiency；Compatibility；Interaction capability；Reliability；Security；Maintainability；Flexibility；Safety。
- **Relevance**：这是产品质量模型，不是源代码审美标准。可维护性、灵活性等可映射到内部设计属性，但需要额外操作化。
- **Limits**：不应将产品质量模型直接当作代码质量评分；2023 版的 Interaction capability / user engagement 面向用户交互体验，不等于源代码“美学”。ISO 原版完整文本未逐页核验。

### ER-20261111-CA-Q03 — 模块化与信息隐藏

- **Source**：D. L. Parnas (1972), *On the Criteria To Be Used in Decomposing Systems into Modules*. Communications of the ACM 15(12), 1053–1058。
- **DOI / URL**：https://doi.org/10.1145/361598.361623 ；大学转录 https://www.cs.lafayette.edu/~gexia/cs301/resources/parnas.html 。
- **Type**：经典设计论证。`read_status=discovered; claim_status=unverified`。
- **Scope / location / excerpt**：检索摘要和转录索引；结论定位词 “design decisions which are likely to change”。全文未读；转录页本身提示不保证原文完全准确。
- **Method / sample**：对同一问题的不同模块分解作设计比较，而非大规模因果实验；具体实例细节待原文核对。
- **Supports**：围绕需隐藏／可能变化的设计决策组织模块，是理解架构清晰性的经典入口。
- **Limits**：不推出模块越多越好；未来变化判断会出错，抽象也有成本。
- **Allowed**：作为机制与设计准则来源；**Forbidden**：用经典权威保证某个项目分层必然降低成本。

### ER-20261111-CA-Q04 — 认知限度与专业谦逊

- **Source**：Edsger W. Dijkstra (1972), *The Humble Programmer*. Communications of the ACM 15(10), 859–866；1972 ACM Turing Award Lecture，EWD340。
- **DOI / URL**：https://doi.org/10.1145/355604.361591 ；https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD340.html 。
- **Type**：学术演讲／规范性论证。`read_status=access_failed; claim_status=unverified`。
- **Scope / excerpt**：大学档案检索摘要关于认知限制、复杂度与纪律；WebFetch 安全检查失败，不提供假造逐字引文。
- **Method / sample**：历史与理论论证，无实验样本。
- **Supports**：品质追求可理解为对人的认知能力限制的回应，而不只是装饰偏好。
- **Limits**：不能代替现代程序理解实验，也不直接支持 AI 工具效果。

### ER-20261111-CA-Q05 — 重构的工作定义

- **Source**：Martin Fowler (2004-09-01), *Definition Of Refactoring*，作者网站。
- **URL**：https://martinfowler.com/bliki/DefinitionOfRefactoring.html 。DOI：不适用。
- **Type**：专业实践定义。`read_status=discovered; claim_status=unverified`。
- **Scope / location / excerpt**：索引中的定义段，“without changing its observable behavior”。未直接读取正文。
- **Method**：术语说明，无实验样本。
- **Supports**：区分行为保持的结构改善，与功能修改、优化或一般重写。
- **Limits**：定义并不自动证明某次修改行为保持；需要实际测试或更强验证。

### ER-20261111-CA-Q06 — 技术债与偿还决策

- **Source**：Martin Fowler (2009-10-14), *Technical Debt Quadrant*，作者网站。
- **URL**：https://martinfowler.com/bliki/TechnicalDebtQuadrant.html 。DOI：不适用。
- **Type**：工程实践概念模型。`read_status=discovered; claim_status=unverified`。
- **Scope / excerpt**：检索可见 prudent/reckless 与 deliberate/inadvertent 两轴。
- **Method / sample**：解释性分类，非统计分类器。
- **Supports**：债务可能来自学习而不只是偷工减料；偿还要考虑未来变化成本。
- **Limits**：并非所有不喜欢的代码都是债；不证明债务可由一个指标准确货币化。

### ER-20261111-CA-Q07 — 重构的经济停止条件

- **Source**：Martin Fowler，*Workflows of Refactoring*。页面年份本轮未可靠取得，不猜填。
- **URL**：https://martinfowler.com/articles/workflowsOfRefactoring/fallback.html 。DOI：不适用。
- **Type**：工程师实践论述。`read_status=discovered; claim_status=unverified`。
- **Scope / excerpt**：索引摘录 “Don't refactor unless you think you will recoup your investment later by quicker work.”；正文未读。
- **Method / sample**：经验性指导，无统一实验样本。
- **Supports**：质量改进应该面向实际工作及回报，而非完美主义。
- **Limits**：对安全、合规等硬约束，本研究不以节省时间作为唯一理由；此补充是综合判断，不归给作者。

### ER-20261111-CA-Q08 — 重构并非全面改善质量

- **Source**：Satnam Kaur, Paramvir Singh (2019), *How does object-oriented code refactoring influence software quality? Research landscape and challenges*. Journal of Systems and Software 157, 110394。
- **DOI / URL**：https://doi.org/10.1016/j.jss.2019.110394 ；https://www.sciencedirect.com/science/article/pii/S0164121219301694 ；https://arxiv.org/abs/1908.05399 。
- **Type**：系统映射研究。`read_status=discovered; claim_status=unverified`。
- **Scope / location**：出版社／预印本摘要的检索汇总，未读正文。
- **Method / sample**：摘要索引报告 142 项实证研究。
- **Findings**：索引报告重构不一致地改善所有属性；学术环境结果比工业环境更正向。
- **Limits**：检索截止、编码规则、各属性效应与异质性未原文核验。不是“重构普遍有害”的证据。
- **Relevance**：要求具体说明改善哪项属性、付出什么代价，不能仅统计重构次数。

### ER-20261111-CA-C01 — 国内代码坏味综述

- **Source**：田迎晨、李柯君、王太明、焦青青、李光杰、张宇霞、刘辉 (2023)，《代码坏味研究综述》，软件学报 34(1):150–170。
- **DOI / URL**：https://doi.org/10.13328/j.cnki.jos.006431 ；https://www.jos.org.cn/jos/article/issue/2023_34_1 。本轮尝试全文路径 https://www.jos.org.cn/html/2023/1/6431.htm 未成功，因此不将路径正确性视为已验证。
- **Type**：中文综述。`read_status=access_failed; claim_status=unverified`。
- **Scope / location / excerpt**：官方期刊目录摘要索引，“1990年至2020年6月”“339篇”；正文未读取。
- **Method / sample**：摘要称对上述339篇分类，比较工业界和学术界关注。
- **Limits**：中文文献覆盖不是 CNKI 系统检索；研究截止于2020年，不能代表2026年全貌。未原文核对完整筛选协议。
- **Relevance**：将坏味作为研究对象／风险线索，而不是通用缺陷裁决；具体坏味与缺陷关系仍需逐研究验证。

### ER-20261111-CA-C02 — 国内程序理解综述

- **Source**：金芝、刘芳、李戈 (2019)，《程序理解:现状与未来》，软件学报 30(1):110–126。索引报告在线发表于2018-11-20。
- **URL**：https://www.jos.org.cn/html/2019/1/5643.htm 。DOI：本轮未可靠核验，不按网页编号猜写。
- **Type**：综述。`read_status=discovered; claim_status=unverified`。
- **Scope**：官方索引摘要关于认知、方法、软件工程，静态／动态分析和学习技术；未读正文。
- **Method / sample**：综述；纳入文献数与筛选方法未核验。
- **Relevance / limits**：为“代码短但难懂”的认知问题提供国内入口，不直接证明哪种代码风格更易理解。

### ER-20261111-CA-I01 — AI 的受控任务加速证据

- **Source**：Sida Peng, Eirini Kalliamvakou, Peter Cihon, Mert Demirer (2023), *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*。
- **DOI / URL**：https://doi.org/10.48550/arXiv.2302.06590 ；https://arxiv.org/abs/2302.06590 ；https://www.microsoft.com/en-us/research/publication/the-impact-of-ai-on-developer-productivity-evidence-from-github-copilot/ 。
- **Type / version**：预印本及机构记录，2023版本。`read_status=discovered; claim_status=unverified`。
- **Scope / excerpt**：摘要索引 “55.8% faster”；非本轮实测。
- **Method / sample**：受控实验，实现 JavaScript HTTP server；人数、退出样本和精确计算口径本轮未核验，不猜填。
- **Supports**：特定任务下允许 Copilot 的实验组完成更快。
- **Limits**：不是系统生命周期质量、维护成本或全部开发任务的提升；不把“faster”擅自换算成吞吐量百分比。机构与工具供应商关系需纳入独立性评估。

### ER-20261111-CA-I02 — METR 2025 熟悉仓库减速证据

- **Source**：Joel Becker, Nate Rush, Beth Barnes, David Rein (2025). “Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity.” METR research paper. METR PDF 首页及机构博客署名 Beth Barnes；arXiv 元数据页显示 Elizabeth Barnes，本账本按 PDF 正文署名记录并保留该元数据差异。
- **URL / DOI**：METR 论文 PDF：https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf ；研究说明：https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ ；arXiv：https://doi.org/10.48550/arXiv.2507.09089
- **Type / status**：随机任务实验论文与机构说明；全文 PDF 已读。`read_status=fulltext_read; claim_status=sample_design_and_ci_checked`。
- **Method / sample**：16 名经验丰富的开源开发者、246 项来自熟悉仓库的任务；随机任务是否允许使用当时的 AI 工具。
- **Findings**：允许 AI 的任务完成时间平均增加约 19%，论文报告 95% 区间约为 2%–39% 的时间增加。处理条件是“允许使用 AI”，不是强制使用。
- **Limits**：小样本、熟悉仓库、早期 2025 工具和特定任务；不能泛化到所有开发者、任务或 2026 coding agents；时间增加不等于代码质量下降。
- **Relevance**：构成“AI 必然提速”的反向证据，说明生产力效果具有情境依赖性。

### ER-20261111-CA-I03 — METR 2026 方法更新及选择偏差

- **Source**：METR (2026-02-24), “We are Changing our Developer Productivity Experiment Design.”
- **URL**：https://metr.org/blog/2026-02-24-uplift-update/
- **Type / status**：机构方法更新；官方页面全文已读。`read_status=official_page_read; claim_status=design_change_and_bias_checked`。
- **Findings**：前轮记录后续实验存在参与者／任务选择和测量问题；参与者与任务进入研究的选择机制可能影响效果估计，其方向和幅度须据官方原文核验。本轮暂撤“偏向AI适用场景”的方向断言，不据搜索索引反向定论；后续估计不能直接当作稳健、无偏的普遍提速率。
- **Limits**：这不是“2026 AI 已证明提速”的证据，也不自动推翻 2025 年在特定环境观察到的减速。
- **Relevance**：强调生产力研究必须报告任务、样本、工具版本、分配方式和自选择偏差。

### ER-20261111-CA-I04 — AI 的现场实验补充：Cui 等人（2026）

- **Source**：Kevin Zheyuan Cui, Mert Demirer, Sonia Jaffe, Leon Musolff, Sida Peng, Tobias Salz (2026). “The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers.” *Management Science* 72(11):9408–9420; published online 2026-02-27.
- **DOI / URL**：https://doi.org/10.1287/mnsc.2025.00535 ；INFORMS：https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535 ；在线附录：https://pubsonline.informs.org/doi/suppl/10.1287/mnsc.2025.00535/suppl_file/mnsc.2025.00535.sm1.pdf ；作者工作论文：https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4945566
- **Type / status**：同行评审期刊论文；读取作者工作论文全文、INFORMS 最终出版页与在线附录。`read_status=fulltext_read_working_paper_plus_final_metadata; claim_status=sample_and_main_result_checked`。
- **Method / sample**：三组现场随机实验，Microsoft、Accenture、一家匿名 Fortune 100 企业；最终样本 4,867 名开发者（附录清洗后分别为 1,521、316、3,030）。随机分配访问 AI 代码补全工具。
- **Findings**：INFORMS 官方摘要原文报告合并分析中完成任务数量增加 26.08%（standard error: 10.3%）；经验较少的开发者采用率和生产力收益更高。保留官方原始写法，不改写为“百分点”。
- **Limits**：任务完成数量不是代码质量；工作论文版本使用 PR 等产出指标，构建成功率也只是很窄的质量代理，不覆盖架构、可维护性、安全性和长期缺陷。实验工具以代码补全为主，不能直接等同于 2026 agentic coding 工作流。
- **Relevance**：证明特定企业和任务环境下 AI 可提高产出，但不证明生产力红利会自动转化为工程品质。

### ER-20261111-CA-Q09 — 技术债隐喻原始入口

- **Source**：Ward Cunningham (1992), *The WyCash Portfolio Management System*，OOPSLA ’92 Experience Report / Addendum，29–30。
- **DOI / URL**：会议记录 https://doi.org/10.1145/157709.157715 ；作者版本 https://c2.com/doc/oopsla92.html 。期刊版本的卷期／年份另有记录，不混合填入会议书目。
- **Type / scope**：工业经验报告；`read_status=discovered; claim_status=unverified`。本轮只读索引元数据及作者网站的摘要总结；正文未读。定位：作者网页，索引标1992-03-26；无经正文核对短引文。
- **Method / sample / finding**：Smalltalk金融软件WyCASH+经验报告，债务隐喻是后续理论追踪入口；不是债务利息普遍量化实验。
- **Relevance / limits**：用跨时间成本思考临时方案及学习后的设计调整；不得把所有坏代码都称作原作者定义的技术债，不猜测固定债务增长率。

### ER-20261111-CA-Q10 — Clean Code 的文献身份

- **Source**：Robert C. Martin (2008), *Clean Code: A Handbook of Agile Software Craftsmanship*，第一版，Prentice Hall / Pearson，ISBN 9780132350884。
- **URL**：https://www.pearson.com/en-us/subject-catalog/p/clean-code-a-handbook-of-agile-software-craftsmanship/P200000009044 。DOI：不适用。
- **Type / status**：实践著作；`read_status=discovered; claim_status=unverified`。仅出版社书目与样章索引；索引区分2008发行、2009版权，无正文阅读。
- **Method / sample**：实践指导与示例，不能作为每条规则已被实验确认的依据；本轮未分析原书示例。定位：出版社简介；无正文短引文。
- **Relevance / limits**：属于工艺传统的重要实践表达，不是ISO标准或统一科学理论。不能将小函数、命名等建议直接变为跨语言硬阈值；本条仅核查文献身份。

### ER-20261111-CA-Q11 — 可读性量化入口

- **Source**：Raymond P. L. Buse, Westley R. Weimer (2010), *Learning a Metric for Code Readability*，IEEE Transactions on Software Engineering 36(4):546–558。
- **DOI / URL**：https://doi.org/10.1109/TSE.2009.70 ；作者稿 https://web.eecs.umich.edu/~weimerw/p/weimer-tse2010-readability-preprint.pdf 。
- **Type / status**：经验性可读性建模；`read_status=discovered; claim_status=unverified`。
- **Scope / method / sample**：作者稿检索摘要报告120名标注者，以局部代码特征学习可读性判断，并研究大型代码样本中的关联；未读正文，抽样、评价量表、训练测试分离、任务条件未核验。定位：摘要；不抄录未经核验的性能数。
- **Supports / limits**：可读性可以被操作化研究；对主观标签的预测不等于对真实理解、修改正确性或全系统维护性的预测。
- **Relevance**：Batch02须把偏好评分与实际任务表现分开测量。

### 追加检索式（已执行）

21. `"Measuring the Impact of Early-2025 AI" "Becker" "Barnes"` — METR PDF 首页与官方博客署名 Beth Barnes；arXiv 元数据页显示 Elizabeth Barnes；本表按 PDF 正文署名记录，并保留差异。
22. `Ward Cunningham 1992 WyCash portfolio management system technical debt OOPSLA 4 6` — 后两个数字不获确认，不作为书目数据；采用会议记录29–30。
23. `site.pearson.com "Clean Code" "2008" Martin`。
24. `Buse Weimer 2010 Learning a Metric for Code Readability 120 participants IEEE`。


## 合并登记：美学与工艺


共同字段：访问日期 2026-11-11；`experiment_status: not-run`。下文 `read_status: access_failed` 表示实际抓取失败，仍可能通过搜索发现元数据；`discovered` 表示仅发现来源。两者都不等于读过正文。搜索工具生成的说明不冒充原文短摘录；无可核对摘录时明确留空。

### ER-20261111-CA-A01 — Coding Beauty and Decoding Ugliness

- **Source**：Marina Fedorova, Melissa Mazmanian, Paul Dourish (online first 2024-04-15; issue 2025). “Coding Beauty and Decoding Ugliness: The Role of Aesthetic Concerns in Programming Practices.” *Science, Technology, & Human Values*, 50(1), 69–93.
- **DOI / URL**：https://doi.org/10.1177/01622439241245746 ；全文 PDF：https://journals.sagepub.com/doi/pdf/10.1177/01622439241245746
- **Type / status**：同行评审定性实地研究。`read_status=fulltext_read; claim_status=method_and_findings_checked`。
- **Method / sample**：2014 年在 Yandex 莫斯科办公室开展约三个月田野工作；26 名程序员半结构化访谈，另有 4 次管理者／专家访谈，并结合现场观察；访谈俄语进行并转录、翻译。
- **Findings**：Yandex 内不存在单一的 beautiful code 审美理想；开发者保留不同理解。相较之下，对多种 ugly code 形式有较共享的识别；“not ugly”成为经集体认可、可进入代码库的默认类别。审美语言既能容纳专业背景差异，也参与形成一致的本地代码实践与新人社会化。
- **Limits**：单一企业、单一时期的定性组织研究；不是代码风格随机实验，不测量缺陷率、维护成本或质量因果效果。
- **Relevance**：支持“代码美学是组织实践与专业文化的一部分”，不支持“存在一个跨团队的客观美代码标准”。审美评价与工程质量需分别测量。

### ER-20261111-CA-A02 — Aesthetics Versus Readability of Source Code

- **Source**：Ron Coleman (2018). “Aesthetics Versus Readability of Source Code.” *International Journal of Advanced Computer Science and Applications*, 9(9).
- **DOI / URL**：https://doi.org/10.14569/IJACSA.2018.090902 ；全文 PDF：https://thesai.org/Downloads/Volume9No9/Paper_2-Aesthetics_versus_Readability_of_Source_Code.pdf
- **Type / status**：探索性定量研究。`read_status=fulltext_read; claim_status=method_checked_with_measurement_caveat`。
- **Method / sample**：GNU Core Utilities 的 114 个程序，原始约 70,000 LOC；剔除编译／预处理指令、原型、typedef 等后形成 1,043 个单函数 C 文件、约 53,000 LOC。计算 11 个 beauty factors 与 8 个 readability scores，并使用 Spearman’s rho 分析 88 组相关。
- **Findings**：论文报告显著相关的绝对 Spearman 系数约在 0.05–0.59 之间，没有强相关；作者报告其中位相关平方值为 0.0961，并据此认为 beauty 与 readability 不是可互换代理。
- **Limits**：beauty factor 是特定形式／分形维度代理指标，不是程序员主观审美测量；单一 C 项目语料；没有真实维护者理解、缺陷定位或修改任务实验。Spearman ρ²是秩相关平方，不能直接解释为原尺度美学指标中由可读性解释的方差比例；即使回归R²也不自动具有因果解释。
- **Relevance**：只能作为“特定美学代理指标与可读性代理指标并非同一变量”的探索性证据，不能声称已建立客观代码美学量表。

### ER-20261111-CA-A03 — Towards an Anatomy of Software Craftsmanship

- **Source**：Anders Sundelin, Javier Gonzalez-Huerta, Krzysztof Wnuk, Tony Gorschek (2022). “Towards an Anatomy of Software Craftsmanship.” *ACM Transactions on Software Engineering and Methodology*, 31(1), Article 6. DOI: 10.1145/3468504.
- **DOI / URL**：https://doi.org/10.1145/3468504 ；作者公开稿：https://anders.sundelinkarlskrona.se/wp-content/uploads/2021/06/TowardsAnAnatomyOfSoftwareCraftsmanship-authorCopy.pdf ；博士论文收录版：https://bth.diva-portal.org/smash/get/diva2%3A1997635/FULLTEXT01.pdf
- **Type / status**：同行评审论文；全文读取作者公开稿，最终卷期和 DOI 由 BTH 论文书目交叉核验。`read_status=fulltext_read_author_copy; claim_status=method_and_results_checked`。
- **Method / sample**：2018 年 12 月 Google Scholar 检索得到 980 条；按两项标准排除 522 与 346 条，留下 112 篇候选；以 4 篇数据库种子论文起步，再依据作者经验和推荐增加 5 篇种子，进行四轮 snowballing；最终纳入 18 篇论文和 11 本书。结合 Ericsson 一个金融市场产品约七年的纵向工业案例（约 20 个全球部署）。研究期报告按 Git Author tag 识别155个贡献者身份（自然人去重口径待核），案例访谈报告为6名参与者；第一作者曾是项目开发者。
- **Findings**：形成四主题、17 原则、47 项层级实践：A 价值导向架构（3 原则／10 实践）；D 迭代设计、开发与验证（3／10）；C 共享专业文化（6／18）；F 反馈（5／9）。
- **17 principles**：A1 Participating software architects；A2 Encapsulation & separation of concerns；A3 Clean, minimalistic code；D1 Incremental development；D2 Testing pyramid, layered testing；D3 Design documentation；C1 Standard development environment；C2 Common professional culture；C3 Cross-team communication；C4 Visibility / Transparency；C5 Accountability；C6 Culture of learning；F1 On-site customer (proxies)；F2 Short feedback loops；F3 Reviews；F4 Learning from feedback；F5 Continuous integration and tests。
- **Limits**：单一产品和组织；第一作者参与案例产品开发，存在 insider perspective；研究主要建立概念地图，并未通过对照实验证明 17 原则的因果收益；47 项实践不能直接当作普遍强制清单。
- **Relevance**：本研究最直接的软件工艺基础，说明工程品质涉及架构、迭代、测试、专业文化和反馈，而非仅仅局部代码风格。

### ER-20261111-CA-A04 — On Quantifying Software Craftsmanship Concepts

- **Source**：Anders Sundelin (2025). *On Quantifying Software Craftsmanship Concepts*. Blekinge Institute of Technology, Doctoral Dissertation Series No. 2025:12. ISBN 978-91-7295-512-7.
- **URL**：https://bth.diva-portal.org/smash/get/diva2%3A1997635/FULLTEXT01.pdf
- **Type / status**：博士论文；本轮定点阅读摘要、目录、Paper I 与 Future Work 相关章节，未声称逐页读完全部论文。`read_status=targeted_read; claim_status=ai_statement_context_checked`。
- **Method / scope**：混合方法研究，包含系统文献综述、纵向工业案例、案例研究、经验报告和行动研究；摘要称量化 anatomy 中部分实践的影响。
- **Findings / AI passage**：作者在 Future Work 中讨论 LLM：强调反馈、迭代设计、专业文化、价值导向架构和可自动验证的测试边界；并明确表示 LLM 对未来专业软件工程师的影响仍有待观察。
- **Limits**：AI 部分属于研究展望和作者判断，不是 AI 编码生产力或代码质量的实证结果；论文中也不是所有实践都被量化。
- **Relevance**：可作为“软件工艺如何面对 LLM”的学术研究接口，不应引用为“研究已经证明 AI 必须如何工作”。

### ER-20261111-CA-A05 — Manifesto for Software Craftsmanship

- **完整书目**：Software Craftsmanship Manifesto（2009，集体签署文本；不是期刊论文）。官方页面：https://manifesto.softwarecraftsmanship.org/
- **Source type / status**：官方规范性宣言。官方搜索索引返回完整四项陈述，已与公开会议材料交叉核对；官方 SPA 页面本轮只解析出语言导航，未直接读取页面 DOM 全文。`read_status=official_text_crosschecked; claim_status=wording_crosschecked_by_official_index`。
- **核心陈述**：不仅要 working software，也要 well-crafted software；不仅响应变化，也要持续增加价值；不仅关注个人互动，也要建设专业共同体；不仅客户协作，也要形成 productive partnerships。
- **Method / sample**：不适用；这是价值宣言，不是效果实验。签署人数不能作为有效性样本。
- **Limits**：表达应追求什么，不证明追求后必然产生何种结果；不能从宣言单句推导一套不计成本的完美主义规则。
- **Relevance**：可作为软件工艺运动的规范性思想来源；需与同行评审的实证研究分开引用。

### ER-20261111-CA-A06 — Principles behind the Agile Manifesto

- **完整书目**：Agile Manifesto signatories (2001). *Principles behind the Agile Manifesto*. https://agilemanifesto.org/principles.html
- **Source type / status**：官方规范性文本；官方原则页面全文已读取。`read_status=official_page_read; claim_status=wording_checked`。
- **关键原则**：持续关注技术卓越与良好设计会增强敏捷性；简洁是最大化不做工作之艺术；团队定期反思并调整行为以提升有效性。
- **Method / sample**：不适用；规范文本不是效果实验。
- **Relevance**：软件工艺与敏捷不是简单对立。技术卓越、设计质量、简洁和反思已在 Agile Principles 中明确出现；争论应转向实践强度、组织机制与工程结果，而非制造二元阵营。
- **Limits**：原则声明不等于这些实践在所有团队中都已落实，也不单独证明其因果收益。

### ER-20261111-CA-A07 — The Craftsman

- **完整书目**：Richard Sennett. *The Craftsman*. New Haven: Yale University Press, 2008。非期刊，未发现/核验 DOI。需注意本次定位到的 Yale 页面是2009-03-31平装版，ISBN 9780300151190，不能用它的日期替换原著2008年。
- **URL**：[Yale官方书页](https://yalebooks.yale.edu/book/9780300151190/the-craftsman/)；[On Work 的p.9引文索引](https://onwork.edu.au/bibitem/2008-Sennett%2CRichard-The%2BCraftsman-excerpt%2Bp.9/)；[Boston University书评](https://www.bu.edu/cpt/resources/book-reviews/craftsman-by-richard-sennett/)。后两者仅用于定位，不能代替作者原书。
- **Source type**：一手理论著作；本轮实际取得的是出版社元数据/简介索引与二手引文索引。
- **read_status**：`access_failed`。**实际读到范围**：搜索结果；出版社页抓取失败，原书与任何章节均未读。**claim_status**：引文定位 `unverified`；不是原书已读。
- **原文定位与短摘录**：搜索工具转引 On Work/BU，指向2008版 **p.9**：“Craftsmanship names an enduring, basic human impulse, the desire to do a job well for its own sake.” 这是**二手索引转引、待对原书**，不是本轮从书页抄录的引文。
- **方法/样本**：理论专著，具体历史材料、章节论证和选择过程未读；不虚构实验样本或因果识别方法。
- **理论用途**：提供一种工艺动机的解释——工作做得好可以被视为自身目的，而非只有外部报酬或工具性结果。它可解释价值取向，不能证明每位程序员都如此，或这种动机必然优于其他动机。
- **限制/反证**：句中“basic human impulse”是作者理论命题，应与跨文化心理学检验区分。不能仅据这句话将追求完美、过度设计、身份精英主义合理化；亦不能据此推定书中赞同这些行为。
- **Supports / Contradicts**：候选支持“品质可能有内在价值”的理论溯源；不支持“所有工艺追求都值得投入”。
- **项目相关性**：为解释开发者为何在可交付之外关心作品品质提供概念，而不是工程投资判据。
- **允许措辞**：“Sennett 的理论常以‘把工作做好本身就是目的’来界定工艺动机；本轮仅定位到p.9的二手引文与官方书目，尚未读原书。”
- **禁止更强措辞**：“心理学证明程序员天生追求工艺”“Sennett证明优美代码降低缺陷”“已读完The Craftsman”。
- **权利**：Yale版权图书；未下载付费全文，搜索出现的非出版社章节副本未抓取，不作其权利合法性的判断。


## 合并登记：精益与产品开发


**共同字段**：访问／检索日均为 2026-11-11；`experiment_status: not-run`。权利均为原作者／出版商／机构所有，未核开放许可，不推定可全文转载。`read_status: access_failed` 表示尝试正文失败但仍有索引线索；`discovered` 表示只发现索引未请求正文。以下“短摘录”若仅为标题／章名，会明确标识；**没有伪造正文引文**。搜索工具返回总结不保证逐字忠实，不能再加引号冒充原文。

### ER-20261111-CA-L01 — The Lean Gap（指定 2013 年综述）

- **Source**：Joakim Pernstål, Robert Feldt, Tony Gorschek (2013). “The Lean Gap: A Review of Lean Approaches to Large-Scale Software Systems Development.” *Journal of Systems and Software*, 86(11), 2797–2821.
- **DOI / URL**：https://doi.org/10.1016/j.jss.2013.06.035 ；作者机构全文：https://gorschek.com/wp-content/uploads/2019/11/The-lean-gap-A-review-of-lean-approaches-to-large-scale-software-systems-development.pdf
- **Type / status**：系统性映射研究（SMS）。`read_status=fulltext_read; claim_status=selection_and_statistics_checked`。
- **Method / sample**：五个数据库（ACM DL、IEEE Xplore、Inspec、ISI Web of Science、Scopus）于 2011-02-05 检索。原文方法部分 Table 2／§3.2 将发表年份窗口写为 1990–2010；结果段 §3.3 又写为 1990–2011，存在内部不一致，不擅自裁定为单一范围。初始 13,984 条，去重 3,754 条后 10,230 条候选；标题／关键词／摘要筛选排除 10,176 条，余 54 条；再排除 16 条，最终纳入 38 篇。
- **Findings**：16/38（约 42%）明确涉及大型软件开发；76% 被归类为非实证研究；只有 9/38（约 24%）属于 evaluation 或 validation research；16 项大型开发研究中只有 4 项为实证研究。两轮筛选试点的 Fleiss’ Kappa 从 0.50 提高到 0.74。
- **Limits**：年份窗口存在原文内部不一致；数据库检索日为 2011-02-05，不能当作 2026 年现状。38 是论文数，不是独立实验数；76% 不是失败率。摘要筛选、分类和数据提取存在研究者判断，作者讨论了相关威胁。
- **Relevance**：为制造业精益思想迁移到软件工程设定证据边界；支持“迁移原则并验证机制”，不支持机械照搬 TPS。

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

- **Source**：Toyota Motor Corporation. *Toyota Production System*. n.d., official website.
- **URL**：https://global.toyota/en/company/vision-and-philosophy/production-system/
- **状态／类型**：官方机构说明，全文已读。`read_status=official_page_read; claim_status=official_definition_checked`。
- **Findings**：TPS 两大支柱为 Jidoka 与 Just-in-Time；Toyota 将日常增量 Kaizen 作为持续改善基础。Jidoka 强调发现异常即停止、防止缺陷流向下游、将质量构建在流程中；JIT 强调流程同步与连续流，按需、按时、按量生产。
- **Important nuance**：官方页面说明 JIT 流程会维持满足生产同步所需的最低部件库存，故不能将 JIT 简化为零库存、零缓冲或极限压缩。
- **Limits**：官方页面直接支持 Toyota 对自身 TPS 的定义，不单独证明某个软件实践会改善软件绩效。
- **Relevance**：提供质量内建、异常停止、流程同步和持续改善的原始组织机制。

### ER-20261111-CA-L04 — Deming Institute 的 PDSA 说明

- **Source**：The W. Edwards Deming Institute. *The PDSA Cycle*. n.d., institutional explanation.
- **URL**：https://deming.org/explore/pdsa/
- **状态／类型**：官方机构说明全文已读；不是 Deming 亲笔原件。`read_status=official_page_read; claim_status=institutional_explanation_checked`。
- **Findings**：PDSA 将 Plan、Do、Study、Act 组织为持续学习循环；Deming Institute 强调第三步为 Study，而非简单的 Check。Study 关注预测、实际结果、偏差与理论修正。
- **Limits**：本页支持机构对 PDSA 的解释，不足以单独完成 PDSA/PDCA 的完整历史起源考证；不能把 Deming 简化成“发明 PDCA”。
- **Relevance**：支持把软件改进看作带预测、观测和学习的循环，而不是完成清单。

### ER-20261111-CA-L05 — ASQ 的 TQM 定义

- **Source**：American Society for Quality (ASQ). *Total Quality Management (TQM): What is TQM?* n.d.
- **URL**：https://asq.org/quality-resources/total-quality-management
- **状态／类型**：专业质量机构说明全文已读。`read_status=official_page_read; claim_status=definition_and_limits_checked`。
- **Findings**：TQM 被描述为客户导向、全员参与、流程方法、系统整合、战略一致、持续改善、事实决策和沟通的组织质量管理方式。页面同时列出管理承诺不足、数据不可靠、短期利润导向、缺少共同愿景和跨团队协作等常见困难。
- **Limits**：这是专业机构的定义与教学材料，不是 TQM 效果的系统综述或随机实验。
- **Relevance**：帮助把质量从末端测试扩展为组织层面的责任、流程与持续改善。

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


## 美学与工艺主张和访问日志


| Claim | Evidence | Allowed wording | Forbidden stronger wording | Uncertainty / Next check | Decision |
|---|---|---|---|---|---|
| 美学判断既涉及个人理想也涉及团队规范 | A01 | 限定为索引所述单组织质性解释 | 已证明普遍因果规律 | 读Methods、Findings、Discussion，核对观察与访谈证据 | weaken |
| 美学与可读性不能简单等同 | A02 | 模型比较的候选启示 | 美学无用/美学必然易读 | 核对指标定义、表格、语言与数据集 | weaken |
| 工艺包含4主题17原则47实践 | A03 | 索引中提出的分类 | 17条科学定律、47项必须遵守 | 读§5/Fig.3与完整编码方法 | keep（限定位线索） |
| 有七年金融案例 | A03/A04同源 | 索引报告纵向案例 | 七年因果证明、两项独立复制 | 核对案例起止、组织/参与者、作者角色和替代解释 | weaken |
| 博士论文有AI展望 | A04 | 未核验 | 已有/不存在/已证实有效 | 在合法可访问正文中查Future Work/AI/LLM | revise为缺口 |
| 工艺补充而非否定可工作软件 | A05 | 索引首项的not only语义 | 工艺、敏捷、XP完全等价 | 官方四项完整文本及历史一手说明 | weaken |
| 内在品质动机是工艺理论的一条线索 | A07 | Sennett理论的待核对定位 | 所有人类/程序员均被实证证明如此 | 读2008版p.9及上下文，检查作者对完美主义与限制的讨论 | weaken |

## 真实检索式与访问失败日志

以下按调用批次列出；并行调用无严格先后含义。共16次，不包括本地文件操作。

| # | 类型 | 实际请求 | 结果 |
|---|---|---|---|
| 1 | WebSearch | `"Coding Beauty and Decoding Ugliness"` | 定位SAGE DOI、双年份、作者及摘要线索。 |
| 2 | WebSearch | `"Sundelin" "Software Craftsmanship" 2025 2022` | 定位2022论文、2025博士论文及BTH大学库PDF。 |
| 3 | WebSearch | `Ron Coleman "Aesthetics Versus Readability" 2018` | 定位出版社记录/PDF、元数据、方法与数字摘要。 |
| 4 | WebFetch | `https://journals.sagepub.com/doi/10.1177/01622439241245746` | safe-fetch失败；未返回正文。 |
| 5 | WebFetch | `https://thesai.org/Downloads/Volume9No9/Paper_2-Aesthetics_versus_Readability_of_Source_Code.pdf` | safe-fetch失败；未返回PDF正文。 |
| 6 | WebFetch | `https://bth.diva-portal.org/smash/get/diva2%3A1997635/FULLTEXT01.pdf` | safe-fetch失败；未返回论文正文。 |
| 7 | WebSearch | `Richard Sennett The Craftsman 2008 "for its own sake" Yale excerpt` | 定位Yale书页、p.9二手引文、2008/2009版本差异。 |
| 8 | WebFetch | `https://manifesto.softwarecraftsmanship.org/` | safe-fetch失败；未返回官方正文。 |
| 9 | WebFetch | `https://agilemanifesto.org/principles.html` | safe-fetch失败；未返回官方正文。 |
| 10 | WebFetch | `https://yalebooks.yale.edu/book/9780300151190/the-craftsman/` | safe-fetch失败；未返回出版社页面。 |
| 11 | WebSearch | `"Towards an Anatomy of Software Craftsmanship" "themes" "principles"` | 得到四主题、17/47、§5/Fig.3与18篇/11书/七年案例索引线索。 |
| 12 | WebSearch | `"On Quantifying Software Craftsmanship Concepts" "AI" "seven"` | 无明确匹配；噪声结果未采用。 |
| 13 | WebSearch | `site:bth.diva-portal.org "On Quantifying Software Craftsmanship Concepts" "intelligence"` | No links found；不是否定证据。 |
| 14 | WebSearch | `"Coding Beauty and Decoding Ugliness" "interviews" "Yandex"` | SAGE索引方法摘要：三个月、26开发者+4管理者等，未读正文。 |
| 15 | WebSearch | `software craftsmanship manifesto "Not only" "XP" agile` | 主要命中转载/读书笔记和A03作者稿；不提升为一手正文证据。 |
| 16 | WebSearch | `"manifesto" "Not only working software" "well-crafted software"`；allowed_domains=`["manifesto.softwarecraftsmanship.org"]` | 定位官方站索引首项及2009版权年份。 |

六次失败均返回同类信息：`Unable to verify if domain [域名] is safe to fetch. This may be due to network restrictions or enterprise security policies blocking claude.ai.` **这是工具访问检查失败，不是HTTP 403/404，不证明网站付费、链接失效或文章不存在。** 收到协调者关于同类限制的提醒后，未再尝试抓取或规避；用剩余少量搜索定位，随后停止。


## 精益主张和访问日志


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

## Batch01-A 新增认知与程序理解来源

### ER-20261111-CA-K01 — Empirical Studies of Programming Knowledge

- **Source**：Elliot Soloway and Kate Ehrlich (1984). “Empirical Studies of Programming Knowledge.” *IEEE Transactions on Software Engineering*, SE-10(5), 595–609.
- **DOI / URL**：https://doi.org/10.1109/TSE.1984.5010283 ；公开 PDF：https://www.cs.kent.edu/~jmaletic/Prog-Comp/Papers/soloway84.pdf
- **Type / status**：同行评审实证论文；全文已读。`read_status=fulltext_read; claim_status=two_studies_and_samples_checked`。
- **Method / sample**：两项程序理解研究；Study I 涉及 139 名学生程序员；Study II 涉及 41 名专业程序员。
- **Findings**：作者提出 programming plans 与 programming discourse rules；违反熟悉的计划／惯例会使程序更难理解。Study I 的一组正确表现约为 Alpha 88%、Beta 31%；Study II 首轮关键语句回忆约为 42% 对 24%。
- **Limits**：历史语言与受控程序片段研究，不是大型现代代码库维护实验；不能推出所有团队惯例都正确。
- **Relevance**：说明代码表达会影响读者预期和程序理解，为“代码优美与认知可达性可能有关”提供实证机制。

### ER-20261111-CA-K02 — Cognitive Dimensions of Notations

- **Source**：Thomas R. G. Green (1989). “Cognitive Dimensions of Notations.” In A. Sutcliffe and L. Macaulay (eds.), *People and Computers V*, Cambridge University Press, 443–460.
- **URL**：作者公开 PDF：https://www.cl.cam.ac.uk/~afb21/CognitiveDimensions/papers/Green1989.pdf
- **Type / status**：认知／HCI 理论框架；全文已读。`read_status=fulltext_read; claim_status=conceptual_dimensions_checked`。
- **Scope**：分析记法与使用环境如何影响可见性、隐藏依赖、黏滞性、过早承诺、角色表达性和困难的心智操作等。
- **Limits**：概念分析，不是经验证的代码评分量表；维度不是完全正交的自然常数。
- **Relevance**：帮助把“清晰、难懂、别扭”转成可研究的认知变量，而非直接等同于审美分数。

### ER-20261111-CA-K03 — Comprehension Strategies in Programming

- **Source**：Nancy Pennington (1987). “Comprehension Strategies in Programming.” In G. M. Olson, S. Sheppard, and E. Soloway (eds.), *Empirical Studies of Programmers: Second Workshop*, Ablex, 100–113.
- **URL**：SEI 注释书目摘要：https://www.sei.cmu.edu/documents/1557/1990_011_001_15824.pdf ；书目记录：https://cir.nii.ac.jp/crid/1571135651216799360?lang=en
- **Type / status**：程序理解研究章节；本轮仅读取二手注释书目摘要和书目元数据，未取得原章全文。`read_status=secondary_summary_only; claim_status=summary_only`。
- **Reported method / sample**：SEI 摘要称研究包含 40 名专业程序员，阅读并修改一个中等长度程序，分析 think-aloud 与程序理解表现。
- **Reported finding**：高理解表现者倾向于同时参照 program model 与 domain model。
- **Limits**：当前仅二手摘要，不将其当作原文全文证据；后续若作为核心论据，应取得原章节或相关期刊论文全文。
- **Relevance**：为程序模型与业务领域模型的交叉理解提供研究线索。
