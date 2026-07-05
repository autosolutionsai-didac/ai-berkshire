# IonQ, Inc. (IONQ / NYSE / USD) — Financials & Valuation

**Analyst lens:** Warren Buffett (owner-earnings, cash generation, margin of safety)
**Run date:** 2026-07-05 · **Currency:** USD throughout
**Price anchor:** $49.12 (close 2026-07-02) · ~373.27M shares · market cap ≈ $18.34B (verified <1%)

> "Price is what you pay; value is what you get." — Buffett
> "The first rule is don't lose money. The second rule is don't forget the first." — Buffett

> **Screen context:** IonQ was **EXCLUDED** by the Phase-1 quality screen (fails ROE, cumulative FCF, net margin, dilution, earnings-quality). Forced test-continuation; no preset stance.

> **Valuation-method statement (mandatory):** IonQ has **deeply negative earnings and cash flow**, so **PE, PEG, and P/FCF are meaningless**. Per instruction, valuation is anchored on **EV/revenue and P/S vs. peers, plus explicit three-scenario analysis**. No earnings multiple is used.

---

## 1. Three-to-five-year financial trend (fact, sourced)

| USD | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Q1'26 |
|---|---|---|---|---|---|---|
| Revenue | 2.1M | 11.1M | 22.0M | 43.1M | **130.02M** (+202%) | **64.7M** (+755% YoY) |
| Gross margin | — | ~70%* | ~60%* | ~43%* | **40.4%** | **23.8%** ⬇ |
| Operating income | neg | neg | neg | neg | **−633.72M** | **−271.5M** |
| Net income (GAAP) | neg | neg | neg | neg | **−510.38M** | **+805.4M** ⚠️ artifact |
| Operating cash flow | neg | neg | neg | **−283.19M** | −151.0M |
| Free cash flow | neg | neg | neg | **−299.60M** | ~−160M `[est]` |

*Early-year gross margins reflect tiny denominators; not comparable. The clean trend is: **revenue compounding triple-digits, gross margin deteriorating as low-margin hardware dominates the mix, and operating losses widening in absolute dollars.***

**The GAAP "profit" trap (must-flag).** Q1'26 GAAP net income of **+$805.4M** is **not profit** — it is a **~$1.06B non-cash gain** from marking warrant liabilities to fair value. Those liabilities *fall when IonQ's stock falls*, so the "record profit" is a byproduct of the **share price declining** during the quarter. **Strip it out: IonQ lost ~$255M `[estimate]`.** Ignore GAAP net income and EPS for IonQ; the clean reads are **operating loss (−$271.5M)** and **adjusted EBITDA (−$96.8M, missed ~−$79.9M consensus)**.

---

## 2. Profitability, cash flow, and burn

- **Profitability:** None. ROE, ROA, net margin all deeply negative (FY2025 net margin ≈ −393%). Even FY2025's net loss (−$510M) is *smaller* than its operating loss (−$634M) because interest income + warrant marks flatter the headline — **the operating loss is the honest number**.
- **Gross-margin direction:** **Wrong way.** 40.4% (FY2025) → 23.8% (Q1'26) as system/hardware sales dominate. Scale is *hurting* margins, not helping — evidence against operating leverage so far.
- **Stock-based comp:** **$128.52M in Q1'26 = ~199% of revenue** (verified: 128.52/64.7 = 198.6%). SBC exceeds revenue and is the structural engine of dilution (shares ~193M at 2021 listing → ~373M now, ≈ +93%).
- **Burn:** Operating burn −$151M in Q1'26 (~doubled the 2025 quarterly pace); FY2026 adjusted-EBITDA guide **−$310M to −$330M** — management explicitly expects the loss to *widen in dollars*.

---

## 3. Balance sheet & runway

| Item | Value | Read |
|---|---|---|
| Cash + equivalents + investments | **~$3.1B** (Mar 31, 2026) | Raise-funded (~$3.35B equity issued FY2025), not earned |
| Debt | Minimal | Financed by equity, not leverage |
| FY2026 adj-EBITDA burn guide | −$310M to −$330M | ~$320M/yr midpoint |
| **Operating runway** | **~5 years** at current burn (~$604M annualized ÷ $3.1B ≈ 5.1×); ~4 years if burn accelerates | Liquidity is **not** the near-term risk |

**The real balance-sheet risk is not insolvency — it is dilution and M&A cash drain.** SBC ~$128M/quarter plus a **~79M-share warrant overhang** plus equity-funded deals (SkyWater $1.8B pending, ~43% cash) mean the share count keeps rising and cash can exit faster via acquisitions than via operations. **Bottom line: IonQ won't run out of cash soon; shareholders will keep getting diluted.**

---

## 4. Valuation — EV/revenue vs. peers (no PE, by design)

**Recomputed multiples (`financial_rigor.py`):**
- Market cap: **$49.12 × 373.27M = $18.34B** (0.03% deviation vs. reported — verified)
- Enterprise value: $18.34B − ~$3.1B net cash ≈ **$15.24B**
- **EV / FY2025 revenue = 117×** · EV / FY2026 guided mid ($265M) = **57.5×**
- **P/S = 141× FY2025** · ~69× FY2026 guided

**Peer comparison (P/S, 2026):**

| Company | Ticker | Modality | ~Revenue | ~P/S | Note |
|---|---|---|---|---|---|
| **IonQ** | IONQ | Trapped-ion | $130M (FY25) | **~141×** | Most revenue of the pure-plays |
| Rigetti | RGTI | Superconducting | ~$4.4M (Q1'26) | **~465-836×** | Tiny revenue, extreme multiple |
| D-Wave | QBTS | Annealing | small; Q1'26 rev −42% YoY | **~791×** | Bookings +1,994% but revenue fell |
| IBM | IBM | Superconducting | ~$62B+ (co.) | **~7-8×** (whole co.) | Quantum is a *tiny* fraction; not comparable pure-play |
| Quantinuum | (IPO'd Jun 2026 @ $60) | Trapped-ion | private→public | n/a | Direct trapped-ion rival, now listed |

**Counter-intuitive but important:** on P/S, **IonQ is the *cheapest* pure-play** (141× vs. RGTI/QBTS at 465-836×) precisely because it has the most revenue — the multiple is "less insane," not sane. Versus IBM (a profitable, diversified 7-8× P/S business whose quantum effort is fully funded by other earnings), IonQ is ~18-20× more expensive per dollar of sales with none of the profits. **There is no valuation anchor that makes IonQ look cheap in absolute terms; it only looks cheap *relative to even more speculative peers*.**

---

## 5. Three-scenario valuation (tool output — verification record)

Because earnings are negative, the scenario engine is **repurposed**: the "EPS" field = **FY2025 revenue per share ($0.3483)**, growth = **revenue CAGR 2025→2030 (5-yr)**, and the "target PE" field = **terminal P/S multiple**. This yields target price = future revenue-per-share × terminal P/S — a clean EV/revenue-style scenario. **Caveat: this holds share count flat, which is optimistic** (see dilution note below).

```
============================================================
Three-Scenario Valuation
============================================================
  Current price: 49.12 USD
  Current EPS:   0.3483   [= FY2025 revenue per share]
  Forecast period: 5 years  [to 2030]

  Scenario      Growth/yr  Target PE   Target EPS   Target price   Change
  ------------ ---------- ---------- ------------ ------------- --------
  Bull                50%        30x         2.64          79.3   +61.5%
  Base                35%        15x         1.56          23.4   -52.3%
  Bear                15%         5x         0.70           3.5   -92.9%
  [Growth = revenue CAGR; "PE" = terminal P/S multiple]
  ✅ All calculations use exact decimals, auditable and reproducible
```

**Implied 2030 total revenue (tool-verified):** Bull ≈ **$987M** · Base ≈ **$583M** · Bear ≈ **$262M**.

**Dilution overlay (honest correction):** the scenarios above assume flat shares. With SBC ~199% of revenue and equity-funded M&A, ~8%/yr dilution over 5 years multiplies per-share value by **0.68** (tool-verified 1/1.08⁵). So realistic per-share targets are roughly: **Bull ~$54, Base ~$16, Bear ~$2.4.** Dilution alone erases most of the bull-case upside from today's price.

**Scenario read:** the distribution is **violently asymmetric to the downside**. Even the *bull* case (50% revenue CAGR to ~$1B by 2030 at a still-rich 30× P/S) returns only ~+62% before dilution — and after dilution barely beats today's price. The base and bear cases lose 52% and 93%. **This is the signature of an over-priced option: you need the near-perfect outcome merely to break even, and ordinary disappointment is catastrophic.**

---

## 6. Margin-of-safety verdict

| Test | Result |
|---|---|
| Intrinsic value estimable with confidence? | **No** — no earnings, no positive FCF, terminal value depends on an unsettled technology race |
| Price vs. any defensible value anchor | **Far above** — 117× EV/revenue, 141× P/S; cheapest pure-play only relative to more speculative peers |
| Margin of safety at $49.12 | **None / negative** — even the bull scenario needs a near-perfect outcome to justify the price; base/bear imply −52%/−93% |
| Buffett "don't lose money" | **Fails** — the payoff distribution is dominated by large-loss outcomes |

**Dimension rating: ★ (1 / 5).** On Buffett's framework — owner earnings, demonstrated cash generation, a computable intrinsic value, and a margin of safety — IonQ scores at the floor. There are no earnings to value, cash flow is deeply negative and worsening, dilution is structural, and the price embeds a technology outcome that may be a decade away or may never arrive. **The one honest positive** is a ~5-year cash runway and premium-priced raises (management sold stock well) — but that mitigates *financing risk*, not *valuation risk*.

**Counter-argument (both sides):** a venture investor rightly notes that *every* transformational technology looked un-valuable on a Buffett screen early (Amazon 1999). Multiples this high are the market pricing optionality, not steady-state economics. **True — but the Buffett lens is explicitly designed to decline that trade, and this file is written from that lens.** The honest synthesis: IonQ is **an expensive option on quantum fault tolerance, not an investment in a cash-generating business.**

---

### Sources
- Anchor: `reports/IonQ/data-snapshot.md`; earnings deep-read `reports/IonQ/IonQ-earnings-2026Q1.md`
- stockanalysis.com/stocks/ionq (financials, cash flow); macrotrends (revenue history)
- Peer P/S: stockanalysis.com/macrotrends for RGTI, QBTS; Yahoo Finance key-statistics; Motley Fool quantum coverage (May 2026)
- Quantinuum IPO June 2026 @ $60 (Quantinuum press)
- Calc & scenarios: `tools/financial_rigor.py` (market cap 0.03% dev; EV/rev 117×/57.5×; three-scenario; dilution 0.68×; SBC 198.6% of revenue)

*Objectivity note: PE/PEG explicitly excluded as meaningless; facts sourced, estimates flagged `[est]`; both sides shown; tool output embedded verbatim as verification record. Whole-star rating.*
