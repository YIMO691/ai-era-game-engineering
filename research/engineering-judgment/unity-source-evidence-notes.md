---
title: Unity／C# 工程判断训练：取消消费与网络池化的回收所有权
date: 2026-11-06
cutoff: 2026-11-06
status: static-research-draft
experiment_status: not-run
publication_status: private-not-reviewed
tags:
  - engineering-research
  - engineering-judgment
  - Unity
  - CSharp
---

# Unity／C# 两个固定源码案例

> **公开导出注（2026-11-12）**：以下研究状态、访问和审查记录属于原 2026-11-06 草案；本次只作本地白名单导出。公开授权不等于人工研究审核、实验通过或生产验收。私有状态描述是历史记录；模板及操作文本仅作资料，不在本次执行。转换与排除见 [导出清单](export-manifest.json)。


> **important** — 范围与可信度
> 这是供主报告使用的两个独立案例，不是完整研究包。已先读工作区 `CLAUDE.md` 与 `references/research-contract.md`；按本次“唯一可写目标”的更具体要求，把证据登记和主张边界放在本文件，不另建 `sources.md`、计划、元数据或报告文件。初查目标不存在；工作区 Git 查询返回“不是 Git 仓库”，没有创建仓库或提交。
>
> 截止与访问日期均为 **2026-11-06**。只读公共 GitHub REST、固定 SHA 的官方源码和测试；源码内容仅在读取管道/工具输出中处理，没有落地下载工程、安装依赖、执行下载代码、编译或运行 Unity。所有来源的 `experiment_status=not-run`。测试正文已读不等于测试通过；下文 oracle 是建议的判定依据，不是实验结果。
>
> Unity 文档站的一次 WebFetch 被安全检查拒绝，已登记为 ER-20261106-game-26，没有改用 curl、代理或其他客户端重试该站。其余源码、测试与 Issue／PR 正文是实际成功读取的官方来源，不依赖搜索摘要或社区镜像。

## 一、选择与冻结

正文中的 `[04]`、`[15～20]` 等是本文件稳定证据 ID `ER-20261106-game-04`、`ER-20261106-game-15` 至 `ER-20261106-game-20` 的缩写；完整元数据见第五节，同源不重复计数。

研究问题不是“池化是否好”，而是：**一个操作已经取消或一个对象已经收到 despawn 回调，是否就足以把底层实例交给下一位使用者？谁有权宣布旧生命周期结束？**

| 案例 | 实际冻结对象 | 背景与决策价值 |
|---|---|---|
| A：Cysharp／UniTask | tag `2.5.10` → commit `7c0f199fe0d3fc528024488ccd671e6c7b27745b`；提交时间 2024-10-03T00:42:37Z；包内版本同为 2.5.10 | Unity 客户端可取消等待、PlayerLoop 调度与 promise 池化的消费协议；不要把异常表现改写当成无成本包装。 |
| B：Unity Technologies／Netcode for GameObjects | tag `ngo/1.9.1` → commit `7d27c5141123e3b9f31419ccca7768a640a45d56`；提交时间 2024-04-18T16:34:14Z；包内版本同为 1.9.1 | 动态网络 prefab 在 server／host／远端 client 上有不同的实体获取入口；网络 despawn 与 Unity 对象归池不是同一动作。 |

两个 tag 的 GitHub REST `git/ref` 返回的对象类型都为 `commit`，本次不需要再解引用 annotated tag。下文源码链接全部使用这些实际 SHA；没有以当前 `master`、`develop` 或“最新版”代替冻结。固定旧版本是为了可复核，不表示截至截止日它们仍是推荐最新版本。[ER-20261106-game-01、13]

UniTask 的 `package.json` 声明 Unity 2018.4；该快照 README 写的最低正式支持版本是 2018.4.13f1。NGO 的 manifest 声明 Unity 2021.3，依赖 Unity Transport 1.4.0 与 mono-cecil 1.10.1。这里只记录包声明，不声称已用这些 Editor／后端完成兼容性测试。[ER-20261106-game-01、03、13]

**停止条件已满足**：每案都有固定实现、实际函数调用路径、已读测试、官方契约文字及至少一个真实公共讨论记录；不为补数量追逐未验证的版本或 Issue。没有使用 Addressables 备选。

## 二、案例 A：取消已经被观察到，不等于 promise 已经回池

### A1. 具体情境与要作出的判断

题设为一个 UI／技能流程：组件持有取消源，启动时 token 未取消，创建尚未结束的 `UniTask.Delay`，随后在等待中取消。团队准备统一使用 `SuppressCancellationThrow`，理由是“取消本来不是错误；不抛异常更轻，而且 UniTask 内部会池化”。另一个提案是所有等待都加 `cancelImmediately: true`，认为这样“完成得更快，也能更快归池”。

**需要判断**：在冻结版本中，这两个改动是否保留底层 promise 的消费／回收协议？如果返回值已经表达取消，是否还可推断其 source 已清理、runner 不再持有它、实例已可复用？

本案主路径限定为 `DelayType.DeltaTime`、已注入并持续推进的指定 PlayerLoop、单次消费。EditMode 的类型切换、Unity 原生 AsyncOperation、线程池定时器和全部 UniTask 操作符不在结论范围内。

### A2. 模块边界：三个不同的“完成”

| 模块 | 本路径中的职责 | 不能据此自动推出的事 |
|---|---|---|
| 调用方／取消源 | 决定何时不再需要等待，持有 token；消费返回的 awaitable | 请求取消不是归还 `DelayPromise` 的 API。 |
| `UniTask`／awaiter／`IsCanceledSource` | 表达状态、注册 continuation、调用底层 `GetResult` 或把取消改写为 bool | 包装层返回 bool 不保证底层 `GetResult` 被执行。 |
| `DelayPromise`／completion core | 判断时间、完成状态，保存 continuation；在特定 `GetResult` 路径重置并尝试归池 | core 已取消不等于 loop item 已被移除，也不等于池接收成功。 |
| `PlayerLoopHelper`／`PlayerLoopRunner` | 将 item 放入指定 timing 的 runner；根据 `MoveNext` 返回值移除队列引用 | runner 只移除 item，不替所有 source 执行消费清理。 |
| `TaskPool<DelayPromise>` | 空闲实例的 `TryPop`／`TryPush`，受容量与 gate 约束 | `TryReturn` 被调用也只能说尝试回池，不能无条件说一定缓存。 |

源码定位分别见 ER-20261106-game-04～09。

**正常、非即时取消的调用链**：

1. `UniTask.Delay` 的重载分派到 DeltaTime 分支，再进入 `DelayPromise.Create`。创建时先检查预取消；本题设未取消，因而从池取实例或 new，保存 token 与初始帧，再把 item 交给 `PlayerLoopHelper.AddAction`。[04]
2. `PlayerLoopHelper.AddAction` 找到该 timing 的 runner；未注入时抛异常。`PlayerLoopRunner.AddAction` 在 runner 正运行时先入等待队列，否则放入 item 数组。[06、07]
3. 指定 runner 执行 `DelayPromise.MoveNext`。取消检查位于时间累加之前；检测到取消则调用 core 的 `TrySetCanceled`，随后返回 false。[04]
4. 已注册 continuation 可以由 core 在 `TrySetCanceled` 内直接调用。普通 awaiter 的 `GetResult` 会进入 `DelayPromise.GetResult`；core 抛取消异常，但 promise 的 `finally` 在非即时分支仍执行 `TryReturn`。[04、05、08]
5. `TryReturn` 清 tracking、重置 core 和字段、处置 cancellation registration，最后尝试 `pool.TryPush`。runner 则根据 `MoveNext=false` 去除自己的引用。两件事职责不同，且 continuation 可能重入；不能把它们口头合并为一个瞬时动作。[04、07～09]

### A3. 已读源码暴露的两个不同回收问题

**事实 A-1：抑制取消的包装层可能跳过源消费。**

`UniTask.cs` 的非泛型 `SuppressCancellationThrow` 会检查当前状态；pending 时创建 `IsCanceledSource`。该包装的 `GetResult` 发现 source 已取消就直接返回 true，不调用底层 `source.GetResult`；若调用包装时 source 已是 canceled，前面的快捷分支也直接返回已完成的 true。泛型包装也有取消时不调用底层 `GetResult` 的分支。[05]

因此，对本题“创建时未取消、普通轮询取消、等待中被取消并通过 suppress 包装消费”的组合，静态调用链能推出：**返回值可以正确表示取消，但没有走到 `DelayPromise.GetResult → TryReturn`。** `MoveNext` 的取消分支只有完成 core 与返回 false；runner 移除引用时也没有替它回池。[04、05、07]

这是一个**固定版本的回收协议缺口判断**，不是“现场实测内存泄漏”。未回池可能影响后续分配与复用；是否仍有强引用、能否被 GC、是否持续保留内存及实际开销，需要另外检查引用链与运行环境，不能从池容量或 Issue 标题直接推断。

**事实 A-2：即时取消的普通 await 也不等于正常归池路径。**

`cancelImmediately=true` 且 token 可取消时，`DelayPromise.Create` 注册回调，回调直接对 core 尝试取消。`DelayPromise.GetResult` 的 `finally` 特别检查“即时取消且 token 已取消”，成立时只移除 tracking，不执行 `TryReturn`。之后 `MoveNext` 看到取消返回 false，也没有补充归池调用。[04]

因此，这与 suppress 跳过源消费是**两个不同分支**：前者可能根本不进入 source 的 `GetResult`；后者即便进入，也有明确的跳过归池条件。不能把二者混写成“同一个已确认 bug”，更不能建议删掉所有条件、在完成回调里无条件复用实例。

**研究者推论，而非作者解释**：即时回调可以先于 runner 下一次处理发生，core 又可能同步触发消费 continuation。如果此时把仍在 runner 队列中的同一实例重置并重新借出，旧 runner 入口可能接触下一代任务状态。这个时序说明“完成就立刻归池”的改法需要额外所有权协议，但已读来源没有直接说明作者正是出于这个理由写下该条件。[04、07、08]

### A4. 作者设计理由：有证据的与没有证据的

| 判断 | 证据地位 |
|---|---|
| 默认轮询而非即时 registration，是带成本取舍的 API 选择 | README 直接说明默认在 PlayerLoop 检查取消，即时模式使用 `CancellationToken.Register`，其成本更重。[03] 这是作者机制与动机说明，不是本研究的性能测量。 |
| suppress 的动机是避免抛／捕获取消异常的成本 | README 直接说明，并要求尽量在最靠近源的位置调用。[03] 不由此推导“整个 pipeline 零异常／零分配”。 |
| 作者有意让 suppress 绕过 promise 回收 | **没有找到直接证据。** 实现有该控制流；不能把实现结果自动解释成设计意图。 |
| 即时取消跳过归池，是为了防止 runner 对复用实例的旧引用 | **没有直接作者证据；仅为上节标明的研究者时序推论。** |
| `SuppressCancellationThrow` 的回收问题已有官方修复承诺或验证 | **不能这样说。** Issue #661 的报告与冻结源码的分支相符，但报告未明确版本；唯一已读评论是 stale bot。REST 显示其于 2025-12-11 被 bot 关闭，`state_reason=not_planned`，不是维护者确认的修复或回归通过。[12] |

Issue #661 的真实页面题为 *DelayPromise Leaks when use SuppressCancellationThrow*，2025-05-14 创建。本文只采用其“有人明确报告了这一消费分支”的事实；是否构成运行时 leak，仍不由该标题证明。[12]

### A5. 方案比较与工程建议

以下是**研究者方案比较**；除明确标出的现有实现外，不冒充作者曾比较过的历史方案。

| 方案 | 为什么可能采用／收益 | 代价、适用及失效边界 |
|---|---|---|
| 保持 `cancelImmediately=false`，普通单次 await，在业务边界捕获取消异常 | 冻结源码有明确的 source 消费与 `finally → TryReturn` 路径；默认取消时序与 PlayerLoop 一致。[04、05] | 有异常传播成本；取消依赖该 timing 继续推进。池满或竞争可使 `TryPush` 失败；不是“必然零分配”。若本就不能容忍等待下一次 loop 检查，此方案不满足时延需求。 |
| 直接使用现有 suppress／即时模式 | suppress 提供 bool 结果；即时模式在不等待下一次轮询的路径尝试完成 core，满足不同 API 表达或响应需求。[03～05] | 本快照不能再顺带承诺同样的回收路径。要单独评估 source 消费、队列残留、registration 生命周期；不能仅凭取消结果正确验收池化。 |
| 反事实：把回收改成“两阶段／多条件归还”协议 | 显式区分结果消费、scheduler 脱离、registration 回调不再操作旧代，条件满足后再复用；可处理即时完成与重入。 | **研究者反事实，未实现未运行。** 需要状态机、代际验证、异常路径和并发／重入测试，可能增加字段、分支与同步成本；不能用简单地把 `TryReturn` 搬进 `MoveNext` 来替代。 |
| 反事实：对这一热路径暂不池化，先保证一次性 source 生命周期 | 降低“旧队列引用＋复用实例”的推理难度，使正确性优先。 | **研究者反事实。** 会有分配／GC 代价；若 profile 表明池化有决定性收益，仍需更完整协议。本文没有数据判断两种开销谁更小。 |

**本案独立建议**：在冻结版本的高频取消路径，不把 suppress／即时选项当作纯语法重构。先选择可接受的取消时序与异常表达，再按 source 的实际消费路径审查回收。若要修改上游实现，需要把 scheduler 脱离和回调生命周期一起纳入，而不是只修 bool 返回值。

### A6. 可迁移与不可照搬

- **可迁移**：把“结果终态”“结果已消费”“scheduler 已不再访问”“可复用”分别建模；审查适配器时必须检查它是否转发了带清理语义的消费方法，而不仅是状态和值。[04～08]
- **可迁移**：测试至少同时覆盖功能结果和生命周期；“取消返回 true”不是“底层 source 被恰好归还一次”的 oracle。
- **不可照搬**：不是所有 Task／UniTask source 都把清理放在同一个 `GetResult`；本案不支持“全项目禁用 suppress”或“所有 cancelImmediately 实现都不归池”。
- **不可照搬**：`short` 版本号、具体 PlayerLoop timing、池的 gate 与字段重置顺序都是实现细节；不能把这套实现直接移植为任意多线程对象池的完整安全协议。[08、09]
- **边界**：README 明确 UniTask 通常不能重复 await；不能在 suppress 之后补一次 await 来“补清理”。编辑器、停止推进的 loop、类型分派、预取消和完成／取消竞争均须另设测试条件。[03、04]

### A7. 独立判断练习与建议 oracle

**先给学习者的题设**：同一个尚未取消的 token，分别创建三个足够长的 DeltaTime Delay；均在下一次相关 runner 执行前取消，且仅消费一次。

1. 默认模式＋普通 await 并捕获取消；
2. 默认模式＋`SuppressCancellationThrow`；
3. 即时模式＋普通 await 并捕获取消。

要求不运行代码，先分别填写：谁完成 core、何时能移除 loop item、底层 `GetResult` 是否被调用、`TryReturn` 是否被尝试。再回答：如果只看到 bool 正确、Tracker 消失或池大小没增长，能否下结论“没有泄漏／已经回池”？设计一个不靠重复 await 的补充测试。

> **note** — 建议 oracle（静态预期；没有执行）
> - 1：runner 检测取消并完成 core；普通消费进入 `DelayPromise.GetResult`，在 finally 尝试 `TryReturn`；runner 根据 false 移除 item。池是否接收仍取决于 `TryPush`，不是保证。[04、05、07～09]
> - 2：runner 同样完成 core；包装返回 true，但取消分支不调用底层 `GetResult`，因而上述 `TryReturn` 路径未发生；runner 移除不补做 source 消费。[04、05、07]
> - 3：registration 回调可以先完成 core；普通消费虽进入 `GetResult`，其即时取消条件跳过 `TryReturn`。下一次 runner 的取消检查仍返回 false。[04、08]
> - 已读 `AsyncTest.ExceptionlessCancellation` 与 `ExceptionCancellation` 测的是 **DelayFrame**，分别检查取消 bool／异常及前者的帧差；它们没有断言 DelayPromise 复用、回池次数或即时取消竞态。`DelayTest.DelayFrameZero` 也只是特定时序下的帧数契约，不是内存 oracle。[10、11]
> - 建议未来在另获授权的固定版本测试副本中观测：每个 source 实例及代际的借出、结果消费、runner 移除、registration 结束、`TryReturn` 尝试与 `TryPush` 成功次数。分别测试取消前／后订阅、正常完成与取消竞争、continuation 重入启动新 Delay、pool 上限及暂停 loop。只观察公开池大小会混入缓存容量／并发活动，不能唯一判断回收。
> - 若要声称“内存泄漏”，还需强引用路径、足够长时间的存活观测及明确环境；本次没有这些材料或实验。core 在完成函数内可直接调用 continuation，本路径也没有自动切回主线程的步骤，不应从“使用 UniTask”推断一切回调都有主线程亲和性。[08]

## 三、案例 B：网络 despawn 与物理归池不能由一个名字代替

### B1. 具体情境与版本边界

题设是 server-authoritative 的动态炮弹池。server／host 显式从应用池取 `NetworkObject`，然后调用其 `Spawn`；远端 client 注册 `INetworkPrefabInstanceHandler`，用自己的池创建本地对应物。团队想统一在 `OnNetworkDespawn` 和 handler 的 `Destroy` 中都执行 Return，并认为 `Despawn(false)` 能“避免销毁，因而所有机器都原样保留对象”。

**要判断**：这是否会漏还、重复还，或在 NGO 仍读取旧对象网络状态时过早发布为空闲？`destroy=true` 是否必然执行 Unity `Object.Destroy`？host 是否该按 server 和本地 client 借出两次？

范围限定：冻结的 NGO 1.9.1、正常运行会话、已注册且映射有效的动态 prefab、可见远端 client、应用手动 Get＋`Spawn` 入口。场景内对象、可见性 hide/show、连接中同步、shutdown、disconnect、prefab override 及便利入口 `InstantiateAndSpawn` 是额外分支，不能套用同一张计数表。[15～19]

### B2. 模块和所有权边界

| 模块 | 负责什么 |
|---|---|
| 应用 pool／spawner | 哪个物理实例可借出、初始业务状态与归还策略；这不是 `OwnerClientId` 的含义。 |
| `NetworkObject` | 提供 `Spawn`／`Despawn` 等入口，将操作交给本地 `NetworkManager.SpawnManager`。 |
| `NetworkSpawnManager` | 管理网络身份、spawned registry、ownership table、observers、本地网络生命周期与收发消息。 |
| `NetworkPrefabHandler` | 以 prefab hash／映射寻找应用 handler，将物理实例获取／释放交给扩展点；不是另一个 network registry。 |
| `CreateObjectMessage`／`DestroyObjectMessage` | 将远端网络生命周期转成本机生成／despawn；每个进程中的物理实例不同。 |

`SpawnInternal` 与 `DespawnObject` 都有 server 权限检查。因此“我是该对象的 network owner”不能单独成为在普通 client 调用本案 Spawn／Despawn 的权限依据。[15、16]

### B3. 实际调用链与关键事实

**生成链**：

1. server／host 的应用代码先取得并激活物理实例，再调用 `NetworkObject.Spawn → SpawnInternal → SpawnNetworkObjectLocally`。公共入口没有替调用方再执行一次 handler `Instantiate`。[15]
2. `SpawnNetworkObjectLocallyCommon` 设置身份、owner、spawn 状态、加入 registry／observers，再通知网络行为。`SendSpawnCallForObject` 对 server client ID 直接返回，host 不再给自己发一次生成消息。[16]
3. 远端接收 `CreateObjectMessage.Handle → CreateObject → NetworkObject.AddSceneObject → CreateLocalNetworkObject → GetNetworkObjectToSpawn`；有注册 handler 就进入 `HandleNetworkPrefabSpawn → INetworkPrefabInstanceHandler.Instantiate`，然后同步／登记本地网络对象。[15～18]
4. 官方仓库内的 pool 示例确实把 host／server 生成放在 `SpawnObjects`，自行 Get、SetActive、设置位置／速度后调用 `Spawn`；它的 handler `Instantiate` 从本机池获取并激活实例，handler `Destroy` 仅把池内对象设为 inactive。[20]

**正常 despawn 链**：

1. `NetworkObject.Despawn` 的**实际公共签名默认 `destroy=true`**；它进入 `NetworkSpawnManager.DespawnObject → OnDespawnObject`。[15、16]
2. `OnDespawnObject` 在发送销毁通知、设置 `NetworkObject.IsSpawned=false`、移除 spawned registry、清 observers **之前**调用 `InvokeBehaviourNetworkDespawn`。因此 `OnNetworkDespawn` 不是“NGO 已不再读取此对象”的统一边界。[15、16]
3. 对动态对象，发往远端的 `DestroyObjectMessage.DestroyGameObject` 被设置为 true，不直接复制 server 本地的 false；场景内对象才走另一个条件。[16]
4. 本地逻辑清理后，仅在 `destroyGameObject=true` 且 GameObject 仍存在时进入物理释放分支：若有 handler 则调用 `HandleNetworkPrefabDestroy`，否则调用 Unity `Object.Destroy`。handler 根据 prefab 映射调用应用的 `Destroy`，本身并不强制销毁实例。[16、17]
5. 远端 `DestroyObjectMessage.Handle` 查本地 registry，再以消息中的 flag 调用本机 `OnDespawnObject`；该消息在目标尚未生成时还有延迟处理分支。本案计数预期只覆盖对象已生成的常规路径。[19]

由此可得一个经常被名字掩盖的结果：**有 pooling handler 时，`Despawn(true)` 可以让网络对象结束这一代生命周期，同时由 handler 保留并停用 Unity 实例；`true` 不是“不允许池化”。** 而应用采用 `Despawn(false)` 时，正常路径中 server／host 的 handler 不负责本地归还，应用必须自行处理；对动态对象的远端副本仍会走收到消息后的释放路径。[15～20]

### B4. 必须保留的反例与文档冲突

- **不能把 XML 注释里的默认值当成签名。** `NetworkPrefabHandler.cs` 的 Destroy 注释写“默认 destroy 参数（false）”，但同一固定快照的 `NetworkObject.Despawn` 默认是 true。可采用其“false 不进入正常 server handler 释放”的条件描述，不能采用其默认值文字。[15、17]
- **不能把“Instantiate 只在 client 调用”升级为全入口定理。** handler 的 XML 注释有 Client Side Only 描述，但 `NetworkSpawnManager.InstantiateAndSpawnNoParameterChecks` 在 host 或 `forceOverride` 条件下调用 `GetNetworkObjectToSpawn`，后者可能分派给 handler。本案只对“应用已有实例再调用 `Spawn`”断言无额外 handler 获取；便利入口要另追调用链。[16、17]
- **不能把正常 despawn 的 flag 规则推广到 shutdown。** `DespawnAndDestroyNetworkObjects` 的 handler 分支可以先 `OnDespawnObject(..., false)`，再直接调用 handler destroy；`DestroySceneObjects` 又有不同顺序。不能据一张正常运行表格证明关闭阶段也恰好回调一次。[16]
- **不能把旧 Issue 当成 1.9.1 的现存故障。** Issue #990 报告的是 2021 年 MLAPI develop 环境，指出手工 server 获取对象没有形成 client spawn 时的 hash 映射。维护者关联 PR #977，报告者后回复已修复。当前冻结文件具有“instance 映射找不到时以 source prefab hash 查 handler”的后备分支；本文没有运行旧版／新版回归，也不声称 #990 可在 1.9.1 重现。[17、24、25]

### B5. 作者设计理由与研究者解释分开

**有直接证据**：PR #977 的公开正文明确说明，重命名接口方法及补 XML 文档，是为了更贴近方法功能、避免用户困惑；也明确讨论了 host override 的 source hash 发送、host 注册 override 以使 destroy handler 能触发，以及移除部分递归 `OnDespawnObject` 路径。它还记载过复用对象因 NetworkTransform 位置更新延迟产生闪烁的动机。[25]

这些只能证明作者在该历史 PR 中表达的目标；本文没有审读其所有 diff／review，也没有把其时的缓解手段（例如样例可见性延迟）当成跨版本通用方案或已测收益。

**有直接契约文字**：handler 接口明确允许 Destroy 时不物理销毁，而改为停用对象；Instantiate 的 pooling 提醒要求重新激活。官方 sample 的动作与此相符。[17、20]

**研究者解释**：把“网络身份／消息／registry”留在 NGO，把“具体 Unity 对象如何获取与保留”交给 handler，能让同一网络生命周期适配普通创建销毁、池化或 prefab override。手动 server Get＋Spawn 路径避免 host 再建一个本地副本，与它不向自身发送生成消息的实现一致。[15～20] 但没有找到作者直接比较“框架内建通用池”与“应用 handler 池”的完整设计决策记录，故不把这个方案比较伪装成作者原话。

### B6. 替代方案、收益和代价

以下除“现有扩展点机制”外，均是**研究者反事实／建议**，不是宣称上游已采用或测量过。

| 策略 | 为什么可能采用／收益 | 代价与边界 |
|---|---|---|
| 现有 handler 机制：应用 Get＋Spawn，正常释放用 `Despawn(true)`，handler 作为该本地实例唯一归还点 | 复用物理实例同时保留 NGO 正常逻辑清理；通过同一释放扩展点处理有映射的各端实例。handler 可先重置业务状态再停用。[16、17、20] | 注册／hash 映射、激活、角色和生命周期顺序必须正确。若 `OnNetworkDespawn` 再 Return 一次，会产生双重发布风险。池容量／重置成本与节省多少分配，本次无测量。 |
| 反事实：server 用 `Despawn(false)`，**调用返回后**由应用显式 Return；远端仍由 handler Return | 清楚保留 authoritative 物理实例，把 server 的归还策略留给业务；适合 server／client 获取路径本就不同的架构。 | 必须按进程／角色分开责任；不能在所有端都手工 Return 并再保留同样的 handler Return。漏掉 server 手工归还就留有非 spawned 的活动实例；需要另外审查 shutdown 与 override。 |
| 反事实：暂不池化；不注册该物理释放 handler，正常 `Despawn(true)` 交给 Unity 销毁 | 减少借出代际、空闲集合及重置责任；适合生成频率低或尚未证明有性能瓶颈的对象。 | 创建销毁与 GC／原生对象成本可能增加；实际帧时间仍需 profile，不能称为“必然更慢”。应用不应同时保留把同一实例当作可复用对象的其他引用。 |
| 反事实：在 `OnNetworkDespawn` 中就发布实例到 free pool | 看起来能集中清理通知。 | **不建议作为唯一且立即可借出的归还点。** 本快照后续仍用对象的网络身份发送消息及清 registry；若 Return 同步触发重新借出／Spawn，存在旧流程触碰新一代状态的时序风险。可以在该回调清业务状态或预约延后归还，但必须另定义发布为空闲的安全边界。[15、16] |

**本案独立建议**：给每个物理实例、每次借出的 generation 定义唯一 Return owner；在明确角色及入口后选 handler 归还，或 server false＋手工归还，不两套叠加。`OnNetworkDespawn` 先作为业务生命周期通知，而不是默认的“实例已可再次借出”证明。不同进程各归还自己的实例不是双还；同一进程同一代被两个回调都归还才是需要拦截的问题。

### B7. 适用／失效边界与可迁移性

- **适用**：高频动态、server-authoritative prefab，资源就绪、handler 已注册、prefab hash 匹配，且应用能完整重置自己的血量、事件订阅、物理状态与异步任务。重置清单属于研究者建议；本次没有证明 NGO 替应用完成了这些业务重置。
- **失效／需另研究**：scene object、host override 多 hash、远端 prefab 尚未就绪、可见性变化、断线与关服、跨场景存活、便利生成入口。source 中确有不同分支，不能用常规动态对象表格替代。[16～19]
- **可迁移**：拆开“逻辑身份注销”和“物理实例复用”；按角色、入口、代际追踪责任；在对称命名接口下核实是否真的对称调用。
- **不可照搬**：`Destroy` 只是扩展点名字、`destroy` flag 在本地／消息中的具体传播、source prefab hash 规则及 host 自身消息排除都是 NGO 1.9.1 的机制，不是所有联机框架或资源系统的普遍规则。
- **不可照搬**：样例用 `activeInHierarchy` 寻找空闲、按需扩容，并没有因此成为有容量上限、借用代际、并发防重、完整业务重置的生产池。[20] 样例 companion 代码将 `HasHandler` 传给 Despawn 并在 false 时自行停用；本次未读其全部场景配置，不假定该字段总为何值。[21]

### B8. 独立判断练习与建议 oracle

**给学习者的题设**：host＋两个可见远端 client，或 dedicated server＋两个远端 client；同一动态炮弹 prefab，各端已注册同源 handler，无 override。server 一律手动 Get 后 `Spawn`。每个 handler 的 Destroy 做 Return；业务 `OnNetworkDespawn` 也做 Return。

1. 分别使用 `Despawn(true)`／`Despawn(false)`，先画出“每进程、每代实例”的获取／释放责任，指出哪里可能双还或漏还。
2. 若只看到 `OnNetworkDespawn` 已被调用，能否在这个回调中同步借出同一对象并 Spawn？请指出旧调用链后续仍读取什么。
3. 审核现有测试：一个名为“server／client shutdown 都调用 OnNetworkDespawn”的测试存在，是否就足够当作两端断言正确的 oracle？

> **note** — 建议 oracle（普通运行路径的静态预期；没有执行）
> - 以本题手动 Get＋Spawn 入口：authority 每个炮弹自己 Get 一次，handler `Instantiate` 不因这次公共 `Spawn` 再借出；每个可见远端 client 的生成链则各调用一次本地 handler。host 不应为其本地 client 再借出第二个实体。[15～18、20]
> - `Despawn(true)`：在映射有效、没有其他终止流程的正常路径，authority 及各远端实例均走各自 handler Destroy；同一实例的 `OnNetworkDespawn` 再 Return 是第二个归还点。[16、17、19]
> - `Despawn(false)`：authority 的正常释放分支不调用 handler；需要应用在公共调用返回后归还。本题为动态对象，远端收到的 DestroyGameObject 仍为 true，不能假定远端也跳过 handler。[16、19]
> - 在 `OnNetworkDespawn` 就立即发布／重用不具有“旧 NGO 流程已结束”的保证：后续还读取 NetworkObjectId／可见性，构造消息、置 IsSpawned、移除 registry、清 observers，之后才执行普通 handler 物理释放分支。[15、16]
> - 已读 `NetworkPrefabHandlerTests.NetworkPrefabHandlerClass` 直接调用内部 handler dispatch，检查实例、位置／旋转、移除注册及最后无剩余实例；其测试 handler 真正执行 Unity Destroy，并不是端到端池复用测试。[22]
> - 已读 `NetworkObjectOnNetworkDespawnTests.TestNetworkObjectDespawnOnShutdown` 确实有 Host／Server 两种 fixture，但 server shutdown 后第 109 行等待的仍是 **OnClientNetworkDespawnCalled**，没有改为 server 标记。client 标记前一步已满足，因此不能把该后半断言当作 server callback 的独立证明。这是静态可见的测试 oracle 缺口，不是本研究运行后发现的产品错误。[23]
> - 建议未来按 instance ID＋自定义 borrow generation 记录 Get／Spawn／OnNetworkDespawn／handler Destroy／Return；断言 free 集合中没有仍在 registry 的对象、同代发布为空闲至多一次、下一代不收到旧回调副作用。分别测试 true／false、host／server、重复终止、断线／shutdown、override、耗尽扩容与迟到消息；后几项不是本文已证实通过的条件。

## 四、主张晋升表：允许怎样写，不允许怎样写

| 主张 | 证据 | claim_status／允许措辞 | 禁止更强措辞／下一检查 |
|---|---|---|---|
| 两个案例冻结在实际可核查提交 | 01、13 | direct：REST ref、commit 元数据与 manifest 已读，一致 | 不能称最新推荐版本；未做构建重现或签名校验。 |
| UniTask suppress 的 canceled 分支跳过底层消费 | 04、05、07 | direct（控制流事实）＋inference（该组合不会执行已读归池路径） | 不能称测得内存 leak、确定内存不会释放；需引用链／生存期实验。 |
| 即时取消有不同完成与回收时序 | 03、04、07、08 | direct：registration 完成 core、特定 GetResult 分支跳过 TryReturn | “避免旧 runner 引用”只是研究者解释；不能把该解释当作者原话。 |
| 现有取消测试不足以证明回收 | 10、11 | direct：已读断言不检查回池／复用；不推广到全部测试仓库 | 不声称仓库根本没有其他测试；下一步是定点扩展生命周期断言。 |
| NGO true 可以归池，false 不保证各端保留行为相同 | 15～20 | direct：handler 分支与动态对象消息 flag 已读 | 只限具体对象种类、入口和常规路径；不覆盖所有场景／shutdown。 |
| host 获取不是天然“两端两次” | 15～18、20 | direct：手动 Get＋Spawn 链与发往自身生成消息的排除 | 不推广到 InstantiateAndSpawn；该入口已有反例分支。 |
| XML 默认值文字与公共签名冲突 | 15、17 | contradiction：本快照签名默认 true，XML 说 false | 应以实现与公共签名核对该版本，不概括所有官方文档不可信。 |
| 旧 server handler 问题有真实公开历史记录 | 24、25、17 | direct：报告、关联 PR、回复和当前后备分支存在 | 不声称已在冻结版复现旧故障，或独立验证修复。 |
| 关服测试 server 侧 oracle 有缺口 | 23 | direct：第二次等待检查了 client 标记 | 不声称所有 NGO server shutdown 都不回调。 |
| 两阶段回收／单一 Return owner 值得考虑 | A5、B6 的源码约束 | inference：研究者方案 | experiment_status=not-run；不写“生产已验证”“性能提升 X%”。 |

同仓多个文件用于核对一条调用链，不是多个独立重复实验。Issue、PR、README 分别提供现场报告、设计文字和公开契约，也不能合并成未发生的运行验证。

## 五、证据登记（本文件内唯一清单）

### 共同字段与权利约定

- 所有项访问日期：**2026-11-06**；所有项 **`experiment_status=not-run`**，并在各条显式重复。没有实验数据、通过率、benchmark 或用户访谈。
- `U`：UniTask 2.5.10／`7c0f199fe0d3fc528024488ccd671e6c7b27745b`，快照提交日 2024-10-03。`N`：NGO 1.9.1／`7d27c5141123e3b9f31419ccca7768a640a45d56`，快照提交日 2024-04-18。各源码项的“日期”是这一快照日期，**不是宣称文件最后修改日或功能引入日**。
- `MIT-U`：Copyright (c) 2019 Yoshifumi Kawai / Cysharp, Inc.，见 02。`MIT-N`：Copyright (c) 2021 Unity Technologies，见 14。若日后复制实质源码，应附相应版权及 MIT 许可全文；本笔记只作少量短引与中文分析，没有把第三方源码重许可。
- GitHub REST 元数据公开可读，不把这件事等同额外再分发授权。Issue／PR 正文及评论不自动继承源码 MIT：作者保留文本权利，本研究仅短引、链接、不复制图片、不访问 PR 中的非公开 Jira。
- 每条仅有一个很短的“摘录”字段，同一原始来源的摘录合计不超过 25 个英文词；函数标识与行号用于定位，不以大段代码替代分析。文件行号来自实际读取内容，网页可能因显示方式不同需按函数名复核。
- `read_status=read` 表示下面列出的范围已实际读过，不表示通读仓库；源码通过固定 raw URL 或官方 REST contents 的 base64 正文读取，Issue／PR 通过官方 REST 读取 title／body 等字段。**没有把仅搜索到的候选当正文证据**。

### UniTask 来源

#### ER-20261106-game-01 — Cysharp／UniTask：tag、commit、manifest 版本锚

- 类型／机构：官方仓库 GitHub REST 元数据＋package manifest／Cysharp。
- URL 与标题：[git ref tags/2.5.10](https://api.github.com/repos/Cysharp/UniTask/git/ref/tags/2.5.10)；[release commit](https://github.com/Cysharp/UniTask/commit/7c0f199fe0d3fc528024488ccd671e6c7b27745b)（读取接口：[git/commits](https://api.github.com/repos/Cysharp/UniTask/git/commits/7c0f199fe0d3fc528024488ccd671e6c7b27745b)）；[package.json](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/src/UniTask/Assets/Plugins/UniTask/package.json)。
- 日期／版本／定位：提交 2024-10-03T00:42:37Z；U；ref.object、commit.sha/date/message、manifest version/unity/license。
- 摘录：`"version": "2.5.10"`。
- 读取范围：ref JSON；commit 的 SHA、作者／提交者日期、message 字段；manifest 全文。支持版本锚，不支持编译兼容性。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：API 元数据公开；manifest MIT-U。

#### ER-20261106-game-02 — UniTask：LICENSE

- URL／标题：[LICENSE](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/LICENSE)。机构：Cysharp。
- 日期／版本／定位：2024-10-03 快照；U；版权、许可条件与免责声明。
- 摘录：`Copyright (c) 2019 Yoshifumi Kawai / Cysharp, Inc.`
- 读取范围：许可全文；确认软件和随附文档的 MIT 条款，不推定覆盖独立 Issue 评论。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U，保留版权及许可要求。

#### ER-20261106-game-03 — UniTask：README 官方取消／PlayerLoop／池化契约

- URL／标题：[README.md](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/README.md)。机构：Cysharp。
- 日期／版本：2024-10-03 快照；U。
- 定位／重点读取范围：L143–159 基础／最低 Unity；L201–209 单次消费约束；L327–350 suppress 与即时取消成本；L478–602 PlayerLoop；L981–1004 测试和 Editor 限制；L1053–1066 Pooling Configuration。另读关键词相邻上下文，未通读 1159 行全文。
- 摘录：`heavier than checking CancellationToken on the player loop.`
- 支持：作者公开契约与理由；限制：README 中性能措辞不是本研究 benchmark。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U。

#### ER-20261106-game-04 — UniTask：UniTask.Delay.cs

- URL／标题：[Runtime/UniTask.Delay.cs](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/src/UniTask/Assets/Plugins/UniTask/Runtime/UniTask.Delay.cs)。机构：Cysharp。
- 日期／版本：2024-10-03 快照；U。
- 定位：L147–196 Delay 重载／类型分派；L698–828 `DelayPromise`，尤其 Create L722–755、GetResult L757–774、MoveNext L791–815、TryReturn L817–827。
- 摘录：`if (!(cancelImmediately && cancellationToken.IsCancellationRequested))`。
- 读取范围：L1–197、L691–890；其中上述 DelayPromise 全类已读。没有把 IgnoreTimeScale／Realtime 作为本案已完整分析的路径。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U。

#### ER-20261106-game-05 — UniTask：UniTask.cs 消费与取消包装

- URL／标题：[Runtime/UniTask.cs](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/src/UniTask/Assets/Plugins/UniTask/Runtime/UniTask.cs)。机构：Cysharp。
- 日期／版本：2024-10-03 快照；U。
- 定位／重点读取范围：L68–74 非泛型 suppress；L169–208 `IsCanceledSource`；L290–363 非泛型 Awaiter；L468–535 泛型 suppress／source；L625–708 泛型 Awaiter，另读检索上下文。
- 摘录：`if (source.GetStatus(token) == UniTaskStatus.Canceled)`。
- 支持：取消分支绕过底层 GetResult、普通 awaiter 的消费分派；不直接证明运行时对象持续存活。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U。

#### ER-20261106-game-06 — UniTask：PlayerLoopHelper.AddAction

- URL／标题：[Runtime/PlayerLoopHelper.cs](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/src/UniTask/Assets/Plugins/UniTask/Runtime/PlayerLoopHelper.cs#L492-L505)。机构：Cysharp。
- 日期／版本／定位：2024-10-03 快照；U；L492–505 AddAction／无 timing 异常。
- 摘录：`runner.AddAction(action);`
- 读取范围：L485–516；未通读所有 PlayerLoop 注入逻辑。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U。

#### ER-20261106-game-07 — UniTask：PlayerLoopRunner

- URL／标题：[Runtime/Internal/PlayerLoopRunner.cs](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/src/UniTask/Assets/Plugins/UniTask/Runtime/Internal/PlayerLoopRunner.cs)。机构：Cysharp。
- 日期／版本／定位：2024-10-03 快照；U；AddAction L29–49、RunCore L157–257。
- 摘录：`if (!action.MoveNext())`。
- 读取范围：全文 260 行；核对 running 时等待队列、false／异常时去引用、压缩与队尾补入。未由此声称所有跨线程复用安全。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U。

#### ER-20261106-game-08 — UniTask：completion core

- URL／标题：[Runtime/UniTaskCompletionSource.cs](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/src/UniTask/Assets/Plugins/UniTask/Runtime/UniTaskCompletionSource.cs)。机构：Cysharp。
- 日期／版本：2024-10-03 快照；U。
- 定位／重点读取范围：`UniTaskCompletionSourceCore<TResult>.Reset` L85–99；TrySetCanceled L176–192；Version／GetStatus／GetResult L194–251；OnCompleted 前半 L259–291；另读接口／相邻上下文与自动重置源 L385–440，未通读 944 行全文。
- 摘录：`continuation(continuationState);`
- 支持：完成时可直接调用 continuation、GetResult 抛取消、Reset 增代；不支持任意高层调用自动切回主线程。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U。

#### ER-20261106-game-09 — UniTask：TaskPool

- URL／标题：[Runtime/TaskPool.cs](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/src/UniTask/Assets/Plugins/UniTask/Runtime/TaskPool.cs)。机构：Cysharp。
- 日期／版本／定位：2024-10-03 快照；U；SetMaxPoolSize／GetCacheSizeInfo；TryPop L80–100、TryPush L103–121。
- 摘录：`if (size < TaskPool.MaxPoolSize)`。
- 读取范围：全文 123 行；支持回池可能失败、缓存大小不是唯一生命周期 oracle。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U。

#### ER-20261106-game-10 — UniTask：AsyncTest 取消测试

- URL／标题：[Assets/Tests/AsyncTest.cs](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/src/UniTask/Assets/Tests/AsyncTest.cs#L303-L335)。机构：Cysharp。
- 日期／版本／定位：2024-10-03 快照；U；ExceptionlessCancellation L303–316、ExceptionCancellation L318–335。
- 摘录：`canceled.Should().Be(true);`
- 读取范围：两个完整测试及 Cancel／Pool／Suppress 关键词命中的邻近上下文；不是整个测试套件。测试对象为 DelayFrame，断言功能结果／帧差，不检查本案 DelayPromise 回池。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U。

#### ER-20261106-game-11 — UniTask：DelayTest

- URL／标题：[Assets/Tests/DelayTest.cs](https://github.com/Cysharp/UniTask/blob/7c0f199fe0d3fc528024488ccd671e6c7b27745b/src/UniTask/Assets/Tests/DelayTest.cs)。机构：Cysharp。
- 日期／版本／定位：2024-10-03 快照；U；DelayFrame L22–39、DelayFrameZero L42–56、DelayRealtime L194–207。
- 摘录：`Time.frameCount.Should().Be(frameCount + 1);`
- 读取范围：全文 220 行；只把断言作为已写测试意图，不声称帧数或时间区间实际通过。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-U。

#### ER-20261106-game-12 — UniTask Issue #661

- URL／标题：[DelayPromise Leaks when use SuppressCancellationThrow](https://github.com/Cysharp/UniTask/issues/661)；读取接口：[issue](https://api.github.com/repos/Cysharp/UniTask/issues/661)、[comments](https://api.github.com/repos/Cysharp/UniTask/issues/661/comments?per_page=100)。机构：Cysharp 官方仓库内公开用户报告，不是维护者设计声明。
- 日期／版本：2025-05-14T14:29:10Z 创建；2025-12-11T00:27:37Z 关闭／更新；报告未给精确包版本。2025-11-11 唯一已读评论来自 stale bot。
- 定位／摘录：正文 Problem；（公开版省略第三方原句：未确认再分发许可；保留证据 ID、来源定位与中文分析）
- 读取范围：REST title／body／日期／状态／closed_by／state_reason 与全部一条评论；未追踪全部事件历史。证实报告存在及机器人关闭，不证实运行 leak 或修复。
- 状态：`read_status=read`；`claim_status=direct`（报告／关闭记录），`unverified`（运行泄漏／修复）；`experiment_status=not-run`。许可：公开 Issue 作者文本，未推定 MIT，仅短引链接。

### Netcode for GameObjects 来源

#### ER-20261106-game-13 — Unity／NGO：tag、commit、manifest 版本锚

- URL／标题：[git ref ngo/1.9.1](https://api.github.com/repos/Unity-Technologies/com.unity.netcode.gameobjects/git/ref/tags/ngo/1.9.1)；[release commit](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/commit/7d27c5141123e3b9f31419ccca7768a640a45d56)（读取接口：[git/commits](https://api.github.com/repos/Unity-Technologies/com.unity.netcode.gameobjects/git/commits/7d27c5141123e3b9f31419ccca7768a640a45d56)）；[package.json](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/com.unity.netcode.gameobjects/package.json)。机构：Unity Technologies 官方仓库。
- 日期／版本／定位：提交 2024-04-18T16:34:14Z；N；ref.object、commit.sha/date/message、manifest version/unity/dependencies。
- 摘录：`"version": "1.9.1"`。
- 读取范围：ref JSON；commit 上述字段；manifest 全文；另读 tag 列表仅用于发现，不采用当前 tag 排序作版本依据。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：API 公开元数据；manifest MIT-N。

#### ER-20261106-game-14 — NGO：根目录与包内 LICENSE

- URL／标题：[根目录 LICENSE.md](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/LICENSE.md)；[包内 LICENSE.md](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/com.unity.netcode.gameobjects/LICENSE.md)。机构：Unity Technologies。
- 日期／版本／定位：2024-04-18 快照；N；版权、MIT 条款及免责声明。
- 摘录：`Copyright (c) 2021 Unity Technologies`。
- 读取范围：两份全文，文字同为 MIT；根目录许可用于核对 testproject 示例的仓库许可背景，不把示例冒充 package runtime。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-N；复制实质代码须保留声明与全文。

#### ER-20261106-game-15 — NGO：NetworkObject 公共入口

- URL／标题：[Runtime/Core/NetworkObject.cs](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/com.unity.netcode.gameobjects/Runtime/Core/NetworkObject.cs)。机构：Unity Technologies。
- 日期／版本：2024-04-18 快照；N。
- 定位／重点读取范围：SpawnInternal L761–782；Spawn／SpawnWithOwnership／Despawn L856–893；InvokeBehaviourNetworkDespawn L1387–1395；AddSceneObject L1857–1897，另读检索命中的相邻上下文与便利入口文档；未通读 2077 行全文。
- 摘录：`public void Despawn(bool destroy = true)`。
- 支持：真实默认值、server 权限、已有实例 Spawn、远端生成与生命周期通知。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-N。

#### ER-20261106-game-16 — NGO：NetworkSpawnManager

- URL／标题：[Runtime/Spawning/NetworkSpawnManager.cs](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/com.unity.netcode.gameobjects/Runtime/Spawning/NetworkSpawnManager.cs)。机构：Unity Technologies。
- 日期／版本：2024-04-18 快照；N。
- 定位：InstantiateAndSpawnNoParameterChecks L395–414；GetNetworkObjectToSpawn L420–484；CreateLocalNetworkObject 动态分支 L493–508；SpawnNetworkObjectLocallyCommon L648 起；SendSpawnCallForObject L756–770；DespawnObject L789–802；shutdown／场景释放 L840–929；OnDespawnObject L958–1075。
- 摘录：`DestroyGameObject = networkObject.IsSceneObject != false ? destroyGameObject : true`。
- 读取范围：以上核心分支、L614–732 的本地登记调用及检索上下文；L350–414、L740–774、L1038–1053 为证据缺口定点补读。未宣称通读整个 1135 行文件；已核读本案关键完整 OnDespawnObject。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-N。

#### ER-20261106-game-17 — NGO：NetworkPrefabHandler 与接口 XML 官方说明

- URL／标题：[Runtime/Spawning/NetworkPrefabHandler.cs](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/com.unity.netcode.gameobjects/Runtime/Spawning/NetworkPrefabHandler.cs)。机构：Unity Technologies。
- 日期／版本／定位：2024-04-18 快照；N；接口 Instantiate／Destroy XML L11–44；AddHandler L74–105；host hash 注册 L114–158；HandleNetworkPrefabSpawn L255–272、HandleNetworkPrefabDestroy L278–295。
- 摘录：`default destroy parameter (i.e. false)`。
- 读取范围：全文 425 行；摘录是本案指出的版本内文档冲突，不能作为公共默认值的正确契约。后备 source-hash handler 查找与物理释放委派有实际代码支持。
- 状态：`read_status=read`；`claim_status=direct`（实现／说明存在），`contradiction`（默认值文字）；`experiment_status=not-run`。许可：MIT-N。

#### ER-20261106-game-18 — NGO：CreateObjectMessage

- URL／标题：[Runtime/Messaging/Messages/CreateObjectMessage.cs](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/com.unity.netcode.gameobjects/Runtime/Messaging/Messages/CreateObjectMessage.cs)。机构：Unity Technologies。
- 日期／版本／定位：2024-04-18 快照；N；Deserialize L16–33、Handle L35–47、CreateObject L50–61。
- 摘录：`NetworkObject.AddSceneObject(sceneObject, networkVariableData, networkManager)`。
- 读取范围：全文 63 行；注意 prefab 未就绪／同步中的延迟处理，不把全部接收情况都化约为即时生成。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-N。

#### ER-20261106-game-19 — NGO：DestroyObjectMessage

- URL／标题：[Runtime/Messaging/Messages/DestroyObjectMessage.cs](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/com.unity.netcode.gameobjects/Runtime/Messaging/Messages/DestroyObjectMessage.cs)。机构：Unity Technologies。
- 日期／版本／定位：2024-04-18 快照；N；Deserialize L16–33；Handle L35–46。
- 摘录：`OnDespawnObject(networkObject, DestroyGameObject)`。
- 读取范围：全文 48 行；支持本地 flag 传播和未生成目标的 defer 分支，不是网络可靠性实验。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-N。

#### ER-20261106-game-20 — NGO 官方仓库：pool 示例

- URL／标题：[testproject/Assets/Samples/PrefabPool/NetworkPrefabHandlerObjectPool.cs](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/testproject/Assets/Samples/PrefabPool/NetworkPrefabHandlerObjectPool.cs)。机构：Unity Technologies；类型：官方仓库样例，**不是 package runtime 内建池**。
- 日期／版本／定位：2024-04-18 快照；N；OnNetworkSpawn L22–49；GetNextSpawnObject L57–68；Instantiate L70–77；Destroy L87–93；SpawnObjects L95–127。
- 摘录：`Host and Server spawn the objects`。
- 读取范围：全文 128 行；未打开其 Unity scene／prefab 配置，未验证运行，也未认为它实现了完整生产池协议。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-N（根目录许可见 14）。

#### ER-20261106-game-21 — NGO 官方样例：GenericPooledObjectBehaviour

- URL／标题：[testproject/Assets/Samples/PrefabPool/GenericPooledObjectBehaviour.cs](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/testproject/Assets/Samples/PrefabPool/GenericPooledObjectBehaviour.cs)。机构：Unity Technologies；类型：样例 companion。
- 日期／版本／定位：2024-04-18 快照；N；OnNetworkDespawn L35–57；OnNetworkSpawn L62–80；Update L133–165。
- 摘录：`NetworkObject.Despawn(HasHandler);`
- 读取范围：全文 186 行；只采用 HasHandler 条件分派与 false 时自行停用的源码事实，不推定实际场景中该字段赋值，也不把 0.12 秒可见性延迟当通用修复。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-N。

#### ER-20261106-game-22 — NGO：NetworkPrefabHandlerTests

- URL／标题：[Tests/Runtime/NetworkPrefabHandlerTests.cs](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/com.unity.netcode.gameobjects/Tests/Runtime/NetworkPrefabHandlerTests.cs)。机构：Unity Technologies。
- 日期／版本／定位：2024-04-18 快照；N；NetworkPrefabHandlerClass L88–174；测试 handler L206–239。
- 摘录：`Assert.False(networkPrefaInstanceHandler.StillHasInstances());`
- 读取范围：全文 240 行；其 handler 用 Unity Destroy，且直接调用内部 dispatch；不是“网络池借还跨端恰好一次”测试。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-N。

#### ER-20261106-game-23 — NGO：NetworkObjectOnNetworkDespawnTests

- URL／标题：[Tests/Runtime/NetworkObject/NetworkObjectOnNetworkDespawnTests.cs](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/blob/7d27c5141123e3b9f31419ccca7768a640a45d56/com.unity.netcode.gameobjects/Tests/Runtime/NetworkObject/NetworkObjectOnNetworkDespawnTests.cs)。机构：Unity Technologies。
- 日期／版本／定位：2024-04-18 快照；N；Host／Server fixture L13–15；TestNetworkObjectDespawnOnShutdown L76–111，尤其 L102–110。
- 摘录：`() => OnNetworkDespawnTestComponent.OnClientNetworkDespawnCalled`。
- 读取范围：全文 113 行；第 109 行是本案 oracle 审核发现，不声称已运行测试或证明产品漏回调。
- 状态：`read_status=read`；`claim_status=direct`；`experiment_status=not-run`。许可：MIT-N。

#### ER-20261106-game-24 — NGO Issue #990：历史 server handler 缺失

- URL／标题：[INetworkPrefabInstanceHandler not called on server](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/990)；读取接口：[issue](https://api.github.com/repos/Unity-Technologies/com.unity.netcode.gameobjects/issues/990)、[comments](https://api.github.com/repos/Unity-Technologies/com.unity.netcode.gameobjects/issues/990/comments?per_page=100)。机构：Unity 官方仓库；报告者 LukeStampfli，关联回复 NoelStephensUnity（REST 标为 MEMBER）。
- 日期／版本：创建 2021-07-28T11:22:16Z；关闭 2021-07-30T10:18:59Z；metadata 更新 2024-10-31；作者报告 MLAPI develop，**不是冻结 NGO 1.9.1 的实验**。
- 定位／摘录：[报告者关闭回复](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/990#issuecomment-889794522)；（公开版省略第三方原句：未确认再分发许可；保留证据 ID、来源定位与中文分析）。
- 读取范围：body／日期／状态与全部两条评论；正文中的截图未读。只把旧故障、hash 映射问题描述及关联修复记录作为历史证据。
- 状态：`read_status=read`；`claim_status=direct`（历史报告／回复），`unverified`（独立重现／修复实验）；`experiment_status=not-run`。许可：公开讨论作者文本，未推定 MIT，仅短引链接。

#### ER-20261106-game-25 — NGO PR #977：接口、host、XML 的公开设计说明

- URL／标题：[refactor!: NetworkPrefabHandler and INetworkPrefabInstanceHandler API & XmlDoc changes](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/pull/977)；读取接口：[pulls/977](https://api.github.com/repos/Unity-Technologies/com.unity.netcode.gameobjects/pulls/977)。机构：Unity Technologies 官方仓库。
- 日期／版本：2021-07-23T20:09:43Z 创建；2021-07-29T19:06:43Z merged。REST 实际返回 merge commit `d6b2a4864a79742c28afaaab02e46791dcb73270`，此处仅是历史元数据，不把它替代本案 N 快照。
- 定位／摘录：PR description 的接口命名理由；（公开版省略第三方原句：未确认再分发许可；保留证据 ID、来源定位与中文分析）
- 读取范围：title／body／created、updated、merged、merge_commit_sha、state 字段；未读全部 diff／review／提交链，不访问正文链接的 Jira。直接支持作者写过的目标，不证明完整方案比较或收益。
- 状态：`read_status=read`；`claim_status=direct`（设计文字）；`experiment_status=not-run`。许可：公开 PR 作者文本，未推定 MIT，仅短引链接。

### 访问失败，未用于证明正文

#### ER-20261106-game-26 — Unity Object-pooling 文档 URL（未读取正文）

- URL：[docs-multiplayer.unity3d.com/netcode/1.9.1/advanced-topics/object-pooling/](https://docs-multiplayer.unity3d.com/netcode/1.9.1/advanced-topics/object-pooling/)。机构：拟读取 Unity 官方文档站；类型：失败访问记录。
- 标题／日期／版本：仅按 URL 记为 object-pooling；页内标题、发布日期及实际正文版本均**未核验**。访问 2026-11-06；URL 带 1.9.1 不等于正文已冻结。
- 摘录：无。读取范围：无正文；WebFetch 返回无法验证域名安全。未换客户端重试或通过镜像取同页。
- 影响：不引用此页面内容；本案官方说明来自成功读取的固定源码 XML、官方仓库样例及公开 PR 描述。没有因访问失败降低其它已取得源码的 read_status，也没有假填文档证据。
- 状态：`read_status=access_failed`；`claim_status=unverified`；`experiment_status=not-run`。许可：正文未取得，未主张其转载授权。

## 六、交付边界

两个案例共同支持的判断训练原则是：**API 的结果或回调名字不能代替所有权证明；可复用的判据必须包含旧持有者已不再访问，以及唯一、按代际定义的归还责任。** 这属于由两条具体调用链抽出的研究者归纳，不是声称两个项目有同一产品缺陷。

未完成项仍然明确：没有编译／运行、性能或存活测量；没有作者确认 UniTask 分支意图；没有历史修复的独立回归；没有 NGO 复杂关服／场景／override 全路径证明；没有外部独立审阅或人工技术审核。本文可用于工程判断训练与后续验证设计，不是生产验收或已审核发布稿。

## 公开导出附注：第三方短引的 MIT 许可

以下许可仅适用于本文件中已登记 MIT 的 UniTask / NGO 源码与随附文档短引，不适用于 Issue、PR、论文或网页。许可身份沿用原研究记录，本次未联网重新核验。

Copyright (c) 2019 Yoshifumi Kawai / Cysharp, Inc.

Copyright (c) 2021 Unity Technologies

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
