# Supply-Chain Bottleneck Hunter: AI-Driven Bottleneck Arbitrage Across the Global Value Chain

Run a supply-chain bottleneck scan and opportunity hunt across the $ARGUMENTS super-trend.

## Core Idea

Don't ask "what stock does AI recommend"; ask "if this trend keeps expanding, which link runs short first?"

Traditional research fixates on market leaders and well-known verticals. This system flips it around: **start from the chokepoints of the physical supply chain, and find the companies nobody is watching — the ones whose stockout would force the entire industry to stop and wait.**

Source of excess return: the first-layer bottlenecks (GPUs, HBM, power) are already fully priced. The real alpha sits in the **second and third layers** — optical modules, lasers, InP substrates, SOI wafers, epitaxy equipment, wafer-level test, IC substrates, specialty glass fiber cloth, and so on.

---

## Step 1: Confirm the Super-Trend

### 1.1 Trend screening criteria

Don't chase hallucinations inside minor fads. Only pursue super-trends that meet ALL of the conditions below:

| Criterion | Requirement | Verification method |
|------|------|---------|
| Durability | At least 3-5 years of certain growth | Search industry forecasts and capex plans |
| Physicality | Requires actual hardware/materials/equipment build-out | Distinguish "software upgrade" from "physical expansion" |
| Scale | Global capex > $50B/year | Search leading players' capex guidance |
| Acceleration | Demand growth > supply-expansion pace | Compare demand growth rate vs. capacity-expansion plans |

### 1.2 Current list of tracked super-trends

Update on each run. Initial list:

1. **AI infrastructure build-out** — data centers, GPU clusters, network interconnect, power
2. **Energy transition** — nuclear restart, grid upgrades, energy storage
3. **Defense modernization** — Western defense-spending upcycle, supply-chain reshaping
4. **Semiconductor reindustrialization** — US/EU/Japan subsidized fabs, equipment/materials bottlenecks
5. **Space economy** — satellite internet, surging launch cadence

If the user specifies a concrete trend (e.g. "AI infrastructure"), focus only on that trend.

### 1.3 Trend-verification output

```
Trend name:
Core driver: (one sentence)
Verification events already observed (at least 3):
  1. [date] [event] [source]
  2.
  3.
Capex scale: ~$XX B/year globally, growth YY%
Supply-demand gap assessment: demand growth > supply-expansion pace? Yes/No/Uncertain
Trend confirmation: ✅ Trackable / ❌ Insufficient evidence, not tracked for now
```

---

## Step 2: Physical Decomposition of the Supply Chain

### 2.1 Layered-decomposition framework

**Don't stop at the concept layer — decompose down to physical entities.**

```
Layer 0 (endpoint): final product/service
    │
Layer 1 (core components): core hardware already fully in market focus
    │                 ⬆ Fully priced, limited alpha
    │─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
    │                 ⬇ Low attention, alpha concentration zone
    │
Layer 2 (sub-components/materials): parts and materials supporting the core components
    │
Layer 3 (upstream equipment/raw materials): equipment and raw materials needed to make the sub-components
    │
Layer 4 (infrastructure): power, cooling, land, talent, certification
```

### 2.2 Decomposition template, using AI infrastructure as an example

```
Layer 0: AI model training/inference services
Layer 1: GPUs/accelerators, HBM memory, servers, data centers
Layer 2 (priority scan zone):
  ├─ Network interconnect: optical modules, optical fiber, switch chips, copper cables
  ├─ Optical-comms core: lasers (EML/VCSEL/CW), modulators, photodetectors
  ├─ Semiconductor materials: InP substrates, GaAs substrates, SOI wafers, SiC substrates
  ├─ Advanced packaging: CoWoS substrates, HBM TSV, ABF substrate film
  ├─ PCB/substrates: high-frequency high-speed PCB, IC substrates, specialty glass fiber cloth
  ├─ Test: wafer-level test (probe card), burn-in test, ATE
  ├─ Thermal/cooling: liquid-cooling systems, CDU, immersion coolant
  └─ Power connection: busway, UPS, distribution cabinets, transformers
Layer 3:
  ├─ Epitaxy equipment: MOCVD, MBE
  ├─ Litho/etch: specialty-wavelength lithography, InP etch
  ├─ Raw materials: high-purity metals (indium, gallium, germanium), specialty gases, sputtering targets
  └─ Certification/standards: MSA standards, Telcordia certification
Layer 4:
  ├─ Power: nuclear, natural-gas generation, transmission and transformation
  ├─ Cooling water / thermal infrastructure
  └─ Data-center land/permits
```

### 2.3 Decomposition of other trends

Run a similar decomposition for each confirmed super-trend. Use WebSearch to search:
- "{trend} supply chain bottleneck 2026"
- "{trend} shortage critical component"
- "{trend} capacity constraint"
- "{trend} sole source supplier"

---

## Step 3: Bottleneck Identification — Finding the "Chokepoint"

### 3.1 Six criteria for judging a bottleneck

For each link in Layer 2-3, evaluate criterion by criterion:

| # | Criterion | Question | Score |
|---|------|------|------|
| 1 | **Supply concentration** | Global suppliers ≤ 3? | 🔴 ≤2 / 🟡 3-5 / 🟢 >5 |
| 2 | **Expansion lead time** | How long to add new capacity? | 🔴 >2 yr / 🟡 1-2 yr / 🟢 <1 yr |
| 3 | **Substitution difficulty** | Can other tech/materials substitute? | 🔴 Irreplaceable / 🟡 Partly replaceable / 🟢 Easily replaced |
| 4 | **Capacity utilization** | Current capacity utilization? | 🔴 >90% / 🟡 70-90% / 🟢 <70% |
| 5 | **Demand growth** | Downstream demand growth? | 🔴 >50%/yr / 🟡 20-50% / 🟢 <20% |
| 6 | **Customer qualification cycle** | How long for a new supplier to qualify? | 🔴 >1 yr / 🟡 6-12 mo / 🟢 <6 mo |

**Bottleneck rating:**
- 🔴🔴🔴 ≥4 → **S-tier bottleneck** (single-point-of-failure level, top priority)
- 🔴🔴 3 → **A-tier bottleneck** (severely constrained)
- 🔴 1-2 → **B-tier bottleneck** (under pressure but manageable)
- No 🔴 → not a bottleneck, skip

### 3.2 Bottleneck-map output

```
Supply-Chain Bottleneck Map — {trend name}
Update date: YYYY-MM-DD

S-tier bottlenecks (single point of failure):
  1. [link name] — [one-sentence reason] — suppliers: [company list]
  2.

A-tier bottlenecks (severely constrained):
  1.
  2.

B-tier bottlenecks (under pressure):
  1.
  2.

Recent changes (vs. last scan):
  - [added/upgraded/downgraded/resolved] [link name] — [reason]
```

---

## Step 4: Company Screening — From Bottleneck to Target

### 4.1 For each S-tier and A-tier bottleneck, identify all relevant listed companies

Search methods:
- WebSearch "{bottleneck link} supplier listed company"
- WebSearch "{bottleneck link} manufacturer stock"
- WebSearch "{bottleneck product} market share company"

### 4.2 Initial screen (quick filter)

| Criterion | Requirement | Rationale |
|------|------|------|
| Listing status | Already listed (A-share/HK/US/Japan/Taiwan/Europe) | Tradable |
| Bottleneck-business share | >30% of revenue from the bottleneck link | Purity |
| Market cap | Prefer < $10B | Large caps are already fully priced |
| Liquidity | Average daily turnover > $1M | Can enter/exit |

### 4.2.1 Valuation check (mandatory, cannot be skipped)

**A real bottleneck ≠ an investment opportunity.** You must compute PS and PE for each company and note them in the report. Use the combined conditions below to judge whether the valuation is overextended:

#### Valuation red light (meet any one → signal strength capped at ★★, flag "⚠️ valuation overextended")

1. **Market cap > 20% of TAM**: the company's market cap already exceeds 20% of its addressable market, meaning growth expectations are over-internalized
2. **PS > 30x and revenue growth < 100%**: high valuation but growth too weak to support it. Companies growing >100% are exempt from the PS red line but must still be flagged "⚠️ high valuation requires sustained high growth to be validated"
3. **Market cap > 10x the optimistic 5-year revenue forecast**: even if the most optimistic assumptions fully materialize, the current pricing is still too high
4. **Stock doubles within 60 days of a secondary offering**: clear sentiment-driven signature, drop signal strength one tier

#### Valuation yellow light (needs extra explanation, otherwise downgrade)

1. **Loss-making + PS > 15x**: may enter ★★★ but must lay out the path to profitability and a timeline
2. **PS more than 5x that of profitable peers**: must explain the source of the premium (market share, growth-rate gap, moat difference)
3. **PE > 80x**: compute PEG and explain whether growth supports it

#### Valuation green light (bonus)

- PS < 10x and revenue growing → signal strength may gain one tier
- PE < 30x with a moat → flag "valuation has a margin of safety"

#### Valuation-reasonableness test (mandatory)

For each target, answer: "If I buy at the current market cap, assume the most optimistic scenario fully materializes, and exit at 25x PE in 10 years, what is the annualized return?" Annualized return < 10% → flag "current price offers no margin of safety."

**Note**: the purpose of the valuation check is to prevent obvious errors like recommending "a loss-making company at 100x PS," not to exclude every high-valuation early-stage company. The key is whether growth, TAM, and competitive landscape can support the current valuation — this needs case-by-case analysis, not a blanket rule.

### 4.3 Deep-screening dimensions

For companies that pass the initial screen, evaluate each one:

```
## {Company name} ({ticker})

**Bottleneck positioning:**
- Specific position in the supply chain
- Market share: #X globally, XX% share
- Customer list (known)

**Capacity and expansion:**
- Current capacity / utilization
- Expansion plan / timeline
- Funding needed for expansion vs. existing cash

**Financial snapshot:**
- Market cap / revenue / profit / growth
- Bottleneck-business revenue share
- Gross-margin trend (the tighter the bottleneck, the more gross margin should rise)

**Risk checklist:**
- [ ] Substitute-technology risk: can it be bypassed?
- [ ] Dilution risk: large secondary offerings / convertibles?
- [ ] Geopolitical risk: located in a sensitive region / subject to export controls?
- [ ] Management risk: any track record of misconduct?
- [ ] Customer-concentration risk: overly dependent on a single customer?
- [ ] Valuation overextension: does the current valuation already price in 3 years of growth?

**Bottleneck-durability judgment:**
- When will this bottleneck be resolved?
- After it resolves, what does this company still have?
- Is it one-off or persistent?
```

---

## Step 5: Cross-Verification — Don't Just Listen to One Story

### 5.1 Positive verification

| Verification item | Question | Search method |
|--------|------|---------|
| Customer verification | Have top customers signed / designed it in? | Search company announcements, mentions in customer earnings |
| Revenue verification | Is the bottleneck already showing up in revenue growth? | Search the last 2-3 quarters of earnings |
| Price verification | Are prices rising? | Search industry quotes, analyst reports |
| Capacity verification | Is capacity really tight? | Search lead-time data, customer complaints |
| Capital verification | Is there expansion capex? | Search company capex guidance |

### 5.2 Reverse verification (Munger-style inversion)

| Reverse question | Meaning |
|---------|------|
| Why don't smart people buy this stock? | Find the known bearish thesis |
| Can this bottleneck be bypassed? Any substitute route? | Technology-roadmap risk |
| Can China / other players replicate the capacity quickly? | Supply-shock risk |
| If end demand slows 50%, what happens to this company? | Downside sensitivity |
| Has management diluted with offerings at the highs before? | Management trust |
| What growth assumptions are embedded in the current valuation? | Valuation reasonableness |

### 5.3 Signal cross-verification

- Are multiple companies at the same bottleneck all rising? (industry verification)
- Are downstream customers mentioning tight supply in earnings? (customer verification)
- Do industry associations / research firms have relevant data? (third-party verification)

---

## Step 6: Output — The Bottleneck-Opportunity Board

### 6.1 Bottleneck-opportunity ranking table

| Rank | Company | Ticker | Market cap | Annual revenue | PS | PE | Bottleneck link | Bottleneck rating | Market share | Revenue growth | Signal strength | Valuation verdict |
|------|------|------|------|--------|-----|-----|---------|---------|---------|---------|---------|---------|
| 1 | | | | | x | x | | S/A | | | ★1-5 | Reasonable/High/Overextended |

**Mandatory fields**: market cap, annual revenue, PS, PE are required — do not skip with "to be verified." If financial data cannot be obtained, signal strength may not exceed ★★.

Signal-strength rating (the valuation-check result directly affects the rating):
- ★★★★★ Multiple cross-verifications, customer already designed in, revenue already showing, valuation green light (reasonable PS + profitable or near-profitable)
- ★★★★ Most verifications pass, valuation green or yellow light (with explanation attached)
- ★★★ Logic holds but partly unverified, valuation yellow light acceptable (e.g. high-growth early-stage company)
- ★★ Early signal, or bottleneck logic holds but valuation red light (market cap > 20% of TAM, PS > 30x with insufficient growth, market cap far above 5-year forecast, etc.)
- ★ Pure concept, unverified

### 6.2 One-page summary for each opportunity

```
🎯 {Company name} ({ticker}) — {one-sentence bottleneck positioning}

Why it's a bottleneck:
(2-3 sentences explaining why this link is a chokepoint)

Why this company:
(2-3 sentences explaining why this company and not another)

Catalyst timeline:
- Near term (1-3 mo): [specific events, e.g. earnings, capacity ramp, customer qualification]
- Mid term (3-12 mo): [industry trends, expansion milestones]

Key risks:
1.
2.

Key data: market cap $XX / annual revenue $XX / PS Xx / PE Xx / revenue growth XX% / bottleneck-business share XX%

Valuation margin-of-safety test: buy at current market cap, exit at 25x PE in 10 years — requires net profit to reach $XX, implying annual revenue of $XX (X times today's), annualized return XX%. Conclusion: has / lacks margin of safety.

Cross-verification status: ✅ customer verified / ✅ revenue verified / ✅ valuation reasonable / ⚠️ valuation overextended / ❌ unverified items

Conclusion: worth deep research / add to watchlist / not tracked for now
```

### 6.3 Action recommendations

| Target | Recommended action | Rationale |
|------|---------|------|
| A | Run `/investment-team` deep research | S-tier bottleneck + multiple verifications |
| B | Add to watchlist, wait for next quarter's earnings | Logic holds but revenue not yet showing |
| C | Not tracked for now | Substitute-technology risk too high |

---

## Step 7: Incremental Updates — Dynamic Maintenance of the Bottleneck Map

### 7.1 Incremental updates on each run

1. Check whether the identified bottlenecks still hold
   - Have new suppliers entered?
   - Has capacity expanded enough to resolve the bottleneck?
   - Any breakthrough in substitute technology?

2. Scan for newly emerging bottlenecks
   - Search supply chain / shortage / bottleneck news from the last 7 days
   - Check supply-chain-related disclosures during earnings season

3. Update bottleneck ratings (upgrade/downgrade/resolve)

### 7.2 State files

Maintain in the `reports/bottleneck-map/` directory:
- `master-map.md` — the master bottleneck map (continuously updated)
- `watchlist.md` — the watchlist (continuously updated)
- `YYYY-MM-DD/` — one folder per day, containing all scan reports for that day
- `deep-dive/` — a separate file per company for deep analysis

---

## Hourly Scan Mode (for scheduled tasks)

Run once per hour, using a "only publish a report when there's something worth it" mode:

### Scan flow (hourly)

1. **News scan**: search supply-chain-related news from the past 1-2 hours
   - Keywords: supply chain bottleneck, shortage, capacity constraint, allocation, lead time, sole source, bottleneck, stockout, capacity, price increase
   - Coverage: English + Chinese sources
2. **Market signals**: check price moves of tracked companies (pay special attention to abnormal moves >5%)
3. **Earnings/announcements**: check whether any bottleneck-related company has released earnings or a major announcement
4. **Valuation opportunities**: check whether any watchlist company has entered a buy zone due to a broad market selloff or similar
5. **Decide whether to publish a report:**
   - New bottleneck signal, clear target opportunity, or major status change → **publish a report**
   - No new findings → **no report**, just log "no new signals this round"

### Report-output rules

**One folder per day**: `reports/bottleneck-map/YYYY-MM-DD/`

**File-naming rule** (tell at a glance whether there's a target from the filename):

| Situation | Filename format | Example |
|------|-----------|------|
| Clear target found | `HH-MM-ticker1-ticker2.md` | `09-00-FORM-IBDN.md` |
| Bottleneck signal but no clear target | `HH-MM-signal-scan.md` | `14-00-signal-scan.md` |
| No new findings | No file generated | — |

**Tickers in the filename = companies that pass the valuation check and are worth deep research.** Companies that appear only in the signal-scan stage but fail the valuation check are not put in the filename.

### Report template (when there's a target)

```markdown
# Bottleneck Hunter — YYYY-MM-DD HH:MM

## Clear Targets

### {Company name} ({ticker}) — {one-sentence bottleneck positioning}

**Why it's worth attention now**: (the specific event/data change that triggered this attention)

**Bottleneck positioning**: Layer X, {link name}, bottleneck rating S/A/B
**Financial snapshot**: market cap $XX / annual revenue $XX / PS Xx / PE Xx / revenue growth XX%
**Valuation check**: red/yellow/green light (with specifics)
**Valuation margin of safety**: 10-year 25x-PE exit method, annualized return XX%

**Bull case** (2-3 points):
1.
2.

**Bear case** (2-3 points):
1.
2.

**Recommendation**: run deep research / add to watchlist / wait for a better price

---

## Other Signals (no clear target)

| Link | Signal | Source | Preliminary judgment |
|------|------|------|---------|

## Watchlist Status Changes

(upgrade/downgrade/added/removed; write "no change" if none)
```

### Report template (signal scan only)

```markdown
# Bottleneck Hunter Signal Scan — YYYY-MM-DD HH:MM

## New Signals

| Link | Signal description | Source | Investable target? | Next step |
|------|---------|------|----------------|-------|

## Watchlist Status

No change / Changed (list them)
```

---

## AI Research-Bias Awareness

| Bias | Manifestation | Countermeasure |
|------|-----|------|
| Leader preference | Search results dominated by large-cap companies | Deliberately search small-cap suppliers, add "small cap" keyword |
| English-language preference | Missing Japanese/Korean/Taiwanese companies | Must search suppliers in Japan/Korea/Taiwan markets |
| Narrative preference | Drawn in by the "AI concept" label | Look only at actual supply-chain position, not market labels |
| Confirmation bias | After finding a bottleneck, only look for supporting evidence | Force reverse verification (Step 5) |
| Recency bias | Relying on stale information | Prioritize data from the last 30 days |

---

## Core Principles (highest priority)

1. **Don't let AI recommend stocks — let AI decompose the supply chain** — the question matters more than the answer
2. **Physical first** — only focus on links that require actual physical products/materials/equipment
3. **Second and third layers** — don't chase the fully-priced leaders
4. **Cross-verify** — at least 2 independent sources for every conclusion
5. **Be honest about uncertainty** — if you can't find data, write "insufficient data"; don't fill it in with speculation
6. **Bottlenecks are time-limited** — every bottleneck gets resolved; the key is judging the time window
7. **Small cap ≠ good opportunity** — a small cap can also be a bad company; it must pass the financial-quality bar
8. **A real bottleneck ≠ an investment opportunity** — a company can sit on the tightest bottleneck, but if PS > 30x or it's still loss-making, the current price is not a buy point. **Valuation is a hard gate that cannot be overridden by bottleneck purity, signal strength, or narrative appeal.** Better to miss a bottleneck stock that already ran than to buy a loss-making company at 100x PS
9. **Follow the objectivity principles in CLAUDE.md** — don't presuppose a bullish view; data first, conclusion after

---

## Output Requirements

1. **Report location:**
   - Full scan: `reports/bottleneck-map/{trend}-bottleneck-{YYYYMMDD}.md`
   - Daily scan: `reports/bottleneck-map/daily/{YYYY-MM-DD}-{am/pm}.md`
   - Master bottleneck map: `reports/bottleneck-map/master-map.md`
   - Watchlist: `reports/bottleneck-map/watchlist.md`
2. **Language**: English
3. **Style**: direct, sharp, no filler
4. **Data**: cite the source for all data; label estimates as "estimate"
5. **No presupposed stance**: lay out data → derive logic → reach conclusion
6. **Both sides**: attach a counter-argument to every core judgment
