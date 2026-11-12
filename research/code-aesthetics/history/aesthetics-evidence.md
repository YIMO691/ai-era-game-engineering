---
title: 代码美学与软件工艺——受访问限制的证据定位备忘录
created_at: 2026-11-11
version: "0.2.1"
topic_id: 20261111-code-aesthetics-batch01
tags:
  - engineering-research
  - code-aesthetics
  - software-craftsmanship
status: evidence-reviewed-with-explicit-gaps
---

# 代码美学与软件工艺：证据定位备忘录

> [!WARNING]
> 公开研究草案：Batch01-B仍为PARTIAL，人工研究审核pending，代码／参与者实验未执行。公开提交授权不等于研究通过。
> 本文件是历史记录，其中已读／通过／归档声明不代表当前独立核验。
> 文内“未发布”、本地文件名、行号和检查点属于原研究时点；本页已作公开目录与链接适配，不是字节保真档案。当前阅读顺序与发布边界见[课题入口](../README.md)。


> [!NOTE] v0.1 分支记录与 v0.2 补读状态
> 本文件开头记录的是 v0.1 当时的访问受限状态，不应再被当作当前阅读状态。Batch01-A 已通过作者公开 PDF、期刊 PDF、机构仓储和官方页面合法补读 A01、A02、A03 等来源。当前状态以本文件末尾的 Batch01-A 更新和 [sources](../evidence/sources.md) 为准。没有使用代理或绕过付费限制。

## 研究问题与边界

- 问题：代码“美”与“工艺品质”分别是怎样的研究对象；哪些命题是经验描述，哪些是价值主张；指定研究的分类、案例和展望能否定位到原始来源？
- 类型：exploratory；不预设美学必然提升可读性或工艺运动必然改善交付。
- 竞争解释：审美可能帮助协作与形成共享标准，也可能只是对既有规范的合法化；形式美指标可能与可读性相关，也可能只测量不同的代理变量。
- 范围：四项指定研究、官方软件工艺宣言与敏捷/XP关系、一项工艺动机的一手理论来源。仅核查博士论文是否含 AI 展望，不开展 AI 研究；不研究精益或质量经济学。
- 工程适用边界：本批没有 Unity/C# 的直接样本、代码实验或性能测量；不得把一般讨论转化成 Unity 架构规则。
- 停止条件：约 15 次定点访问；正文访问受到一致阻止后停止重复抓取，记录缺口。本轮实际 16 次，最后一次用于纠正过宽的宣言检索，定位官方站。
- 执行：先读研究契约；相关目录 Git 检查返回 `fatal: not a git repository`；同题路径初查未发现已有文件。本文件是用户指定的临时汇总，仅写本文件，不创建/修改 topic.json、sources.md 或其他产物。

## 关键纠错与核查结论

| 待核查项 | 本轮可以说什么 | 不能说什么 |
|---|---|---|
| Fedorova 等论文年份 | 出版社搜索结果给出 online 2024-04-15、卷期 2025 年 50(1):69–93。应保留双日期。 | 把 2024 与 2025 当两篇独立研究；声称已读取出版社正文核验日期。 |
| “四主题、17原则、47实践” | 索引明确把这套分类归于 Sundelin 等的 *Towards an Anatomy of Software Craftsmanship*。主题名称见 A03，仍待全文逐项核对。 | 把它误归于代码美学论文，或称“实验验证了17条普适法则”。 |
| 七年金融案例 | 搜索输出把七年纵向金融市场产品案例和 18 篇论文、11 本书的综述一起归于 anatomy 研究。 | 把七年当七年随机对照、因果证明，或再与博士论文重复计算成独立复制研究。 |
| Coleman 美学/可读性 | 出版社索引显示比较分形美学指标与可读性模型，相关性不等于同一性；数字只属于待核对线索。 | “美观代码更易读已经得到人类实验验证”；“相关系数证明美学导致质量提升”。 |
| 博士论文 AI 展望 | 已找到大学库 PDF；正文读取被阻止，两次相关搜索未确认具体展望段落。 | “论文证明 AI 可量化/替代工艺”，或反过来说“论文不存在 AI 展望”。 |
| 宣言与敏捷/XP | 官方索引确认“Not only working software, but also well-crafted software”；XP 联系只有待查二手/作者稿索引线索。 | 宣称已读官方完整宣言；把工艺、敏捷、XP说成同义词，或声称宣言本身列出了完整XP实践。 |
| Sennett 工艺动机 | 已定位作者专著和官方出版社页；“for its own sake”可作待核对的一手理论线索。 | 把哲学/社会理论命题升级为普遍人类心理事实或软件质量因果证据。 |

## 证据记录

共同字段：访问日期 2026-11-11；`experiment_status: not-run`。下文 `read_status: access_failed` 表示实际抓取失败，仍可能通过搜索发现元数据；`discovered` 表示仅发现来源。两者都不等于读过正文。搜索工具生成的说明不冒充原文短摘录；无可核对摘录时明确留空。

### ER-20261111-CA-A01 — Coding Beauty and Decoding Ugliness

- **完整书目**：Marina Fedorova, Melissa Mazmanian, Paul Dourish. *Coding Beauty and Decoding Ugliness: The Role of Aesthetic Concerns in Programming Practices*. *Science, Technology, & Human Values*, 50(1), 69–93, 2025；首次 online 2024-04-15。出版者 SAGE。
- **DOI / 原始URL**：[10.1177/01622439241245746](https://doi.org/10.1177/01622439241245746)；[出版社文章页](https://journals.sagepub.com/doi/10.1177/01622439241245746)；[出版社摘要页](https://journals.sagepub.com/doi/abs/10.1177/01622439241245746)。书目来自本次出版社搜索结果，尚未打开核验。
- **Source type**：经验论文；本轮获取层级为出版社搜索索引/搜索摘要。
- **read_status**：`access_failed`。**实际读到范围**：WebSearch 的元数据和内容摘要；WebFetch 未返回正文。**claim_status**：内容 `unverified`，下述方法和发现均是定点复核线索。
- **原文定位与短摘录**：检索结果将样本细节定位为 **Methods**；没有可验证页码，也没有取得足以作为论文直接引文的正文。短摘录：**未取得**；不把工具生成的概述放进引号。
- **方法/样本线索**：Yandex 莫斯科总部，2014 年三个月田野；26 次开发者半结构化深度访谈、4 次管理者专家访谈及工作场所观察；俄语访谈、录音转写后译为英语；访谈约 1–4 小时。搜索摘要称“美/丑”反复出现在早期访谈后，研究者加入相应问题。以上具体数字均未对全文核验。
- **发现线索**：开发者对“美”的定义可以多元、模糊；识别“丑”代码则可能有助于执行本地惯例、使新人适应现有代码库。不是把“美”简化成格式整齐。
- **限制/反证**：按上述方法线索，这是一家公司、特定时期、文化与语言环境中的质性解释，不是跨文化比较或效果实验；翻译、进入现场的机会、受访者自述与研究者解释均需检查。尚未读到作者对这些问题的正式反思，不能把本段称为作者原文限制。
- **Supports / Contradicts**：可作为审美同时涉及个人理想与社会规范的候选证据；与“存在单一普适美学标准”的简单叙事存在张力，尚不足以普遍证伪任何标准。
- **项目相关性**：提示团队评价“丑代码”时区分可说明的维护问题与纯粹的内部审美习惯；这只是待验证的设计启示。
- **允许措辞**：“出版社索引所述的 Yandex 质性研究提示，美学判断可能同时维持多样性和本地一致性，全文尚待核验。”
- **禁止更强措辞**：“论文证明丑代码一定造成缺陷”“俄国程序员的审美代表全部软件文化”“审美规范的排斥效应已被本轮完整核验”。
- **权利**：出版社版权文本；未取得可重用许可信息，仅保留书目与内容转述，不复制或下载付费正文。

### ER-20261111-CA-A02 — Aesthetics Versus Readability of Source Code

- **完整书目**：Ron Coleman. *Aesthetics Versus Readability of Source Code*. *International Journal of Advanced Computer Science and Applications* (IJACSA), 9(9), 12–18, 2018。出版者 The Science and Information Organization。
- **DOI / URL**：[10.14569/IJACSA.2018.090902](https://doi.org/10.14569/IJACSA.2018.090902)；[出版社记录](https://thesai.org/Publications/ViewPaper?Code=IJACSA&Issue=9&SerialNo=2&Volume=9)；[出版社PDF](https://thesai.org/Downloads/Volume9No9/Paper_2-Aesthetics_versus_Readability_of_Source_Code.pdf)。
- **Source type**：量化比较论文；本轮仅搜索索引/摘要。
- **read_status**：`access_failed`。**实际读到范围**：搜索工具返回的出版社条目与方法/结果摘要；PDF正文零页。**claim_status**：`unverified`。
- **原文定位与短摘录**：卷期页码可定位整篇，但结果表、方法章节和对应页码未取得。**没有经正文核验的短摘录**。
- **方法/样本线索**：约 53,000 行开源系统代码；11 个美学因子与8个可读性模型；美学采用分形相关指标。搜索摘要报告显著相关的最大绝对值约 0.59，中位数约 0.33。代码库名称、语言、抽样单位、模型训练集重叠、多重检验处理、置信区间均未核对。
- **发现线索**：作者将美学与可读性视为有关但不同的性质。数字目前不可用于计算效果量、比较语言或推广到团队实践。
- **限制/反证**：必须区分“指标分数的相关”与“人类体验的相关”，更不能跳到维护成本或缺陷因果关系。尚不能确定本文是否另有直接人类实验，因此也不写“本文绝对没有任何人类数据”；只能说目前取得的摘要描述的是模型/指标比较。
- **Supports / Contradicts**：可作为“美学≠可读性”的候选区分依据；不能凭低到中度相关就证明两者心理机制独立。
- **项目相关性**：不可用一个视觉/分形美学指标替代代码理解、调试或演进评估。
- **允许措辞**：“出版社索引描述了一项美学指标与可读性模型的相关比较；其结果不支持直接把两个指标等同。”
- **禁止更强措辞**：“研究证明美感和可读性无关”“所有美丽代码都易读”“53,000行代码构成跨语言普适证据”。
- **权利**：搜索指出出版者提供开放获取PDF，但本轮未核对具体许可，不据此擅自认定 CC BY 条款。

### ER-20261111-CA-A03 — Towards an Anatomy of Software Craftsmanship

- **完整书目**：Anders Sundelin, Javier Gonzalez-Huerta, Krzysztof Wnuk, Tony Gorschek. *Towards an Anatomy of Software Craftsmanship*. *ACM Transactions on Software Engineering and Methodology*, 31(1), Article 6, 49 pages, 2022。出版者 ACM。搜索同时发现 2021 作者稿路径；不能把路径年份当作正式卷期年份。
- **DOI / URL**：[10.1145/3468504](https://doi.org/10.1145/3468504)；[BTH/DiVA项目记录](https://bth.diva-portal.org/smash/project.jsf?pid=project%3A2667)；[大学库相关PDF](https://www.diva-portal.org/smash/get/diva2%3A1586608/FULLTEXT03.pdf)；[作者稿](https://anders.sundelinkarlskrona.se/wp-content/uploads/2021/06/TowardsAnAnatomyOfSoftwareCraftsmanship-authorCopy.pdf)。大学库相关PDF的具体版本未打开核实。
- **Source type**：文献综合与纵向案例研究论文；本轮只读搜索结果。
- **read_status**：`discovered`。**实际读到范围**：题名、作者、期刊元数据、搜索工具根据大学库与作者稿形成的摘要。作者稿本轮未抓取。**claim_status**：`unverified`。
- **原文定位与短摘录**：搜索工具把分类定位为作者稿 **Section 5、Figure 3**，这是待检查定位，不是假称已读的页码。返回的主题标签如下，尚未逐字对照PDF：
  - “Value-focused architecture”——价值聚焦的架构：3原则、10实践。
  - “Iterative design, development, and verification”——迭代设计、开发与验证：3原则、10实践。
  - “Shared professional culture”——共享专业文化：6原则、18实践。
  - “Feedback”——反馈：5原则、9实践。
  - 合计4主题、17原则、47实践；该算术一致性不等于已经核验所有条目的边界、命名或编码过程。
- **方法/样本线索**：综述18篇论文和11本书，加上金融市场产品软件开发的七年纵向案例。参与者人数、公司数量、数据收集跨度的具体起止、作者的项目角色、资料编码与一致性核验均未知。
- **发现线索**：形成工艺概念的层次化分类，主题范围超出格式与个人编码技巧，含架构、交互实践、共享文化和反馈。
- **限制/反证**：分类综合不是17条规则效果的逐项试验；书籍与运动倡导文本可能提供价值主张而非经验检验。纵向长度不自动消除选择偏差、组织变革与人员变动的混杂；金融领域经验不可不加论证迁移到游戏客户端。以上为方法审慎判断，未冒充作者明确承认的限制。
- **Supports / Contradicts**：支持进一步寻找工艺的多层次结构；不能支持“craftsmanship就是个人追求漂亮代码”。同样不能支持“每个项目应完整落实47实践”。
- **项目相关性**：提供分类候选而非团队考核清单；需要逐项验证适用问题、实际约束与代价。
- **允许措辞**：“大学库及作者稿的索引表明，该研究提出四主题、17原则、47实践，并结合七年金融领域案例；具体编码与论据尚待全文检查。”
- **禁止更强措辞**：“七年证明工艺必然提高质量”“17条经实验验证的科学定律”“47项是普遍强制标准”。
- **权利**：原始出版者 ACM；作者稿/大学库的可访问性不等同于自由再许可，具体许可未读。

### ER-20261111-CA-A04 — On Quantifying Software Craftsmanship Concepts

- **完整书目**：Anders Sundelin. *On Quantifying Software Craftsmanship Concepts*. 博士论文，Blekinge Institute of Technology（BTH，瑞典布莱金厄理工学院），2025。非期刊文章；论文系列号、ISBN、答辩日期与 DOI 未核实。
- **URL**：[BTH/DiVA论文PDF](https://bth.diva-portal.org/smash/get/diva2%3A1997635/FULLTEXT01.pdf)；库内标识 `diva2:1997635`；[BTH院系页](https://www.bth.se/english/about-bth/departments/department-of-software-engineering)。
- **Source type**：博士论文；本轮仅大学库索引线索。
- **read_status**：`access_failed`。**实际读到范围**：搜索摘要称其为2025博士论文、包含A03；未读任何论文页、目录、综合章节或附录。**claim_status**：题名与归属为待原页核对元数据；内容 `unverified`。
- **原文定位与短摘录**：AI 展望未取得章节、页码或原文，**短摘录缺失**。不能补写所谓“未来AI将……”句子。
- **方法/样本**：整篇论文的研究设计、所有组成论文及其关系尚未知。搜索输出关于A03的七年案例不能冒充博士论文全部研究设计，也不作为第二份独立案例证据。
- **核查结果**：`"On Quantifying Software Craftsmanship Concepts" "AI" "seven"` 没有明确匹配；`site:bth.diva-portal.org "On Quantifying Software Craftsmanship Concepts" "intelligence"` 没有结果。这仅是搜索无命中，不是“展望不存在”的证据。
- **限制/反证**：不能仅依据题名“Quantifying”就说工艺已被完整、客观、自动化地量化。即使以后读到AI展望，也应先分类为作者未来工作建议，而不是实验结果。
- **Supports / Contradicts**：目前只支持继续追踪该博士论文这一检索行动；不支持AI相关实质论断。
- **项目相关性**：作为理论后续研究入口；不能用来背书自动化评价程序员或软件工艺。
- **允许措辞**：“已定位2025年BTH博士论文，正文访问受阻，AI展望尚未核验。”
- **禁止更强措辞**：“论文已经证实AI能够评价/替代工艺”“论文没有讨论AI”。
- **权利**：大学库托管，具体全文许可未核验。

### ER-20261111-CA-A05 — Manifesto for Software Craftsmanship

- **完整书目**：Software Craftsmanship 宣言社区/签署者（集体文本；个人作者名单未核验）. *Manifesto for Software Craftsmanship*. 官方网站，页面索引显示2009版权年份。非期刊，无 DOI。
- **URL**：[官方宣言](https://manifesto.softwarecraftsmanship.org/)。
- **Source type**：官方规范性宣言，是运动自我表述的一手来源，不是实验研究。
- **read_status**：`access_failed`。**实际读到范围**：官方站搜索命中及一句索引引文；抓取失败，未读完整四项陈述和结尾。**claim_status**：索引句子 `unverified`（尚未对原页），性质区分为分析判断。
- **原文定位与短摘录**：官方页面首项宣言的索引引文：“Not only working software, but also well-crafted software”。可标“官方页搜索索引引文”，不得标“正文已读摘录”。
- **方法/样本**：不适用；这是集体价值声明。签署人数并不能作为有效性样本。
- **发现与敏捷关系**：索引呈现质量、持续增加价值、专业社区、富有成效的伙伴关系四项关注。与敏捷价值表述的对应关系是可检查的文本线索；本轮未完整核验全部对照句。尤其 `not only` 不能翻成“不要能工作的软件，只要精美代码”。
- **XP关系与缺口**：本轮广域搜索返回 Martin/Mancuso 的书籍转载、笔记以及 A03 作者稿，摘要称工艺倡导XP工程实践。未读一手正文，也未访问权利不明的图书副本。因而只保留“运动与XP实践的历史关联待核验”，不将这些搜索摘要登记为新的独立证据。不能从宣言单句推导一套XP技术规范。
- **限制/反证**：宣言表达应该重视什么，不证明重视后必然发生何种结果；表述不能自动排除形式主义、规范强制或过度设计。
- **项目相关性**：可提供团队价值讨论的文本，但具体实践和例外必须另行论证。
- **允许措辞**：“官方索引的‘not only…but also…’表述将工艺品质作为工作软件以外的关注，而非替代工作软件。”
- **禁止更强措辞**：“宣言科学证明工艺优于敏捷”“工艺宣言等于XP”“宣言要求不计成本地做到完美”。
- **权利**：官方网页；具体许可与可复制范围本轮未读。

### ER-20261111-CA-A06 — Principles behind the Agile Manifesto（待恢复正文）

- **完整书目**：Agile Manifesto 作者群（17名发起者姓名本轮未核对）. *Principles behind the Agile Manifesto*. Agile Manifesto 官方网站，通常书目年份2001；本轮原页日期未核验。非期刊，无 DOI。
- **URL**：[敏捷宣言原则官方页](https://agilemanifesto.org/principles.html)。
- **Source type**：官方规范性文本。
- **read_status**：`access_failed`。**实际读到范围**：无页面文本。**claim_status**：`unverified`；`experiment_status: not-run`。
- **原文定位与短摘录**：计划检查 technical excellence/good design、simplicity、sustainable development 等原则，但未取得原文；**本记录不提供未经读取的引文或编号**。
- **方法/样本**：不适用，规范文本不是效果实验。
- **发现/限制**：本批没有新增正文发现；不能凭熟悉宣言就声称已复核其与软件工艺的精确文本关系。计划以简洁性原则检查“工艺必然等于增加设计”的说法，但当前只是下一步研究任务。
- **项目相关性**：用于后续区分技术卓越与不必要设计，不把本轮未读原则直接当论证依据。
- **允许措辞**：“已尝试读取官方敏捷原则页但访问失败，文本对照尚未完成。”
- **禁止更强措辞**：“本轮已用官方原文确认全部历史关系”“敏捷排斥工艺/工艺纠正敏捷必然成立”。
- **权利**：官方文本，具体版权许可本轮未读。

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

## 综合：经验发现、价值主张与风险不能混写

1. **经验研究候选**：A01关注审美判断在组织中的实际使用；A02比较量化代理指标；A03做概念综合并结合纵向案例。这三类方法回答的问题不同，不能汇成一个“美代码必然更好”的统一实验证明。
2. **规范/理论候选**：A05/A06说明共同体倡导什么；A07解释为什么工作品质可能具有内在价值。这些文本即使完整读过，也不能单独证明可读性、质量或生产率改善。
3. **过度设计**：本轮没有读到指定作者讨论 overengineering 的原段，因此不把其归为已确认发现。作为竞争解释，追求个人欣赏的抽象与形式，可能与具体任务的简洁、可修改性冲突；需要真实变更任务与必要性论证，不能以“工艺”二字豁免检验。这是研究者提出的风险假设。
4. **规范排斥**：A01的索引线索涉及执行本地惯例和新人社会化；“规范协调”与“排斥不同做法/人群”不能直接画等号。可以把后者列为待查问题，不能声称已证实身份歧视。A03的共享文化亦不能自动说明文化必然包容。
5. **文化差异**：Yandex的俄语现场不等于全世界开发者；A03的金融领域案例也不等于游戏、教育或开源社区。当前未见跨文化对照证据，因此“普遍审美标准”和“各文化必然不同”都不能冒充本批发现。
6. **重复计数**：A03出现在A04中不形成独立复现；同一论文的出版社页、作者稿、大学库副本也不是三项独立证据。

## 论断晋升表

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

## 最小后续动作与证据缺口

- **优先级1**：通过用户合法提供的开放全文/机构授权材料，读A03的§5/Fig.3及方法、案例章节；核实四主题、17/47与七年案例的具体含义。再读A01方法、发现与讨论，核实哪些是观察、哪些是作者解释。
- **优先级2**：读A02模型定义及结果表，确认是否有新的人类评价、代码抽样单位与统计控制；不要在此之前引用0.59/0.33为确定结论。
- **优先级3**：读A04综合章节和未来工作，回答AI展望是否实际存在及其措辞强度；这不扩展为AI研究。
- **优先级4**：恢复A05/A06官方文本；为XP历史关系补一份合法可得的一手作者说明。对A07取得2008版p.9及上下文的合法节选。当前任务中的“一手理论正文阅读”与“敏捷/XP完整关系核验”均未完成，不能隐去。
- **停止决定**：本批 stop，等待可读正文；不因没有全文而循环检索，不将这份备忘录晋升为已核验报告。
- **文件校验范围**：只做本地结构/标记检查，不等于文献内容正确；未在Obsidian图形界面验证阅读视图。

## Sources（主要原始来源入口）

- [Fedorova, Mazmanian & Dourish — SAGE](https://journals.sagepub.com/doi/10.1177/01622439241245746)
- [Coleman — 出版社记录](https://thesai.org/Publications/ViewPaper?Code=IJACSA&Issue=9&SerialNo=2&Volume=9)
- [Sundelin et al. — DOI](https://doi.org/10.1145/3468504)
- [Sundelin et al. — BTH/DiVA研究记录](https://bth.diva-portal.org/smash/project.jsf?pid=project%3A2667)
- [Sundelin博士论文 — BTH/DiVA](https://bth.diva-portal.org/smash/get/diva2%3A1997635/FULLTEXT01.pdf)
- [Manifesto for Software Craftsmanship — 官方](https://manifesto.softwarecraftsmanship.org/)
- [Principles behind the Agile Manifesto — 官方](https://agilemanifesto.org/principles.html)
- [Sennett — Yale University Press（2009平装版页）](https://yalebooks.yale.edu/book/9780300151190/the-craftsman/)


## Batch01-A 原文补读更新（2026-11-11）

### A01 — Fedorova et al. (2025 issue)

已读取 SAGE 公开 PDF 全文。研究在 2014 年 Yandex 莫斯科办公室进行约三个月田野工作，包含 26 名程序员半结构化访谈和 4 次管理者／专家访谈。其贡献是解释“美／丑”如何作为组织语言参与团队规范、专业身份和新人社会化；不是对代码质量进行量化的实验。

**修订：** 不再把这篇文章概括成“研究证明优美代码提升可维护性”。它证明的是审美判断在编程实践中的社会组织作用。

### A02 — Coleman (2018)

已读取期刊 PDF 全文。样本来自 GNU Coreutils 的约 1,043 个单函数 C 文件，约 53,000 行；作者定义 11 个美学因素，与 8 个可读性模型进行比较。

**修订：** `beauty factor` 是作者提出的特定形式／分形维度代理指标，不是人类程序员对代码美感的直接评价。研究没有测量真实维护任务的正确率、缺陷或长期演进成本。应作为探索性量化尝试，而不是代码美学的标准测量法。

### A03 — Sundelin et al. (2022)

已读取作者公开稿全文，并用 BTH 博士论文的书目记录核对最终卷期与 DOI。研究综合 18 篇论文、11 本书和一个约七年的 Ericsson 金融软件案例，提出四主题、17 原则、47 项层级实践。

**修订：** 47 项实践不是“经大规模实验证明的 47 条最佳规范”。论文的核心价值是构建软件工艺的分类与工业案例解释；其单一案例、作者 insider perspective 和非因果研究设计必须同时报告。

### A04 — Sundelin (2025)

对博士论文摘要、目录、Paper I 与 Future Work 相关章节进行了定点阅读。AI/LLM 部分讨论未来工程师如何管理 LLM、如何将需求转成可自动验证的边界，并明确将长期影响列为开放问题。

**修订：** 这不是 AI 编码效果实证研究，不能引用为 AI 已经提高或降低代码质量的证据。

### A05 / A06 — 宣言与敏捷原则

- Software Craftsmanship Manifesto（2009）为规范性价值声明，强调不仅要能工作，也要 well-crafted software、持续增加价值、形成专业共同体和生产性伙伴关系；它不是实证研究。
- Agile Manifesto Principles 官方页面明确包含持续关注技术卓越与良好设计、简洁、定期反思等原则。软件工艺运动与敏捷并非简单对立关系。

详见 [07_Batch01-A核心文献原文核验与证据修订记录](batch01-a-verification.md) 与 [sources](../evidence/sources.md)。
