---
title: 代码质量研究：来源、主张与缺口
topic_id: 20261105-client-code-quality
created_at: 2026-11-05
publication_status: not-published
tags:
  - evidence
  - code-quality
---

# 来源、主张与证据边界

访问/复核日期：2026-11-05。正文用CQ-01等短别名，对应下列唯一的ER证据记录。read不等于实验验证；本题所有代码的experiment_status均为not-run，没有编译、Unity运行、性能或真实读者实验。引用用于限定事实/设计讨论，不证明某个仓库全局优秀或某种写法提高多少阅读效率。

## 官方规范与工具原稿

共同来源：Microsoft / dotnet/docs，main快照`951c3a5bdf253157f9b403e1f490bc42f5171fbc`，提交日期2026-11-04。直接从GitHub官方仓库读取文档原稿，不是仅读README或搜索片段。根LICENSE标识CC BY 4.0，LICENSE-CODE为Microsoft MIT；Framework Design Guidelines页面另有Pearson转载版权声明，不把它机械归为可任意复制的普通MIT内容。本文只必要短引/转述、署名链接，不复制书籍长段。

### ER-20261105-cq-01 / CQ-01 — Common C# code conventions

- [固定原稿](https://github.com/dotnet/docs/blob/951c3a5bdf253157f9b403e1f490bc42f5171fbc/docs/csharp/fundamentals/coding-style/coding-conventions.md#L12-L34)。页面ms.date=2025-01-15；read_status=read，实际读L1–190，重点12–34、42–54、166–174。
- 短摘录：“not an authoritative list”。
- direct：文档/示例规范为可适配约定；教学/采用新特性目标与runtime/compiler热路径目标不同；EditorConfig/分析器辅助实施约定；事件lambda建议限于不需移除的处理器。
- inference：Unity项目不能因其“官方”身份就照搬所有现代语法、性能偏好和事件写法。
- 不支持：所有团队都应采用某种var/行数风格，或者LINQ在Unity必然合适；本轮未读取嵌入外部snippet源文件，不能称其示例已编译。

### ER-20261105-cq-02 / CQ-02 — Overview of .NET source code analysis

- [固定原稿](https://github.com/dotnet/docs/blob/951c3a5bdf253157f9b403e1f490bc42f5171fbc/docs/fundamentals/code-analysis/overview.md#L12-L20)。页面ms.date=2025-11-05；read_status=read，实际读L1–160。
- 短摘录：“suggestion, warning, or error”。
- direct：Roslyn分析器按启用规则产生CA/IDE诊断和可配严重性；.NET SDK/目标框架/分析级别影响默认行为，SDK升级可能带来规则变化。
- inference：诊断覆盖的静态模式适合自动化，不等于对业务owner/整体架构的证明。
- 不支持：Unity项目默认等同.NET5+ SDK工程，所有StyleCop/Roslyn规则已安装可用；本轮未审计Roslyn实现或StyleCop项目许可/规则。

### ER-20261105-cq-03 / CQ-03 — Framework design guidelines

- [固定原稿](https://github.com/dotnet/docs/blob/951c3a5bdf253157f9b403e1f490bc42f5171fbc/docs/standard/design-guidelines/index.md#L14-L18)。页面ms.date=2008-10-22；read_status=read，实际读全文46行。
- 短摘录：“Some of the information in these guidelines may be out-of-date.”
- direct：目标是可复用.NET类库的统一编程模型与API易用性；建议需理解取舍；来源为2008年第二版书摘且页面明确部分可能过时。
- 不支持：本轮完整阅读其所有子页或新版书籍；所有API设计建议都可原样用作Unity业务组件规则。Pearson转载声明见原稿L43–45。

## 实际源码

### ER-20261105-cq-04 / CQ-04 — Queue<T>：不变量、重复与注释

- 机构：.NET Foundation and Contributors；dotnet/runtime main快照`4f4cbe49cc5ef3ecfb4c67ef7aa7057bcf82391b`，提交日期2026-11-05。
- [Queue.cs](https://github.com/dotnet/runtime/blob/4f4cbe49cc5ef3ecfb4c67ef7aa7057bcf82391b/src/libraries/System.Private.CoreLib/src/System/Collections/Generic/Queue.cs#L191-L235)；[MoveNext L333–345](https://github.com/dotnet/runtime/blob/4f4cbe49cc5ef3ecfb4c67ef7aa7057bcf82391b/src/libraries/System.Private.CoreLib/src/System/Collections/Generic/Queue.cs#L333-L345)。read_status=read，实际读L1–300、310–434，未宣称审计整个runtime。
- direct：Dequeue空队列抛异常，TryDequeue返回false；共同维护head/size/version与必要引用清空；MoveNext局部推进并回绕索引，注释解释分支替代取余的作者性能理由。
- inference：相似代码可有不同对外失败契约，不应只为消除重复强行统一；有用注释可承载机器环境相关理由。
- 不支持：注释已证明目标Unity/IL2CPP设备上取余一定更慢；复制最新runtime实现就适合旧Unity API/profile。
- 权利：已读LICENSE.TXT全文，MIT，版权.NET Foundation and Contributors；必要源码短引保留许可，见third-party-notices.md。

### ER-20261105-cq-05 / CQ-05 — Enumerable.Select：公共表达与内部特化

- 同一runtime SHA与机构；[Select.cs L13–105](https://github.com/dotnet/runtime/blob/4f4cbe49cc5ef3ecfb4c67ef7aa7057bcf82391b/src/libraries/System.Linq/src/System/Linq/Select.cs#L13-L105)。read_status=read，实际读L1–155。
- direct：有输入类型、IsSizeOptimized、数组空/非空、List等分支；部分分支构造迭代器；作者注释讨论native AOT泛型代码大小，索引重载将入口参数检查与yield迭代器分开。
- inference：一句“LINQ”不足以给成本结论；短公共调用可以封装内部复杂性，但维护者仍要理解具体实现与版本。
- 不支持：所有查询零分配/必分配固定字节；Unity使用相同LINQ实现；运行时优化必定消除某个new；源码条件分支不是设备测量。
- 权利：MIT，同CQ-04。04/05为同一仓库，不能说成两份独立实证。

### ER-20261105-cq-06 / CQ-06 — Graphics RTHandle：借用/接管/释放

- Unity Technologies；Graphics master快照`0efc28ea742b1966b9dd9cc4489e58b986a13faf`，提交日期2026-10-26。
- [RTHandle.cs L191–197、245–254](https://github.com/Unity-Technologies/Graphics/blob/0efc28ea742b1966b9dd9cc4489e58b986a13faf/Packages/com.unity.render-pipelines.core/Runtime/Textures/RTHandle.cs#L245-L254)；[RTHandleSystem.cs L1459–1478](https://github.com/Unity-Technologies/Graphics/blob/0efc28ea742b1966b9dd9cc4489e58b986a13faf/Packages/com.unity.render-pipelines.core/Runtime/Textures/RTHandleSystem.cs#L1459-L1478)。read_status=read；独立取证读取主文件及关联范围，主线程定点复核RTHandle L175–259、System L1450–1489。
- direct：RenderTexture的Alloc overload默认transferOwnership=false；SetRenderTexture保存ownership；Release先从owner登记移除，仅ownership=true时请求CoreUtils.Destroy，再清纹理引用/标识等状态。
- inference：资源类型、登记关系和底层资源释放责任是不同概念；不能把所有Release看成无条件销毁底层资源。
- 不支持：GPU内存立即归还、所有Dispose/Destroy/Release语义相同、此快照兼容6000.0.85f2。package.json实际为17.7.0，未声明unity字段；目标编辑器兼容范围未验证。
- 权利：主线程已读根与包LICENSE.md，Unity Companion License（非MIT）；定点读代理缓存的官网v1.4正文（2024-10-29）L203–221，涉及Unity配套用途、竞争分析限制、派生作品及notice条件；[许可入口](https://www.unity3d.com/legal/licenses/Unity_Companion_License)。网页不是固定commit内容。第三方通知由取证任务定点核查，不能概括为可删。工作区只链接/分析此源码，不复制或改写其实现，不对外分发派生补丁；这不是法律意见。

### ER-20261105-cq-07 / CQ-07 — MonoGame集合事件：短方法外的协议

- MonoGame Foundation；develop快照`76ed1c24f7dbe91421023c553978fa723548b22a`，提交日期2026-11-03。
- [GameComponentCollection.cs L31–99](https://github.com/MonoGame/MonoGame/blob/76ed1c24f7dbe91421023c553978fa723548b22a/MonoGame.Framework/GameComponentCollection.cs#L31-L99)；[EventHelpers.cs L24–28](https://github.com/MonoGame/MonoGame/blob/76ed1c24f7dbe91421023c553978fa723548b22a/MonoGame.Framework/EventHelpers.cs#L24-L28)。read_status=read；主线程读取两文件全文。
- direct：插入/单项删除先改集合再通知；Clear先逐项通知再清集合；禁止索引替换；事件helper判空后同步调用，无catch/重入屏障；这些方法没有调用组件Dispose。
- inference：Clear回调可观察到原集合；回调抛异常可能阻止最后清空；回调重入修改可能改变遍历观察。静态推演，不是已复现bug，也未核对所有外部调用者约束。
- 不支持：MonoGame整体设计错误；将Clear改成快照/先清空必然等价、更快或更好；移除必然释放组件。
- 权利：已读LICENSE.txt全文，含Ms-PL及Mono.Xna MIT；框架文件头有MonoGame版权；源码再分发需保留相关条款。工作区不复制其源码，只保留固定链接和行为分析。首次确切路径404后，一次tree定位成功；不能把前一404当API不存在。

### ER-20261105-cq-08 / CQ-08 — 既有Unity异步研究复用

- [前题来源登记](../unity-task-lifetime/sources.md)，本轮已重新读取；复用其01/02/03固定源码记录，不重新联网抓取已取得资料。
- UnityCsReference SHA`a189316266b40ba267ca77dddf88609ea6d769f9`，6000.0.85f2，2026-11-03；[MonoBehaviour token getter/取消入口](https://github.com/Unity-Technologies/UnityCsReference/blob/a189316266b40ba267ca77dddf88609ea6d769f9/Runtime/Export/Scripting/MonoBehaviour.bindings.cs#L28-L48)；[SynchronizationContext](https://github.com/Unity-Technologies/UnityCsReference/blob/a189316266b40ba267ca77dddf88609ea6d769f9/Runtime/Export/Scripting/UnitySynchronizationContext.cs#L59-L115)。read_status=read-reused；不是用户审核通过的实验结果。
- direct：getter失效对象异常分支、懒建CTS与Cancel入口、Post/Exec队列机制。
- inference：需要区分执行位置、业务请求有效期、结果ownership；不能仅靠await/token/判空替代全部协议。
- 不支持：官方网页契约已补齐、所有await回主线程、原生销毁的精确时序。前题访问失败不在本题重报为新尝试。
- 权利：Unity Reference-Only License，不是MIT；本题不复制其实现。

## 作者原文访问失败与未读书籍

独立取证任务实际尝试下列4个公开合法原文候选；WebFetch统一错误为`Unable to verify if domain … is safe to fetch`，提示可能有网络/企业策略限制。不是HTTP403结论；未绕过，也未用搜索片段/二手文章冒充正文。均read_status=access_failed、claim_status=unverified，无原文摘录，版权/版本页未核验。公开节选不等于开放再分发许可。

| ER ID（别名） | 作者、标题/候选URL | 实际读到与限制 |
|---|---|---|
| ER-20261105-cq-09（CQ-09） | John Ousterhout / Stanford，[A Philosophy of Software Design第二版节选候选](https://web.stanford.edu/~ouster/cgi-bin/aposd2ndEdExtract.pdf) | 0页；版本来自发现信息，未读版权页；不能引用具体深模块/短函数论证 |
| ER-20261105-cq-10（CQ-10） | Martin Fowler，[Definition Of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html) | 未读正文；不可伪装成此次已读作者定义 |
| ER-20261105-cq-11（CQ-11） | Martin Fowler，[Refactoring Boundary](https://martinfowler.com/bliki/RefactoringBoundary.html) | 未读正文；不声称已核对作者的行为边界 |
| ER-20261105-cq-12（CQ-12） | Hunt/Thomas / Pragmatic Bookshelf，[DRY节选候选](https://media.pragprog.com/titles/tpp20/dry.pdf) | 0页；20周年版来自发现信息，未读版权页/章节 |

CQ-13（任务输入记录，非已读证据）：Clean Code由任务书指定；本轮没有取得合法书籍原文，没有尝试付费访问，不填虚构URL/章节。四本经典均未完整阅读；本报告不按书名授权自己的综合建议，不给未经原文核验的引号或页码。

## 主张晋升与反证表

| 主张 | 证据/类别 | 允许说什么 | 不允许升级 | 可推翻/修订条件 |
|---|---|---|---|---|
| 规范应按项目目标适配 | 01/03 direct + synthesis | 官方原稿明确边界；据此反对无条件搬运 | 任何规范都不重要 | 已有团队硬约束优先，违反可能有真实成本 |
| 短函数/低指标不足以证明整体质量 | 04/07实例 + synthesis | 事件顺序/不变量仍需跨方法追踪 | 已实证长函数更易读 | 实际读者任务或需求变更显示提取有稳定收益 |
| ownership要作为协议表达 | 06/08机制 + synthesis | 借用/接管/释放和结果资格分别说明 | 所有资源都用同一模板即可安全 | 具体API已保障、或为共享/引用计数资源，应改方案 |
| 少量重复可能比错误抽象代价低 | 04差异 + design proposal | 按契约/变化原因决定，比较不改候选 | DRY错误、禁止接口/模式 | 重复知识反复同因变更且边界稳定时抽象可能合适 |
| LINQ成本需具体化 | 05 direct + boundary | 具体输入路径/运行时不同，需测量 | 任意LINQ一定GC/零GC或for一定快 | 目标版本/后端/负载测量形成限定结论 |
| 易懂/优雅降低理解成本 | 本研究操作性定义/待验证假设 | 用意图、跳转、解释错误、修改影响等观察讨论 | 已建立客观优雅分数或人类因果实证 | 控制熟悉度/任务后的读者测试可支持或推翻 |

## 后续最小补证

用户可提供合法授权书摘或在可访问环境下重新读取原网址，再逐条修订作者观点部分；不要从盗版/镜像补齐。随后选择一个真实但授权的修改任务验证指南，不自动访问业务工程。没有实际项目版本与设备预算前不制定普适性能禁令，不安装分析器来冒充完成研究。
