# AI Berkshire - Project Instructions

## Project overview

A value-investing research skill collection built on Claude Code. Four-master framework: Buffett, Munger, Duan Yongping, Li Lu.
GitHub: xbtlin/ai-berkshire

## Project structure

```
skills/          - investment-research skill definitions (.md), copied to ~/.claude/commands/ to use
tools/           - helper tools (financial_rigor.py for exact calculation)
reports/         - investment research report output
assets/          - images and other static resources
```

## Report directory structure

Every report is filed under a folder named after the **company**; all reports for a company live in that company's folder:

```
reports/
├── AI-industry-research/     - AI value-chain panorama research (pinned)
│   ├── AI-five-layer-cake-industry-panorama-20260605.md
│   └── AI-five-layer-cake-article-20260605.md
├── Tencent/                  - all Tencent research reports
│   ├── Tencent-research-20260408.md
│   ├── Tencent-earnings-2025Q4.md
│   ├── Tencent-management-20260409.md
│   └── Tencent-thesis.md
├── Pinduoduo/                - all Pinduoduo research reports
├── PopMart/                  - all Pop Mart research reports
├── nuclear-power-industry-20260409.md - industry reports go in the root
├── AI-compute-funnel-20260509.md      - funnel-screen reports go in the root
├── AI-rotation-call-20260509.md       - theme-level composite calls go in the root
├── portfolio-latest.md                - portfolio reports go in the root
└── multi-company-checklist-20260408.md - multi-company reports go in the root
```

## Report naming conventions

| Skill | File naming format | Example |
|------|---------|------|
| /berkshire-skill | `{Company}/` folder with each phase output + `{Company}-decision-{YYYYMMDD}.md` capstone | `reports/Pinduoduo/Pinduoduo-decision-20260408.md` |
| /investment-team | `{Company}/` folder with 4 perspectives + final report | `reports/Pinduoduo/final-report.md` |
| /investment-research | `{Company}-research-{YYYYMMDD}.md` | `reports/Tencent/Tencent-research-20260408.md` |
| /investment-checklist | `{Company}-checklist-{YYYYMMDD}.md` | `reports/Tencent/Tencent-checklist-20260408.md` |
| /industry-research | `{industry}-industry-{YYYYMMDD}.md` (root) | `reports/nuclear-power-industry-20260409.md` |
| /industry-funnel | `{industry}-funnel-{YYYYMMDD}.md` (root) | `reports/AI-compute-funnel-20260509.md` |
| /private-company-research | `{Company}-private-{YYYYMMDD}.md` | `reports/ByteDance/ByteDance-private-20260408.md` |
| /earnings-review | `{Company}-earnings-{period}.md` | `reports/Tencent/Tencent-earnings-2025Q4.md` |
| /earnings-team | `{Company}/` folder with 4 master perspectives + research draft + article + reader review | `reports/Tencent/Tencent-earnings-2025Q4.md` (article final) |
| /thesis-tracker | `{Company}-thesis.md` (long-lived) | `reports/Tencent/Tencent-thesis.md` |
| /portfolio-review | `portfolio-latest.md` (root, continuously updated) | `reports/portfolio-latest.md` |
| /management-deep-dive | `{Company}-management-{YYYYMMDD}.md` | `reports/Tencent/Tencent-management-20260409.md` |

## /investment-team file structure

```
reports/{Company}/
├── README.md                              - research-framework overview + core conclusion
├── 01-business-model-duan-yongping.md
├── 02-financials-valuation-buffett.md
├── 03-industry-competition-munger.md
├── 04-risk-management-li-lu.md
└── final-report.md                        - Team Lead synthesis report
```

## Core principles of investment analysis (highest priority)

- **Objective, objective, objective** - every analysis must rest on facts and data; subjective assertion is strictly forbidden.
- Strictly separate "fact" from "opinion": facts are backed by data, opinions must be explicitly labeled "opinion" or "speculation."
- **No preset stance**: do not decide bull or bear in advance. Lay out the data, then the logic, then the conclusion. The conclusion must fall naturally out of the data.
- Do not use subjective phrasing like "I think," "I feel," or "obviously"; use "the data shows," "the evidence indicates," or "according to source X" instead.
- **Show both sides**: every core judgment must carry a counter-argument ("but on the other hand ...") so the reader can weigh it.
- Be honest about uncertainty - say "uncertain" or "insufficient data" rather than filling certainty with guesses.
- Every skill (investment-team, investment-research, earnings-review, etc.) must follow these principles when it runs.

## Report language and style

- All reports are written in **English**.
- Style: direct, sharp, no filler.
- Data must be sourced; key figures cross-validated against at least 2 sources.
- Estimates must be marked "estimate."
- Ratings use the star glyph (1-5 stars), no half stars.
- Weave in commentary quotes from Buffett / Munger / Duan Yongping / Li Lu.

## GitHub operations

- Local clone path: `~/ai-berkshire/`
- Remote repo: `https://github.com/xbtlin/ai-berkshire.git`
- Before pushing, `git pull --rebase origin main` (the remote often has new commits).
- Write commit messages in English, describing clearly what changed.
- Do not push intermediate process files (e.g. data_collection.md); push only the final report.

## Common commands

```bash
# Push a report to GitHub
cd ~/ai-berkshire
git add reports/xxx.md
git commit -m "Add xxx report"
git pull --rebase origin main
git push origin main
```

## Notes

- Market cap must be re-computed by hand: share price x total shares, compared against the reported market cap.
- Currency units must be explicit (HKD / CNY / USD) to prevent mix-ups.
- Compute PE / ROE and similar metrics precisely with tools/financial_rigor.py.
- After finishing a report, proactively ask whether to push it to GitHub.
