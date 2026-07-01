---
name: industry-funnel
description: "AI Berkshire skill: Industry Funnel Screen: A Value-Investing Selection Pipeline From the Whole Market Down to 3 Names. Source: skills/industry-funnel.md."
---

## Codex adapter note

This skill is generated from `skills/industry-funnel.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Commands that reference `~/ai-berkshire/tools/...` assume the repo is checked out at `~/ai-berkshire`; if needed, prefer the current workspace path.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Industry Funnel Screen: A Value-Investing Selection Pipeline From the Whole Market Down to 3 Names

Run a funnel-style value-investing screen on the $ARGUMENTS industry/theme, narrowing from a whole-market scan layer by layer down to 3 final candidates.

## When to Use

When you name an industry or investment theme (e.g. "AI compute", "innovative drugs", "robotics") and want to:
1. Miss no important candidate (including A-shares, HK stocks, US stocks, and pre-IPO candidates)
2. Filter out "story stocks" and companies of insufficient quality using a uniform standard
3. Focus your effort on the 3 leaders truly worth deep research
4. Have an explicit keep/drop standard at each layer, so the process is reviewable and traceable

Difference from `industry-research`:
- `industry-research` emphasizes value-chain structure and the full landscape, slicing by segment
- `industry-funnel` emphasizes the single-stock screening funnel, narrowing from the whole market down to 3 names

The two are complementary: first use `industry-research` to understand the value-chain structure, then use `industry-funnel` to select specific candidates.

---

## Funnel Structure Overview

```
Layer 1: Whole-market scan   30-60 names   (union of activity + gainers + top 30 by market cap)
        ↓ 5 hard value-investing metrics
Layer 2: Coarse screen        ≤ 10 names   (all 5 metrics pass + moat ★★★ or above)
        ↓ Detailed analysis
Layer 3: Detailed analysis    ≤ 10 names   (300-500 words of structured analysis per name)
        ↓ Final selection
Layer 4: Four-master deep dive   3 names    (800-1200 words each, Buffett/Munger/Duan/Li views)
        ↓
Output: investment recommendation + action signal + position sizing
```

Each layer must record a rejection reason for every name it filters out — no black boxes.

---

## Step 1: Whole-Market Scan Entry

### 1.1 Definition of Active Stocks (union of three groups)

**Group A - Trading activity**:
- Ranked among the industry leaders by average daily turnover over the past 30 days (take the top 30 separately for A-shares/HK stocks/US stocks)

**Group B - Gainers list**:
- Top 20 by gain over the past 30 days
- Top 20 by gain over the past 90 days
- Union of the two

**Group C - Market-cap anchor**:
- Top 30 by market cap within the industry (regardless of price move)

Final scan pool = A ∪ B ∪ C, expected 30-60 names.

### 1.2 Markets That Must Be Searched

| Market | Suggested sources |
|------|---------|
| A-shares (Shanghai/Shenzhen) | Tonghuashun/East Money industry sectors, TDX |
| HK stocks | Futu/Tonghuashun HK, HKEX industry classification |
| US stocks | NASDAQ/NYSE industry ETF holdings, Yahoo Finance |
| International markets | Do not miss relevant companies in Japan/Korea/Taiwan/Europe (especially semiconductors and electronics) |
| Private companies | Break out a "future IPO candidates" subsection, noting the latest valuation and potential IPO timing |

### 1.3 Output Format

| Company | Ticker | Market | Market cap | One-line core business | Share of this industry | Selection group (A/B/C) |
|-------|------|-----|------|----------|-----------|----------------|

**Key self-checks**:
- Be cautious with "loosely related" names whose industry share is < 30%; flag them as "not a pure play"
- Do not miss Chinese/Asian markets just because English-language material is scarce
- Do not miss small-cap companies just because AI hype favors leaders

---

## Step 2: Coarse Screen on 5 Hard Value-Investing Metrics → ≤ 10 names

Apply the 5 hard metrics to each of the 30-60 companies from Step 1.

### 2.1 The 5 Hard Metrics

| # | Metric | Pass standard | Relaxation condition | Data source |
|---|------|---------|---------|---------|
| 1 | PE valuation | Reasonable (vs. historical range and peers) | High growth can be relaxed to PEG < 1.5 | Financials + Wind/Tonghuashun |
| 2 | ROE | > 15% or improving trend over past 3 years | Asset-heavy industries can be relaxed | Financials |
| 3 | Operating cash flow | Positive and > 70% of net profit | — | Financials |
| 4 | Debt-to-asset ratio | < 60% | Utilities/power can be relaxed to 70% | Financials |
| 5 | Moat quick-take | ★★★ or above | — | Qualitative judgment |

**5 types of moat**:
- Brand/pricing power
- Switching cost/user stickiness
- Network effect
- Economies of scale
- Technology/license/resource barriers

### 2.2 Output Format

| Company | PE | ROE | Cash flow/net profit | Debt ratio | Moat | Overall | Keep/drop | Rejection reason |
|------|----|----|-----------|-------|-------|------|------|---------|

**Keep rules**:
- All 5 metrics pass → keep outright
- 4 metrics pass + 1 close → keep but flag yellow
- Fewer than 4 pass → drop, note the reason

**Target**: keep ≤ 10 names. If too many are kept (> 12), raise the moat bar to ★★★★ and screen once more.

---

## Step 3: Detailed Analysis (≤ 10 names, 300-500 words each)

For the companies kept in the coarse screen, do a structured analysis of each.

### 3.1 Per-Company Analysis Template

```
## {Company} ({Ticker})

**One-line business model**:
(what it sells, to whom, how it makes money)

**Financial quality**:
- Revenue growth / profit growth / gross margin / ROE / cash flow
- Key change (the most important financial inflection over the past 1-2 years)

**Moat depth**:
- Primary moat type + concrete evidence
- A brief judgment on whether the moat will still be there 5 years out

**Top 3 risks**:
1.
2.
3.

**Valuation quick-take**:
- Current PE/PS/EV/EBITDA + position within historical range
- Peer comparison
- One-line conclusion: expensive / reasonable / cheap

**Advance to the final 3?**: Yes / No (reason)
```

### 3.2 Selection Standard for the Final 3

Do not simply rank by score and take the top 3; select for "portfolio complementarity":
- At least 1 "high-certainty, low-elasticity" name (Buffett type)
- At least 1 "medium-certainty, medium-elasticity" name (growth type)
- Optionally 1 "high-elasticity, high-risk" name (option type)

If a given sub-track cannot muster 3 good-enough names, prefer to write "2 finalists + 1 watch" rather than pad the list.

---

## Step 4: Four-Master Deep Dive (3 names, 800-1200 words each)

Run the four-master deep dive on the 3 finalists.

### 4.1 Duan Yongping View: The Nature of the Business

- Define in one sentence what business this company is in
- Is it a good business? Why?
- What is its "benfen" (benfen, staying true to one's role)? Has management strayed from it?
- Where does the "durability" of the business model come from?

### 4.2 Buffett View: Moat Depth

- Score using the five moat types (★1-5), listing concrete evidence
- Will the moat still be there in 10 years?
- Where is the "margin of safety" for buying now?

| Moat | Strength | Concrete evidence |
|-------|------|---------|
| Brand/pricing power | | |
| Switching cost | | |
| Network effect | | |
| Economies of scale | | |
| Technology/license barrier | | |

### 4.3 Munger View: Risks and Failure Modes

- How is this company most likely to fail? (list the top 3 failure paths)
- What is it worth in the worst case? (bare-bones valuation)
- Why do smart people not buy it? (inversion argument)
- Are there ethical/compliance/management risks?

### 4.4 Li Lu View: Positioning Within Civilization-Level Trends

- Is this company's track a "civilization-level paradigm shift" or a "temporary craze"?
- The closest historical technology-revolution analogy?
- The endgame for this company 10-20 years out?
- Is it a winner-take-all structure?

### 4.5 Overall Recommendation

```
Recommendation: ★★★★☆
Position type: core / satellite / option / watch
Suggested buy range: current price / on an N% pullback / wait patiently
Suggested position weight: X% of this theme's allocation
Key monitoring metric: (what signal would flag that this company's logic has reversed)
```

---

## Step 5: Comprehensive Output

Consolidate at the end of the report:

### 5.1 Final 3 Portfolio Table

| Company | Type | Recommendation | Suggested position | Core logic | Key risk |
|------|------|-------|---------|---------|---------|
| A | Core | ★★★★★ | 50-60% | | |
| B | Satellite | ★★★★☆ | 25-35% | | |
| C | Option | ★★★☆☆ | 5-15% | | |

### 5.2 Industry-Level ETF Alternative

If you would rather not pick stocks, list 1-3 relevant ETFs (A-shares/HK stocks/US stocks).

### 5.3 Overall Industry Positioning Judgment

- Historical percentile of industry PE/PB
- Fund flows (northbound, ETF creations/redemptions, sell-side coverage density)
- Whether the industry is overall in the "early / expansion / mature / decline" phase

### 5.4 Information-Sufficiency Self-Assessment (mandatory)

| Dimension | Grade | Notes |
|-----|------|-----|
| Completeness of company financial data | A/B/C | |
| Timeliness of valuation data | A/B/C | |
| Judgment on industry structure | A/B/C | |
| Management information | A/B/C | |

A = data sufficient and reliable; B = partially missing but does not affect the main conclusion; C = substantially missing, conclusion requires caution.

### 5.5 Data Points to Update

Explicitly list: which data are estimates, which data need later verification, and which quarter's earnings deserve focused tracking.

### 5.6 Source List

The source link for every data point/conclusion, listed by category (financials, sell-side research, news, industry reports).

---

## AI Research Bias Awareness (important)

Traps AI easily falls into during the funnel screen:

| Bias | Manifestation | Countermeasure |
|------|-----|------|
| Leader preference | Large-cap companies have more material and longer analysis, so they look "better" | Rank by hard metrics and moat score, not by report length |
| English preference | US-stock material is abundant, so A-shares/HK stocks get undervalued | Search in both Chinese and English; A/H companies cannot be missed |
| Story preference | High gains + media buzz = a "better-looking" AI-concept stock | Distinguish "AI revenue share" vs. "AI story share"; look at the real business |
| Present preference | Companies with good current financials get picked easily, possibly missing turnaround dark horses | The Layer-2 coarse screen allows "improving trend" as a relaxation condition |
| Listed preference | Looking only at listed companies may miss the best players in the track | Must list "future IPO candidates", noting valuation and timing window |

---

## Output Requirements

1. **Report location**: `reports/{industry}-funnel-{YYYYMMDD}.md` (industry reports go in the reports/ root directory)
2. **Language**: Chinese
3. **Style**: direct, sharp, no filler
4. **Data**: label the source of all data; mark estimates as "estimate"
5. **No preset stance**: lay out data → derive logic → reach conclusion
6. **Both sides**: attach a counter-argument to every core judgment
7. **Keep a rejection record at each layer**: dropped companies must also be named, with reasons

---

## Data Spot-Check (release audit)

After the report is written, run the data spot-check; only pass the audit before publishing:

```bash
# Step 1 — Extract the spot-check list (15% random sample)
python3 ~/ai-berkshire/tools/report_audit.py extract \
  --report <report file path>

# Step 2 — For each item on the list, pull data from a reliable source (see skills/financial-data.md)

# Step 3 — Output the pass/reject verdict
python3 ~/ai-berkshire/tools/report_audit.py verdict \
  --results '<filled-in JSON>' \
  --report <report file name>
```

**[PASS]** all checks pass → report can be published; **[REJECT]** any check fails → fix and re-audit.

---

## Follow-Up Actions

After the funnel selects the final 3, run each of these separately on every name:
- `/investment-team` — full four-master parallel deep research (separate subdirectory + 5 documents)
- `/investment-checklist` — run through Buffett's pre-purchase checklist end to end
- `/management-deep-dive` — management deep-dive

`industry-funnel` is the entry point; the follow-up skills are the deep dig.
