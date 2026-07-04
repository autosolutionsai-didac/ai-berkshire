---
name: investment-team
description: "AI Berkshire skill: Research Team: Four-Role Parallel Analysis Framework. Source: skills/investment-team.md."
---

## Codex adapter note

This skill is generated from `skills/investment-team.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Commands that reference `~/ai-berkshire/tools/...` assume the repo is checked out at `~/ai-berkshire`; if needed, prefer the current workspace path.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Research Team: Four-Role Parallel Analysis Framework

Conduct a team-based investment research analysis of $ARGUMENTS. Use the Team tools to create a genuinely multi-agent parallel research team.

## Execution Flow

### Step 1: Present the team framework

Show the user the following team structure and start once confirmed:

| Role | Responsibilities | Analytical framework |
|------|------|----------|
| **team-lead** (you) | Coordination, synthesis and judgment, producing the final report | Combined four-master framework |
| **business-analyst** | Business model & moat analysis | Duan Yongping's lens |
| **financial-analyst** | Financial statements & valuation analysis | Buffett's lens |
| **industry-researcher** | Industry structure & competitive dynamics | Munger's lens |
| **risk-assessor** | Risk assessment & management evaluation | Li Lu's lens |

### Step 1.5: AI research-bias assessment

Before creating the team, show the user an "AI researchability" assessment of the company:

**Information-richness rating** (determines the research strategy):
| Tier | Characteristics | Research-strategy adjustment |
|------|------|------------|
| Tier A (information-rich) | Listed for years, broad sell-side coverage | Have the team focus on **contrarian testing** and **non-consensus perspectives**, avoiding "correct but useless" output that merely echoes the market |
| Tier B (moderate information) | Recently listed, limited coverage | Every agent's estimated figures must be tagged with a confidence level; the team-lead must note "data sufficiency" when synthesizing |
| Tier C (information-scarce) | Obscure / newly listed / emerging market | The team shifts to "first-principles mode": rather than chasing report completeness, focus on the handful of core questions about the business's essence |

**Key reminder**: More information ≠ higher certainty; less information ≠ lower certainty. The confidence AI can express ≠ the true certainty of the investment. Certainty comes from the business model itself, not from the volume of available material.

Communicate the rating to each agent, as it shapes how they conduct research.

### Step 2: Create the team

Use TeamCreate to create the team:
- team_name: `{company}-research` (lowercase English, e.g. `meituan-research`)
- agent_type: `team-lead`

### Step 3: Create the 4 tasks

Use TaskCreate to create the following 4 tasks (each must have a subject, description, and activeForm):

#### Task 1: Business model analysis
- subject: `Analyze {company}'s business model, moat, and user value`
- description includes:
  1. Essence of the business model: definition of the core business, breakdown of the revenue structure
  2. How the platform/product flywheel operates
  3. Moat analysis: brand / switching cost / network effect / economies of scale / technology barriers, verified one by one
  4. User/customer value: what unique value it creates for each party
  5. Business matrix and synergies
  6. Assessment against Duan Yongping's "good business" criteria: differentiation, pricing power, sustainable competitive advantage
  7. Requires searching the latest earnings reports, industry reports, and other public information

#### Task 2: Financial and valuation analysis
- subject: `Analyze {company}'s financial data, profitability, and valuation`
- description includes:
  1. Revenue, net profit, and operating profit trends over the past 3-5 years
  2. Profitability metrics: ROE, ROA, gross margin, operating margin
  3. Cash-flow analysis: operating cash flow, free cash flow, capex
  4. Balance-sheet health: cash reserves, leverage ratio, liquidity
  5. Valuation analysis: PE/PS/PB/EV, etc., versus historical and peer benchmarks
  6. Margin-of-safety assessment: intrinsic value vs. current share price
  7. **Financial-rigor verification (must call the tool via Bash; mental math is forbidden)**:
     - Market-cap check: `python3 ~/ai-berkshire/tools/financial_rigor.py verify-market-cap --price {price} --shares {shares} --reported {reported market cap} --currency {currency}`
     - Valuation check: `python3 ~/ai-berkshire/tools/financial_rigor.py verify-valuation --price {price} --eps {EPS} --bvps {book value per share}`
     - Cross-validation of key data: `python3 ~/ai-berkshire/tools/financial_rigor.py cross-validate --field {field} --values '{JSON}' --unit {unit}`
     - Three-scenario valuation: `python3 ~/ai-berkshire/tools/financial_rigor.py three-scenario --price {price} --eps {EPS} --shares {shares in 100M} --growth {optimistic} {base} {pessimistic} --pe {optimistic PE} {base PE} {pessimistic PE}`
     - Embed the tool's output directly into the report as a verification record

#### Task 3: Industry and competitive analysis
- subject: `Analyze the {industry} landscape and {company}'s competitive position`
- description includes:
  1. Industry size and growth: market size, growth rate, penetration
  2. Competitive landscape: market share of major rivals, comparison of competitive strategies
  3. Threat assessment of core competitors: analyze each major rival one by one
  4. Landscape of each sub-segment
  5. Industry trends: technological change, policy impact, new entrants
  6. Value-chain analysis: value distribution across upstream, midstream, and downstream
  7. Requires searching the latest industry data and competitive developments

#### Task 4: Risk and management assessment
- subject: `Assess {company}'s investment risks and management quality`
- description includes:
  1. Management assessment: the CEO's circle of competence, integrity, strategic vision, capital-allocation skill, and quality of past decisions
  2. Regulatory risk: current and potential regulatory impact
  3. Competitive risk: threat level of each competitor
  4. Business risk: losses in new businesses, uncertainty of expansion
  5. Macro risk: impact of the economic cycle and the industry cycle
  6. Governance structure: ownership structure, related-party transactions, shareholder-return policy
  7. Long-term certainty: what will the company look like in 10 years? What could disrupt its business model?
  8. Requires searching the latest regulatory developments, management statements, etc.

### Step 4: Launch the 4 parallel agents

Use the Task tool to launch all 4 agents simultaneously (**they must be invoked in parallel within a single message**):

Configuration for each agent:
- `subagent_type`: `general-purpose`
- `run_in_background`: `true`
- `team_name`: the corresponding team name
- `name`: the corresponding role name (business-analyst / financial-analyst / industry-researcher / risk-assessor)

Prompt template for each agent:

```
You are the "{role name}" on the {company} research team, responsible for analyzing {company} from {master}'s investment perspective.

Please complete task #{task number}: {task subject}

Specific requirements:
{contents of the task description}

**Research method**:
- Use WebSearch to search for the latest public information (earnings reports, industry reports, news)
- **Financial data must come from two independent sources**, following the `skills/financial-data.md` specification (US stocks: macrotrends+stockanalysis; HK stocks: aastocks+macrotrends; A-shares: East Money+CNINFO); flag any discrepancy >1% between the two sources
- Ensure data accuracy and cite sources for key figures
- Analysis must go deep, not stay on the surface

**Output requirements**:
- The report must be thorough, presenting key data in Markdown tables
- Each analytical dimension must have a clear conclusion and rating
- The report must end with an overall conclusion for that dimension

**When finished**:
1. Use TaskUpdate to mark task #{task number} as completed
2. Send the complete analysis report to team-lead via SendMessage (type: "message", recipient: "team-lead")
```

### Step 5: Receive the reports and track progress

- Show the user a live progress table (which agents have finished, which are still researching)
- Each time a report arrives, update progress and present its key takeaways (3-5 points)
- Wait until all 4 reports are in

### Step 6: Shut down the team members

Once all reports are in, send a shutdown_request to all 4 agents (via SendMessage, type: "shutdown_request").

### Step 7: Synthesize the final report

Synthesize the 4 analysis reports and produce a final report with the following structure:

---

#### 1. One-sentence conclusion
> Summarize in one paragraph (50-100 words) whether it is worth investing in and the core rationale

#### 2. Four-dimension scoring table
| Dimension | Framework | Rating (1-5 stars) | Core judgment |
|------|------|------------|----------|

Overall score: X / 5

#### 3. Key-data snapshot
Table of key financial and operating metrics (2-year comparison)

#### 4. Summary of each analytical dimension
Extract the 3-5 most important findings for each dimension

#### 5. Investment thesis (Bull vs. Bear)
- 🟢 Bull case (5-7 points)
- 🔴 Bear case (5-7 points)

#### 6. Buffett pre-purchase checklist
| # | Check item | Pass? | Notes |
10 core check items, assessed one by one

#### 7. Final investment recommendation
- Qualitative-judgment table (business quality / management / valuation / timing)
- Tiered action-recommendation table (aggressive / balanced / conservative → recommendation + price range)
- Key catalysts (3-5 add-to-position signals / 3-5 trim signals)

#### 8. Concluding paragraph
A final summary of 100-200 words

---

### Step 8: Save the report

Save everything into the company folder `reports/{Company}/` (English company name), matching the project report convention:

- Write each of the four analyst reports received from the sub-agents to its own file: `01-business-model-duan-yongping.md`, `02-financials-valuation-buffett.md`, `03-industry-competition-munger.md`, `04-risk-management-li-lu.md`.
- Write the team-lead synthesis (the complete final report) to `reports/{Company}/final-report.md`.

(date format YYYYMMDD where a date is needed)

### Step 9: Data spot-check (release audit)

```bash
# Step 1 — Extract the spot-check list (15% random sample)
python3 ~/ai-berkshire/tools/report_audit.py extract \
  --report <report file path>

# Step 2 — For each item on the list, pull the figure from a reliable source (see skills/financial-data.md)

# Step 3 — Output the release/reject verdict
python3 ~/ai-berkshire/tools/report_audit.py verdict \
  --results '<completed JSON>' \
  --report <report file name>
```

**[Release]** all items pass → the report may be published; **[Reject]** any item fails → fix and re-audit.

### Step 10: Clean up the team

Use TeamDelete to clean up the team resources.

## Important notes

1. **The 4 agents must be launched in parallel** — invoke the Task tool 4 times in a single message
2. **Agents report via SendMessage** — not file-based collaboration, but message-based communication
3. **Data accuracy** — require agents to use WebSearch for the latest data, with cross-validation of key figures
4. **Conclusions must be clear** — do not shy away from giving a buy / wait-and-see / avoid recommendation and a specific price range
5. **All analysis must be backed by data** — attach data sources
6. **Be patient** — the 4 agents will take several minutes to research; update the user on progress in real time
7. **Anti-bias awareness** — when synthesizing, the team-lead must assess: is each agent's analysis constrained by how much material was available? Does it converge too much with market consensus? The final report must include an "information-richness rating" and an "AI research-limitations statement"
8. **The honesty principle under information scarcity** — it is better to leave a blank in the report marked "insufficient data" than to fill the framework with speculation and fake certainty
