---
name: berkshire-skill
description: "AI Berkshire skill: Berkshire Skill: One-Command Full Investment Pipeline. Source: skills/berkshire-skill.md."
---

## Codex adapter note

This skill is generated from `skills/berkshire-skill.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Commands that reference `~/ai-berkshire/tools/...` assume the repo is checked out at `~/ai-berkshire`; if needed, prefer the current workspace path.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Berkshire Skill: One-Command Full Investment Pipeline

Run the complete AI Berkshire research pipeline on $ARGUMENTS (a company or stock) in a single command. This orchestrator chains the toolkit's individual skills in dependency order and ends with a capstone that synthesizes everything into one decision report.

**What it does:** you type `/berkshire-skill <company/stock>` once, and it walks the company through a value-investing funnel — quick elimination screen -> four-master deep research -> management -> earnings -> buy checklist -> thesis -> a final Comprehensive Investment Decision Report — halting early if the company fails a hard gate, exactly like a real investment process.

**What it is not:** it does not re-implement the other skills. Each phase executes the canonical workflow already documented in the referenced `skills/<name>.md` file, so the individual commands (`/investment-team`, `/investment-checklist`, ...) stay the single source of truth and remain usable on their own.

---

## Core principles (apply to every phase)

These override any looser wording inside a sub-skill:

- **Objective, objective, objective** — every judgment rests on facts and data, never on assertion.
- **Separate fact from opinion** — facts are backed by data with sources; opinions and speculation are explicitly labeled "opinion" / "speculation."
- **No preset stance** — do not decide bull or bear first. Lay out the data, then the logic, then let the conclusion fall out.
- **Show both sides** — every core judgment carries a counter-argument ("but on the other hand ...") so the reader can weigh it.
- **Honesty over false precision** — when data is missing, say "insufficient data." Never fill certainty with guesses.
- **English output** — all reports this pipeline writes are in English.
- **Numbers are computed, not eyeballed** — use `tools/financial_rigor.py` for market cap, valuation, and three-scenario math; cross-validate key financials against two independent sources per `skills/financial-data.md`.
- **Explicit currency** — every monetary figure carries its currency (USD / HKD / CNY / ...); never compare figures across currencies without converting and saying so.
- **Star ratings** use the star glyph (1-5), no half stars.

---

## Phase 0 - Identify and prepare

**Supported input formats:**

| Input | Behavior |
|-------|----------|
| `/berkshire-skill <company/stock>` | Normal full run |
| `/berkshire-skill <company> force` | Run every phase even if the Phase 1 quality screen eliminates the company; the elimination verdict is still recorded and carried into the capstone |
| `/berkshire-skill <company> resume` | Continue an interrupted run: adopt the run date of the most recent phase outputs in `reports/{Company}/` (today's date if none exist), skip every phase whose output file already exists for that run date, and start from the first missing phase |

1. **Parse `$ARGUMENTS`** into: company name (English), ticker (if given), market (US / HK / A-share / private), and any trailing flag (`force` / `resume`).
2. **Resolve the listing.** If the company trades in multiple venues (e.g. Tencent = 0700.HK plus the TCEHY ADR), pick the primary listing and state the ticker, exchange, and reporting currency the entire run will use.
3. **Detect public vs private.** If the company is unlisted (no public financials — e.g. ByteDance, SpaceX, miHoYo), take the **private-company branch** described at the end. Otherwise continue with the public-company sequence.
4. **Create the working folder and pin the run date.** Create `reports/{Company}/` (English company name); every phase writes its output here so later phases and the capstone can read them. Set `{YYYYMMDD}` to today **once** and use it for every dated filename this run writes, even if the run spans midnight or resumes later the same day. If the folder already contains files from earlier dates, list them with their dates and treat them as **historical context only** — they are not this run's inputs (see Phase 7).
5. **Take the data snapshot.** Fetch once, up front: current share price (with timestamp and source), total share count, market cap recomputed via `tools/financial_rigor.py verify-market-cap`, the latest reported fiscal period, and the primary listing + currency from step 2. Write it to `reports/{Company}/data-snapshot.md`. Every later phase anchors its valuation math to this snapshot instead of re-fetching, so figures stay consistent across a multi-hour run. (The snapshot is an intermediate working file — do not push it to git.)
6. **Run the information-richness rating once** (A / B / C), reusing the pattern in `skills/investment-team.md`:
   - **A (information-rich):** listed for years, broad analyst coverage -> emphasize contrarian checks and reverse thinking, avoid restating consensus.
   - **B (moderate):** recently listed, limited coverage -> label the confidence of every estimated figure.
   - **C (information-scarce):** obscure / newly listed / frontier market -> switch to first-principles mode; do not fake completeness.
   - Reminder to carry into every phase: **more data != higher certainty, less data != lower certainty. The confidence an AI can express != the real certainty of the investment. Certainty comes from the business model, not from the volume of available material.**
7. **Announce the plan** to the user: list the phases below, note that the run is automatic but will **halt at any hard gate failure** (unless `force` was given), and set expectations — this is a long, search-heavy run (typically well over an hour of wall-clock time across dozens of web searches), with a progress update after each phase. Then begin.

---

## Public-company sequence

Run these phases in order. After each phase, show the user a one-line progress update (phase name, output file, and the 3-5 key findings). Where a sub-skill's documented output path differs (some default to the home directory), **override it to write into `reports/{Company}/`** so everything stays colocated.

**Execution model (context budget):** run each of Phases 1-6 through the Task tool as background subagent(s). The subagent executes the referenced skill's workflow, writes the output file into `reports/{Company}/`, and returns **only the 3-5 key findings**. Keep just those summaries in the orchestrating session; Phase 7 re-reads the full files from disk. Do not execute the sub-skill workflows inline — a full pipeline run inline will exhaust the session context before the capstone. Phases 3 and 4 are independent of each other and may run in parallel; all other phases run in sequence. Under `resume`, skip any phase whose output file already exists for the pinned run date.

### Phase 1 - Quality screen (elimination gate)

Execute the workflow in **`skills/quality-screen.md`** for the single company: the 7 hard metrics (10-yr avg ROE > 8%, 5-yr cumulative FCF > 0, interest coverage > 2x, gross margin > 15%, OCF/NI > 0.7, net margin > 5%, share dilution < 20%), honoring its three exemption clauses.
- Output: `reports/{Company}/{Company}-quality-screen-{YYYYMMDD}.md`
- **HARD GATE:** if the company is *eliminated* (fails the metrics and no exemption applies), write a short elimination note into the capstone, report the verdict to the user, and **halt** — do not run the deeper phases. (This mirrors a real funnel. With the `force` flag — or if the user asks afterwards — continue the full run anyway, carrying the elimination verdict into every later phase and the capstone. "Insufficient data" on a metric is not a failure; it degrades the information-richness rating, it does not eliminate.)

### Phase 2 - Research team (analytical core)

Execute the workflow in **`skills/investment-team.md`** for the company: four parallel perspectives — business model (Duan Yongping), financials and valuation (Buffett), industry and competition (Munger), risk and management (Li Lu) — then the team-lead synthesis.
- Outputs into `reports/{Company}/`: the four perspective files (`01-business-model-duan-yongping.md`, `02-financials-valuation-buffett.md`, `03-industry-competition-munger.md`, `04-risk-management-li-lu.md`) and the team-lead `final-report.md`.
- This phase must use `tools/financial_rigor.py` for all market-cap/valuation math, as its skill file specifies.

### Phase 3 - Management deep-dive

Execute the workflow in **`skills/management-deep-dive.md`** ("buying a stock is buying people"): strategy track record, execution, the integrity core (commitments vs delivery, crisis behavior, stakeholder treatment), capital allocation, governance, and the post-CEO scenario.
- Output: `reports/{Company}/{Company}-management-{YYYYMMDD}.md`

### Phase 4 - Earnings review

Execute the workflow in **`skills/earnings-review.md`** on the latest filing (annual or most recent quarter), reading primary documents (10-K/10-Q/annual report, earnings call, MD&A, footnotes) rather than third-party summaries.
- Output: `reports/{Company}/{Company}-earnings-{period}.md`

### Phase 5 - Buy checklist (decision gate)

Execute the workflow in **`skills/investment-checklist.md`**: the six gates — circle of competence, business quality, moat depth, management trustworthiness, valuation margin of safety, emotional discipline — plus the mirror test and hard disqualifiers.
- Output: `reports/{Company}/{Company}-checklist-{YYYYMMDD}.md`
- **HARD GATE:** an integrity disqualifier is a veto. Record the verdict in the capstone and skip the optional publishing add-on; still produce the decision report (with an Avoid verdict).

### Phase 6 - Thesis tracker

Execute the workflow in **`skills/thesis-tracker.md`**, honoring its mode detection:
- **No `{Company}-thesis.md` yet — establish mode:** the 5-question core thesis (<= 200 words), 3-7 core assumptions with verification method and cadence, the red-line list with severity, and the valuation anchors (buy / optimistic / neutral / pessimistic).
- **`{Company}-thesis.md` already exists — tracking-check mode (Mode B):** check every core assumption and red line against this run's fresh findings, update the health score, and append to the tracking-record table. Do not rebuild the thesis over an existing one — re-running the pipeline is a refresh, not a reset.
- Output: `reports/{Company}/{Company}-thesis.md`

### Phase 7 - Capstone: Comprehensive Investment Decision Report

This is the report built from all the rest. Read every file **this run produced** in `reports/{Company}/` — the files stamped with the pinned run date, plus the fixed-name outputs from Phases 2 and 6 (`01-…` through `04-…`, `final-report.md`, `{Company}-thesis.md`) and the data snapshot — and synthesize one report using the proven final-report structure from `skills/investment-team.md`. Files from earlier run dates are prior research: cite them explicitly as "prior research, dated {date}" where useful, but never blend them in as current findings:

1. **One-line verdict** (50-100 words): worth investing or not, and the core logic.
2. **Four-dimension scorecard** (business / financials / industry / risk-management), each 1-5 stars with the core judgment, plus a composite score.
3. **Key-data snapshot**: the critical financial and operating metrics (latest 2 years), each with a source.
4. **Per-phase summaries**: 3-5 most important findings from each of Phases 1-6.
5. **Bull vs Bear**: 5-7 bull points and 5-7 bear points.
6. **Buy checklist result**: the pass/fail table from Phase 5.
7. **Final recommendation**: Buy / Hold / Avoid, with valuation range, tiered position sizing (aggressive / balanced / conservative), key catalysts (add-signals and trim-signals), and the red-line list.
8. **Closing paragraph** (100-200 words), including the information-richness rating and an explicit AI-research-limitations note.

- Output: `reports/{Company}/{Company}-decision-{YYYYMMDD}.md`
- **Release audit (data spot-check):** run the audit before declaring the report final:
  ```bash
  # Step 1 - extract a 15% random sample of data points
  python3 ~/ai-berkshire/tools/report_audit.py extract --report reports/{Company}/{Company}-decision-{YYYYMMDD}.md
  # Step 2 - re-fetch each sampled figure from a reliable source (see skills/financial-data.md)
  # Step 3 - verdict
  python3 ~/ai-berkshire/tools/report_audit.py verdict --results '<filled JSON>' --report {Company}-decision-{YYYYMMDD}.md
  ```
  **[RELEASE]** all pass -> report is final; **[SEND BACK]** any fail -> fix and re-audit. Run at most **2** fix-and-re-audit cycles; if the audit still fails after the second fix, stop and present the failing data points to the user instead of looping.
- **Optional publishing add-on:** after the decision report is final and only if the verdict is not Avoid, offer to also produce a public-facing article via `skills/wechat-article.md` (single piece) or `skills/deep-company-series.md` (8-part series). Do not run it unless the user says yes.

---

## Private-company branch

For unlisted companies, adapt the sequence:

- **Phase 0 data snapshot** degrades to: latest funding round, implied valuation, and round date — every figure flagged `[estimate]`.
- **Skip Phase 1** hard metrics (no reliable public financials); note it as "insufficient data" rather than a pass/fail.
- **Phase 2 -> execute `skills/private-company-research.md`** instead of `investment-team.md`: funding history, revenue proxies (user metrics, app rankings, spend data, all flagged `[estimate]`), competitive positioning, management via LinkedIn/Crunchbase, and valuation via comparable private rounds / future-IPO scenarios.
- **Skip Phase 4** (earnings review) unless the company files something public.
- **Keep Phase 3** (management) and **Phase 6** (thesis), adapted to the sparse-data reality.
- **Phase 7 capstone** proceeds, but the report leads with an explicit data-sufficiency caveat and marks every estimate as such.

---

## Skills not run by this pipeline

These operate at a different granularity than a single company/stock and remain standalone commands: `industry-research`, `industry-funnel`, `bottleneck-hunter` (industry/theme level), `portfolio-review` (portfolio level), `news-pulse` (event-driven attribution), `earnings-team` (heavier publishing variant of earnings-review), and `dyp-ask` (conversational). `financial-data.md` is a data-sourcing standard that the phases already follow, not a step.

---

## Important notes

1. **Hard gates** — the pipeline behaves like a real funnel, not a box-ticking exercise. A Phase 1 quality-screen elimination **halts** the run (the deeper phases are skipped, unless the `force` flag was given). A Phase 5 integrity veto does not skip the capstone — it forces an **Avoid** verdict in the decision report and skips only the optional publishing add-on.
2. **One folder per company** — every artifact lands in `reports/{Company}/`; the capstone reads all of *this run's* outputs. Files from earlier run dates are prior research, never current inputs.
3. **Progress updates** — after each phase, surface the output file and 3-5 key findings so the user can follow along.
4. **Anti-bias at the synthesis** — the capstone must assess whether each phase was constrained by data availability or converged too closely with market consensus, and say so.
5. **Force a conclusion** — do not hide behind hedging: give Buy / Hold / Avoid with a concrete valuation range and position sizing.
6. **Honesty when scarce** — leave blanks marked "insufficient data" rather than dressing up guesses as certainty.
