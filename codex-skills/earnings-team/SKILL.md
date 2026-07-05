---
name: earnings-team
description: "AI Berkshire skill: Earnings Deep-Read Team: Four-Master Parallel Interpretation + WeChat Publishing. Source: skills/earnings-team.md."
---

## Codex adapter note

This skill is generated from `skills/earnings-team.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Commands that reference `~/ai-berkshire/tools/...` assume the repo is checked out at `~/ai-berkshire`; if needed, prefer the current workspace path.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Earnings Deep-Read Team: Four-Master Parallel Interpretation + WeChat Publishing

Conduct a team-based earnings deep-read (earnings review) analysis of $ARGUMENTS. Four masters interpret the earnings report in parallel, an editor polishes it into an article, a reader reviewer safeguards quality, and the final output is a WeChat article that can be published directly.

**Supported input formats**: `Company Quarter`, e.g., `Tencent 2025Q4`, `PDD 2025 annual report`, `Meituan latest`

## Design Philosophy

A good earnings analysis must solve two problems:
1. **You can see the future clearly** — this requires deep research from four distinct perspectives
2. **Readers can see the value** — this requires editorial polish and reader-perspective quality control

This Skill's workflow has three stages:
- **Stage One - Research**: The four masters deep-read the earnings report in parallel (Duan Yongping reads the essence of the business, Buffett audits financial quality, Munger reads competitive shifts, Li Lu hunts for risk signals)
- **Stage Two - Synthesis**: The Team Lead synthesizes the four perspectives and produces a first-draft research report
- **Stage Three - Publishing**: An editor Agent rewrites it into a WeChat article + a reader-reviewer Agent proposes revisions → the Team Lead finalizes

---

## Stage One: Four Masters Research in Parallel

### Step 1: Obtain Primary Materials

Use the Agent tool to launch background Agents to obtain the following raw materials **in parallel**:

| Material Type | Source | Priority |
|---------|---------|--------|
| Earnings report original | Company IR page, SEC EDGAR (US stocks), HKEX Disclosure (HK stocks), CNINFO (A-shares) | Highest |
| Earnings call transcript | Seeking Alpha, company IR page, Xueqiu | Highest |
| Management's letter to shareholders | Extracted from annual report | High (annual reports only) |
| Prior-period earnings/call | Same as above | High (used for commitment tracking) |

**Material Availability Rating**:

| Grade | Characteristics | Impact |
|------|------|------|
| Grade A | Complete original obtained | Execute all steps normally |
| Grade B | Only partial original or third-party summaries obtained | Mark as "non-primary source", reduce weight of footnote analysis |
| Grade C | Only news reports and data-website summaries available | Focus on core data changes, skip footnote mining, mark as "insufficient primary materials" |

Inform each Agent of the material availability rating, as it affects their depth of analysis.

### Step 2: Present the Team Framework to the User

| Stage | Role | Master/Position | Core Task |
|------|------|----------|---------|
| Research | **Team Lead** (yourself) | Overall coordination | Coordinate, synthesize, finalize |
| Research | Business Essence Interpreter | Duan Yongping | Has this business gotten better or worse? |
| Research | Financial Quality Auditor | Buffett | Is it earning real money or fake money? |
| Research | Competitive Shift Interpreter | Munger | How is the competitive landscape changing? |
| Research | Risk Signal Hunter | Li Lu | What is management hiding? |
| Publishing | Editor | WeChat writing | Rewrite the research report into a good article |
| Publishing | Reader Reviewer | Ordinary investor | Can readers understand it? Do they gain anything? |

### Step 3: Launch 4 Parallel Research Agents

Use the Agent tool to launch 4 background Agents **in a single message**.

---

#### Agent 1: Business Essence Interpretation (Duan Yongping Perspective)

**Core question: Does the business essence reflected in this earnings report show improvement or deterioration?**

> Duan Yongping: "Investing is buying a business. Reading an earnings report isn't about reading the numbers — it's about seeing whether the business has changed."

Analysis content:

1. **Revenue Structure Breakdown and Interpretation**
   - Revenue by business/by region — which are accelerating, which are decelerating
   - Not just listing numbers — what business logic does each segment reflect
   - Does revenue growth come from "volume" or "price"? Which is healthier?

2. **Changes in User/Customer Value**
   - Changes in operating metrics such as DAU/MAU/paying users
   - Quality metrics such as user time spent, ARPU, retention rate
   - Is the platform/product's value to users strengthening or weakening?

3. **Moat Detection**
   - Gross margin changes reflect whether pricing power is solid
   - Market share changes reflect whether competitive barriers are effective
   - Any signals that customer switching cost / network effect is being eroded

4. **"Good Business" Standard Assessment**
   - Duan Yongping's three conditions: differentiation, pricing power, sustainable competitive advantage — changes this period
   - Is the business getting "heavier" or "lighter"?
   - If the company shut down tomorrow, would users be very pained? Has that changed because of this earnings report?

5. **Management's Product Intuition**
   - When management discusses products/users, do they use concrete language or bureaucratic language?
   - Are there impressive product insights or worrying signs of disconnection?

**Output requirement**: Mark each sub-item as 🟢improvement / 🟡flat / 🔴deterioration, and give a Duan Yongping-style summary comment.

---

#### Agent 2: Financial Quality Audit (Buffett Perspective)

**Core question: Is this company earning real money or fake money? Has the margin of safety changed?**

> Buffett: "The first thing I do with every earnings report is turn to the cash flow statement."

Analysis content:

1. **Extraction and Verification of Core Financial Data**
   - Revenue, gross profit, operating profit, net profit — both GAAP and Non-GAAP
   - GAAP vs Non-GAAP difference: how much, where, and whether the gap is widening or narrowing
   - Cross-validate key data with at least two sources

   ```bash
   python3 ~/ai-berkshire/tools/financial_rigor.py cross-validate \
     --metric "revenue" --values {value1} {value2} --sources "source1" "source2"
   ```

2. **Cash Flow Analysis (Most Important)**
   - Operating cash flow vs net profit ratio (>100% is good, <80% warrants caution)
   - Free cash flow = operating cash flow - capex
   - Capex composition: maintenance vs expansion
   - Buyback and dividend amounts

3. **Profit Quality Examination**
   - Accounts receivable growth vs revenue growth
   - Inventory growth vs revenue growth
   - Trend in the gap between operating cash flow and net profit
   - Whether capitalized expenditure suddenly increased
   - Proportion of non-recurring gains

4. **Balance Sheet Health**
   - Changes in net cash / net debt
   - Changes in accounts receivable / inventory turnover days
   - Goodwill and intangible asset impairment risk

5. **Valuation and Margin of Safety Update**

   ```bash
   python3 ~/ai-berkshire/tools/financial_rigor.py verify-market-cap \
     --price {price} --shares {shares} --reported {reported market cap} --currency {currency}
   python3 ~/ai-berkshire/tools/financial_rigor.py verify-valuation \
     --price {price} --eps {EPS} --bvps {book value per share}
   python3 ~/ai-berkshire/tools/financial_rigor.py three-scenario \
     --price {price} --eps {EPS} --shares {shares in 100M} \
     --growth {optimistic} {neutral} {pessimistic} --pe {optimistic PE} {neutral PE} {pessimistic PE}
   ```

**Output requirement**: Attach tool output records to all calculations, profit-quality signal lights 🟢/🟡/🔴, and a Buffett-style summary comment.

---

#### Agent 3: Competitive Landscape Interpretation (Munger Perspective)

**Core question: What changes in the competitive landscape does this earnings report reveal?**

> Munger: "I want to know where I'm going to die, so I never go there."

Analysis content:

1. **Infer Competitive Changes from Earnings Data**
   - Revenue growth vs industry growth — outperforming or underperforming?
   - Gross margin changes reflect intensifying/easing competition
   - Marketing expense ratio changes — does it take more money to acquire customers?
   - R&D investment — proactive investment or forced catch-up?

2. **Comparison with Peer Competitors in the Same Period**
   - Comparison of key metrics of major competitors for the same period (if already published)
   - Comparison of growth rate, margins, investment intensity
   - Who's winning? Who's losing?

3. **Management's Discussion of Competition**
   - How they describe the competitive environment on the call
   - Do they name competitors? Is the tone confident or anxious?
   - Are there new competitive threats?

4. **Industry Trend Signals**
   - Impact of technological change (AI / new platforms, etc.)
   - Impact of regulatory changes on the competitive landscape
   - Consumption/demand-side trends

5. **Munger-Style Inversion Thinking**
   - What would kill this company? Does this earnings report contain any signals pointing to these threats?
   - Looking back 5 years from now, will this earnings report be a "turning point"?

**Output requirement**: Competitive landscape judgment (strengthening / flat / deteriorating), competitor comparison table, and a Munger-style inversion comment.

---

#### Agent 4: Risk Signal Hunter (Li Lu Perspective)

**Core question: What has management hidden in this earnings report? Which signals are flashing?**

> Li Lu: "The most important thing in investing is to avoid permanent loss of capital."

Analysis content:

1. **Management Tone Analysis**
   - Read management's discussion and call remarks paragraph by paragraph, tagging signals:
   - 🟢candor signal (proactively admitting problems) / 🟢clarity signal (has quantified targets)
   - 🔴vagueness signal (empty talk) / 🔴deflection signal (evasive answers) / 🔴externalized attribution

2. **Commitment Tracking**
   - Prior-period management's specific commitments vs this period's actual delivery, item by item
   - Duan Yongping: "To judge whether management is reliable, look at whether they did what they said before."

3. **Footnotes and Hidden Information**
   - Related-party transactions, equity-incentive dilution, contingent liabilities
   - Accounting policy changes, segment margin differences
   - Changes in customer/supplier concentration

4. **Earnings Call Q&A Highlights**
   - The 3-5 sharpest analyst questions and a quality score for management's answers

5. **Permanent Loss of Capital Risk**
   - Whether any signals appear that could lead to permanent loss
   - New developments in regulatory / compliance / litigation risk
   - Whether management has made irreversible wrong decisions

**Output requirement**: Management credibility score ★1-5, commitment fulfillment rate, risk-signal checklist, and a Li Lu-style summary comment.

---

### Step 4: Track Progress

Show the user in real time:

```
📊 {Company} {period} Earnings Deep-Read Progress
━━━━━━━━━━━━━━━━━━━━━━━
Stage One - Research
  ☐ Duan Yongping - Business Essence    ⏳ Analyzing...
  ☐ Buffett - Financial Quality         ⏳ Analyzing...
  ☐ Munger - Competitive Landscape      ⏳ Analyzing...
  ☐ Li Lu - Risk Signals                ⏳ Analyzing...
Stage Two - Synthesis                   ⏸ Waiting
Stage Three - Publishing                ⏸ Waiting
```

Each time a report arrives, update progress and show the core findings (3-5 items).

---

## Stage Two: Team Lead Synthesizes the Research Report

Once all 4 research reports have arrived, the Team Lead synthesizes them into a first-draft research report.

**Synthesis essentials** — this isn't stitching reports together, it's finding cross-references and contradictions:

1. **Points of consensus across the four perspectives**: Conclusions all four masters agree on carry the highest confidence
2. **Points of contradiction across the four perspectives**: e.g., Duan Yongping says the business got better, but Munger says competition is deteriorating — this kind of contradiction is the most valuable analysis
3. **The overlooked corners**: Things none of the four emphasized — could they be precisely the most important?

#### Research Report Structure

```markdown
# {Company} {period} Earnings Deep-Read Report
**Four Masters in Parallel | {date}**

## 1. One-Sentence Conclusion
> 50-100 words: beat/meet/miss expectations, core changes, impact on the investment thesis.

## 2. The 3 Most Important Changes This Period
Focus on the truly important changes, don't list data; keep each change under 100 words.

## 3. Four-Master Scorecard
| Perspective | Master | Core Question | Conclusion | Score | vs. Prior Period |
|------|------|---------|------|------|--------|

## 4. Core Data at a Glance
Table of key financial and operating metrics (this period vs prior period vs YoY)

## 5. In-Depth Analysis from Each Perspective
The 3-5 most important findings from each perspective

## 6. Management Tone and Commitment Tracking
Commitment fulfillment table + tone-change analysis

## 7. What Would the Four Masters Do?
| Master | If Holding | If Not Holding | Rationale |

## 8. Conclusion
1. Beat/meet/miss expectations?
2. Investment thesis impact: strengthened / no impact / weakened / broken
3. Next catalyst
4. Action recommendation
```

---

## Stage Three: Editorial Polish + Reader Review

Once the research report is complete, launch two Agents **in parallel**:

### Agent 5: Editor (WeChat Article Rewrite)

**Position**: Rewrite the hardcore research report into an article that WeChat readers love and can understand.

**Core principles**:
- Retain all key data and conclusions, don't reduce professional depth
- Improve the presentation so non-professional investors can follow the logic
- This isn't "popularization", it's "making professional content read without fatigue"

**Specific tasks**:

1. **Title and Opening**
   - The title should carry information and attract clicks, but no clickbait
   - Good title example: "Kuaishou Bet 26 Billion on AI — Did the Bet Pay Off?"
   - Bad title example: "Shocking! Kuaishou Earnings Blow Up!"
   - Within the first 100 words, make clear: what the most important conclusion of this earnings report is, and why readers should care

2. **Structure Optimization**
   - A research report is for yourself; a WeChat article is for others — adjust the logical order
   - Put "the 3 most important changes" up front (inverted-pyramid structure)
   - Keep tables but streamline them, convert long analysis into bullet points
   - Insert an "interim summary" roughly every 500 words to help readers digest

3. **Presentation Polish**
   - Explain stiff financial jargon with analogies/scenarios: "operating cash flow is 30% lower than net profit" → "earned 100 yuan but only felt 70 in the pocket"
   - The four masters' commentary quotes are the soul of the article — make sure each reads sharp and memorable
   - Paragraphs no longer than 4 lines, sentences no longer than 30 characters
   - Use contrast and juxtaposition appropriately to create reading rhythm

4. **Reader Value Check**
   - For each section, ask yourself: after reading this, what decision can the reader make? If the answer is "nothing", rewrite or delete it
   - The end of the article needs a clear "so what?" — give action guidance separately for holders and for those on the sidelines

5. **Format Adaptation**
   - WeChat-layout friendly: short paragraphs, clear subheadings, concise tables
   - Add appropriate dividers and blockquote formatting
   - Keep article length between 1,000-3,000 words (too long and readers bounce)

**Output**: The complete rewritten WeChat article.

---

### Agent 6: Reader Review (Ordinary Investor Perspective)

**Position**: Read the article as an ordinary investor who "follows value investing, has basic financial knowledge, and holds/follows the company."

**Review dimensions**:

1. **Readability (30% weight)**
   - How many minutes does it take to finish? Are there paragraphs you want to skip?
   - Where is it hard to understand or requires re-reading?
   - How's the rhythm? Any "tired of reading" feeling?

2. **Information Value (30% weight)**
   - After reading, is my understanding of this company deeper?
   - Are there any "oh, so that's how it is" moments?
   - Compared with analyses I've seen elsewhere, what's unique about this one?
   - Which information is redundant and could be deleted without affecting understanding?

3. **Credibility (20% weight)**
   - Is the data sourced? Are the key judgments grounded?
   - Does it present both sides? Or is it only bullish/bearish?
   - Are there any "this is way too confident" judgments that make one uncomfortable?
   - Are the four masters' quotes apt and forceful?

4. **Actionability (20% weight)**
   - After reading, do I know what to do?
   - Are the recommendations for "holders" and "those on the sidelines" specific enough?
   - What should I watch next? (catalysts, timing)

**Output format**:

```markdown
## Reader Review Report

### Overall Score: X/10

### Strengths (2-3 items)
Things the article does well from a reader's perspective

### Must Fix (Hard Flaws)
- Problem 1: specific description → suggested fix
- Problem 2: ...

### Suggested Improvements (Nice to Have)
- Suggestion 1: ...
- Suggestion 2: ...

### Questions readers most want answered but the article didn't
- Question 1
- Question 2

### One-Sentence Overall Verdict
```

---

### Team Lead Finalizes

After receiving the editor's rewrite and the reader review report:

1. **Address the reader review's "must fix" items** — revise item by item
2. **Selectively adopt the "suggested improvements"** — judge whether they're worth it
3. **Fill in the "questions readers want answered but weren't"** — add them if there's data support
4. **Final read-through** — ensure the revised full text is coherent and internally consistent

---

## Output Files

```
reports/{Company}/
├── {Company}-earnings-{period}.md                 ← Final WeChat article (finalized)
├── {Company}-earnings-{period}-research-draft.md  ← Four-master synthesized research report (internal use)
├── {Company}-earnings-{period}-duan-yongping.md   ← Business essence interpretation
├── {Company}-earnings-{period}-buffett.md         ← Financial quality audit
├── {Company}-earnings-{period}-munger.md          ← Competitive landscape interpretation
├── {Company}-earnings-{period}-li-lu.md           ← Risk signal analysis
└── {Company}-earnings-{period}-reader-review.md   ← Reader review report
```

## Release Audit (Data Spot-Check)

Run a spot-check on the final article:

```bash
python3 ~/ai-berkshire/tools/report_audit.py extract \
  --report reports/{Company}/{Company}-earnings-{period}.md

python3 ~/ai-berkshire/tools/report_audit.py verdict \
  --results '<filled-in JSON>' \
  --report {report filename}
```

**[RELEASE]** All pass → ready to publish; **[SEND BACK]** any fail → fix and re-audit.

## Relationship to Existing Skills

| Skill | Position | When to Use |
|-------|------|--------|
| `/earnings-review` | Single-Agent earnings deep-read | Quick pass, only one perspective needed |
| **`/earnings-team` (this Skill)** | **Six-Agent team deep-read + WeChat publishing** | **Key earnings for important companies, needing depth + publishing** |
| `/investment-team` | Four-Agent comprehensive company research | First time researching a company |

## Key Principles

- **Read the original, not summaries**: Do everything possible to obtain primary materials
- **The four perspectives are not four departments**: They must corroborate and challenge each other, not each talk past the other
- **The Team Lead's value lies in integrated judgment**: Find intersections and contradictions, not stitch reports together
- **Conclusions must be clear**: No "overall it basically meets expectations but there are also some points worth watching"
- **Contrarian checking runs throughout**: Every positive finding comes with a counter-argument
- **The editor doesn't lower professionalism**: Make professional content more readable, not turn it into pop-science
- **Reader review isn't a formality**: Genuinely nitpick from the reader's perspective
- **Data accuracy**: Cross-validate key data, use the financial_rigor.py tool to verify calculations
