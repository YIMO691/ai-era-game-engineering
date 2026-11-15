---
title: Batch01-A 接收检查与归档修订记录
created_at: 2026-11-11
version: "0.2.1"
status: audit-complete-with-explicit-limits
topic_id: 20261111-code-aesthetics-batch01
tags: [code-aesthetics, archive-audit, bibliography-audit, batch01a]
---

# Batch01-A 接收检查与归档修订记录（v0.2.1）

> [!WARNING]
> 公开研究草案：Batch01-B仍为PARTIAL，人工研究审核pending，代码／参与者实验未执行。公开提交授权不等于研究通过。
> 本文件是历史记录，其中已读／通过／归档声明不代表当前独立核验。
> 文内“未发布”、本地文件名、行号和检查点属于原研究时点；本页已作公开目录与链接适配，不是字节保真档案。当前阅读顺序与发布边界见[课题入口](../README.md)。


## 0. 目的与处理原则

本记录承接接收方对 Batch01-A v0.2 的独立检查意见。处理原则：

1. 保留 v0.1，不覆盖、不重命名、不把 v0.2 直接标记为最终版。
2. 不因 SHA-256 不匹配直接推断内容被篡改；先比较具体字节差异和文本内容。
3. 不以刷新哈希代替书目与论证审核。
4. 不执行原包中的 `verify_package.py` 或其他包内脚本；仅使用独立的 Python 标准库代码读取文件、检查 ZIP 和计算哈希。
5. 所有研究结论仍区分原文发现、官方摘要、作者推断和本研究综合；不把 36 项来源登记说成 36 篇全文已读。

## 1. 接收方报告的两个归档问题

### 1.1 中文文件名编码

对先前交付的 `code-aesthetics-batch01a-v0.2-download.zip` 检查发现：

- ZIP CRC 通过；
- 归档内有 11 个含非 ASCII 字符的文件名；
- 这 11 个文件名均未设置 ZIP UTF-8 general-purpose bit flag（0x0800）；
- 文件名在该归档中已表现为错误字符编码。

对原始工作归档 `code-aesthetics-batch01-v0.2.zip` 的对照检查则发现，11 个中文文件名均设置了 UTF-8 标记。问题出在此前的重新打包／下载副本，而不是所有 v0.2 归档都存在相同问题。

**修复**：v0.2.1 使用真实 Unicode 文件名重新写入 ZIP，并逐项检查非 ASCII 文件名的 UTF-8 标记。没有通过猜测重命名文件；ZIP 中的文件名与实际文件名逐字一致。

### 1.2 书目文件 SHA-256 不一致

比较原始 v0.2 ZIP 中的书目文件与接收工作目录中的书目文件后，发现差异集中在 I04 的一处表达：

- 原归档文本：`standard error: 10.3%`；
- 工作目录文本：`标准误 10.3 个百分点`。

后者是归档后编辑的表达，且没有得到 INFORMS 官方摘要支持。INFORMS 正式出版页的原文是：

`26.08% increase (standard error: 10.3%)`

因此，本版恢复官方摘要原始写法 `standard error: 10.3%`，不擅自改写成“百分点”。这说明原清单未同步于后续编辑；它本身不证明内容遭到恶意篡改。旧归档内该文件 SHA-256 为 `bb8e12b0fcfee4eb1b57bbce673feecaa64ee1607e9611e439b9eab9d9c111d0`，此前下载副本为 `37dd30716037df53129d99902fe1b2dcc18343ffffdac4e451f2badcbd0ab4ab`；逐行 diff 只发现上述 I04 一行差异。

**修复**：不仅恢复该表达，还重新审核和同步整个 `02_核心文献注释书目.md` 的阅读状态、方法、样本、限制与版本边界。

## 2. 书目内容交叉审查的实质修订

### 2.1 A01：Coding Beauty and Decoding Ugliness

原文：SAGE 公开 PDF，Methods、Research Setting、Coding Beauty、Ugliness 与 “Not Ugly” 相关段落。

确认：
- 2014 年 Yandex 莫斯科总部三个月定性田野；
- 26 次开发者半结构化深度访谈；
- 4 次管理者专家访谈；
- 多日工作场所观察；访谈以俄语进行，持续 1–4 小时，录音、转录并翻译；
- 研究者最初没有把代码美学设为访谈中心问题，是在参与者反复提及 beautiful / ugly 后加入相关追问；
- 组织内没有单一 beautiful code 理想；对多种 ugly code 形式有较共享的识别；“not ugly”成为可进入代码库的默认类别。

修订：不再把研究简化成“大家对丑代码有共识”一句话，而是保留其更重要的发现：审美语言既容纳专业背景差异，也推动本地实践一致和新人社会化。它是定性组织研究，不测量缺陷率或维护成本。

原文入口：https://journals.sagepub.com/doi/pdf/10.1177/01622439241245746

### 2.2 A02：Aesthetics Versus Readability of Source Code

原文：期刊 PDF，方法、数据集、beauty factors、readability scores 与统计结果。

确认：
- 语料来自 GNU Core Utilities 的 114 个程序；
- 过滤后形成 1,043 个单函数 C 文件，约 53,000 LOC；
- 11 个 beauty factors 与 8 个 readability scores，进行 88 组相关分析；
- 使用 Spearman’s rho；
- 论文报告显著相关的绝对系数约 0.05–0.59，未观察到强相关；作者报告其中位相关平方值为 0.0961。

修订：
- 不再泛称“53,000 行 Linux 代码”而不交代样本单位；
- 明确 beauty factor 是作者构造的代理指标，不是程序员主观审美评分；
- 不把 Spearman ρ 平方直接等同于一般回归中的因果方差解释率；
- 不推断美学与真实维护绩效已被证明相互独立。

原文入口：https://thesai.org/Downloads/Volume9No9/Paper_2-Aesthetics_versus_Readability_of_Source_Code.pdf

### 2.3 A03：Towards an Anatomy of Software Craftsmanship

原文：作者公开稿，§3.1、§3.2、§3.3、§5、§7。

确认：
- 2018 年 12 月 Google Scholar 初始检索 980 条；
- 两项标准分别排除 522 与 346 条，余 112 条候选；
- 以 4 篇数据库种子论文起步，再依据研究者经验与推荐增加 5 篇；
- 四轮 snowballing，最终纳入 18 篇论文和 11 本书；
- Ericsson 金融科技产品约七年纵向案例，产品约有 20 个全球部署；
- 155 名开发者是按 Git Author tag 统计的贡献者，不是访谈人数；
- 案例访谈参与者为 6 人；
- 第一作者曾参与该项目开发，存在 insider perspective；
- 结果为四主题、17 原则、47 项层级实践。

修订：在报告和书目中明确区分 155 个 Git 作者标签与 6 名访谈参与者；强调分类图谱不是 17 项原则逐条因果验证。

作者稿：https://anders.sundelinkarlskrona.se/wp-content/uploads/2021/06/TowardsAnAnatomyOfSoftwareCraftsmanship-authorCopy.pdf\
正式出版 DOI：https://doi.org/10.1145/3468504

### 2.4 L01：The Lean Gap

原文：作者机构 PDF，§3.2、Table 2、§3.3、§4.2–4.3。

**本轮发现此前勘误本身过度确定，已撤回。**

原文年份范围存在内部不一致：
- 方法部分 §3.2 / Table 2 写发表年份窗口为 1990–2010；
- 结果段 §3.3 写为 1990–2011；
- 五个数据库检索日期均为 2011-02-05。

因此，不能将该研究简单“修正”为 1990–2011，也不能只保留 1990–2010 而隐去冲突。正确写法是明确报告原文冲突与数据库检索日期。

筛选数字确认：
- 初始 13,984 条；
- 去重 3,754 条，余 10,230 条；
- 标题／关键词／摘要筛选排除 10,176 条，余 54 条；
- 再排除 16 条，最终纳入 38 篇；
- 16/38 涉及大型开发；
- 76% 为非实证研究；
- 9/38 属 evaluation 或 validation research；
- 16 项大型开发研究中 4 项为实证研究。

原文入口：https://gorschek.com/wp-content/uploads/2019/11/The-lean-gap-A-review-of-lean-approaches-to-large-scale-software-systems-development.pdf

### 2.5 Q01：Increasing, not Diminishing

原文：arXiv 预印本全文，方法、数据集、回归模型和限制。

确认：
- 两个数据集共 79 个专有项目、46,211 个源代码文件、25 种语言；
- 缺陷数模型 \(R^2=0.038\)；
- Time-in-Development 模型 \(R^2=0.006\)；
- 价值创造曲线是基于观察模型与假设的推演，不是随机重构干预或真实项目 ROI 实验。

修订：明确模型解释力有限，不能从模型曲线推出所有项目中“质量越高，边际回报越大”，也不能把质量投资成本与机会成本当作已被完整计量。

原文入口：https://arxiv.org/abs/2401.13407

### 2.6 I02：METR 2025

确认：论文 PDF 首页和 METR 官方博客署名为 Beth Barnes；arXiv 元数据页显示 Elizabeth Barnes。

修订：本包按论文 PDF 正文署名记录 Beth Barnes，并保留元数据差异，不声称已证明两种写法的身份关系。

论文 PDF：https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf\
METR 说明：https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/\
arXiv：https://arxiv.org/abs/2507.09089

### 2.7 I04：Cui 等人的 2026 年现场实验

INFORMS 正式页面核对：
- 作者顺序与正式出版信息；
- 在线发表日期 2026-02-27；
- *Management Science* 72(11):9408–9420；
- 三组现场随机实验、4,867 名开发者；
- 官方摘要写完成任务数量增加 26.08%，standard error: 10.3%。

本包读取了作者工作论文全文，并核对正式出版页与在线附录；**没有宣称已经逐页比较最终出版版与工作论文的全部差异**。

官方入口：https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535

## 3. 文档同步范围

已同步：
- `01_思想基础与理论溯源研究报告.md`：移除旧的“全文待核”表述，更新 A01/A02/A03/L01/Q01/I02/I04 证据范围；
- `02_核心文献注释书目.md`：逐条同步已读状态、方法、样本、限制与版本边界；
- `07_Batch01-A核心文献原文核验与证据修订记录.md`：撤回 L01 年份单边修正；
- `10_独立交叉核验与勘误记录.md`：增加原文冲突与 METR 作者元数据差异；
- `sources.md`：更新 L01、A01/A02/A03、I02/I04 来源条目；
- `evidence-lean.md`：修订 L01 年份范围描述；
- `review.md`：记录接收审查与本轮修订；
- `05_Batch02研究问题与计划.md`：不再要求重复补读已经完成的承重文献；
- `00_研究包说明与阅读导航.md`、`topic.json`、`validation.txt`、`SHA256SUMS.txt`：同步版本、状态、文件清单和检查点。

## 4. v0.2.1 归档规则

- 版本：`v0.2.1`，不覆盖 v0.1 或原 v0.2。
- ZIP 顶层目录：`code-aesthetics-batch01-v0.2.1/`。
- 中文文件名：必须保留真实 Unicode 字符，且 ZIP general-purpose bit flag 包含 UTF-8 标记（0x0800）。
- `topic.json`：保存研究文件检查点，不对自身做哈希，也不记录 ZIP 哈希。
- `SHA256SUMS.txt`：记录 ZIP 内除清单自身以外的所有文件，包括 `topic.json`。
- 外部 `.zip.sha256`：记录最终 ZIP 文件哈希，不放入 ZIP。
- ZIP 不包含旧版 ZIP、下载副本或外部论文全文。
- 不执行包内 `verify_package.py`；其仅作为用户可选的本地结构验证工具。

## 5. 本轮验证结果

具体值见 `validation.txt`、`topic.json`、`SHA256SUMS.txt` 与 ZIP sidecar。

本轮自有检查覆盖：
- Markdown 文件数量与文件名；
- 36 个来源 ID 的唯一性；
- 文内 Obsidian wikilink 目标存在性；
- Mermaid 源代码块数量（不代表渲染成功）；
- `topic.json` 解析、artifact 清单和检查点哈希；
- SHA256 清单逐项匹配；
- ZIP CRC、成员路径、成员清单、文件字节一致性；
- 所有非 ASCII 文件名的 UTF-8 标记。

未执行：
- 包内 Python 验证脚本；
- Mermaid 渲染器；
- Obsidian 阅读视图视觉验收；
- 用户项目代码实验；
- 人类参与者实验。

## 6. 仍未解决的研究缺口

1. ISO/IEC 25010:2023 官方付费原版未逐页读取；当前为官方元数据与公开采用版文本交叉核对。
2. I04 最终出版版与作者工作论文尚未逐页比较全部差异。
3. K03 Pennington 原章未取得；仅有二手摘要。
4. A04 博士论文为定点阅读；Poppendieck 原书、部分中文综述和 2013 年后的精益软件研究仍需按问题补读。
5. 本批没有执行代码或用户实验；理论框架仍是待检验研究框架。

**最终状态：** `BATCH_01A_COMPLETE_WITH_LIMITATIONS`。v0.2.1 是完成接收修订和归档校验的候选研究包，不是最终学术出版物，也不替代用户人工审阅。
