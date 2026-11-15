---
title: Batch 01-A — 核心文献原文核验与证据修订记录
created_at: 2026-11-11
version: "0.2.1"
status: source-audit-completed-with-explicit-gaps
tags: [code-aesthetics, source-audit, batch01a]
---

# Batch 01-A：核心文献原文核验与证据修订记录

> [!WARNING]
> 公开研究草案：Batch01-B仍为PARTIAL，人工研究审核pending，代码／参与者实验未执行。公开提交授权不等于研究通过。
> 本文件是历史记录，其中已读／通过／归档声明不代表当前独立核验。
> 文内“未发布”、本地文件名、行号和检查点属于原研究时点；本页已作公开目录与链接适配，不是字节保真档案。当前阅读顺序与发布边界见[课题入口](../README.md)。


> [!success] 本批已完成定点原文核验
> 与 v0.1 不同，本版已经直接读取多篇论文全文、作者稿或机构原始页面。**这不等于所有登记来源都已全文阅读，也不等于完成系统综述或实验验证。** 每项来源的实际阅读范围见 [sources](../evidence/sources.md)。

## 0. 本批完成范围

目标是修正 v0.1 中最影响结论强度的证据缺口，而不是扩大文献数量。

| 核心来源 | 本次实际读取 | 当前状态 | 可支持的结论 |
|---|---|---|---|
| A01 Coding Beauty and Decoding Ugliness | SAGE 公开 PDF 全文 | `fulltext_read` | 代码美学判断具有社会与组织语境；不提供客观美学分数 |
| A03 Towards an Anatomy of Software Craftsmanship | 作者公开稿全文；BTH 论文元数据与摘要交叉核对 | `fulltext_read_author_copy` | 可准确描述四主题、17原则、47实践及其形成方法 |
| L01 The Lean Gap | 作者机构公开 PDF 全文 | `fulltext_read` | 可准确描述 2013 年研究范围、筛选和证据缺口 |
| Q01 Increasing, not Diminishing | arXiv HTML 全文；ACM 最终出版元数据交叉核对 | `fulltext_read_preprint` | 可描述样本、指标、回归和局限；不能称为真实重构 ROI 实验 |
| Q02 ISO/IEC 25010:2023 | ISO 官方标准产品页；GSO 对 ISO 2023 的采用版公开预览 | `official_metadata_plus_adoption_text` | 可核对九项产品质量特性；没有逐页阅读 ISO 官方付费原版 |
| I04 Cui et al. 三组现场实验 | 作者工作论文全文、INFORMS 最终出版页、在线附录 | `fulltext_read_working_paper` | 可准确描述实验背景与主要结果；不等于长期代码质量提升 |
| A02 Aesthetics Versus Readability | 期刊公开 PDF 全文 | `fulltext_read` | 可审查其 beauty factor 的操作化及统计边界 |
| I02 METR 2025 | METR 公开论文 PDF 全文 | `fulltext_read` | 可描述特定专家熟悉仓库情境下的 19% 时间增加 |
| I03 METR 2026 update | METR 官方方法更新全文 | `official_page_read` | 后续研究存在自选择和测量问题，不能给出稳健通用提速值 |
| A04 Sundelin 2025 dissertation | 摘要、目录、Paper I、Future Work 相关章节定点阅读 | `targeted_read` | AI/LLM 是作者提出的未来研究问题，不是该论文的 AI 实证结果 |
| A05 Software Craftsmanship Manifesto | 官方页面搜索全文索引与原文镜像交叉核对；官方 SPA 页面未完整解析 | `official_text_crosschecked` | 可引用其规范性价值陈述，不是实证研究 |
| A06 Agile Principles | 官方原则页面全文 | `official_page_read` | Agile 原则本身已强调技术卓越、良好设计、简洁与反思 |
| L03 Toyota TPS | Toyota 官方页面全文 | `official_page_read` | 可准确说明 TPS 两大支柱及其官方释义 |
| L04 PDSA | Deming Institute 官方页面全文 | `official_page_read` | 可区分 Study 与 Check；不能据此单独完成历史起源考证 |
| L05 TQM | ASQ 官方说明全文 | `official_page_read` | 可描述 TQM 的组织层面原则和常见实施困难 |
| K01 Soloway & Ehrlich | IEEE 论文公开 PDF 全文 | `fulltext_read` | 计划知识与编程惯例会影响程序理解 |
| K02 Green Cognitive Dimensions | 作者公开 PDF 全文 | `fulltext_read` | 可用认知维度分析记法与环境；不是代码评分标准 |
| K03 Pennington | SEI 注释书目摘要与书目元数据 | `secondary_summary_only` | 可作为程序模型／领域模型交叉参照的研究线索，不能声称读过原章 |

**实验状态：** 本批没有招募参与者、没有运行用户实验、没有执行代码质量对照实验。原文阅读状态不等于实验完成。

---

## 1. A01：Coding Beauty and Decoding Ugliness

**书目：** Marina Fedorova, Melissa Mazmanian, Paul Dourish. “Coding Beauty and Decoding Ugliness: The Role of Aesthetic Concerns in Programming Practices.” *Science, Technology, & Human Values*, 50(1), 69–93, 2025；online first 2024-04-15。DOI: [10.1177/01622439241245746](https://doi.org/10.1177/01622439241245746)。

**原文：** [SAGE PDF](https://journals.sagepub.com/doi/pdf/10.1177/01622439241245746)。

### 方法核验

- 研究场景：Yandex 莫斯科办公室，2014 年开展约三个月的田野工作。
- 访谈：26 名程序员的半结构化访谈，另有 4 次面向管理者／专家的访谈；访谈以俄语进行并转录、翻译。
- 研究方式：访谈与现场观察相结合。研究者在初期访谈中发现“美／丑”反复出现后，才进一步把审美问题纳入访谈追问。
- 这是一项定性组织研究，不是代码质量基准实验，也没有随机分配不同代码风格来测量维护效率。

### 主要发现

1. 开发者对“美丽代码”的正面定义可以保持开放、多元甚至含糊。
2. “丑陋代码”的标签更容易被用于指出违反本地惯例、难以接受或不符合团队期望的实现。
3. 审美判断不仅是个人偏好，也参与团队规范、专业身份、代码审查和新成员融入。
4. “丑”可以成为沟通和协调工具，也可能成为权力、排斥或规范执行的手段。

### 对代码优美论的修正

- 不应假设存在一个跨语言、跨团队、跨文化的单一“美代码”标准。
- “团队觉得丑”不等于代码在行为正确性、缺陷率或维护成本上客观更差。
- 也不能把审美完全降为主观品味：团队审美实践会影响协作与知识传递。
- 后续研究应将**审美评价**与**理解／修改任务表现**分开测量，检验二者是否相关、何时相关。

### 证据边界

单一企业、单一时期、特定组织文化中的定性研究。它能解释审美判断如何在组织中运作，但不能估计其在整个软件行业的普遍比例，也不能证明某一审美规范必然提高产品质量。

---

## 2. A03：Towards an Anatomy of Software Craftsmanship

**书目：** Anders Sundelin, Javier Gonzalez-Huerta, Krzysztof Wnuk, Tony Gorschek. “Towards an Anatomy of Software Craftsmanship.” *ACM Transactions on Software Engineering and Methodology*, 31(1), Article 6, January 2022. DOI: [10.1145/3468504](https://doi.org/10.1145/3468504)。

**原文：** [作者公开稿 PDF](https://anders.sundelinkarlskrona.se/wp-content/uploads/2021/06/TowardsAnAnatomyOfSoftwareCraftsmanship-authorCopy.pdf)。公开稿页眉含有早期出版模板信息；最终卷期与 DOI 以 ACM／博士论文书目记录为准。

### 方法核验

**文献研究：**
- 2018 年 12 月在 Google Scholar 以 software craft / craftsmanship 等词检索，初始得到 980 条结果。
- 按语言、出版类型和是否实质讨论软件工艺等标准筛选，得到 112 篇候选。
- 从中选择 4 篇初始种子论文，再通过前向与后向 snowballing 扩展。
- 最终纳入 18 篇论文和 11 本书。
- 因此，这不是覆盖所有数据库的穷尽性系统检索；结论受种子文献、Google Scholar 和纳入标准影响。

**工业案例：**
- Ericsson 一个面向金融市场的软件产品，跟踪约七年。
- 产品在约 20 个安装环境中使用。
- 研究结合访谈、项目档案、版本控制、测试和开发过程材料。
- 作者参与过该产品开发，能够获得较深的内部资料，但这也要求读者注意研究者的 insider perspective。
- 论文将文献与案例材料通过主题编码综合，形成软件工艺“解剖图”。

### 结果：四主题、17 原则、47 层级实践

| 主题 | 原则编号 | 原则名称（英文原文／中文释义） |
|---|---|---|
| A. Value-focused architecture | A1 | Participating software architects：架构师参与并持续指导产品建设 |
|  | A2 | Encapsulation & separation of concerns：封装与关注点分离 |
|  | A3 | Clean, minimalistic code：清晰、克制、最小化的代码 |
| D. Iterative design, development, and verification | D1 | Incremental development：增量式开发 |
|  | D2 | Testing pyramid, layered testing：测试金字塔与分层测试 |
|  | D3 | Design documentation：设计文档与可执行文档 |
| C. Shared professional culture | C1 | Standard development environment：标准化开发环境 |
|  | C2 | Common professional culture：共同的专业文化 |
|  | C3 | Cross-team communication：跨团队沟通 |
|  | C4 | Visibility / Transparency：可见性与透明度 |
|  | C5 | Accountability：责任感与专业担当 |
|  | C6 | Culture of learning：学习文化 |
| F. Feedback | F1 | On-site customer (proxies)：现场客户／客户代理 |
|  | F2 | Short feedback loops：短反馈周期 |
|  | F3 | Reviews：评审 |
|  | F4 | Learning from feedback：从反馈中学习 |
|  | F5 | Continuous integration and tests：持续集成与测试 |

四组层级实践数量分别为 10、10、18、9，合计 47。实践是作者从文献与案例中归纳的层级条目，不应未经情境适配就变成所有团队的强制检查表。

### 重要的案例细节

- 案例中统一代码风格有助于不同分支之间合并、回移修复和理解代码。
- 工具链并非冻结不变：IDE、操作系统和构建工具随着实际需要演进，但迁移需要培训与协调成本。
- 测试既是安全网，也被当作行为规格和文档；随着测试数量增加，测试自身的结构、命名、稳定性和可读性变得重要。
- 跨团队架构组与 QA 组通过定期评审共享知识、发现遗漏。
- 可见的技术债务、待办和状态有助于协作，但可见不等于已经偿还。

### 关键限制

1. 单一组织、单一产品、特定金融软件场景，外部效度有限。
2. 作者是案例产品的参与者，内部视角增加了资料深度，也可能影响解释。
3. 六位访谈参与者及档案资料可用于三角验证，但不是大样本普遍性估计。
4. 研究的主要贡献是**概念分类与实践地图**，并没有通过对照组证明“实施这 17 条原则会因果性地提升质量或生产率”。
5. 作者提出的 47 项实践应作为研究与诊断入口，而不是成熟度打分表。

**对代码优美论的意义：** 这是最直接的工程实践基础。它将“做好软件”从个人写码风格扩展到架构、测试、团队文化、反馈和组织学习。

---

## 3. L01：The Lean Gap

**书目：** Joakim Pernstål, Robert Feldt, Tony Gorschek. “The Lean Gap: A Review of Lean Approaches to Large-Scale Software Systems Development.” *Journal of Systems and Software*, 86(11), 2797–2821, 2013. DOI: [10.1016/j.jss.2013.06.035](https://doi.org/10.1016/j.jss.2013.06.035)。

**原文：** [Chalmers 作者机构 PDF](https://gorschek.com/wp-content/uploads/2019/11/The-lean-gap-A-review-of-lean-approaches-to-large-scale-software-systems-development.pdf)。

### 方法与数字核验

- 检索范围：方法部分 Table 2／§3.2 写发表年份窗口 1990–2010；结果段 §3.3 又写 1990–2011，属于原文内部不一致。五个数据库检索日期均为 2011-02-05。
- 数据库：ACM Digital Library、IEEE Xplore、Inspec、ISI Web of Science、Scopus。
- 研究者报告初始检索 13,984 条，去重 3,754 条，得到 10,230 条候选；经过筛选后纳入 38 篇。
- 38 篇中，16 篇（42%）明确涉及大型软件开发。
- 76% 的论文被归类为非实证；只有 9/38（24%）被归类为 evaluation research 或 validation research。
- 在 16 篇大型开发研究中，作者指出只有 4 篇属于实证研究。
- 研究发现关注点主要集中于消除浪费和创造流程，而对其他精益产品开发原则、尤其跨部门互动的指导不足。

### 重要方法限制

- 原文年份范围存在 1990–2010 与 1990–2011 的内部不一致；数据库检索日为 2011-02-05。不能把该历史研究结果当作 2026 年的当前研究比例。
- 摘要筛选可能遗漏摘要没有体现的相关研究；作者也将其列为威胁。
- 研究者通过试筛和 Fleiss’ kappa 改进一致性：第一次 0.5，修订后第二次 0.76。
- 论文指出部分研究缺少研究设计、情境和限制说明。
- “76% 非实证”不等于“76% 研究失败”，而是研究类型分类结果。

### 对本研究的意义

这篇论文最重要的价值是给制造业类比设置证据边界：精益思想可以启发软件开发，但不能因为 TPS 在制造业有效，就断言某个精益软件实践在大型复杂系统中必然有效。迁移需要明确机制、组织情境、测量指标和失败信号。

---

## 4. Q01：Increasing, not Diminishing

**书目：** Markus Borg, Ilyana Pruvost, Enys Mones, Adam Tornhill. “Increasing, not Diminishing: Investigating the Returns of Highly Maintainable Code.” *Proceedings of the 7th ACM/IEEE International Conference on Technical Debt (TechDebt 2024)*, 2024, 21–30. 最终 DOI：[10.1145/3644384.3644471](https://doi.org/10.1145/3644384.3644471)。

**全文：** [arXiv HTML](https://arxiv.org/html/2401.13407)；[arXiv PDF](https://arxiv.org/pdf/2401.13407)。

### 数据与指标核验

- 数据来自两个工业数据集，合计 79 个专有软件项目、46,211 个源文件，涉及 25 种编程语言。
- 研究以文件为分析单位，使用 Code Health 等维护健康度指标，考察缺陷数量和实现时间等结果。
- 作者报告的回归模型解释力较低：缺陷模型 \(R^2=0.038\)，实现时间模型 \(R^2=0.006\)。
- 论文随后构建价值创造模型，讨论高维护健康区间的潜在价值。

### 必须修正的过度解读

这不是随机分配重构投资的实验，也没有直接观察团队把某段代码从低质量改到高质量后，实际节省了多少生命周期成本。

因此：
- 相关性不等于因果。
- “高质量区间可能有更高边际价值”是模型推演，不是已测得的普遍 ROI 曲线。
- 不能把回归模型解释力很低的结果描述成质量指标能够准确预测缺陷或开发时间。
- Code Health 是特定工具体系下的代理指标，不能代表完整代码美学。
- 数据来自特定工具客户项目，存在选择与未观测混杂风险。

### 元数据纠错

arXiv HTML 元数据中可见一条旧 DOI 字符串；本包以最终 ACM 会议记录的 DOI `10.1145/3644384.3644471` 为正式引用。不同版本的 DOI 元数据不可混用。

**对代码优美论的意义：** 这篇论文支持“维护健康可能具有经济价值”的研究方向，但不支持“越精致越赚钱”或“任何重构都能回本”。后续需要测量干预成本、风险、后续变化频率和机会成本。

---

## 5. Q02：ISO/IEC 25010:2023

**官方元数据：** [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html)，第 2 版，2023-11-15。官方页面确认该版定义九项产品质量特性；完整标准文本需要通过正式渠道获取。

**术语核对：** [GSO 对 ISO/IEC 25010:2023 的采用版公开预览](https://gso-sims-preview-doc-aws.s3-eu-west-1.amazonaws.com/gso-iso-iec-25010-2025-en.html)。

九项产品质量特性为：

1. Functional suitability — 功能适合性
2. Performance efficiency — 性能效率
3. Compatibility — 兼容性
4. Interaction capability — 交互能力
5. Reliability — 可靠性
6. Security — 安全性
7. Maintainability — 可维护性
8. Flexibility — 灵活性
9. Safety — 安全保障

### 对代码优美论的意义与边界

- ISO/IEC 25010 是**产品质量模型**，不是源代码审美标准。
- 可维护性、灵活性等属性可以与内部代码结构产生联系，但需要另行定义代码级指标和验证方法。
- 2023 版的 Interaction capability 中包含 user engagement 等子特性；这是面向用户交互体验的产品质量维度，不应误读为源代码“美学”维度。
- 本批没有取得 ISO 官方付费全文，因此只声称核验了官方版本元数据和采用版公开文本，不声称完成 ISO 原版逐页合规审读。

---

## 6. I04：Cui 等人的三组软件开发现场实验

**最终出版：** Kevin Zheyuan Cui, Mert Demirer, Sonia Jaffe, Leon Musolff, Sida Peng, Tobias Salz. “The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers.” *Management Science*, published online 2026-02-27. DOI: [10.1287/mnsc.2025.00535](https://doi.org/10.1287/mnsc.2025.00535)。

**原文与附录：**
- [作者工作论文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4945566)
- [INFORMS 最终出版页](https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535)
- [INFORMS 在线附录](https://pubsonline.informs.org/doi/suppl/10.1287/mnsc.2025.00535/suppl_file/mnsc.2025.00535.sm1.pdf)

### 研究设计与主要结果

- 三组现场随机实验，分别在 Microsoft、Accenture 和一家匿名 Fortune 100 企业开展。
- 合并样本为 4,867 名开发者；在线附录报告清洗后样本分别为 1,521、316、3,030。
- 实验向随机分配的开发者提供 AI 代码补全工具访问权限；各实验噪声较大，效果存在差异。
- 合并分析报告完成任务数量增加 26.08%，标准误为 10.3%。
- 经验较少的开发者采用率更高、生产力收益也更大。

### 关键边界

1. 26.08% 是三组实验合并后的任务完成数量估计，不是每位开发者都提高 26%，也不是代码质量提高 26%。
2. 研究场景是 AI 代码补全工具，不能直接等同于 2026 年具备长程规划、工具调用和多文件修改能力的 coding agents。
3. 工作论文版本中以 PR／完成任务等工作产出指标为主，构建成功率等指标不能代表完整架构质量、可维护性、安全性或长期缺陷表现。
4. 本研究支持“某些工具、任务与组织情境下，AI 可以提升开发产出”，不支持“AI 在所有开发任务上都提速”。

---

## 7. 反向证据：METR 2025 与 2026 更新

### I02：2025 熟悉仓库实验

**论文：** Joel Becker, Nate Rush, Beth Barnes, David Rein. “Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity.” [METR 论文 PDF](https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf)。

- 16 名经验丰富的开源开发者。
- 246 项来自他们熟悉、曾参与过的开源仓库任务。
- 随机分配任务是否允许使用当时的 AI 工具。
- 结果：允许 AI 的任务完成时间平均增加约 19%；论文报告 95% 区间约为 2%–39% 的时间增加。
- 处理变量是“允许使用 AI”，不是强制使用；这是特定工具和特定任务环境的 ITT 效果。
- 研究者指出，参与者对 AI 的主观速度预期与实际测量并不一致。

### I03：2026 方法更新

**机构说明：** [METR — We are Changing our Developer Productivity Experiment Design](https://metr.org/blog/2026-02-24-uplift-update/)。

METR 报告后续实验遇到明显的参与者自选择与任务选择问题：一部分开发者不愿被分配到无 AI 条件，且愿意提交的任务可能已经偏向 AI 适用场景。研究团队还指出时间记录和样本构成等因素使后续估计不够稳健。

该更新不等于“AI 已经证明提速”，也不推翻 2025 年在特定条件下观察到的减速。它说明 AI 的净效果受任务、熟悉度、工具版本、采用方式、参与者选择和测量设计影响。

---

## 8. A02：代码美学量化论文的必要降级

**书目：** Ron Coleman. “Aesthetics Versus Readability of Source Code.” *International Journal of Advanced Computer Science and Applications*, 9(9), 2018. DOI: [10.14569/IJACSA.2018.090902](https://doi.org/10.14569/IJACSA.2018.090902)。

**全文：** [论文 PDF](https://thesai.org/Downloads/Volume9No9/Paper_2-Aesthetics_versus_Readability_of_Source_Code.pdf)。

### 方法核验

- 语料来自 GNU Coreutils，约 1,043 个单函数 C 源文件、约 53,000 行代码。
- 作者定义 11 种美学因素／处理，并与 8 种可读性模型比较，形成 88 组相关性分析。
- 使用的 beauty factor 是特定的形式／分形维度操作化指标，并非直接邀请程序员对代码美感打分。
- 作者报告美学指标与可读性模型存在一定相关，但不能彼此替代。

### 必须保留的限制

- 单一项目、单一语言、特定代码风格语料。
- 没有以真实维护者的行为预测、缺陷定位或功能修改任务来验证美学指标。
- 该文没有建立跨语言、跨团队通用的“代码美学分数”。
- Spearman 相关系数的平方不应在所有情形下被随意解释为一般意义的方差解释率；引用作者的统计解释时需保留其模型假设。

**结论：** 这篇论文可以作为“某种美学代理指标与可读性代理指标并不完全重合”的探索性研究，不能作为“代码美学已被客观测量”的证据。

---

## 9. A04：Sundelin 2025 博士论文的 AI 段落

**书目：** Anders Sundelin. *On Quantifying Software Craftsmanship Concepts*. Blekinge Institute of Technology, Doctoral Dissertation Series No. 2025:12, 2025. ISBN 978-91-7295-512-7。

**全文：** [BTH/DiVA PDF](https://bth.diva-portal.org/smash/get/diva2%3A1997635/FULLTEXT01.pdf)。

### 定点核验结果

- 论文摘要明确指出：研究基于文献综述与工业案例形成四主题、17 原则、47 实践，并在后续论文中量化其中部分实践。
- 论文第 1.6.4 节 Future Work 讨论 LLM：作者认为反馈、迭代设计、专业文化和价值导向架构仍重要；未来工程师需要让 LLM 执行正确任务而非仅快速任务，并把业务需求和质量属性转换成可自动验证的测试边界。
- 作者明确指出 LLM 对软件工程职业的长期影响仍有待观察，包括是否替代大量人类活动，或让有经验的工程师更高效地产出更好软件。
- 这是一项研究展望和作者观点，不是关于 AI 生产力或代码质量的实证结论。

---

## 10. 第一批新增的认知科学证据

本次补充 [08_认知科学与程序理解补充研究](../batch01/cognition.md)，并新增来源 K01–K03。

初步结论：
- 程序员并不是逐字扫描代码；他们会调用熟悉的程序计划、惯例和领域知识。
- 违反常见的表达惯例，即使程序仍能运行，也可能增加理解难度。
- 代码记法和工具环境会影响可见性、修改阻力、隐藏依赖、心智操作等认知负担。
- 因而“优美”与认知结构可能有关，但仍不能直接等同于“更少工作记忆负荷”或“更快修改”；需要任务实验检验。

---

## 11. 经核验后的核心结论

### 已有证据支持

1. 代码美学确实参与程序员的日常判断和团队文化，但其意义具有语境性。
2. 软件工艺已经有系统化的原则与实践地图，覆盖架构、迭代、文化和反馈。
3. 精益软件工程存在长期研究脉络，但 2013 年大型软件领域的证据明显不足；必须更新近年研究才能判断现状。
4. 代码健康度、缺陷和实现时间之间存在可研究的关联，但现有模型并不证明重构投资的因果回报。
5. 产品质量标准可帮助拆分质量属性，却不能代替代码美学或内部设计评价。
6. AI 的生产力效果不是单一常数：不同实验的任务、工具、开发者和结果变量不同。

### 尚未证明

1. 代码美学可以被一个客观、跨语言的总分准确表示。
2. “越优美”就一定“越可维护”或“越可靠”。
3. AI 释放的时间必然被组织投入质量改进。
4. 所有质量改进的长期收益都大于实施和验证成本。
5. 精益制造实践在大型软件组织中有统一、稳定的效果。
6. AI 代码生成量增加会自动带来更高的工程品质。

### 对研究计划的决定

Batch 01-A 的定点原文核验可以标记完成，但 Batch 01 的完整研究仍是**批判性范围研究草案**：还未完成最新精益软件研究的系统更新、ISO 官方付费全文审读、所有中文综述全文阅读，也未进行实验。

下一步应进入 Batch02：以认知科学与程序理解为基础，研究代码的清晰、抽象、模块边界和真实理解／修改表现之间的关系，而不是立即制定一套静态“优美代码评分表”。

返回 [00_研究包说明与阅读导航](../README.md)；来源账本见 [sources](../evidence/sources.md)；认知补充见 [08_认知科学与程序理解补充研究](../batch01/cognition.md)。
