# 第 20 周任务卡 · Streamlit 界面、部署与作品集

**本周目标**：把现有的 Super PPT 命令行工具变成可操作、可下载、可展示的 Web 应用。

**最终输入**：

- 主题；
- 可选 Markdown/TXT 资料。

**最终输出**：

- 可下载的 `.pptx`；
- `.outline.json`；
- `.eval.json`；
- 页面上的评测摘要和错误说明。

| 天 | 内容 | 产出 |
|---|---|---|
| Day 100 | Streamlit 基础输入界面 | `day100_streamlit_basics.py` |
| Day 101 | 把生成逻辑重构成可复用函数 | `generator.py` + CLI 回归 |
| Day 102 | 接入界面、生成与下载 | `app.py` |
| Day 103 | 本地部署说明、作品集与最终验收 | 部署文档 + 作品集 |
| 收尾 | 助手整理（不占天数） | 周总结 + Git 收尾 |

---

## Day 100 · Streamlit 基础界面

**要做什么**：做一个只收集输入的页面，不调用 DeepSeek。

**页面内容**：

- 标题：Super PPT；
- 主题输入框；
- “使用文档”复选框；
- 勾选后显示 `.md` / `.txt` 文件上传框；
- “预览输入”按钮；
- 按钮点击后显示主题、模式、文件名和文件大小。

**验收**：

- 执行 `python -m streamlit run homework\week20\day100_streamlit_basics.py` 能打开页面；
- 主题为空时，预览后显示提示；
- 不勾选文档时显示“主题模式”；
- 勾选文档但未上传时显示提示；
- 上传文件后能显示文件名和大小；
- 全程不调用 API。

---

## Day 101 · 重构生成核心

**要做什么**：把 `ppt.py` 中的生成流程抽成可导入函数，避免 Streamlit 导入脚本时直接执行命令行逻辑。

**目标接口**：

```python
generate_presentation(topic, doc_path=None, output_dir=None)
```

**返回内容**：

```text
pptx 路径
outline 路径
eval 路径
评测报告
```

**验收**：

- `ppt.py` 命令行行为保持不变；
- 普通主题模式可调用；
- RAG 模式可调用；
- 评测失败能返回明确错误；
- 不依赖命令行 `sys.argv`。

---

## Day 102 · Streamlit 接入

**要做什么**：在 `app.py` 中连接界面和 `generate_presentation`。

**验收**：

- 无文档时生成普通 PPT；
- 有文档时生成 RAG PPT；
- 显示评测 `score` 和 `issues`；
- 提供 `.pptx` 下载按钮；
- 可查看大纲与评测 JSON；
- 异常显示用户能看懂的提示。

---

## Day 103 · 部署与作品集

**要做什么**：

- 补充 `streamlit` 依赖；
- 写清本地启动命令；
- 写清 Streamlit Community Cloud 的部署步骤；
- README 增加截图占位、功能、架构、评估和限制；
- 完成最终端到端测试。

**验收**：

- 新机器能按 README 安装并启动；
- API Key 不进入仓库；
- 本地页面可生成并下载 PPT；
- 部署文档能让别人复现；
- 作品集说明工具解决什么问题、如何评估。

---

## 收尾（助手负责，不占天数）

**当前结果（2026-11-26）**

| 项目 | 状态 |
|---|---|
| Day 100 输入界面 | 通过 |
| Day 101 生成核心重构 | 通过，CLI 回归成功 |
| Day 102 Streamlit 接入 | 通过，真实网页生成 `score=100` |
| Day 103 部署与作品集 | 通过 |
| Streamlit Community Cloud | 已上线 |

本地页面已验证：

- 空主题提示；
- 文档未上传提示；
- 真实普通主题生成成功；
- 显示 5 页、`score=100`、0 个问题；
- 提供 PPT、大纲和评测三个下载按钮；
- 本地服务返回 HTTP 200。

**公网应用**：
https://super-ppt-kpcvhtoahtitynwunugtvw.streamlit.app/

用户已在浏览器中完成打开、生成和下载验证，第 20 周通过。
