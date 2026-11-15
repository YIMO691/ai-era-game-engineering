---
title: 代码优美论 Batch 01 — 核心文献注释书目
created_at: 2026-11-11
version: "0.3-audit"
baseline: "0.2.1"
audit_result: PARTIAL
status: cross-checked-draft-with-explicit-limits
tags: [code-aesthetics, bibliography, batch01]
---

# 核心文献注释书目

> [!WARNING]
> 公开研究草案：Batch01-B仍为PARTIAL，人工研究审核pending，代码／参与者实验未执行。公开提交授权不等于研究通过。
> 文内“未发布”、本地文件名、行号和检查点属于原研究时点；本页已作公开目录与链接适配，不是字节保真档案。当前阅读顺序与发布边界见[课题入口](../README.md)。


> [!WARNING] Batch01-B 当前独立证据层
> 下文v0.2.1阅读声明和条目状态均为Batch01-A历史记录；本轮不能继承。A01/A02/A03/L01/Q01/Q02/I02/I03/I04/K01/K02/K03的独立访问状态均为NOT_ACCESSIBLE，搜索仅作发现。36项是来源登记数，不是本轮核验通过数。具体判断以 [12_Batch01-B核心论断证据审校](../audit/claim-evidence-matrix.md)、[sources](../evidence/sources.md) 的Batch01-B状态表为准。
>
> **A02**：保留前轮0.33与0.0961两条记录，集合／中位数定义／平方顺序待核，不能直接互推或把0.33改为0.31。美学可作为单独操作化的候选构念，不等于已具判别效度或统计独立。**A03**：Git身份数不自动等于去重自然人数；分类是理论发展材料，不是完整因果理论验证。
>
> **Q01/Q02**：Time-in-Development的起止、单位与两个模型各自N待核；低R²不代表零关联或可计算ROI。九项产品质量术语、采用版条款及工作译名尚未独立确认，不把采用版当ISO官方全文。**I02/I03/I04**：时间、任务数量、质量分别判断；I03选择偏差方向暂不确定。I04的26.08%须补ITT/IV/LATE、采用定义、标准化分母和合并权重；不把样本总数视作采用者人数。SE原写法10.3%保留，但不能仅由%断言百分点解释在任何尺度下都错；不将其理解为26.08%的10.3%。工作稿不能默认等同正式版。
>
> **K01/K02/K03**：88%/31%与42%/24%的分母、子组、任务、轮次未核；94/45只是经验分层检索线索，不是Alpha/Beta条件人数。六维逐项归于Green1989尚未确认；不判定已混入后版。Pennington原章与SEI条目均未取得，作者摘要／编者评论和模型术语归属待核。详见 [08_认知科学与程序理解补充研究](cognition.md)。只补这些承重缺口，不要求重做全书目。

> [!NOTE] v0.2.1 阅读状态说明
> 本书目已按 Batch01-A 原文核验记录与来源账本重新同步。36 项来源不等于 36 篇全文已读论文：A01、A02、A03、L01、Q01、I02、K01、K02 已读论文全文／作者稿；I04 读工作论文全文并核对正式出版元数据与在线附录；Q02 仅核对 ISO 官方元数据及公开采用版文本；A04 为定点阅读；K03 为二手摘要。唯一权威状态以 [sources](../evidence/sources.md) 的 `read_status` 为准。

## 阅读优先级与剩余缺口

- **已完成承重原文核验**：A01、A02、A03、L01、Q01、I02；其方法、样本与限制已进入下文和 [07_Batch01-A核心文献原文核验与证据修订记录](../history/batch01-a-verification.md)。
- **部分核验／仍有版本边界**：Q02（未取得 ISO 官方付费原版）；I04（工作论文全文＋正式出版元数据和在线附录，尚未逐页比较最终版与工作论文）；A04（定点章节）；K03（二手摘要）。
- **仍待按研究问题补读**：L02、L06—L09、Q03—Q11、C01/C02、I01、A05—A07、K03 等；具体以每项 `read_status` 为准。
- 不重做宽泛检索；Batch01-B已发现的承重口径与独立核验缺口仍须定点回到原文，不能因前轮已读声明跳过。具体启动门见 [15_Batch02研究启动条件](../batch02/entry-gates.md)。

短编号对应 `ER-20261111-CA-` 前缀。正式证据登记按ID合并同一论文多个版本，不计为独立复制。

## 一、代码美学与工艺

### A01 · Fedorova, Mazmanian & Dourish：美学作为编程实践

**书目**：Marina Fedorova, Melissa Mazmanian, Paul Dourish. *Coding Beauty and Decoding Ugliness: The Role of Aesthetic Concerns in Programming Practices*. *Science, Technology, & Human Values* **50(1):69–93 (2025)**；online-first **2024-04-15**。两日期指同一研究。

**DOI／原文**：[10.1177/01622439241245746](https://doi.org/10.1177/01622439241245746)；[SAGE PDF](https://journals.sagepub.com/doi/pdf/10.1177/01622439241245746)。

- **方法／样本**：2014 年在 Yandex 莫斯科总部开展三个月密集定性田野工作；26 次俄语半结构化深度开发者访谈，另有 4 次管理者专家访谈及多日工作场所观察。访谈持续 1–4 小时，录音、转录并由作者翻译。研究者最初没有把代码美学作为访谈中心问题，是在受访者反复提及 beautiful / ugly 后才加入追问。
- **主要发现**：组织内不存在单一、统一的 beautiful code 定义；开发者可以保留不同审美理想。与此同时，参与者对多种 ugly code 形成了较共享的识别方式；作者将“not ugly”解释为该组织中可接受代码的默认类别，不在此断言正式准入规章。审美语言既维持专业背景多样性，也推动代码风格与实践趋同，并参与新人社会化。
- **价值**：把代码美学从个人口味和格式规范扩展为代码评审、团队协作、专业身份和组织治理中的实践。
- **局限／不可推出**：单一公司、单一时期的定性组织研究；不是风格随机实验，不测量缺陷率、维护成本或代码质量的因果改善；不能据此制定跨组织的统一审美规则。
- **Batch01-A历史状态**：`fulltext_read`；方法、主要发现与研究边界已核验。

### A02 · Coleman：美学指标与可读性模型

**书目**：Ron Coleman (2018). *Aesthetics Versus Readability of Source Code*. *International Journal of Advanced Computer Science and Applications* **9(9)**。

**DOI／原文**：[10.14569/IJACSA.2018.090902](https://doi.org/10.14569/IJACSA.2018.090902)；[期刊 PDF](https://thesai.org/Downloads/Volume9No9/Paper_2-Aesthetics_versus_Readability_of_Source_Code.pdf)。

- **方法／样本**：测试语料来自 GNU Core Utilities 的 114 个开源程序，原始规模近 70,000 LOC；去除编译／预处理指令、原型、typedef 等内容后，形成 **1,043 个单函数 C 文件、约 53,000 LOC**。作者为每个文件计算 11 个 beauty factors 与 8 个 readability scores，构成 11×8 相关矩阵；因分布非正态而采用 Spearman’s rho。
- **主要发现**：作者报告显著相关的绝对 Spearman 相关系数范围约为 \(|ρ|=0.05\) 至 \(0.59\)，没有强相关；论文进一步报告其中位相关平方值为 0.0961，并据此主张 beauty 与 readability 不是可互相替代的代理变量。
- **价值**：提醒研究者区分“美学代理指标”和“可读性代理指标”，不能把可读性模型当作代码美学的完整测量。
- **局限／不可推出**：beauty factor 是作者构造的特定形式／分形维度代理，不是参与者对代码美感的直接评分；语料来自单一 C 项目，不含真实维护者理解、缺陷定位或修改任务实验。Spearman ρ²是秩相关平方，不能直接解释为原尺度美学指标中由可读性解释的方差比例；即使回归R²也不自动具有因果解释。该研究不能证明美学与真实维护绩效独立。
- **Batch01-A历史状态**：`fulltext_read`；样本构造、指标、统计方法和限制已核验。

### A03 · Sundelin 等：软件工艺的解剖分类

**书目**：Anders Sundelin, Javier Gonzalez-Huerta, Krzysztof Wnuk, Tony Gorschek (2022). *Towards an Anatomy of Software Craftsmanship*. *ACM Transactions on Software Engineering and Methodology* **31(1), Article 6**。

**DOI／原文**：[10.1145/3468504](https://doi.org/10.1145/3468504)；[作者公开稿 PDF](https://anders.sundelinkarlskrona.se/wp-content/uploads/2021/06/TowardsAnAnatomyOfSoftwareCraftsmanship-authorCopy.pdf)。作者稿文件名／内部页眉保留早期占位元数据，正式出版记录应以 ACM DOI 与 2022 年卷期为准。

- **文献方法**：作者于 2018 年 12 月在 Google Scholar 搜索得到 980 条结果；按两项标准排除 522 与 346 条，留下 112 篇候选；以 4 篇数据库种子论文起步，再依据研究者经验和推荐增加 5 篇种子；进行四轮前向／后向 snowballing，最终纳入 18 篇论文和 11 本书。
- **工业案例**：Ericsson 一个金融科技产品约七年的纵向案例（2009–2016，约 20 个全球部署）。研究期内报告按 Git Author tag 识别155个贡献者身份（自然人去重口径待核）；这不是访谈人数。案例访谈为 6 名参与者，另结合版本控制、文档、需求和缺陷报告等档案材料。第一作者曾是该项目开发者，存在 insider perspective。
- **主要发现**：归纳四个主题、17 项原则和 47 项层级实践：价值导向架构（3 原则／10 实践）、迭代设计开发与验证（3／10）、共享专业文化（6／18）、反馈（5／9）。
- **价值**：把软件工艺从“程序员写码态度”扩展为架构、迭代、测试、团队文化、责任与反馈的社会—技术实践地图。
- **局限／不可推出**：单一产品／组织案例；研究并未逐条随机验证 17 项原则的因果效果；155 是 Git 作者标签计数，6 才是案例访谈参与者；47 项实践不能直接转化为所有项目的强制清单。
- **Batch01-A历史状态**：`fulltext_read_author_copy`；方法、案例、分类及威胁已核验。作者稿中的 2020 占位页眉不是正式出版年份。

### A04 · Sundelin：量化工艺概念的博士论文

**书目**：Anders Sundelin (2025). *On Quantifying Software Craftsmanship Concepts*. 博士论文，Blekinge Institute of Technology，Doctoral Dissertation Series No. 2025:12。

**原文**：[BTH/DiVA 全文 PDF](https://bth.diva-portal.org/smash/get/diva2%3A1997635/FULLTEXT01.pdf)。

- **方法／范围**：本轮未对整篇论文及其全部组成研究进行完整逐章阅读；对与 A03 及 AI/LLM 研究议程相关的章节作了定点阅读。
- **已核验内容**：论文包含软件工艺概念量化研究；关于云迁移与 LLM/AI 对软件工艺的影响，属于未来研究议程，不是已经完成的 AI 影响实证。
- **价值**：追踪软件工艺从概念分类走向量化研究的后续发展，并提示 AI 对专业工艺的影响仍是开放问题。
- **局限**：不能因论文题名含 Quantifying 就声称软件工艺已有完整客观评分；不能将 Future Work 当成研究发现。
- **Batch01-A历史状态**：`targeted_read`；只确认相关章节，不宣称整篇论文已读。

### A05—A07 · 宣言与品质动机：不是效果试验

| ID／书目 | 原始入口 | 方法／材料 | 用途与边界 | 本轮状态 |
|---|---|---|---|---|
| A05 · Software Craftsmanship 社区，*Manifesto for Software Craftsmanship*（2009） | [官方宣言](https://manifesto.softwarecraftsmanship.org/) | 集体规范性声明，无实验样本 | “not only working software, but also well-crafted software”把做工品质加入价值关注；签署不是有效性验证 | `official_text_crosschecked` |
| A06 · Agile Manifesto 作者群，*Principles behind the Agile Manifesto*（2001） | [官方原则](https://agilemanifesto.org/principles.html) | 规范性文本，无实验样本 | 用于核对技术卓越、简洁与敏捷价值的关系；不等于完成 XP 历史考证 | `official_page_read` |
| A07 · Richard Sennett，*The Craftsman*，Yale University Press（2008） | [Yale 书页](https://yalebooks.yale.edu/book/9780300151190/the-craftsman/) | 理论专著，未阅读全文 | 工艺内在动机的理论入口；出版社书目不能代替原书论证 | `access_failed` |

## 二、精益制造、产品开发与软件工程

### L01 · Pernstål, Feldt & Gorschek：The Lean Gap

**书目**：Joakim Pernstål, Robert Feldt, Tony Gorschek (2013). *The Lean Gap: A Review of Lean Approaches to Large-Scale Software Systems Development*. *Journal of Systems and Software* **86(11):2797–2821**。

**DOI／原文**：[10.1016/j.jss.2013.06.035](https://doi.org/10.1016/j.jss.2013.06.035)；[Chalmers 作者机构 PDF](https://gorschek.com/wp-content/uploads/2019/11/The-lean-gap-A-review-of-lean-approaches-to-large-scale-software-systems-development.pdf)。

- **方法／范围**：系统性映射研究（SMS）。五个数据库在 **2011-02-05** 检索；方法部分 Table 2／§3.2 写发表年份范围为 **1990–2010**，但结果段 §3.3 又写成 **1990–2011**。这是原文内部不一致，本书目保留冲突，不擅自把其中一处改成确定事实。
- **筛选数字**：初始 13,984 条；去重 3,754 条后剩 10,230 条；标题／关键词／摘要筛选排除 10,176 条，余 54 条；再排除 16 条（全文不可得、重复报告或主题不清），最终纳入 38 篇。
- **主要发现**：16/38（约 42%）明确涉及大型软件开发；76% 被分类为非实证研究；9/38（约 24%）属于 evaluation 或 validation research；16 项大型开发研究中只有 4 项为实证研究。两轮筛选试点的 Fleiss’ Kappa 从 0.50 提高到 0.74。
- **价值**：为制造业精益思想迁移到大型软件工程设置证据边界；支持“迁移原则并验证机制”，不支持机械照搬 TPS。
- **局限／不可推出**：38 是论文数量，不是 38 个独立现场实验；76% 不是失败率；42% 不是成功率。该研究只描述其检索范围与时期，不能代表 2026 年现状。
- **Batch01-A历史状态**：`fulltext_read`；方法、筛选流程、样本统计与质量评估已核验。

### L02 · Poppendieck & Poppendieck：软件精益的实践框架

**书目**：Mary Poppendieck, Tom Poppendieck (2003). *Lean Software Development: An Agile Toolkit*. 第1版，Addison-Wesley Professional。ISBN **9780321150783**；未核到DOI。

**原文**：[InformIT出版商记录](https://www.informit.com/store/lean-software-development-an-agile-toolkit-9780321150783)。

- **方法／材料**：实践工具书；索引介绍七原则、22思考工具，不是22个效果实验。
- **重要定位**：第2章 *Amplify Learning*，第6章 *Build Integrity In*；不得用后来版本的措辞替换2003章名。
- **价值**：软件开发需要学习、整合与全局价值，不只是机械加快生产动作。
- **局限**：实践框架不能单独证明跨企业、跨规模的平均收益；目录和正文未直接读取。
- **状态**：`access_failed`。

### L03—L05 · 官方概念来源

| ID／来源 | 原始入口 | 已核验内容／用途 | 不能支持什么 | 本轮状态 |
|---|---|---|---|---|
| L03 · Toyota Motor Corporation，*Toyota Production System* | [官方 TPS](https://global.toyota/en/company/vision-and-philosophy/production-system/) | 官方页面说明 Jidoka 与 Just-in-Time 两支柱、异常停止与按需流动 | 软件测试门禁必然有效；满负荷或零缓冲就是精益 | `official_page_read` |
| L04 · W. Edwards Deming Institute，*PDSA Cycle* 与 FAQ | [PDSA](https://deming.org/explore/pdsa/)／[FAQ](https://deming.org/about-us/f-a-qs/) | 官方说明 Study 阶段强调预测、观察与学习 | “Deming 发明 PDCA”；PDSA 已被实证证明普遍优于 PDCA | `official_page_read` |
| L05 · American Society for Quality，*Total Quality Management (TQM)* | [ASQ](https://asq.org/quality-resources/total-quality-management) | 专业机构定义客户导向、全员参与和持续改进 | TQM 等于测试部门，或质量史是单向升级 | `official_page_read` |

### L06—L09 · 后续综述与迁移边界

| ID／书目 | DOI／入口 | 方法与样本（索引层级） | 用途与局限 |
|---|---|---|---|
| L06 · Martínez León、Farris，*Lean Product Development Research: Current State and Future Directions* (2011)；完整作者名、刊物卷页未核 | [10.1080/10429247.2011.11431885](https://doi.org/10.1080/10429247.2011.11431885) | 综述；索引称21年研究、七知识领域；纳入数未核 | 产品开发不能直接等同重复制造；未读方法，不能确认具体干预收益 |
| L07 · Eetu Kupiainen, Mika V. Mäntylä, Juha Itkonen，*Using metrics in Agile and Lean Software Development—A systematic literature review of industrial studies* (2015)，Information and Software Technology 62:143–163 | [10.1016/j.infsof.2015.02.005](https://doi.org/10.1016/j.infsof.2015.02.005) | 工业研究系统综述；纳入数未核 | 关注度量用途及效果；敏捷／精益混合范围，不是L01的严格更新 |
| L08 · Melanie Paz, Alonso Sasagawa, José Antonio Taquía Gutiérrez，*Systematic Literature Review of Lean Tools Applied to Software Development* (2022)，IEOM会议论文；正式会名页码未核 | [10.46254/EU05.20220448](https://doi.org/10.46254/EU05.20220448) | 索引称19篇；等待、Kanban与理解障碍线索 | 最常用不等于最有效；不能与L01的38篇比较出增长或退步 |
| L09 · Cukor Kirinić、Hegedić，*Trends and Future Research Direction of Lean Product Development* (2023)，Sustainability 15(24):16721；完整作者名与DOI未核 | [出版社入口](https://www.mdpi.com/2071-1050/15/24/16721) | 索引称2011—2022的85篇 | 产品开发研究线索，不证明大型软件精益证据已充分 |

L06/L07/L09为`discovered`，L08为`access_failed`；均未读正文。以上是有用补检入口，不为凑数量提升为承重证据。

## 三、质量工程、维护性与经济学

### Q01 · Borg 等：收益曲线不是投资定律

**书目**：Markus Borg, Ilyana Pruvost, Enys Mones, Adam Tornhill (2024). *Increasing, not Diminishing: Investigating the Returns of Highly Maintainable Code*. *Proceedings of the 7th ACM/IEEE International Conference on Technical Debt*, 21–30。

**DOI／原文**：[10.1145/3644384.3644471](https://doi.org/10.1145/3644384.3644471)；[arXiv 2401.13407](https://arxiv.org/abs/2401.13407)。

- **方法／样本**：观察性仓库挖掘与回归分析，合并两个公开数据集：CodeRed 39 个专有项目与 UOwns 40 个专有项目，共 79 个项目、46,211 个源代码文件、25 种语言。质量变量为 CodeScene Code Health；结果变量包括文件关联缺陷数和 Time-in-Development。
- **主要结果**：三次多项式模型对缺陷数的 \(R^2=0.038\)，对 Time-in-Development 的 \(R^2=0.006\)；作者明确指出模型没有解释很大比例的变异。价值创造曲线是基于模型输入和假设的推演，提出高质量区间的边际收益可能增强。
- **价值**：提示代码质量与缺陷、开发时间的关系可能非线性；质量改进值得用生命周期经济性研究，而不只看代码审美。
- **局限／不可推出**：观察性研究，不是重构干预实验；未直接计入每项重构成本、机会成本和因果净收益；Code Health 是特定工具构念，数据来自其客户项目。不能把模型曲线当成所有项目的真实 ROI，也不能推出“越追求完美越划算”。
- **Batch01-A历史状态**：`fulltext_read`；数据集、指标、回归表现、价值模型与局限已核验。

### Q02 · ISO/IEC 25010:2023：产品质量的参照，不是美学评分

**书目**：ISO/IEC (2023). *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*. **ISO/IEC 25010:2023**，第2版，2023-11-15。

**入口**：[ISO](https://www.iso.org/standard/78176.html)；[IEC](https://webstore.iec.ch/en/publication/90024)。未核到DOI，用标准号识别。

- **方法／样本**：规范性质量模型；不存在对应的效果实验样本。
- **已核验内容**：ISO 官方页面确认 2023 版标准元数据；九项产品质量特性名称通过公开的 GSO 采用版文本辅助核对。未取得 ISO 官方付费原版逐页阅读。
- **价值**：把“好”拆为可评价、会冲突的产品属性；避免以可维护性覆盖全部产品质量。
- **局限**：不能推出代码优美分数，也不保证全部质量属性有一个通用最优权重。security与safety应分别解释。
- **Batch01-A历史状态**：`official_metadata_plus_adoption_text`；不标记为 ISO 官方原版全文已读。

### Q03/Q04 · 两篇1972经典

| ID／书目 | DOI／原文 | 方法／材料 | 价值、局限与补读 |
|---|---|---|---|
| Q03 · D. L. Parnas，*On the Criteria To Be Used in Decomposing Systems into Modules* (1972)，CACM 15(12):1053–1058 | [10.1145/361598.361623](https://doi.org/10.1145/361598.361623) | 设计方案对照与机制论证，非规模化随机实验 | 围绕易变设计决策思考信息隐藏；不是模块越多越好。应读原始例子、评价维度和结论 |
| Q04 · Edsger W. Dijkstra，*The Humble Programmer* (1972)，CACM 15(10):859–866；EWD340 | [10.1145/355604.361591](https://doi.org/10.1145/355604.361591)／[大学档案](https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD340.html) | 图灵奖演讲，理论／历史论述；无实验样本 | 认知限制与专业纪律入口；不代替现代认知实验，不证明AI效果 |

Q03为`discovered`；Q04为`access_failed`。没有把转录索引说成原始论文已读。

### Q05—Q07/Q09 · 重构与债务的原始实践文本

| ID／书目 | 入口 | 核心用途 | 局限与状态 |
|---|---|---|---|
| Q05 · Martin Fowler (2004-09-01)，*Definition Of Refactoring* | [定义](https://martinfowler.com/bliki/DefinitionOfRefactoring.html) | 保持可观察行为的结构改进；区分重构和一般重写 | 实践定义，无实验样本／DOI；discovered，不能凭定义确认某次改动无回归 |
| Q06 · Martin Fowler (2009-10-14)，*Technical Debt Quadrant* | [债务象限](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) | 审慎／鲁莽、有意／无意（deliberate/inadvertent）的分类 | 解释模型，不是统一货币化公式；discovered |
| Q07 · Martin Fowler，*Workflows of Refactoring*，网页年份未核 | [工作方式](https://martinfowler.com/articles/workflowsOfRefactoring/fallback.html) | 使后续工作更快，经济动机与停止条件 | 经验指导，不覆盖安全义务的全部理由；discovered；无DOI |
| Q09 · Ward Cunningham (1992)，*The WyCash Portfolio Management System*，OOPSLA ’92 Addendum:29–30 | [作者版](https://c2.com/doc/oopsla92.html)／[10.1145/157709.157715](https://doi.org/10.1145/157709.157715) | 工业经验报告，技术债隐喻的原始入口 | 单一系统经验不是通用债务利率；discovered；不混用期刊再版信息 |

### Q08 · Kaur & Singh：重构效果的异质性

**书目**：Satnam Kaur, Paramvir Singh (2019). *How does object-oriented code refactoring influence software quality? Research landscape and challenges*. Journal of Systems and Software **157:110394**。

**DOI／原文**：[10.1016/j.jss.2019.110394](https://doi.org/10.1016/j.jss.2019.110394)；[arXiv 1908.05399](https://arxiv.org/abs/1908.05399)。

- **方法／样本**：系统映射；摘要索引报告142项实证研究。
- **候选发现**：质量属性的改善并不一致，学术环境与工业环境结果存在差异。
- **价值**：为“重构次数更多不等于质量更好”提供反方研究入口。
- **局限**：未核各属性方向、效应、研究质量与选择条件；不能把不一致改写为重构通常有害。
- **状态**：`discovered`；重点补读分类、工业样本和不利结果。

### Q10/Q11 · 实践建议与可读性测量是不同证据

| ID／书目 | 入口 | 方法／条件 | 价值与限制 |
|---|---|---|---|
| Q10 · Robert C. Martin，*Clean Code: A Handbook of Agile Software Craftsmanship*，2008，第1版，Prentice Hall/Pearson；ISBN9780132350884 | [出版社](https://www.pearson.com/en-us/subject-catalog/p/clean-code-a-handbook-of-agile-software-craftsmanship/P200000009044) | 实践著作与示例；本轮仅书目，未读案例 | 研究工艺表达，不把规则当实验结论；2008发行与2009版权区分；无DOI |
| Q11 · Raymond P. L. Buse, Westley R. Weimer (2010)，*Learning a Metric for Code Readability*，IEEE TSE 36(4):546–558 | [10.1109/TSE.2009.70](https://doi.org/10.1109/TSE.2009.70)／[作者稿](https://web.eecs.umich.edu/~weimerw/p/weimer-tse2010-readability-preprint.pdf) | 索引报告120名人类标注者及局部代码特征建模；分割与量表未核 | 评价标签可量化；预测标签不能直接代替任务理解和维护收益 |

两项均`discovered`；Q11的预测效果数值未采用。

## 四、国内研究入口

### C01 · 代码坏味研究综述

**书目**：田迎晨、李柯君、王太明、焦青青、李光杰、张宇霞、刘辉 (2023)，《代码坏味研究综述》，《软件学报》**34(1):150–170**。

**DOI／入口**：[10.13328/j.cnki.jos.006431](https://doi.org/10.13328/j.cnki.jos.006431)；[官方期刊目录](https://www.jos.org.cn/jos/article/issue/2023_34_1)。

- **方法／样本**：摘要索引报告分析1990年至2020年6月间339篇相关论文。
- **价值**：国内坏味研究、趋势、学术／工业关注差异的系统入口。
- **局限**：纳入与分类方法未读；截止2020年不代表2026；不能把检测坏味直接等同已证明缺陷。
- **状态**：`access_failed`；CNKI直接详情未取得，不能说完成CNKI系统检索。

### C02 · 程序理解：现状与未来

**书目**：金芝、刘芳、李戈 (2019)，《程序理解:现状与未来》，《软件学报》**30(1):110–126**；索引称2018-11-20网络发表。DOI本轮未核，不按网页编号推造。

**入口**：[期刊HTML](https://www.jos.org.cn/html/2019/1/5643.htm)。

- **方法／材料**：综述，认知、方法与软件工程角度，静态／动态分析及学习技术；纳入数与完整筛选方法未知。
- **价值**：将“读得顺”转为程序理解问题，而非简单句法偏好。
- **局限**：本轮仅官方索引，不借综述标题证明任何具体代码风格更好。
- **状态**：`discovered`。

## 五、AI时代：支持、反例与更新

### I01 · Peng等：受控任务中的加速

**书目**：Sida Peng, Eirini Kalliamvakou, Peter Cihon, Mert Demirer (2023). *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*. arXiv预印本。

**DOI／入口**：[10.48550/arXiv.2302.06590](https://doi.org/10.48550/arXiv.2302.06590)。

- **方法／条件**：受控JavaScript HTTP服务器实现任务；样本人数、退出和精确估计口径未核。
- **结果线索**：摘要称AI组完成“55.8% faster”；本版不再转换为另一百分比。
- **用途／局限**：支持特定实现任务可加速；不测得全生命周期质量收益，须关注工具供应商参与及独立复制。
- **状态**：`discovered`；正文方法未读。

### I02 · Becker 等：熟悉仓库中的减速

**书目**：Joel Becker, Nate Rush, **Beth Barnes**, David Rein (2025). *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*. METR 研究论文／arXiv 预印本。

**DOI／入口**：[10.48550/arXiv.2507.09089](https://doi.org/10.48550/arXiv.2507.09089)；[METR 论文 PDF](https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf)；[METR 研究说明](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)。

- **方法／样本**：随机对照任务实验；16 名经验丰富的开源开发者在自己长期熟悉的成熟仓库中完成 246 项真实任务。任务随机分配为允许或不允许使用当时的 AI 工具；允许使用时主要为 Cursor Pro 与 Claude 3.5/3.7 Sonnet。
- **主要结果（前轮转述，本轮未复核）**：任务完成时间效应估计约增加19%，所记区间约2%–39%；估计方法、变换尺度、聚类和区间构造待原文确认，不直接称算术平均效应。处理条件是允许使用AI，不等于实际使用；时间增加19%不等于生产率下降19%。
- **作者元数据说明（前轮记录）**：来包记METR PDF及博客为“Beth Barnes”、arXiv元数据为“Elizabeth Barnes”；本轮未直接复核这些载体，暂保留前轮署名，不宣称已证明两种写法的身份关系。
- **价值（条件性）**：若所报方法与减速结果成立，可构成“所有真实开发任务必然提速”的情境性反例；不能仅凭与另一研究不同，就识别熟悉度、任务或版本各自的因果作用。
- **局限／不可推出**：样本小、熟悉仓库、工具属于早期 2025；不能外推到所有开发者、任务或 2026 agentic coding；时间增加不等于代码质量下降。
- **Batch01-A历史状态**：`fulltext_read`；论文 PDF、设计、样本、区间与限制已核验。

### I03 · METR：后续研究的选择与测量问题

**书目**：METR (2026-02-24). *We are Changing our Developer Productivity Experiment Design*。机构研究更新，无已核 DOI。

**入口**：[METR 更新](https://metr.org/blog/2026-02-24-uplift-update/)。

- **方法／内容（前轮转述）**：官方研究更新讨论选择与测量问题并调整设计。本轮未取得正文；任务不提交、参与者退出与计时机制的方向和幅度均待核，不断言样本必然偏向AI适用场景。
- **价值**：提醒读者不要把早期实验数字当作跨工具、跨时期的永久常数；评估方法本身也需要持续校准。
- **局限／不可推出**：该更新不直接证明新工具普遍加速，也不能简单替换 2025 年实验在其原始条件下的观察结果。
- **Batch01-A历史状态**：`official_page_read`；官方方法更新正文已核对。

### I04 · Cui 等：现场实验补充

**书目**：Kevin Zheyuan Cui, Mert Demirer, Sonia Jaffe, Leon Musolff, Sida Peng, Tobias Salz (2026). *The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers*. *Management Science* **72(11):9408–9420**；published online **2026-02-27**。

**入口／DOI**：[10.1287/mnsc.2025.00535](https://doi.org/10.1287/mnsc.2025.00535)；[INFORMS 正式出版页](https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535)；[在线附录](https://pubsonline.informs.org/doi/suppl/10.1287/mnsc.2025.00535/suppl_file/mnsc.2025.00535.sm1.pdf)；[作者工作论文](https://doi.org/10.2139/ssrn.4945566)。

- **方法／样本**：Microsoft、Accenture 和一家匿名 Fortune 100 企业开展三组现场随机实验；合并样本 4,867 名开发者。公司在正常业务过程中随机向一部分开发者提供可建议代码补全的 AI 助手访问权限。
- **主要结果（前轮转录，本轮未直接取得摘要）**：来包记合并“completed tasks”增加 **26.08%（standard error: 10.3%）**，并记经验较少者采用率及收益更高。26.08%究竟对应ITT还是IV/LATE、采用定义、标准化分母、合并权重和版本均待核；不能仅因随机给权限就断言主结果是全体开发者的ITT。
- **标准误释义**：保留10.3%是忠实转录政策，不由百分号判定所有“百分点”表达数学错误。若效应及SE原尺度为.2608和.103，乘100后同为26.08和10.3；这不等于完成率增加26.08个百分点，也不表示SE是26.08%的10.3%。不补造论文未核的置信区间。
- **版本说明**：Batch01-A历史记录称读过作者工作论文、最终出版页及附录；Batch01-B均未直接取得，不能继承为本轮已读。工作稿与正式版的承重差异仍待比对。
- **价值（条件性）**：若所报结果与方法获核实，可作为特定企业环境下的正向产出证据，与METR形成情境对照；不作为本轮已认证的普遍生产力收益。
- **局限／不可推出**：任务完成数量不是代码质量、可维护性、架构质量或安全性；研究工具是代码补全助手，不等于完整 agentic coding 工作流；不能把特定场景下的产出变化解释为 AI 自动提高工程品质。
- **Batch01-A历史状态**：`fulltext_read_working_paper_plus_final_metadata`；工作论文全文、正式元数据与在线附录已核验。

## 六、纳入、暂缓和反证原则

1. 未找到的“Assessing the Quality Impact of Refactoring”精确题名不进入书目；以已定位的Q08替代相关研究问题，不伪造匹配。
2. Fedorova的2024 online与2025卷期、Sundelin的文章与博士论文收录、AI论文的预印本与正式版本均不重复计算为独立研究。
3. 所有无法确定的中文译名、作者全名、出版年份、DOI或样本都留缺口；不是为了形式完整而猜填。
4. 负结果、不一致结果、方法更新和实践停止条件与支持材料同列，而不是放到不可见的附录。
5. 补核顺序由结论承重程度决定，不由引用次数、知名度或“是否支持代码优美论”决定。

返回 [00_研究包说明与阅读导航](../README.md)；下一步 [05_Batch02研究问题与计划](../batch02/research-plan.md)。

## Batch01-A 原文补读与书目修订（历史记录）

下表只转录前轮阅读自述，不是当前核验结果。A01的26是次数还是去重人数、A03的155个Git身份如何去重，均按12保留待核；不能从该历史表恢复“当前已通过”。

| ID | 文献 | Batch01-A报告的读取状态 | 前轮所记内容与边界（本轮未认证） |
|---|---|---|---|
| A01 | Fedorova et al. (2025 issue) | SAGE PDF 全文 | 2014 年 Yandex 莫斯科三个月田野；26 名开发者访谈、4 次管理者专家访谈；多元美学与共享“丑陋”识别；不测量质量因果 |
| A02 | Coleman (2018) | 期刊 PDF 全文 | GNU Coreutils 114 个程序；1,043 个单函数 C 文件、约 53,000 LOC；11 个 beauty factors × 8 个 readability scores；Spearman 相关及代理指标限制 |
| A03 | Sundelin et al. (2022) | 作者公开稿全文 | 980 条初始搜索结果、112 候选、9 个起始种子、四轮 snowballing；18 篇论文、11 本书；七年 Ericsson 案例、155 Git 作者、6 名访谈参与者 |
| A04 | Sundelin (2025) | 相关章节定点阅读 | AI/LLM 是未来研究议程，不是 AI 影响实证 |
| L01 | Pernstål et al. (2013) | 作者机构 PDF 全文 | 38 篇纳入、16 篇大型开发、76% 非实证；原文年份窗口存在 1990–2010 与 1990–2011 的内部不一致，检索日为 2011-02-05 |
| Q01 | Borg et al. (2024) | arXiv 全文；ACM 元数据交叉核对 | 79 个专有项目、46,211 个源文件、25 种语言；缺陷与 Time-in-Development 模型 \(R^2\) 约 0.038 和 0.006；价值模型不是重构 ROI 实验 |
| Q02 | ISO/IEC 25010:2023 | ISO 官方元数据 + GSO 采用版公开文本 | 九项产品质量特性；不是代码美学评分；ISO 官方付费原版未逐页读取 |
| I02 | METR (2025) | 论文 PDF 全文 | 16 名开发者、246 项任务；允许 AI 的任务完成时间增加约 19%，95% 区间约 2%–39%；作者名元数据有 Beth／Elizabeth 差异 |
| I03 | METR (2026) | 官方方法更新全文 | 后续研究存在选择与测量问题，不能简单替换早期实验 |
| I04 | Cui et al. (2026) | 作者工作论文全文 + INFORMS 最终元数据与在线附录 | 4,867 人、完成任务增加 26.08%，官方摘要写 standard error 10.3%；最终版与工作论文尚未逐页差异审查 |
| K01 | Soloway & Ehrlich (1984) | IEEE 论文 PDF 全文 | 程序计划与表达惯例影响程序理解 |
| K02 | Green (1989) | 作者公开 PDF 全文 | Cognitive Dimensions 是分析工具，不是代码评分量表 |
| K03 | Pennington (1987) | SEI 二手注释摘要 | 原章未取得，保持 partial |

当前独立访问状态以 [sources](../evidence/sources.md) 的Batch01-B层为准；正文历史read_status不升级为本轮阅读。其余24项未纳入本轮重点复核。不得将作者稿、预印本、工作论文、正式卷期和在线发表年份混为独立研究，也不得把摘要中的产出指标解释为长期质量结果。
