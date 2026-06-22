# Topic Research Report Skill

`topic-research-report` is a bilingual research-report skill. Give it one topic, and it researches the topic online by default, then produces two Markdown reports:

- `调研报告-中文.md`
- `research-report-en.md`

The skill is designed for deep research, not slide outlines, video scripts, voiceover drafts, social posts, or search-result summaries.

## What It Does

- Turns a broad topic into a workable research question.
- Uses web research by default unless the user explicitly asks for offline or source-only work.
- Produces Chinese and English reports with matching facts, not line-by-line translation.
- Separates facts, interpretation, disputes, uncertainty, and evidence limits.
- Checks time-sensitive topics such as IPOs, listings, launches, financing, policy changes, and product releases against the current research date.
- Avoids common AI-sounding writing patterns and removes validation-style wording from the final report.

## Output Structure

By default, generated files are placed under:

```text
skill output/topic-research-report/<timestamp>-<topic>/
├── 调研报告-中文.md
└── research-report-en.md
```

## Usage

Create the output package:

```bash
python3 scripts/create_topic_package.py "SpaceX上市" --base "skill output/topic-research-report"
```

Then complete the research and fill both report files according to `SKILL.md` and the files in `references/`.

Validate the output:

```bash
python3 scripts/check_topic_outputs.py "skill output/topic-research-report/<timestamp>-<topic>"
```

## Repository Layout

```text
.
├── SKILL.md
├── README.md
├── references/
│   ├── human-writing-rules.md
│   ├── report-template.md
│   └── topic-research-framework.md
└── scripts/
    ├── check_topic_outputs.py
    └── create_topic_package.py
```

## Writing Rules

The skill intentionally avoids:

- generic AI-style openings and conclusions
- fake certainty
- unsupported numbers, dates, names, or quotes
- outdated forward-looking wording for events that already happened
- internal validation language such as "the report should" or "right framing is"
- personal style injection

The final report should read like a normal research report: title first, then body.
