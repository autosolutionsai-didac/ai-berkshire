# AI Berkshire — a value-investing research team in one command

> "Price is what you pay. Value is what you get." — Warren Buffett

**AI Berkshire** turns the methodologies of four value-investing masters — **Buffett, Munger, Duan Yongping, and Li Lu** — into a set of research skills for Claude Code and Codex. Point it at a company and it produces a professional-grade, decision-ready research report — not a hedged "on one hand, on the other hand" essay.

**One person + Claude Code = an entire investment research team.**

---

## The headline: one command runs the whole funnel

```bash
/berkshire-skill Tencent
```

`/berkshire-skill` walks a single company through a complete value-investing funnel, phase by phase, and ends with a capstone **Comprehensive Investment Decision Report** synthesized from everything before it:

```
quality-screen ─▶ investment-team (four masters) ─▶ management-deep-dive
     ─▶ earnings-review ─▶ investment-checklist ─▶ thesis-tracker
          ─▶ 📄 Comprehensive Investment Decision Report
```

- **It behaves like a real funnel, not a checklist.** A quality-screen elimination or a checklist integrity veto **halts the run early** — bad businesses don't get a 7-phase writeup.
- **It doesn't reinvent the skills.** Each phase runs the canonical workflow of the individual skill below, writing into one shared `reports/{Company}/` folder, so the standalone skills stay the single source of truth and still work on their own.
- **Flags:** `quick` (fast triage), `force` (run every phase even if the screen eliminates), `resume` (continue an interrupted run).

```bash
/berkshire-skill Apple quick      # fast triage before committing to a full run
/berkshire-skill IonQ force       # push past the quality-screen gate
```

Prefer to drive it yourself? Every phase is also a standalone slash command (see the [skills catalog](#skills-catalog-19-skills)).

---

## What makes it different from just asking an AI

You can always ask Claude "should I buy Pinduoduo?" and get a balanced answer that ends in "…do your own research." That looks right but **can't drive a decision.** AI Berkshire is built around decision discipline:

**1. It forces a verdict.** Every run ends in **Buy / Hold / Avoid** (or Pass / Gray Zone), with a concrete valuation range and tiered position sizing — never a fence-sit.

**2. Four masters in genuine tension, not one voice.** The four perspectives are designed to *contradict* each other. On Pinduoduo: Buffett sees a cash machine at 6x ex-cash P/E (buy); Li Lu sees culture/certainty risk (if unsure, don't). That conflict is the real state of a decision — and a single prompt can't produce it.

**3. Structured anti-bias.** Information-richness rating (A/B/C) to fight the "more data = more certainty" illusion; Munger-style inversion ("how could this die?"); an 8-item quick-kill checklist where any red line is a veto; and honest "insufficient data" instead of confident guessing.

**4. Numbers are computed, not eyeballed.** LLMs can't do reliable mental math, and mixing HKD with CNY wrecks a valuation. Every figure goes through `tools/financial_rigor.py` (exact `decimal.Decimal` arithmetic) and is cross-checked against ≥2 independent sources.

```bash
python3 tools/financial_rigor.py verify-market-cap \
  --price 510 --shares 9.11e9 --reported 4.65e12 --currency HKD
# ✅ Verified — deviation only 0.08%
```

**5. Multi-agent parallelism.** `/investment-team` launches 4 independent agents that each search, cross-validate, and conclude on their own, then a team lead synthesizes — 4× the search volume and four real perspectives, not one prompt split four ways.

**6. Reproducible.** Same input → structurally consistent, equally deep output. Compare seven companies on identical criteria, or re-run the same company in six months and diff the changes.

---

## Architecture

<p align="center">
  <img src="assets/architecture.png" alt="AI Berkshire architecture" width="360" />
</p>

**Three layers:**
- **Skill layer** — 19 clear entry points ("what you want to do"): the full pipeline, deep research, earnings, industry screening, portfolio management, and thinking tools.
- **Agent layer** — skills fan out into parallel agents that search independently, challenge each other, and get synthesized by a team lead.
- **Tool layer** — exact-precision math, live web search, and a release auditor that spot-checks every report's data before it's considered final.

---

## Skills catalog (19 skills)

### 🚀 Full pipeline

| Skill | Purpose |
|-------|---------|
| [`/berkshire-skill`](skills/berkshire-skill.md) | One command runs the whole funnel end to end and emits a capstone decision report. Halts early on a hard-gate failure. |

### 🔬 Deep research

| Skill | Purpose |
|-------|---------|
| [`/investment-research`](skills/investment-research.md) | Four-master comprehensive analysis of a public company |
| [`/investment-team`](skills/investment-team.md) | 4 agents research in parallel — fastest, most comprehensive |
| [`/management-deep-dive`](skills/management-deep-dive.md) | "Buying a stock is buying its people" — deep management/integrity dossier |
| [`/private-company-research`](skills/private-company-research.md) | Detective-style research on info-scarce private firms (SpaceX, ByteDance…) |
| [`/deep-company-series`](skills/deep-company-series.md) | 8-part, publication-grade long-form series |

### 📊 Earnings analysis

| Skill | Purpose |
|-------|---------|
| [`/earnings-review`](skills/earnings-review.md) | Deep-read of primary filings only — no sell-side summaries |
| [`/earnings-team`](skills/earnings-team.md) | Four masters interpret earnings in parallel → editor → publishable article |

### 🏭 Industry & screening

| Skill | Purpose |
|-------|---------|
| [`/industry-research`](skills/industry-research.md) | Map every opportunity across an industry's value chain |
| [`/industry-funnel`](skills/industry-funnel.md) | Full market → rough cut ≤10 → 3 deep dives |
| [`/quality-screen`](skills/quality-screen.md) | 7 hard metrics that quickly eliminate non-first-class companies |
| [`/bottleneck-hunter`](skills/bottleneck-hunter.md) | Find physical supply-chain bottlenecks behind a supertrend |
| [`/investment-checklist`](skills/investment-checklist.md) | Buffett's six gates — a 10-minute go/no-go |

### 📈 Portfolio management

| Skill | Purpose |
|-------|---------|
| [`/portfolio-review`](skills/portfolio-review.md) | Position sizing, concentration, and rebalancing |
| [`/thesis-tracker`](skills/thesis-tracker.md) | Post-buy discipline: track whether your thesis has been falsified |
| [`/news-pulse`](skills/news-pulse.md) | A stock moved — figure out *what happened* in 10 minutes |

### 🧠 Thinking & writing tools

| Skill | Purpose |
|-------|---------|
| [`/dyp-ask`](skills/dyp-ask.md) | Think through any question the Duan Yongping way |
| [`/financial-data`](skills/financial-data.md) | Retrieve & cross-validate data from 2+ sources; flags >1% deviation |
| [`/wechat-article`](skills/wechat-article.md) | Author + editor + reader agents produce a publishable article |

---

## Quick start

### 1. Install a client

**Claude Code:**
```bash
npm install -g @anthropic-ai/claude-code
```

**Codex** (macOS/Linux): `curl -fsSL https://chatgpt.com/codex/install.sh | sh` (or `npm install -g @openai/codex`, or `brew install --cask codex`). Windows: `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"`.

### 2. Install the skills

```bash
git clone https://github.com/autosolutionsai-didac/ai-berkshire.git
cd ai-berkshire

# Claude Code — copies skills/*.md to your global commands dir
./scripts/install-claude-commands.sh

# Codex — generates & installs Codex skills to ~/.codex/skills
./scripts/install-codex-skills.sh
# (optional) Claude-Code-style slash prompts for Codex
./scripts/install-codex-prompts.sh
```

`skills/*.md` are the canonical Claude Code sources; `codex-skills/` and `codex-prompts/` are generated from them by `scripts/sync-codex-*.py` — never hand-edited.

### 3. Use it

```bash
# The whole funnel, one command
/berkshire-skill Tencent
/berkshire-skill Apple quick

# Or drive individual phases
/investment-team Meituan
/earnings-review Tencent 2025Q4
/industry-funnel AI Compute
/investment-checklist Moutai, NVIDIA, Apple
/portfolio-review Tencent 30%, Meituan 20%, Moutai 20%, Cash 30%
/news-pulse Tencent
/dyp-ask Where is Pinduoduo's real moat?
```

In Codex, refer to skills by name (e.g. *"Use investment-research to research Tencent"*), or via the `/prompts:<name>` menu if you installed the slash prompts.

---

## How the four masters work together

```
              Duan Yongping — "the right business" (business essence)
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
     Buffett                    Munger                     Li Lu
   moat + margin           inversion + risk           civilizational
    of safety              list + bias audit          trend / paradigm
```

They don't just divide labor — they **challenge each other**. Duan says "great business" → Munger asks "how could it die?" Buffett says "cheap enough" → Li Lu asks "will it still exist in 10 years?" You don't get four reports stapled together; you get four thinking systems colliding.

Every report is anchored by **`tools/financial_rigor.py`** — exact-decimal market-cap and valuation verification, multi-source cross-validation, three-scenario (bull/base/bear) targets, and Benford's-law anomaly checks — plus **`tools/report_audit.py`**, which randomly samples data points from a finished report and re-verifies them before it can be declared final.

Reports are written in English and filed under `reports/{Company}/`, one folder per company.

---

## Real track record

> Screenshots from a real brokerage account (Futu Securities). Past performance does not guarantee future results.

| | 2024 full year | 2025 |
|---|:---:|:---:|
| **This framework (live)** | **+69.29%** | **+66.38%** |
| S&P 500 | +23.31% | +16.39% |
| Nasdaq Composite | +28.64% | +20.36% |
| Hang Seng Index | +17.67% | +27.77% |
| CSI 300 | +14.68% | +17.66% |

<p align="center">
  <img src="assets/2024-returns.png" width="280" />
  <img src="assets/2025-returns.png" width="280" />
</p>

Two consecutive years beating every major global index, with cumulative live returns exceeding ¥1.46M over the period.

---

## Roadmap

- [x] Four-master framework, multi-agent team, and Buffett checklist
- [x] Industry value-chain scan + funnel screening + quality screen
- [x] Private-company research, earnings deep-read, portfolio review, thesis tracker
- [x] Financial-rigor tools (exact arithmetic, market-cap verification, cross-validation, Benford)
- [x] **One-command full pipeline (`/berkshire-skill`)** with hard gates, flags, and a release audit
- [ ] Historical backtesting: research verdicts vs. actual price performance
- [ ] Macro-cycle analysis framework
- [ ] Live data feeds via MCP (Wind / Bloomberg / Yahoo Finance)

---

## Disclaimer

For educational and research purposes only. This is **not** investment advice. Investing involves risk; always do your own due diligence.

## License

MIT

---

> "The best investment you can make is in yourself." — Warren Buffett

[![Star History Chart](https://api.star-history.com/svg?repos=autosolutionsai-didac/ai-berkshire&type=Date)](https://star-history.com/#autosolutionsai-didac/ai-berkshire&Date)
