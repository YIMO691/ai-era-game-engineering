# 变更记录

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
- GitHub 与 Obsidian 实际视觉渲染未验证；本条记录本地检查，不预先声明发布或远端 CI 通过。
- 来源恢复、独立事实核验和 Unity 实验尚未实施；没有本项目性能测量结果。
- 导入报告的 v1.0 是原报告标记，不是本项目的研究完成版本。
