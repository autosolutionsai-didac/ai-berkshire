# Quality Screen: 7 Metrics to Quickly Rule Out Non-First-Class Companies

Run the quality screen on $ARGUMENTS to quickly rule out names that fail to meet first-class company standards.

**Supported input formats**:

| Input type | Example | Notes |
|---------|------|------|
| Single stock | `Tencent, Meituan, NVIDIA` | Screen each company one by one |
| Industry | `China beer industry` `global cloud computing` `HK sportswear brands` | First search for the industry's major listed companies (10-20), then screen each |
| Market/Index | `Hang Seng Index constituents` `CSI 300` `Nasdaq 100` | Pull the constituent list, then screen each |
| Theme | `China's top 50 high-dividend stocks` `global AI-compute chain` | First search for theme-related companies, then screen each |

In industry/market/theme mode, the output additionally includes: pass-rate statistics, in-industry rankings, and a sector-comparison summary.

## Design Principles

- **Goal**: Never wrongly kill a first-class company, but reliably rule out companies that are clearly not first-class
- **Logic**: 7 hard metrics + 2 exemption rules; better to let one slip through than to kill one by mistake
- **Scope**: All listed companies (banks/insurers are exempt from metric #3, interest coverage)

---

## The 7 Quality-Screen Metrics

| # | Metric | Exclusion condition | What it measures |
|---|------|---------|-------------|
| 1 | 10-year average ROE | < 8% | Capital efficiency — can shareholders' money beat its opportunity cost |
| 2 | 5-year cumulative free cash flow | Negative | Hard cash — is the profit "paper wealth" |
| 3 | Interest coverage (EBIT/interest) | < 2x | Solvency safety — ability to service interest |
| 4 | Long-term gross margin | < 15% | Pricing power — is the product/service differentiated |
| 5 | Operating cash flow / net income (5-year average) | < 0.7 | Earnings quality — can reported profit be turned into cash |
| 6 | Long-term net margin | < 5% | Risk resilience — does profit go to zero when revenue wobbles |
| 7 | 5-year share-count inflation | > 20% (non-M&A reasons) | Shareholder interest — is management diluting your stake |

## The 3 Exemption Rules

### Exemption A: Strategic-investment-phase exemption (applies to metric #1)

If all 3 of the following conditions are met, metric #1 (ROE below threshold) can be waived:
1. Listed for less than 10 years
2. Gross margin > 30% (proves the business model itself has pricing power)
3. Operating cash flow positive in the most recent 2 years (proves the cash-generating ability is already in place)

**Logic**: High gross margin + turning cash-flow positive shows the business model is sound; the low ROE is only because the company is still in its investment phase. Typical case: Meituan.

### Exemption B: Deliberately-low-margin exemption (applies to metric #6)

If both of the following conditions are met, metric #6 (net margin below threshold) can be waived:
1. Gross margin > 30% (able to earn but choosing not to)
2. Net margin has recovered above 5% in the past 2 years, or shows a clear upward trend

**Logic**: A high gross margin indicates pricing power; the low net margin is a strategic choice (reinvestment) rather than a lack of ability. Typical case: Amazon.

### Exemption C: High-turnover thin-margin model exemption (applies to metrics #4 and #6)

If all 3 of the following conditions are met, metric #4 (gross margin) and metric #6 (net margin) below threshold can be waived:
1. ROE > 20% (proves that despite low margins, return on capital is extremely high)
2. Operating cash flow / net income > 1.0 (no issue with earnings quality)
3. The business model is of the "membership / platform commission / high-turnover thin-margin" type (profit is not embedded in product markups)

**Logic**: For some first-class companies, profit is not hidden in the gross margin but in membership fees, turnover efficiency, or platform take rates. Their gross and net margins are naturally very low, but an extremely high ROE shows first-class capital efficiency. Typical case: Costco (12% gross margin, 2.5% net margin, but ROE 25%+ and membership renewal rate 90%+).

---

## Execution Flow

### Step 1: Parse the input and determine the screening scope

**Mode determination**:
- If the input is a specific company name/ticker → **single-stock mode**, go directly to Step 2
- If the input is an industry/market/theme → **batch mode**, first do the following:
  1. Use WebSearch to search for the major listed companies in that industry/market/theme
  2. Industry mode: cover the top 15-20 listed companies by market cap in that industry
  3. Index mode: pull the full constituent list
  4. Theme mode: search for related companies, covering 15-30
  5. List the full company roster for confirmation (if >30 companies, process in parallel batches)

For each company, determine its full name, ticker, and exchange.

### Step 2: Parallel data collection

Launch an independent background Agent for each company, using WebSearch to gather the following data:

1. **ROE**: year-by-year ROE for the past 10 years (or since IPO), and compute the average
2. **Free cash flow**: operating cash flow and capex for the past 5 years, and compute 5-year cumulative FCF
3. **Interest coverage**: latest annual EBIT and interest expense, and compute the ratio
4. **Gross margin**: gross-margin trend over the past 5 years
5. **Operating cash flow / net income**: the ratio over the past 5 years, and compute the average
6. **Net margin**: net-margin trend over the past 10 years, and compute the average
7. **Change in share count**: total shares 5 years ago vs. now, and compute the inflation ratio

Data-source priority: company annual reports > brokerage research > financial-data platforms

### Step 3: Test each metric in turn

For each company, test the 7 metrics one by one:
- ✅ Pass
- ❌ Fail
- ⚠️ Borderline (with a numeric note)

If a metric is breached, check whether the corresponding exemption condition is met.

### Step 4: Output the result

#### Output format

```markdown
# Quality-Screen Results

**Screening date**: {today's date}
**Number of companies**: {N}

## Summary table

| Company | ①ROE | ②FCF | ③Interest cov. | ④Gross margin | ⑤OCF/NI | ⑥Net margin | ⑦Dilution | Result |
|------|------|------|----------|---------|---------|---------|-------|------|
| xxx | ✅ 24% | ✅ | ✅ | ✅ 56% | ✅ | ✅ 30% | ✅ | **Pass** |
| yyy | ❌ 3% | ❌ | ❌ | ✅ 20% | ✅ | ❌ 2% | ✅ | **Excluded** |
| zzz | ⚠️→✅ | ✅ | ✅ | ✅ 35% | ✅ | ⚠️→✅ | ✅ | **Pass via exemption** |

## Companies that passed (N)
[list]

## Companies excluded (N)
| Company | Metric breached | Specific data | Reason for exclusion |
|------|---------|---------|---------|

## Companies that passed via exemption (N)
| Company | Exemption clause | Specific data | Exemption rationale |
|------|---------|---------|---------|

## Borderline disputes (if any)
[supplementary notes on companies near a threshold]

## Sector summary (industry/market mode only)

**Pass rate**: {passed}/{total} = {percentage}
**Industry-quality assessment**: [assess the overall quality of the industry based on the pass rate]

| Quality tier | Companies | Common traits |
|---------|------|---------|
| First-class (all passed + high ROE) | xxx, yyy | ... |
| Qualified (all passed but mediocre metrics) | aaa, bbb | ... |
| Eliminated | ccc, ddd | ... |

**Industry stock-selection conclusion**: [one line on whether the industry is worth digging into, and which 2-3 names most deserve attention]
```

---

## Notes

1. **Banks/insurers**: Metric #3 (interest coverage) does not apply; their business model is fundamentally spread-based
2. **REITs**: ROE can swing widely due to property revaluations; use "core operating-profit ROE" instead
3. **Insufficient data**: If a data point cannot be obtained, mark it "data insufficient" rather than defaulting to pass/fail
4. **Cyclical industries**: Use the average over a full cycle (covering at least one peak and one trough), not a single year
5. **Short listing history**: For companies listed less than 5 years, use all available data but flag "insufficient data window" in the results

## Statement of Limitations

This set of metrics can rule out companies that are "clearly bad," but passing the screen does not mean a company is "definitely good." Companies that pass still require further research:
- Is the business model sustainable
- Is management trustworthy
- Is the current valuation reasonable
- Is the competitive landscape deteriorating

Screening out the weak is the first step, not the last.
