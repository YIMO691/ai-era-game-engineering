# 研究档案

这里存放从本书主线退役的文件。它们没有被删除：内容、相对位置与彼此的链接都保留，原研究专题的目录结构也保持不变，正文引用的来源和证据仍然指向这里。退役的理由只有一个：**读者不需要先读它们，也能读懂本书**。

如果你认为某份文件应该回到正文或附录，请在 PR 或议题中指出；恢复只需要把文件移回 `book/` 并加入[目录](../README.md)。退役与整理的决定见[决策记录](../docs/decisions.md) D-005。

各专题目录中的 `export-manifest.json` 与 `meta.json` 是导出来源与上一轮知识库设计的数据，同样只作追溯，下表不逐一列出。

## 一、延伸阅读：可以继续深入的材料

这些文件内容有价值，但与正文或附录重叠较多，或篇幅超出主线需要。想在某一章上深入时从这里继续。

| 文件 | 内容与退役理由 | 对应章节 |
|---|---|---|
| [decision-handbook.md](research/engineering-judgment/decision-handbook.md) | 第5章的完整版：M2/M5 模型、分级协议、抽象与重构、技术债 | 第5章 |
| [source-reading-handbook.md](research/engineering-judgment/source-reading-handbook.md) | 进入陌生工程、阅读源码与还原设计理由的方法 | 第5章 |
| [human-ai-collaboration-handbook.md](research/engineering-judgment/human-ai-collaboration-handbook.md) | 人机职责矩阵、委派合同与独立验证阶梯 | 第5、6章 |
| [training-and-assessment-handbook.md](research/engineering-judgment/training-and-assessment-handbook.md) | 十四域×五级与十二周训练设计（未验证） | 第5章 |
| [code-quality-guide.md](research/client-code-quality/code-quality-guide.md) | 第4章的实用指南版，与正文和附录E重叠 | 第4章 |
| [unity-csharp-examples.md](research/client-code-quality/unity-csharp-examples.md) | 4 个固定源码案例与 7 个原创教学案例 | 第4章 |
| [training-route.md](research/client-code-quality/training-route.md) | 质量训练路线（未执行） | 第4章 |
| [ui-lifecycle-and-craft.md](research/code-aesthetics/guides/ui-lifecycle-and-craft.md) | UI 生命周期与工艺的实践指南 | 第2章 |
| [capability-matrix.md](research/ai-code-quality-workflow/capability-matrix.md) | 候选工具的能力矩阵 | 第6章 |
| [adoption-plan.md](research/ai-code-quality-workflow/adoption-plan.md) | 采用方案（设计，未执行） | 第6章 |
| [claude-code-configuration.md](research/ai-code-quality-workflow/claude-code-configuration.md) | 配置设计（设计，未部署） | 第6章 |
| [implementation-guide.md](research/ai-code-quality-workflow/implementation-guide.md) | 实施指南（设计，未执行） | 第6章 |
| [unity-csharp-adaptation.md](research/ai-code-quality-workflow/unity-csharp-adaptation.md) | 工作链的 Unity/C# 适配 | 第6章 |
| [PROJECT-CONTRACT-TEMPLATE.md](research/ai-cqep/PROJECT-CONTRACT-TEMPLATE.md) | 项目工程契约模板 | 第7章 |
| [CLAUDE-ADOPTION.md](research/ai-cqep/CLAUDE-ADOPTION.md) | 协议的采用说明与任务模板 | 第7章 |

## 二、研究记录：来源、证据与审校

正文引用的来源、证据笔记与审校结论都在这里，追溯某个判断的出处时使用。它们是研究过程的记录，不是阅读材料。

| 文件 | 内容与退役理由 |
|---|---|
| [sources.md](research/sources.md) | 早期两份原始报告的来源缺口登记（含 Q-01/Q-02） |
| [sources.md](research/unity-task-lifetime/sources.md) | 第3章的来源登记 |
| [plan.md](research/unity-task-lifetime/plan.md) | 第3章原研究计划 |
| [review.md](research/unity-task-lifetime/review.md) | 第3章原审查记录 |
| [sources.md](research/client-code-quality/sources.md) | 第4章的来源登记 |
| [third-party-notices.md](research/client-code-quality/third-party-notices.md) | 第4章引用的第三方材料声明 |
| [plan.md](research/client-code-quality/plan.md) | 第4章原研究计划 |
| [review.md](research/client-code-quality/review.md) | 第4章原审查记录 |
| [sources.md](research/engineering-judgment/sources.md) | 第5章的完整书目、版本与允许措辞 |
| [research-plan.md](research/engineering-judgment/research-plan.md) | 第5章原研究计划 |
| [research-review.md](research/engineering-judgment/research-review.md) | 第5章审查结果与剩余阻塞 |
| [baseline-audit.md](research/engineering-judgment/baseline-audit.md) | 第5章对早期四份基线的审计 |
| [ai-evidence-notes.md](research/engineering-judgment/ai-evidence-notes.md) | AI 实证研究的阅读笔记 |
| [cognition-evidence-notes.md](research/engineering-judgment/cognition-evidence-notes.md) | 认知与学习文献的检索笔记（仅片段） |
| [unity-source-evidence-notes.md](research/engineering-judgment/unity-source-evidence-notes.md) | UniTask 与 NGO 源码证据笔记 |
| [sources.md](research/ai-code-quality-workflow/sources.md) | 第6章的来源登记 |
| [evidence-official.md](research/ai-code-quality-workflow/evidence-official.md) | 第6章取证附录：官方生态 |
| [evidence-ecc.md](research/ai-code-quality-workflow/evidence-ecc.md) | 第6章取证附录：ECC |
| [evidence-openhands.md](research/ai-code-quality-workflow/evidence-openhands.md) | 第6章取证附录：OpenHands |
| [evidence-tools.md](research/ai-code-quality-workflow/evidence-tools.md) | 第6章取证附录：质量工具 |
| [review.md](research/ai-code-quality-workflow/review.md) | 第6章原审查记录 |
| [evidence-notes.md](research/code-aesthetics/final/evidence-notes.md) | 第2章的证据与取舍说明 |
| [sources.md](research/code-aesthetics/evidence/sources.md) | 代码优美论的来源登记 |
| [conclusion.md](research/code-aesthetics/audit/conclusion.md) | 代码优美论内容审校结论 |
| [claim-evidence-matrix.md](research/code-aesthetics/audit/claim-evidence-matrix.md) | 代码优美论主张—证据矩阵 |
| [revision-decisions.md](research/code-aesthetics/audit/revision-decisions.md) | 代码优美论修订决定 |
| [review.md](research/code-aesthetics/audit/review.md) | 代码优美论审校记录 |
| [aesthetics-craft.md](research/code-aesthetics/audit/aesthetics-craft.md) | 审校分项：美学与工艺 |
| [cognition.md](research/code-aesthetics/audit/cognition.md) | 审校分项：认知 |
| [lean.md](research/code-aesthetics/audit/lean.md) | 审校分项：精益 |
| [quality-ai.md](research/code-aesthetics/audit/quality-ai.md) | 审校分项：质量与 AI |
| [foundations.md](research/code-aesthetics/batch01/foundations.md) | 第一批：思想基础与理论溯源 |
| [bibliography.md](research/code-aesthetics/batch01/bibliography.md) | 第一批：注释书目 |
| [concept-map.md](research/code-aesthetics/batch01/concept-map.md) | 第一批：概念图 |
| [framework.md](research/code-aesthetics/batch01/framework.md) | 第一批：框架 |
| [cognition.md](research/code-aesthetics/batch01/cognition.md) | 第一批：认知 |
| [research-plan.md](research/code-aesthetics/batch02/research-plan.md) | 第二批：实验计划（未执行） |
| [entry-gates.md](research/code-aesthetics/batch02/entry-gates.md) | 第二批：入组门槛 |
| [constructs.md](research/code-aesthetics/batch02/constructs.md) | 第二批：构念定义 |
| [scoring-protocol.md](research/code-aesthetics/batch02/scoring-protocol.md) | 第二批：评分协议 |
| [ui-request-materials.md](research/code-aesthetics/batch02/ui-request-materials.md) | 第二批：实验材料 |
| [intake-record.md](research/code-aesthetics/history/intake-record.md) | 历史：接收记录 |
| [prior-crosscheck.md](research/code-aesthetics/history/prior-crosscheck.md) | 历史：与早期报告的交叉核对 |
| [batch01-a-verification.md](research/code-aesthetics/history/batch01-a-verification.md) | 历史：第一批核验 |
| [aesthetics-evidence.md](research/code-aesthetics/history/aesthetics-evidence.md) | 历史：美学证据 |
| [cognition-evidence.md](research/code-aesthetics/history/cognition-evidence.md) | 历史：认知证据 |
| [lean-evidence.md](research/code-aesthetics/history/lean-evidence.md) | 历史：精益证据 |

## 三、被取代或重复的文件

这些文件的内容已经并入正文、附录或本书的目录，单独保留只会让读者看到两份相近的东西。

| 文件 | 内容与退役理由 |
|---|---|
| [README.md](research/README.md) | 旧的研究专题目录，由本书目录取代 |
| [README.md](research/unity-task-lifetime/README.md) | 旧专题入口，由第3章导读取代 |
| [README.md](research/client-code-quality/README.md) | 旧专题入口，由第4章导读取代 |
| [README.md](research/engineering-judgment/README.md) | 旧专题入口，由第5章导读取代；含运行模型名（见决策记录 P4） |
| [README.md](research/ai-code-quality-workflow/README.md) | 旧专题入口，由第6章导读取代 |
| [README.md](research/ai-cqep/README.md) | 旧专题入口，由第7章导读取代 |
| [README.md](research/code-aesthetics/README.md) | 旧专题入口，由第2章导读取代 |
| [research-overview.md](research/engineering-judgment/research-overview.md) | 第5章的摘要版，与正文重复 |
| [blog.md](research/unity-task-lifetime/blog.md) | 第3章的教学文章版，与正文重复 |
| [late-icon-callback-tutorial.md](research/engineering-judgment/late-icon-callback-tutorial.md) | 迟到回调教程，与第2、3章案例重复 |
| [roadmap.md](docs/roadmap.md) | 早期路线图，由第8章“下一阶段议程”取代 |
| [knowledge-architecture.md](docs/knowledge-architecture.md) | 知识库架构设计，由“整理成一本书”的决定取代（决策记录 D-005） |
| [README.md](knowledge/README.md) | 生成的知识地图，由本书目录与附录C取代 |
| [claims.json](knowledge/claims.json) | 命题登记数据，内容已写入附录C |
| [vocabulary.json](knowledge/vocabulary.json) | 受控词表，随知识地图一并退役 |
| [PUBLICATION.md](research/PUBLICATION.md) | 公开导出的授权与范围记录；编辑源约定已由决策记录 D-002 取代 |
| [PUBLICATION.md](research/code-aesthetics/PUBLICATION.md) | 代码优美论的发布记录 |
| [obsidian.md](docs/obsidian.md) | Obsidian 本地阅读说明，依赖私有笔记库入口 |

## 四、原始输入与导出来源

研究开始时用户提供的两份报告（逐字节保真，引用与结论均未核验），以及各专题从私有研究稿导出时的来源清单。只用于追溯，不作为现行观点。

| 文件 | 内容与退役理由 |
|---|---|
| [manifesto.md](imports/manifesto.md) | 原始深度研究报告（保真导入） |
| [deep-research-draft.md](imports/deep-research-draft.md) | 早期草稿（保真导入） |
| [imports.json](imports/imports.json) | 两份导入件的哈希登记 |
| [import-notes.md](imports/import-notes.md) | 导入与证据缺口说明 |

返回[目录](../README.md)。
