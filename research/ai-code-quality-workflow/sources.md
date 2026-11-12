# 来源与证据登记

> 公开导出说明（2026-11-12）：以下为原稿研究或通用模板，不是实际配置；历史状态、检查与未运行项不因公开授权而升级。来源与排除边界见 [README](README.md) 和 [导出清单](export-manifest.json)。

访问日期均为2026-11-05。`read`只指注明范围已实际读取；`claim-checked`指具体主张与正文对照；`not-run`指未执行候选源码/插件/测试。元数据、文件正文、机制推导、效果实证分开。同仓库多文件不是独立效果交叉验证。取证附录只是本登记的定位展开，不另算来源。

## 继承材料 B1

机构/作者：本私有研究工作区此前AI辅助研究；标题：游戏客户端代码质量与工程审美；公开导出入口：[客户端代码质量](../client-code-quality/README.md)。本轮全文读取指定七份：research-report、code-quality-guide、unity-csharp-examples、code-review-checklist、training-route、sources、skill-proposal。另读review与topic恢复信息，核对10份Markdown实际SHA与旧topic检查点一致。报告SHA为`9927087f89b058058789acd56ca81ad58f3d8f4d671a653a3a124f3b186e6280`。

- 直接支持：已有指南/案例/清单/训练和“不预设新增Skill”的结论确实存在。
- 限制：旧题awaiting_review、human pending、not-published；11例未编译/运行、经典原文缺口未关闭；本题不升级这些状态，也不重复登记它引用的全部外部原始来源为本题新读来源。
- 权利：延续私有研究材料边界，不将公共仓库许可证扩展到Vault，不复制生产代码。

## 官方插件 O1

机构：Anthropic；标题：Claude Code Plugins Directory及四插件。仓库：<https://github.com/anthropics/claude-plugins-official>。固定SHA：`fa4eb54397ee2faccb6940512a19c017cb1337f3`，commit 2026-11-04T02:41:16Z，main，API archived=false。仓库pushed_at=2026-11-05T07:28:35Z不是每插件更新时间；四manifest版本分别code-simplifier 1.0.0，其余1.0.1。

`read_status=read; claim_status=claim-checked; experiment_status=not-run`。范围与行号展开于[官方取证](evidence-official.md)。

主要固定定位：

- [根README](https://github.com/anthropics/claude-plugins-official/blob/fa4eb54397ee2faccb6940512a19c017cb1337f3/README.md)：5行信任警告，30–43行目录结构；四条marketplace条目及各manifest也已解析。
- [独立simplifier定义](https://github.com/anthropics/claude-plugins-official/blob/fa4eb54397ee2faccb6940512a19c017cb1337f3/plugins/code-simplifier/agents/code-simplifier.md#L9-L52)：短摘录“Only refine code that has been recently modified”；支持范围/主动修改/JS偏置，不证明行为等价。
- [code-review命令](https://github.com/anthropics/claude-plugins-official/blob/fa4eb54397ee2faccb6940512a19c017cb1337f3/plugins/code-review/commands/code-review.md#L31-L72)：短摘录“Potential issues that depend on specific inputs or state”位于不要报告清单；支持过滤/验证/评论闸门。[README](https://github.com/anthropics/claude-plugins-official/blob/fa4eb54397ee2faccb6940512a19c017cb1337f3/plugins/code-review/README.md#L15-L25)所写blame与80阈值不同于实际command，作为反证保留。
- [feature-dev命令](https://github.com/anthropics/claude-plugins-official/blob/fa4eb54397ee2faccb6940512a19c017cb1337f3/plugins/feature-dev/commands/feature-dev.md#L35-L109)、[explorer](https://github.com/anthropics/claude-plugins-official/blob/fa4eb54397ee2faccb6940512a19c017cb1337f3/plugins/feature-dev/agents/code-explorer.md#L14-L51)、architect/reviewer已读：支持探索、亲读关键文件、获批实现与多agent成本，不证明有Unity验证。
- [toolkit命令](https://github.com/anthropics/claude-plugins-official/blob/fa4eb54397ee2faccb6940512a19c017cb1337f3/plugins/pr-review-toolkit/commands/review-pr.md#L13-L87)及六agent已读：[测试](https://github.com/anthropics/claude-plugins-official/blob/fa4eb54397ee2faccb6940512a19c017cb1337f3/plugins/pr-review-toolkit/agents/pr-test-analyzer.md#L19-L78)、[错误](https://github.com/anthropics/claude-plugins-official/blob/fa4eb54397ee2faccb6940512a19c017cb1337f3/plugins/pr-review-toolkit/agents/silent-failure-hunter.md#L121-L128)、[类型](https://github.com/anthropics/claude-plugins-official/blob/fa4eb54397ee2faccb6940512a19c017cb1337f3/plugins/pr-review-toolkit/agents/type-design-analyzer.md#L89-L118)。支持按风险选角色；Sentry/构造校验等要求须适配；评分不当测量。
- [hookify入口](https://github.com/anthropics/claude-plugins-official/blob/fa4eb54397ee2faccb6940512a19c017cb1337f3/plugins/hookify/hooks/pretooluse.py#L17-L62)、[规则引擎](https://github.com/anthropics/claude-plugins-official/blob/fa4eb54397ee2faccb6940512a19c017cb1337f3/plugins/hookify/core/rule_engine.py#L35-L94)、hooks.json及learning-output-style hooks.json/session-start.sh已读。支持事件脚本/上下文注入/fail-open的实现存在；未核验宿主完整事件契约和全部依赖，不作为可启用配置保证。

许可：四插件分别LICENSE全文已读，均Apache-2.0；只是链接/分析和少量短引，不复制实现。未来复制需检查版权/NOTICE、附许可并标明修改。根目录不能替所有external plugin统一授权；Hook两个示例未作完整单独许可审计。不是法律意见。

## 官方Skills O2

机构：Anthropic；标题：Skills、skill-creator。仓库：<https://github.com/anthropics/skills>。SHA：`ca45fc496a3436251f191354091d557da31c15b5`，commit 2026-10-28T19:20:38Z，main，archived=false，pushed_at=2026-10-28T19:20:39Z。根API license=null，不推为无权利或整仓统一开源。

`read_status=read; claim_status=claim-checked; experiment_status=not-run`。

- [README](https://github.com/anthropics/skills/blob/ca45fc496a3436251f191354091d557da31c15b5/README.md#L14-L24)：演示/教育免责声明和document skills不同许可。
- [skill-creator](https://github.com/anthropics/skills/blob/ca45fc496a3436251f191354091d557da31c15b5/skills/skill-creator/SKILL.md#L73-L109)：短摘录“Progressive Disclosure”；支持按需加载组织，不是自动遵守保证。169–329行的baseline/断言/反馈/盲比较已读。
- [run_eval.py](https://github.com/anthropics/skills/blob/ca45fc496a3436251f191354091d557da31c15b5/skills/skill-creator/scripts/run_eval.py#L35-L181)：实际写临时commands/启动claude、检测触发、清理；不是质量基准。
- [aggregate_benchmark.py](https://github.com/anthropics/skills/blob/ca45fc496a3436251f191354091d557da31c15b5/skills/skill-creator/scripts/aggregate_benchmark.py#L136-L153)：token缺失用output_chars；207–217行前两组delta、271行固定3次的元数据，不能原样当准确实验统计。
- grader.md、comparator.md全文已读；它们仍是模型判断。spec/agent-skills-spec.md全文只有迁移到agentskills.io的链接；没有据此声称读过完整标准。

许可：实际skill-creator/LICENSE.txt全文为Apache-2.0；不外推到所有Skills。未下载运行依赖或执行评测；Windows pipe/select兼容性、触发率和质量收益未实测。

## 本机CLI C1

来源：本机`claude --version`、`gh --version`与只读`--help`输出，访问日期2026-11-05；没有公开固定URL。Claude Code 2.1.310，gh 2.97.0。实际读取主CLI、plugin install、plugin marketplace、marketplace add、plugin list、agents的帮助；未执行安装/列插件清单/加源/新会话。

直接支持：主CLI `--plugin-dir`仅本会话加载；install与marketplace add均可显式scope且默认user；**install --marketplace未注册源时先写user settings**；`--setting-sources`可选user/project/local。短摘录：“If marketplace not added, it is added first, IN USER SETTINGS”。这是参数和副作用说明，不是配置写入/插件运行验证。当前没有精确已安装第三方插件清单；系统存在同名Skill不等于官方同名插件已装。

## 官方宿主文档访问失败 F1

三次WebFetch，均未读到正文：

- <https://code.claude.com/docs/en/plugins>
- <https://code.claude.com/docs/en/hooks>
- <https://code.claude.com/docs/en/memory>

错误均为：`Unable to verify if domain code.claude.com is safe to fetch. This may be due to network restrictions or enterprise security policies blocking claude.ai.`

`read_status=failed-before-body; claim_status=unverified`。不是HTTP403、网站不存在或文档不支持的证明。不换渠道/镜像绕过安全拒绝。影响：未能完整核验Rules路径匹配、CLAUDE自动发现/导入细节、Hooks schema/阻塞语义和插件加载优先级。采用C1帮助与O1实际示例作有限独立依据；仍不提供可直接启用的Hook配置或保证所有路径规则自动生效。

## Unity宿主文档发现与访问缺口 F2

主动检索Roslyn analyzer导入、Unity Test Framework命令行和Profiler目标构建。检索结果只作发现，不将搜索摘要算已读正文：

- [Unity 6000.0：Install an existing analyzer](https://docs.unity3d.com/cn/6000.0/Manual/install-existing-analyzer.html)：尝试WebFetch，安全验证失败，错误同F1但domain为docs.unity3d.com。`read_status=failed-before-body`。不换镜像/渠道绕过；没有据它保证某个Roslyn版本、标签或导入步骤。
- [2020.1命令行文档候选](https://docs.unity3d.com/es/2020.1/Manual/CommandLineArguments.html)、[2022.2 Profiling候选](https://docs.unity3d.com/2022.2/Documentation/Manual/profiler-profiling-applications.html)：`read_status=discovered-only`，本轮未取正文，版本不是用户实际Unity版本，不能确认当前测试CLI的组合/退出行为或构建设置。

影响：Unity专项采用方案按验证责任和审批步骤表达；不给“已核验可运行”的Unity Test Runner命令或analyzer安装处方。实际Unity/UTF版本、Roslyn兼容性、Editor与Player结果必须在后续授权沙盒验证。本轮没有访问真实业务工程来填这些空白。

## ECC E1

来源ID：`ER-20261105-ai-code-quality-workflow-ecc-01`（正文简写E1，指同一来源，不是另一份独立证据）。维护者：affaan-m。原入口：<https://github.com/affaan-m/everything-claude-code>；API canonical：<https://github.com/affaan-m/ECC>。SHA `b38be6a7f6350964d59328b52f0624e1d1d552d1`，commit 2026-10-30T03:06:32Z，main、archived=false、pushed_at=2026-11-02T04:56:08Z。release v2.2.3元数据不等于该SHA。

`read_status=read-scoped; claim_status=claim-checked-scoped; experiment_status=not-run`。取证者实际读12份文件的精确范围/固定链接、README部分段落、MIT许可、依赖及失败记录统一展开于[ECC取证](evidence-ecc.md)的S1–S12。

- 直接支持：development-workflow、tdd-guide、refactor-cleaner流程存在；csharp-reviewer偏.NET/Web；实际quality-gate无.cs分支。
- 短摘录/决定性定位：[quality-gate.js 69–152](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/scripts/hooks/quality-gate.js#L69-L152)的`return rawInput`；[dispatcher 114–140](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/scripts/hooks/posttooluse-dispatcher.js#L114-L140)将字符串结果归一化exitCode=0。strict只控制部分日志，不是合并门禁。主线程实际重读这些段、dispatcher 260–281、stop 185–249和csharp-reviewer全文确认此限定。
- [csharp-reviewer 41–70](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/agents/csharp-reviewer.md#L41-L70)：ConfigureAwait(false)、50行、record/DI等不是本题推荐的Unity硬约束。候选提示里的技术断言本身也要核验，不因“专业reviewer”而自动正确。
- 限制：没有读全套installer/解析器/其他hook；无“安全、离线、无外发、可回滚”的全仓保证。README声明可选跨提供方diff外发及user级配置写入，不启用。
- 许可：MIT，2026 Affaan Mustafa；将来复制实质部分保留版权/许可；不覆盖依赖或服务条款。维护信号仅API/README，不宣称CI通过。

## OpenHands H1 / H2

- H1 = `ER-20261105-openhands-01`，OpenHands contributors，Agent Canvas。旧入口 <https://github.com/All-Hands-AI/OpenHands> 的只读API最终返回canonical <https://github.com/OpenHands/OpenHands>，未单独测初始跳转状态链。main SHA `6d2d9df4af1337abf4ed967a7b396f46fed7559c`，commit 2026-11-05T03:15:24Z，非归档，pushed_at=2026-11-05T04:18:46Z。当前包1.35.0；Node>=24/npm11.12.1是该快照依赖信息。
- H2 = `ER-20261105-openhands-02`，OpenHands contributors，Software Agent SDK。<https://github.com/OpenHands/software-agent-sdk>，main SHA `28f4dfeeec4473060873185d301495d1c3743947`，commit 2026-11-05T05:46:25Z，非归档，pushed_at=2026-11-05T07:18:03Z。manifest 1.59.0、Python>=3.12；不能据版本相同证明Canvas部署包与两HEAD配对。

两者均`read_status=read-scoped; claim_status=claim-checked-scoped; experiment_status=not-run`。取证者读README/LICENSE/manifest/边界文档及9项关键实现、测试和workflow，精确范围与固定链接展开于[OpenHands取证](evidence-openhands.md) K1–K9及引用表；未展开第三仓extensions或完整状态存储实现。

- H1直接支持：[README 151–177](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/README.md#L151-L177)明确Canvas/SDK/automation边界；主线程实际重读。不是旧单仓runtime，不作为Claude Code插件安装。
- H2短摘录：[local_conversation.py 2051–2053](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L2051-L2053)：“Reaching the iteration limit or getting stuck does not raise”。[basic script 161–165](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/01_basic_action/agent_script.py#L161-L165)未显式检查终态就打印成功；这是静态成功判定风险，未运行复现。主线程重读对应源码。
- H2：[同文件456–485](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L456-L485)先保存再发布；[3166–3188](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L3166-L3188)警告工具非幂等。主线程实际重读；不能推出崩溃一致性、exactly-once或workspace回滚保证。
- H2实际review workflow把实现委托给extensions；没有取得独立reviewer内部实现。mock恢复测试和trace序列化测试不证明代码审查效果。自身CI的pass/skipped/live secret边界详附录，不报告本次CI执行通过。
- 权利/依赖：两LICENSE全文为MIT，分别2025/2026 OpenHands contributors；SDK涉及LiteLLM/Pydantic/httpx/FastMCP/ACP/Laminar等，Server另有Docker/FastAPI/SQLAlchemy。许可不覆盖所有依赖/模型/云服务。无安装、执行、真实恢复或Unity实验；只借鉴事件、终态、副作用核对原则。

## CodeRabbit R1

稳定ID：`ER-20261105-ai-code-quality-workflow-coderabbit-01`（简写R1）。CodeRabbit，Skills。<https://github.com/coderabbitai/skills>，main SHA `778c35a36e0afd2549c3fba86ec6e64afe649df3`，commit 2026-10-31T09:01:24Z，非归档，pushed_at=2026-11-05T06:02:56Z；release v1.1.1日期2026-04-22，README 1.2.0-unreleased不等于release。

`read_status=read-scoped; claim_status=claim-checked-scoped; experiment_status=not-run`。取证者读README 1–329、LICENSE、code-review SKILL、autofix SKILL及auth-recovery全文；精确链接/issue快照见[工具取证](evidence-tools.md) §1。

- [README 294–313](https://github.com/coderabbitai/skills/blob/778c35a36e0afd2549c3fba86ec6e64afe649df3/README.md#L294-L313)短摘录：“sends the code changes under review and the repository context”。主线程重读确认外部服务边界；MIT接入材料不等于开源/离线审查引擎。数据保留、训练使用、子处理者及合同未核验，不批准外发。
- 实际通过可信绝对路径的CLI运行`review --agent`；NDJSON区分heartbeat/review_skipped/completed，默认不包括原始untracked。severity不是修复授权；build/lint建议不是强制闸门。
- [autofix 261–268](https://github.com/coderabbitai/skills/blob/778c35a36e0afd2549c3fba86ec6e64afe649df3/skills/autofix/SKILL.md#L261-L268)整文件staging；主线程搜索核对对应定义。逐项批准不能自动隔离同文件既有未提交改动。issue #77与#61仅是公开讨论/静态缺口辅助证据，不是本次漏报或误提交复现；#61维护者说明已部署限制提示修复。
- 许可：MIT全文已读，仅本仓材料。CLI、认证、服务、额度、引擎效果及Unity理解均未实测；无登录、上传、收费调用。

## Unity专项分析器 U1

稳定ID：`ER-20261105-ai-code-quality-workflow-unity-analyzers-01`（U1）。Microsoft，Microsoft.Unity.Analyzers。<https://github.com/microsoft/Microsoft.Unity.Analyzers>，main SHA `a1ae8f287db28e0514a818f5cc2276125afbf5fe`，commit 2026-10-28T14:01:25Z，非归档；pushed_at=2026-10-30T13:44:58Z；release 1.28.0于2026-09-29。最新commit是测试依赖更新，不冒称诊断改进。

`read_status=read-scoped; claim_status=claim-checked-scoped; experiment_status=not-run`。取证者读README、doc/index、MIT LICENSE及SerializedFieldSuppressor、UnusedCoroutineReturnValue、csproj全文，见工具取证§2。

- [UNT0012实现](https://github.com/microsoft/Microsoft.Unity.Analyzers/blob/a1ae8f287db28e0514a818f5cc2276125afbf5fe/src/Microsoft.Unity.Analyzers/UnusedCoroutineReturnValue.cs#L40-L118)：直接expression statement + MonoBehaviour派生类型方法 + IEnumerator返回时诊断Info，fix包StartCoroutine；主线程全文重读。短摘录`WellKnownFixAllProviders.BatchFixer`不代表批量修复符合业务意图。
- suppressor仅在指定属性/类型条件下抑制若干字段诊断，不证明资产已赋值/全部UnityEvent入口安全；issue235属null语义取舍，不当本轮误报复现。
- csproj netstandard2.0、Roslyn Workspaces `[3.11.0.0]`；源码开发.NET10不等于Unity玩家runtime要求。先核对IDE随附分析器及重复加载，F2仍阻塞用户Unity宿主兼容保证；不默认NuGet安装。
- MIT全文已读；构建目标可能调用工具/Husky，未执行restore/build。没有本次Unity诊断/CodeFix运行记录。

## StyleCop S1

稳定ID：`ER-20261105-ai-code-quality-workflow-stylecop-01`（S1）。DotNetAnalyzers，StyleCopAnalyzers。<https://github.com/DotNetAnalyzers/StyleCopAnalyzers>，master SHA `986988bd01f81e2430e91c32214e2186be45be3c`，commit 2026-11-03T20:21:57Z，非归档，pushed_at=2026-11-04T16:40:17Z。所列最新release 1.3.171-beta是prerelease。

`read_status=read-scoped; claim_status=claim-checked-scoped; experiment_status=not-run`。取证者读README、MIT LICENSE、SA1402、analyzer csproj、Directory.Packages.props，精确范围/固定链接见工具取证§3。

- SA1402检查单文件顶层类型组织，Warning、部分partial/file-local例外；支持“团队风格检查”，不支持“设计更优”。
- netstandard1.1、旧兼容注释与中央Roslyn5.9.0不能直接确定发布包最低宿主要求，shipping pin导入链未读。issue4377是升级配置摩擦，不是架构质量实验。
- MIT全文已读；不隐去beta、不默认全部Error、不保证当前Unity可加载；没有执行或效果数据。

## Roslynator A1

稳定ID：`ER-20261105-ai-code-quality-workflow-roslynator-01`（A1）。.NET contributors，Roslynator。<https://github.com/dotnet/roslynator>，main SHA `b7ba8866006f39b4ffec30743b00cbf82070db5c`，commit 2026-10-31T14:39:29Z，非归档，pushed_at=2026-11-01T09:50:14Z；release v5.0.1于2026-10-04。

`read_status=read-scoped; claim_status=claim-checked-scoped; experiment_status=not-run`。取证者读README、LICENSE短声明、UnusedMemberAnalyzer、UnusedMemberCodeFixProvider及Directory.Build.props，见工具取证§4。

- [删除式CodeFix](https://github.com/dotnet/roslynator/blob/b7ba8866006f39b4ffec30743b00cbf82070db5c/src/Analyzers.CodeFixes/CSharp/CodeFixes/UnusedMemberCodeFixProvider.cs#L34-L59)的短摘录`RemoveMemberAsync`：主线程全文重读，修复实际删除节点，不能验证scene/prefab/反射可达性。
- analyzer有条件Unity消息保护，完整开关/Walker/发布包变体未核验，不能断言全部callback受保护或当前必误删。构建3.8/4.7/5.0变体不等于用户Unity兼容证明；IDE扩展、OmniSharp与Unity编译宿主不同。
- 许可声明Apache-2.0，未获取它外链全文，不重新分发实现。issue1596含报告者修正，不将其误读为当前所有Unity忽略EditorConfig。未执行analyzer/format/fix，不启用无人值守删除式Fix All。

## NetArchTest N1

稳定ID：`ER-20261105-ai-code-quality-workflow-netarchtest-01`（N1）。Ben Morris / contributors，NetArchTest。<https://github.com/BenMorris/NetArchTest>，master SHA `a761f63b694a6facd4be01fbc8fe2ae26579572e`，commit 2023-07-03T11:01:36Z，非归档但pushed_at=2024-07-29T18:02:58Z、release v1.3.2于2021-05-23；不称近期活跃。

`read_status=read-scoped; claim_status=claim-checked-scoped; experiment_status=not-run`。取证者读README、MIT LICENSE、DependencySearch、TypeParser与csproj，见工具取证§5。

- 以选定程序集中的source类型检查显式target namespace依赖方向，不会自动推导合理架构。选择空集/未装载程序集可能假通过，须非空断言/marker覆盖/故意违约负例；issue150原例也有namespace选错，不当全部解析错误证据。
- [TypeParser](https://github.com/BenMorris/NetArchTest/blob/a761f63b694a6facd4be01fbc8fe2ae26579572e/src/NetArchTest.Rules/Dependencies/TypeParser.cs#L9-L32)短摘录`BindingFlags.NonPublic`；主线程全文重读，耦合Cecil非公开API。netstandard2.0/Cecil0.11.5不保证当前Unity宿主适配。
- MIT全文已读；未读全部IL遍历，不保证传递依赖全覆盖；不看一般scene/prefab/Addressables引用。未运行架构测试，维护/升级成本使其仅为有条件候选。

## 主张晋升与停止表

| 主张 | 证据 | 允许措辞 | 禁止升级 | 后续检查 / 决策 |
|---|---|---|---|---|
| 模型插件可组织探索/审查 | O1/O2/E1 | 定义存在、有限借鉴 | 装后必然提高质量 | 同任务对照；保留为候选 |
| 静态检查可重复执行指定规则 | U1/S1/A1/N1 | 已读实现的限定检查 | 无误报/覆盖全部Unity | 宿主与正反例；有条件采用 |
| 最小组合更适合当前约束 | B1+O1+C1+F1/F2及各候选边界 | 本研究的低维护设计判断 | 已实证最优/快多少 | 用户授权后小样本试点 |
| AI独立角色审阅有价值 | O1/R1仅提供流程 | 可发现待核验线索 | 独立效果证明/校准置信度 | 运行/人工核验；限制措辞 |
| 服务/恢复/Hook有边界 | R1/H2/E1/O1 | 已定位限定风险 | 已发生事故/全仓不安全 | 定点实验或不启用 |
| 性能、缺陷率、收益 | 本轮无实验 | 未知 | 改善百分比、通过率 | 目标设备/人工对照；暂不作结论 |

取证范围至此足以比较机制与采用条件。停止扩展仓库，不因未读完整生态而继续无界下载；完整宿主文档、发布包配对和真实Unity实验缺口保留在正文与状态中。
