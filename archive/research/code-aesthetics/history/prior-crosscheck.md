---
title: Batch01-A 独立交叉核验与勘误记录
created_at: 2026-11-11
version: "0.2.1"
status: completed-with-limitations
tags: [source-audit, corrections, code-aesthetics]
---

# Batch01-A 独立交叉核验与勘误记录

> [!WARNING]
> 公开研究草案：Batch01-B仍为PARTIAL，人工研究审核pending，代码／参与者实验未执行。公开提交授权不等于研究通过。
> 本文件是历史记录，其中已读／通过／归档声明不代表当前独立核验。
> 文内“未发布”、本地文件名、行号和检查点属于原研究时点；本页已作公开目录与链接适配，不是字节保真档案。当前阅读顺序与发布边界见[课题入口](../README.md)。


## 0. 目的与范围

本文件记录对 v0.2 研究包的第二轮独立核验，重点检查容易影响理论推断的样本、研究方法、统计量、发表元数据和证据边界。

本轮核查了以下原始来源或官方页面：

- Fedorova et al. (2025) SAGE 公开 PDF；
- Coleman (2018) IJACSA 公开 PDF；
- Sundelin et al. (2022) 作者公开稿；
- Pernstål et al. (2013) 作者机构公开 PDF；
- Borg et al. (2024) arXiv 全文与 ACM 最终出版页；
- Cui et al. (2026) INFORMS 最终出版页；
- Soloway & Ehrlich (1984) IEEE 论文公开 PDF；
- Green (1989) 作者公开 PDF；
- Sundelin (2025) BTH 博士论文全文；
- METR (2025) 论文 PDF 与 METR (2026) 方法更新页面。

本轮不是全库系统检索，也没有运行新的实验。网页行号用于本轮核验记录；未来网页结构可能变化，建议同时保存 DOI 和原始 URL。

---

## 1. 明确勘误

### COR-01：The Lean Gap 的年份范围不是可直接“修正”的单一数字

**此前勘误过度确定：** 曾把年份范围统一写成 1990–2011。重新对照全文后，发现原文内部确有冲突，不能将其中一处直接当作唯一正确答案。

**原文逐处核验：**
- 方法部分 §3.2 / Table 2 明确写发表年份范围为 **1990–2010**。
- 结果段 §3.3 又写搜索结果覆盖 **1990–2011**。
- 五个数据库的实际检索日期均为 **2011-02-05**。
- 因此，准确表述应为：“原文方法表与结果段对年份窗口存在内部不一致；数据库检索日为 2011-02-05。”不擅自裁定唯一范围。

**筛选数字：**
- 初始 13,984 条；去重 3,754 条，剩 10,230 条；
- 标题／关键词／摘要筛选排除 10,176 条，剩 54 条；
- 再排除 16 条，最终 38 篇；
- 16/38 涉及大型开发，76% 非实证，9/38 属 evaluation 或 validation，16 项大型开发研究中 4 项为实证。

**核验入口：**
- 原文 PDF：https://gorschek.com/wp-content/uploads/2019/11/The-lean-gap-A-review-of-lean-approaches-to-large-scale-software-systems-development.pdf
- §3.2 / Table 2：网页抽取行 451–469，写 1990–2010。
- §3.3：网页抽取行 625–639，写 1990–2011 及筛选数字。
- §4.2–4.3：网页抽取行 709–829，列出大型开发与研究类型统计。

**影响：** 研究包撤回“已修正为 1990–2011”的确定性说法，改为记录原文冲突。该问题不改变 38 篇等筛选结果，但影响检索范围的精确表述。2013 年论文不能代表 2026 年现状。

### COR-02：METR 2025 论文作者名

**旧表述：** Elizabeth Barnes。

**采用书目写法：** Beth Barnes（按 METR 论文 PDF 首页署名）。

**原文依据与差异：** METR 论文 PDF 首页和 METR 官方研究博客署名为 Joel Becker、Nate Rush、Beth Barnes、David Rein；arXiv 元数据页显示 Elizabeth Barnes。当前没有证据支持把两种记录视为不同作者，也不应隐去差异。

**核验入口：** https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf ；https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ ；https://arxiv.org/abs/2507.09089

**影响：** 书目按 PDF 正文署名记录 Beth Barnes，并保留 arXiv 元数据差异；实验结果与研究结论不变。

### COR-03：Cui 等人（2026）的标准误单位

**旧表述：** “标准误 10.3 个百分点”。

**修正为：** “标准误 10.3%”，与 INFORMS 官方摘要的原始写法一致。除非对估计量定义和量纲作进一步说明，不将其改写成“百分点”。

**原文依据：** INFORMS 官方出版页摘要写为 `26.08% increase (standard error: 10.3%)`。

**核验入口：** https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535

**影响：** 只修正单位表达，不能据此推断代码质量或架构质量变化。

---

## 2. 核心文献原文核验摘要

### A01 — Coding Beauty and Decoding Ugliness

**核验：** SAGE 公开 PDF。

- 正式刊载：*Science, Technology, & Human Values*, 50(1), 69–93, 2025；online first 2024-04-15。
- 田野工作：Yandex 莫斯科总部，2014 年，约三个月。
- 访谈：26 名开发者半结构化深度访谈，另有 4 次面向管理者／专家的访谈；并进行多日现场观察。
- 核心发现：开发者可以使用“beautiful”而不就其定义达成一致；通过学习避免资深开发者称为“ugly”的代码，团队仍能形成相似的“不丑”实践。
- 边界：这是定性组织研究，不是代码风格对照实验，不证明某种审美直接降低缺陷率或维护时间。

原文入口：https://journals.sagepub.com/doi/pdf/10.1177/01622439241245746

### A02 — Aesthetics Versus Readability of Source Code

**核验：** 期刊公开 PDF。

- 语料：GNU Coreutils 114 个开源程序；处理后形成 1,043 个单函数 C 文件，约 53,000 LOC。
- 比较：11 个 beauty factors 与 8 个 readability models，合计 88 组分析。
- 作者报告：最大绝对统计显著相关约 |ρ|=0.59，中位绝对相关约 |ρ|=0.33。
- 重要谨慎：作者在讨论中使用 R² 解释相关程度；对 Spearman ρ 直接平方并称为一般“解释方差”需要谨慎，不应把作者的模型解释升级为通用统计定律。
- 边界：特定代码语料与特定 fractal beauty factor；没有通过真实维护任务验证其是否预测更好理解或修改。

原文入口：https://thesai.org/Downloads/Volume9No9/Paper_2-Aesthetics_versus_Readability_of_Source_Code.pdf

### A03 — Towards an Anatomy of Software Craftsmanship

**核验：** 作者公开稿全文 + BTH / ACM 发表元数据。

- 2018 年 12 月 Google Scholar 检索得到 980 条结果；经两项标准筛选后保留 112 篇候选。
- 从候选中选 4 篇初始 seed，再根据研究者经验与推荐增加 5 篇，最终 9 篇 seed；之后开展四轮 snowballing。
- 文献综述最终纳入 18 篇论文与 11 本书。
- 工业案例跟踪金融市场产品约七年；研究期有 155 名个人开发者贡献代码，访谈 6 名参与者并使用版本控制、文档、需求和缺陷档案。
- 形成四主题、17 原则、47 项层级实践。
- 重要边界：这是原则与实践的分类地图，不是 17 项原则各自的随机对照效果验证。单一金融产品案例、作者参与项目的 insider perspective 和组织环境均限制外部效度。

原文入口：https://anders.sundelinkarlskrona.se/wp-content/uploads/2021/06/TowardsAnAnatomyOfSoftwareCraftsmanship-authorCopy.pdf\
最终出版 DOI：https://doi.org/10.1145/3468504

### L01 — The Lean Gap

**核验：** 作者机构 PDF 全文。

- 13,984 条初始命中；去重后 10,230 条；最终纳入 38 篇。
- 16/38（42%）明确涉及大型开发。
- 76% 非实证；9/38（24%）属于 evaluation 或 validation research。
- 16 篇大型开发研究中只有 4 篇为实证研究。
- The Lean Gap 原文年份窗口存在 1990–2010（方法表）与 1990–2011（结果段）的内部不一致；数据库检索日为 2011-02-05。
- 边界：这是 2013 年论文所覆盖的历史研究状态，不代表当前领域全貌。

原文入口：https://gorschek.com/wp-content/uploads/2019/11/The-lean-gap-A-review-of-lean-approaches-to-large-scale-software-systems-development.pdf

### Q01 — Increasing, not Diminishing

**核验：** arXiv HTML 全文 + ACM 最终出版元数据。

- 两个工业数据集，79 个专有项目、46,211 个源文件、25 种语言。
- 以文件为单位，分析 Code Health 与缺陷数、Time-in-Development 的关系。
- 回归模型的 R² 约为 0.038（缺陷）和 0.006（Time-in-Dev）；作者明确说模型未捕获大量变异。
- 价值创造模型是从回归结果推演出的相对价值模型，不是重构干预的真实 ROI 试验。
- 最终 ACM DOI 为 `10.1145/3644384.3644471`；arXiv HTML 的旧 DOI 字符串不作为最终引用。

原文入口：https://arxiv.org/html/2401.13407\
最终出版入口：https://doi.org/10.1145/3644384.3644471

### I02 — METR 2025

**核验：** METR 论文 PDF 全文。

- 16 名经验丰富的开源开发者，246 项来自其熟悉仓库的任务。
- 随机分配是否允许使用当时的 AI 工具。
- 允许 AI 的任务完成时间平均增加约 19%；95% 区间约为 2%–39% 时间增加。
- 这只描述特定样本、仓库熟悉度、工具版本和任务条件；不能泛化为所有开发者或 2026 coding agents。

原文入口：https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf

### I03 — METR 2026 方法更新

**核验：** METR 官方方法更新页面。

- METR 明确指出后续实验受到参与者自选择、任务选择和并发 agent 使用时的时间测量问题影响。
- 研究团队称后续实验数据只能作为当前提速幅度的弱证据。
- 不能把这篇更新解释为“2026 年 AI 已被证明提速”，也不能将其解释为 2025 年 RCT 的减速结论被推翻。

官方入口：https://metr.org/blog/2026-02-24-uplift-update/

### I04 — Cui et al. (2026)

**核验：** INFORMS 最终出版页与作者工作论文。

- 正式发表信息：*Management Science*, 72(11), 9408–9420；Published Online 2026-02-27。
- 三组现场随机实验：Microsoft、Accenture、一家匿名 Fortune 100 企业。
- 合并样本 4,867 名开发者。
- 官方摘要报告完成任务数量增加 26.08%，标准误 10.3%。
- 实验工具是提供智能代码补全建议的 AI coding assistant；不能直接等同于具有长程规划和多工具执行能力的 coding agents。
- 26.08% 是完成任务数量结果，不是代码质量提升比例。

最终出版入口：https://doi.org/10.1287/mnsc.2025.00535

### K01 — Soloway & Ehrlich (1984)

**核验：** IEEE 论文公开 PDF 全文。

- Study I：139 名学生程序员，其中 94 名初学者、45 名进阶学生；Alpha / Beta 程序对照。
- Study II：41 名专业程序员；考察熟悉的 program plans 与程序惯例对关键语句回忆的影响。
- 论文报告 Study I 一组正确表现约 88% vs 31%；Study II 首轮关键语句回忆约 42% vs 24%。
- 边界：这是历史性受控程序片段研究，不是大型生产代码库维护实验。

原文入口：https://www.cs.kent.edu/~jmaletic/Prog-Comp/Papers/soloway84.pdf

### K02 — Green (1989)

**核验：** 作者公开 PDF 全文。

- 讨论记法与环境对 opportunistic planning 的影响。
- 维度包括 viscosity、visibility、hidden dependencies、premature commitment、role-expressiveness、hard mental operations 等。
- 作者明确表示认知维度并非完全正交、精确的自然常数，而是近似的分析工具。
- 边界：概念框架，不是代码评分标准。

原文入口：https://www.cl.cam.ac.uk/~afb21/CognitiveDimensions/papers/Green1989.pdf

### A04 — Sundelin (2025)

**核验：** BTH 博士论文定点阅读 Future Work。

- 作者提出 LLM 时代仍需要软件工艺的反馈、迭代设计、专业文化和价值导向架构。
- 强调把业务需求及性能、稳定性、健壮性等质量属性转成可自动验证的测试边界。
- 同时明确提出：LLM 会替代多少人类工作，或帮助资深工程师更快产出更好软件，仍是开放问题。
- 边界：属于博士论文的研究展望，不是 AI 生产力实证结论。

原文入口：https://bth.diva-portal.org/smash/get/diva2%3A1997635/FULLTEXT01.pdf

---

## 3. 对研究框架的影响

本轮核验没有推翻 v0.2 的核心理论结构，但加强了三点：

1. **代码美学必须与任务表现分开。** 读者说“漂亮”不能自动证明更容易理解或修改。
2. **程序理解需要认知变量。** 计划知识、惯例、可见性、隐藏依赖、程序模型和领域模型为后续构念操作化提供了入口。
3. **AI 生产力与质量提升之间存在机制断点。** 需要分别验证端到端净节约、组织再分配、具体质量干预有效性。

因此，当前理论仍保持为工作框架，不冻结为一套统一“优美分数”。

---

## 4. 本轮未解决事项

- ISO/IEC 25010:2023 官方付费全文未逐页阅读；
- Cui 最终版全文与作者工作论文未逐页做版本差异审查；
- Pennington 1987 原章未取得；
- Poppendieck 原书、部分中文综述及近年精益软件综述仍有阅读缺口；
- 没有用户实验或代码质量干预实验；
- 没有 Mermaid 渲染或 Obsidian 视觉验收；
- 尚未获得用户人工审核。

**结论：** Batch01-A 定点原文核验已完成，状态为 `BATCH_01A_COMPLETE_WITH_LIMITATIONS`。这不代表 Batch01 系统综述完成，也不代表代码优美论已获验证。
