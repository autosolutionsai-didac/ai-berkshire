# Marvell Technology (MRVL) Investment Research Report

**Date:** May 16, 2026
**Share price:** $176.89 (close on 2026.5.15)
**Market cap:** $154.7 billion
**Research framework:** Combined Buffett-Munger-Duan Yongping-Li Lu four-master analysis

---

## Information richness rating: Grade A (information-rich)

Marvell is a Nasdaq-listed company with dense sell-side coverage (26+ analysts), heavy media coverage during earnings season, and an extremely hot AI/semiconductor sector narrative.

**AI research limitation disclosure:** Because information is so abundant, this report carries a risk of "excessive consensus" — much of the analysis converges with mainstream market opinion. The report therefore emphasizes contrarian checks: why wouldn't smart investors buy this? What risks are being overlooked? How much optimism is already priced in?

**Bias self-check:**
- [x] The sense of certainty comes mainly from the volume of material rather than deep understanding of the business's essence — the true customer stickiness of custom ASICs requires more primary-source verification
- [x] AI-generated output closely tracks market consensus (bullish on AI infrastructure / bullish on custom silicon), limiting the informational edge
- [x] Must guard against the narrative bias of "high growth = good company"

---

## Step 1: Key data overview

### Core financial data

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|------|--------|--------|--------|--------|--------|--------|
| Revenue ($B) | 2.97 | 4.46 | 5.92 | 5.51 | 5.77 | 8.20 |
| YoY growth | — | +50% | +33% | -7% | +5% | +42% |
| Non-GAAP gross margin | 63.3% | — | — | — | 61.0% | ~62% |
| GAAP operating margin | -8.7% | -7.8% | 4.0% | -10.3% | -12.5% | — |
| Non-GAAP operating margin | 24.2% | — | — | — | ~33% | ~38% (est.) |
| Operating cash flow ($M) | 817 | 819 | 1,289 | 1,371 | 1,681 | — |
| Free cash flow ($M) | ~650 | 650 | 1,083 | 1,034 | 1,397 | — |

Data sources: Marvell IR press releases, StockAnalysis.com, SEC filings

### FY2026 segment revenue mix (as of January 2026)

| Segment | Revenue | Share | YoY growth |
|------|------|------|---------|
| Data center | ~$6.0B | 74% | +46% |
| Enterprise networking | ~$626M | 8% | bottoming out |
| Carrier infrastructure | ~$338M | 4% | 5G slowdown |
| Consumer | ~$316M | 4% | stable |
| Automotive/industrial | ~$322M | 4% | sold to Infineon |
| **Total** | **$8,195M** | **100%** | **+42%** |

### Current valuation (tool-verified calculations)

| Metric | Value | Verification method |
|------|------|----------|
| Market cap | $154.7B | 874.5M shares × $176.89 = $154.7B ✅ |
| PE (TTM, GAAP) | 57.6x | $176.89 / $3.07 ✅ |
| Forward PE (FY2027E) | ~46.5x | Based on consensus EPS ~$3.80 |
| PS (TTM) | 18.9x | $154.7B / $8.195B ✅ |
| P/FCF | 110.6x | $176.89 / $1.60 (FY2025 FCF per share) ✅ |
| PEG | ~1.12 | Based on 30%+ growth expectations |
| Beta | 2.25 | high volatility |
| 52-week range | $58.61 - $192.15 | up more than 200% over the past year |

### Cross-validation record for key data points

```
Market cap check: 874.5M × $176.89 = $154.69B vs. reported $154.7B → deviation 0.01% ✅
FY2026 revenue: Marvell IR / Futurum / SeekingAlpha — three sources agree → $8,195M ✅
Shares outstanding: StockAnalysis 874.5M / Marvell PR basic 865.5M / diluted 877M → deviation <2% ✅
```

---

## Step 2: Business-essence analysis — Duan Yongping's "the right business"

### One-sentence definition

**Marvell is the "plumber" of the AI data center — it does not do general-purpose GPU compute, but instead designs custom chips for hyperscale cloud providers and supplies high-speed optical interconnect, holding the number-two position in the Broadcom-Marvell ASIC duopoly.**

### Business model canvas

| Dimension | Characteristics |
|------|------|
| Revenue model | Chip sales (one-time) + custom design services (multi-year contracts) |
| Customer type | Hyperscale cloud providers (AWS/Google/Microsoft) as the core |
| Value proposition | Help customers design purpose-built AI chips more efficient than general-purpose GPUs |
| Repeat-purchase driver | Each chip design cycle lasts 3-4 years, creating technology lock-in |
| Gross margin | Non-GAAP ~61%, typical for a fabless semiconductor company |

### Two business pillars

1. **Custom ASIC (Custom XPU):** Co-designs AI accelerator chips with AWS (Trainium), Microsoft (Maia), and Google. FY2026 revenue of $1.5 billion, growth has doubled. Marvell contributes SerDes, interconnect, packaging and other IP, integrated into the customer's proprietary chip.

2. **Optical interconnect (Optical DSP):** 800G/1.6T PAM4 optical DSP chips that connect GPU/XPU clusters within data centers. Market share exceeds 60%, with a technology lead of 1-2 generations.

### Gross margin analysis

Non-GAAP gross margin holds in the 61-63% range, typical for a fabless semiconductor company (designs IP, does not own fabs). But note:

- GAAP gross margin is only 41% — the gap comes from the large intangible-asset amortization tied to acquisitions (Inphi $10 billion, Cavium $6 billion, and others)
- Gross margin shows no clear expansion trend, indicating limited pricing power in the custom ASIC business — customers are hyperscalers far larger than Marvell itself
- Comparison: Broadcom's Non-GAAP gross margin exceeds 70%, Nvidia's exceeds 75%. Marvell's 61% is comparatively low, reflecting its positioning as a "design service provider" rather than a "platform" company

### Operating leverage

- Revenue grew from $5.5 billion in FY2024 to $8.2 billion in FY2026 (+49%), while Non-GAAP operating margin rose from ~25% to ~38%
- Positive operating leverage is evident: the marginal leverage of R&D spend shows up at scale
- But this is a typical feature of semiconductor companies, not a unique advantage

### Duan Yongping-style question

> What is good about this business? If you had to describe it in one sentence, what would it be?

**What's good**: it occupies the "shovel-seller" position in the AI wave, and once a customer selects a design partner, switching mid-stream is difficult.

**On the other hand**: this is fundamentally a business "dependent on major customers." AWS and Google hold absolute bargaining power — Marvell is essentially their high-end outsourced design team. The quality of this business is inferior to Nvidia, which owns its own ecosystem, or Broadcom, which has a broader customer base.

---

## Step 3: Moat assessment — Buffett's "economic moat"

| Moat type | Assessment | Strength |
|-----------|------|------|
| Brand/pricing power | ❌ Not applicable. B2B chip design, no consumer brand. Facing giant customers like AWS/Google, pricing power is limited | Weak |
| Switching costs | ✅ Custom ASIC design cycles run 3-4 years and integrate deeply with the customer's architecture, making a mid-stream switch extremely costly | Strong |
| Network effects | ❌ Not present. Chip design does not exhibit network-effect characteristics | None |
| Economies of scale | ⚠️ Limited. IP reuse lowers marginal design cost, but scale is far smaller than Broadcom's | Moderate |
| Technology/patent barriers | ✅ 10,000+ patents, 60%+ market share in optical DSP, first-mover in 2nm, leading in SerDes | Strong |

### Moat trend

**Past 5 years: clearly widening**
- The 2021 Inphi acquisition established leadership in optical interconnect
- Custom ASIC customers expanded from one to three to four hyperscalers
- Entry into 5nm/3nm advanced process nodes widened the technology gap
- Nvidia's $2 billion investment validated the platform's value

**Next 5 years: key variables**
- Possible widening: AI compute demand keeps surging, custom ASIC penetration rises from ~10% to 25%+
- Risk of narrowing: Broadcom's scale advantage keeps expanding; hyperscalers' in-house design capability strengthens (Google already has in-house TPU experience); new entrants (such as Alchip, GUC) erode the low end of the market

### Buffett-style question

> Will this moat still be there in 10 years? What could destroy it?

**A plausible surviving scenario:** If AI compute demand keeps growing strongly and custom ASICs retain their economic advantage, Marvell's multi-generation design experience and IP accumulation will continue to form a barrier.

**Scenarios that could destroy it:**
1. Hyperscalers build internal chip-design teams (Google has already done part of its TPU design this way)
2. General-purpose GPU architecture efficiency catches up, eliminating the ASIC's cost advantage
3. New chip-design EDA tools/AI-assisted design sharply lower design barriers
4. Broadcom, leveraging greater scale and more customers, continues to squeeze Marvell's living space

---

## Step 4: Inversion and risk checklist — Munger's "invert, always invert"

### Paths by which Marvell could fail

| Failure path | Probability | Impact | Notes |
|----------|------|----------|------|
| AWS/Microsoft cut AI capex | Medium (20-30%) | Fatal | 74% of revenue comes from data center; customer concentration is extremely high |
| Core customer switches design partner | Low-medium (15%) | Severe | AWS shifts to Broadcom or in-house design, revenue cliff |
| General-purpose GPUs keep crushing ASICs | Low (10%) | Severe | Nvidia's architecture keeps improving, eroding the ASIC's cost advantage |
| Broadcom cuts prices sharply to win customers | Medium (20%) | Moderate | Broadcom has the scale advantage to wage a price war |
| China geopolitical risk | Medium (25%) | Moderate | China accounted for 43% of FY2025 revenue; tariff/sanctions impact uncertain |
| Celestial AI integration fails | Low-medium (15%) | Moderate | $3.25 billion acquisition, revenue not expected until FY2028, technology path unproven |
| AI bubble bursts | Medium (20%) | Fatal | Valuation is based on 30%+ growth expectations; once growth slows, a double hit of valuation compression plus earnings miss follows |

### Historical analogies

| Company | Similarity | Outcome |
|------|--------|------|
| **Xilinx (2015-2022)** | FPGA/ASIC design, dependent on major customers, acquired by AMD | Acquired (an OK outcome) |
| **3Com (1990s)** | Second place in networking equipment, fell behind Cisco | Declined, acquired by HP |
| **LSI Logic (2000s)** | Custom ASIC design service provider, concentrated customer base | Growth stalled, acquired by Avago (now Broadcom) |
| **Altera (2010-2015)** | FPGA design, dependent on major customers such as Intel | Acquired by Intel |

**Historical lesson:** In semiconductors, the long-term independent survival rate of "the second-place design service provider" is not high. Either you get acquired, or the leader keeps pulling further ahead. Marvell needs to prove it can grow from "a strong number two" into "a co-equal number one."

### Bias self-check

- **Narrative bias:** The narrative "AI changes the world → custom chips are needed → Marvell benefits" is too neat and too linear. In reality the technology path is full of uncertainty
- **Anchoring effect:** With the stock up from $58 to $177, it's easy to anchor on "it can still go higher." But from the $177 starting point, the upside is now far smaller than the downside risk
- **Survivorship bias:** What we observe is the story of Marvell successfully winning AWS/Microsoft contracts; we don't see the bids that were lost or the projects that were cancelled

### Core bear thesis

1. **Absurd valuation:** PS of 18.9x, P/FCF of 110x, forward PE of 46.5x — even assuming FY2028 revenue of $15 billion, the implied forward PS at the current market cap is still 10x+
2. **Customer concentration is a time bomb:** if AWS fails to renew a single contract, revenue could fall 20-30%
3. **Broadcom's scale crush:** Broadcom's ASIC market share is 60-70%, with more customers, a fuller IP portfolio, and more pricing flexibility
4. **Continued GAAP losses:** five consecutive years of GAAP net losses; Non-GAAP figures paper over large acquisition-related amortization and stock-based compensation
5. **China exposure:** 43% of FY2025 revenue came from China, and geopolitical risk is underappreciated

### Munger-style question

> Where am I most likely to be wrong? Why would smart people not buy — or even short — this company?

**The most likely mistake:** equating "the long-term AI trend is certain" with "Marvell's near-term certainty is high." AI trend certainty ≠ this company will necessarily keep winning contracts ≠ the current valuation is reasonable. There are large logical leaps between each of the three steps.

**Why smart investors wouldn't buy:** at $177 you need to believe Marvell can grow revenue from $8.2 billion to $15 billion within 3 years while also expanding margins — if any link in that chain breaks, the downside is 30%+. The risk/reward is asymmetric.

---

## Step 5: Management assessment — Duan Yongping's "the right people" + Buffett's "management integrity"

### CEO Matt Murphy's key decisions in review

| Time | Decision | Outcome | Rating |
|------|------|------|------|
| 2016 | Joined Marvell, launched strategic transformation | Pivoted from consumer electronics to data infrastructure | ★★★★★ |
| 2017 | $6 billion acquisition of Cavium | Gained DPU/security processor capability, successfully integrated | ★★★★ |
| 2019 | Acquired Avera + Aquantia | Strengthened ASIC and Ethernet, paved the way for subsequent growth | ★★★★ |
| 2021 | $10 billion acquisition of Inphi | Established leadership in optical interconnect, proved highly correct in hindsight | ★★★★★ |
| 2021 | $1.1 billion acquisition of Innovium | Entered the data-center switch-chip market | ★★★ |
| 2025 | Sold automotive Ethernet business to Infineon | Focused on the core business, raised $2.5 billion in cash | ★★★★ |
| 2026 | $3.25 billion acquisition of Celestial AI | Positioning in photonic interconnect, still to be validated | Pending |

### Capital allocation capability

- **R&D spending:** FY2025 R&D expense was about $1.9 billion, or 33% of revenue — above the industry average, but reasonable given the high IP intensity of custom ASIC
- **M&A success rate:** 4 out of 5 large acquisitions (Cavium, Inphi, Innovium, Avera) are viewed by the market as successful — an unusually high hit rate
- **Buybacks:** in 2026 the company launched a $5 billion buyback authorization plus a $1 billion accelerated buyback, signaling management's confidence in its own valuation
- **Dividend:** minimal (~0.2% yield), prioritizing growth investment instead

### Management ownership and incentive alignment

- Murphy directly holds about 256,000 shares (worth ~$45 million), a reasonable proportion of total compensation
- 96% of compensation structure is equity-based — highly aligned with shareholder interests
- A small recent sale of 37,500 shares ($3.97 million) — a minor proportion, normal monetization
- **On the other hand:** management's total ownership stake is very low (<0.1%), a common issue at large tech companies

### Organizational capability

- In July 2025, Chris Koopmans was promoted to President and COO — clear succession planning
- A dedicated Data Center business-unit president (Sandeep Bharathi) was established — organizational structure matches strategy
- Key-person risk: if Murphy departs, the market might apply a 10-15% uncertainty discount

### Duan Yongping-style question

> If the CEO retired, could this company maintain its competitiveness?

**Plausibly yes:** Murphy has already established a clear strategic direction (focus on data center), a succession pipeline (Koopmans), and a customer relationship network. Core technical capability is embedded within the organization.

**The risk lies in:** in the semiconductor industry, the CEO/CTO's personal judgment on technology direction is critical. Murphy's strategic acumen in M&A (especially his timing on the Inphi acquisition) is hard to replicate. Whether the next generation of leadership can make decisions of equal quality remains uncertain.

---

## Step 6: Industry and civilizational trends — Li Lu's "civilizational evolution framework"

### Judgment on the civilizational paradigm shift

AI is indeed the most important technology paradigm shift since the internet. The exponential growth in data-center compute demand is driving structural demand for custom chips and high-speed interconnect.

**But a distinction must be drawn:**
- ✅ AI is a civilizational-scale trend = high certainty
- ⚠️ Custom ASIC is a necessary component of AI = medium certainty (general-purpose GPUs still dominate)
- ⚠️ Marvell is the long-term winner in custom ASIC = lower certainty (competition is intense, customers can switch)

### Technology-revolution analogies

| Historical analogy | Marvell's corresponding role | Outcome |
|----------|----------------|------|
| Steel companies of the railroad era | The plumber supplying the "rails" | A few survived and thrived, most were eliminated |
| Cisco of the internet era | Networking equipment supplier | 20 years after the 2000 bubble, still hasn't reclaimed its prior high |
| Qualcomm of the mobile internet era | Supplier of core chip IP | Successful, but valuation has long lagged the market |
| Intel of the cloud-computing era | Server chip supplier | Benefited enormously early on, later eroded by AWS in-house design plus AMD/Arm |

**Key lesson:** "Shovel-selling" businesses perform extremely well in the early stages of a technology wave, but face two long-term risks: (1) customers building in-house capability; (2) competitors catching up.

### TAM and ceiling

| Market | 2025 | 2028 forecast | CAGR |
|------|--------|-----------|------|
| Data-center semiconductors | ~$40B | $94B | ~35% |
| Custom ASIC | ~$10B | $40.8B | ~47% |
| Optical interconnect | ~$5B | $15B+ | ~30% |

Marvell management's target: 20% data-center market share by 2028 (up from 10%), implying revenue of ~$19 billion. This target is very aggressive.

### Position in the industry value chain

```
AI application layer (OpenAI/enterprise customers)
    ↓
Cloud platform layer (AWS/Google/Microsoft) — decides whether to use GPU or ASIC
    ↓
Chip design layer ← Marvell sits here (custom ASIC + optical interconnect)
    ↓
Chip manufacturing layer (TSMC)
```

Marvell occupies the middle layer — subject to upstream cloud providers' capex decisions and dependent on downstream TSMC's manufacturing capacity. Squeezed from both sides, with limited autonomy.

### Li Lu-style question

> Looking back 20 years from now, will this company be "the Standard Oil of this era" or "the flash-in-the-pan 3Com"?

**Most likely outcome:** neither Standard Oil nor 3Com. More likely to be **"the Qualcomm of this era"** — achieving substantial growth in the AI wave, becoming an important but non-dominant participant, with its long-term valuation reverting to a reasonable level (20-30x PE).

**Optimistic scenario (20% probability):** becomes the Broadcom of the AI era — through continued M&A and customer expansion, growing into a data-infrastructure giant with $50 billion+ in revenue.

**Pessimistic scenario (20% probability):** becomes the next acquired LSI Logic — customer concentration erodes bargaining power, and after growth slows, it is acquired by a larger player.

---

## Step 7: Valuation and margin of safety — Buffett's "intrinsic value" + Duan Yongping's "the right price"

### Current market pricing

| Metric | Marvell | Broadcom | Nvidia | Industry average |
|------|---------|----------|--------|----------|
| Trailing PE | 57.6x | ~62x | ~41x | ~35x |
| Forward PE | ~46.5x | — | ~28x | ~30x |
| PS (TTM) | 18.9x | ~15x | ~25x | ~8x |
| P/FCF | 110.6x | ~35x | ~45x | ~30x |
| PEG | 1.12 | ~1.5 | ~0.9 | 1.0-1.5 |

### Reverse DCF: what expectations does the current stock price imply?

At $176.89, assuming a terminal PE of 25x and a discount rate of 10%:
- Implies FY2029 EPS needs to reach ~$7.0 (2.3x the current $3.07)
- Implies revenue needs to reach ~$18B (2.2x the current $8.2B)
- Implies a 4-year revenue CAGR of ~22%

**Judgment:** the growth expectation implied by market pricing (4-year CAGR of 22%) is broadly consistent with management guidance (FY2027 +30%, FY2028 +40-50%). If management delivers on guidance, the current price is roughly reasonable; if growth falls short, the downside is significant.

### Three-scenario valuation (precise tool-based calculation)

| Scenario | 3-year EPS growth | Target PE | 3-year target price | Change |
|------|-----------|--------|-----------|--------|
| **Bull** | 40%/year | 50x | $421 | +138% |
| **Base** | 30%/year | 40x | $270 | +53% |
| **Bear** | 15%/year | 30x | $140 | -21% |

**Probability-weighted expected value:** assuming bull 25% / base 50% / bear 25%
- Expected target price = $421×0.25 + $270×0.50 + $140×0.25 = $275
- Expected return = +55% (3-year), roughly 16% annualized

### Historical valuation comparison

- Marvell's forward PE range over the past 3 years: 25x-65x
- The current 46.5x sits at a moderately high level
- At the late-2022 trough, forward PE was around 25x (a period of slowing growth plus industry inventory correction)

### Peer valuation comparison

Marvell's PEG (1.12) looks cheaper than Broadcom's (~1.5), but:
- Broadcom has a more diversified customer base, higher margins, and greater scale
- Nvidia's PEG is even lower (~0.9), with a more secure market position
- Marvell's "cheapness" may reflect the market's discount for customer-concentration risk

### Duan Yongping-style question

> If the stock market closed tomorrow for 5 years, would you be willing to hold at this price?

**Answer: leaning toward hesitant.** The $177 price requires everything to go right — AI capex to keep growing, Marvell to retain its customer relationships, Broadcom to refrain from a price war, and China risk not to materialize. If any one of these assumptions fails, the return five years from now could be disappointing.

If the price were at $120-130 (corresponding to a 30-35x forward PE), the margin of safety would be more adequate.

---

## Step 8: Comprehensive decision memo

### Summary assessment

| Dimension | Conclusion | Confidence |
|------|------|--------|
| Business quality (Duan Yongping) | Above average — custom ASIC has technology barriers and customer lock-in, but is fundamentally an "outsourced design for big customers" business with limited pricing power | ★★★ |
| Moat (Buffett) | Moderate-to-strong — switching costs and technology barriers are the core, but scale trails Broadcom and customers can switch | ★★★ |
| Management (Duan Yongping + Buffett) | Excellent — Murphy's strategic vision and M&A execution rank among the best in the industry | ★★★★ |
| Biggest risk (Munger) | Customer concentration plus overvaluation — any sign of growth falling short of expectations would trigger a sharp decline | ★★★★ |
| Civilizational trend (Li Lu) | Favorable — AI data center is a high-certainty trend, and Marvell sits at a key position in the value chain | ★★★★ |
| Valuation (Buffett + Duan Yongping) | Expensive — the current price already fully reflects optimistic expectations, leaving insufficient margin of safety | ★★ |

### Final decision

| Strategy | Recommendation |
|------|------|
| **Those with no position** | Stay on the sidelines and wait. At the current $177, the valuation already fully prices in three years of future growth, and the risk/reward is unfavorable. Wait for a pullback to the $120-135 range (corresponding to a forward PE of 30-35x) before considering a position |
| **Existing holders** | May continue to hold but set a stop-loss. If your cost basis is far below the current price, ride the trend while staying alert. FY2027 Q1 earnings (May 27) is the key validation point |
| **Sell signals** | (1) any news of a major customer (AWS/Microsoft) delaying or cancelling an ASIC project (2) AI capex growth declining for two consecutive quarters (3) Broadcom winning the next-generation contract from one of Marvell's existing customers (4) further deterioration in US-China relations disrupting the supply chain |
| **Add-to-position signals** | (1) a 30%+ pullback to the $120-135 range (2) FY2027 revenue growth exceeding expectations (>35%) (3) a new major ASIC customer added (e.g., Meta/ByteDance) (4) Celestial AI's technology validated ahead of schedule |

### Simulated commentary from the four masters

> **Buffett:** "This is a good company in a good industry. But a good company at the wrong price can still be a bad investment. Buying at 57 times earnings requires a great many things to go right for you to make money. I'd rather buy below 30 times."

> **Munger:** "Invert. When everyone is excitedly talking about AI chips, ask yourself: what happens if AI capex falls 30% next year? What happens if AWS decides to design in-house the way Google did with the TPU? At a $154.7 billion market cap, you're not betting on whether the company is good — you're betting on whether it's good enough to exceed everyone else's expectations in the market."

> **Duan Yongping:** "It's the right company, and the CEO is the right person. Murphy's acquisition decisions have been right time after time — that kind of judgment is rare. But the price isn't quite right — I want to buy at a price where 'no matter what happens, I can't lose much.' $177 isn't that price."

> **Li Lu:** "AI is a certain trend in civilizational evolution, and Marvell stands on the right side of it. But history tells us that within a technology paradigm shift, the 'shovel sellers' end up with mixed outcomes — you need to distinguish who is Cisco (hasn't reclaimed its prior high 20 years later) from who is TSMC (continuously creating value). Right now, Marvell trades more like the former's valuation while hoping for the latter's growth."

---

## AI analysis confidence vs. investment certainty

| Dimension | AI analysis confidence | Investment certainty | Notes |
|------|-------------|-----------|------|
| Financial data | High (multi-source verified) | — | historical data is reliable |
| Industry trend | High (clear consensus) | Medium | long-term AI demand is certain, near-term volatility is not |
| Competitive landscape | Medium | Medium | the duopoly is currently stable, but uncertain 5 years out |
| Durability of customer relationships | Low (lacks primary-source information) | Low | contract details are not public; willingness to renew requires verification |
| Management capability | Medium | Relatively high | there is a clear historical decision record to judge |
| Valuation reasonableness | High (tool-verified) | Low | valuation depends on future growth assumptions, not historical data |

**Key distinction:** the data accuracy in this report is high (AI analysis confidence is high), but the certainty of the core investment judgment — "can Marvell sustain 30%+ growth" — remains low, because it depends on hard-to-predict variables such as customer relationships, competitive dynamics, and the AI capex cycle.

**High-confidence conclusions:**
- Marvell holds the clear number-two position in data-center ASICs
- Management execution is excellent, and its M&A integration capability is best-in-class
- The current valuation (57x PE / 18.9x PS) prices in very optimistic growth expectations

**Low-confidence conclusions (requiring primary-source verification):**
- Whether AWS/Microsoft will continue choosing Marvell for their next-generation ASICs
- The long-term economic comparison between custom ASIC and general-purpose GPU
- The commercialization timeline for Celestial AI's photonic interconnect technology
- The sustainability of 43% China revenue exposure under geopolitical pressure

---

## Data sources

- Marvell Technology Investor Relations (quarterly/annual earnings press releases)
- StockAnalysis.com (financial data, valuation metrics)
- Futurum Group (Q3/Q4 FY2026 analysis)
- Seeking Alpha (analyst articles, revenue guidance)
- TipRanks/MarketBeat (analyst ratings and price targets)
- CNBC (Nvidia investment, Celestial AI acquisition)
- Tom's Hardware (industry developments)
- Counterpoint Research (ASIC market forecasts)
- Marvell official blog and press releases (technology roadmap)

---

*Report completed: May 16, 2026*
*Next update trigger: FY2027 Q1 earnings (May 27, 2026)*
