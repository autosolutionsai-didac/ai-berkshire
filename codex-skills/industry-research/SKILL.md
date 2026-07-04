---
name: industry-research
description: "AI Berkshire skill: Industry Investment Research: Value-Chain Panorama + Four-Master Single-Stock Framework. Source: skills/industry-research.md."
---

## Codex adapter note

This skill is generated from `skills/industry-research.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Commands that reference `~/ai-berkshire/tools/...` assume the repo is checked out at `~/ai-berkshire`; if needed, prefer the current workspace path.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Industry Investment Research: Value-Chain Panorama + Four-Master Single-Stock Framework

Conduct systematic value-chain investment research on the $ARGUMENTS industry.

## Research Objectives

Starting from an investment theme / logic chain, complete the following:
1. Validate every link in the investment logic chain
2. Draw a complete value-chain panorama
3. Scan every listed company globally (A-shares / HK stocks / US stocks / international)
4. Apply the four-master framework to the leading companies in each sub-segment
5. Output an industry-level portfolio allocation recommendation

---

## Step 1: Building and Validating the Investment Logic Chain

### 1.1 Draw the logic chain
Use an arrow-linked chain to express the causal relationship from "underlying trend" to "beneficiary target," for example:
```
Underlying trend A
    → drives demand B
        → creates bottleneck / hard demand C
            → beneficiary value chain D
```

### 1.2 Validate link by link
For every arrow in the logic chain, raise a challenge and look for evidence:

| Link | Core assumption | Validation method | Data source |
|------|---------|---------|---------|
| A→B | | Search industry data / forecasts | |
| B→C | | Search supply-demand analysis | |
| C→D | | Search real cases / signed deals | |

### 1.3 Find "validation events that have already happened"
List the **already-signed / already-implemented real business events** (not forecasts) that support this logic chain — e.g., large companies' procurement agreements, policy documents, industry reports, etc.

---

## Step 2: Drawing the Value-Chain Panorama

### 2.1 Map the value-chain structure
Break the industry down into upstream → midstream → downstream → supporting links, for example:
```
Upstream: raw materials / resource extraction → material processing / purification
Midstream: core equipment manufacturing → system integration / engineering construction → new-technology R&D
Downstream: operations / services → end customers
Supporting: testing / certification → maintenance services → financial instruments (ETFs / trusts)
```

### 2.2 Identify each link's "business characteristics"
For each link, annotate:

| Link | Business model | Gross-margin range | Competitive landscape | Barrier type | Cyclicality |
|------|---------|-----------|---------|---------|--------|
| | Sell resources / sell equipment / sell services / collect rent | | Monopoly / oligopoly / full competition | Resource / license / technology / scale | Strong / medium / weak |

### 2.3 Flag the "chokepoint links"
Identify the links in the value chain where supply is tightest, substitution is hardest, and margins are highest — these are often where the best investment targets sit.

---

## AI Research Bias Awareness: Special Traps in Industry Research

In industry research, AI data bias is amplified in unique ways:

**Industry-level biases**:
| Bias type | Manifestation | Countermeasure |
|---------|------|------|
| Mature-industry preference | Traditional industries (banking / energy / consumer) have abundant material, so AI analysis looks "more certain" | Certainty comes from the business model, not from the number of research reports |
| New-industry underestimation | New industries (AI applications / synthetic biology, etc.) have little material, so AI analysis skews conservative | Judge industry value with "endgame thinking," not "current data" |
| Leader preference | Large companies have far more material than small ones, so AI naturally tends to recommend leaders | Small companies may have a better risk-reward ratio — don't ignore one just because the AI analysis is short |
| Listed-company preference | Scanning only listed companies misses the key unlisted players in the value chain | You must search for unlisted companies and flag "future IPO candidates" |
| English-language preference | AI handles English-language material more strongly and may underestimate Chinese / Asian market players | You must search both Chinese- and English-language sources |

**Anti-bias measures during value-chain scanning**:
1. For each link, don't only list "companies the AI can easily find" — also proactively search for "obscure but potentially high-quality targets"
2. For small-cap companies with scarce information, don't lower the recommendation just because the analysis is short — judge by the core questions (business essence, moat, management), not by report length
3. In the final report, tag each company's "information sufficiency" (Grade A/B/C) so the reader knows how reliable the AI analysis is

## Step 3: Global Listed-Company Scan

Use the Task tool to launch background Agents and comprehensively search all listed companies in the industry.

### Search checklist
- US-stock (NYSE / NASDAQ / NYSE American) companies
- A-share (Shanghai / Shenzhen) companies
- HK-stock companies
- Other international markets (Japan / Korea / Europe / Australia, etc.)
- Industry ETFs
- Key unlisted companies (possible future IPOs)

### For each company, collect
- Company name (Chinese and English)
- Ticker and exchange
- Market cap (approximate)
- One-line description (its position and role in the value chain)
- Whether it is a pure-play target (pure nuclear power vs. diversified with a nuclear-power business)
- Which value-chain link it belongs to

### Output format
Classify by value-chain link, one table per link, containing all scanned companies.
Then stratify by investment certainty:
- **Tier 1**: large-cap, pure-play, industry leader
- **Tier 2**: mid-cap, pure-play or high-share, segment leader
- **Tier 3**: small-cap, development-stage, high-risk high-beta
- **Tier 4**: large diversified companies with a relevant business line

---

## Step 4: Four-Master Analysis of the Leading Companies in Each Link

For the **Tier 1 and Tier 2 companies** in each value-chain link, perform the following analysis (a brief note suffices for Tier 3/4 companies):

### 4.1 Business essence (Duan Yongping)
- Define in one sentence what this company does in the value chain
- Revenue structure and growth rate
- Gross-margin / net-margin levels and trends
- Cash-flow characteristics
- **Follow-up**: Is this a good business? Why?

### 4.2 Moat (Buffett)
Score using the five moat types (★1-5):

| Moat | Strength | Evidence |
|--------|------|------|
| Brand / pricing power | | |
| Switching cost | | |
| Network effect | | |
| Economies of scale | | |
| Technology / license barrier | | |

**Follow-up**: Will the moat still be there in 10 years?

### 4.3 Risk (Munger)
- How is this company most likely to fail?
- What is it worth in the worst-case scenario?
- Why do smart people not buy it?

### 4.4 Management (Duan Yongping + Buffett)
- Who is the CEO / founder? Record of key decisions
- Ownership stake and interest alignment
- Brief assessment (Grade A/B/C)

### 4.5 Valuation snapshot
- Current PE / PS / EV/EBITDA
- Comparison with competitors in the same link
- Brief assessment: expensive / fair / cheap

### 4.6 Recommendation rating
Mark with ★1-5:
- ★★★★★ = core-position candidate
- ★★★★☆ = satellite-position candidate
- ★★★☆☆ = watchlist
- ★★☆☆☆ = high-risk option
- ★☆☆☆☆ = not recommended

---

## Step 5: Industry-Level Risk Assessment (Munger's "Checklist")

### 5.1 Systemic-risk checklist

| Risk | Probability | Impact | Response strategy |
|------|------|------|---------|
| Some link in the investment logic chain is falsified | | | |
| A substitute technology emerges | | | |
| Policy / regulatory black swan | | | |
| Cyclical demand pullback | | | |
| Valuation bubble bursts | | | |

### 5.2 Historical analogy
Find a historically similar value-chain investment theme and analyze how it ultimately played out:
- What is the analogous industry?
- Who was the eventual winner? (Upstream / midstream / downstream?)
- Did most investors make money or lose money?
- What is the lesson for the current industry?

### 5.3 Bias self-check
- Narrative bias: Is the story too perfect?
- Anchoring effect: Are you anchored to the recent rally?
- Herd effect: Is it because "everyone is buying"?

---

## Step 6: Civilizational-Trend Judgment (Li Lu framework)

- Is the underlying trend this industry rests on a "civilizational-level paradigm shift" or a "temporary craze"?
- What is the closest historical technological-revolution analogy?
- In 10-20 years, what is the endgame for this industry?
- In the value chain, which link is most likely to see "winner-take-all"?
- Which link is most likely to be disrupted?

---

## Step 7: Portfolio Allocation Recommendation

### 7.1 Recommended portfolio
Output in the following structure:

| Tier | Position weight | Target | Value-chain link | Core rationale |
|------|---------|------|---------|---------|
| **Core position** | 50-60% of the theme position | | | Most certain, widest moat |
| **Satellite position** | 25-35% of the theme position | | | Higher beta, slightly lower certainty |
| **Option position** | 5-15% of the theme position | | | High risk, high reward, can go to zero |
| **ETF alternative** | Can replace all of the above | | | The "lazy solution" for those who don't want to pick stocks |

### 7.2 Buy / sell signals

| Signal type | Specific condition |
|---------|---------|
| Add-to-position signal | |
| Trim signal | |
| Exit signal | |

### 7.3 Theme position-cap recommendation
Based on the certainty and risk level of the investment logic chain, recommend a maximum percentage of the total portfolio that this theme should occupy.

---

## Step 8: Comprehensive Decision Memo

### Industry summary table

| Dimension | Conclusion | Confidence |
|------|------|--------|
| Investment logic chain (degree of validation) | | |
| Best link (Duan Yongping's "right business") | | |
| Widest moat (Buffett) | | |
| Biggest risk (Munger) | | |
| Civilizational-trend positioning (Li Lu) | | |
| Overall valuation level | | |

### Simulated commentary from the four masters
Using blockquote format, simulate the four masters' commentary on this industry's investment opportunity.

---

## Output Requirements

1. Every analysis must be backed by data, with data sources attached
2. Present key data in Markdown tables
3. Represent the value-chain panorama with a text diagram in a code block
4. Analyze at least 2-3 leading companies per link
5. Make the global company scan as complete as possible (A-shares / HK stocks / US stocks / international)
6. Finally, write the complete report to `reports/{industry}-industry-{YYYYMMDD}.md` (industry reports go in the reports/ root, date format YYYYMMDD)
7. Conclusions must be clear, giving specific targets, position sizes, and price-range recommendations
8. End each analysis module with the corresponding master's "follow-up"

## Data Spot-Check (Release Audit)

After the report is written, run a data spot-check; it may be published only once it passes:

```bash
# Step 1 — Extract the spot-check list (15% random sample)
python3 ~/ai-berkshire/tools/report_audit.py extract \
  --report <report file path>

# Step 2 — For each item on the list, pull figures from reliable sources (see skills/financial-data.md)

# Step 3 — Output the release / reject verdict
python3 ~/ai-berkshire/tools/report_audit.py verdict \
  --results '<filled-in JSON>' \
  --report <report file name>
```

**[Release]** all pass → the report may be published; **[Reject]** any fail → fix and re-review.
