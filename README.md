# 一名 Unity 客户端工程师的成长：AI 时代的思考与学习

当 AI 让“写出代码”越来越便宜，一名 Unity 客户端工程师还要学什么，怎样才算真正成长？这本书一项一项地去学、去想、去验证，每一项都问三个问题：**责任**（此刻归谁）、**证据**（凭什么相信）、**限度**（做到哪里为止）。优化是贯穿全书的另一条线。

这是一本进行中的书：[学习路线](book/roadmap.md)列出了 89 个条目，已经写成的章节只是起点。已写成章节的观点都是**有依据、待检验的工程主张**：人工研究审核尚未发生，也没有执行过实验。详见[前言](book/00-preface.md)。

## 目录

**[前言](book/00-preface.md)**：这是一本什么书，怎样读

**[学习路线](book/roadmap.md)**：全书骨架。89 个可单独学习的条目分属八篇，每项标出核心问题、前置条目与本书覆盖情况，并附优化线索引。

**第一篇　出发与方法**

- [1.1　从实现代码到对结果负责](book/part1-method/1-1-from-code-to-responsibility.md)：工程能力不是代码产量，而是从问题到交付结果的完整责任。
- [1.2　为什么仍要把代码写好](book/part1-method/1-2-why-write-good-code.md)：让意图、约束与代价更容易被理解，让改变有依据，也让改进能够适时停止。
- [1.3　工程判断](book/part1-method/1-3-engineering-judgment.md)：作出可反驳的预测，找能改变决定的证据，事后更新一条带条件的规则。
- [1.4　三个问题：责任、证据与限度](book/part1-method/1-4-ownership-evidence-bound.md)：全书方法的来源，以及第一阶段研究的缺口。

**第二篇　运行时基础**：待学习（F1–F7，从“Unity 的一帧”开始）

**第三篇　系统建模**

- [3.1　迟到的结果：谁拒绝，谁释放](book/part3-system/3-1-the-late-result.md)：await 返回后，执行位置、提交资格、资源归属是三个问题；不再需要不等于不再负责。
- 待学习：状态与数据流 S1–S7、架构与模块化 A1–A8

**第四篇　性能与优化**：待学习（优化思维 OP1–OP7、性能与内存 P1–P13）

**第五篇　资源、网络与数据**：待学习（资源、构建与迭代 R1–R6，网络与同步 N1–N6，数据与持久化 D1–D3）

**第六篇　验证与可观测**：待学习（测试 T1–T5、可观测 O1–O5）

**第七篇　代码与工艺**

- [7.1　客户端代码质量](book/part7-craft/7-1-client-code-quality.md)：好代码让必要的行为、状态、依赖与约束可被可靠理解、验证和修改。
- 待学习：重构、技术债、读懂陌生系统、设计评审等（J3–J7）

**第八篇　AI 协作与团队**

- [8.1　AI 工作链](book/part8-ai-team/8-1-ai-quality-chain.md)：把约束、最小修改、可执行检查、定向审查与反馈接成可追溯的链。
- [8.2　AI-CQEP：一份最小工程协议](book/part8-ai-team/8-2-ai-cqep-protocol.md)：八条约束、六个阶段与按风险裁剪的验证。
- 待学习：AI 辅助调试、权限安全、对自身能力的影响，以及团队与交付 L1–L7

**附录**

- [附录A　工程实践规则](book/appendix-a-practice-rules.md)：57 条带编号与证据等级的规则。
- [附录B　术语与分级对照](book/appendix-b-glossary.md)
- [附录C　核心命题索引](book/appendix-c-propositions.md)：22 条承重命题的性质、状态、证据与推翻条件。
- [附录D　案例库](book/appendix-d-cases.md)：UniTask 与 NGO 的源码案例。
- [附录E　编码与审查清单](book/appendix-e-review-checklist.md)
- [附录F　AI-CQEP 速查卡](book/appendix-f-ai-cqep-quick-reference.md)
- [附录G　记录模板](book/appendix-g-record-templates.md)
- [附录H　研究方法](book/appendix-h-research-method.md)

## 研究档案与维护

[研究档案](archive/README.md)保存已写成章节的来源登记、证据笔记、审校记录、延伸手册和原始输入报告，并逐份写明退役理由；正文的引用仍然指向那里。结构上的决定记在[决策记录](docs/decisions.md)，改动和实际验证结果记在[变更记录](CHANGELOG.md)，参与方式见[贡献指南](CONTRIBUTING.md)。

本仓库是全部内容唯一的编辑源。在仓库根目录运行以下命令，可以检查文档格式、仓库内链接、目录完整性与两份保真导入件，无需安装依赖：

```bash
python -I -m unittest discover -s tests -p 'test_*.py' -v
python -I scripts/check_docs.py
```

这些检查不证明研究事实、外链内容、Unity 行为或页面渲染正确。远端结果见[GitHub Actions](https://github.com/YIMO691/ai-era-game-engineering/actions)。

## 许可

原创文档与图示采用 CC BY 4.0，原创独立代码、测试和工作流采用 MIT，署名 YIMO691。适用范围与第三方例外以[LICENSE](LICENSE)为准；缺失引用不意味着第三方材料获得重新授权。
