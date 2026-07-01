---
name: deep-company-series
description: "AI Berkshire skill: Deep Company Series: Dissecting One Company Across 8 Long-Form Essays. Source: skills/deep-company-series.md."
---

## Codex adapter note

This skill is generated from `skills/deep-company-series.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Commands that reference `~/ai-berkshire/tools/...` assume the repo is checked out at `~/ai-berkshire`; if needed, prefer the current workspace path.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Deep Company Series: Dissecting One Company Across 8 Long-Form Essays

Write an 8-part deep-dive long-form series for $ARGUMENTS, to be published on public channels (WeChat Official Account / Video Account, etc.). **The core IP is not "being able to write" but "being able to revise" — 99% of finance articles violate this skill's fact-checking standards.**

Reference sample: `reports/Tencent/Understanding-Tencent/`

---

## 1. When to Use

The user wants a "textbook-grade" deep study of a company, published publicly as a **long-form series**. Different from a single research note:
- 8 essays totaling roughly 120,000 characters, forming a complete loop from cognitive reset to decision framework
- Each essay stands on its own (suitable for standalone sharing), but a single valuation / management / price-judgment thread runs through all of them
- Written for readers "willing to spend 90 minutes to truly understand a company," not for brokerage clients

**When NOT to use this skill**: a single research note, a quarterly-earnings comment, or industry research — for those use `/investment-research`, `/earnings-review`, or `/industry-research`.

---

## 2. Series Outline Template (8 Essays)

| # | Title Template | Core Question | Word Count |
|---|---------|---------|------|
| 01 | You think you understand X — you don't | Cognitive reset: break 3 common illusions | 4,000-5,000 |
| 02 | X's moat — `<one-sentence business essence>` | How deep is the moat, will it still be there in 5/10 years | 6,000-8,000 |
| 03 | X's biggest profit engine — `<most profitable business>` | What is the core business, why is it durable | 6,000-8,000 |
| 04 | The other company hidden on X's books — `<hidden asset>` | Investment portfolio / subsidiaries / hidden value | 8,000-10,000 |
| 05 | In the AI (or current narrative) era, is X a winner or a loser | Era variable: break down AI impact by business line | 8,000-10,000 |
| 06 | Dissecting X's financials the Buffett way | Financial depth: gross margin / FCF / ROE / SBC | 8,000-10,000 |
| 07 | `<management quote>` — is X's management worth entrusting | Capital-allocation discipline + integrity test + succession | 8,000-10,000 |
| 08 | What price is worth buying, what signal forces a sell (series finale) | DCF three scenarios + red-line checklist + position-sizing framework | 10,000-12,000 |

Add a `00-series-overview.md` as a table-of-contents index; not published.

---

## 3. Writing-Style Guidelines

### Tone

- **Direct, sharp, no fluff** — the first sentence gives a number or a counterintuitive conclusion
- **Value-investing framework** — Buffett / Munger / Duan Yongping / Li Lu perspectives woven in (but don't pile on quotes)
- **No preset stance** — lay out the data first, then reason, then reach a conclusion
- **Present both sides** — every core judgment carries a "but on the other hand..." counterpoint
- **WeChat-Official-Account feel** — the first 18-20 characters must stand on their own (mobile preview)

### Banned Words

| Banned | Reason | Replacement |
|------|------|------|
| obviously / inevitably / definitely | subjective absolutism | data shows / evidence indicates |
| I think / I feel | subjective tone | delete, or change to "by this framework" |
| textbook-grade / stroke of genius | clickbait praise | describe the concrete fact |
| severely mismatched / severely undervalued | strong subjective words | give a specific discount percentage |
| perfect / flawless | one-sided judgment | add a counter-observation |

### Title Style

- Use a **contrast number** or **counter-consensus conclusion** as the hook ("7 failed challenges in 15 years," "annual pay of RMB 42.92M is 0.0017% of profit")
- Keep the subtitle neutral and content-summarizing ("— `<essence judgment>`")
- **Avoid clickbait metaphors**: "mini-Buffett," "the Chinese X," "GOAT" — all off-limits
- Use terminology familiar to professional readers ("Berkshire" rather than "Buffett," company names over personal names)

---

## 4. Rigorous Fact-Check Checklist (Core IP)

### "False-Precision" Traps to Watch for Before You Even Write

1. **Probability-weighted expected value**: calculations like `30% × A + 50% × B + 20% × C = expected +X%` are almost all garbage — the probability allocation is purely subjective and gives the reader a false sense of precision. **Only list scenarios + trigger conditions + direction; do not compute a weighted expectation.**
2. **Third-party MAU/share estimates**: QuestMobile / Qimai / CBNData and others vary enormously in methodology (they can differ 2-3x at the same point in time). **Use only the two most credible comparisons as an anchor; describe the rest qualitatively.**
3. **Linear extrapolation of historical growth**: `2025 +33% × 5-year CAGR → 2030 X` is financially illiterate forecasting. **Scenario assumptions + high/low range + it is not a promise.**
4. **Undisclosed shareholding percentages**: for private companies like ByteDance or Halti, stakes are **never publicly disclosed**. **Give a range and mark it "unknowable."**
5. **Strong attribution**: a competitor's failure = because of X. List all the multiple causes; **this piece does not do single-cause attribution.**

### The 7 Checks You Must Run When Revising

```
□ 1. Cross-essay number consistency: total market cap, Non-IFRS net profit, key stakes % aligned across the whole series
□ 2. Metric labeling: which is used where — Non-IFRS / GAAP / Non-IFRS-SBC / FCF — clear throughout
□ 3. Double-counting scan: consolidated subsidiaries are not in the "investment portfolio," SOTP is not counted twice
□ 4. Cross-comparison fairness: no "core-business PE (ex cash + portfolio)" vs "peer PE (not ex)"
□ 5. Delete all probability weighting: see the item above
□ 6. Soften all absolutist phrasing: grep "obviously|inevitably|severely|textbook|perfect"
□ 7. Third-party data source labeling: every non-financial-report figure is followed by "(source: X)"
```

### Model Preferences

Before writing, **list the known hard-error risks first**:
- Historical return multiple: must use the cumulative-invested basis (e.g. Riot is 33x, not 58x)
- Shareholding percentage: must use the latest Futu / financial-report basis (e.g. Tencent holds 1.5% of Meituan, not 6.4%)
- "Dividend-in-specie" accounting treatment: deemed-disposal gains are recognized on the declaration date under IFRIC 17 (e.g. JD in 2021, Meituan in 2022 but the amount is small)
- Total shares will rebound: SBC granted concentrated at the start of the year makes the share count rise short-term

---

## 5. Execution Flow

### Phase 1: Research (complete before writing essays 01-02)

1. Read the company's last 5 years of annual reports and the latest quarterly report
2. Read at least 3 independent sell-side research notes (find consensus + counter-consensus)
3. Use `/investment-team` or `/investment-research` to first generate an internal research draft
4. Confirm the core thesis of all 8 essays with the user (avoid finishing the writing only to find the direction was wrong)

### Phase 2: Writing (write in order 01→08, no skipping)

- After finishing each essay, save it to `reports/{Company}/Understanding-{Company}/0X-XX.md`
- Do not push to GitHub immediately — wait for the user's review
- Revise after the user gives revision comments
- Only git push once revisions are done

### Phase 3: Cross-Essay Consistency Scan (after all 8 essays are written)

Dispatch Explore agents to scan the 8 essays in parallel for the following checks:
1. Whether the same figure (market cap, net profit, shareholding percentage) is consistent across essays
2. Whether the same term (FBS, SBC, Non-IFRS) is explained on first appearance
3. Cross-references: whether essay 02's "see essay 06 for details" actually corresponds
4. Whether the key-points recap matches the body text in figures

### Phase 4: Final Pre-Publish Check

```bash
# Must grep locally once before pushing (per ai-berkshire privacy rules)
grep -r "linxuan\|/Users/\|<user's company codename>" reports/ | head
```

Only after confirming everything is clean, run `git pull --rebase && git commit && git push`.

---

## 6. Revision-Handling Flow

When the user gives revision comments, handle them in this order:

### 1. Fact-check first (do not edit directly)

If the user says "X data is wrong," first use Bash/Read to find the original data and cross-verify:
- Check the same company's earnings / financial-report reports in the ai-berkshire project
- Check Futu / official disclosures
- Provide a three-way comparison of "what the user said vs. what I found vs. what I used before"

### 2. Judge the Revision Level

| Level | Type | Handling |
|------|------|------|
| 🔥 Hard error | wrong number, wrong attribution, wrong metric basis | must fix, no hesitation |
| ⚠️ Subjectivity | strong subjective words, absolutism, clickbait metaphors | soften or delete |
| 🔬 Granularity | source labeling, metric refinement | lower priority, balance against readability |
| ❓ Unreliable | large discrepancy in third-party estimates | **deleting is safer than fixing** (explicit user instruction) |

### 3. Linked Checks After Revising

When you fix one spot, first think "where else references this number/concept." Examples:
- Changed total market cap → update PE / core-business PE / discount / FCF Yield across the whole series
- Changed shareholding % → update the TOP 10 ranking + historical-shareholding table + trim list
- Changed a metric basis/definition → update the first definition + subsequent references + key-points recap

### 4. Report Immediately After Pushing

```
Push succeeded (commit hash).
Summary of [N] revisions [with table]:
- What was changed
- What was changed in linkage
- What was not changed

Awaiting instructions for the next step.
```

---

## 7. What This Skill Does NOT Do

- **Does not make the investment decision for the reader** — every essay ends with "this does not constitute investment advice"
- **Does not forecast the stock price** — only gives "scenarios + trigger conditions"
- **Does not compute a weighted "expected annualized return"** — subjective probability allocation misleads the reader
- **Does not write "big-name investor X also holds it"** — using someone else's position to back your own judgment is anti-value-investing
- **Does not force all 8 essays** — if an essay lacks enough standalone content (e.g. a company's management is not distinctive enough), merge it into another or reduce the essay count

---

## 8. Compliance and Privacy

- All public reports **use only public information** (financial reports, official disclosures, brokerage research, well-known third-party institutions)
- Do not use any **user personal information** (company codename, internal IM, undisclosed position information)
- Before pushing, must grep-scan for privacy fields such as `linxuan` / `/Users/` / the user's company codename (see `~/.claude/projects/-Users-linxuan/memory/feedback_privacy_upload.md`)
- Public attribution follows the user's multi-layer identity strategy; do not mix identities

---

## One-Line Summary

**The core ability to write the "Understanding X" series ≠ writing well, but revising strictly** —
89% of long-form finance pieces die from false-precision numbers, subjective weighted expected values, and absolutist phrasing. This skill exists precisely to flag all these pitfalls: avoid them before writing, and scrub them clean afterward.
