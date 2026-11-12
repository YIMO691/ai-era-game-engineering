# 游戏客户端代码质量与工程审美

本目录是课题 `20261105-client-code-quality` 的公开研究文档导出，讨论 Unity/C# 代码的表达、职责、生命周期、资源归属、审查与验证边界。

## 阅读入口

- [研究报告](research-report.md)：核心判断、方案取舍与证据边界。
- [实用指南](code-quality-guide.md)与[审查清单](code-review-checklist.md)：日常判断和通用教学模板。
- [代码对照案例](unity-csharp-examples.md)：4 个固定源码分析案例、7 个原创教学案例。
- [训练路线](training-route.md)：尚未执行的练习设计。
- [来源登记](sources.md)、[第三方材料声明](third-party-notices.md)、[原研究计划](plan.md)、[原审查记录](review.md)。
- [导出清单](export-manifest.json)：逐文件来源/导出 SHA-256、变换、排除项与源检查点核对。

## 原研究阶段与公开边界

原研究日期为 2026-11-05，阶段为 `awaiting_review`，人工审核 `pending`。正文中的 `publication_status: not-published` 等标记描述原研究快照，不代表当前公开授权状态。

用户已授权公开这些研究文档；2026-11-12 本次仅进行本地白名单导出，没有提交或推送。公开授权不等于人工学术审核、技术验证、实验通过或生产使用批准；原文待审、未运行和证据缺口全部保留。

四本经典均未完整阅读，相关公开原文候选的访问失败记录未补证。所有示例未编译/运行，没有 Unity、Profiler、设备性能或真实读者效果数据。本次未联网、未执行文档内命令或代码、未运行仓库代码与测试。

## 导出处理与权利

- 完整静态审阅后，仅导出本目录列出的研究文档。内部 Skill 适配/部署评估 `skill-proposal.md` 不导出；指向它的链接改为明确的排除说明。通用 Review、训练模板保留。
- 不导出 `topic.json`、原始会话、私有任务提示、配置、凭据或下载全文；计划中的私人任务书文件名改为通用说明。
- wikilinks 转为文件级相对链接；历史检查命令中的本机绝对路径改为通用位置。原审查记录不是本次导出执行记录。
- .NET Queue 短引保留 .NET Foundation and Contributors 署名和完整 MIT 许可。Unity Graphics、MonoGame、Unity C# Reference 仅保留分析、定位及各自权利限制，不改称 MIT。原创教学代码仍未验证。
- 跨目录引用仅指向 [Unity Task 生命周期来源](../unity-task-lifetime/sources.md)；本课题来源保持独立登记。

AI 辅助：Claude Code 工具环境中的模型于 2026-11-12 完成静态审阅、白名单转换和文件级检查；仅写入本目录，无新研究。人工决定限于公开授权，未记录对应版本的人工内容审核。回退可移除整个新增目录，不需修改私有源文件。

文件级校验不替代外链内容、完整 Markdown 渲染、事实、许可法律意见或 Unity 运行验证。仓库全局检查与测试按本次“不运行仓库代码”的范围限制未执行。
