---
name: news-pulse
description: Company news pulse — rapid attribution when a stock moves. Uses 4 parallel Agents to scout company events / regulatory policy / industry peers / market sentiment, producing an "event timeline + primary-cause verdict for the move + whether it triggers a thesis re-review."
---

## Codex adapter note

This skill is generated from `skills/news-pulse.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Commands that reference `~/ai-berkshire/tools/...` assume the repo is checked out at `~/ai-berkshire`; if needed, prefer the current workspace path.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Company News Pulse: Rapid Stock-Move Attribution Team

Run a recent-news reconnaissance and stock-move attribution on $ARGUMENTS. **This is not deep research; it is rapid intelligence response** — the goal is to answer, within 10 minutes: "What has recently happened at this company? What is the real cause of the stock move? Do we need to re-review the investment thesis?"

## When to use

- A holding/watchlist stock rises or falls sharply (typical trigger lines: single-day ±5%, one-week ±10%)
- The stock moves after earnings and you want to quickly figure out what the market is reacting to
- You saw a news headline but aren't sure whether it is noise or a real signal
- **Not applicable**: full research (use `/investment-team`), earnings deep-read (use `/earnings-review`), long-term thesis tracking (use `/thesis-tracker`)

## Execution flow

### Step 1: Confirm parameters and scenario

Clarify the following with the user (if not already provided in $ARGUMENTS):

| Parameter | Description | Default |
|------|------|------|
| **Company name** | Chinese/English/ticker all accepted | Required |
| **Time window** | Look-back days for scouting news | Default 14 days; can shrink to 7 during earnings season |
| **Stock move** | Rise/fall magnitude + time, e.g. "down 12% / 3 days" | Optional; if provided, used to focus the attribution |
| **Focus emphasis** | Company events / regulatory / industry / sentiment | Default: even weight across all four |

If the user only gives a company name, ask back first: "How many days of recent news? Is there a specific stock move you want explained?" — **do not silently assume**.

### Step 2: Information-availability rating

Refer to the A/B/C rating in `investment-team.md`, but with different dimensions:

| Level | Characteristics | Scouting strategy |
|------|------|---------|
| **Level A (information-rich)** | Large-cap, broad media coverage, earnings season | The focus is **noise reduction and attribution** — too much information actually makes the real cause hard to find; each Agent must exercise judgment and filter out "re-reported" secondhand news |
| **Level B (moderate information)** | Mid/small-cap, average coverage | Standard mode; attach 1-2 independent sources to each key event |
| **Level C (information-scarce)** | HK small-cap, newly listed, obscure | Switch to "reconnaissance mode" — you may find no news at all that explains the move, and **that conclusion itself has value** (the move may be technical/flow-driven rather than fundamental) |

Communicate the rating to each Agent, as it affects how they scout.

### Step 3: Create the team

Use TeamCreate to create the team:
- `team_name`: `{Company}-newspulse` (lowercase English, e.g. `pdd-newspulse`)
- `agent_type`: `team-lead`

### Step 4: Create 4 scouting tasks

Use TaskCreate to create the following 4 tasks:

#### Task 1: Company-event scout (company-event-scout)

- **subject**: `Scout {Company}'s company-body events over the past {N} days`
- **description**:
  1. **Official announcements**: recent disclosures on regulatory filing platforms such as HKEX / SEC / CNINFO
  2. **Earnings and guidance**: latest quarterly/annual report, earnings pre-announcement, earnings-call highlights
  3. **Management actions**: executive changes, insider buying/selling, buybacks, dividends, equity incentives
  4. **Major business events**: new product launches, M&A / restructuring, divestitures, major customers/orders
  5. **Capital operations**: refinancing, convertible bonds, ADR conversion, return-to-A-share / delisting motions
  6. **Litigation and compliance**: being sued, self-disclosed compliance events
  7. For each event, tag: **date / source link / one-sentence summary / possible relevance to the stock move (high/medium/low)**
  8. Output a timeline table in reverse-chronological order

#### Task 2: Regulatory and policy (regulatory-watcher)

- **subject**: `Scout regulatory and policy changes for {industry/company} over the past {N} days`
- **description**:
  1. **Industry regulation**: new rules, fines, rectifications, license changes in the industry
  2. **Cross-border policy**: US-China relations (China ADRs), tariffs, export controls, data security
  3. **Tax policy**: changes related to VAT, corporate income tax, personal income tax
  4. **Antitrust and competition law**: investigations, fines, blocked M&A
  5. **Sector-specific policy**: pharma centralized procurement, education "double reduction," real-estate "three red lines," internet-platform regulation, etc.
  6. **Money and FX**: changes in exchange rate / interest rate / capital controls affecting this company
  7. For each policy, tag: **date / source / degree of direct impact on this company (direct/indirect/unrelated)**
  8. Key judgment: whether a "policy black swan" has just landed

#### Task 3: Industry and competitors (industry-peer-analyst)

- **subject**: `Scout {Company}'s industry landscape and peer moves over the past {N} days`
- **description**:
  1. **Direct rivals**: list 3-5 core competitors and check recent events for each (earnings, products, price wars, personnel)
  2. **Supply chain up/downstream**: upstream raw materials/suppliers, downstream customers/channels — recent changes in price, capacity, orders
  3. **Industry as a whole**: industry prosperity data, shipment volumes, demand-side signals (consumption data, tender data, etc.)
  4. **Substitute threat**: impact of new technologies / new business models on the industry
  5. **Industry-index performance**: recent performance of peer stocks; is this company outperforming / underperforming / in line
  6. Key judgment: **is this a company-specific event, or a beta swing across the whole industry?**
  7. Tag each event with source and date

#### Task 4: Market sentiment and sell-side / big-V voices (sentiment-tracker)

- **subject**: `Scout {Company}'s market sentiment and institutional-view changes over the past {N} days`
- **description**:
  1. **Sell-side rating changes**: recent rating/target-price adjustments from Goldman Sachs, Morgan, CICC, etc.
  2. **Institutional holding changes**: 13F disclosures (US stocks), Stock Connect holdings, northbound-capital flows
  3. **Short data**: short-interest ratio, newly published short reports (if any)
  4. **Big-V opinions**: you can run `python3 ~/ai-berkshire/tools/xueqiu_scraper.py` to pull recent relevant posts from big-V voices such as Duan Yongping
     - Duan Yongping user_id: `1247347556`
     - Command example: `python3 ~/ai-berkshire/tools/xueqiu_scraper.py --user-id 1247347556 --keywords {Company},{ticker} --output /tmp/dyp-{Company}.md`
     - Only invoke when the company is a name Duan Yongping / Li Lu follow; otherwise skip to save time
  5. **Rumors and chatter**: unverified media rumors, hot social-media discussion topics (Xueqiu / X / Reddit)
  6. **Technical signals**: whether key support/resistance was hit, whether there were block trades, margin-financing anomalies
  7. Key judgment: **is this fundamentally driven or sentiment/flow driven?**

### Step 5: Launch the 4 Agents in parallel

**You must call the Task tool 4 times in parallel within a single message.** Configure each Agent:
- `subagent_type`: `general-purpose`
- `run_in_background`: `true`
- `team_name`: `{Company}-newspulse`
- `name`: the corresponding role name (company-event-scout / regulatory-watcher / industry-peer-analyst / sentiment-tracker)

Prompt template for each Agent:

```
You are the "{role name}" in the {Company} News Pulse team, responsible for scouting recent events over the past {N} days along the {scouting dimension} dimension.

Time window: {start date} ~ {today's date}
Stock-move background: {the move info provided by the user; if none, write "No specific move, routine check-up"}
Information-availability level: {A/B/C}

Please complete Task #{task number}: {task subject}

Specific scouting requirements:
{contents of the task description}

**Scouting method**:
- Prefer WebSearch for time-sensitive queries (add a date or "recent," "latest," "2026" to keywords)
- Use WebFetch to deep-read primary sources for key events (original announcement text, earnings reports, regulatory filings)
- Do "independent-source verification" for each event — a rumor needs at least 2 independent sources
- **Do not be misled by clickbait**: tag events where headline and body do not match as "misleading headline"

**Output format (important)**:
1. **Core findings**: the 3-5 most critical events, 1-2 sentences each
2. **Complete event timeline table** (reverse-chronological):
   | Date | Event | Source | Relevance to stock move | Persistence |
3. **Attribution conclusion for this dimension**: based on the events scouted, answer "Can this dimension explain the stock move? With what confidence?"
4. **Data-gap statement**: which information was not found, which points are questionable, which need more information
5. Strictly distinguish "fact" from "speculation" and follow the objectivity principles in CLAUDE.md

**When done**:
1. Use TaskUpdate to mark the task as completed
2. Use SendMessage to send the complete scouting report to team-lead (type: "message", recipient: "team-lead")
```

### Step 6: Track progress in real time

- As each scouting report arrives, show the user the 3 core findings for that dimension
- Wait for all 4 to arrive
- Once all 4 are in, send a shutdown_request to the 4 Agents via SendMessage

### Step 7: team-lead synthesizes the attribution

Aggregate the 4 scouting reports and output the **stock-move attribution report** (not a research report — the focus is "judgment"):

---

#### 1. One-sentence attribution
> Use one short passage (one or two sentences) to state: the primary cause of this stock move + the secondary cause + a nature verdict (value event / sentiment swing / unclear)

#### 2. Complete event timeline (merging all 4 dimensions)

In reverse-chronological order, merge events across all dimensions:

| Date | Dimension | Event | Source | Attribution weight |
|------|------|------|------|-----------|
| 2026-04-30 | Company | XX | link | 🔴 High |
| 2026-04-29 | Industry | XX | link | 🟡 Medium |
| 2026-04-28 | Sentiment | XX | link | ⚪ Low |

Weight legend: 🔴 High (enough to explain the move on its own) / 🟡 Medium (contributes partially) / ⚪ Low (background noise)

#### 3. Attribution table

| Candidate explanation | Evidence | Counter-evidence | Confidence | Persistence |
|---------|------|------|------|--------|
| e.g. earnings miss | revenue 5% below expectations, gross margin declined | management explained it as a one-off factor | High | Short-term 1-2 weeks |
| e.g. industry beta | peers fell 8% over the same period | this stock fell notably more than the industry | Medium | In sync with the industry |

#### 4. Nature verdict (core conclusion)

Check one:

- [ ] **Value event**: a real change in fundamentals occurred (earnings, moat, management, endgame); the investment thesis needs re-review
- [ ] **Sentiment/technical swing**: no change in fundamentals; driven by flows/sentiment/beta; can be viewed as an opportunity or as noise
- [ ] **Cause unclear**: no event found that matches the magnitude of the stock move — **this is the most dangerous conclusion**; either the market already knew something (insider/front-running), or we missed an information source
- [ ] **Mixed**: partly a value event + partly sentiment amplification

#### 5. Per-dimension scouting summary

For each dimension, the 3-5 most important findings + that dimension's attribution contribution.

#### 6. Action recommendations

| Action | Recommended? | Reason |
|------|--------|------|
| Trigger investment-thesis re-review (`/thesis-tracker`) | | |
| Trigger deep earnings read (`/earnings-review`) | | |
| Trigger management re-review (`/management-deep-dive`) | | |
| Position action (add / trim / no change) | | Suggestion only; the final decision rests with the user |
| Observe only | | |

#### 7. Tracking checklist for the next 7-30 days

- [ ] Pending event 1 (e.g. 5/15 earnings call)
- [ ] Metric to track 2
- [ ] Key signal to watch 3

#### 8. Information-gap statement

Honestly list the questions this reconnaissance could not resolve, the information that could not be found, and the items that need more disclosure. **Better to mark "uncertain" than to fill in with speculation.**

---

### Step 8: Save the report

Write to `reports/{Company}/{Company}-news-{YYYYMMDD}.md`. If the `reports/{Company}/` directory does not exist, create it (indicating this company has no prior research report yet).

### Step 9: Clean up the team

Use TeamDelete to release the team resources.

## Key principles

1. **Speed beats completeness** — the core value of this skill is delivering an attribution verdict within 10-15 minutes; do not fall into deep analysis (that is the job of other skills)
2. **Attribution over enumeration** — finding events is not hard; the hard part is judging "which event is worthy of this stock move." Subtract, don't add
3. **Be honest about "unclear"** — when the primary cause cannot be found, explicitly write "cause unclear." This is more valuable than forcing a causal chain (the market may be front-running bad news)
4. **Do not preset a stance** — do not lean toward "this is a sentiment swing, no big deal" just because you hold the stock. Write whichever side the evidence points to
5. **Distinguish "catalyst" from "coincidence"** — an event that happened at the same time is not necessarily the primary cause of the move; check whether the magnitude of impact matches
6. **Respect information availability** — a Level C company may simply have no findable news, and that conclusion itself must be written out
7. **Follow the objectivity principles in `CLAUDE.md`** — every judgment is backed by data sources; distinguish fact from opinion
8. **Do not make decisions for the user** — provide attribution and an action-recommendation checklist, but leave buy/sell decisions to the user
