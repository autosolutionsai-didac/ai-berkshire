---
name: investor-onboarding
description: Investor onboarding and intake. Profiles the investor (capital, horizon, risk tolerance, tax wrapper, market access, exclusions), derives an allocation frame from that profile, researches candidates that fit it, and on explicit approval hands them to the deep-research pipeline. Use when someone asks "where should I start", "help me start investing", "what should I buy with X", or wants candidates matched to their own constraints rather than to a named company or industry.
---

# Investor Onboarding: From "who are you" to "here is what to research"

Profile the investor described in $ARGUMENTS, derive an allocation frame from that profile, and research candidates that fit it.

**Supported input formats**:

| Input | Behavior |
|------|------|
| `/investor-onboarding` | Mode detect. No profile file exists → **Create** (run the intake). Profile exists → **Use** (confirm it in one line, skip the intake, go straight to research) |
| `/investor-onboarding update` | **Update** mode. Load the profile and ask only what has changed |
| `/investor-onboarding reset` | Archive the profile to `reports/investor-profile-{YYYYMMDD}.md`, then Create from scratch |
| `/investor-onboarding amount=50000 GBP; horizon=12y; risk=balanced; wrapper=ISA; residence=UK` | **Prefilled**. Parse the record, ask zero questions, go straight to the allocation frame |
| `/investor-onboarding label=spouse ...` | Any of the above against `reports/investor-profile-spouse.md` |

> "Risk comes from not knowing what you are doing." -- Warren Buffett
>
> "Knowing what you don't know is more useful than being brilliant." -- Charlie Munger

## Design concept

This toolkit answers "is this company any good?" extremely well and "is this right for me?" not at all. Every other skill takes a company, an industry or a theme as its input. None of them knows the investor. Three symptoms of the same hole:

- `skills/portfolio-review.md` explicitly **refuses** to name candidates and delegates elsewhere. Nothing picks that up.
- `skills/berkshire-skill.md` Phase 7 emits **all three** position-sizing tiers because it does not know who is reading.
- `skills/industry-funnel.md` hard-codes its final three as "1 stable + 1 growth + 1 high-elasticity" -- a fixed risk profile presented as neutral.

This skill fills that hole, and it does so by **parameterising the existing research skills, not by duplicating them**. Candidate generation already exists four times over in `quality-screen`, `industry-funnel`, `industry-research` and `bottleneck-hunter`. What did not exist is a profile to point them at.

## Scope and boundary

- This skill produces **research candidates for you to evaluate**, not instructions to act.
- It expresses allocation as **percentages of a frame**. It never states a currency amount to invest, a number of shares to buy, or a date to trade.
- It never connects to a broker and never places an order.
- Tax and eligibility notes describe **structural mechanics** (how withholding works, what a wrapper permits). Rates and rules change -- verify every one against a current source at run time, and never hardcode a rate as fact.
- If you are running this **for anyone other than yourself**, personal recommendations on specific securities are a regulated activity in most jurisdictions. Do not.

## Execution process

### Step 0: Prepare

1. Run `date` to establish today. Pin the run date once and reuse it for every dated filename in this run.
2. Detect the mode from the table above.
3. Read `reports/investor-profile.md` if it exists. Read `reports/portfolio-latest.md` if it exists -- that file is owned by `/portfolio-review` and describes positions actually held, which is different from a profile.
4. In Use mode, restate the profile in one line and ask only "still accurate?" before proceeding. Never re-run a full intake on a returning user.

### Step 1: Intake

Ask only what you do not already know. Anything supplied in `$ARGUMENTS` or already recorded in the profile is never asked again.

**Interaction tiers -- follow the first one that applies:**

- **Tier A -- `AskUserQuestion` is available.** Ask in four batches, at most four questions per call. Keep headers short. Always leave the free-text path open.
- **Tier B -- it is not available** (Codex, headless, or any non-interactive run). Print the **entire questionnaire once as a single numbered block**, then stop and wait for one reply. Parse whatever comes back -- `1b 2a 3c`, prose, or partial. Never turn this into thirteen sequential questions: in Codex that is unusable and in a non-interactive run it deadlocks.
- **Tier C -- prefilled or existing profile.** Ask nothing.

**Batch 1 -- Capital and horizon**

| # | Question | Header | Options |
|---|------|------|------|
| 1 | How much are you looking to put to work in this portfolio? | Amount | Under 10k / 10k-100k / 100k-1M / Over 1M |
| 2 | Is this a lump sum, or regular contributions? | Cadence | Lump sum / Monthly / Both / Reallocating money already invested |
| 3 | When would you realistically need this money back? | Horizon | Under 3 years / 3-7 / 7-15 / 15+ |
| 4 | What have you invested in before? | Experience | First portfolio / Funds only / I pick individual stocks / Professional |

**Batch 2 -- Risk, stated and revealed**

| # | Question | Header | Options |
|---|------|------|------|
| 5 | In the last big drawdown you lived through, what did you **actually do**? | Last drop | Bought more / Held / Trimmed / Sold out / Wasn't invested yet |
| 6 | How far could this portfolio fall from its peak before you would change your mind about the plan? | Drawdown | ~10% / ~25% / ~40% / 50%+ |
| 7 | If this money halved and stayed there for three years, what breaks? | Capacity | Nothing / A goal is delayed / Real hardship / It is my emergency fund |
| 8 | What is this portfolio for? | Objective | Income I can spend now / Total return / Growth, no income needed / Preserve capital |

**Batch 3 -- Constraints that are yours, not the market's**

| # | Question | Header | Options |
|---|------|------|------|
| 9 | Which account(s) will hold this? (multi-select) | Account | ISA / SIPP / 401k or IRA / Taxable brokerage / PEA or assurance-vie / Other |
| 10 | Where are you tax-resident, and what currency do you think in? | Tax base | Free text, e.g. `UK / GBP` |
| 11 | What can your broker actually buy? (multi-select) | Access | UK-EU listings (UCITS) / US-listed / HK / A-shares via Connect / Japan-Korea / Not sure |
| 12 | Anything you will not own? (multi-select) | Excludes | Nothing / Tobacco, gambling, defence / Fossil fuels / Alcohol / Other |

**Batch 4 -- Existing book**

| # | Question | Header | Options |
|---|------|------|------|
| 13 | What do you already own, roughly? Tickers and rough weights are enough. "Nothing" is a fine answer | Holdings | Free text |

### Step 2: Hard gates

Apply these **before** any research. They work like the elimination gate in `skills/quality-screen.md` and the integrity veto in `skills/investment-checklist.md`: they stop the run rather than colouring it.

| Trigger | Action |
|------|------|
| Q3 is under 3 years, **or** Q7 is "emergency fund" or "real hardship" | **Halt.** State plainly that equity research is the wrong tool for this money, and produce no shortlist. Offer to continue only for a clearly separate long-horizon pot |
| The user asks for leverage, margin, options or CFDs | Out of scope. Say so once and do not proceed with them |
| Q1 is under ~10k **and** Q4 is "first portfolio" | Not a halt. Force the frame to **100% ETF core, no single stocks**, and give the honest reason: below that size, per-trade costs and the research time per name are not recoverable. Gate 2 in Step 7 then does not apply |

### Step 3: Derive the risk band

Compute three separate inputs and take the **minimum**, never the average:

| Input | Source |
|------|------|
| Revealed | Q5 -- what they actually did |
| Stated | Q6 -- what they say they can take |
| Capacity | Q7 -- what they can afford to lose |

If the three disagree by more than one band, **surface the contradiction in the output** rather than resolving it silently. For example: "You describe yourself as aggressive, but you sold out in the last drawdown. This frame is built on the behaviour, not the self-description -- tell me if you disagree."

Without the minimum rule this skill becomes a flattery machine that talks people into risk they have already demonstrated they cannot hold.

### Step 4: Build the allocation frame

| Band | Equity / cash | Positions | Max single | ETF core | Stock satellite | Geography | Skills permitted |
|------|------|:----:|:----:|:----:|:----:|------|------|
| Defensive | 50-70 / 30-50 | 3-6 | 15% | 85-100% | 0-15% | Home + global developed | `/etf-review` only |
| Balanced | 75-90 / 10-25 | 6-10 | 20% | 60-80% | 20-40% | Global developed + up to 15% EM | `/etf-review`, `/berkshire-skill` |
| Growth | 85-95 / 5-15 | 8-12 | 25% | 40-60% | 40-60% | Global + up to 25% EM | + `/industry-funnel`, `/quality-screen` |
| Aggressive | 90-100 / 0-10 | 8-15 | 30% | 20-40% | 60-80% | Unconstrained within access | + `/bottleneck-hunter` |

`/bottleneck-hunter` is gated to Aggressive deliberately -- that skill is explicitly small-cap and high-risk, and is currently offered to every user equally.

**How the frame parameterises the existing skills:**

| Skill | What the profile injects | What it does not change |
|------|------|------|
| `/quality-screen <universe>` | The universe string, built from Q11 access plus theme. Exclusions applied to the candidate list before launching | The 7 metrics. They are absolute company-quality tests, not preferences |
| `/industry-funnel <industry>` | Risk band as an override on the final-3 composition; market scope narrowed from its default to Q11 | The funnel layers |
| `/etf-review <fund>` | Wrapper, tax residence, base currency, existing holdings for overlap | The rubric |
| `/berkshire-skill <name> quick` | Nothing at invocation. Phase 7 reads the profile from disk | Any phase |
| `/portfolio-review <holdings>` | Nothing. It owns the holdings file; this skill hands off to it | Everything |

Write the profile file now, before any research. Schema is in the output section below.

### Step 5: Research

1. **Market context pass.** One bounded burst: where the cycle sits, what cash yields in the base currency, current valuations for the geographies in scope. Timeboxed. This is not a substitute for `/industry-research`.
2. **Core candidates.** 2-4 funds derived from Q9, Q10 and Q11 constraints. These go to `/etf-review`.
3. **Satellite candidates.** Themes or industries consistent with the frame. Run `/quality-screen <geography + theme>` or `/industry-funnel <industry>` with the risk-band override. Apply exclusions **before** launching so no research is wasted.
4. **Cap the stock shortlist at 5.** Follow the data standard in `skills/financial-data.md`: two independent sources for every figure.

**Never put profile data into a search query.** The profile holds amounts, account types and residence. Search for "UCITS global equity ETF accumulating", never "best ETF for my 250k ISA".

### Step 6: Gate 1 -- shortlist approval

1. Write the shortlist into the profile with `Status: pending approval` on every row **before** presenting it. The gate must survive a lost session.
2. Present the shortlist table and the estimated wall-clock cost of the next step. Each `quick` triage is a multi-search run; a full `/berkshire-skill` run is well over an hour.
3. **End the turn. Make no further tool calls.** Do not launch `/etf-review` or `/berkshire-skill` in the same turn as the shortlist, under any circumstances.
4. The user's next message is the gate. Approval means an explicit go, a named subset, or an edit. **Silence, "looks good so far", or an ambiguous reply is not approval** -- re-ask once, naming the candidates.
5. On approval, set each row's `Status` to `approved` or `rejected` and record the decision in the run log.

### Step 7: Handoff, then Gate 2

Fork by asset type. **This is a rule, not a preference:**

- **Funds** go to `/etf-review`. Never to `/berkshire-skill` -- running seven company accounting ratios against a fund produces confident nonsense.
- **Stocks** go to `/berkshire-skill <name> quick`.

Run both as background subagents, following the execution model in `skills/berkshire-skill.md`: each subagent writes its file and returns only 3-5 key findings; verify the file actually landed and relaunch if it did not.

Present the triage table, then **Gate 2** with the same mechanics as Gate 1.

**Gate 2 does not apply when the frame is ETF-only** (Defensive band, or the sub-10k floor from Step 2). Say so plainly rather than inventing single-stock candidates to satisfy the flow.

### Step 8: Full runs and close the loop

Run `/berkshire-skill <name>` in full on the selections, one at a time. Then:

- `/portfolio-review` once positions exist -- it owns `reports/portfolio-latest.md`.
- `/thesis-tracker` per holding, to write the sell conditions before buying rather than after.

Append every action to the run log.

## Output format

Write to `reports/investor-profile.md` (or `reports/investor-profile-{label}.md`):

```markdown
# Investor Profile

**Created**: YYYY-MM-DD | **Last updated**: YYYY-MM-DD | **Revision**: N

## Profile record

​```text
amount_band: 100k-1M
contributions: monthly
base_currency: GBP
tax_residence: UK
wrappers: ISA, SIPP
horizon_years: 12
objective: growth
risk_band: Balanced
stated_max_drawdown: 40%
revealed_behaviour: held through the last drawdown
capacity_for_loss: a goal is delayed
market_access: UK-EU UCITS, US-listed; no US-domiciled ETFs
exclusions: none
experience: funds only
existing_holdings: see reports/portfolio-latest.md
​```

## 1. Intake answers
| Question | Answer | Source |
|------|------|------|
(source is asked / prefilled / assumed -- assumed answers must be flagged to the user)

## 2. Risk band derivation
| Input | Value | Band |
|------|------|------|
| Stated | | |
| Revealed | | |
| Capacity | | |
| **Band = min()** | | |

Contradictions surfaced: ...

## 3. Allocation frame
(the instantiated row from Step 4)

## 4. Research parameters
| Downstream skill | Parameters passed |
|------|------|

## 5. Candidate shortlist
| Candidate | Type | Role in frame | Proposed weight | Why it fits your constraints | What would rule it out | Status | Decided on |
|------|------|------|------|------|------|------|------|

## 6. Run log
| Date | Action | Result |
|------|------|------|

## 7. Review cadence
Next review: ... | Triggers for an earlier one: ...
```

Weights are **percentages of the frame**. Never a currency amount, never a share count, never a date to buy.

---

## Notes

- **Ask for behaviour, not self-description** -- everyone says they would buy the dip. Q5 asks what they did in a real episode; the band is the minimum of stated, revealed and capacity.
- **Never re-interrogate a returning user** -- Use mode confirms in one line and moves on.
- **The profile is the most sensitive file this toolkit writes.** It lives under `reports/`, which is gitignored and local-only. Never commit it, and never put its contents into a search query.
- **Percentages, not amounts** -- a verdict about an asset is research; an instruction about a person is advice. This distinction is what keeps the skill on the right side of the line.
- **Two gates, both hard** -- the run stops at each one. A gate that the model talks itself through is not a gate.
- **This skill does not generate research** -- it points existing skills at a profile. If you find yourself writing screening logic here, it belongs in `quality-screen` or `industry-funnel` instead.
- **Output quality inherits upstream condition** -- `skills/industry-funnel.md` is machine-translated and partly corrupted. Funnel-derived candidates are capped by that file's quality until it is rewritten.
- **Tax rules rot faster than equity research**, and a tax mistake is irreversible in a way a bad stock call is not. State the mechanic, look up the rate.
