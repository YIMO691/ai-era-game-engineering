---
title: Task 生命周期课题：共用来源登记
topic_id: 20261105-unity-task-lifetime
created_at: 2026-11-05
publication_status: not-published
tags:
  - engineering-research
  - evidence
---

# 共用来源与主张边界

访问日期均为 2026-11-05。报告与 Blog 共用此文件，不重复建立参考文献副本。以下四条源码均来自同一 Unity 仓库，是不同机制定位，不是四份独立交叉验证。官方网页正文未取得，跨来源契约核验尚未完成。没有实验结果。

## 已读固定源码

共同机构：Unity Technologies。版本：Unity 6000.0.85f2 C# reference source code，commit `a189316266b40ba267ca77dddf88609ea6d769f9`，提交日期 2026-11-03。类型 fixed-source；read_status=read；experiment_status=not-run。权利：文件头与 LICENSE.md 指向 Unity Reference-Only License，不是 MIT；原研究仅引用必要短片段与链接，未复制完整源码，未全文审核该许可网页；公开导出将下列四处源码短摘录改为行为转述，保留原文定位和权利限制。C# reference 不包含完整原生引擎实现。

### ER-20261105-unity-task-01 — MonoBehaviour 的取消入口

- [MonoBehaviour.bindings.cs L28–48](https://github.com/Unity-Technologies/UnityCsReference/blob/a189316266b40ba267ca77dddf88609ea6d769f9/Runtime/Export/Scripting/MonoBehaviour.bindings.cs#L28-L48)。已读范围：本轮直接读取前 100 行，关键核对 28–48；本记录不声称全部 API 已审计。
- 原摘录内容转述（公开导出不复制实现）：对象失效时抛出 MissingReferenceException；需要时创建 CancellationTokenSource；取消入口在已有 token source 时请求取消。
- direct：getter 懒建 CTS；已失效对象读取 getter 有异常分支；RaiseCancellation 调用 Cancel。
- inference：需要在对象有效时取得 token，不能在迟到 continuation 中才首次读取 getter。
- 不支持：原生何时调用 RaiseCancellation、与 OnDestroy 的精确顺序；Cancel 一定终止所有操作或释放所有结果。
- 本地获取文件 SHA-256：`dc8c50cea6122797e9a91fe5bacc33c0c122fe50b0510143d2549e56482203aa`。

### ER-20261105-unity-task-02 — UnitySynchronizationContext 的队列

- [UnitySynchronizationContext.cs](https://github.com/Unity-Technologies/UnityCsReference/blob/a189316266b40ba267ca77dddf88609ea6d769f9/Runtime/Export/Scripting/UnitySynchronizationContext.cs#L59-L115)。已读全文；重点 L59–90、97–115、143–166。
- 原摘录内容转述（公开导出不复制实现）：Post 把回调及其状态封装为工作请求并入队；Exec 依次调用工作请求；初始化时设置同步上下文。
- direct：Post 入队、Exec 调用、初始化设置上下文；WorkRequest 包含 callback、state、wait handle，没有业务场景 owner 字段。
- inference：投递到此队列与业务请求仍有效不是同一个条件；主线程执行位置不能独立充当业务有效期证明。
- 不支持：所有 Task await 必然经过此队列；后台入口和 ConfigureAwait(false) 仍回主线程；退出时所有队列必定排空。
- SHA-256：`87d2dad9f3eb998d2b2b2ddfbb8801c5a4df84e2924eeb8eddecbba2248d2510`。

### ER-20261105-unity-task-03 — Unity Object 有效性与 Destroy 绑定

- [UnityEngineObject.bindings.cs L118–178](https://github.com/Unity-Technologies/UnityCsReference/blob/a189316266b40ba267ca77dddf88609ea6d769f9/Runtime/Export/Scripting/UnityEngineObject.bindings.cs#L118-L178)；[L438–447](https://github.com/Unity-Technologies/UnityCsReference/blob/a189316266b40ba267ca77dddf88609ea6d769f9/Runtime/Export/Scripting/UnityEngineObject.bindings.cs#L438-L447)。已读范围 L115–204、390–449。
- 原摘录内容转述（公开导出不复制实现）：比较一侧为空的对象时，还会检查另一侧原生对象的存活状态；Destroy 的实现跨越原生绑定边界。
- direct：CompareBaseObjects 不只判断 CLR 引用是否为空；MonoBehaviour/ScriptableObject 在原生对象不存活的路径返回 false；Destroy 的核心实现位于原生边界。
- inference：对象有效性检查不能识别“对象仍在但请求已被新请求替代”；这属于业务状态问题。
- 不支持：精确原生销毁时点、每类资产的完整释放行为、所有判空写法完全等价。
- SHA-256：`9fa31f5a663294f6ef7bf59e816bac813bf47c1214eb790e83e173f2837fd0df`。

### ER-20261105-unity-task-04 — 场景卸载的托管/原生边界

- [SceneManager.bindings.cs](https://github.com/Unity-Technologies/UnityCsReference/blob/a189316266b40ba267ca77dddf88609ea6d769f9/Runtime/Export/SceneManager/SceneManager.bindings.cs#L24-L45)；L105–129。已读全文。
- 原摘录内容转述（公开导出不复制实现）：内部卸载入口声明为返回 AsyncOperation 的外部绑定；卸载包装转交给当前 SceneManagerAPI 的按名称或索引异步卸载入口。
- direct：此托管包装将卸载请求转给 API/原生绑定，返回 AsyncOperation。
- 不支持：读取此文件就能证明整个卸载调用链、原生销毁顺序或用户 Task/资源自动归属与清理。
- SHA-256：`f843e3c2b18e50647161a05dcf1cc606199be09379f893e1658370b8a6bd8742`。

## 正文访问失败：不是已读文献

以下为独立子任务实际请求记录。统一 read_status=access_failed、claim_status=unverified、experiment_status=not-run；无原文摘录。工具错误为 `Unable to verify if domain <域名> is safe to fetch. This may be due to network restrictions or enterprise security policies blocking claude.ai.`。不是观察到 HTTP 403，不代表网站不存在；未走其他通道绕过。

| ID | 机构、拟读主题与 URL | 版本粒度与待核验内容 |
|---|---|---|
| ER-20261105-unity-task-05 | Unity：[async-await support](https://docs.unity3d.com/6000.0/Documentation/Manual/async-await-support.html) | 6000.0 系列；Task continuation 与主线程条件 |
| ER-20261105-unity-task-06 | Unity：[destroyCancellationToken](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour-destroyCancellationToken.html) | 6000.0 系列；触发/缓存契约，不替代补丁源码 |
| ER-20261105-unity-task-07 | Unity：[Object.Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | 6000.0 系列；实际销毁时点 |
| ER-20261105-unity-task-08 | Unity：[UnloadSceneAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.UnloadSceneAsync.html) | 6000.0 系列；销毁对象与资产释放的区别 |
| ER-20261105-unity-task-09 | Microsoft：[Task cancellation](https://learn.microsoft.com/en-us/dotnet/standard/parallel-programming/task-cancellation) | 通用 .NET 指南；取消请求、终止与 Task 状态 |
| ER-20261105-unity-task-10 | Microsoft：[Task.ConfigureAwait](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.configureawait?view=net-8.0) | 拟读 net8 API 说明；不是 Unity 使用 .NET 8 的证据 |
| ER-20261105-unity-task-11 | Microsoft：[Cancellation in managed threads](https://learn.microsoft.com/en-us/dotnet/standard/threading/cancellation-in-managed-threads) | 通用 .NET 取消协议，不直接证明 Unity runtime 行为 |

OnDestroy 页面未请求，无正文证据；不增加一个“已失败访问”的虚构记录。一次 6000.0.0f1 标签查询出现 `error connecting to api.github.com`，该结果不证明标签不存在；随后查询固定 SHA 并获取上述源码成功。本题未采用该失败标签。

## 主张晋升表

| 主张 | 依据与类型 | 允许表述 | 禁止升级 | 不确定性与下一检查 | 决策 |
|---|---|---|---|---|---|
| token 取得应早于 owner 失效 | 01 direct + inference | 固定源码 getter 在 this==null 时抛异常，故提前取得 | token 能独立覆盖所有退出窗口 | 原生触发时点，待 06 正文与 Editor 验证 | keep |
| 主线程不等于请求有效 | 02、03 inference | 队列执行与业务有效期需分别论证 | 所有 Task 必回主线程、所有队列都有泄漏 | 捕获上下文条件待 05、10 | keep |
| 只取消不足以证明迟到结果安全 | 01、04 证据边界 + 设计反例 | 已读绑定未提供全链保证；协议必须处理未及时停止的结果 | 已实验证明 Unity 取消无效 | 实际 producer 契约待 09、11 与运行验证 | weaken |
| 交接前由接收协程释放，交接成功后由 owner 释放 | 01–04 不直接证明；本研究的设计提案 | 在独占结果、同步无重入交接等前提下提出协议 | Unity/API 官方保证、生产级已测方案 | 具体释放 API、线程、异常与共享 ownership 待补 | keep as proposal |
| 场景卸载自动释放一切 | 04 不支持；08 未读 | 目前证据不足，不能作此承诺 | 卸载必然取消 Task/释放全部资产 | 待官方契约及具体资源 API | discard |

## 后续补证优先级

先补 05、06、08、09、11 的合法可访问正文或用户提供的授权本地副本，定位具体条款；再核对 07、10 与 OnDestroy。未取得前保留缺口，不重复扩搜技术文章凑数。随后由用户决定是否进入独立 Unity 实验；本阶段不运行实验。
