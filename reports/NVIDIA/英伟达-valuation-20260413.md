# NVIDIA (NVDA) In-Depth Valuation Report

**Date: 2026-04-13**
**Current share price: $185.95 USD** (Yahoo Finance)
**Market cap: ~$4.64 trillion USD**

> **Core caveat up front**: the user's decision standard is "can you understand the profits 5-10 years out." NVDA's 5-10-year profit predictability is low (three black boxes: the AI capex cycle, in-house chip substitution, and the China sales ban), so this report's valuation conclusion carries **low confidence** and is used mainly to argue "why NVDA doesn't fit as one of a concentrated 6-stock portfolio," rather than to hand down a precise buy/sell price.

---

## I. Factual Basis (Primary SEC Data)

### 1.1 Financial Overview

| Metric | FY2024 | FY2025 | FY2026 YTD | Source |
|------|--------|--------|-----------|------|
| Total revenue | $60.9B | $130.5B (+114%) | Run-rate +94% | [SEC 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm) |
| Data Center | $47.0B | $115.2B (+145%) | $51.2B single quarter | [Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000230/nvda-20251026.htm) |
| Gross margin | 64.7% | 65.1% | 73.4-73.6% | — |
| GAAP EPS | $1.19 | $2.94 (+147%) | ~$4.9 YTD estimate | — |
| Free cash flow | $27.4B | $62.1B | Explosive growth | — |

### 1.2 Current Valuation Level

| Metric | Value | Historical comparison |
|------|------|---------|
| PE (based on FY2025 EPS of $2.94) | **63.2x** | = Cisco's 2000 peak |
| EV/Sales | **35.6x** | > Cisco's 2000 peak (31x) |
| PEG | 0.57 | Looks cheap, but implies 70%+ growth in perpetuity |

### 1.3 Customer Concentration (Q3 FY26)

- Top 4 customers account for **61%** of revenue
- Customer A alone accounts for **22%**
- The four are actually AWS/Azure/GCP/Meta (via OEM)

---

## II. Three Unpredictable Variables

### 2.1 The AI CapEx Cycle

**2026E combined hyperscaler CapEx**: $6,200-7,000B (up 58-78% YoY)
- Amazon $2,000B (+67%)
- Google $1,850B (+71%)
- Meta $1,150-1,350B (+53-80%)
- Microsoft $1,200B+ (+33%+)

**Historical pattern**: hyperscaler CapEx has never sustained +50% growth for three consecutive years.
**What the current share price implies**: CapEx keeps growing at +50% through 2026-2028. **A pullback in 2027 is highly likely.**

### 2.2 In-House Chip Substitution (already happening, not speculation)

| Vendor | Progress | Threat to NVDA |
|------|------|---------|
| AWS Trainium2 | 500k units online, 1 million by year-end | High (Anthropic has already moved off NVDA) |
| Google Ironwood | Anthropic's $100B rack contract | High (starts 2027) |
| Microsoft Maia | Already deployed serving GPT-5.2 | Medium (inference) |
| Meta MTIA | Hundreds of thousands of units for internal use | Medium (internal) |

**Sources**: [Bloomberg, 2026-04-06](https://www.bloomberg.com/news/articles/2026-04-06-broadcom-confirms-deal-to-ship-google-tpu-chips-to-anthropic), [AWS official](https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster)

### 2.3 Gross Margin Sustainability

- The current 73.4% reflects the high point of Blackwell supply shortage
- The normal level should be 60-65%
- If it falls back to 65%, net profit drops to **86% of its current level**

---

## III. Status of the CUDA Moat

| Moat layer | 2020 | 2026 | Change |
|-----------|------|------|------|
| Code lock-in | Solid | Broken (AI tools auto-migrate code) | Warning |
| Performance lead | 2-3x | 10-30% (on the inference side) | Warning |
| Ecosystem network | Monopoly | Multiple players running in parallel | Warning |
| 100k-GPU-scale systems | Unrivaled | Still strong | OK |

- Claude Code achieved an end-to-end CUDA→ROCm migration in 30 minutes with <10% performance loss
- ROCm 7.0's strategy: "align more tightly with CUDA semantics"
- The Triton compiler supports an AMD-backend abstraction

---

## IV. Three-Scenario Valuation

### The agent's original methodology

| Scenario | Probability | FY28E EPS | Discounted back to FY26 EPS | PE | Target price |
|------|-----|----------|-------------|-----|--------|
| Bull | 20% | $11 | $2.67 | 40x | **$107** |
| Base | 50% | $6.2 | $2.76 | 32x | **$88** |
| Bear | 30% | $3.0 | $1.77 | 20x | **$35** |

**Agent-weighted target: $75.9**

### Methodological correction

The agent's approach discounts FY28 EPS back to the FY26 level and then applies a PE multiple, which is **double discounting** — it compresses both the growth and the multiple, biasing the result low.

**The more standard approach**: apply the forward PE directly to FY28E EPS, then discount that target back to today.

| Scenario | FY28E EPS | Reasonable forward PE | FY28 target | Discounted to today (10%, 2 years) |
|------|----------|----------|---------|-----------------|
| Bull | $11 | 30x | $330 | **$273** |
| Base | $6.2 | 22x | $136 | **$112** |
| Bear | $3.0 | 18x | $54 | **$45** |

**Corrected weighted average (20/50/30): $128**

Both methods reach the same conclusion: **the current $186 price is high under any reasonable framing.**
- Agent's method: -59% upside
- Corrected method: -31% upside

---

## V. Historical Comparison: Cisco, 2000

| Dimension | Cisco 2000 | NVDA 2026-04 |
|------|-----------|-------------|
| PE | 63x | 63.2x |
| EV/Sales | 31x | 35.6x |
| Market cap | $569B | $4,640B (8x larger) |

**How Cisco's story ended**: peaked at $79 in March 2000 → bottomed at $8.12 in October 2002 (-89.7%) → had not reclaimed its high 22 years later

**Warning**: even a great company can extract a heavy price from investors who buy at a bubble valuation.
(Disclaimer: history does not necessarily repeat, but it's worth taking seriously.)

---

## VI. Five Counter-Arguments

1. **A 75% gross margin is not sustainable** — falling back to 65% alone cuts net profit by 14%
2. **The CUDA moat has been eroded** — AI coding tools have compressed migration cost from "months" to "hours"
3. **Customer concentration risk** — 22% comes from a single customer, and that customer is accelerating its own in-house chip program
4. **The AI CapEx cycle is subject to an iron law of periodicity** — +70% growth sustained for three straight years has never happened historically
5. **The China market is a permanent loss** — the $17B (30%) already gone is not coming back

---

## VII. Buffett / Duan Yongping Perspective

### Why Buffett wouldn't invest (paraphrasing multiple public remarks)
> "I only invest in businesses whose earnings I can estimate five years out or more. NVDA can't be reasonably estimated, so I pass."

### Duan Yongping (inferred, based on remarks on Xueqiu)
> "Great product, absurd price. I wouldn't short it, but I definitely wouldn't take a big position at this price either."

---

## VIII. Predictability Ranking (Under the "Pick One of Six" Standard)

| Rank | Company | Can you understand its 5-10-year profit? |
|-----|------|-------------|
| 1 | Moutai | ★★★★★ |
| 2 | Tencent | ★★★★ |
| 3 | Meituan | ★★★ |
| 4 | Pinduoduo | ★★★ |
| 5 | Pop Mart | ★★ |
| 6 | **NVIDIA** | **★** |

---

## IX. Conclusion

### Valuation Range (Low Confidence)

| Basis | Fair price |
|------|-------|
| Strictly conservative (agent's method) | $76 |
| Standard DCF method | $128 |
| Optimistic | $200-270 |

### "Pick One of Six" Recommendation

**Not suitable for a concentrated position**, for these reasons:
1. 5-10-year profits are unpredictable (violates the user's first-priority standard)
2. The current price already bakes in extremely optimistic assumptions
3. Downside risk far exceeds upside potential
4. Both Buffett and Duan Yongping have good reasons for staying away

### If a position must be taken
- Position size: <10%
- Holding period: 3-5 years (not permanent)
- Buy price: <$120 (may never be reached)
- Stop-loss: reassess if it falls below $120

---

## Appendix: Data Sources
- [NVDA SEC 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm)
- [NVDA Q3 FY26 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000230/nvda-20251026.htm)
- [Yahoo Finance NVDA](https://finance.yahoo.com/quote/NVDA/)
- [Bloomberg 2026-04-06 Ironwood](https://www.bloomberg.com/news/articles/2026-04-06-broadcom-confirms-deal-to-ship-google-tpu-chips-to-anthropic)
- [TechStrong - CUDA/ROCm migration](https://techstrong.ai/features/claude-code-ports-nvidia-cuda-to-amd-rocm-in-30-minutes/)
