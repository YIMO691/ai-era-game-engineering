# 代码优美论：最终文章与研究材料

**先读：[代码优美论：AI时代，为什么仍要把代码写好](final/article.md)**。这篇v1.0文章从品质动机出发，经由精益迁移、UI请求案例与AI成本，讨论何时改进、何时停止；可独立阅读，不以完成后续实验为门槛。

> [!WARNING]
> **文章写作已定稿；证据状态仍为PARTIAL，人工研究审核仍pending，代码与读者实验未执行。** 最终文章是批判性综合，不是实证论文或编码标准。参见[证据与取舍说明](final/evidence-notes.md)；追溯原研究缺口时阅读[内容审校结论](audit/conclusion.md)。

本课题研究：当需求与行为相同时，被认为更优美的代码是否帮助维护者正确理解和修改？收益在什么条件下存在，成本又何时超过收益？不预设简洁、抽象、工艺、精益或AI天然更好。

## 目录与阅读顺序

```text
code-aesthetics/
├── README.md                 当前入口与状态
├── PUBLICATION.md            公开范围、转换与验证记录
├── export-manifest.json      原文件身份与公开副本映射
├── final/                    v1.0文章、证据说明与独立导出清单
├── batch01/                  理论溯源、书目、概念与认知
├── batch02/                  研究计划、材料与评分草案
├── audit/                    当前独立审校、决策与审查
├── evidence/                 本课题唯一来源账本
├── guides/                   学习者阅读稿
└── history/                  前轮历史记录，不作当前认证
```

### 追溯研究材料

最终文章与[证据说明](final/evidence-notes.md)构成主要阅读路径。以下材料用于追溯和可选后续研究，不是文章阅读的前置任务。

1. [当前审校结论](audit/conclusion.md)：为何是PARTIAL、哪些原文仍缺失。
2. [思想基础与理论溯源](batch01/foundations.md)：品质动机、精益迁移、质量经济与AI成本。
3. [构念与测量草案](batch02/constructs.md)：把美感、理解、修改与成本分开。
4. [界面请求材料](batch02/ui-request-materials.md)：A/B中性版本及共同契约；**含两个版本的研究者母版，不可整份发给参与者**。
5. [评分与可行性协议](batch02/scoring-protocol.md)：**含答案，仅供研究者／自学核对**；13条轨迹都是预期值，不是运行结果。

### Batch01：理论与研究入口

- [核心文献注释书目](batch01/bibliography.md)
- [概念与理论关系图](batch01/concept-map.md)：Mermaid与文字替代；未做渲染验收。
- [初步理论框架](batch01/framework.md)
- [认知科学与程序理解](batch01/cognition.md)
- [来源账本](evidence/sources.md)：36项稳定来源编号，当前／历史阅读状态分层。
- [教学稿：从界面刷新谈工程品质](guides/ui-lifecycle-and-craft.md)

### Batch02：只推进一组最小材料

- [研究问题与计划](batch02/research-plan.md)
- [启动条件与证据依赖门](batch02/entry-gates.md)
- [构念与测量](batch02/constructs.md)
- [界面请求A/B材料及题面](batch02/ui-request-materials.md)
- [评分、数据字典与可行性协议](batch02/scoring-protocol.md)

材料使用C#风格伪代码，尚未固定编译环境、执行轨迹或招募参与者。若另行实施实验，应先实现共同契约验收；本轮文章已完成，不自动推进实验。单组材料不能证明抽象的一般效果或长期经济收益。

### 当前审校与可追溯决策

- [73条核心论断矩阵与八项命题挑战](audit/claim-evidence-matrix.md)
- [修订差异与决策](audit/revision-decisions.md)
- [内容审校结论](audit/conclusion.md)
- [事实、教学和设计审查](audit/review.md)
- 分支备忘录：[美学／工艺](audit/aesthetics-craft.md)、[精益](audit/lean.md)、[质量／AI](audit/quality-ai.md)、[认知](audit/cognition.md)。

本轮17次原文访问受安全检查阻断，24次搜索只作索引发现；12项重点来源未取得直接证据。文件校验和搜索结果不构成原文核验。

### 历史材料（不作为当前通过声明）

- [Batch01-A原文核验记录](history/batch01-a-verification.md)
- [前轮交叉核验与勘误](history/prior-crosscheck.md)
- [接收检查与归档记录](history/intake-record.md)
- 早期证据备忘录：[美学](history/aesthetics-evidence.md)、[精益](history/lean-evidence.md)、[认知](history/cognition-evidence.md)。

历史材料中的“全文已读”“PASS”“未发布”只描述原记录时点，不能覆盖当前PARTIAL。公开目录已转换链接、移除本机路径并添加状态说明，不是原研究包的字节保真存档；原行号不能直接用作公开副本行号。

## 公开与复用边界

[公开整理说明](PUBLICATION.md)列出许可、排除项、验证和AI协助范围；[研究材料清单](export-manifest.json)记录原26份输入与公开副本的SHA-256；[最终文章清单](final/export-manifest.json)另行记录v1.0正文与证据说明的两个文件，不覆盖历史记录。未上传ZIP、私人路径、提示词文件、原始会话、外部论文全文或本地检查点。

原创内容按[仓库许可](../../LICENSE)及[贡献指南](../../CONTRIBUTING.md)处理；第三方短引文和资料仍归原权利人。来源未核实不意味着获得重许可，也不能用于声称作者认可本框架。

返回[项目首页](../../README.md)；仓库级[来源入口](../sources.md)只索引本课题，不复制第二套来源账本。
