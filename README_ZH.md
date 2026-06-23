<p align="center">
  <a href="README.md">English</a> · <a href="README_ZH.md">简体中文</a> · <a href="README_JA.md">日本語</a> · <a href="README_KO.md">한국어</a> · <a href="README_ES.md">Español</a>
</p>

<p align="center">
  <img src="assets/cover.png" alt="Topic Research Report" width="100%">
</p>

# 话题深度调研报告 Skill

> 输入一个话题，默认联网调研，输出两份没有 AI 味的深度调研报告：中文一份，英文一份。

这是一个面向 Claude Code 和 Codex 的 Skill。它只做一件事：把一个话题调研成完整、可交付、可继续被 PPT 或视频系统二次加工的研究报告。

它不输出口播稿、分镜、PPT 页结构、公众号文章或搜索摘要。后续系统需要怎么改写，是后续系统的事；这个 skill 只负责把研究本身做扎实。

## 它解决了什么

很多“调研报告”看起来像搜索结果拼贴，或者像 AI 在解释自己怎么写。这个 skill 把几个关键约束固化下来：

- **默认联网调研**：除非用户明确要求离线或只用指定资料，否则必须先查真实来源。
- **状态型话题必须核对当前状态**：IPO、上市、发布、融资、政策生效等话题，不能停留在旧公告口径。
- **中英双语但不硬翻译**：两份报告事实一致，表达分别像中文和英文。
- **不写 AI 味**：避免空泛开头、机械总结、客服腔、宣传腔和“质检腔”。
- **有校验脚本**：检查章节、来源数量、过期前瞻词、AI 味表达和不该出现的制作稿内容。

## 输出

默认输出目录：

```text
skill output/topic-research-report/<timestamp>-<topic>/
├── 调研报告-中文.md
└── research-report-en.md
```

报告结构包括：

- 背景与问题
- 关键事实
- 时间线或机制链路
- 深度分析
- 争议与不确定性
- 影响与后续观察
- 证据边界
- 来源清单

## 快速开始

创建输出包：

```bash
python3 scripts/create_topic_package.py "SpaceX上市" --base "skill output/topic-research-report"
```

完成调研并填充两份报告后，运行校验：

```bash
python3 scripts/check_topic_outputs.py "skill output/topic-research-report/<timestamp>-<topic>"
```

## 文件说明

| 路径 | 作用 |
|---|---|
| `SKILL.md` | Skill 主说明，Agent 会先读这个 |
| `references/topic-research-framework.md` | 调研框架和来源原则 |
| `references/human-writing-rules.md` | 通用去 AI 味写作规则 |
| `references/report-template.md` | 中英双语研究报告模板 |
| `scripts/create_topic_package.py` | 创建输出目录和两份报告文件 |
| `scripts/check_topic_outputs.py` | 输出校验脚本 |

## 适合谁

- 需要把一个话题先做成扎实研究材料的人
- 想把调研报告交给后续 PPT 生成、视频生成或内容分发系统的人
- 不想要搜索摘要、AI 风格长文或半成品素材包的人
- 经常处理上市、政策、产品发布、行业变化等时效性话题的人

## 安装

放到 Claude Code skill 目录：

```bash
~/.claude/skills/topic-research-report
```

或放到 Codex skill 目录：

```bash
~/.codex/skills/topic-research-report
```

## License

MIT

## Star 趋势

[![Star 趋势图](https://api.star-history.com/svg?repos=ai-martin-lau/topic-research-report&type=Date)](https://star-history.com/#ai-martin-lau/topic-research-report&Date)
