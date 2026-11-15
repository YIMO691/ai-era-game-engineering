# 附录C　核心命题索引

> **用途**：书的索引。全书反复使用的 22 条承重命题列在这里，每条注明它是什么性质的主张、目前的状态、在哪几章展开、证据在哪里，以及什么结果会推翻它。读完一章后回到这里，可以看到它与其他章共享了哪些判断。

阅读时请注意两点。第一，“有支撑”只表示在所列证据范围内成立，不表示经过人工审核或实验；全书目前没有执行过任何实验。第二，“待验证假设”和“受质疑”的命题单独列在最后，它们是下一阶段研究最需要回答的问题。

命题按[第8章](08-ownership-evidence-bound.md)的三条轴归类：**责任**（此刻归谁、何时失效、谁承担后果）、**证据**（凭什么相信、证据能否支持这类主张）、**限度**（做到哪里为止、深度是否与后果相称）。一条命题可以同时落在几条轴上，这里按主要的一条归类。实践规则编号指[附录A](appendix-a-practice-rules.md)。

## 一、责任

**K-001**　异步、复用与生命周期中的“完成”可分解为执行位置、提交资格与资源归属等相互独立的问题；任一问题的肯定答案不能推出其他问题的答案。

- 性质与状态：综合推论，有支撑
- 展开于：[第2章](02-why-write-good-code.md)、[第3章](03-the-late-result.md)、[第4章](04-client-code-quality.md)、[第5章](05-engineering-judgment.md)；实践规则 G-12
- 证据：[第3章（第 1–2 节：三个问题与固定源码的四条边界）](03-the-late-result.md)；[附录D（C1/C2 的反例结构）](appendix-d-cases.md)；[第8章（命题一的跨专题对齐）](08-ownership-evidence-bound.md)
- 什么会推翻它：在实际项目缺陷样本中，这三类问题经常同时由同一机制决定，或分解无法区分主要缺陷。

**K-002**　不再需要一个结果，不等于不再负责这个结果；取消只是请求减少工作，不证明工作已停止、不会返回资源或无需清理。

- 性质与状态：综合推论，有支撑
- 展开于：[第3章](03-the-late-result.md)、[第4章](04-client-code-quality.md)、[第7章](07-ai-cqep-protocol.md)；实践规则 G-13、G-17、G-18
- 证据：[第3章（第 2.1、4 节：取消入口与资源交接协议）](03-the-late-result.md)；[第4章（8.3 超时要说清是哪一层停止）](04-client-code-quality.md)；[第7章（Unity/C# 适配案例的契约）](07-ai-cqep-protocol.md)
- 什么会推翻它：所用运行时在取消后保证不再产生需要释放的结果，且该保证有版本化文档或源码支持。

**K-003**　提交资格应由业务 owner 管理的请求身份（代次或唯一标识）判断；对象仍有效不推出结果仍可提交。

- 性质与状态：逻辑论证，有支撑
- 展开于：[第2章](02-why-write-good-code.md)、[第3章](03-the-late-result.md)、[第7章](07-ai-cqep-protocol.md)；实践规则 G-14、G-15、G-16
- 证据：[第3章](03-the-late-result.md)；[第2章（第五节贯穿案例）](02-why-write-good-code.md)
- 什么会推翻它：出现不依赖请求身份、仍能区分新旧结果的通用机制，且成本更低。

**K-004**　UniTask 2.5.10 的限定 DelayPromise 中途取消路径中，取消包装的 canceled 分支绕过底层 GetResult，未走到已读的 TryReturn 归池路径。

- 性质与状态：来源事实，有支撑。静态阅读，未运行；不能据此声称实测内存泄漏。
- 展开于：[第5章](05-engineering-judgment.md)
- 证据：[附录D](appendix-d-cases.md)；[第5章（5.1 节）](05-engineering-judgment.md)
- 什么会推翻它：运行可控复现后，该路径实际完成了归池；或所读版本与固定 SHA 不符。

**K-005**　NGO 1.9.1 中，业务 OnNetworkDespawn 之后旧网络流程仍有读取；收到生命周期通知不等于实例可立即复用。

- 性质与状态：来源事实，有支撑。静态阅读，未运行。
- 展开于：[第5章](05-engineering-judgment.md)；实践规则 G-21
- 证据：[附录D](appendix-d-cases.md)；[第5章（5.2 节）](05-engineering-judgment.md)
- 什么会推翻它：运行观测显示通知之后不再有对旧实例的访问。

**K-015**　AI 改变的是工程成本的分布，不改变谁接受风险、谁确认约束、谁决定发布与回滚。

- 性质与状态：价值或规范立场，有支撑
- 展开于：[第2章](02-why-write-good-code.md)、[第5章](05-engineering-judgment.md)、[第7章](07-ai-cqep-protocol.md)；实践规则 G-50、G-51
- 证据：[第2章（第六节）](02-why-write-good-code.md)；[第8章（命题五）](08-ownership-evidence-bound.md)

## 二、证据

**K-006**　主张什么，就需要什么类型的证据；证据的身份（官方、源码、论文）与它能否支持这一类主张要分开判断。

- 性质与状态：价值或规范立场，有支撑
- 展开于：[第2章](02-why-write-good-code.md)、[第5章](05-engineering-judgment.md)、[第7章](07-ai-cqep-protocol.md)；实践规则 G-32
- 证据：[附录H（如何描述证据）](appendix-h-research-method.md)；[第8章（命题二）](08-ownership-evidence-bound.md)
- 什么会推翻它：作为规范立场不由实验证明；若团队实践中按此执行并不降低虚假完成，则其实用价值需要重估。

**K-007**　编辑、人工审核、证据、实验与发布五种状态彼此正交，任一状态不能推出另一状态。

- 性质与状态：概念区分，有支撑
- 展开于：[第2章](02-why-write-good-code.md)、[第5章](05-engineering-judgment.md)；实践规则 G-33
- 证据：[第8章（命题二与状态词表）](08-ownership-evidence-bound.md)；[附录B（状态词表）](appendix-b-glossary.md)
- 什么会推翻它：出现两种状态在本仓库语境下总是同时变化、无需分别记录的情况。

**K-008**　验证的独立性指错误来源不同，而不是审查者身份不同；多个模型或多次询问一致不构成独立验证。

- 性质与状态：逻辑论证，有支撑
- 展开于：[第2章](02-why-write-good-code.md)、[第5章](05-engineering-judgment.md)、[第7章](07-ai-cqep-protocol.md)；实践规则 G-36、G-48
- 证据：[人机职责与独立验证](../archive/research/engineering-judgment/human-ai-collaboration-handbook.md)；[第2章（第六节：更多候选不等于更多独立证据）](02-why-write-good-code.md)
- 什么会推翻它：有证据表明不同模型在给定任务上的错误高度不相关。

**K-009**　样例、注释与测试本身也要被审查；测试通过只证明它检查的那部分成立。

- 性质与状态：特定案例，有支撑
- 展开于：[第5章](05-engineering-judgment.md)；实践规则 G-34
- 证据：[附录D](appendix-d-cases.md)

**K-014**　AI 节省的时间转为品质收益需要三个条件同时成立：净节约确实存在、部分资源确实分配给品质、这次投入对具体问题有效。

- 性质与状态：逻辑论证，有支撑
- 展开于：[第2章](02-why-write-good-code.md)；实践规则 G-52
- 证据：[第2章（第六节：从生成收益到品质收益）](02-why-write-good-code.md)

**K-016**　Peng 等 v1 的标准化 JavaScript HTTP server 实验中，完成者耗时减少 55.8%（95% CI 21%–89%）；研究未测代码质量。

- 性质与状态：来源事实，有支撑。只在该研究设定内成立，不推广到维护或学习收益。
- 展开于：[第5章](05-engineering-judgment.md)
- 证据：[第5章（第 8 节）](05-engineering-judgment.md)；[正文已读](../archive/research/engineering-judgment/ai-evidence-notes.md)

**K-017**　METR 2026-02-24 跟进的两个子集中心估计显示耗时下降，但区间跨零，并披露了选择、完成、计时与产物差异。

- 性质与状态：来源事实，有支撑。难以代表当前净效应。
- 展开于：[第5章](05-engineering-judgment.md)
- 证据：[第5章（第 8 节）](05-engineering-judgment.md)；[正文已读](../archive/research/engineering-judgment/ai-evidence-notes.md)

**K-018**　项目宗旨所引的两项 AI 效率数字（约 26% 提升、约 19% 变慢）可以作为论据使用。

- 性质与状态：来源事实，受质疑。宗旨正文与来源登记的未核状态存在张力，见阶段性综合 7.5 节；待所有者决定如何处理宗旨正文。
- 展开于：[第1章](01-from-code-to-responsibility.md)
- 证据：[第1章（正文引用）](01-from-code-to-responsibility.md)；[Q-01/Q-02 未核验，URL 未提供](../archive/research/sources.md)
- 什么会推翻它：核对原论文后，估计对象、版本或口径与宗旨表述不符。

**K-021**　把项目约束、最小修改、可执行检查、定向审查和反馈接成工作链，比新增生成工具或全套插件更能改善 AI 参与的交付质量。

- 性质与状态：待验证假设，提出。尚无对照数据。
- 展开于：[第6章](06-ai-quality-chain.md)、[第7章](07-ai-cqep-protocol.md)；实践规则 G-41、G-48、G-49
- 证据：[第6章（结论）](06-ai-quality-chain.md)；[第7章（11.2 如何检验）](07-ai-cqep-protocol.md)
- 什么会推翻它：在相同任务的对照中，工作链组没有更少的缺陷或返工。

**K-022**　工程判断力可以通过“事前预测—外部反馈—新题迁移”的产物来训练与观察，而不是按工龄或阅读量评价。

- 性质与状态：待验证假设，提出。未验证效度与效果。
- 展开于：[第5章](05-engineering-judgment.md)；实践规则 G-54、G-55
- 证据：[第5章（第 9 节）](05-engineering-judgment.md)；[十四域×五级与十二周设计](../archive/research/engineering-judgment/training-and-assessment-handbook.md)
- 什么会推翻它：控制领域熟悉性后，训练组在未见任务上的预测与错误发现没有改善。

## 三、限度

**K-010**　分析、审查与验证的深度应由后果、传播、未知与可检测/可恢复性决定，任一维度为高即升级，不取平均；代码行数不是风险指标。

- 性质与状态：综合推论，有支撑。未证明最优成本。
- 展开于：[第2章](02-why-write-good-code.md)、[第5章](05-engineering-judgment.md)、[第7章](07-ai-cqep-protocol.md)；实践规则 G-7、G-9、G-10、G-11
- 证据：[第 3–4 节：分析深度与分级协议](../archive/research/engineering-judgment/decision-handbook.md)；[第7章（4.1 风险裁剪）](07-ai-cqep-protocol.md)；[第8章（命题三）](08-ownership-evidence-bound.md)
- 什么会推翻它：在真实项目中按此分级并不比按改动规模分级更好地预测缺陷后果。

**K-011**　可回滚的代码不等于可撤回的经济、数据或玩家损害；后者的风险不能用代码回滚能力来降级。

- 性质与状态：逻辑论证，有支撑
- 展开于：[第5章](05-engineering-judgment.md)、[第7章](07-ai-cqep-protocol.md)；实践规则 G-8、G-38
- 证据：[第5章（1 节关键修订第 5 条）](05-engineering-judgment.md)；[第 4 节：最小有效分级协议](../archive/research/engineering-judgment/decision-handbook.md)

**K-012**　工程判断的 Tier 1–3 与 AI-CQEP 的 L/M/H 在触发逻辑上可以对齐；差异在于 AI-CQEP 的常规功能无论风险都先审方案。

- 性质与状态：综合推论，提出。对齐由阶段性综合提出，未经人工审核。
- 展开于：[第5章](05-engineering-judgment.md)、[第7章](07-ai-cqep-protocol.md)
- 证据：[第8章（4.3 本文的对齐）](08-ownership-evidence-bound.md)；[附录B（变更风险分级）](appendix-b-glossary.md)
- 什么会推翻它：两套分级对同一批变更给出系统性不同的档位。

**K-013**　停止条件应在事前写下；“关键未知的合理变化不会改变选择”是判断能否停止的可回答问题。

- 性质与状态：综合推论，有支撑。效果待验证。
- 展开于：[第2章](02-why-write-good-code.md)、[第5章](05-engineering-judgment.md)；实践规则 G-37、G-39
- 证据：[第 5 节：S1–S6 停止规则](../archive/research/engineering-judgment/decision-handbook.md)；[第2章（第七节停止信号）](02-why-write-good-code.md)
- 什么会推翻它：事前写下停止条件并不减少过度分析或过早交付。

**K-019**　追求品质有内在满足、对他人的责任、工具性收益三种理由；动机是否值得尊重、改动是否有效、投入是否适当需分别判断。

- 性质与状态：概念区分，有支撑
- 展开于：[第2章](02-why-write-good-code.md)；实践规则 G-2
- 证据：[第2章（第二节）](02-why-write-good-code.md)

**K-020**　判断重复与抽象应看是否因同一原因而变化、隐藏了什么知识，而不是出现次数或外观整洁。

- 性质与状态：综合推论，有支撑
- 展开于：[第2章](02-why-write-good-code.md)、[第4章](04-client-code-quality.md)、[第5章](05-engineering-judgment.md)、[第7章](07-ai-cqep-protocol.md)；实践规则 G-24、G-25
- 证据：[第2章（第三节）](02-why-write-good-code.md)；[第4章（第 6 节：抽象与必要复杂性）](04-client-code-quality.md)；[第 6 节：抽象与复用](../archive/research/engineering-judgment/decision-handbook.md)；[第7章（5.3 复用与新增抽象的闸门）](07-ai-cqep-protocol.md)
- 什么会推翻它：有对照数据表明按出现次数抽象的维护成本不高于按变化原因抽象。

## 四、待回答的问题

| 编号 | 状态 | 缺口 |
|---|---|---|
| K-012 | 提出 | 对齐由阶段性综合提出，未经人工审核。 |
| K-018 | 受质疑 | 宗旨正文与来源登记的未核状态存在张力，见阶段性综合 7.5 节；待所有者决定如何处理宗旨正文。 |
| K-021 | 提出 | 尚无对照数据。 |
| K-022 | 提出 | 未验证效度与效果。 |

维护方式：修订某条命题时，保留原表述，在条目下追加“修订（日期）：改了什么、为什么”，编号永不复用；被推翻的命题标为“已推翻”并保留。

返回[目录](../README.md)。
