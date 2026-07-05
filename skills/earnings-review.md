# Earnings Deep-Read: In-Depth Reading of Primary Sources

Perform an earnings deep-read analysis of $ARGUMENTS.

**Supported input formats**: `company period`, e.g., `Tencent 2025Q4`, `PDD 2025 annual report`, `Meituan latest` (defaults to the most recent period).

> "I never read sell-side research; I only read the original filings." — Li Lu
>
> "I read 500 pages a day. That's how knowledge builds up, like compound interest." — Buffett

## Design Philosophy

Most AI investment-research tools rely on secondhand information (news, research-report summaries, data websites). But the core skill of Buffett and Li Lu is **reading primary sources** — annual reports, quarterly reports, earnings-call transcripts.

The problems with secondhand information:
- It has been filtered — analysts selectively present the data that favors their views
- It lags — by the time others have digested it, the alpha is gone
- It lacks context — "revenue grew 15%" is divorced from management's discussion of the quality of that growth

This skill reads primary sources directly, focusing on what Buffett and Li Lu actually look at.

## Execution Flow

### Preliminary Step: Source Availability Rating

| Grade | Characteristics | Impact |
|------|------|------|
| Grade A | Full original text obtained (10-K / annual report / earnings-call transcript) | Execute all steps normally |
| Grade B | Only partial original text or third-party summaries obtained | Flag "non-primary source," lower the weight of footnote analysis |
| Grade C | Only news coverage and data-website summaries available | Focus on core financial-data changes, skip footnote mining, flag "insufficient primary sources" |

### Step 1: Obtain Primary Sources

Use the Task tool to launch multiple background Agents to obtain the following original materials **in parallel**:

1. **Original filings**: obtain from the company IR page, SEC EDGAR (US stocks 10-K/10-Q), HKEX disclosure (HK stocks), CNINFO (A-shares)
2. **Earnings-call transcripts / recordings**: obtain from Seeking Alpha, the company IR page, Xueqiu, etc.
3. **Management's letter to shareholders** (if an annual report): read in full
4. **Investor-day / analyst-day materials** (if any recent)

If the full original text cannot be obtained, piece it together using standard data sources per the `skills/financial-data.md` conventions (US stocks: macrotrends+stockanalysis; HK stocks: aastocks+macrotrends; A-shares: East Money+CNINFO), but you must flag "not the original filing, drawn from third-party summaries," and mark any key data point where two sources diverge by >1%.

### Step 2: Core Financial Data Extraction and Verification

#### 2.1 Income Statement

| Metric | Current period | Prior period | YoY change | Management guidance | Met target? |
|------|------|------|---------|-----------|---------|

Must cover:
- Total revenue and revenue breakdown by segment / by region
- Gross profit, change in gross margin
- Operating profit, change in operating margin (distinguish GAAP vs Non-GAAP)
- Net profit (note the impact of non-recurring items)
- EPS (basic vs diluted)

#### 2.2 Cash Flow Statement (Buffett's top priority)

| Metric | Current period | Prior period | Change | Focus point |
|------|------|------|------|--------|

Must cover:
- Operating cash flow vs net profit ratio (>100% is good, <80% warrants caution)
- Capex and its composition (maintenance vs expansion)
- Free cash flow = operating cash flow − capex
- Buyback amount, dividend amount
- Cash and equivalents ending balance

#### 2.3 Balance Sheet Health

Must cover:
- Cash + short-term investments vs interest-bearing debt
- Trend in net cash / net debt change
- Change in accounts-receivable turnover days (is credit being loosened to pull revenue forward?)
- Change in inventory turnover days (is inventory piling up?)
- Goodwill and intangible assets as a share of assets (any impairment risk?)

**Data verification**: use `tools/financial_rigor.py` to verify key data:

```bash
# Cross-validate revenue and net profit (at least 2 sources)
python3 ~/ai-berkshire/tools/financial_rigor.py cross-validate \
  --metric "revenue" --values 108.3e9 107.9e9 --sources "Company filing" "Yahoo Finance"

# Market-cap check
python3 ~/ai-berkshire/tools/financial_rigor.py verify-market-cap \
  --price 101 --shares 1.488e9 --reported 1.44e11 --currency USD

# Valuation-metric verification
python3 ~/ai-berkshire/tools/financial_rigor.py verify-valuation \
  --price 101 --eps 9.6 --bvps 26.5 --fcf-per-share 10.2
```

### Step 3: Deep-Read of Management Discussion (MD&A)

This is the part where Buffett and Li Lu spend the most time. It's not about reading the numbers — it's about **listening to how management talks**.

#### 3.1 Management Tone Analysis

Read the management discussion / earnings-call remarks paragraph by paragraph, and flag the following signals:

| Signal type | Concrete manifestation | Example |
|---------|---------|------|
| 🟢 **Candor signal** | Proactively admits problems, gives specific reasons | "The margin decline this quarter is mainly because our investment in area X exceeded expectations" |
| 🟢 **Clarity signal** | Specific strategy statements with quantified targets | "We plan to raise business X's market share from 15% to 20% over the next 12 months" |
| 🔴 **Vagueness signal** | Heavy use of empty phrases like "we believe" and "over the long run" | "We are confident about the future" |
| 🔴 **Deflection signal** | Dodges direct questions, changes the subject | Asked about margins, pivots to revenue growth |
| 🔴 **Externalized attribution** | Blames problems entirely on macro / industry / competitors | "Due to the macro environment..." |

#### 3.2 Promise Tracking

Extract management's specific promises from the prior period's earnings report / call, and compare with actual results this period:

| Prior-period promise | This-period delivery | Assessment |
|---------|------------|------|
| "Margins will recover to X% in the second half" | Actual Y% | ✅ Met / ❌ Missed / ⚠️ Partially met |

**Duan Yongping**: "The simplest way to tell whether a management team is reliable is to check whether they did what they said they'd do."

#### 3.3 Key-Question Identification

Extract the sharpest analyst questions from the earnings-call Q&A, along with the quality of management's answers:

| Analyst question | Management answer | Answer quality (1-5) | Evasive? |
|-----------|-----------|:------------:|:-------:|

### Step 4: Footnote and Hidden-Information Mining

The footnotes hide information management doesn't want you to see easily:

#### 4.1 Must-Check Footnote Items

- [ ] **Related-party transactions**: are the terms with the major shareholder / related parties at arm's length?
- [ ] **Stock-based compensation**: how large is the dilution from options / RSUs? What's the strike price?
- [ ] **Contingent liabilities**: off-balance-sheet risks such as litigation, guarantees, commitments
- [ ] **Accounting-policy changes**: has revenue recognition, depreciation life, etc. been changed?
- [ ] **Segment information**: margin differences across businesses, is a "good business subsidizing a bad business"?
- [ ] **Customer / supplier concentration**: share of the top five customers / suppliers

#### 4.2 Anomaly Detection

- [ ] Accounts-receivable growth > revenue growth (may be channel stuffing)
- [ ] Inventory growth > revenue growth (may be piling up)
- [ ] Operating cash flow < net profit with the gap widening (earnings quality in doubt)
- [ ] Capitalized expenditures suddenly increase (may be dressing up profit)
- [ ] Share of non-recurring gains suddenly rises

### Step 5: Comparison with Historical Data

#### 5.1 Trend Analysis

Place this period's key metrics into a time series of at least 4 quarters (or 3 annual reports):

| Metric | Q-4 | Q-3 | Q-2 | Q-1 | Current | Trend read |
|------|-----|-----|-----|-----|------|---------|

Focus on:
- Are margins improving or deteriorating?
- Is revenue growth accelerating or decelerating?
- Is cash-flow quality rising or falling?
- Is capex intensity increasing or decreasing?

#### 5.2 Comparison with Management Guidance

| Metric | Management's prior guidance | Actual result | Deviation | Interpretation |
|------|--------------|---------|------|------|

### Step 6: Output the Deep-Read Report

#### Report Structure

```
1. Core-data snapshot (one-page table)
2. The 3 most important changes this period (no more than 500 words)
3. Management tone and promise tracking
4. Hidden information in the footnotes
5. Key questions (curated earnings-call Q&A)
6. Relationship to the investment thesis (if holding a position)
7. Conclusion: what did this earnings report change?
```

#### The Conclusion Must Clearly Answer

1. **Was this earnings report a beat, in line, or a miss?** (Don't say "basically in line" and then list a pile of two-sided hedges)
2. **Impact on the investment thesis**: strengthens / no impact / weakens / breaks
3. **What is the next catalyst to watch?**
4. **If you already hold, should you add / hold / trim?**

### Step 7: Save the Report

Write the report to `reports/{Company}/{Company}-earnings-{period}.md`, e.g., `reports/Tencent/Tencent-earnings-2025Q4.md`

### Step 8: Data Spot-Check (Release Audit)

After the report is written, run the data spot-check; only a pass allows release:

```bash
# Step 1 — Extract the spot-check list
python3 ~/ai-berkshire/tools/report_audit.py extract \
  --report reports/{Company}/{Company}-earnings-{period}.md

# Step 2 — For each item on the list, pull data from a reliable source (see skills/financial-data.md)

# Step 3 — Output the pass/reject verdict
python3 ~/ai-berkshire/tools/report_audit.py verdict \
  --results '<filled-in JSON>' \
  --report {report_filename}
```

**[RELEASE]** All checks pass → release; **[SEND BACK]** Any check fails → fix and re-audit.

## Key Principles

- **Read the original, not the summary**: obtain primary sources by every means possible
- **Watch the change, not the absolute value**: the trend matters more than the number itself
- **Listen to the tone, not just the content**: how management says it matters as much as what they say
- **Check the footnotes, not just the main text**: the devil is in the details
- **Give a conclusion, don't just summarize**: the purpose of a deep-read is to form a judgment, not to restate the earnings report
