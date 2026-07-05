# IonQ, Inc. — Comprehensive Investment Decision Report

**Company:** IonQ, Inc. · **IONQ / NYSE / USD**
**Run date:** 2026-07-05 · **Currency:** USD throughout
**Price anchor:** $49.12 (close 2026-07-02) · ~373.27M shares · **market cap ≈ $18.34B** (recomputed `$49.12 × 373.27M`, 0.03% deviation vs reported — `tools/financial_rigor.py`)
**Information-richness rating: A** (NYSE-listed, full SEC filings, ~13–17 analyst coverage; all anchor facts cross-validated ≥2 sources; market cap reconciled to <1%)

---

> ## ⛔ ELIMINATION BANNER — READ FIRST
>
> **IonQ was EXCLUDED by the Phase-1 quality screen.** It fails **5 of 7 hard metrics** (ROE, 5-yr cumulative FCF, net margin, share-count dilution, earnings-quality/OCF), with interest coverage not meaningful and only gross margin passing. **None of the three exemption clauses applies** (each requires positive operating cash flow or positive returns, which IonQ does not have). In a normal `/berkshire-skill` run this elimination is a **HARD GATE that halts the pipeline**.
>
> The deeper phases (four-master research team, management deep-dive, Q1'26 earnings deep-read, buy checklist, thesis) were run **only under a `force` override, as an end-to-end pipeline test**. Every one of them converged on the same conclusion. The final verdict is **AVOID**.
>
> This report is written with **no preset stance** (CLAUDE.md): data first, logic second, conclusion last — the AVOID falls out of the data, not a prior. Both sides are shown on every core judgment.

---

## 1. One-line verdict

**IonQ is a well-capitalized, technically-credible, triple-digit-growth *option on quantum fault tolerance* — priced at ~141× sales as if victory were assured, funded by ~199%-of-revenue dilution, run by a capable but heavily-promotional capital-markets operator whose integrity is "not a clear yes," with a payoff distribution (base −52%, bear −93%) violently asymmetric to the downside. On all four master frameworks it is a speculation, not an investment. Verdict: AVOID.** The quality-screen exclusion stands; the deeper phases only confirmed it.

*(≈95 words)*

---

## 2. Four-dimension scorecard

| Dimension | Framework | Rating | Core judgment |
|---|---|:---:|---|
| Business model & moat | Duan Yongping | **★★** | Real trapped-ion tech/IP + broad cloud distribution, but no pricing power, negative scale economics, growth substantially *bought* not earned |
| Financials & valuation | Buffett | **★** | No earnings/FCF to value; 141× P/S, 117× EV/rev; three-scenario base −52%; **no margin of safety** — the binding constraint |
| Industry & competition | Munger | **★★** | Enormous but *deferred* TAM; weak seat in the value chain vs IBM/Google/Quantinuum; inversion finds 7 failure modes to 1 success path |
| Risk & management | Li Lu | **★★** | ~5-yr cash runway (a genuine plus), but dilution + timeline + valuation + integrity "not a clear yes"; ten-year certainty near-zero |

**Composite (research team): (2+1+2+2)/4 = 1.75 → ★★.**
**Composite (Phase-5 six-gate checklist): (2+1+2+2+1+2)/6 = 1.67 → ★★.**
**Management deep-dive (weighted): 2.25 → ★★** (integrity ★★, strategy/execution ★★★, capital allocation ★★, governance ★★).

*Both composites round to ★★ and agree. The valuation dimension at ★ is load-bearing: even the bull case barely clears today's price after dilution.*

---

## 3. Key-data snapshot (FY2024 → FY2025 → Q1 2026)

| Metric (USD) | FY2024 | FY2025 | Q1 2026 | Source |
|---|---|---|---|---|
| Revenue | $43.1M | **$130.02M** (+201.9%) | **$64.7M** (+755% YoY) | IonQ 10-K / 8-K; stockanalysis.com; data-snapshot.md |
| Gross margin | ~43% | **40.4%** | **23.8%** ⬇ | stockanalysis.com; Q1'26 8-K |
| Operating income | negative (exact *insufficient data*) | **−$633.72M** | **−$271.5M** | stockanalysis.com; Q1'26 8-K |
| GAAP net income | negative | **−$510.38M** | **+$805.4M** ⚠️ artifact | IonQ IR / 10-K; Q1'26 8-K |
| Net income ex-warrant `[est]` | — | — | **≈ −$255M** | derived (Q1 GAAP less ~$1.06B warrant gain) |
| Operating cash flow | negative | **−$283.19M** | **−$151.0M** | stockanalysis.com; Q1'26 8-K |
| Free cash flow | negative | **−$299.60M** | ~−$160M `[est]` | stockanalysis.com; earnings deep-read |
| Stock-based comp | — | — | **$128.52M (~199% of revenue)** | Q1'26 10-Q (via search); `financial_rigor.py` (198.6%) |
| Cash + equivalents + investments | — | ~$3.1B | **~$3.1B** (Mar 31, 2026) | IonQ Q1'26 press release |
| Backlog / RPO | — | — | **~$470M (+554% YoY)** | IonQ Q1'26 8-K |
| Shares outstanding | — | — | **~373.27M** (+93% since ~193M at 2021 listing) | stockanalysis.com; companiesmarketcap |
| Market cap / P/S / EV-rev | — | — | **$18.34B / 141× / 117×** | recomputed `financial_rigor.py` |
| FY2026 guide (raised) | — | — | rev **$260–270M**; adj-EBITDA **−$310M to −$330M** | IonQ Q1'26 8-K / Investing.com |

> ⚠️ **The GAAP "profit" trap.** Q1'26 GAAP net income of **+$805.4M** is **not profit** — it is a **~$1.06B non-cash gain** from marking liability-classified warrants to fair value. Those liabilities *fall when IonQ's stock falls*, so the "record profit" is a byproduct of the **share price declining** during the quarter. Strip it out: IonQ **lost ~$255M** `[est]`. The clean reads are operating loss (−$271.5M) and adjusted EBITDA (−$96.8M, missing ~−$79.9M consensus). Ignore GAAP net income and EPS for IonQ. *(Note: TTM net income of +$327M is the same warrant artifact and is likewise not earnings.)*

---

## 4. Per-phase summaries (Phases 1–6)

**Phase 1 — Quality screen (`IonQ-quality-screen-20260705.md`): EXCLUDED.**
1. Fails **5 of 7** hard metrics: ROE deeply negative every year; 5-yr cumulative FCF strongly negative; net margin ≈ −393% (FY2025); dilution +93% since 2021; OCF/earnings-quality moot (no profit to convert).
2. Only **gross margin passes** (40.4% FY2025 > 15% threshold); interest coverage **not meaningful** (negative EBIT, minimal debt) → treated as fail.
3. **No exemption applies** — Strategic-investment (needs OCF positive last 2 yrs: fails, OCF −$283M/−$401M), Deliberately-low-margin (needs net-margin recovery: fails), High-turnover thin-margin (needs ROE >20%: fails).
4. Screen note: passing would not have meant "buy"; failing does not mean the equity cannot appreciate — it means IonQ is disqualified from the *quality-first* funnel on current, cash-based fundamentals. A bull case is a venture/thematic framework, not a Buffett-quality screen.

**Phase 2 — Four-master research team (`final-report.md` + `01`–`04`): composite ★★ (1.75), AVOID.**
1. **Business (Duan ★★):** only **1 of 5 classic moats holds** — technology/IP (trapped-ion + acquired "four-nines" 99.99% fidelity); brand weak, network effect absent, switching cost low, scale economics *negative* (margin fell as volume rose). **No pricing power.** No clean revenue segment split disclosed (*insufficient data*).
2. **Financials (Buffett ★):** PE/PEG meaningless; valuation by EV/revenue + scenarios by design. On P/S, IonQ (141×) is the *cheapest pure-play* only vs RGTI (~465–836×) and QBTS (~791×) — "less insane," not sane; vs profitable IBM (~7–8×) it is ~18–20× dearer per sales dollar with none of the profits.
3. **Industry (Munger ★★):** TAM real but *deferred* — provider revenue only **~$1–2B total through 2030** (BCG); QC revenue $43–72B by 2035 (McKinsey). Fault tolerance is a **2030–2040+** event; **inversion surfaces 7 independent failure modes** vs one narrow success path.
4. **Risk (Li Lu ★★):** dilution is the near-certain high-severity risk; ten-year certainty near-zero; base/bear scenarios (−52%/−93%) are permanent-loss-shaped.

**Phase 3 — Management deep-dive (`IonQ-management-20260705.md`): ★★, integrity "not a clear yes."**
1. Run by **Niccolo de Masi** — the SPAC sponsor who took IonQ public in 2021, now **Chairman + President + CEO** simultaneously; both scientist co-founders (Monroe, Kim) gone to advisory; six-year operating CEO Chapman pushed off the board within ~5 months. A capital-markets operator running a deep-physics company (genuine Cambridge physics background — a real mitigant).
2. **Integrity two-sided:** revenue/bookings guidance **beaten 5-for-5 (2021–2025)** and the crudest short (Scorpion 2022) court-discredited; *but* documented 2020 "32 perfect qubits" overstatement (machine ~11), physical-vs-logical qubit conflation ("eliminate Nvidia's Blackwell"), a **"no equity before 2028" pledge broken within six months**, a **CEO-owned Gulfstream leased back to the company**, and complexity theorist **Scott Aaronson's "wild misrepresentations… to governments"** charge.
3. **Insiders one-directional sellers:** ~13.6M shares sold vs ~98K bought over ~18 months; **de Masi ~$106M, Chapman ~$270.7M** cashed out; insider group cut to **<1%** — while the **scientist-founders largely held** (a revealing asymmetry).
4. Governance flags: **say-on-pay 95%→64%→54%**, ISS QualityScore **9/10**, **$89.58M** CEO comp (**217:1** ratio) at a company losing ~$510M. Capital allocation ★★ — genuine strength (raises struck at 20–25% *premiums*) offset by ~$2.5B mostly-stock M&A, several undisclosed prices, two off-thesis deals (Capella satellites, SkyWater foundry).

**Phase 4 — Q1'26 earnings deep-read (`IonQ-earnings-2026Q1.md`): SPLIT — top-line beat around a bottom-line miss.**
1. **Revenue clear BEAT:** $64.7M (+755% YoY) beat the ~$50M guide and ~$49.7M consensus by ~30%; RPO $470M (+554%); FY2026 guide raised to $260–270M; mix now ~60% commercial / ~35% international.
2. **Earnings-quality MISS:** gross margin collapsed 40%→**23.8%**; adjusted EBITDA −$96.8M (worse than ~−$79.9M consensus); adjusted EPS −$0.34 (vs ~−$0.25); operating burn **−$151M** (~doubled). The stock fell **−9.3%** the next session — the market priced the burn, not the headline.
3. **The $805.4M "profit" is a warrant-mark mirage** (rises when the stock falls); underlying loss ~$255M. SBC $128.5M ≈ **199% of revenue**.
4. **~5-year runway** (~$3.1B ÷ ~$604M annualized burn) — liquidity is *not* the near-term risk; **dilution and M&A cash drain** (SkyWater $1.8B pending) are. **No quality metric improved.**

**Phase 5 — Buy checklist (`IonQ-checklist-20260705.md`): FAILED, composite ★★ (1.67), AVOID.** (Full table in §6.)
1. Six-gate score 1.67; two gates at the ★ floor — **Gate 2 (good business)** and **Gate 5 (margin of safety)** — are the binding constraints.
2. **Two independent, unambiguous red lines** fail *regardless* of the integrity call: no margin of safety, and FCF negative every year 2021–2025 with the loss guided to widen.
3. **Mirror test FAILED** — 4 of 5 buy-sentences cannot be completed affirmatively.
4. The automatic ★1 management **hard veto does not fire** (fraud unproven); integrity registers as a **gray-zone stain that compounds, not causes, the AVOID**.

**Phase 6 — Thesis (`IonQ-thesis.md`): established as a "why we are NOT buying" thesis; AVOID / EXCLUDED.**
1. Of the **7 assumptions a bull must hold, 4 are 🔴 impaired and 3 are 🟡 unproven; none is 🟢** — every load-bearing assumption is either broken or unproven on current data.
2. 🔴 assumptions: gross-margin recovery, burn peaking/OCF path, dilution slowing, integrity/governance improving — all fail today.
3. Reconsideration requires a **durable margin recovery AND a valuation reset** (gross margin back toward 40%+ for multiple quarters, credible dated path to positive OCF, dilution slowing, *and* <30× EV/revenue ≈ the ~$15–25 base zone).
4. Red-line monitoring list carried into §7 below.

---

## 5. Bull vs Bear

**🟢 Bull case (the genuine steelman — both sides per CLAUDE.md):**
1. **Best-capitalized pure-play** (~$3.1B) with a ~5-year runway to fund a multi-year technology bet without near-term insolvency.
2. **Revenue compounding triple-digits** — first pure-play past $100M; Q1'26 +755%; FY2026 guide raised to $260–270M; backlog $470M (+554%).
3. **Real technical proof-points** — four-nines (99.99%) two-qubit fidelity; an Ansys run reportedly beating classical HPC by ~12% on 36 qubits; the largest listed pure-play brand.
4. **Coherent vertically-integrated "quantum internet" thesis** (compute + networking + sensing + security) — multiple shots on goal.
5. **Management sold stock at premiums** (raises 20–25% above market) — genuine capital-markets skill; monetized an expensive currency well, de-risking financing.
6. **Enormous deferred TAM** — if trapped-ion reaches useful fault tolerance and IonQ's IP holds, today's ~$18B could look small against a $43–72B (2035) revenue pool.
7. **Analyst consensus constructive** — ~13–17 analysts, Buy/Strong Buy, average target ~$63–69 (high ~$100), implying ~30–40% upside *on thesis*.

**🔴 Bear case:**
1. **No margin of safety** — 141× P/S / 117× EV-revenue; base scenario −52%, bear −93%; even the bull barely clears today's price after dilution.
2. **Structural dilution** — SBC ~199% of revenue, ~79M-share warrant overhang, stock-funded M&A; +93% shares since 2021; holders' claim shrinks every quarter.
3. **The "profit" is a mirage** — Q1 +$805M GAAP net income is a warrant-mark that *rises when the stock falls*; underlying loss ~$255M.
4. **Margins going the wrong way** — 40.4% → 23.8% as low-margin hardware dominates; no operating leverage yet; FY2026 loss guided to *widen*.
5. **Fierce, better-funded competition** — IBM, Google, and **Quantinuum** (same trapped-ion modality, Honeywell-backed, IPO'd Jun 2026, arguably ahead); hyperscalers own the customer.
6. **Integrity "not a clear yes"** — documented overstatements, physical-vs-logical conflation, broken "no equity before 2028" pledge, related-party jet, collapsing say-on-pay, Aaronson's misrepresentation charge; insiders cashed out to <1%.
7. **Timeline risk dominates** — useful fault tolerance is 2030–2040+; the ~$320M/yr burn option can expire before the payoff arrives.

---

## 6. Buy-checklist result — Buffett six-gate table (Phase 5)

| # | Gate | Rating | Verdict |
|---|------|:------:|---------|
| 1 | Circle of competence | **★★** | Business *mechanism* explainable; 10-yr *outcome* (useful fault tolerance) not forecastable — certainty near-zero |
| 2 | Good business (economics) | **★** | ROE deeply negative; FCF negative every year since listing; gross margin collapsing 40.4%→23.8% — **★ floor** |
| 3 | Moat depth | **★★** | Only 1 of 5 moats holds (tech/IP, unproven & partly *acquired*); no pricing power; scale economics negative |
| 4 | Management trustworthy | **★★** | Capable, physics-literate; but integrity "not a clear yes," heavy insider cash-out, say-on-pay 95%→54%, ISS 9/10 |
| 5 | Margin of safety | **★** | 141× P/S, 117× EV/rev; base fair value ~$23 vs $49.12 = ~52% overvalued — **no margin of safety, ★ floor** |
| 6 | Emotional discipline | **★★** | Buy impulse is FOMO/story-driven; fails the 5-year-trading-suspension test; only a small losable option survives |

**Composite: 1.67 → ★★. Result: ❌ FAILED — verdict AVOID.**
Red lines triggered: **(1) Gate 5 — no margin of safety (binding); (2) Gate 2 / Step-5 FCF-negative-3-years veto; (3) Mirror test FAILED (4 of 5 sentences uncompletable).** The standalone ★1 management hard veto **does not fire** (fraud unproven); integrity is a gray-zone stain that compounds — not causes — the failure. Consistent with the four-master ★★ (1.75) and the Phase-1 exclusion.

---

## 7. Final recommendation — **AVOID**

### 7.1 Valuation range (EV/revenue-repurposed three-scenario, `financial_rigor.py`; PE excluded by design)

| Scenario | Rev CAGR 2025→2030 | Terminal P/S | Implied 2030 rev | Target price | vs $49.12 | Dilution-adj `[est]` (×0.68) |
|---|---|---|---|---|---|---|
| **Bull** | 50% | 30× | ~$987M | **~$79** | **+61.5%** | ~$54 (~+10%) |
| **Base** | 35% | 15× | ~$583M | **~$23** | **−52.3%** | ~$16 |
| **Bear** | 15% | 5× | ~$262M | **~$3.5** | **−92.9%** | ~$2.4 |

**Read:** the distribution is the signature of an over-priced option — you need the near-perfect (Bull) outcome merely to earn a modest return after dilution, while ordinary disappointment (Base) loses half and a bad outcome (Bear) loses almost everything. Analyst consensus (~$63–69) sits above our Base fair value (~$23) because the Street prices *optionality*, not owner-earnings — a legitimate but different lens; we flag the divergence rather than adopt it.

### 7.2 Tiered position sizing — **portfolio-aware**

Current hypothetical book (from `reports/portfolio-latest.md`, a legacy Chinese-language file dated 2026-04-09, parsed): **Tencent 35% / Pinduoduo 30% / Pop Mart 20% / cash 15%** — a concentrated China internet + consumer portfolio with **~85% single-country (China) risk** and only 15% cash.

- **Sector/theme overlap with IonQ: none.** IonQ is US-incorporated quantum-computing *hardware* — a different country, sector, and factor set from the book's China internet/consumer names. On a pure-diversification axis it would *reduce* the 85% China concentration the portfolio review flagged as the book's "most fatal structural flaw."
- **But two facts override the diversification appeal:** (a) the book is already **85% equity with only 15% cash** — little risk budget is uncommitted; and (b) **IonQ is an AVOID** — a pre-profit, deeply cash-burning, heavily-diluting speculation that fails the quality screen, the checklist, and the margin-of-safety test. The portfolio review's own remedy for the China concentration was to redeploy cash into **quality, profitable diversifiers** (it named Berkshire/BRK.B, Alphabet, or a broad US index ETF) — *not* a single pre-profit venture option. IonQ is the wrong instrument for that job.

| Investor profile | Recommendation | Condition |
|---|---|---|
| **Conservative (this framework's default, and this book's profile)** | **AVOID — 0% allocation** | Do not initiate at any price on a quality basis; fails the screen, checklist, and margin-of-safety test. If geographic diversification is the goal, use a profitable proxy, not IonQ. |
| **Balanced** | **AVOID / do not initiate** | If quantum exposure is desired, prefer a diversified/profitable proxy (e.g., IBM). Revisit only on a durable margin recovery **and** a valuation reset toward <30× EV/revenue (~$15–25). |
| **Aggressive / venture-tolerant** | **Speculative only — size as a call option** | Cap at a *small, losable* slice **outside** a concentrated quality book; entry meaningfully de-risked only below **~$15–25** (base-scenario zone); accept ongoing dilution and −$300M+/yr burn as the cost of the option. Even here, this is a payoff-distribution bet, not an investment. |

**Practical recommendation for the actual book: no allocation.** Keep the 15% cash (or deploy it into the quality, non-China diversifiers the portfolio review identified). Adding an AVOID-rated pre-profit speculation would spend scarce risk budget on the portfolio's worst risk-reward, not its best.

### 7.3 Catalysts

**Add-to-position (thesis-validating) signals:** (1) gross margin recovers durably back toward **40%+** (software/cloud mix returns); (2) **positive operating cash flow inflection** or a credible dated path to it; (3) **hardware demonstration** of logical-qubit / fault-tolerance milestones on *shipping* systems (not prototypes); (4) **dilution slows** — SBC falls below revenue, warrant overhang cleared, raises stop; (5) **valuation resets** to <30× EV/revenue.

**Trim / avoid (thesis-breaking) signals:** (1) **Quantinuum or IBM** demonstrably passes IonQ on the trapped-ion / fault-tolerance curve; (2) **another large equity raise** or major stock-funded acquisition (e.g., SkyWater $1.8B closing heavy in stock); (3) **backlog fails to convert** to recognized revenue at reasonable margin (validating the bookings-vs-funded concern); (4) **narrative/funding break** — inability to raise on favorable terms; (5) **further governance deterioration** (say-on-pay <50%, more executive exits, related-party expansion).

### 7.4 Red-line list (from the thesis — triggering any one forces re-evaluation)

| # | Red-line condition | Severity | Action when triggered |
|---|---|:---:|---|
| 1 | Management integrity breaks down further — proven misrepresentation, SEC/regulatory action, restatement, or fraud finding | **Fatal** | Exclusion confirmed permanently; no reconsideration |
| 2 | Another large equity raise or major stock-funded acquisition (e.g. SkyWater $1.8B closes with heavy stock) | Severe | Reaffirm AVOID; step up dilution overlay |
| 3 | Backlog / RPO fails to convert to recognized revenue at reasonable margin | Severe | Revenue-quality thesis broken; deepen pass |
| 4 | A competitor (Quantinuum / IBM / Google) demonstrably passes IonQ on the trapped-ion / FT curve | Severe | Only remaining moat (tech/IP) breached |
| 5 | Gross margin stays ≤ ~24% or falls further for 2+ quarters | Severe | Confirms no operating leverage |
| 6 | Narrative / funding break — inability to raise on favorable terms | Severe | Dilution turns from fuel to death-spiral risk |
| 7 | Further governance deterioration — say-on-pay <50%, more executive exits, related-party expansion | Warning | Investigate; weight against any reconsideration |

---

## 8. Closing paragraph

IonQ is the clearest live example of the gap between a *good story* and a *good business*. The story is genuinely compelling: the largest listed pure-play in a field that could be worth tens of billions in revenue by 2035, best-capitalized of its peers, compounding revenue at triple digits, with real technical results and a coherent stack. But every master lens — Duan's "good business," Buffett's owner-earnings and margin of safety, Munger's inversion, Li Lu's downside-first certainty — converges on the same verdict: at 141× sales, funded by 199%-of-revenue dilution, run by a promoter whose integrity is "not a clear yes," with fault tolerance a 2030–2040+ maybe and a base-case fair value ~52% below today's price, this is an **expensive option on the future, not an investment in a durable enterprise**. The composite **★★ (1.75/5)**, the checklist **1.67/5 FAIL**, and the **AVOID** fall directly out of the data. The Phase-1 exclusion stands — not because quantum is uninteresting, but because certainty comes from the business model, and here it is absent.

**Information-richness rating: A (information-rich).** Full SEC filings, IR releases, ~13–17 analyst coverage, multiple independent aggregators; all anchor facts cross-validated ≥2 sources; market cap reconciled to <1% via `financial_rigor.py`.

**AI-research-limitations note (honest, per CLAUDE.md):**
- This session's egress proxy **blocked direct reads of sec.gov, the IonQ IR CDN (q4cdn.com), and transcript hosts (fool.com / seekingalpha.com / investing.com)** — 403 at the proxy. Headline financials were extracted via searches that quote the 8-K/10-Q/10-K directly and cross-checked against ≥2 secondaries (treat as **A-confidence**); **10-Q footnote detail and verbatim earnings-call Q&A are Grade B** and flagged where load-bearing (e.g., RPO conversion margin, live dilution/burn Q&A — marked *insufficient data* rather than guessed).
- **`financial_rigor.py`'s standard PE-based three-scenario is inapplicable to IonQ**: on its negative EPS (−$1.37) the engine returns nonsensical negative target prices (Bull −$90, Base −$42, Bear −$10) — the tool *correctly* demonstrating that a PE framework cannot value a negative-earnings company. Valuation was therefore anchored on an **EV/revenue-repurposed** three-scenario (the "EPS" field = revenue-per-share, the "PE" field = terminal P/S), plus a dilution overlay (0.68× over 5 yrs). The tool *arithmetic* is exact and auditable; the *assumptions* (terminal P/S, CAGR) are analyst judgment. The robust conclusion is the **shape** of the distribution (violent downside asymmetry), not the specific target prices.
- **More information ≠ more certainty.** IonQ is information-rich yet fundamentally *low-certainty*: the uncertainty lives in the technology and business model, not the disclosure. Confidence in the *facts* is high; true *investment certainty* is low. No preset stance — the AVOID is derived from the data.

---

### Sources (consolidated)
- This run's outputs: `reports/IonQ/data-snapshot.md`, `IonQ-quality-screen-20260705.md`, `01`–`04-*.md`, `final-report.md`, `IonQ-management-20260705.md`, `IonQ-earnings-2026Q1.md`, `IonQ-checklist-20260705.md`, `IonQ-thesis.md`
- Portfolio context: `reports/portfolio-latest.md` (prior research, dated 2026-04-09; legacy Chinese-language file)
- IonQ FY2025 10-K (SEC accession 000119312526071562); Q1'26 8-K/10-Q; ionq.com/news & /roadmap
- stockanalysis.com / macrotrends (IONQ, RGTI, QBTS); Yahoo Finance; companiesmarketcap; Motley Fool quantum coverage (May–Jul 2026)
- TAM/roadmaps: McKinsey Quantum Technology Monitor 2026; BCG (2024); MarketsandMarkets; ibm.com/roadmaps/quantum; Quantinuum accelerated-roadmap press + June 2026 IPO @ $60; Google Willow
- Governance: DEF 14A 2026-04-30 & 2025-04-28; Form 4 filings; ISS QualityScore; scottaaronson.blog; Wolfpack Research (Feb 2026, disputed); Kerrisdale (Mar 2025); Scorpion (2022, court-discredited)
- Analyst targets: stockanalysis.com/forecast, MarketBeat, TipRanks, public.com (consensus ~$63–69)
- Verification: `tools/financial_rigor.py` (market cap 0.03% dev; EV/rev 117×/57.5×; P/S 141×; three-scenario; dilution 0.68×; SBC 198.6% of revenue)

*Objectivity statement (CLAUDE.md): every core judgment carries a counter-argument; facts are sourced and separated from labeled opinion/estimate; "insufficient data" is stated where true (no clean revenue segment split disclosed; blocked primary hosts noted); no preset stance — the AVOID conclusion is derived from the data. Currency USD throughout; star ratings are whole stars (1–5), no half-stars.*
</content>
</invoke>
