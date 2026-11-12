# AI 代码质量工程闭环

本目录是既有研究的白名单公开导出，讨论如何把上下文理解、最小实现、确定性验证、定向审查与反馈连接起来，而不是推荐安装全套工具。

## 阅读顺序

1. [研究报告](research-report.md)与[能力矩阵](capability-matrix.md)：结论、候选职责及取舍。
2. [采用方案](adoption-plan.md)、[配置设计](claude-code-configuration.md)、[实施指南](implementation-guide.md)：尚未执行的实践设计与通用模板，不是实际配置或操作授权。
3. [Unity/C# 适配](unity-csharp-adaptation.md)：环境、生命周期、资源与验证责任。
4. [来源登记](sources.md)与取证附录：[官方生态](evidence-official.md)、[ECC](evidence-ecc.md)、[OpenHands](evidence-openhands.md)、[质量工具](evidence-tools.md)。
5. [原稿审查记录](review.md)：历史检查及未解决缺口。

前置研究为[客户端代码质量](../client-code-quality/README.md)，后续综合为 [AI-CQEP](../ai-cqep/README.md)。

## 原稿阶段与证据边界

- 来源课题：`20261105-ai-code-quality-workflow`；原稿日期：2026-11-05。
- 原始元数据阶段为 `awaiting_review`，人工审核 `pending`，原始发布状态 `not-published`。
- 2026-11-12 的公开导出授权不等于研究人工审核、工具运行验证、实验通过或部署批准。
- 源检查点 13/13 个 SHA-256 匹配；其中内部计划不导出。字节一致性不证明内容正确。
- 官方宿主及 Unity 导入文档的访问缺口保留；候选工具、Unity/Player/设备与效果对照均未运行。
- 正文“本轮”“未发布”、CLI 版本、检查成功等均为原稿历史记录，不是本次重新执行或当前兼容承诺。

## 导出与隐私

保留 12 份研究正文/证据记录；不导出 `topic.json`、内部 `plan.md`、实际配置、原始会话、下载源码或全文缓存。通用提示和契约模板是研究产物，不是私有会话或已生效的设置。

移除原稿 frontmatter；wikilinks 和参考式链接改为标准链接；本机工作目录与缓存绝对路径替换为通用占位符，外部来源 URL（含原定位片段）、许可证和第三方署名保留。具体转换与排除项见 [导出清单](export-manifest.json)。原始 `topic.json` 不公开，公开文件应使用清单中的源/导出 SHA-256，不能拿原稿历史哈希校验转换后的文件。

## AI 辅助及本次验证范围

2026-11-12 由 AI 辅助完成全文静态审阅、白名单导出、隐私处理、链接转换和标准库字节/结构检查；只写本目录。未重新研究、联网、运行仓库代码或 Unity，未提交/推送。源文档未修改，人工研究审核未由导出代替。撤回仅涉及本次新建导出文件，须先核对后续用户改动。
