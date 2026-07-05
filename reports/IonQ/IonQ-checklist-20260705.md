# Buffett Six-Gate Pre-Buy Checklist — IonQ, Inc.

**Company:** IonQ, Inc. — **IONQ / NYSE / USD**
**Run date:** 2026-07-05
**Price anchor:** $49.12 (close 2026-07-02) · ~373.27M shares · **market cap ≈ $18.34B** (recomputed, 0.03% deviation — `financial_rigor.py`)
**Information-richness rating: A** (NYSE-listed, full SEC filings, ~13–17 analyst coverage; all anchors cross-validated ≥2 sources)

> "The first rule of investing is don't lose money. The second rule is don't forget the first." — Warren Buffett

> **Grounding & scope (disclosed, not buried):** This checklist is built directly on the completed IonQ work in `reports/IonQ/` — `data-snapshot.md`, `IonQ-quality-screen-20260705.md` (**EXCLUDED**, 5/7 metrics fail), the four-master team synthesis `final-report.md` + files `01`–`04` (**composite ★★ 1.75, AVOID**), `IonQ-management-20260705.md` (**★★**, integrity "not a clear yes"), and `IonQ-earnings-2026Q1.md` (revenue beat / profitability miss; warrant-gain artifact). It does not re-derive facts from scratch and does not contradict those files. Written with **no preset stance**: data first, logic second, conclusion last.

> **AI-research-bias warning (Grade A → the "consensus trap"):** IonQ is information-rich, so every metric *looks* clear — but clarity of *facts* is not the same as *investment certainty*. The disclosure is abundant; the uncertainty lives in the **technology and the business model**, where more data does not help. Analyst consensus (~$63–69 target, Buy/Strong Buy) prices *optionality*, not owner-earnings — a legitimate but different lens, flagged here rather than adopted.

---

## 1. Six-gate scorecard

| # | Gate | Rating | One-line verdict |
|---|------|:------:|------------------|
| 1 | Circle of competence | **★★** | Business *mechanism* is explainable; the 10-year *outcome* (useful fault tolerance) is not forecastable — certainty near-zero |
| 2 | Good business (economics) | **★** | ROE deeply negative, FCF negative every year since listing, gross margin collapsing (40.4%→23.8%); "FCF persistently negative" clause = floor |
| 3 | Moat depth | **★★** | Only 1 of 5 classic moats holds (tech/IP, unproven & partly *acquired*); no pricing power; scale economics negative |
| 4 | Management trustworthy | **★★** | Capable, physics-literate operator; but integrity **"not a clear yes"**, heavy insider cash-out, say-on-pay 95%→54%, ISS 9/10 |
| 5 | Margin of safety | **★** | 141× P/S, 117× EV/revenue; base-case fair value ~$23 vs $49.12 price = ~**52% overvalued**; **no margin of safety** |
| 6 | Emotional discipline | **★★** | Buy impulse is FOMO/story-driven; fails the "5-year trading-suspension" test; only disciplined hold is a small, losable option |

**Composite (arithmetic): (2+1+2+2+1+2)/6 = 1.67 → ★★.** Consistent with the four-master team's ★★ (1.75). *The binding constraints are Gate 2 (no economics) and Gate 5 (no margin of safety), both at the ★ floor.*

---

## 2. Core data snapshot (USD)

| Metric | FY2025 | Q1'26 / latest | Read |
|---|---|---|---|
| Revenue | $130.02M (+202%) | $64.7M (+755% YoY) | Genuine triple-digit scaling |
| Gross margin | 40.4% | **23.8%** | ⬇ collapsing as low-margin hardware dominates |
| Operating income | −$633.72M | −$271.5M | Widening in dollars |
| GAAP net income | −$510.38M | **+$805.4M** ⚠️ | Q1 "profit" = ~$1.06B non-cash warrant gain (artifact; *rises when the stock falls*) |
| Net income ex-warrant `[est]` | — | ≈ −$255M | The real number |
| Operating cash flow | −$283.19M | −$151.0M | Burn ~doubled |
| Free cash flow | −$299.60M | ~−$160M `[est]` | Negative every year 2021–2025, accelerating |
| Stock-based comp | — | $128.52M (~199% of revenue) | Dilution engine; SBC exceeds revenue |
| Cash + investments | ~$3.1B | ~$3.1B | Raise-funded (~$3.35B equity FY2025), not earned; ~5-yr runway |
| Shares outstanding | ~193M → | ~373.27M | +93% since 2021 SPAC listing |
| Market cap / P/S / EV-rev | — | **$18.34B / 141× / 117×** | No absolute-value anchor |
| FY2026 guide (raised) | — | $260–270M rev; adj-EBITDA −$310M to −$330M | Loss guided to *widen* |

*ROE: deeply negative every year (FY2025 net margin ≈ −393%). No dividend. No meaningful PE/PEG/P-FCF (negative earnings & cash flow) — valuation by EV/revenue and scenarios, by design.*

---

## 3. Gate-by-gate detail

### Gate 1 — Circle of competence: ★★
- **How it makes money (one sentence):** IonQ builds and sells trapped-ion quantum computers, sells pay-per-use cloud access to them (via AWS/Azure/GCP), and sells quantum networking/sensing and government R&D — *understandable in mechanism*. **Not a hard veto** (you *can* explain the model).
- **10 years out:** near-zero certainty. Useful fault tolerance is a 2030–2040+ event on every credible roadmap (BCG); no system has reached it; the modality race (trapped-ion vs. superconducting vs. others) is unsettled.
- **Success variables:** (a) trapped-ion wins or co-wins the modality race; (b) IonQ's specific IP stays ahead of IBM/Google/Quantinuum; (c) the dilution-funded narrative holds long enough to reach payoff.
- **Read:** understandable *business*, unforecastable *outcome* — the rubric's ★★ "industry in upheaval, hard to foresee the future."

### Gate 2 — Good business: ★
| Metric | Value | Standard | Judgment |
|---|---|---|---|
| ROE (multi-yr) | Deeply negative every year | >15% | ❌ |
| Gross margin | 40.4% FY / 23.8% Q1'26 | >40% pricing power | ⚠️ Borderline & *deteriorating* |
| Free cash flow | −$299.6M FY; negative every year since listing | consistently positive ≈ net income | ❌ |
| Capex intensity | Low (~$16M FY25) | asset-light preferred | ✅ but irrelevant while OCF −$283M |
| Debt | Minimal | interest-bearing/NI <3yr | ✅ (equity-funded, not levered) |

**FCF has been negative every year 2021–2025 with the loss guided to widen** — this alone drops Gate 2 to the ★ floor ("FCF persistently negative"). Growth is substantially *bought* (stock-funded M&A) and *margin-financed*, not earned. Scale is *hurting* margins — direct evidence against operating leverage.

### Gate 3 — Moat depth: ★★
| Moat type | Present? | Evidence | Trend |
|---|:---:|---|---|
| Brand / pricing power | ⚠️ Weak | Best-known listed pure-play, but no price command; margin fell under volume | Not widening |
| Switching cost | ⚠️ Low | Some gate-set/cloud lock-in; but multi-vendor POCs are routine | Possibly higher *later* |
| Network effect | ❌ Absent | Cloud availability is distribution, not a two-sided network | — |
| Cost / scale | ❌ Negative | Gross margin 40.4%→23.8% as volume rose | Eroding |
| Technology / IP | ✅ Contingent | Trapped-ion IP + four-nines (99.99%) fidelity — real, but *acquired* (Oxford Ionics) & on prototype | Unproven as durable |

**$10B-competitor test:** Quantinuum (same modality, Honeywell-backed, arguably ahead) and IBM/Google (deeper pockets) are *already* doing exactly this. The one candidate moat is a **venture-stage technology option, not a proven economic moat.**

### Gate 4 — Management trustworthy: ★★
| Check | Assessment |
|---|---|
| Honesty (promise vs. delivery) | **"Not a clear yes."** Beats revenue/bookings guidance 5-for-5 (2021–25) — a real positive. But: documented 2020 "32 perfect qubits" overstatement (machine was ~11); physical-vs-logical qubit conflation ("eliminate Blackwell"); "no equity before 2028" pledge broken within 6 months; Scott Aaronson's public "wild misrepresentations… to governments" charge |
| Capital allocation | ★★ — genuine strength: raises struck at ~20–25% premiums (sold overvalued stock well). Offset: ~$2.5B mostly-stock M&A, several undisclosed prices, two off-thesis deals (Capella satellites, SkyWater foundry); revenue substantially *bought* |
| Shareholder orientation | ⚠️ Insiders one-directional sellers (de Masi ~$106M, Chapman ~$270.7M; group cut to <1%) — while the *scientist-founders held*. $89.6M CEO comp (217:1 ratio) at a company losing ~$510M |
| Owner mentality | Mixed — SPAC sponsor turned Chairman+President+CEO; both founders gone; churn-heavy (CFO/CRO turned over, CTO vacant ~1.5 yrs, 5 new directors in 3 yrs) |
| Governance | Single-class voting (✅ real mitigant); but say-on-pay 95%→64%→54%, ISS 9/10, CEO-owned Gulfstream leased back |
| Runs without CEO? | Operationally maybe; the *equity-markets narrative that funds the company* is de-Masi-dependent |

**Rubric placement:** ★★ = "has integrity or governance issues." **Not ★ = "serious integrity problems (hard veto)"** — the grounding reports deliberately stop at "concerning but not proven dishonest / not proven fraud." *(See integrity ruling in §6.)*

### Gate 5 — Margin of safety: ★
| Metric | Value | Judgment |
|---|---|---|
| PE (TTM) / Forward PE | n/m (negative/artifact earnings) | Meaningless — excluded by design |
| P/S | **141× FY2025** (~69× FY26 guided) | Severely rich |
| EV / revenue | **117× FY2025** (57.5× FY26 guided) | Severely rich |
| PB / Dividend / FCF yield | High PB; no dividend; **negative** FCF yield | No income anchor |
| Base-case fair value (team) | **~$23** vs $49.12 price | ~**52% overvalued** |

**Three-scenario (margin-of-safety gate).** The skill's `three-scenario` engine is PE-based; run on IonQ's *negative* EPS (−$1.37) it returns **nonsensical negative target prices** (Bull −$90, Base −$42, Bear −$10) — which is the tool *correctly* demonstrating that **a PE framework cannot value IonQ.** Per instruction, valuation is therefore anchored on the **EV/revenue-repurposed** three-scenario that the Buffett-lens file (`02`) ran and tool-verified ("EPS" = revenue/share, "PE" = terminal P/S):

| Scenario | Rev CAGR | Terminal P/S | Implied 2030 rev | Target price | Change |
|---|---|---|---|---|---|
| Bull | 50% | 30× | ~$987M | $79.3 | **+61.5%** |
| Base | 35% | 15× | ~$583M | $23.4 | **−52.3%** |
| Bear | 15% | 5× | ~$262M | $3.5 | **−92.9%** |

*Dilution overlay (~8%/yr → 0.68× over 5 yrs, tool-verified): realistic per-share ≈ Bull ~$54, Base ~$16, Bear ~$2.4 — dilution alone erases most bull upside.* The distribution is **violently asymmetric to the downside**: you need the near-perfect outcome merely to break even; ordinary disappointment loses 52–93%. **No margin of safety → ★ (severely overvalued).** If wrong at $49.12, the downside is permanent-loss-shaped; "if the price halved, would you add?" — only a venture-tolerant investor sizing it as a small option would, and only far cheaper (~$15–25).

### Gate 6 — Emotional discipline: ★★
- **FOMO?** High risk — a hot quantum name, +triple-digit revenue growth, constructive analyst chorus.
- **Buying only because someone recommended it?** Consensus is Buy — but on thesis/optionality, not owner-earnings.
- **If trading were suspended 5 years, could you accept it?** **No** — thesis hinges on a 2030–2040+ technology event with ongoing ~$320M/yr burn and dilution.
- **Buy thesis in <200 words?** Writable — but only as an explicit *speculation*, not a business-quality investment.
- **Read:** the only disciplined way to hold IonQ is a small, losable, option-sized slice; a full-conviction "investment" buy fails the discipline test.

---

## 4. Key risks (top 5)

1. **Dilution (near-certain, high severity):** +93% shares since 2021; SBC ~199% of revenue; ~79M-share warrant overhang; stock-funded M&A. Holders' claim shrinks every quarter — the true cost of ownership.
2. **No margin of safety:** 141× P/S; base −52%, bear −93%; even the bull barely clears today's price after dilution.
3. **Timeline / commercialization:** useful fault tolerance 2030–2040+; the burn-funded option can expire before the payoff arrives.
4. **Competition:** IBM, Google, and a directly-comparable, deeper-pocketed **Quantinuum** (same trapped-ion modality, IPO'd Jun 2026); hyperscalers own the customer relationship.
5. **Management integrity "not a clear yes" + revenue quality:** documented overstatements/promotional framing, heavy insider selling; disputed-but-unrebutted Wolfpack bookings-vs-funded ($54.6M "black hole") and margin collapse to 23.8%.

*Counter-argument (both sides, per objectivity rules): IonQ is the best-capitalized pure-play (~$3.1B, ~5-yr runway), first past $100M revenue, with real technical proof-points and a coherent vertical "quantum internet" stack; if trapped-ion reaches useful fault tolerance and its IP holds, today's $18B could look small against a $43–72B (2035) revenue pool. This is a legitimate venture thesis — but a payoff-distribution bet on the future, not a business-quality judgment today.*

---

## 5. Mirror test

> "I am buying IonQ at $49.12 per share, because:
> 1. The essence of this business is **building and selling trapped-ion quantum computers + cloud access + networking — I understand the *mechanism*, but NOT the 10-year *outcome* (useful fault tolerance);** ⚠️
> 2. Its moat is **only technology/IP, unproven and partly acquired, and is *narrowing* (margins collapsing under volume), not widening;** ❌
> 3. Management is **capable but promotional, with integrity "not a clear yes," and is *not clearly* trustworthy;** ❌
> 4. The current price equals a **~52% *premium* to base-case intrinsic value (~$23), *without* a margin of safety;** ❌
> 5. Even if I am wrong, the downside is **uncontrollable — base −52%, bear −93%, permanent-loss-shaped.**" ❌

**Result: FAIL.** Four of five sentences cannot be completed affirmatively. *"Cannot complete all 5 sentences = do not buy."*

---

## 6. Step-5 quick-veto list & integrity ruling

| Quick-veto item | Triggered? | Note |
|---|:---:|---|
| Cannot explain how it makes money | ❌ No | Model is explainable |
| **FCF negative 3 consecutive years, no improvement in sight** | ✅ **YES** | Negative every year 2021–2025; FY26 loss guided to *widen* |
| Management has an integrity stain | ⚠️ **Gray / qualified** | Documented 2020 overstatement, broken pledge, related-party jet, expert misrepresentation charge — a plain-language *stain*, but **not proven fraud** |
| Competitive advantage irreversibly eroded | ⚠️ Contingent | Not proven irreversible; but only-moat is unproven & scale economics negative |
| Relies on "next buyer pays more" (greater-fool) | ⚠️ Partial-YES | Price embeds a decade-away outcome; needs multiple/narrative to hold |
| Cannot bear it going to zero | ✅ YES for a full position | Only a small, losable slice survives this test |
| Main reason to buy is "everyone's buying / it's risen" | ⚠️ Largely YES | Buy case is substantially FOMO/story |
| Cannot write buy thesis in <200 words | ❌ No | Writable — but only as speculation |

**Integrity disqualifier — explicit ruling:** The **automatic ★1 management HARD VETO ("serious integrity problems / proven dishonesty") does NOT fire.** The grounding reports deliberately stop at integrity **"not a clear yes" / "concerning but not proven dishonest"** — Gate 4 is ★★, not ★. However, under the Duan/Buffett ordering ("if the first quality — integrity — is not a clear yes, the other two will kill you"), the unresolved-integrity flag is a **gray-zone stain that independently prevents a PASS** even before valuation is considered. It compounds, rather than causes, the failure.

**The checklist does not depend on the integrity call, however:** it FAILS on **two independent, unambiguous red lines** that require no resolution of the integrity question — (a) **Gate 5, no margin of safety** (the binding valuation red line), and (b) the **FCF-negative-3-years quick-veto.**

---

## 7. Conclusion

**❌ FAILED the checklist — 2/6 gates at the ★ floor; verdict AVOID.**

**Red lines triggered:**
1. **Gate 5 — margin of safety (binding):** 141× P/S, base-case fair value ~$23 vs $49.12 — ~52% overvalued, downside asymmetric (base −52% / bear −93%). *"Price is what you pay; value is what you get"* — here you pay for a decade-away maybe.
2. **Gate 2 / Step-5 FCF veto:** free cash flow negative every year since listing, loss guided to widen.
3. **Mirror test FAILED** (4 of 5 sentences uncompletable).

**Integrity disqualifier:** the standalone ★1 management hard veto **does not fire** (fraud unproven); integrity registers as a **gray-zone stain ("not a clear yes")** that compounds — not causes — the AVOID.

**This is not a Grade-C "insufficient data" gray zone.** IonQ is information-rich (Grade A); the data is abundant and points clearly to FAIL. The checklist is doing exactly its job — *screening out a bad choice*, not identifying the best one. IonQ may still appreciate as a thematic/venture bet — but that is a payoff-distribution decision on 2030–2040 fault tolerance, **not** an investment in a durable, cash-generating business clearing the six-gate bar. The Phase-1 quality-screen exclusion, the four-master AVOID, and this checklist all converge.

> "A great business at a fair price is superior to a fair business at a great price." — Charlie Munger. IonQ is *neither* a great business *nor* at a fair price on current fundamentals.
>
> "Buying a business is buying its future cash flows. If you can't see the cash, you're not investing, you're guessing." — Duan Yongping (paraphrase).

**Closing note — Buffett's first rule: "The first rule of investing is don't lose money."** At 141× sales, funded by 199%-of-revenue dilution, run by a promoter whose integrity is "not a clear yes," with a base-case ~52% below today's price, IonQ's payoff distribution is dominated by large-loss outcomes. The disciplined answer is **AVOID** — better to miss this than to be wrong in it.

---

### Objectivity & sourcing statement (CLAUDE.md)

- **Facts vs. opinion:** every figure carries a source/anchor; estimates tagged `[est]`; opinions labeled; both bull and bear shown on every core judgment; "insufficient data" stated where true (no clean revenue segment split disclosed; blocked primary hosts noted in the underlying files).
- **No preset stance:** the FAILED/AVOID verdict is derived from the data (Gates 2 & 5 at the ★ floor), not a prior.
- **Currency USD throughout; star ratings whole stars (1–5), no half-stars.**
- **Tool verification:** `financial_rigor.py` — market cap 0.03% dev; P/S 141×; EV/rev 117×; three-scenario (PE-based run confirmed n/m for negative EPS; EV/revenue-repurposed scenarios per file `02`); dilution 0.68×; SBC 198.6% of revenue.

### Sources (consolidated)
- `reports/IonQ/data-snapshot.md`, `IonQ-quality-screen-20260705.md`, `final-report.md`, `01`–`04`, `IonQ-management-20260705.md`, `IonQ-earnings-2026Q1.md`
- IonQ FY2025 10-K (SEC accession 000119312526071562); Q1'26 8-K/10-Q; ionq.com/roadmap
- stockanalysis.com / macrotrends (IONQ, RGTI, QBTS); Yahoo Finance; Motley Fool quantum coverage
- TAM/roadmaps: McKinsey Quantum Technology Monitor 2026; BCG (2024); IBM & Quantinuum roadmaps; Quantinuum IPO Jun 2026 @ $60
- Governance: DEF 14A 2026-04-30 & 2025-04-28; Form 4 filings; ISS QualityScore; scottaaronson.blog; Wolfpack Research (Feb 2026, disputed)
- Analyst targets: stockanalysis.com/forecast, MarketBeat, TipRanks (consensus ~$63–69)
