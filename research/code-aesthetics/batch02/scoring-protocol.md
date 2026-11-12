---
title: Batch02 评分与可行性协议
created_at: 2026-11-11
version: "0.1-design"
status: draft-not-executed
experiment_status: not-run
audience: researchers-only
tags: [batch02, scoring, feasibility]
---

# 评分、预期验收与可行性协议

> [!WARNING]
> 公开研究草案：Batch01-B仍为PARTIAL，人工研究审核pending，代码／参与者实验未执行。公开提交授权不等于研究通过。
> 文内“未发布”、本地文件名、行号和检查点属于原研究时点；本页已作公开目录与链接适配，不是字节保真档案。当前阅读顺序与发布边界见[课题入口](../README.md)。


> [!WARNING] 研究者专用，尚未执行
> 本文含答案，不得发给参与者。所有轨迹是从17契约推导的**预期值**，不是测试日志；没有实验参与者、效果数据或通过率。协议尚未预注册、冻结或获招募授权。当前Batch01-B仍PARTIAL。

## 1. 设计和分配

- 首组`UI-LIFECYCLE-01`，同一人只看A或B，不交叉看同题。未来若获授权开展可行性试点，在参与者层面分配，目标两条件数量尽量接近；分配表在接触结果前生成并保存随机种子与方法，目前未生成。
- **共同说明、所分配版本代码和全部U题面首次同时展示，展示完成即启动U计时，没有不计时的预读阶段。** 之后按U→L→M逐阶段发放，任务之间无评分反馈；评价任务放最后。这样避免美感题直接启动“优美”目标，但前序任务可能训练后序任务。因此M的结果只适用于这条固定流程，不是首次接触代码的独立变更效应。
- 后测美感／可读性分别用1—7分：1=很不协调／很难读，4=中间程度，7=很协调／很易读；允许“不愿评价／无法判断”，不强制中点。问题与锚点统一，不出现“更优美版本”。单题仅探索，不称量表已经验证。
- 不允许AI或联网求解；允许阅读给定契约、伪代码及统一语法说明。对说明含糊只作程序性澄清，保存提问与答复，不提示算法；遇到设计歧义暂停该材料而不是给某一条件额外辅导。
- 评分者不获知预期胜方；代码结构无法完全盲化，不能声称双盲。理解／定位原答尽量匿名，修改验收按行为而非风格。两名评分者先独立评分，保存分歧后再裁决，不用AI自评替代真实评分一致性。
- 正式实验需要更多独立题材和不同变化类型；单组内U1—U3不是三个独立实验样本。

## 2. 理解与定位评分键

view字段顺序固定为`(visible, target, text, loading, error)`。

| 题目 | 预期答案／规则 | 评分 |
|---|---|---|
| U1 | q2后及q1后均为`(true,B,B-new,false,"")`；q1属于旧会话，被忽略 | 0—2 |
| U2 | q2失败后`(true,A,A-1,true,"")`，q3仍待完成；最终`(true,A,A-3,false,"")`，q3的重复结果忽略 | 0—2 |
| U3 | q1后`(true,A,"",true,"")`；q2失败后`(true,A,"",false,"load failed")`；同角色不恢复旧会话有效性 | 0—2 |
| L1 | epoch／open及Show/Close路径隔离会话；sequence／Refresh或Start隔离请求；pending在Complete或Take中只消费一次。须定位代码及解释作用 | 每组1分，共0—3 |

U每题：所有指定时点的五字段和理由均正确=2；至少一个完整时点正确但另一时点或理由错误／缺失，或所有状态正确但理由缺失=1；否则=0。可接受同义表示，不要求复述变量名作为U理由。未作答、拒答、技术缺失另记状态，不仅保留一个0；仅按预定义报告口径映射计分。

L每组只有定位和作用均正确才得1分。A可引用`Complete`，B可引用`RequestGate.Take`，不要求参与者接受提取边界的设计。定位到整个类但未指明对应状态／判断不算完整。

## 3. M1修改验收与诊断分

主要候选结果是**时间上限内最终提交是否满足全部必要契约**，而非代码是否类似参考实现。以下五个诊断项各0/1，不将4/5称“正确完成”：

1. 只对打开且pending的请求取消本地等待，并使当前票据失效。
2. 可见性、target、已有text和error均保持，loading=false。
3. 取消不发请求、不调用网络取消；无pending或关闭时无作用。
4. 取消后成功／失败／重复回包均不污染状态；之后Refresh仍可正常完成。
5. 所有原契约保持，包括Show重开、乱序、错误、关闭与重复终结规则。

**参考实现思路，不是唯一答案**：A在`open && pending`时把pending=false、view.loading=false；B可让gate新增`CancelPending()`返回是否确有待完成请求，若是则把pending=false，面板仅在返回true时关闭loading。下一次Start递增sequence，使旧票据不能被新pending重新激活。只清loading而不失效票据不合格；用Close代替取消也不合格。不要要求为了加功能必须抽象或必须内联。

没有可执行验收器时，只能给“纸面评分”，不能登记`execution_pass=true`；人工推演不能补造编译／运行通过。

## 4. 验收轨迹库草案

以下每条都从新实例开始；a/b为普通文本。`success(q,x)`、`fail(q)`是向指定票据投递结果。验收应记录**每一步**的view及累计请求target列表，而不只比较终点。预期值由共同契约独立定义，不从A运行输出复制成B的答案。

| ID | 事件序列／重点检查 | 契约预期（未执行） |
|---|---|---|
| T01 | 初始Refresh；Close；Close | 均隐藏空白，无请求 |
| T02 | Show(A)→q1；success(q1,a) | loading从true到false；显示a，恰一请求A |
| T03 | Show(A)→q1；Close；success(q1,a) | 关闭后保持初始显示，无额外请求 |
| T04 | Show(A)→q1；Close；Show(B)→q2；success(q2,b)；success(q1,a) | 最终B/b，q1不改任何字段 |
| T05 | Show(A)→q1；Show(A)→q2；success(q1,a)；success(q2,b) | 直接重开同角色也使q1无效；q1不关闭q2的loading |
| T06 | Show(A)→q1；success(q1,a)；Refresh→q2；Refresh→q3；fail(q2)；success(q3,b) | 旧失败不显示error、不关闭loading；最终b |
| T07 | Show(A)→q1；success(q1,a)；Refresh→q2；fail(q2) | 最终保留a，loading=false，error=load failed |
| T08 | Show(A)→q1；success(q1,a)；fail(q1)；success(q1,b) | 只接受第一次终结，保持a且无错误 |
| T09 | Show(A)→q1；fail(q1)；success(q1,a)；Refresh→q2；success(q2,b) | 第一次失败后重复成功被忽略；Refresh清error，q2可成功 |
| T10 | Show(A)→q1；CancelPending；success(q1,a)；fail(q1) | 保持可见A、空text／error，loading=false；只一请求 |
| T11 | Show(A)→q1；success(q1,a)；Refresh→q2；CancelPending；Refresh→q3；success(q2,b)；success(q3,c) | q2不能利用新的pending生效；最终c |
| T12 | 初始CancelPending；Show(A)→q1；fail(q1)；CancelPending；Close；CancelPending | 无pending时完全不变（包括错误）；关闭时仍隐藏，无额外请求 |
| T13 | Show(A)→q1；success(q1,a)；Refresh→q2；CancelPending；CancelPending；fail(q2) | 保留a、无错误、非loading；重复取消无作用 |

T01—T09用于基线A/B；M1必须保持T01—T09并满足T10—T13。它们不是充分的全空间证明。未来补充不同结果顺序、任意次数重复和重开组合的模型轨迹；禁止仅检查A=B而不检查契约。没有性能目标，不从这组测试声称性能等价。

## 5. 计时、失败与估计对象

- U计时包含共同说明和代码的首次阅读；L/M从各自新题面展示完成开始，到该阶段最终提交、退出或达到预先固定的上限结束。包含阅读、编辑及允许的本地验证，不含招募和设备设置。阶段间不得继续阅读或编辑，必要技术等待另记。U的计时只记录一次，不因U1—U3三条评分记录而重复累加；全流程观察投入为各阶段耗时之和并另报等待／中断。材料作者／验收制作投入另记，不能消失在总成本之外。
- U、L、M各有上限`tau_U/tau_L/tau_M`，**目前未定**。先用非效果评估的试读／可行性阶段校准，锁定后再收正式数据，不边看组间差异边改上限。
- 每阶段状态必须属于`submitted / timeout / withdrew / technical_error / not_started`之一。submitted另有correct/incorrect判定；超时可保存末版作诊断，但超时后完成不算限时成功。退出不是自动独立删失，也不强行填成超时。
- 首要报告是分配至各版本的全部人数、各状态人数和缺失原因；拟议操作性终点为“已分配者中限时提交且通过的比例”。获同意保留但未成功者在此终点记0，原状态仍保留；技术中断单列并作敏感性分析。此终点是研究流程下的成功概率，不是潜在维护能力。
- 因撤回同意而不得保留的个人数据按事先同意流程删除／不采集，不能为了ITT强留。可合法保留的匿名分配总数与缺失计数是否可用须在招募前明确；缺失结局报告上下界（全未成功／全成功），不作无依据插补或悄悄完整案例分析。
- 观察耗时按结果状态分别描述；成功者耗时明确是条件性统计。未完成者的观察终点不是正确完成所需时间，不把超时上限当完成时间，也不将退出按独立删失直接作生存推断。
- 可行性阶段不估“证明理论”的p值；正式方案若成立，主要比较可用限时成功率绝对差及区间。样本量须由有工程意义的差异、精度目标与试点噪声设计，当前不填人数／功效。多题扩展要处理参与者与题目聚类，偏好相关和经验交互只作预先说明的探索。

## 6. 最小数据字典（无数据行）

| 字段 | 类型／允许值 | 规则 |
|---|---|---|
| participant_id | 随机研究ID | 不含姓名、账号、公司或仓库路径 |
| consent_version | 文本 | 同意书版本；当前未建立／未收集 |
| assignment_id, variant | 文本；A/B | 保留分配方法与映射，评分副本用匿名码 |
| material_id, material_sha256, protocol_sha256 | 文本 | 使用实际发放副本hash，不仅是研究者母版hash |
| language_familiarity, callback_familiarity, ui_familiarity, pattern_familiarity | 各自0—4或missing | 0=无经验，1=学过未独立使用，2=偶尔使用，3=经常使用，4=长期排障／维护经验；探索性自报 |
| prior_exposure | yes/no/unknown | 看过A/B母版或答案则不可进入独立效果样本，可仅作材料反馈 |
| task_id | U1/U2/U3/L1/M1 | U阶段共享计时，不把每题拆出伪独立时间 |
| status, missing_reason | 上节枚举；文本 | 不以0分掩盖缺失类型 |
| started_at, ended_at, elapsed_ms, limit_ms | 时间与非负整数或missing | 使用同一单调时钟计耗时；技术异常保留原因，不事后猜填 |
| submitted_artifact_sha256 | hash或missing | 只保存本研究材料，不采集参与者私人代码 |
| score_rater1, score_rater2, score_final | U 0—2；L 0—3；M 0—5或missing | 原始评分、分歧与裁决分开保留 |
| contract_pass, execution_pass | true/false/not_run/missing | 纸面判断不等于execution_pass |
| help_count, help_log | 整数；文本 | 只记录任务相关帮助，不录屏或采系统日志 |
| beauty_rating, readability_rating | 1—7或missing | 后测、单题；不纳入正确性总分 |

招募前另定保存期限、访问者、撤回方式和删除流程并取得授权；本轮没有数据，不创建含虚构参与者的CSV。

## 7. 可行性门与停止规则

| 门 | 必须出现的真实证据 | 当前状态 |
|---|---|---|
| 材料可执行 | 固定C#版本、编译日志、两版对契约的逐轨迹结果 | 未执行；当前是伪代码 |
| 题面可用 | 非作者能理解符号／请求编号、无答案泄露 | 未执行；参与者副本尚未生成 |
| 评分可用 | 独立评分记录和分歧归因；必要时修订评分键 | 未执行；不声称一致性达标 |
| 时限可用 | 合法试读／可行性记录、无明显统一天花板或地板效应 | 未执行；时限未定 |
| 授权可用 | 招募、同意、隐私、资源和退出流程 | 未取得；不启动招募 |
| 确认性准备 | 更多独立材料、主终点、效应目标、样本量与缺失方案锁定 | 未完成 |

任一版本违约、评分答案依赖未写前提、旧回包轨迹遗漏、正式参与者看过答案或计时不可靠，先停止该材料的数据收集并升版修订，不以多收样本补救。若发现结果偏向A、B或无优势，均如实保留；不因不符合优美论而改题或排除参与者。

**当前结论**：已把问题变为可审查的设计草案，不是已验证实验材料。下一步优先实现共同契约验收并检查题面，不扩成AI横评或评分平台。

相关：[16_Batch02构念与测量草案](constructs.md) · [17_Batch02界面请求材料草案](ui-request-materials.md) · [15_Batch02研究启动条件](entry-gates.md)。
