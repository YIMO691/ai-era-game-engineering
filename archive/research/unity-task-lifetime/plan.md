---
title: 场景退出后的 Task 结果与资源归属：研究计划
topic_id: 20261105-unity-task-lifetime
created_at: 2026-11-05
publication_status: not-published
tags:
  - engineering-research
  - unity
---

# 场景退出后的 Task 结果与资源归属

## 问题卡

- Question：Unity 场景退出后，旧异步操作完成时，谁负责拒绝失效结果并释放其持有的资源？
- Type：applied。
- Hypothesis：取消请求不足以替代结果提交资格和资源所有权；需要由业务 owner 确定有效期，由交接协议确定失败与迟到结果的释放方。
- Why：排队恢复到主线程解决执行位置，不直接解决结果是否仍属于当前界面/场景。
- Current evidence：UnityCsReference 固定源码已取得；取消入口、同步上下文、对象判空、卸载绑定已定位。
- Missing evidence：Unity 与 .NET 官方网页正文访问受阻；Task 捕获上下文、取消协议、原生销毁时序未据此核验；无运行实验。
- Supports：源码取消入口与结果释放无绑定；队列条目无业务 owner；可构造“对象仍活但请求已被替代”的状态模型。
- Falsifies / revises：若目标底层 API 的契约已提供 owner 有效期与失败释放保证，应减少重复保护；若交接可重入或释放需特定线程，示意协议须修改，不能套通用 finally。
- Minimal next action：形成带来源限制的设计报告和教学草稿；分别审查并等待用户，不运行公司工程。
- Decision：read more 的必要证据当前受阻；完成可用草稿后 stop，保留补证行动。

## 范围

Unity 6000.0.85f2；UnityCsReference SHA `a189316266b40ba267ca77dddf88609ea6d769f9`（2026-11-03）。主要异步路径为 System.Threading.Tasks.Task，从 MonoBehaviour 主线程入口讨论。官方在线文档仅预期为 6000.0 系列，不等同补丁快照；本机未安装运行目标 Editor，不预设其实际 .NET runtime/profile。

非目标：Awaitable/UniTask/Addressables 全框架比较、性能排名、引擎原生完整实现、应用退出保证、完整并发库、生产代码交付、Phase 2 实验和 Phase 3 发布。

## 执行与停止条件

1. 查固定源码与官方材料；访问失败单列，不反复绕过安全校验。
2. 围绕“执行位置—提交资格—资源交接”综合，不逐篇摘要。
3. 比较仅判空、仅取消、资格检查+所有权协议；写明适用条件与反例。
4. 写独立报告与教学文章，共用 sources.md 与 topic_id。
5. 分开审核事实和可读性，修订可定位缺陷；结构/恢复检查通过后停 awaiting_review。

验收是文件化研究与写作工作流可用，不是 Unity 行为已验证。缺少官方契约的关键点不得通过 AI 审查假装补齐。下一阶段实验建议只记步骤与否定条件，不生成假数据或工程空树。
