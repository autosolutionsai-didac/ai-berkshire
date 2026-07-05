# Earnings Deep-Read — IonQ, Inc. (IONQ / NYSE) — Q1 2026

**Period:** Q1 2026, three months ended March 31, 2026 (reported May 6, 2026, after market close)
**Annual backdrop:** FY2025 (10-K, year ended Dec 31, 2025)
**Run date:** 2026-07-05 | **Reporting currency:** USD | **Analyst:** /earnings-review deep-read

> "I read 500 pages a day. That's how knowledge builds up, like compound interest." — Buffett
> "I never read sell-side research; I only read the original filings." — Li Lu

> **Screen context (do not bury):** IonQ was **EXCLUDED** by the Phase-1 quality screen (fails 5 of 7 hard metrics — ROE, cumulative FCF, net margin, dilution, earnings-quality/OCF; only gross margin passes; no exemption applies). In a normal pipeline this is a hard gate. This deep-read is a **forced test continuation** and is analyzed honestly, with no preset stance. See `reports/IonQ/IonQ-quality-screen-20260705.md`.

---

## Source Availability Rating: B (headline data at A-confidence; footnotes not read verbatim)

**Honest limitation.** This session's egress proxy blocked direct CONNECT to the primary hosts — `sec.gov` (10-Q/10-K/8-K), IonQ IR CDN (`q4cdn.com` investor deck), and the transcript hosts (`fool.com`, `seekingalpha.com`, `investing.com`), all returning 403 at the proxy. I therefore could **not** read the 10-Q footnotes or the full earnings-call Q&A line-by-line. All figures below were extracted via web search that **quotes the 8-K press release, 10-Q, and investor deck directly**, cross-validated against ≥2 independent secondaries (Zacks/Yahoo, Futurum, Quantum Computing Report, StockTitan, The Quantum Insider, Investing.com) and reconciled with the pre-verified anchor file `reports/IonQ/data-snapshot.md`. Headline financials are internally consistent and cross-checked (treat as A-confidence). **Footnote-level analysis (Step 4) and verbatim Q&A (Step 5) are downgraded to Grade B** — flagged where it matters.

---

## 1. Core-Data Snapshot (one page)

### Income statement — Q1 2026 vs Q1 2025

| Metric (USD) | Q1 2026 | Q1 2025 | YoY | Guidance / consensus | Verdict |
|---|---|---|---|---|---|
| Revenue | **$64.7M** | $7.6M | **+755%** | Guide mid ~$50M; consensus ~$49.7M | ✅ **Beat (+30%)** |
| Gross profit | $15.41M | $3.25M | +374% | — | Grew, but... |
| Gross margin | **23.8%** | ~42.8% | **−~19 pts (−1,913 bps)** | — | ❌ Sharp contraction |
| Loss from operations | **−$271.5M** | n/a | wider | — | ❌ Widened |
| Adjusted EBITDA | **−$96.8M** (ex-SkyWater −$85.0M) | — | wider | consensus ~−$79.9M | ❌ **Miss** |
| Warrant fair-value change | **+$1.06B (non-cash gain)** | — | — | — | ⚠️ Artifact |
| GAAP net income | **+$805.4M** | net loss | — | — | ⚠️ **Mirage** |
| Net income ex-warrant `[estimate]` | **≈ −$255M** | — | — | — | The real number |
| GAAP diluted EPS | **+$2.19** | — | — | — | ⚠️ Mirage |
| Adjusted EPS | **−$0.34** | — | — | consensus ~−$0.25 | ❌ Miss |
| Stock-based comp | **$128.52M** (≈199% of revenue) | — | — | — | ❌ Dilution engine |
| R&D expense | $125.74M | — | — | — | — |

### Cash flow & balance sheet

| Metric (USD) | Q1 2026 | FY2025 | Focus |
|---|---|---|---|
| Operating cash flow | **−$151.0M** | −$283.2M | Burn ~doubled vs 2025 avg (~−$71M/qtr) |
| Free cash flow `[estimate]` | ~−$160M+ | −$299.6M | Accelerating |
| Cash + equivalents + investments | **~$3.1B** (Mar 31, 2026) | ~$3.1B | Raise-funded, not earned |
| Remaining performance obligations (RPO / backlog) | **$470M** | — | +554% YoY |
| Accumulated deficit (YE2025) `[flag: single-source]` | ~$1,194.1M | — | Note: swings with warrant mark |

### Guidance (raised)

| Item | New guidance | Prior guidance |
|---|---|---|
| Q2 2026 revenue | $65M–$68M | — |
| FY2026 revenue | **$260M–$270M** (~+100% organic) | $225M–$245M |
| FY2026 adjusted EBITDA | **−$310M to −$330M** | — |

### FY2025 annual backdrop (anchor, verified)

Revenue $130.02M (+201.9%); gross margin 40.4%; **operating loss −$633.72M**; net loss −$510.38M; OCF −$283.2M; capex −$16.4M; FCF −$299.6M. Note: even FY2025's net loss (−$510M) is *smaller* than its operating loss (−$634M) — i.e., below-operating items (interest income + warrant/other) flattered the headline. **The operating loss is the clean read in both periods.**

### Valuation (market cap recomputed, `financial_rigor.py`)

Price **$49.12** (close Jul 2, 2026) × **373.27M** shares = **$18.34B** market cap (0.03% deviation vs reported — verified). Revenue multiples: **P/S ≈ 141× FY2025 revenue**, **≈ 98× TTM revenue**, **≈ 69× FY2026 guided midpoint ($265M)**. No earnings multiple is meaningful (no operating earnings). Stock is down from a 52-wk high of $84.64 and fell **−9.3% on May 7** (the session after this print).

---

## 2. The 3 Most Important Changes This Period

**(1) Revenue inflected to genuine scale — the commercialization story got materially more real.** Q1 revenue of $64.7M (+755% YoY) beat the ~$50M guide midpoint by ~30% and beat the ~$49.7M Street consensus. RPO/backlog hit $470M (+554%), management raised FY2026 revenue guidance from $225–245M to $260–270M (~100% organic growth), and revenue is now ~60% commercial and ~35% international across 30+ countries — versus a near-total dependence on a few U.S. government contracts a year ago. **Fact:** the top line is no longer a rounding error. **Counter-point:** much of the jump is lumpy hardware/system sales and quantum-networking contracts (partly acquisition-fed — Oxford Ionics, ID Quantique, Qubitekk), not recurring cloud-compute revenue.

**(2) Unit economics deteriorated even as revenue exploded — growth is being *bought*, not *earned*.** Gross margin collapsed from ~40% (FY2025) / ~43% (Q1 2025) to **23.8%** as low-margin system sales dominated the mix. The operating loss (−$271.5M) and adjusted EBITDA loss (−$96.8M, worse than the ~−$79.9M consensus) both widened, and operating cash burn (**−$151M**) roughly doubled the 2025 quarterly pace. FY2026 adjusted-EBITDA guidance of −$310M to −$330M tells you management expects the loss to *keep widening in dollars*. This is the reason the stock fell 9% on a revenue beat: the market priced the burn, not the headline.

**(3) The GAAP "profit" is an accounting mirage — and the mechanism is perverse.** Reported net income of **+$805.4M** ($2.19 EPS) exists **only** because of a **+$1.06B non-cash gain from the change in fair value of warrant liabilities** (Series A/B warrants from the July 2025 J.P. Morgan raise, liability-classified and marked to market). These liabilities *fall in value when IonQ's stock falls* — so the "record profit" is literally a **byproduct of the share price declining during the quarter**, not of operating performance. Strip it out and IonQ **lost ~$255M** `[estimate]`. Add stock-based comp of $128.5M (≈199% of revenue) and equity-funded M&A (SkyWater $1.8B pending; Vector Atomic), and the true shareholder cost this quarter is **dilution**, not the smiling GAAP net-income line.

*(≈380 words)*

---

## 3. Management Tone and Promise Tracking

**Participants:** Niccolo de Masi (Chairman & CEO), Inder Singh (COO & CFO). *(Note: prior long-time CFO Thomas Kramer is not on this call per available transcripts.)*

**Tone read (from opening remarks / secondary coverage; verbatim Q&A not accessible — Grade B):**

| Signal | Manifestation | Read |
|---|---|---|
| 🟢 Clarity | Specific, quantified guidance raise ($260–270M FY26); explicit ~100% organic-growth target; detailed "Walking Cat" fault-tolerance roadmap (256 → 10,000 qubits, logical error rates ~1-in-1-trillion, Q-Day/RSA-2048 in the 2028–2029 window) | Concrete and falsifiable — good |
| 🟢 Candor (partial) | Proactively disclosed that ~$11.8–12M of the adjusted-EBITDA loss is SkyWater-related and quantified the ex-SkyWater figure (−$85.0M) | Reasonable transparency on one cost |
| 🔴 Framing risk | Heavy emphasis on "record revenue," "fourth consecutive record quarter," roadmap and TAM narrative; the $805M GAAP net income headlined the press release with the warrant driver disclosed but de-emphasized | Standard promotional cadence; reader must re-center on operating loss |
| ⚪ Insufficient data | Could not verify how directly management addressed cash burn, dilution and margin compression in live Q&A (transcript hosts blocked) | Flagged, not inferred |

**Promise tracking:** IonQ has repeatedly *met or beaten its own revenue guidance* (Q1 came in ~30% above the midpoint; management notes a fourth straight record). On the "did they do what they said" test (**Duan Yongping**: "check whether they did what they said they'd do"), the **revenue promise track record is good.** The unkept-in-spirit promise is profitability: each period the loss target moves further out, and FY2026 adjusted-EBITDA guidance (−$310M to −$330M) makes explicit that break-even is not on this year's horizon.

---

## 4. Hidden Information in the Footnotes (Grade B — footnotes not read verbatim; reconstructed from disclosed figures)

- **Warrant liability accounting (the headline distortion).** Series A/B warrants are **liability-classified** and remeasured to fair value each quarter through the income statement. In Q1 2026 the share price fell, so the liability fell, booking a **+$1.06B non-cash gain**. This runs in reverse when the stock rises — meaning **GAAP net income for IonQ is anti-correlated with shareholder returns and should be discarded** in favor of operating loss / adjusted EBITDA. This is the exact footnote-signal the deep-read targets.
- **Stock-based compensation $128.5M (≈199% of revenue).** SBC exceeds revenue. It is added back to adjusted EBITDA (so "adjusted" numbers understate the true economic cost), and it is the recurring, structural source of share-count growth (shares ~193M at 2021 listing → ~373M now, ≈+93%).
- **Acquisition machine, mostly equity-funded.** Pending SkyWater ($1.8B), Vector Atomic (quantum sensing, announced Jan 2026), plus completed Oxford Ionics, Lightsynq, ID Quantique (majority stake → creates non-controlling interest), Qubitekk, Capella Space. **Watch-item:** goodwill/intangibles will balloon and become impairment candidates; the $805.4M (press release) vs $804.6M (10-Q) net-income spread is most plausibly the **NCI** from the ID Quantique majority stake `[estimate — not confirmed from footnote]`.
- **Revenue quality.** Mix shift toward system sales (hardware) is the mechanical cause of the gross-margin collapse to 23.8%. **Anomaly to monitor:** is RPO ($470M) convertible at reasonable margin, or does the backlog embed more low-margin hardware? Cannot resolve without the 10-Q segment/RPO footnote — **insufficient data.**
- **Cash is raise-funded.** The ~$3.1B balance came from ~$3.35B of FY2025 equity issuance, not operations. This is a financing story, not a cash-generation story.

---

## 5. Key Questions (analyst focus; verbatim Q&A not accessible — themes from secondary coverage)

> Full call transcript hosts were blocked this session, so the table below reflects the *tensions the print creates* and the focus of post-earnings coverage, **not** verbatim analyst quotes. Answer-quality scores are therefore withheld where I could not hear the answer.

| Question the numbers force | What we know of management's stance | Answer quality | Evasive? |
|---|---|---|---|
| Why did gross margin fall to ~24% from ~40%, and is that structural? | Attributed to system-sales mix; framed as scaling | ⚪ Not verifiable | Insufficient data |
| Adjusted EBITDA (−$96.8M) missed consensus — when does burn peak? | Guided FY26 adj EBITDA −$310M to −$330M; ex-SkyWater burn −$85M | ★★★★ (quantified, candid on SkyWater) | No |
| How much future dilution given SBC ~199% of revenue + equity-funded M&A? | Not clearly addressed in accessible remarks | ⚪ Not verifiable | Insufficient data |
| Is the $805M "profit" real? | Press release disclosed the $1.06B warrant driver | ★★★ (disclosed but headlined the GAAP number) | Partial |
| Path/date to positive operating cash flow? | No break-even date given; roadmap is technical (fault tolerance by 2030), not financial | ⚪ Not verifiable | Insufficient data |

---

## 6. Relationship to the Investment Thesis

There is **no long thesis on file** — IonQ was excluded at the quality gate. This deep-read does not create one. Framed honestly:

- **What a bull would take from this quarter:** revenue is compounding triple-digits with a real, raised guide and a $470M backlog; the company is the best-capitalized pure-play in a potentially enormous quantum TAM, with ~$3.1B to fund a multi-year technology bet; it beat and raised.
- **What a quality investor (this framework) takes from this quarter:** a company selling low-margin hardware at a 24% gross margin, burning ~$150M/quarter (accelerating), diluting shareholders via SBC that exceeds revenue and via billions in equity-funded M&A, and reporting a "profit" that is a non-cash artifact of its own falling stock price. **None of the seven quality metrics improved.** This is a venture/thematic bet on 2028–2030 fault tolerance, priced today at ~69–141× sales — a payoff-distribution decision, not a business-quality decision.

**Munger:** "A great business at a fair price is superior to a fair business at a great price." IonQ is neither a great business nor at a fair price *on current fundamentals* — it is an option on a future business at a high price.

---

## 7. Conclusion — What Did This Earnings Report Change?

**1) Beat, in line, or miss? — SPLIT, and the split is the point.**
- **Revenue: clear BEAT** (+30% vs guide and vs consensus; +755% YoY).
- **Profitability / earnings quality: MISS** (adjusted EBITDA −$96.8M vs ~−$79.9M consensus; adjusted EPS −$0.34 vs ~−$0.25; gross margin collapsed to 23.8%; operating loss −$271.5M).
- **Net verdict:** a top-line **beat wrapped around a bottom-line miss**. The market — which fell **9.3%** the next day — treated it as a **miss on the metrics that matter for a cash-burning company.** From this framework's lens: **MISS**, because losses, burn and dilution accelerated faster than the business improved.

**2) The warrant-gain distortion (must-flag):** The **+$805.4M GAAP net income is not a profit.** It is driven entirely by a **+$1.06B non-cash warrant fair-value gain** that reflects IonQ's *share price falling* during the quarter. Excluding it, IonQ **lost ~$255M** `[estimate]`. Ignore GAAP net income and EPS for IonQ; use **operating loss (−$271.5M)** and **adjusted EBITDA (−$96.8M)**.

**3) Cash runway at current burn:** With **~$3.1B** cash+investments and Q1 operating burn of **−$151M** (~−$604M annualized): **operating runway ≈ 5 years** at the current pace, or ~4 years if burn keeps accelerating toward the FY2026 adj-EBITDA guide. **Liquidity is not the near-term risk.** The binding constraints are (a) **M&A cash outflows** — SkyWater alone is a $1.8B deal — which can consume the balance sheet far faster than operations, and (b) **dilution**, given SBC of ~$128M/quarter and a history of large equity raises. **Bottom line: IonQ won't run out of cash soon; shareholders will keep getting diluted.**

**4) The 3 most important changes:** (i) revenue reached real scale and guidance was raised (genuinely better); (ii) gross margin collapsed to ~24% and cash burn ~doubled (genuinely worse); (iii) the GAAP profit is a warrant-driven mirage masking a ~$255M underlying loss and heavy dilution.

**Impact on (non-existent) thesis:** No change to the exclusion. The quality screen stands — **no metric improved**; the growth is real but purchased with margin, cash and shares.

**Next catalysts to watch:** (a) **SkyWater acquisition close** (Q2/Q3 2026) — size, cash-vs-stock mix, and margin/foundry economics; (b) **gross-margin trajectory** — does it recover as software/cloud mix returns, or is ~24% the new normal; (c) **Q2 2026 print (guided $65–68M)** and whether adjusted EBITDA loss stops widening; (d) technical proof-points on the Walking Cat fault-tolerance roadmap (256 → 10,000 qubits).

**If you already hold:** Outside this framework's mandate (it would never have initiated). Objectively: this is a **position-sizing / risk-tolerance** decision, not a fundamentals decision — the fundamentals say *avoid on quality*; a holder is expressing a venture bet on 2028–2030 quantum fault tolerance and must accept ongoing dilution and −$300M+/yr burn as the cost of the option.

---

### Sources
- IonQ Q1 2026 Form 8-K / press-release exhibit (ionq-ex99_1, SEC EDGAR) — quoted via search (host blocked this session)
- IonQ Q1 2026 Form 10-Q (ionq-20260331, SEC EDGAR) — quoted via search (host blocked)
- IonQ Q1 2026 Investor Update deck (q4cdn) — quoted via search (host blocked)
- IonQ FY2025 Form 10-K (ionq-20251231, accession 000119312526071562) — anchor figures
- Zacks / Yahoo Finance ("IONQ Stock Falls on Q1 Earnings Miss, Revenues Beat"), Futurum, Quantum Computing Report, The Quantum Insider, StockTitan (8-K & 10-Q briefs), Investing.com (slides & transcript brief), tickeron/247wallst (consensus)
- IonQ July 2025 Form 424B5 (J.P. Morgan offering — Series B/pre-funded warrants origin)
- Recompute/valuation: `tools/financial_rigor.py` (market cap 0.03% dev; P/S 141×/98×/69×; runway; SBC ratio)
- Anchor file: `reports/IonQ/data-snapshot.md`; screen: `reports/IonQ/IonQ-quality-screen-20260705.md`

*Objectivity note (CLAUDE.md): every figure carries a source; facts and estimates are separated (`[estimate]`/`[flag]`); both bull and quality-investor readings are shown; genuine limits (blocked primary hosts, unread footnotes/Q&A) are flagged as "insufficient data" rather than filled with guesses. No preset stance — the "avoid on quality" conclusion falls out of the data, not a prior.*
