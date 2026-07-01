---
name: investment-research
description: "AI Berkshire skill: Investment Research: The Buffett-Munger-Duan Yongping-Li Lu Four-Master Comprehensive Analysis Framework. Source: skills/investment-research.md."
---

## Codex adapter note

This skill is generated from `skills/investment-research.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Commands that reference `~/ai-berkshire/tools/...` assume the repo is checked out at `~/ai-berkshire`; if needed, prefer the current workspace path.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Investment Research: The Buffett-Munger-Duan Yongping-Li Lu Four-Master Comprehensive Analysis Framework

Conduct systematic investment research analysis on $ARGUMENTS.

## Research Framework

Grounded in the methodologies of four investing masters — Buffett, Munger, Duan Yongping, and Li Lu — execute the research across the following seven modules in order:

### Preliminary Step: AI Research-Bias Self-Awareness (mandatory)

Before beginning research, first assess the company's "AI researchability" and identify potential data biases:

**Information-richness rating**:
| Level | Characteristics | AI research trap | Countermeasure |
|------|------|-----------|---------|
| Level A (information-abundant) | Listed for many years, heavy sell-side coverage, dense media reporting | Consensus is too strong; AI output converges toward market pricing, leaving limited alpha | Focus on the contrarian test: why don't smart people buy? What risk is being overlooked? |
| Level B (information-moderate) | Listed 1-3 years, limited coverage, some data must be inferred | AI may fill gaps with "reasonable speculation" — looks complete but is false certainty | Tag every inferred data point with a confidence level; distinguish "evidence-based inference" from "fabricated filler" |
| Level C (information-scarce) | Newly listed / obscure stock / emerging market, almost no coverage | AI turns overly conservative for lack of material, mistaking "can't see clearly = bad" | Ask first-principles questions (see below); extract the business essence from limited information |

**First-principles research method for Level C companies**:
When public material is insufficient, do not try to piece together a report that "looks complete." Instead, focus on these underlying questions:
1. Who is the customer? Why do they pay? Is there an alternative?
2. What drives repeat purchases? Is it habit, lock-in, or the continuous creation of new value?
3. Could a competitor replicate this business with 10 billion in capital?
4. What key decisions has management made? What judgment and values do those decisions reflect?

**Bias self-check list** (stay vigilant throughout the research):
- [ ] Does my sense of "certainty" come from the essence of the business, or from the volume of material?
- [ ] If I halved the amount of material on this company, would my conclusion change?
- [ ] Is the AI's analysis highly similar to market consensus? If so, where is my informational edge?
- [ ] Is the possibility of "very little public material but an excellent business" being underrated?

Write the information-richness rating at the start of the report, and in the final conclusion note the distinction between "AI research confidence" and "actual investment certainty."

### Step 1: Data Collection

> **Data-source standard**: See `skills/financial-data.md`. All financial data must come from two independent sources; discrepancies >1% must be flagged.
> - US stocks: macrotrends (primary) + stockanalysis (secondary)
> - HK stocks: aastocks (primary) + macrotrends ADR (secondary)
> - A-shares: East Money (primary) + CNINFO (secondary)

Use the Task tool to launch a background Agent that collects the following data from the web:

1. Revenue structure: segment revenue, growth rates, and gross margins for the most recent fiscal year and the last 4 quarters
2. Financial metrics: revenue, net profit, gross margin, operating margin, free cash flow, and cash reserves over the past 5 years
3. Competitive landscape: market share and comparison with major competitors
4. Business model and moat: sources of core competitive advantage
5. Technical capabilities: core technology stack, R&D investment
6. Management: founder/CEO background, ownership stake, record of key decisions
7. Industry outlook: TAM (total addressable market), growth forecasts
8. Risk factors: geopolitics, regulation, supply chain, etc.
9. Current valuation: market cap, PE, PS, PEG, EV/Revenue
10. Core arguments from both bulls and bears

#### Data cross-validation (mandatory; use the financial-rigor tool)

After data collection is complete, **you must call `tools/financial_rigor.py` to programmatically verify the key data**, eliminating LLM mental-math errors.

**Data points that must be verified**:
- Total shares outstanding (confirmed from at least 2 sources such as the exchange, Yahoo Finance, StockAnalysis)
- Current share price and market cap (**manually compute price × total shares and compare against the reported market cap to guard against unit errors**)
- Most recent fiscal-year revenue and net profit (confirmed from the company annual report + at least 1 third-party source)
- Cash reserves and net cash (cash + short-term investments − total debt; watch for definitional differences)
- Management ownership stake (distinguish economic interest from voting rights; watch for dual-class AB-share structures)

**Mandatory verification steps (invoke the tool via Bash)**:

Step 1 — Market-cap recomputation (exact decimal, not floating point):
```bash
python3 ~/ai-berkshire/tools/financial_rigor.py verify-market-cap \
  --price {price} --shares {total_shares} --reported {reported_market_cap} --currency {currency}
```

Step 2 — Multi-source cross-validation of key data:
```bash
python3 ~/ai-berkshire/tools/financial_rigor.py cross-validate \
  --field {field_name} --values '{"source1": value, "source2": value}' --unit {unit}
```
Execute this separately for revenue, net profit, and cash reserves.

Step 3 — Exact recomputation of valuation metrics (PE/PB/ROE/FCF Yield, etc.):
```bash
python3 ~/ai-berkshire/tools/financial_rigor.py verify-valuation \
  --price {price} --eps {EPS} --bvps {book_value_per_share} --fcf-per-share {FCF_per_share} --dividend {dividend_per_share}
```

**Verification rules**:
1. At least 2 independent sources for each key data point
2. When sources differ, prefer company annual reports / exchange data, and note the reason for the discrepancy
3. **All data involving calculation must be verified through the tool; LLM mental math is prohibited**
4. Embed the tool's output directly into the report appendix, "Key Data Cross-Validation Record"
5. If the tool reports ❌ excessive deviation, you must investigate the cause before continuing the analysis

**Common-error safeguards**:
- Market-cap units: HKD 100M vs RMB 100M vs USD 100M — easy to drop or add a zero
- FCF definition: different sources may define capital expenditure differently (whether leases, acquisitions, etc. are included)
- Debt definition: whether operating-lease liabilities are included
- Ownership stake: for AB-share companies, economic interest ≠ voting rights

### Step 2: Business-Essence Analysis — Duan Yongping's "the right business"

Analytical points:
- Define the essence of this business in one sentence
- Break down the revenue structure (chart)
- 5-year profitability trend (chart)
- Business-model canvas: one-time sale vs subscription/repeat purchase? Hardware vs software vs platform?
- Ecosystem stickiness / strength of customer lock-in
- Gross-margin level versus peers, explaining why it is high/low
- Operating-leverage analysis
- **Duan Yongping-style probe**: What makes this business good? If you could describe it in only one sentence, what would it be?

### Step 3: Moat Assessment — Buffett's "economic moat"

Verify each of the five moat types one by one:

| Moat type | Verification method |
|-----------|---------|
| Brand / pricing power | Can it raise prices without losing volume? |
| Switching cost | How costly is it for customers to migrate to a competitor? |
| Network effect | Does the product get better as more users join? |
| Economies of scale | How large is the cost advantage that scale brings? |
| Technology / patent barrier | How many years ahead is the technology? Can it be replicated? |

Analyze the moat trend: has it widened or narrowed over the past 5 years? Forecast the next 5 years.

**Buffett-style probe**: Will this moat still be here in 10 years? What could destroy it?

### Step 4: Inversion and Risk Checklist — Munger's "invert, always invert"

- List "all the paths by which this company could fail" (table: path / probability / severity)
- Historical analogy: find companies that were historically in a similar position — how did they end up?
- Cross-disciplinary analysis: cross-check using models such as network-effect theory, technology-adoption curves, and competitive game theory
- Bias self-check: narrative bias, anchoring effect, survivorship bias
- Collect the core arguments of the bears

**Munger-style probe**: Where am I most likely to be wrong? Why would smart people refuse to buy / short this company?

### Step 5: Management Assessment — Duan Yongping's "the right people" + Buffett's "management integrity"

- Review of the CEO/founder's key decisions (table: date / decision / outcome / rating)
- Capital-allocation ability: R&D return on investment, M&A success rate, timing of buybacks
- Alignment with shareholder interests: management ownership, compensation structure, insider-selling record
- Organizational capability: team stability, key-person risk
- Corporate-culture characteristics

**Duan Yongping-style probe**: If the CEO retired, could this company stay competitive?

### Step 6: Industry and Civilizational Trends — Li Lu's "civilizational-evolution framework"

- Judge whether the industry is undergoing a "civilization-scale paradigm shift"
- Historical technology-revolution analogies (steam engine / electricity / internet / AI)
- TAM growth-curve and ceiling analysis
- The company's position within the industry value chain
- Technology-roadmap risk
- Customer/supplier concentration analysis

**Li Lu-style probe**: Looking back from 20 years in the future, is this company "the Standard Oil of its era" or "a flash-in-the-pan 3Com"?

### Step 7: Valuation and Margin of Safety — Buffett's "intrinsic value" + Duan Yongping's "the right price"

- Current market pricing (table of key valuation metrics) — **must be verified through the tool**
- Reverse DCF: what growth expectations does the current share price imply?
- Three-scenario valuation — **must be computed precisely through the tool; mental math is prohibited**:
```bash
python3 ~/ai-berkshire/tools/financial_rigor.py three-scenario \
  --price {price} --eps {EPS} --shares {total_shares_in_100M} \
  --growth {bull_growth} {base_growth} {bear_growth} \
  --pe {bull_PE} {base_PE} {bear_PE} --years 3 --currency {currency}
```
- Compare against the company's own historical valuation
- Compare against peer valuations

**Duan Yongping-style probe**: If the stock market closed for 5 years starting tomorrow, would you be willing to hold at this price?

### Step 8: Comprehensive Decision Memo

Summary table:

| Dimension | Conclusion | Confidence |
|------|------|--------|
| Business quality (Duan Yongping) | | |
| Moat (Buffett) | | |
| Management (Duan Yongping + Buffett) | | |
| Biggest risk (Munger) | | |
| Civilizational trend (Li Lu) | | |
| Valuation (Buffett + Duan Yongping) | | |

Final decision table:

| Strategy | Recommendation |
|------|------|
| Those with no position | |
| Those holding a position | |
| Sell signal | |
| Add-to-position signal | |

Simulated commentary from the four masters (in blockquote format).

## Output Requirements

1. All analysis must be data-backed, with data sources attached
2. Present key data using Markdown tables
3. Each module must end with the corresponding master's "probe"
4. Finally, write the complete report to `~/[Company]-investment-research-report.md`
5. The conclusion must be clear; do not shy away from giving a buy / wait-and-see / avoid recommendation
6. The valuation section must give a specific price range
7. **The start of the report** must include the "information-richness rating" (A/B/C) and an "AI research-limitations statement"
8. **The end of the report** must distinguish "AI-analysis confidence" from "investment certainty" — the former depends on the volume of material, the latter on the essence of the business. Clearly tell the reader which conclusions in the report are based on sufficient data and which are based on reasoning from limited information
9. If the company is Level C (information-scarce), the report must end with a "checklist of questions requiring first-hand verification" — recommend that the reader fill the AI's blind spots through methods such as field research, product hands-on experience, and supply-chain interviews

## Data Spot-Check (release audit)

After the report is written to file, **you must** run a data spot-check; it may only be published after passing:

**Step 1 — Extract the spot-check list (15% random sample):**
```bash
python3 ~/ai-berkshire/tools/report_audit.py extract \
  --report <report_file_path>
```
Outputs a JSON template, each item containing `fetched_value` (to be filled in).

**Step 2 — Pull and verify the data:**
For each data point in the list, pull data from reliable sources per the `skills/financial-data.md` standard
(US stocks: macrotrends+stockanalysis; HK stocks: aastocks+macrotrends; A-shares: East Money+CNINFO),
and fill in `fetched_value` / `fetched_source` / `fetched_value2` / `fetched_source2`.

**Step 3 — Output the verdict:**
```bash
python3 ~/ai-berkshire/tools/report_audit.py verdict \
  --results '<filled-in JSON>' \
  --report <report_file_name>
```

- **[Release]**: all spot-check points deviate ≤ 1% → the report may be published
- **[Reject]**: any point deviates > 1% → fix the corresponding data and re-run the spot-check until it passes
