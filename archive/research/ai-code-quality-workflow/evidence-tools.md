# 代码质量工具只读源码证据附录

> 公开导出说明（2026-11-12）：以下为原稿研究或通用模板，不是实际配置；历史状态、检查与未运行项不因公开授权而升级。来源与排除边界见 [README](README.md) 和 [导出清单](export-manifest.json)。

## 取证方法与结论边界

- 取证日：2026-11-05；收尾核对时间为 `2026-11-05T08:36:51Z`。只使用 `gh` 的 GitHub **只读 API**，读取 repository、默认分支 commit、递归 tree、固定 `ref=SHA` 的文件、releases、公开 issue 及 comments。没有安装工具、执行下载源码、运行审查/分析器/测试、构建项目、调用 Skill、Workflow 或再委派。
- 每个仓库使用独立新建空目录缓存，再下载选定文件；不是 clone，也没有执行仓库脚本。所有读取下载数据的 Python 都以 `python -I` 从可信工作目录 `<trusted-working-directory>` 启动；未从缓存目录启动解释器或构建工具。
- 缓存根目录：`<isolated-download-cache>/`。各仓库包含 `repo.json`、`commit.json`、`tree.json`、`releases.json`、`files/` 及相应 `issue-N.json`、`issue-N-comments.json`；`issues-search.json` 保留发现路径。没有缓存认证令牌。
- 下文源码链接全部固定到完整 SHA，并标注行号；“实际阅读”包括完整打开的文件，不把仅在 tree 中发现的测试当成已读证据。五棵 tree 均返回 `truncated: false`。Issue 是可变讨论，不冒充固定源码：保留取证日、编号和本地 JSON 快照，区分报告者陈述、维护者解释与本次源码判断。
- SHA 来自取证时默认分支 HEAD，不等同于最新 release 的源码。维护判断使用提交日期、提交性质、release 和维护者回应；不使用 Star。`pushed_at` 不一定代表默认分支发生源码修改。
- 除 CodeRabbit 外保留四个候选，但用途不同：Unity 专用语义规则、StyleCop 团队风格、Roslynator 诊断/重构、NetArchTest 自定义架构约束。**确定性只意味着给定输入与配置下有明确程序规则，不意味着无误报、覆盖完整或自动修复保语义。**
- 五项共同记录状态：`read_status: read`、`experiment_status: not-run`；文件直接陈述/实现为 direct，本文明确标成源码推导的适用边界为 inference，未读依赖链/当前 Unity 支持为 unverified。各仓库及其 issue 属于同一来源簇，不将同仓多个文件计作独立交叉验证。遵守本任务唯一产物授权，不改 `sources.md`、正文或 `topic.json`，也不推进研究阶段；主线程若采用本附录，需要先在来源登记中赋稳定证据 ID，再绑定正文主张。

## 1. coderabbitai/skills：开源接入指令，不是开源审查引擎

### 版本、许可、维护与阅读范围

- Canonical：`coderabbitai/skills`，默认分支 `main`；SHA `778c35a36e0afd2549c3fba86ec6e64afe649df3`；commit 时间 `2026-10-31T09:01:24Z`。[固定提交](https://github.com/coderabbitai/skills/commit/778c35a36e0afd2549c3fba86ec6e64afe649df3) 的主题是共享 CLI 发现与沙箱恢复说明。仓库未归档；API `pushed_at=2026-11-05T06:02:56Z`；release 快照为 `v1.1.1`，发布于 `2026-04-22T07:33:44Z`。README 自标 `1.2.0-unreleased`，不能把 main 的规则当作该 release 已经发布的行为。
- [LICENSE L1–21](https://github.com/coderabbitai/skills/blob/778c35a36e0afd2549c3fba86ec6e64afe649df3/LICENSE#L1-L21)：MIT，包含版权/许可保留及免责条件。这里只能确定本仓库材料的许可，不能据此认定外部 CLI、云端引擎或服务数据政策也是 MIT。
- 实际阅读：`README.md` L1–329；`LICENSE` L1–21；三个关键文件：`skills/code-review/SKILL.md` L1–147、`skills/autofix/SKILL.md` L1–336、`skills/code-review/references/auth-recovery.md` L1–103。
- 缓存：`<isolated-download-cache>/`。

### 实际调用、等级与修复约束

- 真正启动审查的是已安装且验证可信的 CLI 绝对路径：`"/absolute/path/to/coderabbit" review --agent`，并非 Skill 文件里实现了审查算法。[code-review L29–81](https://github.com/coderabbitai/skills/blob/778c35a36e0afd2549c3fba86ec6e64afe649df3/skills/code-review/SKILL.md#L29-L81) 要求先认证，可附 `--committed`、`--uncommitted`、`--base`、`--base-commit`、`--dir`；默认包括 committed、staged 与 tracked unstaged，**不包括原始 untracked**，staged 新文件则包括。`--include-untracked` 是显式扩大外发范围；`--light` 改变上下文/审查策略，不是输出格式或严重程度阈值。
- [L83–100](https://github.com/coderabbitai/skills/blob/778c35a36e0afd2549c3fba86ec6e64afe649df3/skills/code-review/SKILL.md#L83-L100)：`--agent` 输出按 NDJSON 处理；保留 `critical/major/minor/trivial/info/none`，不是将全部发现归为 Warning。heartbeat 只表示仍活动；`review_skipped` 加零发现不等于干净。实现加审查的迭代是列任务、在授权范围内优先处理 critical/major、再审查、报告剩余问题并停止；**没有一个写死的最大迭代次数**，仅要求避免无界循环。
- PR `autofix` 是另一条流程，不应与上述自主迭代混为一谈。[autofix L171–195](https://github.com/coderabbitai/skills/blob/778c35a36e0afd2549c3fba86ec6e64afe649df3/skills/autofix/SKILL.md#L171-L195) 只选未解决且未过期、根评论作者为指定机器人账号的线程；严重程度原样保留，无法识别则显示 Unknown。`Action=Fix` 要靠本地独立确认，不由高严重程度自动推导。
- [L208–259](https://github.com/coderabbitai/skills/blob/778c35a36e0afd2549c3fba86ec6e64afe649df3/skills/autofix/SKILL.md#L208-L259) 要逐项读代码、解释真假、展示最小 diff、逐次批准；不批量照抄 reviewer prompt。误报处理是上下文复核和暂缓，不是已有测量证明其误报率低。[L261–284](https://github.com/coderabbitai/skills/blob/778c35a36e0afd2549c3fba86ec6e64afe649df3/skills/autofix/SKILL.md#L261-L284) 规定合并提交，build/lint 只是推荐且需用户同意，push 另问；不能将这段流程宣传成强制测试通过的质量闸门。

### 服务、认证、隐私与 Unity 边界

- [README L294–313](https://github.com/coderabbitai/skills/blob/778c35a36e0afd2549c3fba86ec6e64afe649df3/README.md#L294-L313) 明确：审查经本地 CodeRabbit CLI 将代码变更及所需仓库上下文发送至 CodeRabbit 服务；autofix 经 `gh` 与 GitHub 交换 PR 数据；两者分别管理自己的凭据。README 对 Claude plugin 的“无内置 executable/hooks/MCP”描述不能扩展为仓库所有分发变体都无代码或无 hook。
- [auth-recovery L5–53、L73–103](https://github.com/coderabbitai/skills/blob/778c35a36e0afd2549c3fba86ec6e64afe649df3/skills/code-review/references/auth-recovery.md#L5-L53) 要拒绝仓库/临时目录中的候选 executable、只信已确认的官方安装来源，成功获得 `authenticated: true` 才继续，不代读凭据或自动登录。沙箱权限被拒就停止；恢复最多只适用于远程分析开始前的特定认证失败，不适用于网络、限流、计费或已经开始的 review。**这些是被研究的仓库指令，本次没有照其安装、登录或提权。**
- [code-review L138–143](https://github.com/coderabbitai/skills/blob/778c35a36e0afd2549c3fba86ec6e64afe649df3/skills/code-review/SKILL.md#L138-L143) 要求外发前检查所选范围的敏感内容，输出当不可信数据，不直接执行其命令。实际保留期、训练使用、次级处理者和服务合同没有在本次 GitHub 取证中核实，不能替用户作隐私合规批准。
- Unity 能得到变更层面的 AI 提示，但本仓库没有证明审查引擎理解当前 Unity 版本、生命周期、序列化资产、IL2CPP 或平台条件编译。它不能替代本地规则或 Unity 验证；调用还受外部服务可用性、认证、版本与可能的使用额度约束，未做可用性或费用测试。

### 真实失败与指令缺口

- [issue #61](https://github.com/coderabbitai/skills/issues/61) 报告 CLI `0.8.2` 的 `review_completed/findings:0` 与已有发现、上下文不足之间的歧义。维护者在 [2026-10-07 回复](https://github.com/coderabbitai/skills/issues/61#issuecomment-6037290609) 说 fresh run 确已执行，但受不可用仓库上下文限制；已部署报告此限制的修复，后续 CLI 会明确复用；历史 findings 也可能来自旧运行。因此不是“仍有三项漏洞却一定漏报”的本次复现，也不能把 issue 已关闭理解为所有 CLI/Skill 组合均已验证。
- [issue #77](https://github.com/coderabbitai/skills/issues/77) 在 `2026-10-31` 报告 autofix 的工作区隔离、PR 唯一性、分页错误、push 与总结等六处缺口，取证时仍 open。对照固定源码，[autofix L52–64](https://github.com/coderabbitai/skills/blob/778c35a36e0afd2549c3fba86ec6e64afe649df3/skills/autofix/SKILL.md#L52-L64) 没有明确写出拒绝先提交时必须退出，而 [L261–268](https://github.com/coderabbitai/skills/blob/778c35a36e0afd2549c3fba86ec6e64afe649df3/skills/autofix/SKILL.md#L261-L268) 又按整文件 `git add`。这确实不能保证提交只含逐项批准的修改；是可核对的指令缺口，非本次执行事故。公开报告也提示完成状态检查仍需更严格，不能以“零发现”直接结案。
- 本次未执行 CodeRabbit，没有本地成功率、误报率、召回率或修复效果数据。

## 2. microsoft/Microsoft.Unity.Analyzers：Unity 语义优先的确定性底层

### 版本、许可、维护与阅读范围

- Canonical：`microsoft/Microsoft.Unity.Analyzers`，`main`；SHA `a1ae8f287db28e0514a818f5cc2276125afbf5fe`；commit `2026-10-28T14:01:25Z`。[固定提交](https://github.com/microsoft/Microsoft.Unity.Analyzers/commit/a1ae8f287db28e0514a818f5cc2276125afbf5fe) 是测试重试依赖更新，不能单凭它说近期改进了诊断能力。未归档；`pushed_at=2026-10-30T13:44:58Z`；release 有 `1.28.0`（`2026-09-29T19:21:18Z`）、`1.27.0`、`1.26.0`，持续发布是比最近依赖提交更直接的维护信号。
- [LICENSE L1–21](https://github.com/microsoft/Microsoft.Unity.Analyzers/blob/a1ae8f287db28e0514a818f5cc2276125afbf5fe/LICENSE#L1-L21)：MIT。实际阅读 `README.md` L1–94、`doc/index.md` L1–78、LICENSE 全文；三个关键文件为 `SerializedFieldSuppressor.cs` L1–64、`UnusedCoroutineReturnValue.cs` L1–120、`Microsoft.Unity.Analyzers.csproj` L1–35（均位于 `src/Microsoft.Unity.Analyzers/`）。
- 缓存：`<isolated-download-cache>/`。

### Roslyn/框架与一条真实诊断

- [项目 L3–13](https://github.com/microsoft/Microsoft.Unity.Analyzers/blob/a1ae8f287db28e0514a818f5cc2276125afbf5fe/src/Microsoft.Unity.Analyzers/Microsoft.Unity.Analyzers.csproj#L3-L13)：分析器目标 `netstandard2.0`，自身源码 `LangVersion=latest`；`Microsoft.CodeAnalysis.Analyzers` 与 `Microsoft.CodeAnalysis.CSharp.Workspaces` 均显式 `VersionOverride=[3.11.0.0]`。这是构建依赖基线，不是任意 Unity compiler 一定能装载此快照的实测结论。
- [README L20–36](https://github.com/microsoft/Microsoft.Unity.Analyzers/blob/a1ae8f287db28e0514a818f5cc2276125afbf5fe/README.md#L20-L36) 的 `.NET 10 / VS 2026` 是开发此仓库的构建测试要求，测试还需 Unity；**不是要求玩家端 Unity 项目改用 .NET 10**。
- [UNT0012 实现 L16–71](https://github.com/microsoft/Microsoft.Unity.Analyzers/blob/a1ae8f287db28e0514a818f5cc2276125afbf5fe/src/Microsoft.Unity.Analyzers/UnusedCoroutineReturnValue.cs#L16-L71)：注册 invocation；只分析直接作为 expression statement 的调用，语义绑定后要求方法所属类型继承 `MonoBehaviour`、返回匹配 `IEnumerator`，才报告未使用协程返回值。级别 Info、默认启用、跳过生成代码，不是字符串匹配任何叫 Coroutine 的方法。
- 同文件 [L74–118](https://github.com/microsoft/Microsoft.Unity.Analyzers/blob/a1ae8f287db28e0514a818f5cc2276125afbf5fe/src/Microsoft.Unity.Analyzers/UnusedCoroutineReturnValue.cs#L74-L118) 的 codefix 将调用包进 `StartCoroutine(...)`，支持 BatchFixer。规则能发现“调用了迭代器但没有启动协程”的常见错误，但仅检查形状/类型，不证明调用方意图。对返回非迭代器实现的 `IEnumerator`、有即时副作用的工厂方法，也不应机械套修复；这是源码推导的适用边界，未运行案例。

### Unity 消息、序列化误报与安全边界

- [SerializedFieldSuppressor L18–57](https://github.com/microsoft/Microsoft.Unity.Analyzers/blob/a1ae8f287db28e0514a818f5cc2276125afbf5fe/src/Microsoft.Unity.Analyzers/SerializedFieldSuppressor.cs#L18-L57) 条件抑制 `IDE0044`、`IDE0051`、`CA1823`、`CS0649`；识别 `SerializeField`、`SerializeReference`、`OdinSerializeAttribute`，也放行继承 Unity `Object` 类型上的 public 成员。它处理的是“C# 引用图看不到引擎赋值/使用”的问题，不代表证明每个此类字段在资产中真实有值；基类的完整属性匹配细节不在本次阅读范围。
- [规则索引 L52–78](https://github.com/microsoft/Microsoft.Unity.Analyzers/blob/a1ae8f287db28e0514a818f5cc2276125afbf5fe/doc/index.md#L52-L78) 列出对 Unity runtime 消息的 `IDE0051/IDE0060/CA1822/CA1801/IDE0052/IDE1006` 抑制，以及 `Invoke`/协程字符串调用、菜单和初始化属性等场景。**消息部分依据文档索引；其具体匹配实现未读**。Unity 生命周期函数/消息不等于 prefab/scene 中的任意 `UnityEvent` 持久化回调，不能因此声称后者全部受保护；抑制清单也没有覆盖所有第三方诊断 ID。
- [README L10–14、L51–59](https://github.com/microsoft/Microsoft.Unity.Analyzers/blob/a1ae8f287db28e0514a818f5cc2276125afbf5fe/README.md#L51-L59) 说明 VS Unity workload 会随附，VS Code 有官方 Unity 扩展，NuGet 另用于类库/高级用法。接入前应核对 IDE 与 Unity 编译实际装载的 DLL、是否重复注入，不把安装 NuGet 或 SDK 默认分析行为套给 Unity。
- 选读分析器代码没有外部审查服务调用；不需 CodeRabbit 账号才能执行这些本地规则。但未进行全仓网络/供应链审计，也未审核下载 NuGet 的二进制。项目 [L30–33](https://github.com/microsoft/Microsoft.Unity.Analyzers/blob/a1ae8f287db28e0514a818f5cc2276125afbf5fe/src/Microsoft.Unity.Analyzers/Microsoft.Unity.Analyzers.csproj#L30-L33) 含 restore 前后工具/Husky 执行目标，说明“只读项目文件”和“安全执行构建”是不同边界；本次没有 restore/build。

### 真实失败/争议

- README 直接记录 VSIX 与项目本地 analyzer 同时装载会产生重复诊断；不是假设性的“可能噪声”，但本次未重现。
- [issue #235](https://github.com/microsoft/Microsoft.Unity.Analyzers/issues/235) 报告 `1.13.0` 的 UNT0008 在 nullable Unity 对象上仍提示 null propagation。维护者在 [2023-01-26](https://github.com/microsoft/Microsoft.Unity.Analyzers/issues/235#issuecomment-1405353756) 说明这是 Info：Unity destroyed-object 的特殊相等语义使意图不明确；[2025-06-17](https://github.com/microsoft/Microsoft.Unity.Analyzers/issues/235#issuecomment-2980941402) 因该歧义关闭。它是有实际用户报告的语义取舍，**不是维护者确认后已修复的误报 bug**。本次未运行，不能据此给当前快照贴回归标签。

## 3. DotNetAnalyzers/StyleCopAnalyzers：团队风格，不是设计质量裁判

### 版本、许可、维护与阅读范围

- Canonical：`DotNetAnalyzers/StyleCopAnalyzers`，`master`；SHA `986988bd01f81e2430e91c32214e2186be45be3c`；commit `2026-11-03T20:21:57Z`。[固定提交](https://github.com/DotNetAnalyzers/StyleCopAnalyzers/commit/986988bd01f81e2430e91c32214e2186be45be3c) 是合并 PR #4396。未归档；`pushed_at=2026-11-04T16:40:17Z`；release 快照的 `1.3.171-beta`（`2026-11-04T16:40:52Z`）、`1.3.151-beta`、`1.3.149-beta` 均为 prerelease，不能省略 beta 风险说明。
- [LICENSE L1–21](https://github.com/DotNetAnalyzers/StyleCopAnalyzers/blob/986988bd01f81e2430e91c32214e2186be45be3c/LICENSE#L1-L21)：MIT。实际阅读 README L1–33、LICENSE 全文，及三个关键文件：`src/StyleCop.Analyzers/MaintainabilityRules/SA1402FileMayOnlyContainASingleType.cs` L1–153、`src/StyleCop.Analyzers/StyleCop.Analyzers.csproj` L1–64、`Directory.Packages.props` L1–47。
- 缓存：`<isolated-download-cache>/`。

### 支持范围与真实诊断

- [README L15–29](https://github.com/DotNetAnalyzers/StyleCopAnalyzers/blob/986988bd01f81e2430e91c32214e2186be45be3c/README.md#L15-L29)：可配置规则严重程度与团队风格；兼容表将 C# 1–6 对应 1.0.2、7–7.3 对应 1.1.0、8 对应 1.2 beta、9–15 对应 1.3 beta。这是项目声明，不能把它替换成目标 Unity Editor 的 Roslyn 装载测试。
- [项目 L4–14、L41–44](https://github.com/DotNetAnalyzers/StyleCopAnalyzers/blob/986988bd01f81e2430e91c32214e2186be45be3c/src/StyleCop.Analyzers/StyleCop.Analyzers.csproj#L4-L14)：目标 `netstandard1.1`，注释说明保持 Roslyn 1.2+ host 可装载的兼容意图；直接引用 `Microsoft.CodeAnalysis.CSharp`。但 [中央版本文件 L3–26、L44–46](https://github.com/DotNetAnalyzers/StyleCopAnalyzers/blob/986988bd01f81e2430e91c32214e2186be45be3c/Directory.Packages.props#L3-L26) 的 shared Roslyn 是 5.9.0，并明确另有条件导入的 shipping compatibility pins。**导入文件及该条件的赋值不在本次所读三文件中，故不把 5.9.0 误认成发布 DLL 的最低 Roslyn 要求，也不把注释当实测保证。**
- [SA1402 L31–110](https://github.com/DotNetAnalyzers/StyleCopAnalyzers/blob/986988bd01f81e2430e91c32214e2186be45be3c/src/StyleCop.Analyzers/MaintainabilityRules/SA1402FileMayOnlyContainASingleType.cs#L31-L110)：真实实现是每文件顶层类型约束，诊断级别 Warning；跳过 generated code 和包含 top-level statements 的文件，优先保留与文件名相符的类型，对其他相关类型报告；允许同名 partial 部分在一个文件。它没有分析模块职责、依赖反转、业务边界或对象协作。
- [L113–150](https://github.com/DotNetAnalyzers/StyleCopAnalyzers/blob/986988bd01f81e2430e91c32214e2186be45be3c/src/StyleCop.Analyzers/MaintainabilityRules/SA1402FileMayOnlyContainASingleType.cs#L113-L150) 按配置筛选 class/interface/struct/enum/delegate，跳过 file-local 类型。规则分类名叫 Maintainability 并不能证明“拆成一文件一类后设计更好”。

### 依赖安全、Unity 与真实摩擦

- 能力主要是本地 Roslyn 语法/配置判断，不依赖 CodeRabbit 类外部审查账号。项目还引用构建期 code-generation analyzer，[项目 L46–61](https://github.com/DotNetAnalyzers/StyleCopAnalyzers/blob/986988bd01f81e2430e91c32214e2186be45be3c/src/StyleCop.Analyzers/StyleCop.Analyzers.csproj#L46-L61)；中央文件包含测试/工具依赖，不能把整张表都称作使用者运行时依赖。本次未做包漏洞扫描、签名验证或全仓网络审计。
- 所读 SA1402 不涉及 Unity 生命周期或序列化，对 UnityEvent/SerializeField 也没有特别保护逻辑。它不是查 unused 的分析器，因此不能用 Unity suppressor 来证明“所有 StyleCop 风格诊断都已被修正”。Unity 仍需单独确认 host 兼容、分析器接入、配置生效、生成文件与 asmdef 范围；团队自定义风格不要在第一轮一律升 Error。
- [issue #4377](https://github.com/DotNetAnalyzers/StyleCopAnalyzers/issues/4377) 是 `2026-10-22` 的真实升级摩擦：修正 topLevelTypes 行为后 SA1649 增多，调整配置又触发 SA1402。[维护者讨论](https://github.com/DotNetAnalyzers/StyleCopAnalyzers/issues/4377#issuecomment-6340252656) 及 [报告者收尾](https://github.com/DotNetAnalyzers/StyleCopAnalyzers/issues/4377#issuecomment-6413416112) 说明默认只含 class，与 struct/helper 的组织方式不符，最终通过团队 code-style 配置处理并关闭。不是“风格工具发现设计缺陷”，也不是本次复现的引擎 bug。

## 4. dotnet/roslynator：有 Unity 分支，但 codefix 不能视为保语义证明

### 版本、许可、维护与阅读范围

- 本次 API 的 canonical 仍是 **`dotnet/roslynator`**，不需要替换为旧所有者路径；`main`；SHA `b7ba8866006f39b4ffec30743b00cbf82070db5c`；commit `2026-10-31T14:39:29Z`。[固定提交](https://github.com/dotnet/roslynator/commit/b7ba8866006f39b4ffec30743b00cbf82070db5c) 明确修复 RCS1146 在比较左侧为 null 时崩溃（#1862），是具体诊断维护信号，不只是依赖更新。未归档；`pushed_at=2026-11-01T09:50:14Z`；release `v5.0.1`（`2026-10-04T13:30:38Z`）、`v5.0.0`、`v4.16.1`。
- [LICENSE.txt L1–12](https://github.com/dotnet/roslynator/blob/b7ba8866006f39b4ffec30743b00cbf82070db5c/LICENSE.txt#L1-L12)：Apache-2.0，不是 MIT；该文件以简短许可声明引用 Apache 正文。再分发义务应按 Apache-2.0 和实际分发内容核对，本次未下载其外链许可正文。
- 实际阅读 README L1–82、LICENSE 全文；三个关键文件：`src/Analyzers/CSharp/Analysis/UnusedMember/UnusedMemberAnalyzer.cs` L1–333、`src/Analyzers.CodeFixes/CSharp/CodeFixes/UnusedMemberCodeFixProvider.cs` L1–78、`src/Directory.Build.props` L1–121。
- 缓存：`<isolated-download-cache>/`。

### Roslyn 变体、诊断与修复的真实行为

- [Directory.Build.props L3–56](https://github.com/dotnet/roslynator/blob/b7ba8866006f39b4ffec30743b00cbf82070db5c/src/Directory.Build.props#L3-L56) 自身代码语言版本为 C# 12，存在 `roslyn3.8`、`roslyn4.7`、`roslyn5.0` 编译变体，缺省为 5.0.0；CLI Roslyn 也是 5.0.0；测试库依赖下限 3.8 与仓库测试运行版本 5.0 又是不同概念。**存在旧版本分支不等于当前发布包一定包含该变体**；本次未读发布打包矩阵和 analyzer csproj，目标 TFM、具体 release 包对当前 Unity compiler 的兼容性未确认。
- [README L3–18](https://github.com/dotnet/roslynator/blob/b7ba8866006f39b4ffec30743b00cbf82070db5c/README.md#L3-L18) 明确新版 IDE 扩展不包含 analyzers，诊断要用 NuGet；VS Code 扩展依赖 legacy OmniSharp，C# Dev Kit 场景另用 NuGet。不能把 IDE 扩展可运行等同于 Unity 编译必有这些规则。
- RCS1213 对应的 unused member analyzer [L48–174](https://github.com/dotnet/roslynator/blob/b7ba8866006f39b4ffec30743b00cbf82070db5c/src/Analyzers/CSharp/Analysis/UnusedMember/UnusedMemberAnalyzer.cs#L48-L174) 跳过 partial 类型，考虑 StructLayout，主要收集 private 成员。带属性的 method 直接不纳入；在 Unity analysis 明确启用、所属类型继承 MonoBehaviour、方法名位于 UnityScriptMethods 集合且返回形态符合条件时，排除生命周期方法；`IEnumerator Start` 有特例。随后 [L177–204、L308–331](https://github.com/dotnet/roslynator/blob/b7ba8866006f39b4ffec30743b00cbf82070db5c/src/Analyzers/CSharp/Analysis/UnusedMember/UnusedMemberAnalyzer.cs#L177-L204) 经 walker 与部分 DebuggerDisplay 处理后报告未使用成员。
- [UnusedMemberCodeFixProvider L20–59](https://github.com/dotnet/roslynator/blob/b7ba8866006f39b4ffec30743b00cbf82070db5c/src/Analyzers.CodeFixes/CSharp/CodeFixes/UnusedMemberCodeFixProvider.cs#L20-L59) 的修复是删除 member 或变量声明；不是运行时可达性证明，也没有在该修复入口读取 scene/prefab 的验证步骤。误判后果可能是删除真实被动态机制调用的代码，语义风险明显高于调整空白。

### Unity、依赖安全与真实失败

- 上述分支说明其并非完全不懂 Unity，但 `IsUnityCodeAnalysisEnabled()` 的默认值、配置传入路径、完整 callback 名单以及 walker 对序列化字段/字符串调用的完整处理**未在本次三个文件中核实**。不能断言一定误删 SerializeField，也不能承诺生命周期、UnityEvent、反射和自定义消息都已保护。普通 Unity serialized asset 引用是否有效，不是这份入口源码能证明的。
- [issue #1596](https://github.com/dotnet/roslynator/issues/1596) 报告把 RCS1213 放入 Unity `Default.ruleset` 后回调被标记。[报告者 2024-12-26 更正](https://github.com/dotnet/roslynator/issues/1596#issuecomment-2563087583)：VS Code 与 `dotnet format` 实际读取了 `.editorconfig`，原先这部分判断错误；但当时仍有 OnValidate 误报，并报告 Unity 的该 ruleset 场景未采用设置。issue 已于 `2025-01-01` 关闭，不能扩大为当前所有 Unity 都忽略 `.editorconfig`，更不能当成本次实测。
- 本次 default HEAD 的 RCS1146 null 比较崩溃修复，只由 commit 元数据证明“有这个修复提交”；未阅读该修复实现/测试，也未复现崩溃。
- 所读本地诊断/codefix 没有云端审查账号依赖；自身构建 props 引入 Roslynator 其他分析器包，不代表使用者得到相同配置。未审计完整 CLI、NuGet 二进制或供应链安全。**当前 Unity 支持未知**，需按实际 Editor/compiler、解析到的包变体和配置做小范围验证；验证前不建议 unattended Fix All，尤其是删除成员类修复。

## 5. BenMorris/NetArchTest：自己声明依赖方向，不能自动证明架构正确

### 版本、许可、维护与阅读范围

- Canonical：`BenMorris/NetArchTest`，`master`；SHA `a761f63b694a6facd4be01fbc8fe2ae26579572e`；commit `2023-07-03T11:01:36Z`。[固定提交](https://github.com/BenMorris/NetArchTest/commit/a761f63b694a6facd4be01fbc8fe2ae26579572e) 合并 Mono 依赖更新。未归档；`pushed_at=2024-07-29T18:02:58Z`；API release 最新列出 `v1.3.2`（`2021-05-23T18:47:20Z`）。默认分支三年多未提交、release 更旧，不能用“未归档”声称活跃维护；2024/2025 issue 回复仍是可见的支持信号。
- [LICENSE L1–21](https://github.com/BenMorris/NetArchTest/blob/a761f63b694a6facd4be01fbc8fe2ae26579572e/LICENSE#L1-L21)：MIT。实际阅读 README L1–128、LICENSE 全文；三个关键文件：`src/NetArchTest.Rules/Dependencies/DependencySearch.cs` L1–85、同目录 `TypeParser.cs` L1–90、`src/NetArchTest.Rules/NetArchTest.Rules.csproj` L1–29。
- 缓存：`<isolated-download-cache>/`。

### 方向机制、依赖与覆盖盲区

- [README L17–27、L49–70](https://github.com/BenMorris/NetArchTest/blob/a761f63b694a6facd4be01fbc8fe2ae26579572e/README.md#L17-L27) 展示的方向是：先选 source 类型/namespace，再对这些类型施加 `ShouldNot().HaveDependencyOn(targetNamespace)`。这是测试作者声明“谁不能依赖谁”，不是工具从项目自动推导正确分层；反向约束要另写，命名空间命名也不等于业务层确实正确。
- [DependencySearch L18–82](https://github.com/BenMorris/NetArchTest/blob/a761f63b694a6facd4be01fbc8fe2ae26579572e/src/NetArchTest.Rules/Dependencies/DependencySearch.cs#L18-L82) 接收 Mono.Cecil `TypeDefinition` 集合与目标字符串，建立 `CachedNamespaceTree`，逐个 source type 建 `TypeDefinitionCheckingContext`，按 Any/All/Only 查询返回匹配类型；普通 HaveDependency 查询还传入搜索字段常量的开关。其输入不是源代码文本，也不是 Unity asset 数据。具体上下文遍历与 namespace tree 匹配实现未读，不能宣称任意名称前缀、所有 IL 位置、间接依赖传递闭包都已验证。
- [项目 L3–22](https://github.com/BenMorris/NetArchTest/blob/a761f63b694a6facd4be01fbc8fe2ae26579572e/src/NetArchTest.Rules/NetArchTest.Rules.csproj#L3-L22)：目标 `netstandard2.0`，版本 `1.3.2`，直接依赖 `Mono.Cecil 0.11.5`。它不是 Roslyn diagnostic analyzer，不要求由 Unity compiler 装载 Roslyn 插件，而是对所选程序集做架构测试。该兼容声明也不等于已经验证 Unity Test Framework、具体 Editor 平台、IL2CPP 或 stripping 后产物。
- [TypeParser L7–29、L35–85](https://github.com/BenMorris/NetArchTest/blob/a761f63b694a6facd4be01fbc8fe2ae26579572e/src/NetArchTest.Rules/Dependencies/TypeParser.cs#L7-L29) 反射调用 Mono.Cecil **非公开** TypeParser，再读取嵌套名、泛型和数组/指针等字段。这是对依赖内部布局的耦合，不能把升级 Cecil 当无风险安全更新。它也说明不能笼统说“任何字符串类型名都不支持”；但这并不能覆盖运行期拼接、配置/网络提供的类型名与任意反射执行路径。
- 静态程序集规则看不到一般的 scene/prefab/ScriptableObject 持久化对象关系、Addressables 数据和资源命名约定，也不能仅凭类型依赖证明生命周期顺序、线程安全、业务规则正确或运行时协作关系。条件编译、Editor/Player 与 asmdef 的不同编译输入需要分别纳入检查；未选进来的程序集就是覆盖空洞，不能拿单一宿主测试结果代表全部 Unity 平台。
- 所读代码没有外部审查服务或账号依赖，但它要解析受测程序集，且自定义规则本身也是可执行代码。没有运行、不意味已经审计了所有依赖/程序集解析输入的安全性；本次未做漏洞数据库或二进制核验。

### 真实失败：测试通过也可能没有检查到目标

- [issue #150](https://github.com/BenMorris/NetArchTest/issues/150) 的“深层 namespace 未正确断言”报告，第一份示例实际上把生产 namespace `UnitTests.Tests.*` 与过滤 namespace `UDWR.CustAlertLevel.Tests.*` 混用了。[维护者回复](https://github.com/BenMorris/NetArchTest/issues/150#issuecomment-2566391122) 明确说明没有选中类型；因此不能把这个示例当作已确认的 namespace 深度解析 bug。
- 同一线程 [后续用户报告](https://github.com/BenMorris/NetArchTest/issues/150#issuecomment-2609771640) 指出 `InCurrentDomain()` 示例是否失败会受其他测试显式引用类型、从而促使程序集装载影响；[后续解释](https://github.com/BenMorris/NetArchTest/issues/150#issuecomment-2666688263) 建议显式指定程序集。该解释来自参与者而非本次实验；issue 于 `2025-05-21` 关闭，并不证明新版本已自动消除此类测试设置问题。
- 有价值的防护结论是：优先按明确程序集清单/marker 类型选择目标，并在断言依赖前验证选中类型集合非空、关键类型确在集合中；给规则配一个故意违反方向的负例。这里是据源码与报告提出的验证要求，**没有声称本次运行了这些测试**。保留该工具作架构约束候选，但维护陈旧、程序集覆盖和私有 Cecil API 耦合必须列入采用成本。

## 横向取舍：不把不同层次的结果合成一个“质量分”

| 工具 | 这次证据支持的职责 | 不支持的推论 | 对 Unity 的当前取舍 |
| --- | --- | --- | --- |
| CodeRabbit Skill | 用外部 CLI/服务审查变更、保留等级、辅助逐项核实和修复 | Skill 开源所以审查引擎开源；零发现就安全；AI 建议可直接执行 | 隐私/认证/服务准入先行；仅作补充，不作唯一闸门 |
| Microsoft.Unity.Analyzers | Unity 类型/调用规则与部分通用 C# 误报抑制 | 能证明所有资产回调、所有第三方诊断都无误报 | 优先核对已有随附版本与实际装载范围，避免重复接入 |
| StyleCopAnalyzers | 语法、文件组织与团队风格一致性 | 风格告警等于设计/架构缺陷 | 可选且按团队约定启用，升级审查配置变化，不默认全设 Error |
| Roslynator | 多种诊断/重构；所读 unused 规则存在 Unity 条件分支 | codefix 天然保语义；旧 Roslyn 分支保证当前 Unity 可用 | host/package/config 验证前不作无人值守删除式修复 |
| NetArchTest | 团队显式表达并检查选定程序集的依赖方向 | 一条 passing rule 证明分层正确或所有程序集都被检查 | 有条件保留：明确程序集、非空校验、负例与覆盖清单 |

本次没有可比的运行性能、误报率、召回率、修复成功率或维护响应 SLA 数据；不进行虚构排名。分析器自身构建所用 SDK/语言版本、分析器宿主 Roslyn、Unity 工程 C# 语言/API profile 与 Player backend 是四个不同层面，不能互相替代。

## 取证失败、未验证项与复核入口

- **真实取证失败**：第一次批量下载在处理 StyleCop 的 `commit.json` 时，Python 默认 Windows `gbk` 解码产生 `UnicodeDecodeError`；此前 CodeRabbit 与 Unity 选定文件已下载。随后显式使用 `encoding="utf-8"` 读取元数据，完成剩余仓库；未更改权限、未执行仓库数据，也未把这次本地解码失败归因于工具质量。
- 除上述解码错误外，实际发出的仓库 metadata/tree/contents/releases/issue/comments API 请求均成功；没有遭遇网络安全拒绝，也没有改域名、代理或提权绕过。另对研究目录与课题目录分别执行只读 `git rev-parse --show-toplevel`，都返回 exit 128 / `not a git repository`，因此无可报告的 Git 工作区状态；没有初始化仓库。本次没有安装/执行尝试，故不存在可报告的本地“安装失败”“编译通过”或“扫描效果”。
- 每仓库固定源码由其 `commit.json` 的完整 SHA 加 `files/` 下同相对路径复核；维护信号核对 `repo.json`、`releases.json`；公开失败与后续解释核对 `issue-N.json`、`issue-N-comments.json`。缓存仅是本机定点复核副本，不保证永久存在，固定 SHA 链接才是后续重新取证入口。
- 明确未验证：CodeRabbit 外部隐私合同与引擎源码/实际 CLI 版本；StyleCop shipping compatibility pin 的导入链；Roslynator 发布包变体/TFM 与当前 Unity；NetArchTest 完整 IL/namespace 匹配与传递闭包；所有工具在用户实际 Unity 工程上的装载、配置、运行表现及二进制供应链安全。
