# AI 时代的游戏客户端工程：责任、证据与限度

当 AI 让“写出代码”越来越便宜，工程师的能力还剩下什么？本书以 Unity / C# 商业游戏客户端为场景，回答说：理解系统，作出判断，用证据验证结果，并对交付承担责任。书中的判断都是**有依据、待检验的工程主张**：人工研究审核尚未发生，也没有执行过实验。证据状态在[前言](book/00-preface.md)中完整说明。

## 目录

**[前言](book/00-preface.md)**：这本书想回答什么、怎样写成、怎样读

**第一部分　立场**

- [第1章　从实现代码到对结果负责](book/01-from-code-to-responsibility.md)：工程能力不是代码产量，而是从问题到交付结果的完整责任。
- [第2章　为什么仍要把代码写好](book/02-why-write-good-code.md)：让意图、约束与代价更容易被理解，让改变有依据，也让改进能够适时停止。

**第二部分　系统与责任**

- [第3章　迟到的结果：谁拒绝，谁释放](book/03-the-late-result.md)：await 返回后，执行位置、提交资格、资源归属是三个问题；不再需要不等于不再负责。
- [第4章　客户端代码质量](book/04-client-code-quality.md)：好代码让必要的行为、状态、依赖与约束可被可靠理解、验证和修改。

**第三部分　判断**

- [第5章　工程判断](book/05-engineering-judgment.md)：作出可反驳的预测，找能改变决定的证据，事后更新一条带条件的规则。

**第四部分　AI 时代的工作方式**

- [第6章　AI 工作链](book/06-ai-quality-chain.md)：把约束、最小修改、可执行检查、定向审查与反馈接成可追溯的链。
- [第7章　AI-CQEP：一份最小工程协议](book/07-ai-cqep-protocol.md)：八条约束、六个阶段与按风险裁剪的验证。

**结语**

- [第8章　结语：责任、证据与限度](book/08-ownership-evidence-bound.md)：五项命题、三轴框架、研究缺口与下一步。

**附录**

- [附录A　工程实践规则](book/appendix-a-practice-rules.md)：57 条带编号与证据等级的规则。
- [附录B　术语与分级对照](book/appendix-b-glossary.md)
- [附录C　核心命题索引](book/appendix-c-propositions.md)：22 条承重命题的性质、状态、证据与推翻条件。
- [附录D　案例库](book/appendix-d-cases.md)：UniTask 与 NGO 的源码案例。
- [附录E　编码与审查清单](book/appendix-e-review-checklist.md)
- [附录F　AI-CQEP 速查卡](book/appendix-f-ai-cqep-quick-reference.md)
- [附录G　记录模板](book/appendix-g-record-templates.md)
- [附录H　研究方法](book/appendix-h-research-method.md)
- [附录I　学习版图与路线](book/appendix-i-learning-roadmap.md)：78 个可单独学习的条目，分六个阶段，标出本书已覆盖、点到与空白之处。

## 阅读路线

- **作为学习者，想知道还要学什么**：[附录I](book/appendix-i-learning-roadmap.md)，从推荐的第一项开始。
- **只想抓住主线**：第1、2、3、8章。
- **一线工程师**：第3、4章，附录A、E。
- **在团队中引入 AI 协作**：第6、7章，附录F、A。
- **带新人或训练判断**：第5章，附录D、G。
- **研究者与审阅者**：第8章，附录C、H，以及[研究档案](archive/README.md)。

## 研究档案与维护

各章的来源登记、证据笔记、审校记录、研究计划、延伸手册和原始输入报告，都保存在[研究档案](archive/README.md)中，并逐份写明退役理由，正文的引用仍然指向那里。改变结构或编辑约定的决定记在[决策记录](docs/decisions.md)，已发生的改动和实际验证结果记在[变更记录](CHANGELOG.md)，参与方式见[贡献指南](CONTRIBUTING.md)。

本仓库是全部内容唯一的编辑源。在仓库根目录运行以下命令检查文档格式、仓库内链接、目录完整性与两份保真导入件，无需安装依赖：

```bash
python -I -m unittest discover -s tests -p 'test_*.py' -v
python -I scripts/check_docs.py
```

检查不证明研究事实、外链内容、Unity 行为或页面渲染正确。远端结果见[GitHub Actions](https://github.com/YIMO691/ai-era-game-engineering/actions)。

## 许可

原创文档与图示采用 CC BY 4.0，原创独立代码、测试和工作流采用 MIT，署名 YIMO691。适用范围与第三方例外以[LICENSE](LICENSE)为准；缺失引用不意味着第三方材料获得重新授权。
