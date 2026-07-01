---
name: financial-data
description: "AI Berkshire skill: Financial Data Retrieval and Cross-Validation Standard. Source: skills/financial-data.md."
---

## Codex adapter note

This skill is generated from `skills/financial-data.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Commands that reference `~/ai-berkshire/tools/...` assume the repo is checked out at `~/ai-berkshire`; if needed, prefer the current workspace path.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Financial Data Retrieval and Cross-Validation Standard

This standard applies to all research involving corporate financial data. **Every key data point must come from two independent sources; any discrepancy >1% must be flagged.**

---

## Data Source Priority

### US stocks (PDD, Tencent ADR, NetEase ADR, etc.)

| Priority | Source | URL | Access method |
|--------|------|-----|---------|
| 1 (primary) | **macrotrends** | macrotrends.net/stocks/charts/{ticker} | Direct access, no registration |
| 2 (secondary) | **stockanalysis** | stockanalysis.com/stocks/{ticker}/financials | Direct access, no registration |
| Original primary source | SEC EDGAR | sec.gov/cgi-bin/browse-edgar | 10-K / 10-Q original filings |

### HK stocks (Tencent 0700, NetEase 9999, Meituan 3690, etc.)

| Priority | Source | URL | Access method |
|--------|------|-----|---------|
| 1 (primary) | **aastocks** | aastocks.com/tc/stocks/analysis/company-fundamental | Direct access |
| 2 (secondary) | **macrotrends** (ADR ticker) | Tencent uses TCEHY, NetEase uses NTES | Direct access |
| Original primary source | HKEX (HKEXnews) | hkexnews.hk | Annual report PDF |

### A-shares (37 Interactive Entertainment, G-bits, etc.)

| Priority | Source | URL | Access method |
|--------|------|-----|---------|
| 1 (primary) | **East Money** | eastmoney.com → search stock code → financial statements | Direct access |
| 2 (secondary) | **CNINFO** | cninfo.com.cn | Original annual/quarterly report PDF |

---

## Execution Standard

### Step 1: Retrieve data

For each financial metric (revenue, net profit, gross margin, operating cash flow, debt-to-asset ratio, etc.), pull figures separately from **Source 1** and **Source 2**.

### Step 2: Discrepancy calculation and flagging

```
discrepancy rate = |Source 1 value - Source 2 value| / Source 1 value × 100%
```

| Discrepancy | Handling |
|------|---------|
| ≤ 1% | ✅ Consistent; use Source 1 value, cite both sources |
| 1% ~ 5% | ⚠️ Flag as "data discrepancy exists"; note both values and explain the likely cause (exchange rate / accounting basis) |
| > 5% | ❌ Flag as "material data discrepancy exists"; must verify against the original filing and must not be used directly |

### Step 3: Data presentation format

Every key data point must be annotated in the following format:

```
Revenue: RMB 123.9 billion ✅
  - macrotrends: RMB 124.1 billion
  - stockanalysis: RMB 123.7 billion
  - discrepancy: 0.3%
```

Discrepancy example:
```
Net profit: RMB 24.5 billion ⚠️ data discrepancy exists
  - macrotrends: RMB 24.5 billion (GAAP)
  - stockanalysis: RMB 27.8 billion (Non-GAAP)
  - discrepancy: 13.5% — cause: different accounting basis (GAAP vs Non-GAAP)
```

---

## Common Causes of Discrepancies (not necessarily data errors)

| Cause | Explanation |
|------|------|
| GAAP vs Non-GAAP | Most common, especially for profit-related figures |
| Exchange-rate conversion | Different conversion timing for HKD / RMB / USD |
| Fiscal-year definition | Calendar year vs fiscal year (e.g. Apple's fiscal year ends in October) |
| Consolidation basis | Whether minority interests are included |
| Data update lag | A platform may not yet have updated the latest reporting period |

---

## Special Rules

1. **Private (unlisted) companies** (miHoYo, Lilith Games, etc.): when only a single primary source is available, mark the data with `[estimate]` and do not perform cross-validation
2. **Quarterly vs annual data**: prefer annual data for cross-validation; some sources may lag on quarterly data
3. **Original filings take precedence**: if both sources disagree with the original filing (10-K / annual report PDF), the original filing prevails and the source error is flagged

---

## Quick Index

| Scenario | Primary source | Backup source |
|------|---------|---------|
| PDD / Pinduoduo | macrotrends.net/stocks/charts/PDD | stockanalysis.com/stocks/pdd |
| Tencent | macrotrends.net/stocks/charts/TCEHY | aastocks (0700.HK) |
| NetEase | macrotrends.net/stocks/charts/NTES | aastocks (9999.HK) |
| 37 Interactive Entertainment | eastmoney.com (002555) | cninfo.com.cn |
| G-bits | eastmoney.com (603444) | cninfo.com.cn |
| Nintendo | macrotrends.net/stocks/charts/NTDOY | stockanalysis.com/stocks/ntdoy |
| Capcom | macrotrends (CCOEY) | stockanalysis (CCOEY) |
