---
name: etf-review
description: Fund and ETF evaluation. Audits a fund's cost stack, tracking quality, index methodology, legal wrapper, domicile and tax treatment, and its holdings overlap with what you already own. Use for any ETF, index fund or tracker -- the four-master company framework (moat, management, circle of competence) does not apply to a fund and must not be run on one.
---

## Codex adapter note

This skill is generated from `skills/etf-review.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Prefer running commands from the repository root with paths like `python3 tools/financial_rigor.py ...`; if the current thread starts outside the repo, locate the actual checkout path first instead of assuming a fixed home-directory path.
- Before starting research, run the `date` command to confirm today's date; treat it as the baseline for "latest" data and state the data cutoff date in the report header. Never assume the current date from training data.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Fund and ETF Review: What the factsheet does not tell you

Evaluate the fund or ETF named in $ARGUMENTS against its cost stack, tracking quality, legal wrapper, tax treatment and overlap with existing holdings.

**Supported input formats**:

| Input | Behavior |
|------|------|
| `/etf-review VWRP` | Single fund, full review |
| `/etf-review VWRP, VHVG, SWDA` | Comparison mode across several funds |
| `/etf-review VUAG vs CSP1` | Head-to-head on the same underlying index |
| `/etf-review VWRP + profile` | Pull wrapper, residence, base currency and existing holdings from `reports/investor-profile.md` |

> "In investing, you get what you don't pay for." -- John Bogle
>
> "Put 10% of the cash in short-term government bonds and 90% in a very low-cost S&P 500 index fund." -- Warren Buffett, 2013 shareholder letter

## Design concept

A fund has no ROE, no free cash flow, no management to interrogate and no moat. `/quality-screen`, `/investment-checklist` and `/berkshire-skill` do not apply to it and **must not be run on one** -- doing so produces confident nonsense, because all seven quality-screen metrics are company accounting ratios.

What a fund has instead is a **rulebook, a cost stack, a legal wrapper and a tax treatment**. That is what this skill audits.

If you want to interrogate what is *inside* the fund, run `/quality-screen` on its top-10 holdings. That is the correct reuse.

## Execution process

### Step 1: Eligibility gates

Run these first. A fund can be excellent and still be unbuyable or untaxable for a given holder, and there is no point scoring something that fails here. Mark each `[PASS]`, `[FAIL]` or `[CHECK]`.

| # | Gate | Fails when |
|---|------|------|
| **G1** | **Domicile and retail eligibility** | US-domiciled fund with a UK or EU retail investor -- no PRIIPs KID, so brokers block it. UCITS fund with a US taxable investor -- PFIC treatment. A non-eligible fund inside a PEA. **A G1 failure is terminal regardless of quality** |
| **G2** | **Withholding and estate-tax drag** | Quantify in basis points rather than pass/fail. Irish domicile takes 15% US-dividend withholding at fund level under treaty; some domiciles take 30%. A UK SIPP holding US-domiciled assets can reach 0% under treaty. Include the **US estate-tax threshold for non-US persons holding US-domiciled assets** -- the most commonly missed item in this rubric |
| **G3** | **Size and age floor** | AUM below roughly 100m, or under 3 years live -- closure risk, which forces a sale at the issuer's timing and can crystallise a taxable event. Below roughly 50m is a fail unless the issuer has stated a commitment |
| **G4** | **Tradability** | Typical bid-ask spread large relative to the TER; thin on-exchange volume; and check **which listing line** -- the same fund on the LSE in GBP, GBX and USD are different lines, and buying the wrong one adds an FX conversion |

### Step 2: Scorecard

Rate each dimension 1-5 using the star glyph, no half stars. Composite is the weighted sum to one decimal.

| # | Dimension | Weight | ★5 | ★1 |
|---|------|:----:|------|------|
| 1 | **Total cost of ownership** -- TER/OCF plus transaction costs, spread, FX conversion and platform fee | 20% | All-in under 0.15%/yr | Headline TER hides roughly double the all-in cost |
| 2 | **Tracking quality** -- *tracking difference* (the annualised return gap: what it actually costs you) and *tracking error* (its standard deviation: consistency) | 20% | TD at or better than TER, TE under 0.10% | TD twice the TER, or unstable |
| 3 | **Index methodology** -- what is actually measured; provider independence; inclusion rules; rebalance cadence and reconstitution drag | 15% | Independent, transparent, broad, low turnover | A bespoke back-tested index built to sell the product |
| 4 | **Concentration and holdings** -- top-10 weight, effective number of holdings, single-name cap, sector and country skew | 15% | Genuinely diversified | A "global" fund that is 70% one country and 25% seven names |
| 5 | **Structure fit to wrapper** -- accumulating vs distributing matched to objective and account; UK reporting-fund status; PEA eligibility | 10% | The right share class exists for this wrapper | A non-reporting fund in a UK taxable account, where gains are taxed as income |
| 6 | **Replication and counterparty** -- full physical, sampled, or synthetic; collateral quality; number of swap counterparties | 10% | Full physical, or a swap structure with a named advantage | Single counterparty, opaque collateral |
| 7 | **Currency** -- fund base vs listing vs your base vs the currency of underlying revenues; cost of a hedged class | 5% | Right class available; hedging decision matches horizon | Paying to hedge global equity over a 20-year horizon |
| 8 | **Securities lending** -- whether it lends, % of book on loan, revenue split to fund vs manager, collateral level | 5% | No lending, or 100% of revenue to the fund, over-collateralised | Split undisclosed |

Two subtleties that are easy to get wrong:

- **Do not blanket-penalise synthetic replication.** A swap-based S&P 500 UCITS can legitimately capture 0% US dividend withholding and outscore a physical peer for a European holder. Score the structure's fitness **for this holder**, not the label.
- **Compute tracking difference yourself** -- fund NAV total return minus index total return, using `python3 tools/financial_rigor.py calc`. Never quote the issuer's own figure without a second source.

### Step 3: Overlap with existing holdings

This is the one thing no factsheet gives you, and the reason `/investor-onboarding` calls this skill instead of pointing at a comparison website. Not scored -- overlap is a property of the holder, not of the fund.

| Output | Method |
|------|------|
| **Name-level overlap** | Sum of min(weight in A, weight in B) across common holdings, per pair. Compute with `financial_rigor.py calc` |
| **Look-through single-name exposure** | If the user holds this fund *and* a name directly, what is the true combined weight of that name? This is the number that changes decisions |
| **Sector and country look-through** | Combined weights against the geography mix in the allocation frame |

Flag as `Low <30%` / `Moderate 30-60%` / `High 60-80%` / `Duplicative >80%`.

### Step 4: Verdict

| Verdict | Condition | Maps to |
|------|------|------|
| **Core** | All gates pass, composite ★4.0 or better, overlap Low | Buy |
| **Satellite** | Gates pass, composite ★3.0-3.9, or suitable only for a specific role or wrapper | Hold |
| **Redundant** | Good fund, but overlap is High or above with something already held. **Not a quality judgement** | Avoid for now |
| **Ineligible** | G1 failure. The fund may be excellent -- you simply cannot buy it or should not hold it | Avoid |
| **Avoid** | Any other gate failure, or composite below ★3.0 | Avoid |

`Redundant` and `Ineligible` carry genuinely different information from `Avoid` and must not be collapsed into it. Telling a UK investor that VOO is "bad" is false; telling them it is *ineligible* is true and actionable, because the answer is to buy the UCITS equivalent instead.

### Step 5: Audit

Follow the standard release audit used across the toolkit:

```bash
python3 tools/report_audit.py extract --report <report file path>
# verify each sampled figure against a primary source
python3 tools/report_audit.py verdict --results '<filled JSON>' --report <report file name>
```

## Data sources

| Priority | Source | Authoritative for |
|:----:|------|------|
| 1 | Issuer factsheet, KID/KIID, and **annual report** | TER, domicile, replication, share classes, index name. The annual report is the only reliable source for realised tracking difference and the securities-lending revenue split |
| 2 | justETF (UK/EU), etf.com or ETFdb (US) | Cross-check TER, AUM, listings, accumulating vs distributing, replication |
| 3 | Morningstar | Independent tracking difference, holdings overlap, flows |
| Index truth | Index provider factsheet (MSCI, FTSE Russell, S&P DJI, Solactive) | Methodology, rebalance cadence, index total return for the TD computation |
| Wrapper and tax | HMRC reporting-fund list, issuer tax pages, PEA eligibility lists | Reporting status, eligibility |

**Tolerance bands for fund figures.** The general standard in `skills/financial-data.md` (1% pass, 1-5% warn, over 5% fail) is built for large numbers and misfires badly here: a TER of 0.07% against 0.12% is a 71% relative discrepancy but a 5 basis point absolute one. For expense ratios, tracking difference and yields, compare in **basis points absolute**: 2bp or less passes, 2-10bp warns, over 10bp fails and you go to the KID.

## Output format

Write to `reports/{Fund or comparison name}-etf-{YYYYMMDD}.md` in the root of `reports/` -- funds do not accumulate the multi-artifact folder that companies do, and reviews are usually comparative.

```markdown
# {Fund} Review

**Date** | **Verdict** | **Composite** | **Information richness A/B/C**

## Verdict up front
One paragraph. What it is, whether you can hold it, and what it costs you.

## 1. Eligibility gates
| Gate | Result | Detail |

## 2. Scorecard
| Dimension | Weight | Rating | Evidence |
| **Composite** | | ★N.N | |

## 3. Overlap with your holdings
| Measure | Value | Flag |

## 4. Cost in context
What the all-in cost compounds to over the stated horizon, in percentage terms.

## 5. What would change this verdict
## 6. Sources and audit result
```

---

## Notes

- **A fund is not a company.** No moat, no management, no circle of competence. If you catch yourself scoring one of those, you are running the wrong skill.
- **The gates come first** -- there is no point producing a beautiful scorecard for something the holder legally cannot buy.
- **Ineligible is not the same as bad.** The most common real-world case is a US-domiciled fund and a UK or EU investor, where the correct answer is the UCITS equivalent, not avoidance.
- **Cost compounds and is the only input you control.** Everything else in this rubric is a forecast; the TER is a fact.
- **Overlap is holder-relative** -- it is deliberately excluded from the composite, because the same fund is Core for one person and Redundant for another.
- **Tax rules rot faster than equity research.** State the mechanic, look up the rate at run time, and never hardcode a rate as fact.
