---
title: Batch02 界面请求材料草案
created_at: 2026-11-11
version: "0.1-design"
material_id: UI-LIFECYCLE-01
status: draft-not-executed
experiment_status: not-run
tags: [batch02, research-material, lifecycle]
---

# 单组材料：界面请求、关闭与重开

> [!WARNING]
> 公开研究草案：Batch01-B仍为PARTIAL，人工研究审核pending，代码／参与者实验未执行。公开提交授权不等于研究通过。
> 文内“未发布”、本地文件名、行号和检查点属于原研究时点；本页已作公开目录与链接适配，不是字节保真档案。当前阅读顺序与发布边界见[课题入口](../README.md)。


> [!WARNING] 研究者母版，不可整份发给参与者
> 本文件包含A/B两份候选，正式发放时只给共同说明、一个匿名版本和当时任务；不得暴露另一版本、研究假设或18中的答案。伪代码未编译／未运行，行为等价尚未经验验收；不是可复制进Unity的生产代码。材料由本项目自行构造，不含公司工程或第三方代码，未对外发布或授予新许可。

## 1. 共同说明与符号

一个面板显示某个角色的数据。用户可以打开、刷新、关闭，再打开同一或另一角色。网络结果可能乱序或重复，也可能失败。面板只有一个当前实例；销毁视为终止使用该实例，旧实例不能被复用为新实例。

以下是C#风格**伪代码**：`Nat`为不会溢出的自然数，`Ticket`是不可变值；正式C#实现必须另选无碰撞身份策略或明确溢出防护。`None`为无值，`""`为空文本，赋值／成员访问按通常顺序执行。没有隐藏库行为。

- 全部公开调用和回调在同一UI事件队列串行执行，无重入。`Send`只登记请求，回调在当前方法返回后才会执行；它本身不抛异常。
- `Send(target, callback)`中的target被按值捕获；回调形如`callback(ok, text)`。`ok=true`表示成功，`false`表示失败。结果内容是普通文本，无可释放资源或外部副作用。
- 一个请求可不返回、返回一次或重复返回；第一次被接受的终结结果以后，同一票据的结果一律忽略，即使内容不同。
- 不实现网络取消、自动超时、重试、缓存、资源释放或线程切换。失效不是取消；这些是明确排除的生产问题，不声称已经解决。
- 唯一观察项：发出的请求及其target、每个事件结束后的显示状态`view=(visible, target, text, loading, error)`。不比较内部类数、票据数值或瞬间赋值顺序。

## 2. 共同契约

初始`view=(false, None, "", false, "")`，没有有效请求。

| 事件 | 必须满足的外部行为 |
|---|---|
| `Show(x)`，x为合法非空角色标识 | 无论之前是否打开，都开始新一代会话，显示x，清空旧文本／错误，进入loading并发出一个x请求 |
| 面板打开时`Refresh()` | 发出当前角色的新请求；旧请求立即失效；保留已显示文本，清空错误，loading=true |
| 面板关闭时`Refresh()` | 无请求、无状态变化 |
| `Close()`，包括重复关闭 | 全部现存票据失效；回到初始显示状态；不发请求 |
| 当前最新未完成票据成功 | 只接受一次；显示其text，loading=false，error清空 |
| 当前最新未完成票据失败 | 只接受一次；保留现有text，loading=false，error="load failed" |
| 旧会话、旧请求、关闭后或重复终结结果 | 完全忽略，不改变任何显示字段；不能关闭新请求的loading |
| 打开相同角色也算重开 | 旧会话不能因target相同而重新获得有效性 |

## 3. 版本A

```text
record Ticket(Nat epoch, Nat sequence, string target);

class Panel {
    bool open = false;
    bool pending = false;
    Nat epoch = 0;
    Nat sequence = 0;
    string target = None;
    View view = (false, None, "", false, "");

    void Show(string x) {
        epoch += 1;
        open = true;
        target = x;
        view = (true, x, "", false, "");
        Refresh();
    }

    void Refresh() {
        if (!open) return;
        sequence += 1;
        pending = true;
        Ticket ticket = new Ticket(epoch, sequence, target);
        view.loading = true;
        view.error = "";
        Send(ticket.target, (ok, text) => Complete(ticket, ok, text));
    }

    void Close() {
        epoch += 1;
        open = false;
        pending = false;
        target = None;
        view = (false, None, "", false, "");
    }

    void Complete(Ticket ticket, bool ok, string text) {
        if (!open || !pending || ticket.epoch != epoch
            || ticket.sequence != sequence || ticket.target != target) return;
        pending = false;
        view.loading = false;
        if (ok) {
            view.text = text;
            view.error = "";
        } else {
            view.error = "load failed";
        }
    }
}
```

## 4. 版本B

```text
record Ticket(Nat epoch, Nat sequence, string target);

class RequestGate {
    bool open = false;
    bool pending = false;
    Nat epoch = 0;
    Nat sequence = 0;
    string target = None;

    void Open(string x) {
        epoch += 1;
        open = true;
        target = x;
    }

    Ticket Start() {
        if (!open) return None;
        sequence += 1;
        pending = true;
        return new Ticket(epoch, sequence, target);
    }

    void Close() {
        epoch += 1;
        open = false;
        pending = false;
        target = None;
    }

    bool Take(Ticket ticket) {
        if (!open || !pending || ticket.epoch != epoch
            || ticket.sequence != sequence || ticket.target != target) return false;
        pending = false;
        return true;
    }
}

class Panel {
    RequestGate gate = new RequestGate();
    View view = (false, None, "", false, "");

    void Show(string x) {
        gate.Open(x);
        view = (true, x, "", false, "");
        Refresh();
    }

    void Refresh() {
        Ticket ticket = gate.Start();
        if (ticket == None) return;
        view.loading = true;
        view.error = "";
        Send(ticket.target, (ok, text) => Complete(ticket, ok, text));
    }

    void Close() {
        gate.Close();
        view = (false, None, "", false, "");
    }

    void Complete(Ticket ticket, bool ok, string text) {
        if (!gate.Take(ticket)) return;
        view.loading = false;
        if (ok) {
            view.text = text;
            view.error = "";
        } else {
            view.error = "load failed";
        }
    }
}
```

`RequestGate`是该面板内部专用对象，外部不能直接调用；`Open`和随后`Start`之间不存在回调或其他公开事件。A/B使用相同命名、契约和显示分支，主要差异是规则所在位置及调用间接性，不是算法或业务需求不同。

## 5. 分阶段题面（无答案）

每题从全新面板开始；`q1/q2`按实际发出请求的先后编号，不是角色标识。研究者逐阶段发放，不先展示后续题；作答期间不提供正确性反馈。

### U：行为理解

对每题写出指定时点的完整view，并说明哪些结果被接受或忽略及原因。

- **U1**：`Show("A")→q1; Close(); Show("B")→q2; q2成功("B-new"); q1成功("A-old")`。分别给出q2、q1回调后的状态。
- **U2**：`Show("A")→q1; q1成功("A-1"); Refresh()→q2; Refresh()→q3; q2失败; q3成功("A-3"); q3再次成功("A-duplicate")`。给出q2失败后的状态及最终状态。
- **U3**：`Show("A")→q1; Close(); Show("A")→q2; q1成功("old"); q2失败`。给出两个回调后的状态，并解释角色相同是否影响判断。

### L：规则定位

- **L1**：指出哪些状态、判断和失效路径共同确保旧回包不会改变当前显示；至少覆盖“关闭／重开”“连续刷新”“重复终结结果”。请定位具体字段与方法，不只写模式名称。

这是一道规则定位题，不要求声称基线存在缺陷。

### M：需求变更

- **M1**：增加`CancelPending()`。面板打开且有请求待完成时，停止本地等待并使该票据失效；保持面板可见、角色、现有文本和现有错误不变，只把loading改为false；不得调用网络取消或发出新请求。打开但无待完成请求时、关闭时均不做任何事。取消后的晚到结果必须忽略；随后`Refresh()`仍可正常发请求并接受结果。其余契约全部保持。
- 提交修改后的完整伪代码及最多五条说明／自测轨迹。不要求某种类数、方法名或设计模式；满足契约的不同实现均可接受。

## 6. 发放与冻结前检查

本母版保留A/B便于研究者比较；它不等于已隔离的参与者材料。正式发放前必须生成单版本、分阶段副本并人工检查不含另一版本／答案／wiki跳转。实际语言版本、IDE、显示布局、时间上限与匿名版本映射须固定并记录hash。

设计与局限：[16_Batch02构念与测量草案](constructs.md)。评分文档仅供研究者：[18_Batch02评分与可行性协议](scoring-protocol.md)，不得随题面发放。
