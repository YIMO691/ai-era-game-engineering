# OpenHands 当前架构与工程闭环取证附录

> 公开导出说明（2026-11-12）：以下为原稿研究或通用模板，不是实际配置；历史状态、检查与未运行项不因公开授权而升级。来源与排除边界见 [README](README.md) 和 [导出清单](export-manifest.json)。

## 取证口径与版本固定

研究问题：当前 OpenHands 的“理解仓库→执行→测试反馈→审查/PR→失败恢复”究竟由哪些组件承担，哪些闭环可借鉴、哪些保证没有证据。范围止于 canonical 主仓库和其直接引用的一个官方 SDK；静态路径及关键边界得到限定证据后停止，不扩散到第三仓或运行验证。

来源交接 ID：`ER-20261105-openhands-01`（Canvas 固定源码/文档），`ER-20261105-openhands-02`（SDK 固定源码/文档）。两者 `read_status=read`、`experiment_status=not-run`；各主张在下文逐项标明事实、自述、推论或未取得。同一仓库的多个文件不是多个独立研究确认。供主线程按唯一来源登记规则整合到 `sources.md`；本附录任务不修改来源总账、topic 状态或检查点。

本次为 **2026-11-05 的独立静态只读取证**。只用 `gh api` GET 获取仓库元数据、commit、完整递归 tree 和按 SHA 固定的文件；未调用 Skill、未再委派、未安装依赖、未运行下载代码、未启用任何服务、未创建 PR/评论或修改远端。Python 仅以 `python -I -c` 在可信工作目录用标准库读取缓存 JSON/目录，下载目录未作为解释器工作目录或脚本目录。两仓库分别使用新建空临时目录，未混放。没有网络安全拒绝或绕过；主仓库 `pyproject.toml` 请求返回普通 404，随后按 tree 确认为当前 npm 项目，404 响应不作依赖证据。

| 项目 | 固定结果 |
|---|---|
| 用户给定入口 | `https://github.com/All-Hands-AI/OpenHands` |
| 当前 canonical | `OpenHands/OpenHands`，`https://github.com/OpenHands/OpenHands`；旧名称 API 请求最终返回该 `full_name`/`html_url`，响应最终为 HTTP 200。确认了旧入口解析到新仓库，**没有另外保存初始 301/302 链，不声称测得具体跳转状态码**。 |
| 主仓库 default branch | `main` |
| 主仓库完整 SHA | [`6d2d9df4af1337abf4ed967a7b396f46fed7559c`](https://github.com/OpenHands/OpenHands/commit/6d2d9df4af1337abf4ed967a7b396f46fed7559c) |
| 主仓库 author / committer 日期 | 均为 `2026-11-05T03:15:24Z` |
| 定点跟踪的唯一第二仓库 | `OpenHands/software-agent-sdk`，由主仓库 README 的 Agent Server/仓库边界直接引用；没有继续跟踪 extensions、automation、文档站或 CLI 仓库。 |
| SDK default branch | `main` |
| SDK 完整 SHA | [`28f4dfeeec4473060873185d301495d1c3743947`](https://github.com/OpenHands/software-agent-sdk/commit/28f4dfeeec4473060873185d301495d1c3743947) |
| SDK author / committer 日期 | 均为 `2026-11-05T05:46:25Z` |
| 时间依据 | 旧入口 API 响应 `Date: Thu, 05 Nov 2026 08:35:18 GMT`，见本地 `canonical-response.txt`；commit 时间不是发布日期。 |

**版本边界很重要。** 这两个 SHA 是分别固定的当日 default-branch 快照，不是声称生产环境已部署这一对 commit。Canvas 配置固定 Agent Server `1.59.0`，SDK 各包 manifest 也是 `1.59.0`；版本号一致不等于证明发布包内容和这两个 HEAD 完全相同。[C-defaults](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/config/defaults.json#L1-L50)[S-sdk-package](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/pyproject.toml#L1-L54)

### 当前维护、许可与活跃度

- **事实**：两个 public 仓库的 GitHub owner 均为 `OpenHands` organization，`archived=false`；元数据分别记录 `pushed_at=2026-11-05T04:18:46Z`、`2026-11-05T07:18:03Z`。固定主分支最近三条 commit 缓存也显示主仓库当天三条、SDK 11 月 4—5 日三条提交。这支持“当前仍在开发”，不等于维护 SLA 或质量保证。
- **事实**：主仓库 MIT，版权行为 `2025 OpenHands contributors`；SDK MIT，版权行为 `2026 OpenHands contributors`。需要保留许可/版权通知，均含无担保条款。未据此推断模型服务、镜像和全部传递依赖也采用 MIT。[C-license](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/LICENSE#L1-L22)[S-license](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/LICENSE#L1-L21)
- **未取得**：在两份完整、`truncated=false` 的 tree 中按 `CODEOWNERS/governance/maintainer` 文件名搜索未命中。只能确认组织所有权、近期贡献者和提交活动，不能把最新 commit 作者当作所有模块的正式维护负责人。近期作者 login 保存在 `recent-commits.json`；没有请求有写权限的管理 API。

## 实际读取清单

下面是 **9 个当前关键实现/测试/工作流**。不是全仓审计；“全文”表示实际读取文件全文，不表示运行。长文件先进行全文件符号/关键词搜索，再读取表中明确范围。

| 编号 | 固定文件 | 实际读取范围及作用 |
|---|---|---|
| K1 | [Canvas `.github/workflows/ci.yml`](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/.github/workflows/ci.yml#L1-L503) | L1–503 全文；PR/push CI、live E2E、密钥隔离、精确 SHA、报告和失败传播。 |
| K2 | [SDK `openhands-sdk/openhands/sdk/agent/agent.py`](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/agent/agent.py#L231-L1611) | L231–421、479–930、1164–1369、1377–1611；action batch、恢复初始化、LLM step、确认、参数校验、critic 调用点及 observation。未完整阅读 async 重复实现、父类和 mixin。 |
| K3 | [SDK `openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py`](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L232-L3314) | L232–688、744–832、1008–1141、1259–1406、1628–1721、1943–2237、2762–2923、3166–3314；创建/恢复入口、先持久化再发布、上下文、同步 run、预算、暂停/中断、重执行警告。未完整阅读 async run、state/EventLog 底层及所有插件合并分支。 |
| K4 | [SDK `examples/03_github_workflows/01_basic_action/agent_script.py`](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/01_basic_action/agent_script.py#L1-L169) | L1–169 全文；prompt→LLM→默认 agent→当前工作目录→conversation.run。 |
| K5 | [SDK `examples/03_github_workflows/01_basic_action/workflow.yml`](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/01_basic_action/workflow.yml#L1-L124) | L1–124 全文；权限、依赖安装、动态下载脚本、配置检查及日志 artifact。 |
| K6 | [SDK `examples/03_github_workflows/02_pr_review/workflow.yml`](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/02_pr_review/workflow.yml#L1-L45) | L1–45 全文；独立 PR review 的调用入口，而非 reviewer 内部实现。 |
| K7 | [SDK `tests/sdk/agent/test_tool_call_recovery.py`](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/tests/sdk/agent/test_tool_call_recovery.py#L1-L293) | L1–293 全文；mock LLM 下的参数解析及空回复纠偏。 |
| K8 | [SDK `tests/cross/test_pr_review_trace.py`](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/tests/cross/test_pr_review_trace.py#L1-L30) | L1–30 全文；Laminar span context 的 UUID JSON 序列化，**不是 review 正确性测试**。 |
| K9 | [SDK `openhands-tools/openhands/tools/terminal/definition.py`](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-tools/openhands/tools/terminal/definition.py#L1-L362) | L1–362 全文；命令/输入/timeout/reset schema、输出/退出码到 LLM、资源声明及非幂等标注。没有继续读底层 terminal executor。 |

另已实际全文读取的基线/边界文档与依赖 manifest：

- Canvas：[README L1–185](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/README.md#L1-L185)、[LICENSE L1–22](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/LICENSE#L1-L22)、[package.json L1–265](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/package.json#L1-L265)、[config/defaults.json L1–50](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/config/defaults.json#L1-L50)、[docs/architecture.md L1–82](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/docs/architecture.md#L1-L82)、[docs/SELF_HOSTING.md L1–287](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/docs/SELF_HOSTING.md#L1-L287)、[AGENTS.md L1–125](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/AGENTS.md#L1-L125)。远端 AGENTS 作为被研究的仓库政策文本，不作为本次执行指令。
- SDK：[README L1–203](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/README.md#L1-L203)、[LICENSE L1–21](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/LICENSE#L1-L21)、[根 pyproject.toml L1–139](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/pyproject.toml#L1-L139)、[SDK 包 manifest L1–54](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/pyproject.toml#L1-L54)、[Agent Server manifest L1–59](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-agent-server/pyproject.toml#L1-L59)、[tools manifest L1–45](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-tools/pyproject.toml#L1-L45)、[workspace manifest L1–38](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-workspace/pyproject.toml#L1-L38)、[PR review 示例 README L1–245](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/02_pr_review/README.md#L1-L245)。
- API 基线：两仓库 repository JSON、固定 commit JSON、完整 recursive tree、固定 SHA 起算最近三条 commit。未下载整个源码归档，没有把 tree 中出现的文件说成已经审阅其内容。未获取 Actions 实际运行结果或评测数据。

## 架构事实：不要把旧版单仓实现套到当前 HEAD

**事实**：主仓库 README 当前标题是 **Agent Canvas**，定位为 coding-agent/automation 的控制中心；主仓库拥有 UI、backend selection、local-stack orchestration，不拥有 agent 动作执行。SDK 拥有 Python agent、tools、conversations、workspaces、events、Agent Server 的 REST/WebSocket API；automation 拥有调度、webhook、run history 和 dispatch。[C-boundaries](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/README.md#L151-L177)[C-arch](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/docs/architecture.md#L1-L82)[S-boundaries](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/README.md#L83-L87)

**事实**：两份 README 对 TypeScript client 的边界表述存在细微不同：Canvas README 把 `OpenHands/typescript-client` 列为 client 仓库，SDK README 说本仓 `clients/typescript/` 拥有 canonical client。此次未跟踪第三仓，不替维护者消除这处文档差异；能确认 Canvas npm 依赖 `@openhands/typescript-client: 1.59.0`，核心 Python execution 不在 Canvas 中。[C-boundaries](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/README.md#L151-L177)[S-boundaries](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/README.md#L83-L87)[C-package](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/package.json#L1-L265)

可据当前证据复原的主路径为：

1. Canvas UI/本地 stack launcher → 配置的 Agent Server API。
2. SDK `LocalConversation` → 延迟加载项目技能、memory、plugins/MCP/hooks、文件式 agent 定义 → agent 初始化。
3. `Agent.step` 从当前事件视图构造 LLM 消息 → 模型生成 tool calls → schema 校验/确认策略 → tool executor → observation/error 事件 → 下一步。
4. GitHub Actions 示例另外提供 task runner 与 PR review 入口；调度/webhook 产品实现不在本次允许跟踪的两个仓库内。

这不是依据旧版 `CodeActAgent/AgentController/Resolver` 名称拼装的 V0 图。本次不声称做了 V0→V1 的历史迁移审计，也不把曾经存在的旧目录当作当前实现证据。

## 仓库理解：上下文装配有证据，“自动理解全仓”没有证据

- **事实**：`_ensure_agent_ready` 按插件→文件 agent 注册→初始化→LLM registry 的次序延迟初始化；项目技能由 `workspace.working_dir` 加载，`load_project_skills` 为条件，同名项目技能优先。memory 也有 `load_memory` 条件、加载失败继续运行。这是可配置上下文装配，不是已经完成静态全仓分析。[S-init](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L1628-L1717)[S-project-context](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L1259-L1405)
- **事实**：用户消息可获得知识技能后缀；文件 observation 可依据实际触及的 workspace 内路径注入匹配规则，利用已激活集合去重。路径规则过滤不是文件系统访问 sandbox——相应方法只是决定何时加入提示文本。[S-path-rules](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L611-L687)[S-send-run](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L1943-L2235)
- **事实**：system prompt 分静态/动态内容，动态上下文从 secret registry 取得 names/descriptions 等信息；`Agent.step` 使用 `state.view`、可选 condenser 准备模型消息。[S-agent-init-step](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/agent/agent.py#L500-L930)
- **自述**：SDK README 支持按需开启公共技能。此次没有调用这些技能，也没有跟踪其外部仓库。[S-readme](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/README.md#L1-L203)
- **未取得**：没有完成 AGENTS 自动发现底层、仓库索引器、符号图/语义搜索完整路径的取证；不能据本次样本宣称“内建完整仓库理解”“默认会正确加载所有规则”或证明 C#/Unity 项目理解质量。代码/文档/插件均可成为模型输入，提示内容来源本身不构成可信授权。

## 任务执行与测试反馈：通用动作闭环，不是自动验收证明

**事实**：`Agent._step` 优先处理当前分支的 unmatched actions；否则准备上下文并调用 LLM。`_get_action_event` 解析/规范化 tool calls，使用 action schema 校验，产生 `ActionEvent`；校验异常转为结构化错误以供纠正。批处理分开执行和按原 action 次序发事件，finish action 会截断其后的调用。[S-agent-init-step](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/agent/agent.py#L500-L930)[S-agent-validation](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/agent/agent.py#L1377-L1544)[S-batch](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/agent/agent.py#L231-L414)

**事实**：工具调用返回 `ObservationEvent`，其中以 `action_id/tool_call_id` 关联动作。执行中的 `ValueError` 被转为 `AgentErrorEvent`；其他异常可由 conversation run 的异常处理置 `ERROR` 并抛出带 conversation ID/persistence 位置的 `ConversationRunError`。[S-agent-execute](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/agent/agent.py#L1546-L1608)[S-send-run](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L1943-L2235)

**事实**：terminal observation 含文本、工作目录、解释器信息及退出码；输出可截断并保存完整输出位置。`exit_code=-1` 表示 soft timeout/仍在运行，不等于失败。reset 的 schema 明确会丢失终端环境变量/会话状态。[S-terminal-feedback](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-tools/openhands/tools/terminal/definition.py#L86-L201)

**推论**：仓库的真实“测试→修改→重试”可通过 agent 选择测试命令、terminal 返回失败输出、下一轮读取 observation 再修改来实现；此处没有发现专属于 Unity 的测试执行器，也没有证据证明默认 agent 每次都必须先运行测试、必须测试通过才 finish。工具反馈可支撑闭环，不能替代用户定义的验收条件。

**事实：项目自身 CI 是另一层验证，不应与 agent 自检混称。** Canvas CI 在 Ubuntu 运行 lint、unit/component tests、app/library build、package dry-run；Windows 矩阵 `full_checks=false`，只执行其中适用的 build，不是完整测试对称覆盖。普通 PR CI 默认只有 `contents: read`。[C-ci-tests](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/.github/workflows/ci.yml#L24-L95)

**事实**：live E2E 只在 main push 或手动 dispatch 下运行，fork PR 显式跳过；缺 LLM key 为 skipped。手动 PR 测试获取并检出精确 head SHA，校验实际 SHA；测试步骤先保存 exit code，报告/PR comment/artifact 完成后再以该 exit code 失败。因此“日志产生”“报告已发布”“E2E skipped”都不能当作成功验证。[C-ci-live-context](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/.github/workflows/ci.yml#L97-L195)[C-ci-live-result](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/.github/workflows/ci.yml#L276-L503)

### 一个值得单独保留的成功判定陷阱

**事实**：task runner 示例在 `conversation.run()` 返回后直接写 `Task completed successfully`，没有检查 `state.execution_status`；而当前 `LocalConversation.run` 的契约明确说明 iteration limit/stuck 可以返回 `ERROR/STUCK` 而不抛异常（remote run 契约不同）。[S-task-script](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/01_basic_action/agent_script.py#L143-L165)[S-send-run](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L1943-L2235)

**推论**：若直接把这个示例日志作为上层自动化成功信号，会把某些未完成任务误判成功。应读取终态、测试命令结果和必要 artifact，而不是匹配成功字符串。这里是静态交叉阅读得到的具体风险，**没有运行复现**，也没有声称所有 task runner 部署都使用该示例。

## 独立审查与 GitHub PR：入口已取得，外部 reviewer 实现未取得

### 能确认的 review 机制

- **事实**：SDK PR review 示例是独立 GitHub job，通过 PR `labeled/review_requested` 事件触发，只在 `review-this` 或指定 reviewer 条件满足时运行，调用 `OpenHands/extensions/plugins/pr-review@main`。传入 LLM key、GitHub token，可选 Laminar key。示例位于 `examples/`，**不是据此证明该 workflow 已在目标用户仓库启用**。[S-review-workflow](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/02_pr_review/workflow.yml#L17-L44)
- **事实**：该目录 README 明说实际 review scripts 已移至 extensions。依本次仅允许定点跟踪一个 SDK 仓库的边界，没有继续下载 extensions。[S-review-readme](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/02_pr_review/README.md#L1-L245)
- **自述、未核实实现**：review README 描述逐行评论、历史 review/thread 感知、diff 截断和补读、A/B 模型、合并后的延迟评估。这些是当前文档描述，不是本次代码审阅或实测证明。[S-review-readme](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/02_pr_review/README.md#L1-L245)
- **未取得**：实际 reviewer 的独立 conversation/进程如何创建、是否与实施者隔离上下文与写权限、是否能接触 PR 机密、如何提交 review verdict、如何去重评论、如何验证发现、是否强制阻止合并。不能把这个外部入口直接写成“已经审计过的独立审查架构”。
- **事实**：`agent.py` 有可配置 critic 的调用点和 iterative-refinement 的 finish 后续消息机制；此次未读其 mixin 实现。这些接口不等于单独、独立的 PR reviewer。[S-agent-validation](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/agent/agent.py#L1377-L1544)[S-batch](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/agent/agent.py#L231-L414)
- **事实/政策文本**：Canvas `AGENTS.md` 要求实施 agent 不改 verification skill 的期望结果，验证规范维护另开 PR/agent context。这是明确的独立验证治理意图，不是运行时隔离或权限强制证明。[C-verification-policy](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/AGENTS.md#L69-L84)
- **事实**：`test_pr_review_trace.py` 只证明用 JSON mode 可以序列化 UUID span context；既不证明 reviewer 的发现正确，也不证明其独立性。[K8](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/tests/cross/test_pr_review_trace.py#L1-L30)

### GitHub 权限、创建 PR 与供应链边界

| 入口 | 当前文件明确配置 | 不能据此推断 |
|---|---|---|
| basic task workflow | `contents/pull-requests/issues: write`；Ubuntu runner；checkout；安装 Python/uv/SDK；LLM key 交给任务进程；总是上传日志。 | `agent_script.py` 没有确定性的建分支/commit/push/create-PR API 流程，也没有固定 GitHub token 注入给 `gh` 的步骤；“prompt 要求建 PR”不等于已证明能完成。checkout credentials 等仍需按部署具体审计。 |
| PR review 示例 | `contents: read`、`pull-requests/issues: write`，GitHub token 显式交给外部 action；LLM key 必需。 | 外部 action 的容器、checkout 策略、fork token/secret 实际可用性和最小权限未取得；不能推断 fork PR 必然可用或永不泄密。 |
| Canvas live E2E | 另一个 job 提升为 `contents/issues/pull-requests: write`；fork 跳过；发布报告和 `.pr` 媒体到 PR 分支；token 可使用 bot PAT 或内置 token。 | 这是项目 QA 的 comment/artifact 自动化，不是 agent 通用 PR 创建系统；没有创建/审查 PR 的闭环质量证明。 |

依据分别见 [K5](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/01_basic_action/workflow.yml#L1-L124)[S-review-workflow](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/02_pr_review/workflow.yml#L17-L44)[C-ci-live-context](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/.github/workflows/ci.yml#L97-L195)[C-ci-artifact-push](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/.github/workflows/ci.yml#L321-L430)。basic workflow 的默认 `PROMPT_STRING/PROMPT_LOCATION` 都为空，会先被配置检查拒绝；不能说复制即用。[K5](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/01_basic_action/workflow.yml#L1-L124)

**事实**：basic workflow 从可变 `main` 的旧 `OpenHands/agent-sdk` URL 安装包、动态下载 Python 脚本；本次没有解析这些旧 SDK URL 的别名关系。PR review action 也引用可变 `@main`，示例中的常见 Actions 仅按 tag 固定。**推论**：这些模板不是可复现、按完整 commit 固定的安全交付方案；实际采用前应固定可信完整 SHA、审查权限与 secret 暴露、禁用不需要的写权限。此次只阅读，未执行其任何下载/安装命令。[K5](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/01_basic_action/workflow.yml#L1-L124)[K6](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/02_pr_review/workflow.yml#L1-L45)

## 执行失败恢复：事件恢复不能替代外部世界恢复

### 已取得的持久化/会话恢复证据

- **事实**：constructor 提供 `conversation_id/persistence_dir/file_store`；调用 `ConversationState.create` 作为 create-or-resume 边界，`agent=None` 时采用持久化的 agent，并可重新注册持久化 client tool specs。事件默认 callback 调用 `append_event`，在调用用户 callback/pubsub 前执行；持久化失败会阻止后续 callback。此处保证的是代码路径的发布顺序，不是本次证明了全部磁盘 crash consistency/fsync 语义。[S-conversation-persist](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L232-L594)
- **事实**：已有 system prompt 时初始化跳过；缺失 prompt 文件而有可恢复父 ID 时可按原 ID 重建根，并恢复原 HEAD/view。`navigate_to` 改变活动事件分支及 view，保留磁盘上旧分支。[S-agent-init-step](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/agent/agent.py#L500-L930)[S-navigation](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L1008-L1031)
- **未取得**：没有深入阅读 `ConversationState`/`EventLog` 底层、截断写入恢复和跨版本迁移测试；不能声称已验证任意崩溃点完整、无损重放。这里确认的是持久化与恢复入口/局部处理路径。

### 已取得的执行纠偏与停止机制

- **事实**：malformed function call 可形成纠偏消息；上下文超限/结构无效历史在配置了能处理请求的 condenser 时形成 condensation request，历史异常还先 rebuild view，否则上抛。不是任何错误都无限重试。[S-agent-init-step](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/agent/agent.py#L500-L930)
- **事实**：读取的恢复测试 mock 了 LLM，覆盖有效 JSON 换行、非法控制字符 fallback、reasoning-only/empty 回复插入纠偏消息，正常内容不插入。它们不是实际供应商端到端恢复测试，且本次未运行。[K7](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/tests/sdk/agent/test_tool_call_recovery.py#L1-L293)
- **事实**：stuck detector 可先 nudge，再设 `STUCK`；默认单次 run 最多 500 iterations，预算配置和异常产生结构化状态。pause 在 step 边界生效；interrupt 在 async 路径取消 task/token，同步路径退化为 pause。orphan action 可以补 synthetic error 来保持模型消息配对。[S-limits](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L744-L830)[S-send-run](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L1943-L2235)[S-interrupt](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L2794-L2922)

### 明确不能混淆的恢复边界

**事实**：terminal tool 自己声明 `readOnlyHint=False`、`destructiveHint=True`、`idempotentHint=False`、`openWorldHint=True`。`LocalConversation.rerun_actions` 的文档明确警告文件、terminal、API、browser 操作可能非幂等，通常应先重置 workspace；实现会再次调用原 tool，不会自动补偿外部副作用。[S-terminal-nonidempotent](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-tools/openhands/tools/terminal/definition.py#L268-L358)[S-rerun](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L3166-L3312)

**推论，且由调用次序支持**：工具发生外部效果之后、observation 持久化之前仍存在不确定窗口。恢复路径从活动分支识别 unmatched actions 并执行，不能仅由“缺少 observation”判断外部调用从未发生；重执行可能重复 push、建 PR、发评论、部署或其他 API 副作用。[S-agent-init-step](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/agent/agent.py#L500-L930)[S-agent-execute](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/agent/agent.py#L1546-L1608)[S-batch](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/agent/agent.py#L231-L414)

**未取得**：没有发现并验证覆盖所有外部操作的幂等键、事务性 outbox、exactly-once 执行、跨系统补偿/回滚协议。`navigate_to` 只改会话 HEAD，不是 git/workspace/远端 GitHub 回滚；synthetic interrupted error 只修复消息结构，也不证明动作没发生。Canvas QA push 的三次重试/rebase及祖先检查是特定 artifact 发布处理，不应泛化为 SDK 的副作用恢复。[S-navigation](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L1008-L1031)[S-interrupt](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L2794-L2922)[C-ci-artifact-push](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/.github/workflows/ci.yml#L321-L430)

可借鉴的是将“会话恢复”与“操作确认/去重/补偿”设计为两个独立层：重试前先查询外部操作结果，使用稳定 operation ID/PR 标识，保留 unknown 状态并允许人工确认；这是本附录建议，**不是声称仓库已全部实现**。

## 依赖、运行权限、网络、密钥与成本

### 当前依赖形态

- **事实**：Canvas `@openhands/agent-canvas 1.35.0`，Node `>=24`，npm `11.12.1`；React/React Router、Vite、Zustand、TanStack Query、TypeScript client 等直依赖为精确版本；测试含 Vitest、Playwright、Stryker。读取了 manifest，**没有审计 package-lock 全部内容或安装结果**。[C-package](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/package.json#L1-L265)
- **事实**：stack 配置固定 Agent Server `1.59.0`、automation `1.26.1`，启动所请求 Python 范围 `>=3.12,<3.15`。automation 的配置版本不代表此次审阅了该包代码。[C-defaults](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/config/defaults.json#L1-L50)
- **事实**：SDK 为四包 uv workspace，各包版本 `1.59.0`、Python `>=3.12`；核心依赖包括 LiteLLM、Pydantic、httpx、FastMCP、ACP、tenacity、Laminar；tools 包含 browser-use/libtmux/psutil；Agent Server 包含 FastAPI/Uvicorn、SQLAlchemy/aiosqlite、Docker。组件包依赖多为范围，不是所有依赖精确锁定。[S-root-package](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/pyproject.toml#L1-L139)[S-sdk-package](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/pyproject.toml#L1-L54)[S-server-package](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-agent-server/pyproject.toml#L1-L59)[S-tools-package](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-tools/pyproject.toml#L1-L45)[S-workspace-package](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-workspace/pyproject.toml#L1-L38)
- **事实**：根配置有七天 release-age guardrail、少数具名例外和 LiteLLM 精确 constraint；根 pytest 默认排除 stress/acp_live/docker_live。**推论**：不能把“默认 pytest”直接写成覆盖真实 ACP/Docker/压力场景，也不能把仓库 resolver 配置当作所有下游 pip 安装都会强制执行的防线。[S-root-package](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/pyproject.toml#L1-L139)

### 安全边界必须按运行模式分别评估

| 模式/边界 | 已取得证据 | 采用时含义 |
|---|---|---|
| 本机无 sandbox | README 明确 agent-server 对本机文件系统有完整访问；self-hosting 同时警告可执行 shell、访问网络。 | workspace 路径不是强制隔离。任务脚本/测试/仓库内容都可能影响宿主；不应暴露生产凭据或不相关目录。 |
| 单 Docker sandbox | quickstart 发布宿主 loopback 端口，挂载 `.openhands` 状态和整个 `PROJECTS_PATH` 到 `/projects`。 | 容器仍可读写这些挂载；不是每个项目互相隔离。没有从示例取得默认 deny-all egress、容器权限/capabilities 的完整实现。 |
| 每会话 Docker | README 声明每次会话独立容器，挂载 workspace 和 persisted state；同一宿主 workspace 仍共享文件；外层 Canvas/automation 不因此移入 sandbox。 | 会话历史/文件能跨容器替换保留，不等于副作用可回滚；并行改同一路径需独立目录/worktree。需能使用 Docker 的宿主权限，未审计 daemon/socket 隔离。 |
| 网络入口与 session key | npm/source 默认 loopback；公开监听不注入 session key；Docker quickstart显式允许注入但只发布 loopback。self-hosting 要求 API key、TLS/防火墙。 | bind、认证和网络策略须共同成立。此次未启动服务，没有验证实际监听、鉴权拒绝或网络隔离。 |
| 浏览器同源 | self-hosting 明示内置 editor 与 Canvas 同源，脚本可访问保存多个 backend session key 的 localStorage。 | 路径前缀只做路由、不做安全隔离；editor 扩展/资产应视作 session key 的信任边界。 |
| 确认与安全分析 | agent 代码根据 configured analyzer/confirmation policy 分析动作并进入 `WAITING_FOR_CONFIRMATION`；没有 analyzer 返回 UNKNOWN。`execute_tool` 明说绕过 loop 的确认与分析。 | 提示里有 risk 字段不等于强制启用了 analyzer，更不等于容器/网络隔离。直接执行 API 的调用者必须自负防护。此次未读默认 state policy，故不声称默认逐动作人工批准。 |

依据：[C-readme-runtime](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/README.md#L62-L149)[C-selfhost](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/docs/SELF_HOSTING.md#L1-L287)[S-confirmation](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/agent/agent.py#L1164-L1262)[S-rerun](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L3166-L3312)。没有运行容器，也没有把“可选 sandbox”写成所有执行都已 sandbox。

### 密钥、数据与费用

- **事实**：basic task 使用 runner 环境变量 `LLM_API_KEY`；review action 接收 LLM/GitHub keys，可选 Laminar key；SDK conversation 有 secret registry、可选 cipher，constructor 文档明确未传 cipher 时序列化的 secret 会 redacted/lost，传 cipher 才支持加密保存/恢复。secret 名称/描述可以进入动态上下文。[K4](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/01_basic_action/agent_script.py#L1-L169)[K5](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/01_basic_action/workflow.yml#L1-L124)[K6](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/02_pr_review/workflow.yml#L1-L45)[S-conversation-persist](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L232-L594)[S-agent-init-step](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/agent/agent.py#L500-L930)
- **推论**：将 key 包装为 `SecretStr`、日志遮罩或状态加密，不等于禁止 terminal/subprocess/插件读取进程环境，也不等于代码/测试输出不会发送给配置的模型服务。模型 endpoint、MCP、插件、observability 和 CI artifact 都需单独界定允许的数据。此次没有证明完整 secrets sandbox，也没有验证 cipher 密钥管理。
- **事实**：预算默认 `None` 表示无上限；预算函数看 agent/condenser 等 LLM 的 combined accumulated cost，同步 loop 在完成 step 后检查。迭代上限不是金额上限。[S-limits](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L744-L830)[S-send-run](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L1943-L2235)
- **推论**：这不是供应商侧硬性预付费封顶，单 step/并行调用仍可能越过阈值；runner、容器、云 workspace、网络和 observability 费用不应假定都被该 LLM cap 覆盖。实际价格/总成本本次未测。额外 review、condensation、重试和 live E2E 都可能增加模型调用成本。

## 原创结论与可迁移闭环

1. **可借鉴的闭环**：明确 workspace/权限 → 装配可追踪上下文 → 用 action/observation 关联执行 → 测试输出返回下一轮 → 验证终态/退出码 → 固定测试 SHA → 独立 review 与人工合并门禁 → 失败时保留证据和 unknown side-effect 状态。它是组合式工程流程，不是单一 agent 的自动正确性保证。
2. **优先借鉴的具体实践**：发布前先持久化事件；测试报告保留 tested SHA 与最后失败 exit code；fork PR 不暴露 live secret；区分 skipped/failed/passed；验证规范与产品修改分离；持久化恢复与外部副作用去重分离。前五项都有上述文件或政策证据，最后一项是从恢复边界提出的建议。
3. **不要直接照搬的部分**：可变 `@main` 的远程脚本/Action、广泛 GitHub 写权限、把 `run()` 返回当成功、把共享挂载当项目隔离、把 reviewer 入口或 critic 当已验证独立审查、把事件 HEAD 回退当环境回滚。
4. **适用边界**：这里只研究闭环，**不预设替换 Claude Code**，不宣称 Unity/C# 已证实可用。Unity Editor/batchmode、EditMode/PlayMode、资源导入、`.meta`/序列化、平台构建与许可证、图形环境及测试时长成本均未验证；未来评估需另设项目内验收和隔离实验，不能由 Python/React 示例或 README benchmark 推得。

## 主线程定点复核与本地缓存

先看当前边界 [C-boundaries](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/README.md#L151-L177)，再复核四个高价值点：

1. **run 返回不代表成功**：[K4 L161–165](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/01_basic_action/agent_script.py#L143-L165) 对照 [K3 L2039–2057、2161–2191](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L1943-L2235)。
2. **持久化≠幂等恢复**：[K3 L456–485](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L232-L594)、[K2 L747–755](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/agent/agent.py#L500-L930)、[K3 L3166–3188](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py#L3166-L3312)。
3. **独立 review 实现缺口**：[K6 L35–44](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/02_pr_review/workflow.yml#L17-L44) 与 [review README L3–5](https://github.com/OpenHands/software-agent-sdk/blob/28f4dfeeec4473060873185d301495d1c3743947/examples/03_github_workflows/02_pr_review/README.md#L1-L245)；禁止用未跟踪的 extensions 内容填补。
4. **真实 CI 权限/验证结果**：[K1 L97–195](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/.github/workflows/ci.yml#L97-L195)、[K1 L276–290、443–503](https://github.com/OpenHands/OpenHands/blob/6d2d9df4af1337abf4ed967a7b396f46fed7559c/.github/workflows/ci.yml#L276-L503)；普通 PR CI 与 live job 分开。

缓存是按 SHA 获取的选定文件与 API 响应，不是安装目录：

- Canvas：`<isolated-download-cache>/`
- SDK：`<isolated-download-cache>/`

两目录内 `repository.json`、`commit.json`、`tree.json`、`recent-commits.json` 可重查版本与活动；Canvas 另有 `canonical-response.txt`。文件名将仓内 `/` 替换为 `_`（README、LICENSE 和根 manifest 保留原名）；例如 SDK `openhands-sdk_openhands_sdk_conversation_impl_local_conversation.py`。Canvas `pyproject.toml` 是先前 404 响应，勿当源码。所有固定 GitHub 链接如下；缓存目录可能被系统清理，长期复核以 SHA 链接为准。
