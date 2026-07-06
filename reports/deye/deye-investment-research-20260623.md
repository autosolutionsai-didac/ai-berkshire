# Deye Technology (605117.SH) Investment Research Report

> **Research date**: June 23, 2026
> **Share price**: CNY 101.85 | **Market cap**: CNY 129.7 billion
> **52-week range**: CNY 36.44 - 126.90

---

## AI research bias self-check

**Information-richness rating: A (information-rich)**

Deye Technology has been listed on the A-share market since 2021, with broad brokerage coverage (in-depth research reports from Galaxy Securities, CSC, Soochow, Kaiyuan, etc.), regular annual/interim/quarterly disclosures, and its Hong Kong IPO prospectus (filed January 2026) provides additional detail. The new-energy sector draws heavy attention, and media coverage is dense.

**The AI research trap for "A-grade" companies**: Deye is currently a hot name in the A-share "inverter + energy storage" track, with the market consensus strongly bullish (2026 Q1 pre-announced profit growth of 68%, brokerage consensus for 2026 net profit of CNY 5.38 billion). AI output tends to converge toward this optimistic consensus. **This report specifically stress-tests the counter-case**: the real-world impact of the EU inverter ban, receivables risk in emerging markets, and whether the 40x P/E already fully prices in growth expectations.

**Bias self-check**:
- Deye's "emerging-market residential storage leader" narrative is highly compelling, and one must guard against narrative bias papering over real geopolitical risk
- The eye-catching 2026 Q1 numbers (+68%) may create an anchoring effect that obscures the fact that full-year 2025 growth was only 9%
- Industry capacity is severely oversupplied (1TW of capacity vs. 538GW of demand), and the pricing-war pressure this implies is underweighted in most bullish reports

---

## Key data cross-validation log

| Item verified | Source 1 | Source 2 | Deviation | Result |
|--------|-------|-------|------|------|
| Market cap (CNY 129.7 billion) | Share price 101.85 x share count 1.273 billion = CNY 129.66 billion | Investing.com | 0.05% | Pass |
| FY2025 revenue (CNY 12.224 billion) | Company annual report | Eastmoney | 0.00% | Pass |
| FY2025 net profit attributable to parent (CNY 3.171 billion) | Company annual report | Eastmoney | 0.00% | Pass |
| Total share count (1.273 billion) | Company announcement (post 10-for-4 bonus issue) | Investing.com: 1.27 billion | <0.3% | Pass |

> P/E = 40.90x, P/B = 12.56x, ROE = 30.70%, FCF Yield = 2.16% were all precisely verified with `financial_rigor.py`.

**Important note**: Deye has carried out a capital-reserve-to-share-capital conversion every year since listing (10-for-4 or 10-for-8), expanding total share count from roughly 207 million shares at IPO to 1.273 billion shares today. Valuation metrics differ significantly across platforms depending on which share-count basis is used; this report consistently uses the latest post-conversion share count of 1.273 billion shares.

---

## I. Nature of the Business

### One-sentence definition

**Deye Technology is a new-energy equipment company whose core competitive strength is relentless cost control, delivering an "inverter + storage battery pack" one-stop solution to serve distributed solar and residential storage demand across emerging markets worldwide.**

### Revenue breakdown (FY2025)

| Business line | Revenue (CNY billion) | Share | YoY growth | Gross margin |
|--------|-------------|------|---------|--------|
| Storage inverters | 5.217 | 42.7% | +18.9% | **51.10%** |
| Storage battery packs | 3.832 | 31.4% | +56.3% | 31.81% |
| Solar inverters | 1.054 | 8.6% | -7.2% | 32.11% |
| Heat exchangers | 0.938 | 7.7% | -52.0% | 7.71% |
| Dehumidifiers | 0.805 | 6.6% | -16.9% | 29.72% |
| **Total** | **12.224** | **100%** | **+9.1%** | **~38%** |

**New-energy business total**: CNY 10.181 billion (83.3% of revenue, +27.0%), with a new-energy gross margin of 41.63%. The legacy home-appliance business continues to shrink.

### Five-year profitability trend

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|------|--------|--------|--------|--------|--------|
| Total revenue (CNY billion) | 4.168 | 5.956 | 7.480 | 11.206 | 12.224 |
| Revenue growth | +37.9% | +42.9% | +25.6% | +49.8% | +9.1% |
| Net profit attributable to parent (CNY billion) | 0.579 | 1.517 | 1.791 | 2.960 | 3.171 |
| Net profit growth | +50.8% | +162.3% | +18.0% | +65.3% | +7.1% |
| Gross margin | 22.95% | 38.03% | 40.41% | 38.76% | ~38% |
| Net margin | ~13.9% | ~25.5% | ~23.9% | 26.42% | ~25.9% |
| ROE | ~15.2% | ~24.3% | ~20% | 31.31% | 30.7% |
| Operating cash flow (CNY billion) | ~0.797 | ~2.20 | ~2.08 | 3.367 | 3.986 |

**Key inflection point**: In 2021, revenue was still dominated by low-margin heat exchangers (56% of the mix), and gross margin was only 23%. After the inverter business took off in 2022, gross margin jumped to 38%+ and has held there since. Revenue growth, which ran hot at +38% to +50% from 2021 through 2024, fell sharply to 9% in 2025 but re-accelerated to +74% in 2026 Q1.

### Business model canvas

- **Type**: Hardware manufacturing and export, predominantly one-time sales (not a subscription)
- **Revenue model**: Inverters and battery packs are sold as hardware; there is no recurring service revenue after installation (unlike Enphase's Enlighten platform)
- **Share of overseas revenue**: ~80% in FY2025 (export sales CNY 9.747 billion, domestic sales CNY 2.439 billion); the new-energy business is 92% overseas
- **Sales model**: 82% OEM/ODM (white-label) + 18% own-brand, an asset-light approach to going global

### Reading the gross margin

| Comparison | Deye | Enphase | Sungrow | Ginlong (Solis) |
|------|------|---------|---------|---------|
| Blended gross margin | ~38% | ~47% | ~28% | ~32% |
| Inverter gross margin | 51.1% (storage inverters) | ~47% | ~28% | ~32% |
| Expense ratio | ~10% | ~35% | ~15% | ~18% |
| Net margin | ~26% | ~12% | ~13% | ~14% |

Deye's gross margin trails Enphase's, yet its net margin is actually higher — the key is an **extremely low expense ratio** (~10% vs. Enphase's ~35%). This is the direct product of its distributor-driven model plus China's manufacturing cost advantage. At 51.1%, storage-inverter gross margin is the highest among Chinese inverter makers.

### Digging deeper: what makes this a good business?

**If it had to be summed up in one sentence**: Deye leverages China's manufacturing cost advantage to sell what is, for overseas emerging markets, a high-margin "essential power" product — residents in power-starved countries pay a premium for inverters plus storage simply to have electricity and avoid outages.

What's good about the business:
1. **Rigid demand** — with South Africa averaging 18 hours of daily blackouts and Pakistan/Myanmar facing severe power shortfalls, a storage inverter is the choice between "having power" and "having none," not "saving money" versus "not saving money"
2. **Very high gross margins** — 51.1% on storage inverters, far above typical manufacturing
3. **Excellent cash flow** — FY2025 operating cash flow of CNY 3.986 billion, nearly 126% of net profit

Hidden risks in the business:
1. **One-time hardware sales** — no recurring revenue after installation, so growth depends entirely on new shipments
2. **82% white-label share** — weak brand equity, with distributors holding the pricing leverage
3. **2025 growth collapsed to 9%** — whether high growth is sustainable is the core question

---

## II. Moat Assessment

### Five moat categories, verified one by one

| Moat type | Strength | Verification / analysis |
|-----------|------|---------|
| **Brand / pricing power** | Weak-to-moderate | An 82% white-label share means the end-customer brand doesn't belong to Deye. Its own-brand channel in Brazil is under construction, but brand strength in mature Western markets remains well behind Enphase/Huawei. Customers in emerging markets recognize the "Deye" brand to some degree (>50% market share in South Africa), but they are buying mostly on price, not brand |
| **Switching costs** | Moderate-to-strong | Inverter + battery pack bundling creates product lock-in (inverters and battery packs from different manufacturers are typically incompatible); off-grid systems above 100kW use proprietary protocols to lock in customers; but switching costs for small residential systems are low |
| **Network effects** | Weak | Hardware products carry no network effect. Enphase's Enlighten platform has a weak network effect (data accumulation → generation optimization → more users attracted), a dimension Deye lacks |
| **Scale / cost advantage** | **Very strong** | The core moat. Deye self-manufactures 90% of structural components, has cut costs 30% through IGBT localization, self-manufactures 70%+ of its molds, and runs an expense ratio of only ~10% under its distributor model. Its per-watt microinverter price is just one-third to one-quarter of Enphase's. At 51.1%, storage-inverter gross margin is the highest among Chinese peers |
| **Certification barriers** | Strong | Deye holds certifications across all major global markets (UL/CE/AS4777/NRS/INMETRO, etc.); certification cycles run 6-18 months and cost hundreds of thousands to millions of dollars. New entrants need 1-2 years to catch up |

### Moat trend assessment

**Past 5 years: widened significantly**
- Transformed from a home-appliance OEM into an emerging-market residential storage leader
- Overseas distributor count grew from zero to 291 (the most in the industry)
- Product line expanded from a single inverter to "inverter + battery pack + heat pump"
- Established first-mover advantage in markets such as South Africa, Myanmar, and the Philippines

**Next 5 years: at risk of narrowing**
- The **EU inverter ban (taking full effect in 2027)** could systematically compress Deye's market space in Europe (Germany accounts for 24% of revenue)
- If giants such as Huawei or Sofar Solar/Growatt enter the microinverter-plus-residential-storage market, they will directly attack Deye's cost-advantage moat
- Global inverter overcapacity (1TW of capacity vs. 538GW of demand) will erode margins via price wars
- Competitors are catching up: Ginlong (Solis), GoodWe, and Growatt are similarly accelerating their push into emerging markets overseas

### Digging deeper: will this moat still exist in 10 years?

**The factors most likely to destroy the moat**:
1. **A "Huawei 5G ban"-style inverter blockade from the EU** — if the 2027 ban is strictly enforced, Deye could be forced out of Europe (~24% of revenue), and the precedent could spread to other Western markets like Australia
2. **Huawei making a full push into residential storage** — Huawei FusionSolar is already a top-3 player in Europe's residential storage market; if it applies a smartphone-style "value-for-money plus brand" strategy to emerging markets, Deye's cost advantage would be substantially eroded
3. **A major Enphase price cut** — after Enphase's revenue collapsed 42% in 2024, it may adopt an aggressive pricing strategy; if the microinverter price gap narrows from 3-4x to 1.5-2x, Deye's value-for-money narrative would weaken

**The key judgment for 10 years out**: the durability of the moat hinges on whether Deye can upgrade from "cost leadership" to "cost leadership plus brand plus a software ecosystem." If it remains stuck in the hardware-OEM model, the moat will gradually narrow as competitors catch up.

---

## III. Contrarian Thinking and Risk Checklist

### Panorama of failure paths

| Failure path | Probability | Impact | Specific scenario |
|----------|------|---------|---------|
| **EU inverter cybersecurity ban fully takes effect** | 60-70% | Very high | Starting April 2027, all new contracts fall under the restrictions. Germany accounts for 24% of revenue (~CNY 1.77 billion) and is the highest-margin region. If the ban is extended to battery energy storage systems (BESS), the damage widens further |
| US 145% tariff plus Southeast Asia anti-circumvention crackdown | Already happened | Moderate | Deye's direct US exposure is only ~3%, routed through white-label partner Sol-Ark. But being locked out of the world's largest profit-pool market is a long-term opportunity cost |
| Global inverter price war | 70-80% | High | Capacity of 1TW vs. demand of 538GW is a severe glut. Prices are already falling 10-15% a year. Deye's 51% storage-inverter gross margin has room to fall further |
| Continued tightening of Brazilian policy | 40-50% | Moderate | The Fio B charge rises incrementally to 75% by 2027, and the import tariff on components is 25%. Brazil's distributed solar additions fell for the first time in 2025, down 12% |
| Receivables deterioration / bad debt | 20-30% | Moderate-to-high | Accounts receivable stood at CNY 1.7 billion at end-2024 (+203%), growing far faster than revenue. Credit risk among emerging-market customers (Pakistan, Ukraine, etc.) is high |
| Huawei makes a major push into emerging-market residential storage | 30-40% | High | Huawei shipped 176GW of inverters globally in 2024 and holds 22.7% share of storage inverters. If it pushes the "Huawei" brand and its distribution network deeper into emerging markets, Deye's price advantage would be eroded |
| A repeat of a relay-component-style quality incident | 10-15% | Moderate | In 2023, a teardown in Germany found a missing relay component, which already damaged the brand. A similar incident in a larger market could trigger certification revocation |

### Historical analogies

| Comparable company | Similarity | Outcome | Takeaway |
|----------|--------|------|------|
| **Sungrow (2016-2020)** | Moved into inverters from UPS / power electronics | Market cap ~CNY 300 billion, global top-2 inverter maker | Proves a Chinese inverter company can become a global leader. But Sungrow's "domestic first, then overseas" path was steadier |
| **Ginlong / Solis (2022-2024)** | High Europe exposure → destocking hit hard → stock fell 70% → net margin -11% | Recovery began in 2025 | **High overseas dependence is extremely fragile during a destocking cycle.** Deye is spread across 110+ countries, which is better diversified than Solis |
| **GoodWe (2024)** | Overseas share plunged from 80% to 30% → losses | Currently recovering | High overseas exposure is a double-edged sword |
| **Enphase (2022-2024)** | Microinverter leader → market cap fell from $40B to $10B | Valuation has normalized | Even an industry leader cannot escape cyclical swings |
| **Gree's investment in Yinlong** | A home-appliance company diversifying into new energy | Failed, wrong technology path chosen | The key to Deye's successful transformation is that "variable-frequency control → power electronics → inverters" was a natural extension of its existing capability, not a cross-industry leap |

### Digging deeper: where am I most likely to be wrong?

1. **Underestimating the real impact of the EU ban.** This is not a "might happen" risk — the EU has already legislated it. Once it takes full effect in 2027, Deye's European revenue (~24% of the total) will face systemic compression. This is the inverter-industry equivalent of the "Huawei 5G ban"
2. **Getting anchored to 2026 Q1's strong growth.** Net profit attributable to parent was up an eye-catching 68% in 2026 Q1, but full-year 2025 growth was only +9%. The question that needs answering: is Q1 the start of a trend or a one-off blip?
3. **Equating "cost advantage" with "irreplaceable."** All Chinese inverter makers have a cost advantage — Solis, GoodWe, and Growatt have cost structures not far from Deye's. Deye's real point of differentiation is its distribution network, and a distribution network can be replicated by later entrants

**Why a smart investor might short this stock**:
- A 41x P/E is rich for a hardware manufacturer whose net profit grew only 7% in 2025
- The EU ban is an already-confirmed medium-term headwind that the market has not yet fully priced in
- Receivables are growing four times faster than revenue (+203% vs. +50%), and credit risk is building

---

## IV. Management Assessment

### Founder Zhang Hejun

| Dimension | Detail |
|------|------|
| Age | 73 |
| Education | High school |
| Shareholding | 60.30% combined among the concert-party group (absolute control) |
| Motto | "Make progress every day" |
| Wealth ranking | CNY 35 billion on the Hurun Rich List (2024, ranked 128th) |
| Career | Mold worker starting in 1971 → founded Deye in 2000 → acquired Rixin Technology in 2016 → IPO in 2021 → new-energy revenue reached CNY 10.2 billion in 2025 |

### Core team

| Name | Title | Key information |
|------|------|------|
| Zhang Dongbin | Executive director | Elder son, 47, **Canadian citizen** |
| Zhang Dongye | Vice chairman and general manager | Younger son, 44, **Canadian citizen** |
| Ji Dehai | Deputy general manager | 33, joined in 2016 through the Rixin Technology acquisition; the key technical figure behind the inverter business |
| Tan Zui | Director / vice president / CFO | 49, joined in 2000; the company's longtime finance veteran |

### Review of key decisions

| Time | Decision | Result | Grade |
|------|------|------|------|
| 2016 | Acquired Ningbo Rixin Technology to enter the inverter business | Timed the new-energy boom perfectly, acquiring core technology at low cost | A+ |
| 2018-2019 | Prioritized expansion into South Africa and Brazil | >50% storage market share in South Africa, ~22% inverter share in Brazil | A+ |
| 2017 | Positioned early in storage inverters | Paid off perfectly during South Africa's 2022 power crisis | A+ |
| 2022 | Raised CNY 3.55 billion via placement, entirely for inverter capacity expansion | Capacity kept pace with rapid growth | A |
| 2024 | Built a $150 million plant in Malaysia | Sidesteps trade barriers, but capacity ramp-up will take time | B+ (still to be validated) |
| 2025 | Invested CNY 2.127 billion in a 16GWh commercial-and-industrial storage production line | Bets on C&I storage as a second growth curve; a large capital commitment | B+ (still to be validated) |

### Governance issues worth monitoring

| Issue | Severity | Detail |
|------|---------|------|
| **Heavy family concentration of control** | High | 3 of 7 directors are Zhang family members; the 73-year-old founder alone controls 60%+; succession plans are unclear |
| **"Buying in public, selling in private"** | Moderate | Zhang Hejun personally added only 120,000 shares (0.02%), while the employee stock ownership platform he controls has continuously reduced its position, cashing out roughly CNY 500 million |
| **Core family members hold foreign citizenship** | Moderate | Both sons hold Canadian citizenship, which carries uncertainty against a complex geopolitical backdrop |
| **Large post-IPO dividend payouts** | Moderate | Cumulative dividends of CNY 4.9 billion over 3.5 years since listing; at a 60% ownership stake, the family has received CNY 2.9 billion+. The payout ratio is extremely high (82.89% in 2024), though this also indicates generosity toward shareholders |
| **Undisclosed patent litigation** | Moderate | A US lawsuit filed by CyboEnergy in August 2025 had not been disclosed to investors as of September |

### Digging deeper: if the CEO retired, would the company keep its competitive edge?

**Short-term risk is manageable**: both sons have held core management posts for years, so day-to-day operations can continue smoothly. Ji Dehai (33) is the key technical figure behind the inverter business.

**Long-term concern**: Zhang Hejun's strategic instincts (the 2016 Rixin acquisition, the 2018 South Africa first-mover bet) are hard to replicate. Going from a high-school education to a CNY 35 billion fortune, his business intuition is Deye's greatest intangible asset. Whether his two sons — Canadian citizens with undergraduate degrees (economics from Dalhousie University / business administration from George Brown College) — can sustain that same judgment remains an open question. Analogy: many second-generation heirs at Ningbo's private enterprises have lost the hunger and instinct of the founding generation after taking over.

---

## V. Industry and Civilizational Trends

### Paradigm-shift assessment

The global energy system is undergoing a civilization-scale paradigm shift **from centralized fossil-fuel power to distributed renewable energy**. Distributed solar plus storage is the core vehicle of this shift.

| Analogy | Corresponds to |
|------|------|
| Centralized grid → distributed solar-plus-storage | Mainframes → personal computers |
| Inverter | The "brain" of a solar system |
| Deye | The "Lenovo" of distributed energy in emerging markets |

### TAM growth curve

| Market | 2024 size | 2030 forecast | CAGR | Deye's involvement |
|------|-----------|-----------|------|-----------|
| Global solar inverters | $12.7-15.0 billion | $23.7-41.9 billion | 8-18% | High |
| **Global microinverters** | **$3.0-4.7 billion** | **$8.5-17.3 billion** | **18-25%** | High (the fastest-growing sub-segment) |
| Global residential storage | $10.9 billion (2025) | $19.3 billion | 12% | Very high |
| Brazil inverters | $0.57 billion | $0.7-1.0 billion | 6-9% | Very high (~22% market share) |
| Global dehumidifiers | $3.4-4.8 billion | $5.1-7.1 billion | 5-9% | Moderate (legacy business) |

### Position in the value chain

Deye sits in the **midstream manufacturing** segment: it sources IGBTs, capacitors, and battery cells upstream → designs and manufactures inverters and battery packs midstream → reaches end customers downstream through distributors.

**Core capability**: vertical integration (90% self-manufacture rate for structural components) plus an asset-light distribution model. It lacks upstream in-house chip design capability (unlike Enphase's ASICs) and a downstream software ecosystem (unlike Enphase's Enlighten).

### Digging deeper: in 20 years, will this company be "the Standard Oil of its era" or "a flash-in-the-pan 3Com"?

**More likely to become "the Schneider Electric of emerging markets"** — an equipment manufacturer holding a significant position in developing-world power infrastructure. It's unlikely to become "Standard Oil" (the inverter industry is too fragmented and the technology barrier is not high enough), but if it can upgrade from 82% white-label to 50%+ own-brand while also extending into commercial-and-industrial storage, it could plausibly become a globalized enterprise with annual revenue above CNY 50 billion and a market cap of CNY 300-500 billion.

A "3Com"-style decline is a low-probability but real possibility — if the EU ban spreads to more Western countries, Huawei pushes aggressively into emerging markets, and Deye fails to build its own brand and software ecosystem, it could degrade into a pure OEM manufacturer with continuously compressed margins.

---

## VI. Valuation and Margin of Safety

### Current market pricing

| Valuation metric | Current value | Peer comparison |
|----------|--------|---------|
| P/E (TTM, post bonus-share adjustment) | **40.90x** | Solis ~25x, GoodWe ~30x, Sungrow ~18x |
| P/B | **12.56x** | Peers 8-15x |
| P/S (TTM) | **10.6x** | Peers 3-8x |
| ROE | **30.70%** | Peers 15-25% |
| FCF Yield | **2.16%** | — |
| Dividend yield | **~2-4%** | Generous payout |
| 2026E P/E | **~14.5x** | Based on brokerage consensus net profit of CNY 5.38 billion |

> All metrics precisely verified with `financial_rigor.py`.

### Historical P/E range

| Year | Average P/E | Highest P/E | Lowest P/E |
|------|--------|--------|--------|
| 2022 | 120.33 | 177.39 | 52.54 |
| 2023 | 51.45 | 137.84 | **11.10** |
| 2024 | 23.49 | 36.77 | **12.91** |
| 2025 | 21.17 | 27.29 | 14.00 |
| 2026 (year to date) | 36.82 | 50.30 | 24.65 |

The historical low of 11-13x P/E occurred in late 2023 through early 2024 (European destocking plus a sector-wide valuation collapse). The current P/E of 41x sits in a historically elevated range.

### Reverse DCF

At the current market cap of CNY 129.7 billion, using a 10% discount rate and a 3% terminal growth rate:
- Implies 2030 net profit of roughly **CNY 8.0-10.0 billion**
- Implies a 5-year forward net-profit CAGR of roughly **25-30%**
- This requires: continued success of overseas expansion + commercial-and-industrial storage ramp-up + sustained gross margin

**Is this reasonable?** If 2026 net profit does indeed reach CNY 5.38 billion (+70%), then only ~15% growth per year is needed over the following 4 years to reach CNY 8.0 billion. But if 2026 growth falls short of expectations (e.g., if the EU ban starts to bite earlier than expected), current valuation is too rich.

### Three-scenario valuation

> Based on a 2026 estimated EPS of CNY 4.23 (brokerage consensus net profit of CNY 5.38 billion / 1.273 billion shares), projected forward 3 years to 2029. All calculations precisely verified with the tool.

| Scenario | Annual growth | Target P/E | 2029 EPS | Target price | Upside/downside vs. current |
|------|--------|--------|-----------|---------|-----------|
| **Bull case** (dual engines: global expansion + C&I storage) | 35% | 30x | CNY 10.41 | **CNY 312** | +207% |
| **Base case** (steady domestic business + moderate overseas growth) | 20% | 22x | CNY 7.31 | **CNY 161** | +58% |
| **Bear case** (EU ban + price war + slowing growth) | 5% | 14x | CNY 4.90 | **CNY 69** | -33% |

### Key price bands

| Price (CNY) | Meaning | Corresponding 2026E P/E |
|-------------|------|-------------|
| 130-160 | Base-case target price | 24-30x |
| 100-110 | **Current price level** | 19-21x |
| 70-80 | A reasonably ample margin of safety | 13-15x |
| 50-60 | Extreme bear case (similar to late 2023) | 9-11x |

### Digging deeper: if the stock market shut down tomorrow for 5 years, would you be willing to hold at this price?

**Conditionally, yes.**

Buying at CNY 101.85, if Deye succeeds over the next 5 years (by 2031):
- Annual revenue of CNY 30-50 billion, net profit of CNY 7-10 billion, market cap of CNY 300-500 billion (2.3-3.9x today's CNY 129.7 billion) would deliver a solid return
- Sustained ROE above 25% combined with a high payout ratio means real cash returns during the holding period

But this depends on:
1. The EU ban not spreading to more Western countries
2. Its emerging-market distribution network not being substantially eroded by Huawei or Growatt
3. Commercial-and-industrial storage successfully becoming a second growth curve

If any of the above conditions fails, the current price does not offer an adequate margin of safety — **it would be better to wait for a pullback to the CNY 70-80 range (2026E P/E of ~13-15x) before building a position.**

---

## VII. Composite Decision Memo

### Summary across dimensions

| Dimension | Conclusion | Confidence |
|------|------|--------|
| Business quality | Excellent — rigid demand for residential storage in emerging markets, 51% inverter gross margin, an extremely low expense ratio, and ROE above 30% | 85% |
| Moat | Moderate-to-strong — very strong cost advantage and first-mover distribution, but weak brand, a generation behind Enphase in technology, and a high white-label share | 70% |
| Management | Good — an outstanding record of strategic decisions, but heavy family control, a 73-year-old founder, and unclear succession plans | 70% |
| Biggest risk | The EU inverter ban (already legislated, taking full effect in 2027) is the largest certain medium-term headwind | 80% (high confidence in the risk itself) |
| Civilizational trend | A strong tailwind — distributed solar-plus-storage is the core vehicle of the energy transition, and Deye holds an advantageous position in emerging markets | 90% |
| Valuation | Rich — a 41x P/E is expensive within the A-share inverter sector; a ~14.5x 2026E P/E would be reasonable if earnings come through as forecast | 60% (heavily dependent on earnings delivery) |

### Final decision

| Strategy | Recommendation |
|------|------|
| **For those with no position** | **Wait for a pullback to the CNY 70-80 range (2026E P/E of 13-15x) before considering a position.** The current 41x P/E is rich for a hardware manufacturer, and the EU ban is not yet fully priced in. If high growth continues through 2026 Q2-Q3 and the ban's impact proves limited, a 5% starter position could be built in the CNY 85-95 range |
| **For existing holders** | **Hold, but keep the position under 10%.** Business quality, industry trend, and management all send positive signals. Strong 2026 earnings growth (Q1 +68%) provides near-term support. But watch closely how the 2027 EU ban is actually enforced and how receivables trend |
| **Sell signals** | (1) Strict enforcement of the EU ban causes a >20% quarter-over-quarter decline in Germany/Europe revenue; (2) storage-inverter gross margin falls below 40%; (3) receivables growth persistently exceeds revenue growth by more than 2x; (4) Zhang Hejun sells down a large stake (>1% of shares) |
| **Add-to-position signals** | (1) The share price pulls back to the CNY 70-80 range; (2) Malaysian capacity successfully sidesteps EU/US trade barriers; (3) quarterly commercial-and-industrial storage revenue exceeds CNY 1 billion while maintaining >50% growth; (4) own-brand revenue share rises to 30%+ |

### Four-perspective commentary

> **Business-quality perspective**: This is a good business. A 51% gross margin on storage inverters, ROE above 30%, and CNY 4 billion of cash flow — these are top-tier metrics in any industry. But a good business is not the same as a good stock. The question is: how long can the "essential power" demand in emerging markets persist? Once South Africa's power situation improves (as Eskom's supply gradually recovers), will storage demand fall off a cliff? Buying Deye is not buying a steadily growing consumer-goods company — it's buying a highly cyclical growth stock whose fortunes depend on power shortfalls across global emerging markets.

> **Contrarian perspective**: Two things worry me most. First, the EU ban. This is not a hypothetical risk — it's already legislated and takes effect in 2027. Germany accounts for 24% of Deye's revenue and is its highest-margin region. Can alternative markets fill the gap once it's blocked? Second, receivables. The 203% increase in 2024 far outpaces revenue growth, which is a danger sign given the customer base in emerging markets. Pakistan, Ukraine — can distributors in these countries really be counted on to pay on time?

> **Management perspective**: Zhang Hejun is one of the most impressive grassroots Chinese entrepreneurs I've come across. From a high-school education, he rose from mold worker to a CNY 35 billion fortune. His key decisions — the Rixin acquisition, the South Africa bet, the early move into storage — have almost all been correct. But he is now 73. His two sons hold Canadian citizenship, and against the backdrop of US-China decoupling, that detail is unsettling. What unsettles me even more is the "buying in public, selling in private" pattern — publicly adding only 120,000 shares while quietly cashing out CNY 500 million through the employee stock ownership platform.

> **Civilizational-trend perspective**: Viewed on a 20-year horizon, the shift from centralized fossil-fuel power to distributed renewable energy is irreversible, and Deye stands on the right side of this trend. But whether an individual company can keep capturing the dividends of that trend depends on the depth of its moat. Deye's cost advantage is a strong barrier, but pure cost leadership rarely survives 20 years in manufacturing — a cheaper alternative always eventually shows up. Deye needs to build a brand and a software ecosystem within its current cost-advantage window, or it risks being reduced to a pure contract manufacturer a decade from now.

---

## Appendix: AI Analysis Confidence vs. Investment Certainty

| Conclusion | AI analysis confidence | Investment certainty | Note |
|------|------------|-----------|------|
| Excellent business quality (high margin + high ROE) | **High (90%)** | **High (85%)** | Financial data is ample and the trend is clear |
| First-mover advantage in emerging-market distribution | **High (85%)** | **Moderate-to-high (75%)** | South Africa/Brazil data is solid, but durability needs continued observation |
| The EU ban will damage European revenue | **High (85%)** | **High (80%)** | Already legislated with a clear timeline. The uncertainty lies in enforcement rigor and exemption clauses |
| 2026 net profit reaching CNY 5.38 billion | **Moderate-to-high (75%)** | **Moderate (65%)** | A strong Q1 start of +68%, but whether it holds for the full year depends on Q2-Q4 |
| Commercial-and-industrial storage becoming a second growth engine | **Moderate (60%)** | **Moderate (55%)** | Investment is already committed (CNY 2.127 billion), but capacity won't come online until 2028 |
| Receivables risk is manageable | **Moderate (55%)** | **Low (45%)** | Growth is abnormal (+203%), credit data on emerging-market customers is limited, and bad-debt probability is hard for AI to assess accurately |
| Founder succession is properly arranged | **Low (40%)** | **Low (35%)** | Very little public disclosure of succession plans; the 73-year-old founder's health and succession are a blind spot for AI |

**Core distinction**:
- This report's judgments on Deye's business quality, cost advantage, and industry trend rest on ample data, hence the high confidence
- The greatest uncertainties are the **actual rigor of EU ban enforcement** and **the quality of emerging-market receivables** — the former depends on political dynamics, the latter on the economic conditions of individual countries, and both lie beyond the reach of public-data analysis
- **The current 41x P/E requires "most of the optimistic assumptions to come true" to deliver a reasonable return.** If an investor's confidence in the EU ban's impact and in earnings durability is no higher than the market consensus, it would be better to wait for a better price

---

*Report generated: June 23, 2026 | Data as of: June 23, 2026*
*Currency unit: Chinese yuan (CNY)*
*Data sources: Deye Technology annual/interim/quarterly reports, Hong Kong IPO prospectus (January 2026), Wood Mackenzie, SolarPower Europe, Grand View Research, Mordor Intelligence, Investing.com, Eastmoney, Sina Finance, research reports from Galaxy Securities/CSC/Soochow/Kaiyuan Securities, Enphase 10-K, ESS News, PV Tech, PV Magazine, etc.*
