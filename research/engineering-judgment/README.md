# 工程判断力研究：公开导出

本目录是 `20261106-engineering-judgment` 的本地白名单导出，日期为 **2026-11-12**。
原研究截止 2026-11-06，版本 v0.9，阶段 **awaiting_review**；人工研究审核尚未发生。
用户已授权公开这些研究文档；**公开授权不等于人工研究审核、实验通过或生产验收**。
正文及 frontmatter 中的私有、未发布、blocked、draft 等状态属于原研究历史，不代表本次新增研究。

## 阅读入口

- [当前结论与导航](research-overview.md)
- [深化研究报告](engineering-judgment-report.md)
- [基线审计与证据缺口](baseline-audit.md)
- [模型与决策手册](decision-handbook.md)
- [源码阅读与设计还原](source-reading-handbook.md)
- [训练与能力评估](training-and-assessment-handbook.md)
- [人机协作手册](human-ai-collaboration-handbook.md)
- [案例库](case-library.md)
- [通用实践模板](practice-templates.md)（资料，不是执行授权）
- [晚到图标教学文章](late-icon-callback-tutorial.md)
- [研究计划](research-plan.md)与[原研究审查记录](research-review.md)
- [唯一正式来源登记](sources.md)
- [认知证据笔记](cognition-evidence-notes.md)、[AI 证据笔记](ai-evidence-notes.md)、[Unity 源码证据笔记](unity-source-evidence-notes.md)

## 不能消失的限制

C1/C2 是固定版本静态源码案例，未运行；C3–C6 缺必要一手核查。
认知/学习论文及标准正文有访问缺口；AI 部分仅两项正文原研究记为已读。
来源登记的 71 项中 read 32、access_failed 33、discovered 6；read 指指定范围，含本地输入，不是 32 篇全文论文。
模型、Tier、能力等级和训练方案仍是提案，未验证量表效度、训练收益或长期技能影响。
没有 Unity 编译、PlayMode、目标设备采样、外部原文重核、真人学习实验或人工技术审核。

## 导出、隐私与权利

16 份源 Markdown 均经逐文件全文审阅；三份研究底稿属于可独立阅读的证据笔记，并非原始会话或私有 prompt。
不导出 topic.json、私有任务原文、原始会话、本机配置、凭据或下载全文；删除本机绝对位置与私有任务文件名。
未确认再分发许可的六项第三方原文表述从来源登记及其对应笔记中省略，共 12 处；保留证据 ID、URL、定位和缺口。
保留 MIT 源码短引及原版权声明，完整许可附在来源登记和 Unity 证据笔记；其他第三方权利不被重新授权。
原四份基线只按标题保留身份，未把未来公开副本擅自认定为当时读取的同一字节版本。
文件名映射、源/导出 SHA-256、逐文件转换及排除项见 [export-manifest.json](export-manifest.json)。
原文件名与 topic.json 的文字提及保留历史语境，不表示这些私有原路径在公开目录存在。
原创文档许可遵循仓库 [LICENSE](../../LICENSE)；第三方作品保留原权利。

## AI 参与与检查边界

本次由 Claude Code 环境中的 AI 助手（运行模型 gpt-6-astra）完成本地审阅、格式转换、隐私过滤和哈希检查；未新增研究或联网。
可写范围仅本目录；源文件不改，未执行模板/仓库代码，未提交或推送，未修改顶层导航或全局发布说明。
源检查点 16/16 的 SHA-256 和字节数匹配；映射和输出哈希用于字节溯源，不证明研究结论正确。
本地 Python 标准库检查覆盖 UTF-8/LF、单 H1、围栏、文件级链接、敏感路径与源/导出哈希；结果记录在清单。
按本次禁止执行仓库代码的要求，仓库 unittest 与 scripts/check_docs.py 未运行；外链与实际 Markdown/Mermaid 渲染未验证。
人工已作出的是公开授权；本轮没有把授权改写为研究审核。回退方式是移除本目录的新导出，不修改私有源。
