---
title: 本课题第三方材料与许可说明
topic_id: 20261105-client-code-quality
created_at: 2026-11-05
publication_status: not-published
tags:
  - attribution
---

# 第三方材料与许可说明

本文件仅说明本课题实际使用的材料，不为第三方材料重新授权，也不是法律意见。来源、固定版本、阅读范围和访问限制见[来源登记](sources.md)。私有研究不等于取得任意再分发权；本题没有公开发布。

## .NET源码短引：MIT

[代码案例](unity-csharp-examples.md)R1含Queue.MoveNext必要短引。来源：.NET Foundation and Contributors，dotnet/runtime，SHA `4f4cbe49cc5ef3ecfb4c67ef7aa7057bcf82391b`。

- [源码](https://github.com/dotnet/runtime/blob/4f4cbe49cc5ef3ecfb4c67ef7aa7057bcf82391b/src/libraries/System.Private.CoreLib/src/System/Collections/Generic/Queue.cs#L333-L345)
- [该快照LICENSE.TXT](https://github.com/dotnet/runtime/blob/4f4cbe49cc5ef3ecfb4c67ef7aa7057bcf82391b/LICENSE.TXT)

以下文本与实际读取的许可正文一致（排除文件尾空行的展示差异）：

```text
The MIT License (MIT)

Copyright (c) .NET Foundation and Contributors

All rights reserved.

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
```

## 官方文档转述与短引

CQ-01/02/03来自Microsoft的dotnet/docs固定原稿，逐条署名/链接见来源登记。根文档LICENSE标识CC BY 4.0，代码另有LICENSE-CODE；本题对文档作中文转述、必要短引与综合分析，不把它们作为自己原创的官方结论。原稿内容没有被本研究修改；中文解释是本研究的表达，不是官方译文。

Framework Design Guidelines页面另有Microsoft/Pearson转载版权声明，不能仅凭仓库根许可就把书摘整体当成MIT自由复制。本题没有复制整章或书籍长段；只保留必要短摘录与定位。

## 仅链接分析的其他源码

- **Unity Graphics**：Unity Technologies，CQ-06，Unity Companion License，非MIT。本文分析指定RTHandle路径，不复制实现、不生成其派生补丁；不以本说明取代UCL及包内第三方通知。
- **MonoGame**：MonoGame Foundation，CQ-07，LICENSE.txt含Ms-PL及Mono.Xna MIT。本文保留固定链接和行为分析，不复制其源码；不能据此说整个MonoGame只有一种MIT许可。若未来分发源码，须重新核对对应文件、完整许可及notice义务。
- **Unity C# Reference**：CQ-08，Unity Reference-Only License，非MIT；本题不复制其实现，不将其作为可移植到其他产品的代码模板。

以上来源完整SHA与许可入口均登记在sources.md；网页许可文本的访问日期不等于仓库固定快照日期。许可核查范围有限，不承诺完整产品法律审计。

## 未取得的书籍原文与原创教学示例

CQ-09–12的原文候选访问失败，CQ-13未取得合法原文；没有从它们复制书籍内容，书名不构成已阅读证据或开放许可。

T1–T7为本课题原创教学片段，不是生产工程或上述项目的源码。它们仍须满足各自前提并完成目标环境验证；原创并不表示可直接上线。本课题不将既有公开仓库的许可证自动扩展到整个私人Vault。
