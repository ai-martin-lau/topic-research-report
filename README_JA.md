<p align="center">
  <a href="README.md">English</a> · <a href="README_ZH.md">简体中文</a> · <a href="README_JA.md">日本語</a> · <a href="README_KO.md">한국어</a> · <a href="README_ES.md">Español</a>
</p>

# Topic Research Report

> トピックを 1 つ入力すると、デフォルトでオンライン調査を行い、AI っぽさを抑えた深い調査レポートを中国語と英語で出力します。
>
> One topic in, two evidence-based bilingual research reports out.

これは Claude Code / Codex 向けの Skill です。役割は 1 つだけです。トピックを、スライド生成・動画生成・コンテンツ配信などの後工程で使える、完成度の高い調査レポートにすることです。

口播原稿、絵コンテ、スライド構成、SNS 投稿、検索結果の要約は作りません。後工程の変換は別のシステムに任せ、この skill は調査そのものに集中します。

## 何を解決するのか

多くの「調査レポート」は検索結果の貼り合わせか、AI が自分の書き方を説明している文章に見えます。この skill は次の制約を明確にします：

- **デフォルトでオンライン調査**：ユーザーがオフラインや指定資料のみを明示しない限り、まず実際のソースを確認します。
- **時系列が重要な話題は現在状態を確認**：IPO、上場、発表、資金調達、政策変更、製品リリースでは古い告知の表現に留まりません。
- **逐語訳ではないバイリンガル**：中国語版と英語版は事実をそろえ、それぞれ自然な文章にします。
- **AI っぽさを避ける**：曖昧な導入、機械的なまとめ、カスタマーサポート調、宣伝口調、検証メモのような表現を避けます。
- **検証スクリプト付き**：構成、ソース数、古い未来表現、AI っぽい表現、不要な制作稿要素をチェックします。

## 出力

デフォルトの出力先：

```text
skill output/topic-research-report/<timestamp>-<topic>/
├── 调研报告-中文.md
└── research-report-en.md
```

レポート構成：

- 背景と問題
- 重要事実
- タイムラインまたは仕組み
- 深掘り分析
- 争点と不確実性
- 影響と今後見るべき点
- 証拠の範囲
- ソース一覧

## クイックスタート

出力パッケージを作成：

```bash
python3 scripts/create_topic_package.py "SpaceX IPO" --base "skill output/topic-research-report"
```

調査して 2 つのレポートを埋めた後、検証します：

```bash
python3 scripts/check_topic_outputs.py "skill output/topic-research-report/<timestamp>-<topic>"
```

## ファイル

| パス | 役割 |
|---|---|
| `SKILL.md` | Agent が最初に読むメイン指示 |
| `references/topic-research-framework.md` | 調査フレームワークとソース規則 |
| `references/human-writing-rules.md` | AI っぽさを減らすための一般ルール |
| `references/report-template.md` | バイリンガル調査レポートのテンプレート |
| `scripts/create_topic_package.py` | 出力ディレクトリとレポートファイルを作成 |
| `scripts/check_topic_outputs.py` | 最終出力を検証 |

## 向いている人

- スライド、動画、コンテンツ制作の前に信頼できる調査材料が必要な人
- 後工程のシステムに、調査の発明ではなくレポートの変換を任せたい人
- 検索要約、AI 風の長文、雑な素材集を避けたい人
- 上場、政策、製品発表、業界変化など時効性の高い話題を扱う人

## インストール

Claude Code の skills ディレクトリに配置：

```bash
~/.claude/skills/topic-research-report
```

または Codex の skills ディレクトリに配置：

```bash
~/.codex/skills/topic-research-report
```

## License

MIT

## スター推移

[![スター推移グラフ](https://api.star-history.com/svg?repos=ai-martin-lau/topic-research-report&type=Date)](https://star-history.com/#ai-martin-lau/topic-research-report&Date)
