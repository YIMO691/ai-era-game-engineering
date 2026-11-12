# ECC：AI 代码质量工程闭环的独立只读取证附录

> 公开导出说明（2026-11-12）：以下为原稿研究或通用模板，不是实际配置；历史状态、检查与未运行项不因公开授权而升级。来源与排除边界见 [README](README.md) 和 [导出清单](export-manifest.json)。

## 研究边界与结论

研究对象是用户提供的 `affaan-m/everything-claude-code`。GitHub API 将该入口解析为当前仓库 **`affaan-m/ECC`**。本附录研究其“计划—测试—实现—评审—验证—反馈”构造，不是安装建议，也没有执行任何该仓库源码、脚本、安装器、测试、hook 或构建命令。未调用 Skill、Workflow 或其他 Agent；未改配置，未接触业务工程。

**结论：值得借鉴的是把任务约束、RED/GREEN 证据、角色化评审、批量重构与最终验证分开组织；不能把它整体当作已经验证的 Unity 质量门禁。** 本次看到的流程与专业 Agent 主要是提示词；实际 hook 能调用确定性工具，但被审的 `quality-gate` 即使 strict 为 true 也只是记录诊断，不会据检查失败返回阻断。存在自动写文件、工具缺失时跳过、异常时放行及按 profile 禁用的路径。C# 资产真实存在，然而已读 reviewer 主要面向通用 .NET/Web，而所读质量 hook 没有 `.cs` 分支。效果、准确率、漏报率、性能收益均未实测，未知。

## 固定版本与取证来源

- 研究问题：在不安装、不运行的前提下，ECC 哪些结构可用于 Unity/C# 的 AI 代码质量闭环，哪些仍需独立确定性门禁？停止条件是核对流程、专业 C# review、TDD/重构及一条实际质量 hook 链，并显式记录不足；不扩展成全仓安全审计。
- 本附录使用同仓库单一来源组 **`ER-20261105-ai-code-quality-workflow-ecc-01`**；S1–S12 只是该组内部文件定位符，不是 12 份独立交叉验证。供主线程在 `sources.md` 单次登记后引用；本任务按授权仅写此附录，不修改来源总表或课题状态。
- 来源机构/维护者：GitHub 仓库 owner `affaan-m`；来源类型：固定版本源码、配置、项目自述与 GitHub 元信息。12 文件正文 `read_status=read`；未展开的 tree 路径仅 `discovered`；所有 `experiment_status=not-run`。文件内容/分支的存在为 `direct`，行为后果和 Unity 适配为 `inference`，效果保证和未读依赖为 `unverified`。这些状态不把静态推导升级为实验。
- 取证日期：2026-11-05；远端状态是取证当时快照，不代表未来状态。
- 原入口：<https://github.com/affaan-m/everything-claude-code>。
- API 返回 `full_name=affaan-m/ECC`、`owner.login=affaan-m`、`default_branch=main`、`archived=false`。
- 固定完整 SHA：**`b38be6a7f6350964d59328b52f0624e1d1d552d1`**。
- author 与 committer 日期均为 **2026-10-30T03:06:32Z**。
- [固定提交](https://github.com/affaan-m/ECC/commit/b38be6a7f6350964d59328b52f0624e1d1d552d1)：合并 PR #3809，提交说明为整合七项已评审的可靠性与指引修复。这只是维护动作信号，不是这些修复效果的独立证明。
- repo `pushed_at=2026-11-02T04:56:08Z`。它是仓库推送时间，不等同于默认分支提交日期，因此与上述日期不同不构成矛盾。
- 缓存元信息中的 `created_at=2026-01-18T00:51:51Z`，`updated_at=2026-11-05T08:28:14Z`；297447 stars、43976 forks、233 open issues。数字会变化；open issues 不是已确认缺陷数，热度不是质量测量。
- 可选 release API 返回 `v2.2.3`，`published_at=2026-10-01T23:00:36Z`，`draft=false`、`prerelease=false`、`target_commitish=main`。这是未固定标签目标的维护元数据；**不能据此断言该 release 等于本次 SHA**。
- 取证通过只读 `gh api`：repo 元信息、`commits/main` 固定 SHA、该 SHA 的 commit、`git/trees/<SHA>?recursive=1` 及 `contents/<path>?ref=<SHA>`。tree 返回 `truncated=false`。没有 clone、checkout、依赖解析或包安装。
- 缓存目录：`<isolated-download-cache>/`。由 `tempfile.mkdtemp` 新建为空，再保存下载内容；包含 `tree.json`、`repo-metadata.json`、`commit.json`、12 个定点文件与成功重试输出转录的 `latest-release-summary.json`。
- 所有用于缓存与解析的 Python 均以 **`python -I`** 从可信工作目录启动，下载目录仅作为路径参数/数据路径使用；没有从下载目录执行解释器，也没有 import/require 其中源码。

## 12 个关键文件与实际 Read 范围

下列链接全部绑定完整 SHA。表内范围是实际调用 Read 所读范围；除此之外，对 README 做过标题/关键词定位，对 tree 和元信息做过隔离 Python 数据解析。不把 tree 中发现但未读正文的文件当成实现证据。

| ID | 文件与固定 GitHub 行链接 | 实际 Read 范围 | 用途 |
|---|---|---|---|
| S1 | [README.md](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/README.md#L130-L169) | 130–170；267–314；448–497；558–643；1223–1261；1314–1341；1370–1433；1941–1978 | 项目定位、流程承诺、依赖、OS、scope、外发声明 |
| S2 | [LICENSE](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/LICENSE#L1-L21) | 1–21，全文件 | MIT 条件与免责声明 |
| S3 | [rules/common/development-workflow.md](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/rules/common/development-workflow.md#L1-L44) | 1–44，全文件 | 常驻规则层的研究、规划、TDD、review 与 CI 要求 |
| S4 | [agents/csharp-reviewer.md](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/agents/csharp-reviewer.md#L1-L110) | 1–110，全文件 | C# 专业评审提示词及诊断命令 |
| S5 | [agents/tdd-guide.md](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/agents/tdd-guide.md#L1-L100) | 1–100，全文件 | RED/GREEN、覆盖率、边界与回归测试提示词 |
| S6 | [agents/refactor-cleaner.md](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/agents/refactor-cleaner.md#L1-L94) | 1–94，全文件 | 静态检测、引用复核、小批删除与测试 |
| S7 | [hooks/hooks.json](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/hooks/hooks.json#L1-L285) | 1–285，全文件 | 实际事件绑定、入口、超时、异步配置 |
| S8 | [scripts/hooks/posttooluse-dispatcher.js](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/scripts/hooks/posttooluse-dispatcher.js#L1-L347) | 1–347，全文件 | PostToolUse 分派、profile 检查、输出合并与失败处理 |
| S9 | [scripts/hooks/stop-format-typecheck.js](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/scripts/hooks/stop-format-typecheck.js#L1-L290) | 1–290，全文件 | 批量自动格式化、TS 检查、超时与 fail-open |
| S10 | [scripts/hooks/quality-gate.js](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/scripts/hooks/quality-gate.js#L1-L172) | 1–172，全文件 | 名为 quality gate 的实际扩展名、fix/strict 与退出语义 |
| S11 | [scripts/hooks/run-with-flags.js](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/scripts/hooks/run-with-flags.js#L1-L353) | 1–353，全文件 | profile 包装器、缺脚本、异常、截断、子进程退出码 |
| S12 | [scripts/hooks/post-edit-format.js](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/scripts/hooks/post-edit-format.js#L1-L118) | 1–118，全文件 | 对照 quality-gate 注释所指的自动改文件实现 |

补充 README 段落定位：[安装边界 267–310](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/README.md#L267-L310)、[scope 与 hook 448–493](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/README.md#L448-L493)、[配置写入与外部 review 582–640](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/README.md#L582-L640)、[闭环与概念边界 1223–1259](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/README.md#L1223-L1259)、[OS 与 harness 1314–1336](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/README.md#L1314-L1336)、[profile 与数据落盘 1370–1433](https://github.com/affaan-m/ECC/blob/b38be6a7f6350964d59328b52f0624e1d1d552d1/README.md#L1370-L1433)。

## 短主张表

| 主张 | 证据 | 分层结论/限制 |
|---|---|---|
| 有从规划到测试、评审、最终验证的闭环表达 | S1 1223–1247；S3 9–44 | 流程提示词存在；尚不能证明每次执行都被强制或留有正确证据 |
| 专业 C# reviewer 不是空泛宣传 | S4 19–106；tree 有 C# rules/testing/patterns | 真实文本资产；不是 Unity 专用检查器，也不是运行过的编译/测试结果 |
| TDD 要求先见失败再见通过 | S5 27–49、59–87 | 可以作为证据模板；默认 npm/Playwright 语言生态不适用于所有工程 |
| `quality-gate` 不等于阻断门禁 | S10 69–135、144–152；S8 114–140、265–281 | strict 仅控制日志；该模块返回原输入字符串，被归一化为 exit 0，没有质量失败的 block 决策 |
| 自动改文件真实存在 | S9 88–116；S12 42–80；S10 70–99、110–130 | 格式化工具 `--write`，Go `-w`；fix 不总是默认开启，但 Stop 格式化路径主动写入 |
| 失败有明确放行路径 | S11 211–242、282–300、350–353；S9 145–187、245–279 | 缺脚本、部分异常/超时并不必然阻断；不能笼统说所有 hook 都 fail-open |
| “跨平台”不表示等能力 | S1 1314–1336；S9 104–116、145–172 | Windows native 与可选 shell/observer/memory 功能有已声明限制；本机可运行性未验证 |
| 安装范围与外发必须另审 | S1 475、584–640、1419–1431；S7/S8 的额外入口 | README 有用户级/项目级写入与跨提供方 diff 外发说明；未读安装器及全部 hook，完整覆盖/网络行为未知 |

## 提示词闭环与确定性检查的分界

**规则/上下文层。** S3 要求先研究复用、计划、TDD、review，再提交，末尾要求 CI 通过；这些文字没有自行运行 CI。其“每次实现先 GitHub 搜索”“先生成多个规划文档”也不宜全盘移植到私有游戏工程：搜索内容可能含专有标识，繁重文档也应按变更风险裁剪。README 将 rules 定义为常驻上下文、Agent 定义为隔离角色、hook 定义为上下文之外的事件脚本，这是结构划分，不是强制执行结果。

**TDD/重构层。** S5 具有先运行失败测试、最小实现、重构、边界与错误路径清单；默认命令是 `npm test`、`npm run test:coverage`，E2E 例子是 Playwright。S6 的检测命令是 `npx knip/depcheck/ts-prune/eslint`，随后 grep 动态引用、确认公共 API、小批删除与批后测试。两者均有 Write/Edit/Bash 权限声明，不能当作纯只读分析器；“每批提交”等操作也需要本地授权边界覆盖。

**专业 review 层。** S4 以 `.cs` diff、可用时的 `dotnet build` 与 `dotnet format --verify-no-changes` 起步，覆盖异常吞没、async、空值、热路径 LINQ 等；给出带文件行号与严重度的报告格式。“Approve/Block”在此是 reviewer 的输出标准，未见它直接连接 GitHub merge protection 的实现。其工具集虽未列 Edit/Write，却包含 Bash，不能据此视为技术上不可写或不联网。

**阈值不是普遍质量证明。** S3/S5 的 80%+ coverage、S4 的 50 行方法与 4 层嵌套是启发式规则。覆盖率不能证明断言有效、需求正确、竞态不存在，也不能保证帧耗时/内存；行数不能替代职责和复杂度分析。S5 95–100 的 pass@1、pass@3、pass^3 是要求文本，未给出本次运行样本或统计口径，不当作实证。缺陷率下降、独立 review 的增益、所谓学习效果都未知。

## hook 实际链路、自动修改与失效处理

1. **绑定而非仅有脚本。** S7 144–165 将 PostToolUse 分成 sync 与 async 两个 dispatcher，timeout 分别 30/45 秒；S8 34–68 中 accumulator 在 sync，quality-gate 在 async，匹配 Edit/Write/MultiEdit，profile 为 standard/strict。S7 207–214 将 Stop 绑定至 `stop-format-typecheck`，timeout 300 秒。profile 过滤依赖未读的 `lib/hook-flags`，不能仅凭脚本存在宣称它在所有安装模式下启用。
2. **`quality-gate` 的真实能力。** S10 根据 `.ts/.tsx/.js/.jsx/.json/.md` 选择 Biome/Prettier，根据 `.go/.py` 选择 gofmt/Ruff；没有 `.cs`。fix 仅在 `ECC_QUALITY_GATE_FIX=true` 时开启；`ECC_QUALITY_GATE_STRICT=true` 仅让部分非零结果写 stderr。工具不可解析或无 formatter 时直接 return；所有结果最终返回原始输入，未构造非零 exit 或 block。它是轻量格式/局部 lint 辅助，不是 build、测试、覆盖率、SAST 的统一质量验收。
3. **注释与新链路须分开。** S10 9–12、77–80 认为 JS/TS 的 Biome 已由 `post-edit-format` 处理并跳过；但本次 S7/S8 的实际默认绑定是 accumulator → Stop 批处理，没有直接绑定 S12。S9 确实有 `biome check --write`/Prettier `--write`；因此不能说 JS/TS 完全不格式化，也不能仅按旧注释说每次 edit 都立即格式化。accumulator 的内容与依赖未在本次 12 文件中展开，确切收集行为未知，需主线程优先复核。
4. **自动写入与重试。** S9 88–116 在文件存在且找到 formatter 时主动写入；200 行在处理前删除 accumulator，失败后本模块未见重新入队。207–225 只处理 JS/TS，排除识别出的插件 clone 路径。Windows `.cmd` 批处理遇到空白等不安全路径字符时跳过；formatter 失败被 catch，Windows formatter 分支仅检查 `result.error`，未据非零 status 阻断。
5. **类型检查并不等于全工程门禁。** S9 145–187 调用 `npx tsc --noEmit --pretty false`，仅打印与编辑文件路径匹配的最多 10 行诊断；没有设置检查失败的非零退出。工具缺失/Windows 超时可 return，其他异常也被外层捕获。`npx tsc` 未显式加禁止下载选项，若本地依赖不足可能触发 npm 的包解析/网络访问；具体行为取决于 npm/环境，未运行，不能声称离线或无需依赖。
6. **失败处理有多种语义。** S8 248–281 对子 hook 的非零退出保留首个退出码并继续，exception 则记日志；结构化 block 会合并并以成功命令退出向 harness 传达。S8 327–331 的顶层 rejection 设 exit 0，但模块顶层 require 失败不在该 catch 的覆盖范围，不能笼统说“所有失败都成功退出”。S11 在脚本不存在、越界路径、direct run 异常时 exit 0；legacy 子进程基础设施失败返回 1，并转发正常 status。超长输入对指定 GateGuard/MCP hook 可 exit 2，且有显式绕过/放行开关；其他路径多为清空原样回显并继续。不能把 quality-gate 的非阻断性推广为所有安全 hook 都不阻断。
7. **外发与落盘边界未穷尽。** 已读格式化/quality 模块正文中未见直接 HTTP 上传，但它们会调用工具并 import 未展开依赖。S8 还加载 observe、metrics bridge、governance、context monitor、hookify 等未审实现，S7 还有 session/evaluate/cost 等入口。本次不能给出“无外发、无遥测、无隐私风险”的结论。README 283 声称不会自动上传诊断，这不是全部 runtime 无网络证明；640 明示可选 Astra review 会把 diff 发给 OpenAI，且把调用视为同意。本次没有调用它。1419–1431 还说明 session、learned skills、aliases、metrics 会落在 agent data root。

## 依赖、OS、C# 与 Unity 的实际适配

- **基础依赖是文档要求，不是本机验证结果。** S1 168–169 要求 Node.js 18+；Claude plugin setup 还需 Git 与 Claude Code 2.1+ on PATH。S7 的命令确实以 Node 入口启动；S9/S10/S12 再依赖本地 formatter、TypeScript、gofmt、Ruff 等工具。formatter 解析器与包清单未纳入本次内容审查，因此精确 npm 依赖、锁定策略与解析时是否联网未知。
- **OS 不等价。** README 声明 core 支持 Windows/macOS/Linux，同时明确 Windows native 的 observer daemon、memory-vault 写入缺陷及 shell 功能依赖 Git Bash/WSL；macOS 系统 Bash 3.2 与独立 GAN 路径亦有声明限制。这是固定版本 README 自报，不代表关联 issue 在取证时仍未关闭。本次未读取 issue 当前状态。S9/S12 可见 Windows 特殊路径与 `.cmd` 分支，说明有兼容处理，但不能据此保证用户 Windows 环境可用。
- **C# 支持有实物，但偏 .NET。** tree 定位到 `agents/csharp-reviewer.md`、`rules/csharp/{coding-style,hooks,patterns,security,testing}.md`、`skills/{csharp-testing,dotnet-patterns}/SKILL.md`。只有 reviewer 正文在本次已读集合中，其他仅证实路径存在。S4 框架检查集中在 ASP.NET Core、EF Core、Minimal APIs、Blazor。tree 中未找到名为 `unity` 或 `unity-*` 的路径段；这不能证明所有正文均不提 Unity，只说明本次没有定位到专门 Unity 目录/文件。所读 hook 没有 C# 编译或测试执行分支。

| Unity 场景 | 可借鉴 | 不宜直接套用/需补充 |
|---|---|---|
| 纯 C# 领域逻辑、算法、协议转换、边界条件 bug | 先复现失败、小步实现、回归测试、错误路径 review、带行号发现 | 需选择工程实际测试入口；`dotnet test` 成功不等同于 Unity 编译或目标平台可运行 |
| MonoBehaviour、PlayerLoop、资源加载与异步 | 异常不吞、取消/生命周期、分离评审上下文 | 通用 `ConfigureAwait(false)`、DI、record、sealed 建议须结合 Unity 主线程/API、序列化和版本约束，不能机械当 HIGH 缺陷 |
| 场景/Prefab、UnityEvent、序列化字段、反射与动态加载重构 | 小批改动、明确保留公共契约、逐批验证 | knip/ts-prune/grep 不能证明 Unity 对象未使用；需资源引用与 GUID/.meta、序列化迁移及运行时可达性证据，否则误删风险高 |
| 帧时间、GC、IL2CPP/AOT、Burst/Jobs、平台构建 | 将性能/平台风险写成验收条目，评审热路径分配 | coverage、格式化与方法行数不能代替 Unity Profiler、目标设备、Player build 和平台专项验证 |
| Editor 与 PlayMode 回归、引擎集成 | RED/GREEN 日志、可重放命令、最终验证清单 | 需要另接 Unity Test Framework/EditMode/PlayMode 与适配版本的批处理构建；ECC 本次证据不能证明这些已覆盖 |

## scope、覆盖风险、许可与维护信号

**scope/覆盖风险只作研究，不执行安装。** README 475 声明手动 Claude 安装可进入用户级 `~/.claude/skills/` 或项目级 `.claude/skills/`；584–595 声明手动 hook 安装会把脚本放到用户配置根并注册 `settings.json`，plugin 则由 harness 自动加载。文档警告 plugin 与 full manual 叠加会重复执行，且不要直接复制原始 hooks JSON 到 settings；Windows root 为 `%USERPROFILE%\.claude`。这意味着用户级 hook 可能跨项目生效，不宜把“有项目安装模式”误读为“所有路径都天然项目隔离”。README 声称保护用户已有文件、追踪 ECC-owned 项并支持安全卸载；**安装器、状态追踪、冲突解决和卸载实现没有在本次 12 文件展开，真实覆盖/回滚行为未知**。本次无配置写入。

**许可。** S2 为 MIT，版权所有者 `2026 Affaan Mustafa`；复制或分发软件副本/实质部分时需保留版权及许可声明，并以 AS IS、不提供担保。本附录为原创分析和必要短标识/命令引用，没有复制第三方长段。MIT 不替第三方依赖、外部运行时/服务背书，也不构成安全或效果保证。

**维护信号。** 仓库未归档，近期有推送、merge 与正式 release 元数据；tree 有 CI、reusable-test、reusable-validate、release、supply-chain-watch 等 workflow 路径。仅检查路径，未读它们的任务、权限与具体覆盖，也未读运行结果，所以不能说当前 CI 全绿、支持矩阵已实测或供应链已经安全。README 1948–1965 记载 hook 自动加载最低版本与历史重复加载问题，1314–1336 主动列出兼容限制；这些提高了可审查性，但不是可靠性量化结果。

## 失败记录与主线程复核点

- 一次普通网络失败：可选 `gh api repos/affaan-m/ECC/releases/latest` 在隔离 Python 的 subprocess 中报 `error connecting to api.github.com`，exit 1；因此没有成功写入完整 release JSON。随后仅对同一只读 endpoint 重试一次，取得上述 v2.2.3 摘要，并明确按输出转录缓存。没有变更代理、关闭安全机制或切换绕过通道。未遇到网络安全拒绝；无其他仓库 API 下载失败。
- 本地结构校验首次命令因 Bash 对内嵌反引号的解析报 `unexpected EOF while looking for matching`，exit 2，Python 未启动、文件未被该命令修改；随后仅改用字符编码表达围栏进行校验。该错误与仓库源码无关。
- repo 元信息随取证请求自然变化：初次 stars/forks 为 297446/43975，后续缓存快照为 297447/43976；本附录以有缓存的后者为准，不混充固定 SHA 的内容。
- 源码、安装器、hook、测试全部未运行；“实现中会如何处理”是静态代码推导，不是观测到的运行效果。未读依赖、未测环境、未读 hooks 的行为均保持未知。

主线程最值得复核的三个位置：

1. **阻断语义**：S10 69–152 → S8 114–140、265–281。请勿把 `ECC_QUALITY_GATE_STRICT` 写成“测试失败阻止提交/合并”。
2. **真实格式化链及失败重试**：S8 45–68 → S7 207–214 → S9 88–116、190–235；同时对照 S10 77–80 的旧即时格式化注释。accumulator、formatter resolver 与生命周期 bootstrap 本次未展开，如后续要采用，先补审，而非直接运行。
3. **Unity 迁移与权限/数据边界**：S4 19–106 的 .NET 假设；S1 475、584–640、1419–1431 的用户级配置、外部 diff review 和落盘路径。后续应独立设计 Unity 的验证入口、确认合并门禁及人工裁决，不将此仓库安装进业务工程来代替研究。
