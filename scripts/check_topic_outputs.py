#!/usr/bin/env python3
"""Validate bilingual in-depth research report files."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


CN_REPORT_REQUIRED = [
    "背景与问题",
    "关键事实",
    "时间线或机制链路",
    "深度分析",
    "争议与不确定性",
    "影响与后续观察",
    "证据边界",
    "来源清单",
]

EN_REPORT_REQUIRED = [
    "Background and Context",
    "Key Facts",
    "Timeline or Mechanism",
    "Deep Analysis",
    "Disputes and Uncertainties",
    "Implications and Watch Items",
    "Evidence Limits",
    "Sources",
]

AI_TELLS = [
    "值得注意的是",
    "不难发现",
    "众所周知",
    "显而易见",
    "综上所述",
    "由此可见",
    "在当今社会",
    "这意味着",
    "让我们深入",
    "希望对你有帮助",
    "delve",
    "tapestry",
    "testament",
    "pivotal",
    "intricate",
    "seamless",
    "robust",
    "moreover",
    "furthermore",
    "at its core",
    "fundamentally",
    "serves as",
    "stands as",
    "not only",
    "but also",
]

VALIDATION_VOICE = [
    "到 2026 年 6 月 22 日再看",
    "应写",
    "不能再写",
    "报告必须按",
    "合理表述是",
    "这点很重要，因为它决定报告",
    "no longer an offering arrangement",
    "the report should",
    "the report must",
    "should not describe",
    "right framing is",
    "write that public trading",
]

FORBIDDEN_PRODUCT_TERMS = [
    "PPT 页结构",
    "页面标题",
    "建议视觉",
    "口播稿",
    "分镜脚本",
    "屏幕文字",
    "voiceover script",
    "scene script",
    "on-screen text",
    "suggested slide structure",
]

FORBIDDEN_OPENING_TERMS = [
    "## 选题定义",
    "## 研究结论",
    "## 执行摘要",
    "用户原始话题",
    "本次研究问题",
    "研究范围：",
    "目标读者",
    "## Topic Definition",
    "## Main Findings",
    "## Executive Summary",
    "Original topic:",
    "Research question:",
    "Scope:",
    "Audience:",
]

EXPECTED_FILES = {
    "调研报告-中文.md": ("cn_report", CN_REPORT_REQUIRED),
    "research-report-en.md": ("en_report", EN_REPORT_REQUIRED),
}

FORBIDDEN_FILES = [
    "口播稿-中文.md",
    "voiceover-script-en.md",
]

MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}

STATUS_TERMS_CN = ("上市", "交易", "发布", "上线", "生效", "开盘", "收盘", "完成", "融资", "交付")
STATUS_TERMS_EN = (
    "ipo",
    "listed",
    "listing",
    "trade",
    "trading",
    "debut",
    "launch",
    "start",
    "begin",
    "effective",
    "priced",
    "closed",
    "completed",
)
CURRENT_MARKERS_CN = ("现在", "目前", "截至", "已经", "已于", "已开始", "已完成", "不是传闻")
CURRENT_MARKERS_EN = (
    "as of",
    "currently",
    "now",
    "no longer",
    "has begun",
    "began",
    "has started",
    "started",
    "has completed",
)


def read(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8")


def has_heading(content: str, heading: str) -> bool:
    pattern = rf"^#+\s+(?:\d+\.\s*)?{re.escape(heading)}(?:\s*/.*)?\s*$"
    return re.search(pattern, content, re.MULTILINE) is not None


def has_chinese(content: str) -> bool:
    return re.search(r"[\u4e00-\u9fff]", content) is not None


def has_english_words(content: str) -> bool:
    return re.search(r"\b[A-Za-z]{4,}\b", content) is not None


def ai_tell_hits(content: str) -> list[str]:
    hits: list[str] = []
    if "\u2014" in content or "\u2013" in content:
        hits.append("包含破折号字符")

    lowered = content.lower()
    for phrase in AI_TELLS:
        if phrase.lower() in lowered:
            hits.append(f"疑似 AI 味表达: {phrase}")
    return hits


def product_term_hits(content: str) -> list[str]:
    lowered = content.lower()
    hits: list[str] = []
    for term in FORBIDDEN_PRODUCT_TERMS:
        if term.lower() in lowered:
            hits.append(f"包含非调研报告导向内容: {term}")
    return hits


def opening_term_hits(content: str) -> list[str]:
    opening = "\n".join(content.splitlines()[:35])
    hits: list[str] = []
    for term in FORBIDDEN_OPENING_TERMS:
        if term in opening:
            hits.append(f"报告开头仍像表单: {term}")
    return hits


def validation_voice_hits(content: str) -> list[str]:
    lowered = content.lower()
    hits: list[str] = []
    for phrase in VALIDATION_VOICE:
        if phrase.lower() in lowered:
            hits.append(f"报告正文含写作校验腔: {phrase}")
    return hits


def placeholder_count(content: str) -> int:
    empty_fields = len(re.findall(r"[:：]\s*$", content, re.MULTILINE))
    empty_cells = content.count("|  |")
    bracket_placeholders = len(re.findall(r"\[[^\]]*(话题|Topic|Title|标题)[^\]]*\]", content))
    return empty_fields + empty_cells + bracket_placeholders


def make_date(year: int, month: int, day: int) -> date | None:
    try:
        return date(year, month, day)
    except ValueError:
        return None


def find_dates(text: str) -> list[date]:
    dates: list[date] = []
    numeric_pattern = re.compile(r"(\d{4})\s*(?:-|/|年)\s*(\d{1,2})\s*(?:-|/|月)\s*(\d{1,2})")
    for match in numeric_pattern.finditer(text):
        found = make_date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
        if found:
            dates.append(found)

    month_pattern = re.compile(
        r"\b("
        + "|".join(MONTHS)
        + r")\s+(\d{1,2}),\s*(\d{4})\b",
        re.IGNORECASE,
    )
    for match in month_pattern.finditer(text):
        found = make_date(int(match.group(3)), MONTHS[match.group(1).lower()], int(match.group(2)))
        if found:
            dates.append(found)
    return dates


def extract_research_date(content: str) -> date:
    for line in content.splitlines():
        if "检索日期" in line or "Research date" in line:
            dates = find_dates(line)
            if dates:
                return dates[0]
    return date.today()


def has_any(text: str, terms: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(term.lower() in lowered for term in terms)


def stale_expected_hits(content: str) -> list[str]:
    research_date = extract_research_date(content)
    hits: list[str] = []

    for lineno, line in enumerate(content.splitlines(), start=1):
        lowered = line.lower()
        has_forecast_term = (
            "预计" in line
            or "预期" in line
            or "估计" in line
            or "计划" in line
            or "将于" in line
            or "expected" in lowered
            or "scheduled to" in lowered
            or "slated to" in lowered
            or "planned to" in lowered
            or "will begin" in lowered
            or "will start" in lowered
            or "will trade" in lowered
            or "will list" in lowered
            or "will launch" in lowered
        )
        if not has_forecast_term:
            continue

        has_status_term = has_any(line, STATUS_TERMS_CN) or has_any(lowered, STATUS_TERMS_EN)
        if not has_status_term:
            continue

        has_current_marker = has_any(line, CURRENT_MARKERS_CN) or has_any(lowered, CURRENT_MARKERS_EN)
        line_dates = find_dates(line)
        has_past_event_date = any(found < research_date for found in line_dates)
        has_relative_next_day = (
            "预计第二天" in line
            or "计划第二天" in line
            or "expected to trade the next day" in lowered
            or "expected to begin trading the next day" in lowered
            or "expected to start trading the next day" in lowered
            or "scheduled to trade the next day" in lowered
            or "slated to trade the next day" in lowered
        )

        if has_current_marker or has_past_event_date or has_relative_next_day:
            hits.append(
                f"第 {lineno} 行含过期前瞻措辞。过去日期不能搭配预计、计划、expected、scheduled、will 等词；先核对截至检索日期的状态，再改成已发生/未确认/未发生。"
            )
    return hits


def validate_common(filename: str, content: str, required: list[str]) -> list[str]:
    errors: list[str] = []
    for heading in required:
        if not has_heading(content, heading):
            errors.append(f"{filename} 缺少章节: {heading}")

    errors.extend(f"{filename}: {hit}" for hit in ai_tell_hits(content))
    errors.extend(f"{filename}: {hit}" for hit in product_term_hits(content))
    errors.extend(f"{filename}: {hit}" for hit in opening_term_hits(content))
    errors.extend(f"{filename}: {hit}" for hit in validation_voice_hits(content))
    errors.extend(f"{filename}: {hit}" for hit in stale_expected_hits(content))

    if placeholder_count(content) > 10:
        errors.append(f"{filename} 仍有大量空占位内容。")
    return errors


def validate_language(filename: str, kind: str, content: str) -> list[str]:
    errors: list[str] = []
    if kind.startswith("cn") and not has_chinese(content):
        errors.append(f"{filename} 缺少中文正文。")
    if kind.startswith("en") and not has_english_words(content):
        errors.append(f"{filename} 缺少英文正文。")
    return errors


def validate_depth(filename: str, kind: str, content: str) -> list[str]:
    errors: list[str] = []
    source_limit_marked = any(
        marker in content.lower()
        for marker in ["公开资料有限", "来源有限", "public sources are limited", "sources are limited"]
    )
    if source_limit_marked:
        return errors

    if kind == "cn_report":
        chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", content))
        if chinese_chars < 1800:
            errors.append(f"{filename} 篇幅不足，不像深度调研报告；若资料有限，请在证据边界说明。")
    if kind == "en_report":
        words = len(re.findall(r"\b[A-Za-z][A-Za-z'-]*\b", content))
        if words < 900:
            errors.append(f"{filename} is too short for an in-depth research report; mark source limits if public material is thin.")
    return errors


def validate_sources(reports: list[str]) -> list[str]:
    combined = "\n".join(reports)
    urls = re.findall(r"https?://[^\s)）]+", combined)
    source_limit_marked = any(
        marker in combined.lower()
        for marker in ["公开资料有限", "来源有限", "public sources are limited", "sources are limited"]
    )
    if len(set(urls)) < 8 and not source_limit_marked:
        return ["调研报告来源 URL 少于 8 个；若公开来源不足，请在证据边界说明。"]
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description="Check bilingual in-depth topic research outputs.")
    parser.add_argument("output_dir", help="Directory containing bilingual research report files")
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    errors: list[str] = []
    report_contents: list[str] = []

    for forbidden in FORBIDDEN_FILES:
        if (out_dir / forbidden).exists():
            errors.append(f"不应再输出文件: {out_dir / forbidden}")

    for filename, (kind, required) in EXPECTED_FILES.items():
        path = out_dir / filename
        try:
            content = read(path)
        except FileNotFoundError:
            errors.append(f"缺少文件: {path}")
            continue

        errors.extend(validate_common(filename, content, required))
        errors.extend(validate_language(filename, kind, content))
        errors.extend(validate_depth(filename, kind, content))
        report_contents.append(content)

    if report_contents:
        errors.extend(validate_sources(report_contents))

    if errors:
        print("校验失败:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("校验通过: 两份深度调研报告结构完整，且通过基础去 AI 味检查。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
