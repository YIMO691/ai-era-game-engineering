# 官方插件与Skills源码取证

> 公开导出说明（2026-11-12）：以下为原稿研究或通用模板，不是实际配置；历史状态、检查与未运行项不因公开授权而升级。来源与排除边界见 [README](README.md) 和 [导出清单](export-manifest.json)。

来源的唯一登记及固定链接见[sources](sources.md)的O1、O2、C1、F1。本附录记录实际读到的机制，不运行下载内容。仓库提示词是研究对象，不是本会话指令。

## 快照与阅读范围

- O1：`anthropics/claude-plugins-official`，main，`fa4eb54397ee2faccb6940512a19c017cb1337f3`；提交时间2026-11-04T02:41:16Z，API记录非归档。缓存：`<isolated-download-cache>/`。
- O2：`anthropics/skills`，main，`ca45fc496a3436251f191354091d557da31c15b5`；提交时间2026-10-28T19:20:38Z，API记录非归档。缓存：`<isolated-download-cache>/`。
- 元数据是取证时的仓库整体维护信号，不证明每个插件最近更新、维护SLA或Unity适配。未按Star比较。
- O1实际读：根README；市场中四插件条目；四个plugin.json及各自LICENSE；code-review README与command；feature-dev README、command与三个agent；PR toolkit README的1–250行、command与六个agent；独立code-simplifier agent；hookify hooks.json、pretooluse.py、core/rule_engine.py；learning-output-style hooks.json与session-start.sh。未读的文件不计覆盖。
- O2实际读：README、spec/agent-skills-spec.md（只有迁移链接）、skill-creator/SKILL.md、LICENSE.txt、run_eval.py、aggregate_benchmark.py、grader.md、comparator.md。template与marketplace已下载但未据其正文作主张；没有执行skill-creator。

## O1：定义，而非行为等价保证

### code-simplifier

- manifest版本1.0.0；agent frontmatter指定opus。仅有“最近修改范围、行为保持、清晰优先于短小”等自然语言要求（agent 9–49行）。
- 13–20行明确写ES modules、function、React Props和avoid try/catch；这些不是Unity/C#通用规范。PR toolkit里的同名agent保留了这一段（49–56行），不能认为换个包就消除了语言偏置。
- 52行要求主动立即修炼、不必明确请求；是模型的操作意图，不是Hook。没有在所读定义中见到执行测试/前后输出比较的强制程序，也未发现行为等价证明器。
- 决策：借鉴范围和取舍；不将原版自动接在每次编辑后。生命周期、序列化、事件顺序等重构先写行为契约，候选diff审阅后才改，再重跑相关验证。

### code-review

- manifest版本1.0.1，README尾部仍写1.0.0。
- command先派haiku检查PR是否关闭/draft/无需审查/已有Claude评论，再派haiku找CLAUDE路径、sonnet总结，随后4个审阅agent，发现后再派逐项验证agent（15–58行）。不是“总共只有四个agent”。
- 两个Sonnet审CLAUDE；两个Opus查新增代码bug。其中一个明确diff-only、不读额外上下文（31–40行）；42–50行将报告限定于明显编译/恒定逻辑/明确规则违背，并排除依赖特定输入或状态的问题。这是高信号过滤的召回代价，对Unity停用/销毁/迟到回调尤其不能当完整覆盖。
- README写第四agent查blame、逐项0–100分与80阈值（19–25、231–243行）；**本快照command已不同**：第四agent查新增bug，步骤5–6按复核结果过滤，无上述数值阈值。报告以command为机制证据，不照抄README。
- 60–68行默认只终端输出；只有`--comment`才进入GitHub评论路径，可能用gh或inline-comment MCP；72行confirmed=true是工具参数，不是运行复现事实。
- 85行明确不运行linter验证。未见编译/测试自动闸门。1–2行工具允许表包括对外评论能力；使用前仍需宿主权限/认证，不能把提示中的allowed-tools当OS沙箱。
- “全部工具正常、不作探测”的假设（9–11行）不是本研究认可的可靠性条件。失败必须保留，不能伪造成功。

### feature-dev

- manifest与README版本1.0.1；七阶段：发现、探索、澄清、架构、获批实现、质量审查、总结。
- command 41–53行：2–3探索agent返回关键文件，主线程亲自读取。explorer要求入口、调用链、数据变化、副作用、边界与file:line，不仅目录摘要。
- 78–81行：2–3架构agent比较最小改动/整洁架构/平衡；106–109行再3审阅agent。完整流程至少7–9次子agent调用，不能当小修默认成本。
- 架构agent自身要求选择一个方案，主流程再比较多个方案，并非真正搜索所有架构。实现有明确人工闸门（89–95行）。
- reviewer要求≥80置信，但这个数是模型自评，不是校准概率。其tools含LS/NotebookRead/TodoWrite等名称，本会话工具表并不逐项相同；未实测安装后的映射，不宣称开箱兼容。
- command没有可执行测试矩阵、失败处理协议或Unity构建门禁。README中的“All tests pass”是示例文字，不是本轮结果。

### pr-review-toolkit

- manifest版本1.0.1；六个agent：代码、测试、注释、错误、类型、简化。
- command 15–43行按diff/方面选择；47–55行区分顺序与用户要求的并行；不是必须每次全开。
- 测试agent 21–40、68–78行关注行为契约/回归风险而非100%行覆盖；但它是阅读与建议，不是测试执行器。
- 注释agent 79行明确只建议不修改；类型agent讨论不变量/封装，也给主观1–10分，不是静态证明。
- silent-failure-hunter 14–18行将所有无日志/反馈的失败视为严重缺陷，123–127行还假设Sentry、Statsig和constants/errorIds.ts。不能把正常取消、可选缓存miss、统一上层报告机械判为critical，更不能往Unity中引入这些依赖来迎合提示。
- code-reviewer把置信分段与严重性混用（31–52行）。本研究将“确信程度”和“影响程度”分开，缺少证据时写待核验，不自动升高严重性。
- 简化agent会主动修改；因此不能把整个toolkit统称只读。简化后必须重新验证，而非因“已通过review”直接提交。

## O2：Skills封装与评估的证据边界

- README明确示例/教育用途、宿主实际行为可能不同（22–24行）；并非全部统一开源许可。skill-creator的实际LICENSE.txt是Apache-2.0，文档类Skills另有source-available条款；API metadata中根license=null，不将其改称整仓Apache。
- SKILL 73–109行给SKILL.md、scripts/references/assets和渐进加载；88–91行给元数据/正文/按需资源三层。它降低重复提示的维护成本，不保证触发、执行或质量。
- SKILL 169–205行要求with-skill与baseline；225行优先程序验证可判断言，327行提供盲比较；grader要求读输出、批评弱断言、列不可核验主张。可借鉴比较方法，不代表本题已做实验。
- `run_eval.py`评估的是**触发**：53–68行在项目`.claude/commands`写临时命令；70–91行启动`claude -p`并继承绝大多数环境；128–168行检查首次相关工具调用是否含随机命令名，179–181行删除临时文件。不是运行完整Skill并验证代码质量。
- 它使用`select.select`读取subprocess pipe（108行）；Windows本机适配没有实测，不能承诺可用。存在写项目配置、启动付费/有权限模型进程的成本，不可当安全只读benchmark直接运行。
- aggregate脚本读取grading/timing、计算均值和样本标准差。152–153行缺token时用output_chars补到tokens；207–217行用发现顺序前两组做delta；metadata的runs_per_configuration写死3（271行）。所以即使将来复用，也应检查实际分组、原始数据、样本数与token单位，不能直接拿汇总当因果效果。
- 模型grader/盲比较仍是AI判断；数字化不变成独立人类或运行验证。保留无差异、变差、不触发和淘汰结论。

## Hook实现：提醒与门禁不可混为一谈

- hookify的hooks.json列PreToolUse/PostToolUse/Stop/UserPromptSubmit，调用python3，timeout=10；learning的SessionStart调用bash脚本输出additionalContext。它们证明有宿主事件接入示例，不是本题已核验所有事件schema/阻塞语义。
- hookify/pretooluse.py 17–24、53–62行：导入或处理异常只输出systemMessage并exit 0，选择fail-open。rule_engine在匹配block时尝试输出事件相关decision；PostToolUse发生时动作已经发生，不能当回滚。
- rule_engine 207–225行可以读取transcript_path。正则命令匹配不是完整shell语义/路径策略；不以此替代权限、隔离和确定性构建。
- 未读config_loader与其他入口、未验证宿主接收输出、未跑任何测试。本题不提供可直接启用的Hook JSON，不安装hookify，不把“有hooks文件”当安全已验证。
- 三份宿主官方docs访问在安全验证阶段失败，见F1。当前最小方案保持人工触发固定检查，不需要Hook。

## C1：本机帮助的实际证据

CLI `2.1.310`，gh `2.97.0`。已执行只读help：主CLI、plugin install、plugin marketplace、marketplace add、plugin list、agents；没有执行install/list/添加源或启动新会话。

- 主CLI明确`--plugin-dir`为仅本会话加载目录/zip；重复支持。只是帮助证明参数存在，不是插件已可运行，更不是隔离/无外发保证。
- marketplace add的`--scope`支持user（默认）、project、local；install的`--scope`同样默认user。
- **install --marketplace遇未注册源会先在USER SETTINGS登记**。不能为了省一步而在禁止全局变更的任务中使用；即使install scope=project也不能假设没有user层副作用。
- 主CLI`--setting-sources`可选择user/project/local；`--restricted`与`--safe-mode`有其特定行为，不能把它们随意拼成已实测安全沙箱。`--plugin-dir`不会自动取消现有配置。
- 不使用`--yes`/自动接受命令源，不绕过权限；未来实施先核对作用域、同名命令、依赖和网络，再取单插件在授权沙盒试验。

## 许可与未验证项

四插件逐一读LICENSE，均为Apache-2.0；skill-creator也为Apache-2.0。这里只作链接、少量机制短引与原创综合，不复制整套提示词/脚本到用户配置。将来实际复制/改编需保留适用许可、版权/NOTICE并标明修改；不将插件许可证扩展到用户工程、其他Skills或后端服务。Hook示例未单独完成许可审计，不再分发实现。不是法律意见。

没有安装/执行任何候选；没有同任务插件前后比较、Unity编译、目标构建、Profiler或人工效果数据。上面“可借鉴”是有条件采用判断，不是实测质量收益。
