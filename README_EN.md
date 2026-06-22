<p align="center">
  <a href="README.md">简体中文</a> · <a href="README_EN.md">English</a> · <a href="README_JA.md">日本語</a> · <a href="README_KO.md">한국어</a> · <a href="README_ES.md">Español</a>
</p>

<p align="center">
  <img src="assets/cover.png" alt="Topic Research Report Skill" width="100%">
</p>

# Topic Research Report

> Give it one topic. It researches online by default and produces two research reports without the usual AI flavor: one in Chinese and one in English.
>
> One topic in, two evidence-based bilingual research reports out.

This is a Skill for Claude Code / Codex. It does one job: turn a topic into a complete research report that can later be adapted by slide-generation, video-generation, or content-distribution systems.

It does not produce voiceover scripts, storyboards, slide outlines, social posts, or search-result summaries. Downstream systems can transform the report later. This skill focuses on the research itself.

## What It Solves

Many "research reports" read like pasted search results, or like an AI explaining how it is writing. This skill makes several constraints explicit:

- **Web research by default**: unless the user asks for offline work or source-only work, the agent must check real sources first.
- **Current-status checks for time-sensitive topics**: IPOs, listings, launches, financing, policy changes, and product releases cannot stay stuck in old announcement language.
- **Bilingual without rigid translation**: the Chinese and English reports match on facts, while each reads naturally in its own language.
- **No AI flavor**: avoids vague openings, mechanical summaries, customer-service tone, promo language, and validation-style wording.
- **Validation script included**: checks structure, source count, stale forward-looking wording, AI tells, and unwanted production-script content.

## Output

Default output directory:

```text
skill output/topic-research-report/<timestamp>-<topic>/
├── 调研报告-中文.md
└── research-report-en.md
```

The report structure includes:

- Background and Context
- Key Facts
- Timeline or Mechanism
- Deep Analysis
- Disputes and Uncertainties
- Implications and Watch Items
- Evidence Limits
- Sources

## Quick Start

Create the output package:

```bash
python3 scripts/create_topic_package.py "SpaceX IPO" --base "skill output/topic-research-report"
```

After researching and filling both reports, validate the output:

```bash
python3 scripts/check_topic_outputs.py "skill output/topic-research-report/<timestamp>-<topic>"
```

## Files

| Path | Purpose |
|---|---|
| `SKILL.md` | Main skill instructions, read first by the agent |
| `references/topic-research-framework.md` | Research framework and source rules |
| `references/human-writing-rules.md` | General rules for removing AI-sounding writing |
| `references/report-template.md` | Bilingual research-report template |
| `scripts/create_topic_package.py` | Creates the output directory and report files |
| `scripts/check_topic_outputs.py` | Validates the final output |

## Who It Is For

- People who need solid research material before making slides, videos, or content
- Teams that want downstream systems to adapt a report rather than invent the research
- Users who do not want search summaries, AI-style essays, or loose material packs
- Anyone working with time-sensitive topics such as listings, policies, product launches, and industry shifts

## Install

Place it in your Claude Code skills directory:

```bash
~/.claude/skills/topic-research-report
```

Or in your Codex skills directory:

```bash
~/.codex/skills/topic-research-report
```

## License

MIT

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=ai-martin-lau/topic-research-report&type=Date)](https://star-history.com/#ai-martin-lau/topic-research-report&Date)
