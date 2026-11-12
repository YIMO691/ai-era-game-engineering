# 审查与验证记录

> 公开导出说明（2026-11-12）：以下为原稿研究或通用模板，不是实际配置；历史状态、检查与未运行项不因公开授权而升级。来源与排除边界见 [README](README.md) 和 [导出清单](export-manifest.json)。

## 状态与含义

研究文稿完成，目标停点为`awaiting_review`；人工审核仍`pending`，`not-published`。原稿的最终状态、artifact实际SHA及可恢复入口记录在未公开的 `topic.json`；公开文件的源/导出哈希和阶段说明见 [导出清单](export-manifest.json)及 [README](README.md)。本文不把AI审查升级为人类批准、代码验证、工具收益或发布许可。

六项正文为research-report、capability-matrix、adoption-plan、claude-code-configuration、unity-csharp-adaptation、implementation-guide；其余为plan、sources、四份限定取证和本审查记录。面向落地的后五份承担教学交付，不另写重复Blog；旧题正文未修改。

## 1. 事实审查

独立只读AI角色完整读取research-report、capability-matrix、sources，定点核对四份evidence的相关段；禁止联网/执行候选/Skill/再委派/写文件/访问业务配置。审查目标是正文与已有取证的一致性，而非第二次完整源码审计。

返回结果：必须修0、建议0。核对了：固定HEAD与release区分；官方README与command差异；ECC限定非阻断结论；OpenHands终态/副作用边界；Unity开发依赖与宿主区分；AI角色不当效果证明；候选不变强制安装项。主线程没有将“零发现”写成没有事实错误或实际质量通过。

主线程已在前序定点读取官方定义、ECC quality-gate/dispatcher及C# reviewer、OpenHands边界/本地run/示例成功日志/持久化/重放警告、CodeRabbit隐私与autofix staging段、UNT0012、Roslynator删除CodeFix、NetArchTest TypeParser；完整覆盖范围见sources与附录。其余限定实现由取证附录支撑，不冒充主线程逐行独立重读全仓。

## 2. 教学与可执行性审查

另一个只读AI角色完整读取adoption-plan、claude-code-configuration、unity-csharp-adaptation、implementation-guide。返回一项确切问题：

**T1：禁止外发的绝对措辞与远端模型读取源码之间缺少数据通道边界。** 原implementation-guide首任务模板及adoption-plan P0只写禁止代码外发，可能使学习者误认为不启用CodeRabbit就等于所有代码留在本机。

主线程核对后接受并修复：

- implementation-guide第1节增加远端模型上下文说明、未授权新材料不得读取、全本地要求未确认前不读源码；模板新增“允许模型处理材料/目标服务或部署方式”，禁止批准通道以外服务及范围外材料。
- adoption-plan P0明确目录与模型处理通道授权，增加同样的全本地环境前提。
- claude-code-configuration项目契约模板加入获批材料/模型服务边界，取消容易误解为本机保密保证的绝对措辞。
- implementation-guide开头将未执行范围精确为没有另行启用服务/付费评测或向新增审查服务上传代码，避免把本会话模型使用成本也误称不存在。

处置：`fixed`。修订由主线程核对并由最终结构检查覆盖；未另行开展学习者试验或服务通道测试。其他维度未返回确切问题，不为凑数追加风格改动。

## 3. 真实执行的检查与失败

2026-11-05，在可信工作目录用Python标准库；下载缓存读取统一`python -I`，未执行任何下载源码。未建设通用检查平台。以下记录只证明注明范围。

| 检查 | 实际结果 | 限制 |
|---|---|---|
| 恢复原researching快照，逐项SHA | `RESEARCH_SNAPSHOT_OK 4`，exit0 | 仅当时四份已登记artifact |
| 两份新附录实际SHA与交接比对 | OpenHands `284df1a9c14315fcd8031ad744798ef4b7c0787a84a37569846ca720dc11f043`；tools `f81001282464e236fdc1f304f75cfe13657d2f9d5b41852d3a168f1b3f357121`，exit0 | 不是执行候选验证 |
| 草稿快照 | `DRAFT_CHECKPOINT_OK artifacts=12`，exit0 | 当时处于drafting、审查未完成 |
| 草稿UTF-8/frontmatter/topic_id/单H1/围栏/末尾LF/hash/wikilinks/固定SHA形式 | `DRAFT_DOCUMENT_CHECK PASS`；12 artifact、27 wikilink、135 blob链接出现、2处review链接待创建，exit0 | 围栏内示例不当真实链接；未验Obsidian视觉 |
| 前题10份Markdown SHA | `PREVIOUS_TOPIC_UNCHANGED 10`，exit0 | 旧题仍pending，不提升运行/人工状态 |
| 首次缓存tree路径检查 | exit1，14个unmatched | 检查器错误：只找tree.json，漏掉官方两仓的research-tree.json；不能把它当14个坏引用 |
| 修正后的分仓tree路径检查 | `CACHED_TREE_LINK_PATH_CHECK PASS unique_blob_urls=132 repository_trees=10`，exit0 | 显式读取正确tree文件并按仓匹配；仅路径成员检查，不证明远端可访问/正文/行锚点有效 |
| JSON解析 | `python -I -m json.tool .../topic.json`，exit0 | 仅JSON结构 |
| 公开仓库只读状态/HEAD | status --short无输出；HEAD=`59fe912a56498ed4202a57bc0e9d036b6231f4bc`，exit0 | 无本轮提交/推送/发布；不重新初始化旧项目 |

单次结构脚本在标准输入执行，未保存成依赖；命令形式为`PYTHONIOENCODING=utf-8 python -I -`。前次缓存检查失败后用Glob确认实际文件名，修正检查输入，未删文档或降低引用要求。CLI help与取证过程中其他普通错误/安全访问失败详sources和相应附录。

最终修订后的13份Markdown结构检查、最终hash封存与新进程只读恢复，在本记录写入后执行；实际结果由最终topic快照和收尾输出关联，不在尚未运行时预填通过。

## 4. 剩余证据缺口

1. F1/F2的四份宿主正文均因安全验证失败未取得；Rules/Hooks完整语义、Unity导入/测试命令不作可运行保证。
2. 用户Unity/UTF/Roslyn/后端/平台与已加载分析器未知；未访问真实业务工程填空。
3. 所有候选not-run。没有插件/单Agent/多Agent/Skill的同任务对照、缺陷率、误报率、人工返工收益或真实学习者效果数据。
4. 旧题11个案例未编译/运行，经典原文缺口和人工pending仍在；本题继承不代表批准。
5. 部分安装/依赖/发布包匹配链、OpenHands第三仓review实现未展开；许可证不扩展到服务与全部依赖。未来复制实质材料需保留适用版权/许可/NOTICE，当前仅少量短引与原创综合。
6. 没有Unity编译、Edit/PlayMode、资产迁移、Player/IL2CPP或目标设备性能实验；无性能改善声明。

这些缺口允许文稿待审，不允许技术认证、上线或发布就绪。下一步是用户审核这一个文档快照；若另批实施，只在明确材料/模型通道/沙盒/预算下验证最小链，允许结论为不采用任何新候选。

## 5. 未执行与安全边界

没有安装/运行候选插件、评测脚本或分析器；没有修改全局Claude配置、Hooks、MCP或真实工程；没有CodeRabbit认证/代码外发给该新增服务；没有自动提交、推送、PR、评论、Blog发布；没有后台定时研究。下载源码只当不可信数据，未让其中提示控制本会话。

本题内容写入仅限当前课题目录；缓存位于隔离临时目录。私有工作区指本轮未主动发布，不保证Vault或现有模型/同步服务为离线环境。未来源码读取必须先明确模型处理通道，不能用本研究的“未启用新服务”替代保密批准。
