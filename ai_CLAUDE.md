# AI Berkshire - AI Memory File

> This file records the project knowledge, user preferences, and historical decisions that Claude has accumulated while collaborating with the user, for reference in later sessions.

## User profile

- Investment style: value investing, concentrated high-conviction holdings, focused on China internet + consumer + AI.
- Research preference: direct and sharp, no filler; wants clear conclusions, not both-sides hedging; data must be accurate.
- Use case: personal investment-decision support, while also promoting this project as an open-source product.

## Project evolution history

### April 7-9, 2026 (first research batch + framework refinement)

**Research completed:**
1. `/investment-team Pinduoduo` - the first complete 4-agent parallel study, composite score 3.4/5.
2. `/investment-checklist` on 7 companies - Kweichow Moutai, Tencent, NVIDIA, Meituan, Pinduoduo, Pop Mart, Kuaishou.
3. Master holdings tracking - latest 13F for Buffett / Li Lu / Duan Yongping + PDD cost-basis analysis.
4. Deep re-assessment of 5 companies including Meituan (the user challenged the initial assessment).

**Corrections driven by user feedback:**
- Meituan changed from a fail to a conditional pass - the user pointed out: waiting for earnings to recover before buying is too late; 200 billion couldn't break it = a real moat.
- NVIDIA changed from unclear to a conditional pass - AI capex is still accelerating, Jevons Paradox.
- Kuaishou changed from unclear to a conditional pass - Kling AI is underrated, Sora was shut down.

**Key lessons:**
- Do not apply the checklist mechanically; exercise independent judgment.
- "Wait for earnings to recover before buying" is a logical fallacy - the share price prices it in ahead of time.
- A competitor spending more and still gaining no ground = the best evidence of a moat.

### Skill-system evolution

**V1 (5 skills) - covering pre-buy research:**
- investment-research, investment-team, investment-checklist, industry-research, private-company-research

**V2 (9 skills) - completing the post-buy workflow:**
- Added: earnings-review, thesis-tracker, portfolio-review, management-deep-dive.
- Fixed over 2 rounds of self-validation: unified paths, completed tool invocations, parallel collection, anti-bias mechanisms, quantitative scoring formulas.

## Core selling points (already reflected in the README)

1. **Forces a conclusion, no equivocation** - pass / fail / gray, with a concrete price range.
2. **Four-master perspectives in tension** - not a division of labor but mutual challenge, creating real conflict and tension.
3. **Structured anti-bias mechanisms** - A/B/C information-richness rating, Munger inversion, quick veto, anti-consensus.
4. **Financial-data precision** - Decimal exact computation, hand-checked market cap, multi-source cross-validation.
5. **Reproducible research process** - same input -> structurally consistent output, supporting cross-company comparison and longitudinal tracking.
6. **Multi-agent parallel depth** - 4 agents each search + analyze independently, 4x the information.
7. **Live-trading validation** - two-year cumulative gain of 1.46 million, beating the index by 40-50 percentage points in a row.

## User preferences and working habits

- **Report language**: English.
- **Pushing to GitHub**: usually requested once research is done; proactively ask.
- **Git operations**: the remote often has new commits (the user may also be editing elsewhere); always `git pull --rebase` before pushing.
- **Attitude toward mistakes**: point them out directly, no need to soften. The user will challenge the AI's judgment; when that happens, seriously re-assess rather than defend.
- **Do not over-summarize**: the user can read the diff; no need to restate what was done after every operation.
- **Research depth**: prefer to take the time and get it deep and accurate rather than being fast and sloppy.

## Known issues and to-improve

- Some early files under reports/ have non-standard naming (mixed Chinese and underscores); to be unified into English hyphenated format later.
- Some early reports (e.g. Tencent-Holdings-investment-research.md) use the old naming and have not been migrated.
- The actual coverage of the financial_rigor.py tool needs to be validated during skill execution.
- The output examples in the README are illustrative and should later be replaced with excerpts from real reports.
