<p align="center">
  <a href="README.md">English</a> · <a href="README_ZH.md">简体中文</a> · <a href="README_JA.md">日本語</a> · <a href="README_KO.md">한국어</a> · <a href="README_ES.md">Español</a>
</p>

# Topic Research Report

> 주제 하나를 입력하면 기본적으로 온라인 조사를 수행하고, AI 냄새를 줄인 심층 리서치 리포트 두 개를 생성합니다. 하나는 중국어, 하나는 영어입니다.
>
> One topic in, two evidence-based bilingual research reports out.

이것은 Claude Code / Codex용 Skill입니다. 역할은 하나입니다. 하나의 주제를 슬라이드 생성, 영상 생성, 콘텐츠 배포 같은 후속 시스템이 바로 활용할 수 있는 완성도 높은 리서치 리포트로 만드는 것입니다.

이 skill은 음성 원고, 스토리보드, 슬라이드 구성, SNS 글, 검색 결과 요약을 만들지 않습니다. 후속 변환은 다른 시스템이 맡고, 이 skill은 조사 자체에 집중합니다.

## 무엇을 해결하나

많은 "리서치 리포트"는 검색 결과를 붙여 놓은 것처럼 보이거나, AI가 자기 작성 과정을 설명하는 글처럼 보입니다. 이 skill은 다음 제약을 고정합니다:

- **기본값은 온라인 조사**: 사용자가 오프라인 또는 지정 자료만 사용하라고 명시하지 않으면 실제 출처를 먼저 확인합니다.
- **시점이 중요한 주제는 현재 상태 확인**: IPO, 상장, 출시, 자금 조달, 정책 변경, 제품 발표는 오래된 공지 표현에 머물지 않습니다.
- **직역이 아닌 이중 언어 출력**: 중국어와 영어 리포트는 사실이 일치하지만 각 언어에 맞게 자연스럽게 씁니다.
- **AI 냄새 제거**: 모호한 도입, 기계적인 결론, 고객센터 말투, 홍보 문체, 검수 메모 같은 표현을 피합니다.
- **검증 스크립트 포함**: 구조, 출처 수, 오래된 미래 표현, AI식 표현, 불필요한 제작 원고 요소를 검사합니다.

## 출력

기본 출력 위치:

```text
skill output/topic-research-report/<timestamp>-<topic>/
├── 调研报告-中文.md
└── research-report-en.md
```

리포트 구조:

- 배경과 문제
- 핵심 사실
- 타임라인 또는 메커니즘
- 심층 분석
- 쟁점과 불확실성
- 영향과 관찰 포인트
- 증거 범위
- 출처 목록

## 빠른 시작

출력 패키지 생성:

```bash
python3 scripts/create_topic_package.py "SpaceX IPO" --base "skill output/topic-research-report"
```

조사 후 두 리포트를 채운 다음 검증합니다:

```bash
python3 scripts/check_topic_outputs.py "skill output/topic-research-report/<timestamp>-<topic>"
```

## 파일

| 경로 | 역할 |
|---|---|
| `SKILL.md` | Agent가 먼저 읽는 메인 지침 |
| `references/topic-research-framework.md` | 조사 프레임워크와 출처 규칙 |
| `references/human-writing-rules.md` | AI스러운 문장을 줄이는 일반 규칙 |
| `references/report-template.md` | 이중 언어 리서치 리포트 템플릿 |
| `scripts/create_topic_package.py` | 출력 디렉터리와 리포트 파일 생성 |
| `scripts/check_topic_outputs.py` | 최종 출력 검증 |

## 누구에게 적합한가

- 슬라이드, 영상, 콘텐츠 제작 전에 탄탄한 조사 자료가 필요한 사람
- 후속 시스템이 조사를 새로 지어내지 않고 리포트를 변환하기를 원하는 팀
- 검색 요약, AI식 에세이, 느슨한 자료 묶음을 원하지 않는 사용자
- 상장, 정책, 제품 출시, 산업 변화 같은 시의성 있는 주제를 다루는 사람

## 설치

Claude Code skills 디렉터리에 배치:

```bash
~/.claude/skills/topic-research-report
```

또는 Codex skills 디렉터리에 배치:

```bash
~/.codex/skills/topic-research-report
```

## License

MIT

## 스타 히스토리

[![스타 히스토리 차트](https://api.star-history.com/svg?repos=ai-martin-lau/topic-research-report&type=Date)](https://star-history.com/#ai-martin-lau/topic-research-report&Date)
