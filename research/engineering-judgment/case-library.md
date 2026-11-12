---
title: 工程判断案例库
date: 2026-11-06
version: "0.9"
tags: [engineering-judgment, source-case-study, unity]
status: draft
---

# 工程判断案例库

> **公开导出注（2026-11-12）**：以下研究状态、访问和审查记录属于原 2026-11-06 草案；本次只作本地白名单导出。公开授权不等于人工研究审核、实验通过或生产验收。私有状态描述是历史记录；模板及操作文本仅作资料，不在本次执行。转换与排除见 [导出清单](export-manifest.json)。


导航：[从工程思维到工程判断力_深化研究报告](engineering-judgment-report.md) · [成熟项目源码阅读与设计还原手册](source-reading-handbook.md) · [工程判断模型与决策手册](decision-handbook.md) · [sources](sources.md)

> **warning** — 不能把六个真实项目误报为六个已完成案例
> **C1、C2 已由研究子任务读取固定源码、相关测试与公开讨论，可作静态源码案例；没有编译或运行。C3–C6 只完成真实项目检索与待核案例分析，必要正文/源码仍不可得，不满足完整一手案例验收。**本库不以虚构结果填满这些缺口。所有练习是题设，建议 oracle 是静态预期/验证设计，不是实际通过记录。

## 案例索引与证据等级

| 案例 | 用户要求中的类别 | 本轮证据 | 仍缺什么 |
|---|---|---|---|
| C1 UniTask | Unity/C# 1 | 2.5.10 固定 SHA，关键源码/测试、README、Issue 已读 | 运行回收/存活实验、归池条件的作者直接解释 |
| C2 NGO | Unity/C# 2 | 1.9.1 固定 SHA，生命周期/handler/消息/样例/测试、历史 Issue/PR 已读 | 运行及复杂场景、历史修复独立回归 |
| C3 SQLite | 基础设施 1 | 官方测试/WAL 资料的搜索片段 | 官方正文、固定源码、具体故障/测试记录 |
| C4 Linux | 基础设施 2 | 6.6 回归/stable 流程的搜索片段 | 正文、具体回归提交与邮件/修复/回归证据 |
| C5 Kubernetes | 架构演进 | CSI KEP/迁移与发布资料的搜索片段 | 固定 KEP、实现/测试、实际迁移里程碑核验 |
| C6 SWE-agent | AI/Coding Agent | 原始论文/官方仓库入口检索 | 论文正文、真实 tag→SHA、工具/环境/测试源码与成本 |

同仓多个文件能组成一条证据链，不是多份独立实验。C1/C2 的版本是可复核快照，不代表截至 2026-11-06 的推荐最新版本。

## C1. UniTask：取消何时生效，与池化归还是否同一件事

### 1. 背景、版本与问题

Cysharp/UniTask，tag `2.5.10` → `7c0f199fe0d3fc528024488ccd671e6c7b27745b`，提交日期 2024-10-03。版本 ref 与 manifest 已实际读取；MIT 许可已读。证据 `ER-20261106-game-01/02`。

研究题设：团队想把高频可取消等待统一改成 `SuppressCancellationThrow`，或一律加 `cancelImmediately: true`，以为取消结果与归池表现都保持不变。需要判断：**包装层正确报告取消，能否证明 source 已消费并可复用？**

范围：创建时 token 未取消、`DelayType.DeltaTime`、相关 PlayerLoop 已注入且持续推进、单次消费。不是所有 UniTask source，也不是原生资源加载或多线程通用池。

> **question** — 阅读闸门：先提交预测，再开放解析
> 首次练习先停在这里，只根据题设和接口认识填写下表，标记不确定处；保存预测后再阅读 §2–6。尚不知道也是有效基线，不要求先猜中。若已经从本库、主报告或 Blog 知道关键结论，原题只作示范，不能计入无提示独立预测；请评阅者另选未见的 source/取消时序变式，预先确定 oracle 后再开放材料。

| 中途取消路径 | 谁完成 core | 是否消费底层 source | 何时 runner 脱离 | 是否尝试归池 |
|---|---|---|---|---|
| 默认普通 await | 待预测 | 待预测 | 待预测 | 待预测 |
| 默认 suppress | 待预测 | 待预测 | 待预测 | 待预测 |
| 即时普通 await | 待预测 | 待预测 | 待预测 | 待预测 |

### 2. 代码路径与模块边界

路径基于 `src/UniTask/Assets/Plugins/UniTask/Runtime/`：

| 文件/符号 | 读过的关键定位 | 所有权问题 |
|---|---|---|
| `UniTask.Delay.cs` / `DelayPromise` | L698–828；Create、GetResult、MoveNext、TryReturn | 谁完成 core、谁触发重置/尝试归池？ |
| `UniTask.cs` / `SuppressCancellationThrow`、`IsCanceledSource` | L68–74、169–208 等 | 包装是否调用底层 GetResult？ |
| `PlayerLoopHelper.cs` / AddAction | L492–505 | 谁持有调度项？ |
| `Internal/PlayerLoopRunner.cs` / RunCore | L157–257 | 返回 false 后移除哪条引用？ |
| `UniTaskCompletionSource.cs` / core | TrySetCanceled、GetResult、Reset | continuation 可否在完成调用内直接执行？ |
| `TaskPool.cs` / TryPush | L103–121 | 尝试归池是否一定成功？ |

完整固定链接及实际读取范围登记于 `ER-20261106-game-04`～`09`，不是通读仓库。

正常轮询取消链：`Delay → DelayPromise.Create → AddAction → runner.MoveNext → core.TrySetCanceled → continuation/普通 GetResult → finally/TryReturn`；runner 另根据 false 去引用。完成、消费、调度脱离、允许复用不是一个动作。

### 3. 源码事实与设计理由

**静态事实**：

- 普通非即时取消，普通 await 消费会进入 `DelayPromise.GetResult`，finally 尝试 `TryReturn`；池仍可能拒收。
- suppress 包装的 canceled 分支直接返回 true，不调用底层 `source.GetResult`。在本案中途取消组合下，未走到已读的 `DelayPromise.GetResult → TryReturn` 路径。runner 移除并不补做消费清理。
- 即时取消是另一分支：registration 可以直接完成 core；普通 GetResult 的 finally 在“即时且 token 已取消”条件下跳过 TryReturn。不能把两者叫作同一个问题。

**作者直接说明**：README 描述默认 PlayerLoop 轮询与即时 registration 的成本取舍、suppress 避免取消异常开销的动机。`ER-20261106-game-03`。这是机制/动机，不是本研究性能测量。

**研究者推断**：即时完成后若仍有 runner 旧引用，立刻重置复用可能触及下一代状态；因此修复必须考虑消费、调度和回调三方。没有找到作者直接说明“归池条件正是为此而写”的证据。

**未证实**：没有证明永久内存存活、现场 leak 或帧时间退化。Issue #661 确有相关报告，但未给精确版本，之后由 stale bot 关闭，不是维护者确认修复。`ER-20261106-game-12`。

### 4. 备选、收益与代价

| 方案 | 可能收益 | 代价/边界 |
|---|---|---|
| 默认轮询+普通 await，在业务边界处理取消 | 本快照有清楚的消费/finally 路径 | 异常成本、取消等相关 loop 推进；不是一定回池 |
| 保留 suppress/即时取消 | bool 表达或更早完成 core 的语义 | 必须单独审查回收；不能宣称纯语法替换 |
| 两阶段/多条件回收协议 | 显式等待旧访问者脱离再允许复用 | 研究者反事实，未实现；状态、重入、并发验证成本 |
| 相关路径暂不池化 | 减少代际复用复杂性 | 研究者反事实，分配/GC 代价待测 |

不是作者已对比并放弃后两案。不能在 suppress 之后补 await“清理”：通常单次消费约束仍必须遵守。

### 5. 结果、演进与边界

本轮结果是**固定版本静态控制流核查与验证缺口识别**，不是运行修复。已读取消测试主要针对 DelayFrame 的 bool/异常/帧差，不断言本案 DelayPromise 的回收。`ER-20261106-game-10/11`。未阅读全部测试，不能说仓库没有别的覆盖。

不能据此全项目禁用 suppress、宣称所有即时取消都泄漏，或认定后续版本仍有同一行为。

### 6. 可迁移经验与练习

条件规则：**当适配器改写终态或异常时，应检查它是否仍转发携带清理语义的消费操作；当对象会复用时，把完成、消费、旧持有者脱离与可复用分别证明。**这是研究者归纳，不是所有 awaitable 的统一实现。

核对练习：取出 §1 保存的预测，对照三条中途取消路径逐项标记保留/修正，附改变判断的具体源码证据。这里评价证据更新；若此前未保存预测，不追认成事前独立表现，改用未见变式评价。

建议 oracle：实例+代际的借出/消费/runner 移除/registration 结束/TryReturn 尝试/TryPush 成功记录；不能只看 Tracker 消失或池大小。若声称 leak 还须引用链与存活观测。**本轮未运行。**

## C2. NGO：网络身份注销与物理归池不能混为一谈

### 1. 背景、版本与问题

Unity Netcode for GameObjects，tag `ngo/1.9.1` → `7d27c5141123e3b9f31419ccca7768a640a45d56`，提交日期 2024-04-18；manifest 为 1.9.1、声明 Unity 2021.3；MIT 许可已读。`ER-20261106-game-13/14`。声明不等于本轮兼容构建测试。

研究题设：server/host 手动从池 Get 动态炮弹再 Spawn，远端注册 `INetworkPrefabInstanceHandler`。团队想在 `OnNetworkDespawn` 与 handler `Destroy` 都 Return，并认为 `Despawn(false)` 会使所有端对称保留物理对象。

范围：server-authoritative、正常会话、动态 prefab、handler 映射有效、远端可见、手动 Get+Spawn。scene object、shutdown、override、late join 和便利入口需另查。

### 2. 模块与调用链

基于包目录 `com.unity.netcode.gameobjects/`：

- `Runtime/Core/NetworkObject.cs`：SpawnInternal L761–782、Spawn/Despawn L856–893、生命周期通知、AddSceneObject。
- `Runtime/Spawning/NetworkSpawnManager.cs`：生成/注册、发给自身排除、OnDespawnObject L958–1075、关服与便利入口。
- `Runtime/Spawning/NetworkPrefabHandler.cs`：接口、hash 注册、spawn/destroy dispatch。
- `Runtime/Messaging/Messages/CreateObjectMessage.cs`、`DestroyObjectMessage.cs`：远端生成/注销及 flag。
- 仓库 `testproject/Assets/Samples/PrefabPool/`：pool 与 companion 样例，**不是 package runtime 内建池**。

证据 `ER-20261106-game-15`～`21`。

生成：authority 手动 Get → `NetworkObject.Spawn → SpawnInternal → SpawnNetworkObjectLocally`；不因这次 Spawn 再调用 handler Instantiate。host 不向自己的 server client ID 再发生成消息。远端则走 CreateObjectMessage → AddSceneObject → CreateLocalNetworkObject → handler Instantiate → 本地登记。

注销：`Despawn → DespawnObject → OnDespawnObject`；业务 `OnNetworkDespawn` 通知后，仍有消息、IsSpawned、registry、observers 清理；之后才进入常规物理释放分支。

### 3. 事实、冲突与理由

- 实际公共签名默认 `Despawn(bool destroy = true)`。handler XML 却把默认值写成 false，属于本快照内冲突，不能盲信注释。
- 常规有 handler 路径，`Despawn(true)` 把物理释放交给 handler；handler 可停用归池，不必 Unity Destroy。
- `Despawn(false)` 在该 authority 正常路径不调用本地 handler Destroy；动态对象发往远端的 `DestroyGameObject` 仍为 true。各端行为不能只凭同名参数推断对称。
- `OnNetworkDespawn` 不代表旧网络流程已不再读取实例。若此时 Return 就能同步借出，可能在旧流程中改变下一代状态；两处都 Return 则有双重发布风险。
- “Instantiate 只在 client 调用”不是全入口定理：host/forceOverride 的 `InstantiateAndSpawn` 有不同分支。shutdown 也有不同释放顺序。

**直接历史理由**：PR #977 说明接口命名/XML 调整为减少困惑，并讨论 host override/hash 与递归注销。Issue #990 是旧 MLAPI develop 报告并关联该 PR；不能把它写成 1.9.1 已复现故障。`ER-20261106-game-24/25`。

**研究者解释**：网络身份管理与物理实例策略分开，允许创建销毁/池化/override 适配；没有找到作者完整比较“内建池与 handler 池”的 ADR，不能替作者补理由。

### 4. 方案与权衡

| 方案 | 收益 | 代价与实施边界 |
|---|---|---|
| 正常 true、handler 为唯一 Return owner | 沿用扩展点保留逻辑注销，再做物理归池 | 正确注册、重置、角色/代际；不能再在业务通知中重复 Return |
| authority false，调用返回后手动 Return；远端仍由 handler | 与既有分角色获取路径一致 | 两种责任必须显式；shutdown/override 另验证 |
| 不池化，正常销毁 | 减少代际与空闲集合复杂性 | 创建销毁成本待测；不适合已测高频瓶颈时仍盲用 |
| 通知中清业务状态，但延迟发布空闲 | 不把通知误当最终释放 | 必须证明发布时旧访问已结束，不能只固定延迟一帧 |

后三项含研究者反事实，不是上游实测排名。生产池的容量、代际、防重、重置与恢复不能由样例自动获得。

### 5. 结果与测试 oracle 审计

本轮没有运行。已读 `NetworkPrefabHandlerTests` 主要直接验证内部 dispatch，测试 handler 真正 Destroy，并非端到端池借还证明。`ER-20261106-game-22`。

更具体的发现：`Tests/Runtime/NetworkObject/NetworkObjectOnNetworkDespawnTests.cs` L109 在 server shutdown 后仍等待 `OnClientNetworkDespawnCalled`，client 标记此前已满足。因此该后半断言不能独立证明 server 回调；**不是证明 server 真的漏回调**。`ER-20261106-game-23`。

这说明：测试名包含 server/client，不足以证明 oracle 覆盖两端；要看实际变量和前置状态。

### 6. 迁移与练习

条件规则：**逻辑身份注销与物理实例复用分开；按进程、入口、借出代际指定唯一归还责任；回调名不是旧访问结束证明。**网络 owner ID 也不是应用物理内存 owner。

练习：host+两远端，手动 Get+Spawn，分别 true/false，画每进程的 Get/Spawn/OnNetworkDespawn/handler Destroy/Return。指出双还、漏还与过早重用位置；再审查关服测试的实际断言。

建议 oracle：实例 ID+借出 generation、free 集合与 registry 关系、同代至多一次发布、下一代无旧回调副作用。正常路径先验表不能覆盖 shutdown/断线/override；**本轮均未执行**。

## C3. SQLite：把持久化保证转成可破坏的测试

> **warning** — 待核案例，非源码完成案例
> `ER-20261106-infra-01/02` 只有官方资料搜索片段；正文抓取失败，未固定 SQLite release/SHA，未读 `wal.c`，未运行测试或故障注入。以下机制是待核候选，不作为已核验事实。

### 背景与问题

数据库必须在错误、崩溃和资源不足时维持明确的事务/恢复契约。研究决策：选择 WAL 时，怎样把吞吐、并发、checkpoint、部署条件与持久化要求一起验收，而不是只看正常读写速度？

### 证据、路径与设计选择

候选一手材料：官方 `testing.html`、TH3 介绍、`wal.html`。检索片段涉及 OOM/I/O/掉电测试、覆盖分析与 WAL checkpoint；尚未读正文，不能精确声称某版本所有模块达到 100% MC/DC。

源码/测试路径、调用链、故障调度与具体 oracle：**未核实**。TH3 不全公开，不能承诺读者能复现全部内部体系。实际作者在指定版本为何选特定机制：**未核实**。

### 备选与权衡（研究者分析）

- 回滚日志与 WAL 是需要按实际版本核查的备选；不预设 WAL 总更好。
- 待验证场景：长读事务、checkpoint、读写竞争、共享内存/网络文件系统、附加数据库原子性。
- 收益与代价：没有本轮基准，不排名；需要明确 durability 配置、文件系统与故障模型，不能把“测试很多”当无缺陷保证。

### 结果、边界、迁移与练习

运行与后续具体修复记录：**未完成**，不得补造。

可迁移建议：对 Unity 存档/资源更新，先列“部分写入/版本混用/中断恢复”的不变量，再设计可控的失败点；不能直接移植数据库内部测试平台或声称它证明游戏存档安全。

练习：为一个不含真实用户数据的练习存档设计正常、部分写入、磁盘不足、重启恢复矩阵；先规定最终可接受状态，不能只检查未抛异常。需另外授权和执行，本轮未做。

**补齐门槛**：读官方正文 → 固定 release → 读至少一条真实提交/测试路径 → 分清契约、作者实验与本轮验证。

## C4. Linux：回归修复为何不等于顺手改造

> **warning** — 待核流程案例
> `ER-20261106-infra-03/04` 是 Linux 6.6 版本文档的搜索片段；正文访问失败。没有选定并读完一个具体回归的提交/邮件/修复/回测链，因此不能伪装成完整源码故障案例。

### 背景与问题

成熟系统中修复回归，需要在恢复行为与扩大变更半径之间取舍。具体研究问题：什么时候局部补丁/backport 更适合，什么时候应把结构性改造放到独立变更？

### 候选证据与未完成项

候选：6.6 的 `process/handling-regressions.html`、`process/stable-kernel-rules.html`。索引涉及回归追踪、维护者、稳定版补丁和 backport 条件。不可把 `/next` 最新政策写成 6.6 已读契约。

具体文件/函数、引入提交、真实备选争论、修复与回归结果：**尚未取得**。所以“项目实际放弃了重构”或“某补丁缩短修复 X 天”都不能写。

### 备选与权衡（研究者设计）

- 回滚引入变更：恢复已知行为，但可能丢失必要功能或遇依赖。
- 最小局部修复：控制回归半径，但可能保留结构性债务。
- 独立后续重构：改善未来变化，但不应隐含在紧急修复中。

选择要有具体上下文、维护者授权和测试；这里没有真实个案结果替这些方案排名。

### 迁移与练习

可迁移建议：Unity 紧急修复分清止损、原因修复和结构改善；记录后续任务，不趁机重写共享框架。**不照搬 Linux 整套邮件/组织流程。**

练习：对已授权练习仓库的一次回归列回滚/局修/重构三案；指定能够改变选择的证据与最小回归集。当前没有运行结果。

**补齐门槛**：取得一条真实 regression report→引入 SHA→讨论→修复 SHA→stable/backport→验证证据，不只引用流程网页。

## C5. Kubernetes：CSI 迁移的兼容层与终止条件

> **warning** — 待核架构演进案例
> `ER-20261106-infra-05/06/07` 仅检索片段。KEP 625 是浮动 master 链接，未固定；官方博客正文抓取失败。未读实现与升级测试，不能说已核实各里程碑完成。

### 背景与问题

研究对象是从 in-tree 存储/云提供商耦合逐步转向外部组件的真实演进方向。CSI migration 与 cloud-provider removal 有关联但不是同一项变更，不能混合时间线。

判断问题：如何保持旧 API/持久状态兼容、逐步换实现，并最终删掉兼容路径，而不是让双轨永久存在？

### 证据与待核选择

候选 KEP 625、2021 CSI migration 状态、2024 cloud-provider 迁移总结和 1.31 发布记录。索引提到旧 volume API 到 CSI 的转换、分阶段迁移与升级/降级测试。**具体转换路径、feature gate 生命周期、实现文件、真实回退条件均未核实。**旧 roadmap 不是最终落地证明，历史关闭 gate 的回退也不等于 GA 后仍可用。

### 备选、收益与代价（研究者分析）

| 方案 | 可能收益 | 主要风险 |
|---|---|---|
| 一次性替换并要求调用方同步升级 | 迁移期短 | 跨版本/持久状态/运营窗口可能不允许 |
| 保留入口，兼容层转换，逐步替换 | 降低调用方同步变更压力 | 双轨、一致性、观察与维护成本 |
| 永远保留旧实现 | 短期避免迁移 | 依赖负担、重复维护、安全与平台变化 |

不是宣称三案都在该 KEP 中被作者正式对比。实际收益、事故与成本尚未取得原始资料。

### 结果、迁移与练习

本轮不能确认某云/存储插件的迁移成功率或完整移除时间。可迁移的是**契约与实现分离、逐步替换、兼容矩阵、可观测、双轨退出门槛**的设计问题，不是“游戏项目都应上兼容层”。

练习：旧资源加载接口要替换实现，列旧/新客户端×旧/新内容×切换/回退组合，指出哪些持久状态变化不可逆；写清何时删适配层。没有本轮部署或测试。

**补齐门槛**：冻结 KEP 和相关实现，核验实际 milestone、gate 移除与文档、读升级/降级测试和维护讨论。

## C6. SWE-agent：工具界面、执行反馈与外部验收

> **warning** — 待核 AI 案例
> `ER-20261106-ai-04/05/06` 原始论文与源码访问失败。未冻结 release/tag/SHA、容器、模型和数据集 revision；未运行 agent，没有 patch、轨迹、账单或成功率。候选旧版 URL 请求失败，不证明该 tag 存在。

### 背景、问题与入口线索

真实项目 SWE-agent 把 agent-computer interface（ACI）作为研究对象。问题是：模型处理 issue 时，看到什么、怎样搜索/编辑、何时取得执行反馈、何时停止，如何影响可控性与验收？

旧 Issue 索引含 `run.py`、`sweagent/agent/agents.py` / `Agent.run()`，但这些只是历史入口线索，不是当前固定调用链。

待核框架：CLI/配置→任务与仓库→环境初始化→agent 循环→工具/观察→补丁→外部评估→清理。**这是核查提纲，不是源码事实。**

### 设计、替代与权衡

| 研究者备选 | 可能收益 | 必须验证的代价 |
|---|---|---|
| 人主导 IDE+补全 | 人掌握上下文与决定 | 审核整合时间，不只算生成 |
| 通用 shell agent | 工具灵活 | 权限、输出噪声、错误编辑、上下文成本 |
| 检索后直接 patch | 交互较少 | 定位错时缺少执行反馈 |
| 专用 ACI/harness | 组织搜索/编辑/反馈 | 工具维护、截断、语言支持、接口偏置 |

论文题目/索引足以定位研究方向，不足以证实每项机制的消融效果。没有读成本表，不补造美元/任务。benchmark resolved 不等于安全、维护者接受、完整交付或人类学会。

### 结果、边界、迁移与练习

本轮结果只有发现与访问失败。未来比较须固定同模型、同任务/预算、同可见测试与干预，报告所有实例而非精选成功轨迹。功能测试、人工审查、资源/费用、时间和学习应分测。

迁移建议：Unity agent 委派应有路径/权限/版本、最小 diff、独立 oracle 与人工批准；不能由 Python issue benchmark 断言能处理目标引擎的资产/生命周期/平台发布。

练习：给一份“测试通过”的假设补丁记录，列已证明/未证明、可能共享错误的实现与测试、独立反例；设计区分模型贡献与工具贡献的比较。**题设不是已发生的实验。**

**补齐门槛**：论文发表版→真实 ref→完整 SHA→环境/工具/提交/清理/评估源码→分母/成本/失败条件核查；没有运行仍保持 not-run。

## 跨案例综合：能说与不能说

C1/C2 静态证据支持两条窄观察：结果/回调不等于所有权结束；测试必须审查 oracle 而非只看名称。由此提出可迁移检查法是**推论**，还没有证明它提高了训练成绩。

C3–C6 只能说明已经找到哪些真实研究对象、哪些问题值得追查；不能作为 M1–M7 已完成真实案例验证的证据。七模型的案例适配检查、训练效果验证、外部人工技术审核是三件不同的事，后两者本轮均未完成。
