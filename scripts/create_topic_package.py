#!/usr/bin/env python3
"""Create bilingual in-depth research report files for a topic."""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path


CN_REPORT_TEMPLATE = """# 深度调研报告：{topic}

直接从正文开始。第一段交代这个话题为什么值得研究、截至当前检索的状态是什么、报告的核心判断是什么。不要写用户原始话题、研究问题、目标读者、检索日期等表单字段。

第二段交代核心背景、关键矛盾和本文范围。检索日期放到文末证据边界中。

## 背景与问题


## 关键事实

### 事实 1：


### 事实 2：


### 事实 3：


## 时间线或机制链路

| 时间/阶段 | 事件/机制 | 为什么重要 | 来源 |
|---|---|---|---|
|  |  |  |  |

## 深度分析

### 分析 1：


### 分析 2：


### 分析 3：


## 争议与不确定性

| 问题 | 一种解释 | 另一种解释 | 当前判断 | 来源 |
|---|---|---|---|---|
|  |  |  |  |  |

## 影响与后续观察


## 证据边界

- 检索日期：{date}
- 已经比较可靠的信息：
- 仍不确定的信息：
- 来源薄弱处：
- 后续若继续加深应查：

## 来源清单

| 编号 | 来源 | 类型 | 用途 | URL |
|---|---|---|---|---|
| S1 |  | 一手/权威/二手 |  |  |
"""


EN_REPORT_TEMPLATE = """# In-Depth Research Report: {topic}

Start with the body. The first paragraph should state why the topic matters, what the verified current status is, and what the report argues. Do not write form fields such as original topic, research question, audience, or research date at the top.

The second paragraph should set the background, the main tension, and the scope. Put the research date in Evidence Limits near the end.

## Background and Context


## Key Facts

### Fact 1:


### Fact 2:


### Fact 3:


## Timeline or Mechanism

| Time/stage | Event/mechanism | Why it matters | Source |
|---|---|---|---|
|  |  |  |  |

## Deep Analysis

### Analysis 1:


### Analysis 2:


### Analysis 3:


## Disputes and Uncertainties

| Question | One explanation | Another explanation | Current judgment | Source |
|---|---|---|---|---|
|  |  |  |  |  |

## Implications and Watch Items


## Evidence Limits

- Research date: {date}
- Well-supported points:
- Uncertain points:
- Weak spots in sources:
- What to research next:

## Sources

| ID | Source | Type | Use | URL |
|---|---|---|---|---|
| S1 |  | primary/authoritative/secondary |  |  |
"""


FILES = {
    "调研报告-中文.md": CN_REPORT_TEMPLATE,
    "research-report-en.md": EN_REPORT_TEMPLATE,
}


def make_slug(topic: str) -> str:
    cleaned = re.sub(r"[\\/:*?\"<>|]+", "", topic).strip()
    cleaned = re.sub(r"\s+", "-", cleaned)
    return cleaned[:40] or "topic"


def write_file(path: Path, content: str, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"File exists: {path}. Use --force to overwrite.")
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create bilingual in-depth research report files for a topic.")
    parser.add_argument("topic", help="Topic to research")
    parser.add_argument("--base", default="skill output/topic-research-report", help="Base output directory")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    stamp = now.strftime("%Y%m%d-%H%M")
    out_dir = Path(args.base) / f"{stamp}-{make_slug(args.topic)}"
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"输出目录: {out_dir}")
    for filename, template in FILES.items():
        path = out_dir / filename
        write_file(path, template.format(topic=args.topic, date=date), args.force)
        print(f"{filename}: {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
