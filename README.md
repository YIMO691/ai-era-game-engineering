# AI 时代游戏客户端工程研究

以 Unity / C# 商业游戏客户端为实践场景，研究如何定义问题、理解系统、做出取舍，并用证据对交付结果负责，而不是比较代码产量或积累技术名词。

## 从这里开始

- **了解项目：** [项目宗旨：从实现代码，到理解系统与承担工程结果](docs/project-manifesto.md)。
- **阅读最新文章：** [代码优美论：AI时代，为什么仍要把代码写好](research/code-aesthetics/final/article.md)。从品质动机、精益迁移和UI旧回包案例，讨论AI成本、工程取舍与停止条件。
- **按问题查找：** [六个研究专题](research/README.md)。各专题保留自己的来源、适用边界和未验证项。

**文章定稿、公开入库和研究验证是三件事。** 代码优美论v1.0是证据受限的批判性综合文章，不是实证论文；证据状态仍为PARTIAL，人工研究审核待完成，没有运行代码或读者实验。原始导入报告的引用缺口也仍保留，详见[导入与证据缺口说明](docs/import-notes.md)。

## 研究专题

| 专题 | 主要问题与阅读入口 |
|---|---|
| [代码优美与工程品质](research/code-aesthetics/README.md) | [最终文章](research/code-aesthetics/final/article.md)：为什么写好代码，何时抽象、重构或停止；[证据与取舍](research/code-aesthetics/final/evidence-notes.md) |
| [Unity异步任务生命周期](research/unity-task-lifetime/README.md) | 销毁、对象池复用、取消与旧回包回写的责任边界 |
| [客户端代码质量](research/client-code-quality/README.md) | 如何判断质量、开展审查，并把案例用于学习与训练 |
| [工程判断与人机协作](research/engineering-judgment/README.md) | 决策模型、源码阅读、案例与能力评估的边界 |
| [AI代码质量工作流](research/ai-code-quality-workflow/README.md) | 工具能力、证据、最小采用路线及Unity/C#适配 |
| [AI-CQEP工程实践文稿与模板](research/ai-cqep/README.md) | 工程实践体系、采用说明与通用契约模板 |

专题不是已验证结论库，模板不是已部署配置。需要追溯研究过程时，再阅读专题内的来源账本、审校记录和设计草案；不必先完成实验才能阅读最终文章。

## 核心问题与方法

- 什么行为与结果，能区分“实现功能”和“对系统负责”？
- 架构、性能、资源所有权与异步生命周期如何相互制约？
- AI改变哪些成本，哪些约束、判断与交付责任仍须明确？
- 什么依据支持一次改进，什么反例要求修订，做到哪里应该停止？

研究从具体问题与约束出发，区分来源事实、案例、综合推论和待验证假设。需要主张实际效果时，提供相应实验或明确缺口；概念文章则保留其有限结论，不为定稿无限扩张研究。选择Unity/C#是为了落到运行时、设备、生命周期和生产约束，不预设结论适用于所有软件领域。

## 方法、来源与历史

| 文档 | 用途 |
|---|---|
| [研究方法](docs/research-method.md) | 证据规则、实验要求与可复制记录 |
| [来源登记](research/sources.md) | 原始材料缺口及各专题来源入口 |
| [路线图](docs/roadmap.md) | 早期研究路线与验收条件；当前专题进展以各自入口为准 |
| [原始深度研究报告](docs/manifesto.md) | 保真研究输入，不等同于项目宗旨或已证实成果 |
| [历史草稿](docs/historical/deep-research-draft.md) | 追溯早期能力模型，不作为现行标准 |
| [公开范围与维护](research/PUBLICATION.md) | 白名单导出、单一编辑源及发布边界 |
| [Obsidian 阅读说明](docs/obsidian.md) | 本地入口与公开快照的关系 |
| [贡献指南](CONTRIBUTING.md) | 范围、引用、AI披露与检查要求 |
| [变更记录](CHANGELOG.md) | 已发生的改动和实际验证结果 |

私有研究版本是编辑源，公开仓库保存经授权的可追溯快照，不双向自动同步。原报告中的能力分级是待检验提案，不是行业标准或认证量表；不合并不同报告的模型。

## 本地检查

在仓库根目录执行，无需安装额外依赖：

```bash
python -I -m unittest discover -s tests -p 'test_*.py' -v
python -I scripts/check_docs.py
```

检查只覆盖支持的文档约定、仓库内链接及保真导入件，不证明研究事实、外链内容、Unity行为或页面渲染正确。远端结果见[GitHub Actions](https://github.com/YIMO691/ai-era-game-engineering/actions)。

## 参与与许可

欢迎提供可定位的来源、反例、可复现实验及有依据的修订。不为活跃度更新，不承诺会话外自动持续研究。

原创文档与图示采用CC BY 4.0，原创独立代码、测试和工作流采用MIT，署名YIMO691。适用范围与第三方例外以[LICENSE](LICENSE)为准；缺失引用不意味着第三方材料获得重新授权。
