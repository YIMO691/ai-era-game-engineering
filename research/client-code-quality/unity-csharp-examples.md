---
title: Unity/C# 代码质量：真实源码与教学对照
topic_id: 20261105-client-code-quality
created_at: 2026-11-05
status: static-analysis-not-runtime-verified
publication_status: not-published
tags:
  - unity
  - csharp
  - code-quality
---

# 真实源码与教学对照

**所有示例均未编译/未运行。** R为确实读过的固定源码案例；T为原创教学片段，不来自真实业务工程。Refactored表示待评估候选，不是上游已采用补丁或已证行为等价。片段省略using/类型/接线时明确说明，不能直接拼成可用Unity工程。共用[来源](sources.md)；仅必要.NET短引的MIT条件见[第三方声明](third-party-notices.md)。

## R1．Queue：重复不一定是同一种责任

**Original**：CQ-04，固定Queue.cs L194–235。Dequeue与TryDequeue都取头部、必要时清引用、推进索引并更新size/version，但空队列分别抛异常与返回false。MoveNext L333–345把回绕索引集中在一个小方法，原因注释提到作者环境的JIT判断。必要短引：

```csharp
// .NET Foundation and Contributors; MIT; see third-party-notices.md.
int tmp = index + 1;
if (tmp == _array.Length)
{
    tmp = 0;
}
index = tmp;
```

**Reading Issues**：要理解不变量，需一起读head/tail/size与引用清空；相似语句容易让审阅者冲动地“消除重复”。只按行数看不到两个公共API的失败契约。

**Refactored**：候选A保留两个入口与局部重复；候选B提取私有移除核心，但必须保持失败路径、引用清空、索引、version更新的时点，且让调用者仍能看清操作。另一种极短候选`index = (index + 1) % _array.Length`只能在合法容量/索引前提下讨论，不能因短就替换。

**Rationale**：提取应该共享同一不变量，而不是只共享几行形状。MoveNext是稳定的索引操作；把抛异常/返回false也混成布尔模式开关，可能使API契约更难追。

**Trade-offs**：重复有维护漂移风险，提取有跳转与异常路径隐藏成本；可能存在值得共用的核心，但没有证明值得改上游。作者性能注释表达原因，不是本研究对Unity/IL2CPP的基准结论。

**Verification**：静态定位已核对；候选未实现、未编译、未运行。需要空/非空/回绕/引用保留/枚举失效行为刻画及目标运行时测量；不能以阅读体验替代。

## R2．Select：短调用后面可以有必要复杂性

**Original**：CQ-05，Select.cs L13–105。入口按Iterator/IList/数组/List及优化选项分流，空数组有独立路径，部分路径构造迭代器；索引重载把入口校验和yield实现分开。完整原代码用固定链接阅读，不复制大段。

**Reading Issues**：调用者只需表达“映射”，实现维护者却必须理解输入形态、迭代状态和代码大小约束。两种阅读任务需要不同细节，不能给双方同一个“最佳函数长度”。

**Refactored**：候选A为求统一把所有分支改成单个yield循环；候选B保留实现特化，让业务调用者使用小而清晰的API。本研究不提交改动，优先保留上游边界，具体业务热点另评估T7。

**Rationale**：把必要复杂性藏在稳定契约后面可能合理；移除源码分支会改变实现策略，不是天然安全的美化。入口校验与延迟执行的拆分也可能承载行为时点，合并时必须核对。

**Trade-offs**：特化提高实现维护/测试负担；简单实现也许更适合低频自有工具。但不能据此断言特化让所有平台更快，或所有LINQ调用都有同样分配。

**Verification**：只读到所登记范围，未运行。没有Unity对照/吞吐/GC数据，不把当前dotnet/runtime主线视为Unity所用实现。

## R3．RTHandle：命名之外，必须读ownership契约

**Original**：CQ-06，Graphics固定RTHandleSystem.cs L1459–1478与RTHandle.cs L191–197、245–254。外部RenderTexture的Alloc默认不转移ownership；Release移除登记，仅ownership为真时请求销毁底层纹理，然后重置引用/标识。

**Reading Issues**：只看到`Alloc`、`Release`这两个名字，无法知道借用/接管差别；需要跟踪transferOwnership从入口到保存再到释放的流向。这里不复制Unity实现或写派生补丁。

**Refactored**：候选是调用方在自己的业务边界提供语义清楚的“借用外部目标/创建自有目标”入口，并在契约说明谁释放。不是把Graphics实现换成统一IDisposable，更不是所有Release都改成Destroy。若现有API调用已明确传命名参数并有一致团队惯例，可以不加包装。

**Rationale**：改进目标是降低调用者误判释放责任的概率，而非增加类型层数。具体GPU资源协议不能靠通用“资源句柄”标签证明。

**Trade-offs**：包装可能隐藏实际API/增调试跳转；过多Borrow/Own类也会增加接线成本。生命周期诊断需评估重绑定用法与版本兼容，不能预设更好。

**Verification**：关键源码与package.json已核对；包快照17.7.0，未确认目标编辑器兼容范围。未运行，不保证释放立即归还GPU内存。UCL不是MIT，详见来源权利边界。

## R4．MonoGame：短方法也能隐藏系统级时序

**Original**：CQ-07，GameComponentCollection.cs L31–99。Insert/单项Remove先改变集合后通知；Clear则逐项通知后再清空。EventHelpers L24–28同步调用处理器。禁止按索引替换，方法没有替组件调用Dispose。原代码仅通过固定链接阅读。

**Reading Issues**：只读方法名或每个小函数，看不出观察集合的事件处理器在不同操作中看到不同状态。名为“安全触发”的helper也只解决其注明的委托快照/判空问题，不等于处理异常/重入。

**Refactored**：若设计一个全新的自有集合，可以比较：明确禁止回调重入；快照后提交并通知；或保留当前通知时序并记录契约。对既有MonoGame直接先清空再通知，会改变可观察行为，不能称等价重构。

**Rationale**：系统协作质量要读提交点、事件时机与失败语义，不是只看函数是否小巧。静态推演：Clear处理器抛异常可能阻止最后清空，重入修改可能改变遍历观察；是否构成产品bug取决于调用者契约。

**Trade-offs**：快照增加保存/分配与陈旧视图问题；重入屏障限制用法；时序改变可能破坏兼容。增加catch会改变哪些订阅者执行、失败如何传播，也不是无风险补丁。

**Verification**：主线程核对两文件全文，未运行故障复现、未审计全部调用者；不把条件性风险宣布为已确认上游bug。不复制其Ms-PL源码到本文。

## T1．命名、函数与控制流：更清楚，但不必更多层

**Original（原创，普通C#片段）**：假定单线程、balance非负，参数/余额为整数单位。

```csharp
bool Handle(int x)
{
    if (x > 0)
    {
        if (_balance >= x)
        {
            _balance -= x;
            return true;
        }
    }
    return false;
}
```

**Reading Issues**：Handle/x不表达行为；嵌套把拒绝与状态提交夹在一起。这里只做扣减，没有发货/存档事务，不要从例子外推完整购买。

**Refactored（候选）**：

```csharp
bool TrySpendCoins(int amount)
{
    if (amount <= 0 || amount > _balance)
        return false;

    _balance -= amount;
    return true;
}
```

**Rationale**：意图/单位/拒绝条件/唯一写入点更直接；无需为两个条件再建Validator、Policy、Factory。若调用者需要区分金额非法/余额不足，可用受限结果类型，而非继续复用一个bool解释所有失败。

**Trade-offs**：假定balance非负、没有并发/回调插入；并发情况下两个调用可能竞态，改名不解决事务性。`Coins`是否必须写入每个局部变量名取决于上下文，不要求冗余前后缀。

**Verification**：未编译/未运行；候选意图保持示例行为。应比较负数、0、恰好余额、大于余额、连续扣减，确认余额不变/扣减次数；真实货币精度/溢出/线程协议另设计。

## T2．类职责与跨系统主流程：分责任，不分每一行

**Original（原创伪代码）**：一个Button回调同时取静态全局配置、请求网络、扣本地余额、发道具、改Text、记日志。依赖/提交/失败顺序散在多个`DoStepN`转发函数里。

**Reading Issues**：不了解场景状态就无法判断规则；网络失败后可能已扣本地状态；换View也要修改业务类。纯粹把回调拆成十个函数并不减少协议。

**Refactored（候选伪代码，不是可运行支付实现）**：

```text
View：收集用户意图；展示明确状态；不自作权威扣款。
Use case：校验请求 → 请求权威提交 → 接受结果 → 更新模型 → 通知展示。
规则函数：对给定配置/状态计算资格，不访问场景。
边界：提交接口说明幂等/重试/异常/取消与结果归属。
```

**Rationale**：区分View适配、规则判断、跨系统提交；保留Use case的主要顺序在一个可读位置。依赖由现有项目方式传入，不强制引入DI容器。

**Trade-offs**：新增接线与测试边界；20行无异步/外部提交的简单组件未必需要UseCase类。若既有框架已有owner/消息协议，应接入而非再造平行体系。服务器权威/离线策略不同，不能一套例子通吃。

**Verification**：仅职责方案，未实现/运行；需业务语义确认和正常/拒绝/断线/重复/半完成测试，不能标为行为保持重构或上线设计。

## T3．注释、格式与兼容：可见行为不止代码调用

**Original（原创片段）**：`[SerializeField] private float t; // 时间`。调用处无法确定单位/边界。另有`//这里不会分配`但未给版本/口径。

**Reading Issues**：字段名、注释都不够解释；想把t改名并移到普通对象时，可能改变Prefab/Scene持久化身份，不能只靠编译检查。

**Refactored（候选契约表达）**：选择清楚的`cooldownSeconds`；必要XML/注释说明计时基准、时间缩放/暂停约定和允许范围。公共方法如`StartCooldown(float durationSeconds)`，应说明何时开始、重复调用规则，而不是只写“开始冷却”。

**Rationale**：单位适合代码表达；为何用特定时间基准、兼容哪个版本适合注释。TODO应带问题引用或解除条件。格式沿项目约定，不把空格建议抢在生命周期问题前。

**Trade-offs**：字段名/布局迁移是行为兼容工作，需选目标Unity支持的迁移方法并加载原资产验证；这里没有实现迁移API。注释与代码同改，不能用长注释掩盖错误命名。

**Verification**：未编译/运行，未验证序列化迁移或任何“无分配”主张。应在授权独立工程加载原Prefab/Scene/存档，检查数值与引用；本轮没有这些结果。

## T4．抽象：两段相似代码未必共享一种知识

**Original（原创规则片段）**：

```csharp
bool CanBuy(int price, int coins) => price > 0 && coins >= price;
bool CanEnter(int minLevel, int level) => minLevel >= 0 && level >= minLevel;
```

**Reading Issues**：比较形状相似，但金额拒绝0、等级允许0，修改原因和未来变化也不同。把它们揉成`Check(int a, int b, bool allowZero)`会隐藏领域意图。

**Refactored（候选）**：保留两条业务规则，先改善参数/调用语境。若以后重复的是同一个定价协议，才考虑共享价格规则/配置快照。若已有两个外部提交提供者且契约稳定，可在提交边界设策略；不要把“比较大小”也提升为通用工厂层。

**Rationale**：DRY在本指南中的操作性解释是减少同一规则的多处权威，而非删除所有相似字符；这不是本轮已核验的书籍作者引文。

**Trade-offs**：重复的同一知识会漂移，保持重复并非普适答案。接口可隔离不稳定依赖；委托适合小能力；泛型适合真正相同算法；事件适合通知；工厂/装饰器需有创建/横切协议。成本包含导航、类型约束、初始化与调试，不只类数量。

**Verification**：未编译/运行；需对0、边界和真实变化需求比较。没有读者对照数据，不声称读起来一定快多少。

## T5．事件：把订阅期写成可审查协议

**Original（原创Unity形态片段）**：启用时`source.Changed += value => Refresh(value)`，停用时重新写`source.Changed -= value => Refresh(value)`，并允许source中途更换。

**Reading Issues**：不能依赖不同lambda表达式移除原处理器；publisher换了以后，还可能对错误实例退订。CQ-01的lambda建议本来就限定“不需要后来移除”的场景。

**Refactored（候选，省略ScoreSource定义/序列化接线；普通C# publisher、Action<int>事件，主线程串行且普通无回调event accessor）**：

```csharp
private ScoreSource _source;
private bool _listening;

public void Bind(ScoreSource source)
{
    Unsubscribe();
    _source = source;
    if (isActiveAndEnabled)
        Subscribe();
}

private void OnEnable() => Subscribe();
private void OnDisable() => Unsubscribe();
private void OnDestroy() => Unsubscribe();

private void Subscribe()
{
    if (_listening || _source == null)
        return;
    _source.Changed += Refresh;
    _listening = true;
}

private void Unsubscribe()
{
    if (!_listening)
        return;
    _source.Changed -= Refresh;
    _listening = false;
}
```

**Rationale**：保留处理器身份和原publisher，显式选择启用期订阅；替换前先解旧绑定，重复解除幂等。Refresh签名需匹配`void Refresh(int value)`；示例没有声明跨线程安全。

**Trade-offs**：额外标记/接线状态；自定义event accessor可重入/抛异常时需更强协议。若停用后仍需业务监听，应该用明确会话owner，而不是照搬OnDisable解绑。OnDestroy兜底不证明应用强杀也执行清理。

**Verification**：未编译/运行。需在目标Unity核对启用/停用/销毁/重绑定顺序、重复Bind、旧publisher触发与订阅计数；普通ScoreSource假设不适用于UnityEngine.Object publisher的失效判空。

## T6．异步：名称清楚还不够，必须标出结果交接

**Original（原创伪代码）**：`result = await LoadAsync(token); view.Show(result);`。变量名都漂亮，但未说明结果是否过期、谁观察异常、Show是否借用/接管/可能部分成功。

**Reading Issues**：await只连接控制流，不独立保证业务有效期或ownership。借用前题CQ-08的限定分析，不把其未核验网页/未运行方案升级为事实。

**Refactored（候选算法，RequestId/OwnedResult/Produce/IsCurrent/Adopt均为待实现契约，不是Unity API）**：

```csharp
async Task ReceiveAsync(RequestId id, CancellationToken token)
{
    OwnedResult pending = null;
    try
    {
        pending = await ProduceAsync(token);
        // 前提：这里已在owner线程，成功结果非null。
        if (token.IsCancellationRequested || !IsCurrent(id))
            return;
        AdoptWithoutCallbacks(pending);
        pending = null;
    }
    finally
    {
        pending?.Dispose();
    }
}
```

**Rationale**：成功交出后接收路径先负责；过期不提交仍需清理；只有接管成功才把责任转owner；异常由调用方观察，不按token状态武断吞掉其他来源取消。

**Trade-offs**：仅适用独占结果、检查到接管无await/重入、失败不部分接管、Dispose线程合法且不掩盖异常等条件。producer负责尚未交出资源；提前停止等待需另有迟到接收路径；永不完成/进程强杀不保证finally。共享资源改用其引用协议，不混同Dispose/Release/Destroy。

**Verification**：未编译/运行，未证明await后线程或目标producer取消契约。后续至少测A/B倒序、退出后成功、取消/异常、接管失败/成功后退出、释放次数与线程；当前只是设计推演。

## T7．性能与表达：先有相同任务，再谈候选成本

**Original（原创，Enemy为普通C#只读数据；不是可能销毁的Unity对象，读取属性无副作用；数组稳定且无null）**：

```csharp
int CountVisibleAlive(Enemy[] enemies) =>
    enemies.Count(enemy => enemy.IsAlive && enemy.IsVisible);
```

**Reading Issues**：表达简洁，但从语法不知道目标环境的委托/迭代器/扫描成本。CQ-05并不是此Count调用在Unity的实现证据，不能据Select源码给Count的分配数字。

**Refactored（候选）**：

```csharp
int CountVisibleAlive(Enemy[] enemies)
{
    int count = 0;
    for (int i = 0; i < enemies.Length; i++)
    {
        Enemy enemy = enemies[i];
        if (enemy.IsAlive && enemy.IsVisible)
            count++;
    }
    return count;
}
```

**Rationale**：显式扫描可作为热点优化候选，也保留易辨认的纯条件；不是因为for更“底层”就获胜。若每帧只为计数而反复重算，也可研究增量维护，但那会引入缓存一致性责任，不能无条件替换。

**Trade-offs**：候选更长，维护代价和差异可能不值得。闭包是否捕获、是否装箱、枚举静态类型、迭代器/异步状态机在何处创建、初始化/稳态、JIT/AOT/IL2CPP不同，均需具体核对。无null前提改变、属性有副作用或数组并发变化时要重新检查行为。

**Verification**：未编译/运行；无速度/GC数据。先比较输出，再在目标设备同输入/频率/构建/后端、预热和重复下测CPU、GC.Alloc、保留内存。若无稳定收益或非热点，保留更清楚的现有表达。

## 如何使用这些案例

先看Original并自己描述契约，再看候选。对每一项都允许最终选择“不改”。R案例证明的是某些源码事实和阅读任务，不证明某项目被我们审定为优秀；T案例展示推理，不是生产实现或学习效果证据。将一次真实练习的结果记入[训练记录](training-route.md)，再决定是否修订指南。
