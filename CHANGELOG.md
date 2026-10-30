# 变更记录

## 2026-10-30 — 区分项目宗旨与研究报告

- 按用户提供的完整原文新增[项目宗旨与研究纲领](docs/project-manifesto.md)，不从旧报告重新编写宗旨，也不改变原文观点和参考资料。
- 两份原始研究报告的内容、路径及导入清单保持不变；`docs/manifesto.md` 的旧路径保留，但入口明确标为原始深度研究报告，不再与正式宗旨混用。
- README、相关说明和 Obsidian 本地入口按“项目宗旨 → 研究报告 → 后续研究”明确角色；不新增能力框架、实验工程或大规模研究任务。
- 登记宗旨原文的版本和 SHA-256；宗旨包含的 7 条外部来源 URL 仅为原文提供的核验线索，本次没有独立访问或证实其内容。
- 扩展检查器的必备文件与首页导航要求，同时保留旧报告入口；先观察到新增两项测试因缺少要求而失败，再补齐检查配置。
- 实际执行 `python -I -m unittest discover -s tests -p 'test_*.py' -v`：25 项通过，退出码 0；`python -I scripts/check_docs.py` 与 `git diff --check` 均通过。
- 新宗旨与用户输入逐字节一致；两份旧报告及原导入清单与已有 Git 提交完全一致。Obsidian 本地入口 11 个目标文件存在，但阅读视图和本轮 GitHub 渲染未验证。
- 本条记录本轮发布前的本地验证；发布后的远端检查以对应提交的 [Actions 运行](https://github.com/YIMO691/ai-era-game-engineering/actions)为准，不沿用旧提交的 CI 结果。

## 2026-10-29 — 初始研究基础

### 本地文档建设已完成

- 建立[首页](README.md)、[研究方法](docs/research-method.md)、[路线图](docs/roadmap.md)和[贡献指南](CONTRIBUTING.md)，让问题、证据、验证与修订形成最小研究闭环。
- 为两份已保真导入的报告补充[导入说明](docs/import-notes.md)，明确四级思想基线、五级历史草稿与未核验证据的边界。
- 建立[来源登记及核查队列](research/sources.md)，只登记已知材料和待核查主张，不冒充真实外部参考文献。
- 增加 [Obsidian 阅读说明](docs/obsidian.md)与仓库外的本地导航入口，共用一份正文，不复制私有笔记库。
- 本批原创文档由 AI 辅助整理；这不代表导入报告的来源、事实或研究过程已获人工核验。

### 检查与研究状态

- 在 Windows / Python 3.14.6 下实际执行 `python -I -m unittest discover -s tests -p 'test_*.py' -v`：23 项测试通过，退出码 0；实现前曾运行同批测试并观察到检查器缺失导致的失败。
- 实际执行 `python -I scripts/check_docs.py`：退出码 0；必备文件、约定范围内 Markdown、仓库内链接和 README 导航通过，两份导入件字节数及 SHA-256 与记录一致。
- 增加同命令的只读权限 GitHub Actions，官方依赖固定到完整提交 SHA；工作流存在不代表运行成功，具体提交的运行结果见 [Actions](https://github.com/YIMO691/ai-era-game-engineering/actions)。
- 公开仓库已真实创建并推送，默认分支为 `main`，描述及 6 个主题标签已配置；没有启用 Pages、第三方发布服务或额外高权限自动化。
- 初始提交 `a7e9c7f5299901e50003916fbc85e95d74151302` 的本地与远端 SHA 一致，两份 Git blob 原文校验通过；其 [Actions 运行](https://github.com/YIMO691/ai-era-game-engineering/actions/runs/40839002803)及两个检查步骤均为 success。本条记录该次运行，不替未来提交背书。
- 已读取 GitHub API 返回的 README HTML，核对标题、阅读表格与链接；本地 Obsidian 导航的 10 个目标文件均存在。这不是浏览器或 Obsidian 的视觉验收。
- Obsidian 阅读视图、浏览器视觉效果及原文 Mermaid 图形仍未验证。
- 来源恢复、独立事实核验和 Unity 实验尚未实施；没有本项目性能测量结果。
- 导入报告的 v1.0 是原报告标记，不是本项目的研究完成版本。
