# DapuStor Microelectronics (301666.SZ) Investment Research Report

**Date**: June 23, 2026
**Ticker**: 301666.SZ (ChiNext)
**Current share price**: RMB 705.00 (June 23 close, -7.66%)
**Market cap**: approximately RMB 307.4 billion
**Total shares outstanding**: 436 million shares (only 27 million shares, 6.2%, in free float)

---

## Information Availability Rating: Grade C (Scarce Information)

DapuStor listed on April 16, 2026, only 68 days ago. It is the first unprofitable company to list on ChiNext, and prior to listing there was only a prospectus and a handful of media reports. Although the listing has generated significant market buzz, in-depth brokerage coverage remains scarce, and the company's financial history spans only 4 years (2022-2025), all of them loss-making.

**AI Research Limitations Disclosure**:
- Only one full quarter of profitability data exists (Q1 2026); the sustainability of profitability is entirely unverified
- Data on customer order amounts mostly comes from unofficial channels such as Eastmoney's self-media platform, and confidence in it is low
- Data on the actual revenue contribution of the self-developed controller chip is extremely scarce — the prospectus shows that 2024 revenue from the self-developed PCIe 5.0 controller was only RMB 258,300
- Free float is only 6.2%, so the share price does not reflect a genuine supply-demand equilibrium

**Bias self-check**:
- [x] The "AI storage domestic substitution" narrative is extremely strong and prone to inducing an illusion of certainty
- [x] The current RMB 307.4 billion market cap vs. the RMB 6.8 billion Series E valuation 17 months ago — a 45x inflation that demands extreme caution
- [x] Assigning a 200+x PE after just one profitable quarter suggests the market may be trading a "dream" rather than "reality"
- [x] Grade-C information scarcity means my analysis relies heavily on estimation and third-party reporting

---

## Step One: Core Data Overview

### Financial metrics

| Metric | 2022 | 2023 | 2024 | 2025 | Q1 2026 |
|------|--------|--------|--------|--------|--------|
| Revenue (RMB million) | 557 | 519 | 962 | 2,289 | **1,310** |
| Revenue growth | — | -6.8% | +85% | +138% | **+341%** |
| Net profit attributable to parent (RMB million) | -534 | -617 | -191 | -481 | **+370** |
| Gross margin | — | — | 27% (est.) | Very low (Q4 only 3.5%) | **37.6%** |
| Order backlog | — | — | — | — | **RMB 4.7 billion** |

*Cumulative losses from 2022-2025 totaled RMB 1.823 billion. Q1 2026 was the company's first profitable quarter in its history.*

### Valuation metrics (tool-verified)

| Metric | Value | Note |
|------|------|------|
| Market cap | RMB 307.4 billion | ✅ Verified |
| PB | **383x** | ✅ Net assets of only ~RMB 800 million |
| PE (Q1 single-quarter EPS of RMB 0.85) | **829x** | ✅ Single quarter — cannot simply be annualized |
| PE (annualized Q1 profit of ~RMB 1.48 billion) | **~208x** | Assumes the Q1 profit level is sustained for the full year |
| PS (2025 revenue of RMB 2.289 billion) | **~134x** | — |
| PS (annualized Q1 revenue of ~RMB 5.2 billion) | **~59x** | — |
| Dividend yield | 0% | Never paid a dividend |

### Ownership structure

| Shareholder | Economic interest | Voting rights |
|------|---------|--------|
| Yang Yafei (Founder) | 16.71% | **66.74%** (10:1 special voting rights) |
| Shenzhen Guozhong (Shi Anping) | 10.43% | — |
| Zeyi Capital (Chi Ke) | 6.43% | — |
| Nanjing Qilin (Nanjing state-owned capital) | 5.18% | — |
| Public float | ~6.2% | Very low |

### Key data cross-validation log

| Item verified | Result | Source |
|--------|------|------|
| Market cap check (RMB 705 × 436 million shares) | ✅ RMB 307.4 billion, 0.01% deviation | Tool-verified |
| 2025 revenue | ✅ RMB 2.289 billion, consistent across three sources | Annual report, Jiemian News, TMTPost |
| Q1 2026 net profit | ✅ RMB 370 million, consistent across three sources | Quarterly report, Sohu, Jiemian News |
| PB | ✅ 383x | Tool-verified |

---

## Step Two: Business Nature Analysis — Duan Yongping's "The Right Business"

### One-sentence definition

**DapuStor is, at its core, a storage-chip company that "fills the gap in domestic enterprise-grade SSDs with the ingenuity of Chinese engineers." What it does is act as the "data mover" of the AI era — efficiently shuttling data between a server's memory and flash storage.**

### Business model

```
Self-developed SSD controller chip (DP600/DP800)
         +
Self-developed firmware algorithms (AI error correction / wear leveling / data protection)
         +
Externally sourced NAND Flash (Kioxia / YMTC, etc.)
         ↓
    Complete enterprise-grade SSD products
         ↓
  Data center customers (ByteDance / Tencent / Alibaba / Google / Nvidia)
```

**Core characteristics**:

1. **Full-stack self-development, but NAND is sourced externally**: the self-developed controller and firmware are the soul of the product, but 80%+ of costs come from externally purchased NAND Flash. This means gross margin is highly dependent on the NAND price cycle
2. **B2B, large-customer model**: customers are internet/cloud giants — orders are large, but negotiation cycles are long and customer concentration is high (the top 5 customers account for 53-78% of revenue)
3. **High technical barriers but low market share**: 6.4% domestic market share (No. 1 among domestic makers), but 90%+ of the global market is monopolized by Samsung/Micron/Western Digital/Kioxia

### Gross margin volatility — this business's biggest "hidden ailment"

| Period | Gross margin | Reason |
|------|------|------|
| 2024 | ~27% | NAND prices normal |
| Q4 2025 | **3.5%** | Rising NAND prices squeezed profit |
| Q1 2026 | **37.6%** | NAND price declines + product-mix optimization |

**Gross margin swung by more than 34 percentage points within a single year.** This reflects a core fact: DapuStor's profit is not determined by itself — NAND prices are controlled by upstream giants such as Samsung, SK Hynix, and Micron. When NAND prices rise, DapuStor is barely profitable; when NAND prices fall, profit surges.

### The real value of "full-stack self-development"

This is the market's core thesis on DapuStor, but it warrants careful scrutiny:

- ✅ The self-developed DP600/DP800 controller chips — a genuine technical barrier
- ✅ Self-developed firmware algorithms (AI error correction, etc.) — strong software know-how
- ⚠️ **But in 2024, revenue from PCIe 5.0 products carrying the self-developed controller was only RMB 258,300** — the overwhelming majority of revenue still came from products using externally sourced Marvell controllers
- ⚠️ Mass production of the self-developed controller is still at an early stage; commercial validation of "full-stack self-development" remains insufficient

> **Duan Yongping-style question**: What's good about this business?
>
> **The strength lies in high technical barriers plus rigid domestic-substitution demand.** Enterprise-grade SSD controller chips are "hardcore technology" — no more than 10 companies worldwide can build them, and no more than 3-5 in China. Domestic-substitution policy plus data-security drivers give DapuStor an almost guaranteed market space. But the "weakness" of this business is: (1) 80% of costs are held hostage by NAND suppliers, so margins depend on factors outside its control; (2) customer concentration is extremely high, and order swings from a single major customer can cause large fluctuations in quarterly revenue; (3) the global market is still monopolized by Samsung/Micron/Kioxia, and the actual pace of domestic substitution is far slower than the narrative suggests.

---

## Step Three: Moat Assessment — Buffett's "Economic Moat"

| Moat type | Strength | Assessment |
|-----------|------|------|
| **Brand / pricing power** | ★☆☆☆☆ | Almost nonexistent. Enterprise SSD procurement is driven by technical specifications and price, so brand premium is minimal |
| **Switching costs** | ★★★☆☆ | Moderate. Enterprise SSDs require deep integration with customer systems (firmware customization, compatibility testing), and switching suppliers requires 6-12 months of validation. But this switching cost is not as high as that of ERP systems or databases |
| **Network effects** | ★☆☆☆☆ | Nonexistent |
| **Economies of scale** | ★★☆☆☆ | Limited. The larger the NAND purchase volume, the stronger the bargaining power, but DapuStor's procurement scale is far smaller than Samsung's or Micron's |
| **Technical barriers** | ★★★★☆ | **This is the only genuine moat.** Designing enterprise SSD controller chips has an extremely high barrier to entry (hundreds of person-years of engineering effort), with no more than 10 players worldwide. DapuStor's full-stack self-development capability (controller + firmware + module) is nearly unmatched domestically. But technical barriers narrow over time |

### The nature of the moat

DapuStor's moat is not insurmountable — it is a **"first-mover dividend."** It is one of the earliest domestic companies to pursue full-stack self-development for enterprise SSDs, and it has built a first-mover advantage with customers such as Google and ByteDance. But this advantage is a **time lag** rather than a **structural barrier** — competitors such as Deyi Microelectronics and Yingren Technology are catching up.

> **Buffett-style question**: Will this moat still be there in 10 years?
>
> **Uncertain.** Two scenarios: (1) if DapuStor keeps iterating (PCIe 6.0 → 7.0) and maintains a 1-2 generation technology lead, the moat can be sustained; (2) if Samsung/Micron squeeze it with price cuts, or domestic competitors catch up, the moat could narrow. The key variable is whether DapuStor can keep securing sufficient R&D investment — which in turn depends on whether it can stay profitable through NAND price-cycle swings.

---

## Step Four: Inversion and Risk Checklist — Munger's "Invert, Always Invert"

### Failure-path checklist

| Failure path | Probability | Impact | Description |
|----------|------|------|------|
| **Valuation collapse** | **Very high** | **Very high** | RMB 307.4 billion market cap vs. a Series E valuation of RMB 6.8 billion (17 months ago) — a 45x inflation. With only 6.2% of shares in free float, once the lock-up expiry and selling wave arrives (2027), the share price could plunge 60-80% |
| **NAND price increases squeeze profit** | **High** | **High** | The mere 3.5% gross margin in Q4 2025 was a direct result of rising NAND prices. NAND accounts for 80%+ of costs, so price increases eat directly into profit |
| **Self-developed controller commercialization falls short** | **Medium-high** | **High** | 2024 revenue from the self-developed PCIe 5.0 controller was only RMB 258,300. If customers do not validate the self-developed controller's performance, "full-stack self-development" becomes just a concept |
| **Lock-up expiry and selling wave** | **Very high certainty** | **High** | Employee share allotments unlock in 2027 (cost basis RMB 46, paper gains of 15x+), and Series E investors have paper gains of 45x+. Share sales are only a matter of time |
| **Customer concentration risk** | **Medium** | **High** | The top 5 customers account for 53-78% of revenue; any one of them shifting orders elsewhere would cause a major shock |
| **Samsung/Micron price-cut competition** | **Medium** | **High** | Samsung/Micron can dump product at extremely low cost through vertical integration (in-house NAND + self-developed controllers) |
| **US sanctions** | **Medium-low** | **High** | Enterprise SSD controllers have not yet been explicitly listed, but uncertainty exists given the US-China decoupling trend |
| **Technology roadmap shifts** | **Low** | **High** | New standards such as PCIe 6.0/CXL could reshape the competitive landscape |

### Historical analogies

**Negative analogy: Cisco in 2000**
- Similarities: an infrastructure-equipment maker riding a new technology wave (internet ≈ AI), an extremely high valuation (Cisco's PE was 200x), and a market that believed the "new paradigm" justified the high valuation
- Outcome: Cisco fell 80%+ after the dot-com bubble burst. Even though its business was real (routers/switches genuinely are internet infrastructure), the stock took 20 years to recover
- Lesson: **A good business + a good product ≠ a good investment. Price determines returns.**

**Negative analogy: Allwinner Technology in 2015 (A-share chip-stock speculation)**
- Similarities: a small-cap chip stock, an extremely small free float, narrative-driven (domestic substitution), a short-term price surge
- Outcome: fell 70%+ from its peak
- Lesson: an extremely small free float plus narrative-driven speculation is the classic recipe for a bubble

> **Munger-style question**: Where am I most likely to be wrong?
>
> The most likely mistake is being blinded by the "AI storage domestic substitution" narrative and overlooking the absurdity of the valuation. DapuStor may indeed be a technologically excellent company — but a share price of RMB 705 means paying, at 383x PB and 208x forward PE, for a company that has only just turned profitable for one quarter and whose gross margin can fall to 3.5% when NAND prices swing. The reason a smart investor wouldn't buy is simple: **17 months ago the Series E valuation was RMB 6.8 billion; now it's RMB 307.4 billion — do you really believe the company's intrinsic value grew 45x in 17 months?**

---

## Step Five: Management Assessment — Duan Yongping's "The Right People"

### Founder Yang Yafei

Born in 1979, holds a PhD in Electrical Engineering from the University of Rhode Island. From 2000 to 2016 he worked at Qualcomm as a Senior Staff Engineer (16 years), specializing in SoC/storage controllers. In 2016 he resigned and returned to China to found DapuStor, aiming to break the dominance of international giants in enterprise-grade SSDs.

**Core team**: CTO Li Weijun (a researcher at the Institute of Semiconductors, Chinese Academy of Sciences), and Deputy General Manager Huang Yunxin (a former core member of Samsung's storage division). Core members come from Qualcomm, Marvell, Huawei, Samsung, and Micron.

### Assessment of key decisions

| Year | Decision | Rating |
|------|------|------|
| **2016** | Left a secure position at Qualcomm to return to China and start a business | ★★★★★ |
| **2018-20** | Committed to the self-developed controller route (rather than sourcing externally) | ★★★★★ |
| **2023** | Among the first in the world to mass-produce PCIe 5.0 QLC SSDs | ★★★★★ |
| **2024** | Broke into the Google/Nvidia supply chain | ★★★★☆ (scale still to be validated) |
| **2025** | Chose to list on ChiNext (the first unprofitable company to do so) | ★★★★☆ |

### Alignment of interests

- Yang Yafei holds a 16.71% economic interest plus 66.74% of voting rights — absolute control, with his interests deeply aligned with the company's
- Compensation of RMB 1.0892 million per year — extremely modest for the founder of a company with a market cap of around RMB 300 billion
- A three-year post-listing lock-up — no ability to cash out in the short term

> **Duan Yongping-style question**: If the CEO retired, could the company remain competitive?
>
> **In the short term, yes; in the long term, it's uncertain.** DapuStor's technical team has sufficient depth (293 R&D staff, 68.78% of headcount), so product development would not stall even if Yang Yafei stepped away. But Yang's Qualcomm and chip-design background serves as the company's technical anchor in controller chips — losing him could affect technology-direction judgment and key customer relationships.

---

## Step Six: Industry and Civilizational Trends — Li Lu's "Civilizational Evolution Framework"

### AI storage: genuinely at a civilizational-scale paradigm shift

Training and inference for large AI models require massive amounts of high-speed storage:
- Training: terabyte-scale datasets require high-bandwidth SSDs to move data
- Inference: KV cache and model-weight loading require low-latency SSDs
- In 2025, the global enterprise SSD market exceeded $35 billion (+82%), with AI as the core driver

### TAM analysis

| Market | Size | Growth rate |
|------|------|------|
| Global enterprise SSD | Over $35 billion (2025) | +82% |
| China enterprise SSD | Over RMB 42 billion (2025) | +78% |
| AI server PCIe 5.0 SSD | — | +150%+ |

DapuStor's 2025 revenue of RMB 2.289 billion accounts for only about 5% of the Chinese market and less than 1% of the global market. The theoretical ceiling is far from being reached.

### The real pace of domestic substitution

"Domestic substitution" is a genuine policy-driven force, but its pace warrants careful assessment:
- Samsung/Micron/Kioxia still hold 90%+ of the global market
- Domestic SSDs still lag in performance, reliability, and cost
- "Xinchuang" (IT localization) procurement is concentrated mainly in government/enterprise, finance, and telecom operators; internet/cloud providers still prioritize cost-effectiveness

> **Li Lu-style question**: Looking back 20 years from now, will this company be a "Standard Oil" or a "3Com"?
>
> **More likely "the MediaTek of this era, in its early days"** — entering a chip market monopolized by giants on the strength of an engineering-talent dividend and domestic-market demand, and gradually expanding share. But whether it can grow from a "follower" into a "challenger" depends on the commercialization progress of its self-developed controller and how the NAND cycle plays out. Twenty years from now, DapuStor will most likely still exist, but it may not be the leading player — rather, one of the top 10 participants in the industry.

---

## Step Seven: Valuation and Margin of Safety

### Current valuation (tool-verified)

| Metric | Value | Note |
|------|------|------|
| Share price | RMB 705 | June 23 close |
| Market cap | RMB 307.4 billion | ✅ Verified |
| PB | **383x** | ✅ Net assets of only ~RMB 800 million |
| PE (annualized Q1 EPS of ~RMB 3.40) | **~207x** | Assumes the Q1 profit level is sustained for the full year |
| PS (2025 revenue) | **~134x** | — |
| PS (annualized Q1 revenue) | **~59x** | — |
| IPO offer price | RMB 46.08 | 68 days ago |
| Series E valuation (Dec 2024) | RMB 6.8 billion | Inflated 45x over 17 months |

### Peer valuation comparison

| Company | PE (TTM) | PB | Main business |
|------|---------|-----|------|
| **DapuStor** | **~207x (Q1 annualized)** | **383x** | Enterprise SSD |
| Longsys | 13x | ~3x | SSD modules |
| Biwin Storage | 12x | ~2x | Storage modules |
| Demingli | 10x | ~2x | Storage modules |
| GigaDevice | 40x | ~5x | NOR Flash + MCU |
| Montage Technology | 50x | ~6x | Memory interface chips |

**DapuStor's valuation is 10-20x that of its storage-industry peers, one of the highest levels in the entire A-share semiconductor sector.**

### Another angle on valuation — if the dream comes true

Assuming DapuStor eventually becomes China's leading enterprise SSD maker, reaching by 5 years from now:
- Revenue of RMB 10 billion (vs. current RMB 2.289 billion, CAGR ~35%)
- Net profit of RMB 2 billion (net margin 20%)
- Applying a 30x PE
- Fair market cap = RMB 60 billion
- Corresponding share price = RMB 60 billion ÷ 436 million shares ≈ **RMB 138**

**Even under the most optimistic 5-year expectations, the current share price of RMB 705 is still overvalued by more than 4x.**

A more aggressive assumption (5% global market share 10 years from now):
- Revenue of $5 billion ≈ RMB 35 billion
- Net profit of RMB 7 billion (net margin 20%)
- Applying a 25x PE
- Fair market cap = RMB 175 billion
- Corresponding share price = **~RMB 401**

**Even the extremely optimistic 10-year scenario supports only 57% of the current price.**

> **Duan Yongping-style question**: If the stock market closed tomorrow for 5 years, would you be willing to hold at this price?
>
> **Absolutely not.** A share price of RMB 705 means paying RMB 307.4 billion for a company that has only just turned profitable for one quarter, has net assets of only RMB 800 million, and whose gross margin can fall to 3.5% when NAND prices swing. Even if revenue reaches RMB 10 billion and profit reaches RMB 2 billion five years from now, this investment would still be deeply underwater. The current price is not paying for reality — it is paying an extreme premium for an extremely optimistic dream.

---

## Step Eight: Composite Decision Memo

### Summary assessment

| Dimension | Conclusion | Confidence |
|------|------|--------|
| **Business quality** (Duan Yongping) | High technical barriers, with genuine rigid demand for domestic substitution. But NAND accounts for 80%+ of costs, so margins depend on factors outside the company's control; customer concentration is high | ★★★☆☆ |
| **Moat** (Buffett) | Technical barriers are the only moat, but they amount to a "first-mover dividend" rather than a "structural monopoly." Competitors are catching up | ★★☆☆☆ |
| **Management** (Duan Yongping + Buffett) | Yang Yafei's 16 years at Qualcomm, modest compensation, and three-year lock-up — excellent founder quality. The team has strong technical depth | ★★★★☆ |
| **Biggest risk** (Munger) | A valuation bubble (383x PB / 207x forward PE) + the 2027 lock-up expiry selling wave + the NAND price cycle | ★★★★★ |
| **Civilizational trend** (Li Lu) | AI storage is indeed at a civilizational-scale turning point, and the direction of domestic substitution is correct. But there is a huge gap between the company "being on the right track" and it being "a profitable investment" | ★★★★☆ |
| **Valuation** (Buffett + Duan Yongping) | **Extremely overvalued.** Even under the most optimistic 5-year expectations (revenue of RMB 10 billion / profit of RMB 2 billion / 30x PE), the fair price is only ~RMB 138, meaning the current RMB 705 is overvalued by more than 4x | ★★★★★ |

### Final decision

| Strategy | Recommendation |
|------|------|
| **Those with no position** | **Avoid decisively.** The current price of RMB 705 contains no margin of safety whatsoever. Even if DapuStor is an excellent technology company, buying at this price is almost certain to lose money. Those who believe in the domestic storage track should wait until after the 2027 lock-up expiry wave to reassess — by then the share price may have corrected significantly, and there will also be more quarters of profitability data available to validate the thesis |
| **Current holders** | **Sell immediately or cut the position sharply.** Those fortunate enough to have bought at the IPO or at a low price currently hold enormous paper gains and should lock them in. A market cap of RMB 307.4 billion cannot be supported by any reasonable valuation model |
| **Sell signal** | Any time is a sell signal — the current valuation is already far beyond any reasonable range |
| **Add-to-position signal** | The share price falling into the RMB 80-120 range (market cap of RMB 35-52 billion, corresponding to a reasonable 2027 PE of 20-30x, assuming annual profit of RMB 1.5-2.0 billion), combined with four consecutive quarters demonstrating sustainable profitability |

### Fair price range

| Scenario | Target price | Assumptions |
|------|--------|------|
| Extremely optimistic (5 years) | RMB 130-150 | Revenue of RMB 10 billion, profit of RMB 2 billion, PE 30x |
| Neutral (3 years) | RMB 80-120 | Revenue of RMB 6 billion, profit of RMB 1 billion, PE 25x |
| Pessimistic | RMB 30-50 | Growth falls short of expectations, reverting to near the Series E valuation |
| **Current RMB 705** | **Overvalued 4-8x** | — |

### Simulated commentary from the four masters

> **Buffett**: "I don't invest in things I don't understand — SSD controller chips are outside my circle of competence. But there's one thing I do understand: 383x PB means you're paying 383 times net assets. Even if this company turns into China's Samsung tomorrow, buying in today would still very likely lose you money. Price matters enormously."

> **Munger**: "Invert — 17 months ago this company was worth RMB 6.8 billion; today it's worth RMB 307.4 billion. Did its engineer headcount grow 45x? Did its customer count grow 45x? Did its revenue grow 45x? None of the above. So what accounts for the 45x? The answer: the artificial scarcity created by a mere 6.2% free float, plus the frenzy of the AI narrative. This is speculation, not investing."

> **Duan Yongping**: "Yang Yafei is an admirable entrepreneur — 16 years at Qualcomm, then returning home to start a business, on an annual salary of only RMB 1.09 million. That kind of founder deserves a vote of confidence. But not at RMB 705. I'd be willing to seriously study this in the RMB 80-100 range — at that price, even if I'm wrong, I won't lose too much."

> **Li Lu**: "The direction of AI storage is unquestionably correct. DapuStor may well become China's leading enterprise SSD company 10 years from now. But investing is not about forecasting the future — it's about paying a reasonable price for the right future. Those who bought Microsoft in 1999 were completely right about the direction, but it took 16 years to break even. Those who buy DapuStor at RMB 705 may face an even longer wait."

---

## AI Analysis Confidence vs. Investment Certainty

### High-confidence conclusions based on sufficient data

1. **The current valuation is extremely overvalued** — 383x PB and 207x forward PE are mathematical facts, confirmed by tool-verified calculation
2. **The technical team's background is excellent** — Yang Yafei's 16 years at Qualcomm plus a core team from Samsung/Marvell/Huawei, well documented in public information
3. **The extremely small free float has driven up the share price** — a 6.2% float ratio creates artificial scarcity that does not reflect true valuation

### Medium-confidence inferences based on limited information

4. **The sustainability of the Q1 2026 turnaround to profitability** — with only one quarter of data, whether the 37.6% gross margin is sustainable depends heavily on NAND price trends
5. **The quality of the RMB 4.7 billion order backlog** — official data, but the speed of conversion into revenue and the associated margins are unknown
6. **The commercialization progress of the self-developed controller** — 2024 revenue was only RMB 258,300, far from reaching scale

### Low-confidence judgments due to insufficient data

7. **The scale of orders from major international customers** — order amounts from Nvidia/Google/xAI come from unofficial channels and cannot serve as a basis for investment decisions
8. **The long-term market-share ceiling** — competitive responses from Samsung/Micron, technology-roadmap evolution, and policy changes are all unpredictable
9. **The share-price floor after the 2027 lock-up expiry** — depends on market sentiment and earnings validation, and cannot be precisely predicted

### Checklist of questions requiring first-hand verification

1. **Actual shipment volumes and customer feedback for the self-developed DP800 controller**: 2024 revenue from the self-developed PCIe 5.0 controller was only RMB 258,300 — has it increased substantially in 2025/2026?
2. **Terms of NAND procurement agreements**: Is the pricing mechanism with Kioxia/YMTC fixed or floating? What is the price-locking capability?
3. **The actual scale of Google/Nvidia orders**: the amounts have never been officially disclosed, and market rumors are unreliable
4. **The cyclical pattern of gross margin**: has a mechanism been established to hedge against NAND price swings (such as price-lock contracts)?
5. **Competitor progress**: when will enterprise-grade products from Deyi Microelectronics, Yingren Technology, and others reach mass production? Could they siphon off DapuStor's customers?

**Summary**: DapuStor is a domestically developed enterprise SSD company with the right direction and excellent technology, and an admirable founder. But at a price of RMB 705 / a market cap of RMB 307.4 billion, there is no margin of safety whatsoever. The market is trading the dream of "AI storage domestic substitution," not the company's current fundamentals. The recommendation is to stay away from the current price and reassess after the 2027 lock-up expiry wave brings a valuation correction.

---

*Report generated on: June 23, 2026*
*Data sources: company prospectus, 2025 annual report, Q1 2026 quarterly report, Jiemian News, TMTPost, Securities Times, Eastmoney, Ifeng, OFweek, DapuStor's official website*
*Key figures were cross-validated using the financial_rigor.py tool*
*This report is for research reference only and does not constitute investment advice*
