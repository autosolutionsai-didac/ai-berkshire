---
name: investment-checklist
description: "AI Berkshire skill: Buffett Value-Investing Pre-Buy Checklist. Source: skills/investment-checklist.md."
---

## Codex adapter note

This skill is generated from `skills/investment-checklist.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Commands that reference `~/ai-berkshire/tools/...` assume the repo is checked out at `~/ai-berkshire`; if needed, prefer the current workspace path.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Buffett Value-Investing Pre-Buy Checklist

Run the Buffett value-investing pre-buy Checklist analysis on $ARGUMENTS.

**Supported input formats**: one or multiple companies, separated by commas, enumeration marks, or spaces. For example: `Tencent, Kweichow Moutai, NVIDIA` or `NVDA AAPL MSFT`

## Execution Flow

### Step 1: Parse the input and identify every company to analyze

Parse all company names/tickers out of $ARGUMENTS. For each company, determine:
- Full company name, ticker, and listing exchange
- If the company is not listed, mark it as "private (unlisted)" and give a brief note (whether there is an indirect investment route), then skip the full Checklist

### Step 1.5: AI research bias warning

Give each company a quick "information-richness rating" (A/B/C) and flag it in the report:

| Grade | Criteria | Impact on the Checklist |
|------|---------|-----------------|
| Grade A | Listed for years, abundant data | Run normally, but beware the "consensus trap" — every metric looking clear does not mean it is truly certain |
| Grade B | Limited data, requires estimation | Tag every estimated metric with a confidence level; weight data reliability into the "good business" judgment |
| Grade C | Information extremely scarce | Do not force-fill the six-gate tables; honestly mark "insufficient data to judge" and focus on the verifiable core questions |

**Core principle**: the goal of the Checklist is to **screen out bad choices**. For Grade C companies, "insufficient data" does not equal "fail," nor does it equal "pass" — it should be honestly marked as "gray zone, needs additional primary information," rather than being rejected simply because the AI cannot fill out the table.

Duan Yongping once said: there are two kinds of "not understanding it" — one is the business is genuinely too complex to understand, the other is that you simply have not spent the time to look. The limitation of AI research is that it easily conflates "little information available" with "cannot understand it."

### Step 2: Parallel data collection

Use the Task tool to launch an independent background Agent for **each company** to collect data (all companies launched in parallel at the same time). Each Agent is responsible for collecting:

1. **Profitability**: ROE (5-10 year trend), gross margin, net margin, free cash flow
2. **Valuation data**: current share price, market cap, PE (TTM), forward PE, PB, dividend yield
3. **Growth trend**: revenue/profit growth over the past 3 years
4. **Financial health**: debt level, capex requirements, cash reserves, net cash/net debt
5. **Competitive landscape**: market share, key competitors, share-change trend
6. **Moat evidence**: concrete evidence of brand / switching cost / network effect / economies of scale / technical barriers
7. **Management track record**: CEO background, key decisions, shareholdings, capital-allocation record
8. **Latest developments**: major events over the past 6 months (earnings, M&A, regulation, management changes, etc.)

### Step 3: Run the six-gate Checklist company by company

For each listed company, pass through the six gates in order:

---

#### Gate 1: Can I understand this business? (circle of competence)

Must answer:
- [ ] Can you explain in one sentence how this company makes money?
- [ ] Will it most likely still be in the same business 10 years from now?
- [ ] Which key variables determine success or failure?
- [ ] Does your understanding of this industry come from deep research or hearsay?

**Scoring criteria** (★1-5):
- ★★★★★: business model is extremely simple and clear, high 10-year certainty (e.g., Kweichow Moutai: distill liquor, sell liquor)
- ★★★★☆: model is clear but has technical barriers, requiring some specialized knowledge to understand
- ★★★☆☆: model is understandable but 10-year certainty is low, industry changes fast
- ★★☆☆☆: business lines are complex or the industry is in upheaval, hard to foresee the future
- ★☆☆☆☆: entirely outside the circle of competence

**Hard veto**: if you cannot even explain how it makes money, immediately mark it "outside the circle of competence, no analysis."

---

#### Gate 2: Is this a good business? (economic characteristics)

Let the data speak; **key metrics must be computed precisely with the tool**:

```bash
python3 ~/ai-berkshire/tools/financial_rigor.py verify-valuation \
  --price {price} --eps {EPS} --bvps {book value per share} --fcf-per-share {FCF per share} --dividend {dividend per share}
```

| Metric | Company value | Reference standard | Judgment |
|------|-----------|---------|------|
| ROE (5-year average) | | >15% excellent, >20% outstanding | |
| Gross margin | | >40% implies pricing power | |
| Free cash flow | | consistently positive, ≈ net income | |
| Capex intensity | | asset-light beats asset-heavy | |
| Debt level | | interest-bearing debt / net income < 3 years | |

**Scoring criteria** (★1-5):
- ★★★★★: ROE > 25%, high gross margin, strong FCF, asset-light, low debt (all met)
- ★★★★☆: 4 items met
- ★★★☆☆: 3 items met
- ★★☆☆☆: 2 items met or the trend is deteriorating
- ★☆☆☆☆: most items unmet or FCF persistently negative

---

#### Gate 3: Is the moat deep enough? (competitive advantage)

Check item by item:

| Moat type | Present? | Concrete evidence | Widening or narrowing? |
|-----------|---------|---------|--------------|
| Brand / pricing power | | | |
| Switching cost | | | |
| Network effect | | | |
| Cost / scale advantage | | | |
| Technology / patent barrier | | | |

Additional test: if a competitor were given 10 billion, could they replicate this business?

**Scoring criteria** (★1-5):
- ★★★★★: multiple moats stacked and widening
- ★★★★☆: at least one strong moat and stable
- ★★★☆☆: has a moat but not deep enough, or trend unclear
- ★★☆☆☆: moat is being eroded
- ★☆☆☆☆: no obvious moat

---

#### Gate 4: Is management trustworthy? (the human factor)

| Check item | Assessment |
|--------|------|
| Honesty (promises vs. delivery) | |
| Capital-allocation ability (buyback / dividend / M&A record) | |
| Shareholder-interest orientation (shareholdings, compensation) | |
| Owner mentality (founder vs. professional manager) | |
| Corporate governance (related-party transactions, goodwill, audit) | |
| Can the company run as usual after the CEO leaves? | |

**Scoring criteria** (★1-5):
- ★★★★★: founder at the helm, outstanding capital allocation, fully aligned interests
- ★★★★☆: excellent management but with minor blemishes
- ★★★☆☆: management is competent but has governance concerns
- ★★☆☆☆: has integrity or governance issues
- ★☆☆☆☆: serious integrity problems (→ hard veto)

---

#### Gate 5: Is the price cheap enough? (margin of safety)

| Metric | Value | Historical percentile | Judgment |
|------|------|---------|------|
| PE (TTM) | | | |
| Forward PE | | | |
| PB | | | |
| Dividend yield | | | |
| FCF Yield | | | |

Additional test (**must be computed precisely with the tool; no mental math allowed**):
```bash
python3 ~/ai-berkshire/tools/financial_rigor.py three-scenario \
  --price {price} --eps {EPS} --shares {shares in 100M} \
  --growth {optimistic} {neutral} {pessimistic} --pe {optimistic PE} {neutral PE} {pessimistic PE} --currency {currency}
```
- Valuation range across the three scenarios (use the tool's output)
- If the judgment is wrong, how much do you lose at most by buying at the current price?
- If the share price halves, do you dare to add to the position?

**Scoring criteria** (★1-5):
- ★★★★★: below a 50% discount to intrinsic value, extreme margin of safety
- ★★★★☆: at a 30% discount, good margin of safety
- ★★★☆☆: fairly valued, ordinary margin of safety
- ★★☆☆☆: on the expensive side, insufficient margin of safety
- ★☆☆☆☆: severely overvalued

---

#### Gate 6: Position sizing and decision discipline (guarding against emotional loss of control)

Check the following emotional signals:
- Do you want to buy because of FOMO?
- Do you want to buy only because someone recommended it?
- If trading were suspended for 5 years, could you accept it?
- Can you write the buy thesis clearly in under 200 words?

---

### Step 4: The mirror test

Write out a mirror-test statement for each company:

> "I am buying ___ (company) at ___ per share, because:
> 1. The essence of this business is ___, and I understand it;
> 2. Its moat is ___, and it is widening/narrowing;
> 3. Management is ___, and is/is not trustworthy;
> 4. The current price equals a ___ discount to intrinsic value, with/without a sufficient margin of safety;
> 5. Even if I am wrong, the downside is controllable/uncontrollable, because ___."

**Cannot complete all 5 sentences = do not buy.** Clearly mark "pass" or "fail."

---

### Step 5: Quick veto list

Check each company against every item; triggering any one directly marks it "vetoed":

- [ ] Cannot explain clearly how this company makes money
- [ ] Free cash flow has been negative for 3 consecutive years with no improvement in sight
- [ ] Management has an integrity stain
- [ ] The competitive advantage is being irreversibly eroded
- [ ] Making money relies on "the next buyer paying an even higher price" (the greater-fool game)
- [ ] Cannot bear the consequences of this investment going to zero
- [ ] The main reason to buy is "everyone else is buying" or "it has risen a lot lately"
- [ ] Cannot write the buy thesis clearly in under 200 words

---

### Step 6: Output the overview comparison table (mandatory when analyzing multiple companies)

When analyzing multiple companies, you must generate a comparison overview table:

| Company | Checklist pass? | Circle of competence | Good business | Moat | Management | Margin of safety | Core conclusion |
|------|----------------|--------|--------|--------|--------|---------|---------|
| | | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | |

---

### Step 7: Final conclusion and writing to file

Give each company a clear conclusion (do not dodge):
- ✅ **Passes the Checklist** (X/6 gates) — may proceed to the deep-research stage
- ❌ **Fails the Checklist** — state which red line was triggered
- ❓ **Gray zone** — state what the key point of contention is and what the investor needs to judge for themselves
- N/A — private / cannot be bought

Write the complete report to `reports/{Company}/{Company}-checklist-{YYYYMMDD}.md` for a single company (date format YYYYMMDD); for the multi-company case use the root path `reports/multi-company-checklist-{YYYYMMDD}.md`

## Output format requirements

1. Each company gets its own section, containing: six-gate scoring table + core data table + key risks (3-5 items) + mirror test + clear conclusion
2. For multiple companies, append an overview comparison table at the end
3. All scores must use the ★ symbol (★1-5), no half-stars
4. All data must be tagged with its source date; estimated values must be marked "estimate"
5. Add a closing note at the end, echoing Buffett's maxim: "The first rule of investing is don't lose money"
6. Language style: direct, sharp, no filler. Weave in quotes from Buffett / Munger / Duan Yongping as commentary

## Key principles

- **Better to miss than to be wrong**: the goal of the Checklist is to screen out bad choices, not to find the best one
- **Be honest about your circle of competence**: if you don't understand it, say you don't; don't force the analysis
- **Margin of safety is the lifeline**: even a great company can lose you money if bought too expensively
- **The mirror test cannot be skipped**: if you can't state the reason clearly, don't buy — no exceptions
