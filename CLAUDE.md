#AI Berkshire — Project Directive

## Project Overview

A collection of value investing research skills based on Claude Code. The Four Masters Framework: Buffett, Munger, Duan Yongping, and Li Lu.
GitHub: xbtlin/ai-berkshire

## Project structure

```
skills/ — Investment research Skill definition (.md), copy to ~/.claude/commands/ for use
tools/ — auxiliary tools (financial_rigor.py precise calculation)
reports/ — investment research report output
assets/ — static resources such as pictures
```

## Report directory structure

All reports are created in folders by **company name**, and all reports related to the company are placed in the corresponding folders:

```
reports/
├── AI Industry Research/ — Panoramic Research on AI Industry Chain (Top)
│ ├── AI five-layer cake-Industry Panoramic Research-20260605.md
│ └── AI five-layer cake-public account-20260605.md
├── Tencent/ — All Tencent research reports
│ ├── Tencent-research-20260408.md
│ ├── Tencent-earnings-2025Q4.md
│ ├── Tencent-management-20260409.md
│ └── Tencent-thesis.md
├── Pinduoduo/ — All Pinduoduo research reports
├── Bubble Mart/ — All research reports on Bubble Mart
├── Nuclear power-industry-20260409.md — Industry reports in the root directory
├── AI computing power-funnel-20260509.md — put the funnel screening report in the root directory
├── AI-Rotation Judgment-20260509.md — Topic-level comprehensive judgment report placed in the root directory
├── portfolio-latest.md — put the portfolio report in the root directory
├── investor-profile.md — investor profile (root directory; the most sensitive file this toolkit writes — never commit)
└── Multi-company comparison-checklist-20260408.md — put multi-company reports in the root directory
```

## Report naming convention

| Skill | File Naming Format | Example |
|------|---------|------|
| /investment-team | `{Company name}/` Directory contains 4 perspectives + final report | `reports/pinduoduo/final report.md` |
| /investment-research | `{Company name}-research-{YYYYMMDD}.md` | `reports/Tencent/Tencent-research-20260408.md` |
| /investment-checklist | `{Company name}-checklist-{YYYYMMDD}.md` | `reports/Tencent/Tencent-checklist-20260408.md` |
| /industry-research | `{Industry name}-industry-{YYYYMMDD}.md` (root directory) | `reports/nuclear power-industry-20260409.md` |
| /industry-funnel | `{Industry name}-funnel-{YYYYMMDD}.md` (root directory) | `reports/AI computing power-funnel-20260509.md` |
| /private-company-research | `{Company name}-private-{YYYYMMDD}.md` | `reports/bytebeat/bytebeat-private-20260408.md` |
| /earnings-review | `{Company name}-earnings-{Period}.md` | `reports/Tencent/Tencent-earnings-2025Q4.md` |
| /earnings-team | `{Company name}/` The directory contains 4 master perspectives + research manuscripts + public account articles + reader reviews | `reports/Tencent/Tencent-earnings-2025Q4.md` (public account final draft) |
| /thesis-tracker | `{Company name}-thesis.md` (long-term maintenance) | `reports/Tencent/Tencent-thesis.md` |
| /portfolio-review | `portfolio-latest.md` (root directory, continuously updated) | `reports/portfolio-latest.md` |
| /management-deep-dive | `{Company name}-management-{YYYYMMDD}.md` | `reports/Tencent/Tencent-management-20260409.md` |
| /investor-onboarding | `investor-profile.md` (root directory, continuously updated) | `reports/investor-profile.md` |
| /etf-review | `{Fund or comparison name}-etf-{YYYYMMDD}.md` (root directory) | `reports/VWRP-etf-20260802.md` |

## /investment-team file structure

```
reports/{company name}/
├── README.md — Overview of research framework + core conclusions
├── 01-Business model analysis-Duan Yongping’s perspective.md
├── 02-Financial Valuation Analysis-Buffett’s Perspective.md
├── 03-Industry Competition Analysis-Munger’s Perspective.md
├── 04-Risk Management Assessment-Li Lu’s Perspective.md
└── Final report.md — Team Lead comprehensive report
```

## Core principles of investment research analysis (highest priority)

- **Objective, objective, objective** - All investment research analysis must be based on facts and data, and subjective assumptions are strictly prohibited
- Strictly distinguish between "facts" and "opinions": facts are supported by data, and opinions must be clearly marked as "opinions" or "speculations"
- **No preset position**: There is no preset of bullishness or bearishness. First, the data is presented, then the logic is deduced, and finally the conclusion is drawn. Conclusions must flow naturally from the data
- It is forbidden to use subjective expressions such as "I think", "I think", "Obviously", etc. Use "data shows", "evidence shows", "according to XX sources" instead
- **Present both sides**: Each core judgment must be accompanied by negative arguments ("But on the other hand..."), allowing readers to weigh their own
-Be honest about "uncertainty" or "insufficient data" about things you're not sure about, don't fill certainties with speculation
- All skills (investment-team, investment-research, earnings-review, etc.) must comply with the above principles when executing

## Reporting language and style

- All reports are in **English**
- Style: direct, sharp, no nonsense
- Data must be labeled with sources, and key data must be cross-validated from at least 2 sources
- Estimates must be marked "estimated"
- Ratings use ★ symbols (★1-5), excluding half stars
- Interspersed with quotes and comments from Buffett/Munger/Duan Yongping/Li Lu

## GitHub operations

> ### ⛔ Reports are LOCAL-ONLY — never commit them
>
> Everything written under `reports/` stays on the local machine. Do **not** `git add`,
> commit, or push report files, and do **not** ask whether to push them — the answer is
> always no. Research output routinely contains personal holdings, position sizes, and
> account balances, and this repository is public; once pushed, that data is in the git
> history permanently even if the file is later deleted.
>
> `reports/` is gitignored to enforce this. If a report ever needs to be shared, hand the
> file to the user directly (or produce an anonymised version containing only percentages
> and analysis) — never via a commit.

- Local clone path: `~/ai-berkshire/`
- Remote repo: `https://github.com/autosolutionsai-didac/ai-berkshire.git`
- `git pull --rebase origin main` before pushing (the remote often has new commits)
- Write commit messages in English, describing clearly what changed
- Toolkit changes (`skills/`, `tools/`, `docs/`, `scripts/`, `README.md`) are committed as
  normal — the local-only rule applies to `reports/`

## Common commands

```bash
# Commit a toolkit change (NOT reports — those stay local)
cd ~/ai-berkshire
git add skills/xxx.md
git commit -m "Describe the change"
git pull --rebase origin main
git push origin main
```

## Notes

- Market value must be manually calculated and verified: stock price × total share capital, compared with the reported market value
- The currency unit must be clear (HKD/RMB/USD) to prevent confusion
- PE/ROE and other indicators are accurately calculated using tools/financial_rigor.py
- After writing a report, deliver the file to the user directly. Never commit or push it (see GitHub operations above)
