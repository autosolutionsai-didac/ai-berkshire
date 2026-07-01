# Thesis Tracker: A Discipline System for the Post-Buy Period

Run a thesis-tracker check on $ARGUMENTS.

**Supported input formats**:
- `CompanyName` — on first use, build the investment thesis; on subsequent uses, run a tracking check
- `CompanyName build thesis` — force a rebuild of the investment thesis
- `CompanyName quarterly check` — run a thesis check based on the latest earnings report

> "Buying is just the beginning. The real work is the continuous tracking during the holding period." — Li Lu
>
> "When the facts change, I change my mind. What do you do?" — Keynes

## Design Philosophy

Most investors' process is: research → buy → pray. The absence of systematic post-buy tracking leads to:
- Not selling when you should ("just wait a bit longer, it'll come back")
- Panic-selling when you shouldn't ("it's down 20%, was I wrong?")
- Forgetting why you bought it in the first place ("wait, why did I buy this again?")

Buffett and Li Lu's approach is: **write down the sell conditions before you buy**. Then check every quarter whether the thesis is still intact.

## Execution Flow

### Step 1: Determine the operating mode

Check whether an investment thesis file already exists for the company (`reports/{Company}-thesis.md`):
- If it does not exist → enter **Build Thesis** mode
- If it exists → enter **Tracking Check** mode
- If you can't find it but the user says one exists → ask for the file path

---

## Mode A: Build the Investment Thesis

### A0: Data collection

Use WebSearch to obtain the current share price, valuation metrics (PE/PB/dividend yield), and the core figures from the latest earnings report, to fill in the valuation anchors. If a `/investment-research` or `/investment-team` report already exists for the company, read from it first.

Use `tools/financial_rigor.py verify-valuation` to validate the valuation data.

### A1: Core thesis (must be written clearly in under 200 words)

The investment thesis must answer the following 5 questions, one sentence each:

```
I bought ___Company at ___ per share, because:
1. The essence of this business is ___, and I understand how it makes money
2. Its moat is ___, and it is widening / stable
3. Management ___, and the reason they are trustworthy is ___
4. The current price is at a ___ discount to intrinsic value, and the margin of safety comes from ___
5. Even if I'm wrong, the downside is contained, because ___
```

**If you can't complete these 5 sentences, the thesis itself has a problem — it means the buy decision wasn't clear enough.**

### A2: Core assumptions list

Break the investment thesis down into specific, verifiable assumptions:

| # | Core assumption | Verification method | Frequency | Current status |
|---|---------|---------|---------|---------|
| 1 | e.g. Revenue growth stays at 15%+ | Quarterly revenue growth | Each quarter | 🟢 Holds |
| 2 | e.g. Gross margin stable at 60%+ | Quarterly gross margin | Each quarter | 🟢 Holds |
| 3 | e.g. Management keeps buying back shares | Buyback announcements / cash flow statement | Each quarter | 🟢 Holds |
| 4 | e.g. Competitors make no breakthrough | Industry data / competitor earnings | Every six months | 🟢 Holds |
| 5 | ... | ... | ... | ... |

Usually 3-7 assumptions. Too few means the thinking wasn't deep enough; too many means the thesis isn't focused enough.

### A3: Red-line list (triggering any one = mandatory re-evaluation)

| # | Red-line condition | Severity | Action when triggered |
|---|---------|---------|-----------|
| 1 | e.g. Management integrity breaks down (accounting fraud, related-party transactions) | Fatal | Exit immediately |
| 2 | e.g. Core business revenue declines for 2 consecutive quarters | Severe | Trim 50%, re-evaluate |
| 3 | e.g. Moat is clearly breached (a competitor gains equivalent capability) | Severe | Launch deep research, consider exit |
| 4 | e.g. Regulation fundamentally changes the business model | Severe | Re-estimate intrinsic value |
| 5 | e.g. Large-scale, unplanned insider selling by management | Warning | Investigate the reasons in depth |

**Duan Yongping**: "There are only three reasons to sell: 1. you realize you made a mistake; 2. the company's fundamentals have changed; 3. you've found something better."

### A4: Valuation anchors

| Metric | At purchase | Optimistic target | Neutral target | Pessimistic case |
|------|-------|---------|---------|---------|
| Share price | | | | |
| PE | | | | |
| Market cap | | | | |
| Intrinsic-value estimate | | | | |
| Margin of safety | | | | |

### A5: Save the thesis

Write the investment thesis to `reports/{Company}-thesis.md`, including:
- Date established
- Purchase price and position size
- Core thesis (5 sentences)
- Core assumptions list
- Red-line list
- Valuation anchors
- Tracking-record table (initially empty)

---

## Mode B: Tracking Check

### B1: Read the existing thesis

Read `reports/{Company}-thesis.md` and load:
- Core thesis
- Core assumptions list
- Red-line list
- Last check record

### B2: Gather the latest data

Use WebSearch to collect:
1. Latest earnings data (if there is a new quarterly / annual report)
2. Recent major events (management changes, regulatory policy, competitive dynamics)
3. Current share price and valuation metrics
4. Insider-trading records (buying/selling by major shareholders)

### B3: Check each core assumption

For each core assumption, verify it against the latest data:

| # | Core assumption | Last status | Latest evidence | Current status | Change |
|---|---------|---------|---------|---------|------|
| 1 | Revenue growth 15%+ | 🟢 Holds | Q4 revenue growth 12% | 🟡 Weakening at the margin | ⚠️ |
| 2 | Gross margin 60%+ | 🟢 Holds | Gross margin 61.2% | 🟢 Holds | — |
| 3 | ... | ... | ... | ... | ... |

Status definitions:
- 🟢 **Holds** — the latest data supports the assumption
- 🟡 **Weakening at the margin** — data is still within an acceptable range, but the trend is unfavorable
- 🔴 **Impaired** — data clearly does not support the assumption
- ⚫ **Broken** — the assumption has been disproven

### B4: Red-line check

Check the red-line list item by item:

| # | Red-line condition | Triggered? | Evidence |
|---|---------|:-------:|------|
| 1 | Management integrity issue | ❌ Not triggered | — |
| 2 | Core business declines 2 straight quarters | ❌ Not triggered | — |

**If any red line is triggered → flag it prominently in the report and give a clear action recommendation.**

### B5: Valuation update

| Metric | At purchase | Last check | Current | Change |
|------|-------|---------|------|------|
| Share price | | | | |
| PE (TTM) | | | | |
| Intrinsic-value estimate | | | | |
| Margin of safety | | | | |

### B6: Output the tracking report

#### Report structure

```
1. Thesis health score (out of 10)
2. Core-assumption check results (table)
3. Red-line check results (table)
4. Key changes this period (under 500 words)
5. Valuation update
6. Conclusion and action recommendation
7. Focus points to watch at the next check
```

#### Thesis health scoring standard

| Score | Meaning | Recommended action |
|:----:|------|---------|
**Formula**: Health = 10 - (⚫ broken assumptions × 3) - (🔴 impaired assumptions × 2) - (🟡 weakening assumptions × 1) - (red lines triggered × 5), floored at 1 and capped at 10.

| Score | Meaning | Recommended action |
|:----:|------|---------|
| 9-10 | All assumptions hold; thesis is stronger than at purchase | Consider adding to position |
| 7-8 | Core assumptions hold; a few weakening at the margin | Keep holding |
| 5-6 | 1-2 assumptions impaired, but core logic unchanged | Hold, but stay more vigilant |
| 3-4 | Several assumptions impaired; the thesis foundation is shaken | Consider trimming |
| 1-2 | A red line is triggered or a core assumption is broken | Strongly recommend selling |

#### The conclusion must clearly answer

1. **Is the thesis still intact?** Intact / Weakening at the margin / Impaired / Broken
2. **What to do?** Add to position / Hold / Trim / Exit
3. **Next check timing**: After the next earnings release / after a specific event

### B7: Update the thesis file

Append this check record to the tracking-record table in `reports/{Company}-thesis.md`:

| Check date | Health | Key change | Action recommendation |
|---------|:------:|---------|---------|
| 2026-04-09 | 7/10 | Revenue growth slowed to 12%, but margins improved | Hold |

---

## Key Principles

- **Write the sell conditions before you buy** — decisions made when calm beat those made in panic
- **Make the thesis specific enough to verify** — "great company" is not a thesis; "ROE > 25% with a stable trend" is
- **Act the moment a red line is triggered** — the worst move is "let's just wait and see"; that's the start of a big loss
- **Thesis broken ≠ share price falling** — a 30% drop doesn't necessarily mean sell; a broken thesis does
- **Face mistakes honestly** — if the thesis was built wrong, admit it; don't tough it out to save face
