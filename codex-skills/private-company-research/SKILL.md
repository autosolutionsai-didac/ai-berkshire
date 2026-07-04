---
name: private-company-research
description: "AI Berkshire skill: Private Company Research: Multi-Agent Parallel Deep-Research Framework. Source: skills/private-company-research.md."
---

## Codex adapter note

This skill is generated from `skills/private-company-research.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Commands that reference `~/ai-berkshire/tools/...` assume the repo is checked out at `~/ai-berkshire`; if needed, prefer the current workspace path.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Private Company Research: Multi-Agent Parallel Deep-Research Framework

Conduct a team-based deep-research analysis of $ARGUMENTS. Purpose-built for private companies such as Ant Group, Xiaohongshu, SpaceX, and Stripe.

**Ultimate goal**: Under conditions of naturally scarce information, reconstruct as faithfully as possible the company's **true value** — not the valuation the market assigns, but what the business itself is worth.

## Framework Characteristics

Core differences between researching a private company vs. a public company:
- **No standardized financial statements**: information must be pieced together from multiple sources and cross-verified
- **Few valuation anchors**: reliant on funding rounds, comparable-company analysis, and scenario modeling
- **Large information asymmetry**: requires more "jigsaw-puzzle" research methods
- **Uncertain exit path**: IPO / M&A / secondary transfer are all possible

## Self-Awareness of AI Research Bias (the core premise of this framework)

Private companies are the domain where AI research bias is most severe. You must stay alert to the following traps at all times:

**Core tension**: AI excels at structuring information that already exists, but private-company information is naturally scarce. This leads to:
1. **False conservatism**: because material is scarce, AI tends to produce conservative/vague conclusions — but scarce material does NOT mean the company is bad
2. **False precision**: to fill out the report template, AI may dress up "reasonable speculation" as "evidence-based analysis"
3. **The benchmarking trap**: forcibly benchmarking against public companies inherits public-company valuation logic and ignores the private company's unique value
4. **Survivorship bias**: information findable online tends to skew positive (companies proactively spread mostly good news)

**Guiding principles**:
- Better to leave a blank and say "we don't know" than to fill the tables with speculation and fake certainty
- Every data point must be tagged with a confidence level (🟢 high / 🟡 medium / 🔴 low), so the reader can judge for themselves
- Distinguish "verifiable facts" from "AI reasoning," tagged with different formats
- For companies with extremely scarce information, switch to "first-principles mode" — do not chase report completeness, just answer a few core questions:
  1. What real problem does this business solve? Is the demand real demand or false demand?
  2. Why this team? What unique advantage do they have?
  3. If it succeeds, how high is the ceiling? If it fails, where is it most likely to die?
  4. What is the key validation milestone at the current stage?

**Turning information asymmetry to your advantage**: the market has little information on private companies → pricing efficiency is low → this is precisely where excess returns may come from. The goal of AI research is not to eliminate information asymmetry (impossible), but to extract the most decisive judgment criteria from limited information.

---

## Execution Flow

### Step 1: Present the Team Framework

Present the following team structure to the user and launch after confirmation:

| Role | Responsibilities | Core Perspective |
|------|------|----------|
| **team-lead** (yourself) | Orchestration, information jigsaw, cross-verification, final report output | Investment-decision integration |
| **business-decoder** | Business-model teardown & product-user analysis | "What is the essence of this business?" |
| **financial-detective** | Piecing together financial data & valuation modeling | "Reconstruct the true financial picture as much as possible despite missing information" |
| **competitive-mapper** | Industry landscape & competitive dynamics & substitution threats | "Who competes with it, and who could disrupt it?" |
| **risk-governance-analyst** | Full-spectrum risk & management/governance/investor assessment | "What could go wrong, and who is at the helm?" |
| **tech-ip-analyst** | Tech stack / patents / R&D capability / technical moat | "Is the technical barrier real or fake, and how long can it hold?" |
| **signal-miner** | Alternative-data mining: hiring / patents / litigation / app data / supply chain | "Beyond the usual information, what other clues are there?" |

### Step 2: Create the Team

Use TeamCreate to create the team:
- team_name: `{company}-private-research` (lowercase English, e.g. `ant-group-private-research`)
- agent_type: `team-lead`

### Step 3: Create 6 Tasks

Use TaskCreate to create the following 6 tasks (each must have subject, description, activeForm):

---

#### Task 1: Deep Analysis of Business Model and Product Users
- subject: `Deconstruct {company}'s business model, product portfolio, and user ecosystem`
- activeForm: `Analyzing {company}'s business model and user ecosystem`
- description contains:

```
## Deep Business-Model Teardown

### 1. Core Business Definition
- Define the essence of this business in one sentence (Duan Yongping-style definition: use the plainest language to explain this business to someone smart but unfamiliar with the field)
- What problem does the company solve? For whom does it create value?
- How the value proposition differs from comparable products
- If the company didn't exist, how would users solve this problem? How costly are the alternatives?
- Judge the "rigidity" of demand: in an economic downturn, would users cut this expense?

### 2. Revenue-Model Teardown
- Revenue composition: advertising / commissions / subscriptions / transaction take / financial services / SaaS / hardware / licensing fees, etc.
- Share and growth trend of each revenue line (where data exists)
- Estimate monetization-efficiency metrics: ARPU, take rate, ad load, conversion rate, etc.
- Revenue-quality assessment:
  - Share of recurring vs. one-time revenue
  - Revenue concentration: share of top-5 customers/channels
  - Predictability of revenue (contract/subscription type vs. transactional)
  - Whether revenue recognition is reasonable (any signs of early revenue recognition)
- Benchmark monetization efficiency against listed peers

### 3. Unit-Economics (UE) Estimation
- CAC (customer acquisition cost) estimation:
  - Share of paid acquisition vs. organic growth
  - CAC by channel (where available)
  - CAC trend: rising or falling as scale grows?
- LTV (lifetime value) estimation:
  - ARPU × expected lifetime
  - Consider cross-sell and upsell
- LTV/CAC ratio, payback period
- Marginal cost structure: marginal-cost trend of incremental users/transactions
- Economies-of-scale inflection point: when / whether the breakeven point has been passed

### 4. Product Portfolio and Flywheel Effect
- Core products + extension products + incubated products
- How the flywheel runs: network effect / data flywheel / economies of scale
- Synergies and cross-traffic between products
- Product lifecycle: which stage each product is in
- Product iteration speed: app/product update frequency, major feature updates in the past 12 months

### 5. Business Model Canvas (BMC)
Fully describe the business model using the following 9 elements:
| Element | Content |
|------|------|
| Value proposition | |
| Customer segments | |
| Channels | |
| Customer relationships | |
| Revenue streams | |
| Key resources | |
| Key activities | |
| Key partners | |
| Cost structure | |

### 6. Deep User Analysis
- User scale: MAU/DAU (estimated from QuestMobile, Sensor Tower, SimilarWeb, etc.)
- User-growth curve: which stage of the S-curve (argue with specific data)
- User-stickiness metrics:
  - DAU/MAU ratio (daily-active / monthly-active)
  - Average usage time, open frequency
  - Day-1 / 7-day / 30-day retention (where available)
  - User growth vs. retention trend comparison (identify fake growth)
- User profile: age / region / spending power / occupation distribution
- User reputation:
  - App Store / Google Play rating trend (change over the past 12 months)
  - Social-media sentiment analysis
  - Real user feedback on Zhihu / Weibo / Xiaohongshu
  - The main clusters of negative reviews
- User-acquisition efficiency:
  - Ratio of paid acquisition vs. organic growth vs. word-of-mouth
  - Whether reliant on a single acquisition channel

### 7. Pricing-Power Assessment
- Any price-increase history in the past 3 years? User churn after price increases?
- Price comparison with competitors: price leader or follower?
- Assess user price sensitivity
- Reasonableness of commission/take rates within the value chain

### 8. Moat Assessment
Verify and score each of the following 6 dimensions (★1-5):

| Moat Type | Score | Evidence | Trend | Durability Assessment |
|-----------|------|------|------|-----------|
| Network effect | | More users, more value? One-sided or two-/multi-sided? | widening/stable/narrowing | |
| Switching cost | | Cost of users migrating to competitors? Data/relationship/habit migration cost? | | |
| Brand mindshare | | Category = brand? Estimated NPS? | | |
| Data barrier | | Is a data flywheel formed? Proprietary data assets? Data scale? | | |
| Regulatory license | | Any entry barrier? Difficulty of obtaining licenses? | | |
| Economies of scale | | Is the cost advantage from scale significant? | | |

Overall moat rating: wide / medium / narrow / none

### 9. Internationalization Analysis (if applicable)
- Overseas-market expansion status
- Share of international revenue
- Localization strategy and challenges
- Differences in the overseas competitive landscape
```

---

#### Task 2: Piecing Together Financial Data and Valuation Modeling
- subject: `Piece together {company}'s financial data and perform valuation analysis`
- activeForm: `Piecing together {company}'s financial data and valuation`
- description contains:

```
## Piecing Together Financial Data (detective-style research)

Private companies have no standardized financial statements; data must be pieced together from multiple sources and cross-verified. Every data point must be traced to a specific source, with time and confidence noted.

### 1. Data-Source Matrix
**Search the following sources by priority**:

| Priority | Source Type | Specific Sources | Reliability | Search Method |
|--------|---------|---------|--------|---------|
| 1 | Prospectus / regulatory filings | SEC filings, HKEX, prospectus drafts disclosed by the CSRC | 🟢 high | Search "company name + prospectus / IPO filing" |
| 2 | Parent / affiliated listed-company reports | e.g. Ant data in Alibaba's annual report, Google Cloud annual report | 🟢 high | Search related-party disclosures in the parent's annual report |
| 3 | Regulatory penalties / compliance disclosures | Penalty documents from the PBOC, CSRC, SAMR | 🟢 high | Search "company name + penalty / fine / rectification" |
| 4 | Bond / ABS issuance documents | e.g. underlying data in Ant Huabei ABS prospectuses | 🟢 high | Search "company name + bond / ABS / trust" |
| 5 | Business-registration information | Tianyancha/Qichacha business annual reports, paid-in capital | 🟡 medium-high | |
| 6 | Funding news | Valuation, funding amount, investors | 🟡 medium | Search "company name + funding / valuation" |
| 7 | Third-party research reports | Brokerage, consultancy, industry-association reports | 🟡 medium | Search "company name + research report / report" |
| 8 | In-depth media coverage | LatePost, The Information, 36Kr, Bloomberg | 🟡 medium | Directly search these outlets + company name |
| 9 | Industry-data estimation | Back into figures via industry totals and market share | 🔴 low-medium | |
| 10 | Ex-employee / insider leaks | Blind, Maimai, forums | 🔴 low | Reference only, not a primary basis |

### 2. Key Financial-Metric Estimation
Estimate the following data as much as possible. **Each data point must note**: source, time, confidence, and estimation method.

**Revenue side**:
- Total revenue scale and growth (last 3 years, annual/quarterly granularity)
- Revenue-structure breakdown (by business line/product line)
- Decompose revenue-growth drivers: volume (users/transactions) × price (ARPU/average order value)
- Seasonal pattern of revenue

**Cost side**:
- Gross-margin estimation (benchmark against listed peers, explain the selection logic)
- R&D-expense ratio estimation (via headcount × per-capita salary, or share of R&D staff)
- Selling-expense ratio estimation (via acquisition channels and ad-spend data)
- G&A-expense ratio estimation

**Profit side**:
- Operating profit / EBITDA estimation
- Net profit / adjusted net profit estimation
- Profitability timeline: when profitable? If not yet profitable, when is it expected?

**Cash-flow side**:
- Operating cash flow judgment (positive/negative, self-funding or not)
- Capex level and trend
- Free-cash-flow estimation
- Cash on hand / burn rate (estimated from funding amounts, funding intervals, headcount)
- Cash runway: how long can it last at the current burn rate?

**Efficiency metrics**:
- Headcount and productivity (revenue per employee, profit per employee)
- Capital efficiency: how much revenue each 1 yuan of funding produces
- Benchmark efficiency metrics against listed peers

### 3. Cross-Verification of Financial Data
- If a metric has multiple sources, list them all and explain the differences
- Estimate the same metric using different methods and check whether results converge
- Flag "single-source" data that cannot be verified

| Metric | Source A (data/time) | Source B (data/time) | Difference | Adjudication |
|------|-------------------|-------------------|------|---------|

### 4. Funding History and Valuation Evolution
Compile a full funding timeline:

| Round | Time | Amount | Pre-money | Post-money | Lead investor | Co-investors | Valuation-multiple growth | Notes |
|------|------|------|---------|---------|--------|--------|------------|------|

Analysis:
- Whether the valuation-growth curve is healthy (whether the growth multiple per round is reasonable)
- Whether funding intervals are reasonable (too frequent = fast burn? too sparse = funding difficulty?)
- Whether a down round has occurred
- Whether existing shareholders keep doubling down (a confidence signal)
- Inferred deal terms of the latest round:
  - Liquidation preference (1x / 2x / participating)
  - Anti-dilution protection (full ratchet / weighted average)
  - Ratchet/earnout clauses (performance / IPO timing)
  - The impact of these terms on common-share value

### 5. Valuation Analysis (multiple methods cross-checked)

**Method 1: Latest-Funding-Valuation Method**
- Latest-round valuation and time
- "Common-share-equivalent valuation" after accounting for liquidation preferences etc. (typically requires a 20-40% discount)
- Adjustment for time elapsed since then
- Motivation analysis of this round's investors (financial vs. strategic investment; strategic investors may pay a premium)

**Method 2: Comparable-Listed-Company Method**
- Select 3-5 comparable listed companies and explain the selection rationale
- Comparison of key multiples:

| Comparable | P/S | P/E | EV/EBITDA | EV/Revenue | Growth | Margin |
|---------|-----|-----|-----------|------------|------|--------|

- Adjustments applied:
  - Illiquidity discount: 20-30% (note the specific value and rationale)
  - Growth premium/discount
  - Scale discount
  - Regulatory/policy-risk discount

**Method 3: DCF Scenario Analysis**
Three scenarios; list the key assumptions for each:

| Assumption | Bear | Base | Bull |
|------|------|------|------|
| Revenue CAGR over next 5 years | | | |
| Terminal operating margin | | | |
| Terminal growth rate | | | |
| WACC | | | |
| Terminal multiple (EV/EBITDA) | | | |

Each assumption must be evidence-backed, not assumed out of thin air.

**Method 4: Endgame-Market-Cap Back-Solve Method**
- Assume this business's market position at its terminal state 5/10 years out
- Terminal revenue and margin assumptions
- Reasonable terminal multiple (reference mature peers)
- Back out the reasonable current valuation range
- Implied annualized return

**Method 5: Transaction-Comparables Method**
- M&A/funding transactions in the same industry over the past 2 years
- Transaction multiples (P/S, P/E)
- Transaction context and premium/discount factors

### 6. Consolidated Valuation Judgment

| Method | Valuation Range | Confidence | Weight | Weighted Valuation |
|------|---------|--------|------|---------|

- Do the valuations from different methods converge? If they diverge widely, analyze why
- The final valuation range must distinguish "fair valuation" from "conservative valuation" (margin-of-safety valuation)
```

---

#### Task 3: Industry Landscape and Competitive Dynamics Analysis
- subject: `Analyze the competitive landscape and substitution threats in {company}'s industry`
- activeForm: `Analyzing {company}'s industry landscape and competitive dynamics`
- description contains:

```
## Industry Landscape and Competitive Dynamics

### 1. Industry Positioning and Market Size
- Definition of the core segment the company operates in (note: the company's self-definition may be flattering; judge independently)
- The three-layer market size TAM/SAM/SOM:
  - TAM (total addressable market): the entire broad industry
  - SAM (serviceable addressable market): what the company's tech/model can cover
  - SOM (serviceable obtainable market): what it can actually capture today
- Compare market-size data sources (forecasts from different research firms can differ widely)
- Market penetration: current vs. ceiling
- Industry stage: nascent / growth / mature / decline (with evidence)
- Industry-growth drivers: which forces are pushing/blocking industry growth

### 2. Full Value-Chain Map
Draw the complete value-chain structure (text diagram):

```
Upstream suppliers (who? bargaining power?)
    ↓
The company's segment (which position in the value chain? share of the profit pool?)
    ↓
Downstream customers/users (concentration? alternative choices?)
    ↕
Competitors / substitutes / potential entrants
```

- Profit-pool analysis: profit distribution across value-chain segments
- The company's bargaining power in the value chain (upstream/downstream)
- Upstream/downstream dependency analysis: any single-supplier/single-customer dependency
- Structural changes underway in the value chain

### 3. Porter's Five Forces (quantitative scoring)

| Force | Intensity (★1-5) | Key Factors | Impact on the Company |
|------|-----------|---------|-----------|
| Industry rivalry | | Concentration, degree of differentiation, exit barriers | |
| Threat of new entrants | | Capital barrier, tech barrier, regulatory barrier, brand barrier | |
| Threat of substitutes | | Substitute price/performance, switching cost | |
| Supplier bargaining power | | Supplier concentration, switching cost | |
| Buyer bargaining power | | Customer concentration, information transparency | |

Overall industry-attractiveness score: ★1-5

### 4. Deep Scan of the Competitive Landscape

| Competitor | Type | Market Share (est.) | Revenue Scale | Funding/Valuation | Core Strengths | Main Weaknesses | Threat Level |
|---------|------|---------------|---------|----------|---------|---------|---------|
| Direct competitor 1 | Direct | | | | | | |
| Direct competitor 2 | Direct | | | | | | |
| Indirect competitor 1 | Cross-sector | | | | | | |
| Potential entrant 1 | Incumbent giant | | | | | | |

Focus analysis:
- **Direct competitors**: direct rivals in the same segment; analyze each one's strategic intent and resource commitment
- **Indirect competitors**: cross-sector potential competition, especially the related businesses of large firms
- **Substitution threats**: different tech routes/models, especially disruption AI may bring
- **Potential entrants**: probability and method of giants entering (build / acquire / invest)

### 5. Deep Competitor Comparison
Select the 2-3 most direct competitors (both listed and private) for a multi-dimensional comparison:

| Dimension | {company} | Competitor A | Competitor B | Competitor C |
|------|---------|---------|---------|---------|
| Founding year | | | | |
| User scale (MAU) | | | | |
| Revenue scale | | | | |
| Revenue growth | | | | |
| Total funding/market cap | | | | |
| Valuation/revenue multiple | | | | |
| Monetization efficiency (ARPU) | | | | |
| Gross margin | | | | |
| Profitability status | | | | |
| Headcount | | | | |
| Technical capability | | | | |
| Differentiated positioning | | | | |
| Degree of internationalization | | | | |

### 6. Competitive Dynamics and Trends
- Key changes in the competitive landscape over the past 12 months (funding, M&A, product launches, personnel changes)
- Inferred strategic direction of competitors (inferred from hiring, patents, product updates)
- Structural shifts underway in the industry
- Impact of technological change on the competitive landscape (especially AI/large models)
- Impact of regulatory policy on the competitive landscape
- Does the industry have "winner-take-all" characteristics? Or will a stable oligopoly form?

### 7. Competitive Scenario Modeling
- Scenario A: the company wins — what conditions are required? Probability?
- Scenario B: balanced coexistence — each player's survival space?
- Scenario C: disrupted — the most likely disruptor and path?

### 8. Global Benchmarking Analysis
Find overseas/domestic benchmark companies (already listed) and analyze:

| Dimension | Benchmark A | Benchmark B | Implications for {company} |
|------|---------|---------|----------------|
| Development path | | | |
| Current valuation level | | | |
| Time from a similar stage to IPO | | | |
| Post-IPO stock performance | | | |
| Key factors of success/failure | | | |

- Limitations of the benchmarks (China-market specifics, regulatory differences, user-habit differences)
```

---

#### Task 4: Full-Spectrum Risk and Governance Assessment
- subject: `Assess {company}'s full-spectrum risk and management/governance structure`
- activeForm: `Assessing {company}'s risk and governance structure`
- description contains:

```
## Full-Spectrum Risk and Governance Assessment

### 1. Deep Assessment of Founder/CEO

> "Buying a stock is buying the person [running it]." — Duan Yongping

- **Background and track record**: education, career, entrepreneurial experience
  - Any serial-entrepreneur experience? Outcome of the last venture?
  - Years of relevant industry experience
  - Largest team/business previously managed
- **Strategic vision**: search the CEO's public statements over the past 3 years (speeches, interviews, internal letters, social media)
  | Time | CEO's judgment/prediction | Actual outcome | Accuracy |
  |------|--------------|---------|--------|
  - Any correct calls that were ahead of the market?
  - Any staying calm when everyone was bullish?
- **Execution**: whether key milestones were hit on time
  | Commitment | Commitment time | Occasion | Delivery | Assessment |
  |------|---------|---------|---------|------|
- **Character and values**:
  - Attitude toward users/employees/society (judge from specific events, not slogans)
  - Choices when facing difficulty (how layoffs were handled, crisis handling, trade-offs in conflicts of interest)
  - Trade-off between short-term profit vs. long-term value
- **Controversial events**: any negative records (search "CEO name + controversy / scandal / problem")
- **Rating**: ★1-5 (with detailed rationale)

### 2. Core-Team Assessment
- Roster and backgrounds of key executives (CTO/CFO/COO/VP, etc.)
  | Name | Title | Background | Tenure | Prior experience |
  |------|------|------|------|---------|
- Key-talent-flow analysis:
  - Departures of key executives in the past 2 years (who left? where to? why?)
  - Additions of key executives in the past 2 years (poached from where? what does it signal?)
  - Net talent inflow or outflow?
- Team complementarity: are the founding team's capabilities complementary? Any obvious gaps?
- Team-culture signals:
  - Glassdoor/Maimai ratings and trend (the 12-month direction of change matters more than the absolute value)
  - Employee recommendation willingness (would recommend to a friend)
  - CEO approval rating
  - Sentiment on overtime culture and organizational atmosphere
- Key-person dependency: what happens to the company if the CEO/CTO leaves?

### 3. Ownership Structure and Governance

**Equity structure**:
| Shareholder | Ownership % | Voting % | Type | Notes |
|------|---------|-----------|------|------|

- Founder control structure: dual-class shares / concert parties / VIE structure
- Founder ownership trend (dilution at each funding round)
- Employee stock-ownership plan: coverage, vesting conditions, IPO-linked terms

**Governance structure**:
- Board composition (share of independent directors, investor seats)
- Major-decision mechanisms
- Potential conflicts of interest:
  - Related-party transactions (transactions between the founder's other companies and this company)
  - Horizontal competition
  - Conflict points between major-shareholder and minority-shareholder interests

### 4. Deep Analysis of the Investor Roster

| Investor | Round | Amount | Estimated stake | Type | Strategic value | Exit pressure |
|--------|------|------|---------|------|---------|---------|

Analysis:
- Brand-endorsement significance of the lead investor (top-tier VC vs. unknown fund)
- Strategic synergy value of industrial capital (does it bring resources/channels?)
- Investor exit-pressure assessment:
  - How long is left in the fund's life?
  - Have they already sold old shares in the secondary market?
  - Are ratchet/earnout clauses nearing expiry?
- Red-flag signals in the investor roster:
  - Any investors with poor reputations?
  - Have early investors already fully exited?
  - Follow-on situation in the latest round (existing shareholders not following = lack of confidence?)

### 5. Full-Spectrum Risk Checklist

| Risk Type | Specific Risk | Probability (H/M/L) | Impact (H/M/L) | Severity | Hedgeable? | Monitoring Metric |
|---------|---------|---------------|---------------|--------|-----------|---------|
| Regulatory risk | Antitrust, data security, industry crackdown, license risk | | | | | |
| Competitive risk | Giant entry, new-model disruption, price war | | | | | |
| Technology risk | Platform migration, AI disruption, tech-route failure | | | | | |
| Talent risk | Loss of founder/core team | | | | | |
| Funding risk | Liquidity chain, down round, funding difficulty | | | | | |
| IPO risk | Listing window, regulatory approval, market environment | | | | | |
| Geopolitical risk | US-China relations, cross-border data, sanctions | | | | | |
| Commercialization risk | Monetization below expectations, user backlash | | | | | |
| Governance risk | Related-party transactions, opacity, investor conflict | | | | | |
| Compliance risk | Data privacy (GDPR/PIPL), content compliance | | | | | |
| Macro risk | Economic cycle, interest-rate environment, capital-market heat | | | | | |
| ESG risk | Environmental/social/governance-related risk | | | | | |

### 6. Exit-Path Analysis

| Exit Method | Likelihood (★1-5) | Estimated Time Window | Expected Valuation Range | Key Preconditions | Main Obstacles |
|---------|-------------|------------|------------|---------|---------|
| A-share IPO | | | | | |
| HK IPO | | | | | |
| US IPO | | | | | |
| Acquired | | Who are the potential buyers? | | | |
| Secondary transfer | | How liquid? | | | |
| SPAC | | | | | |
| Long-term no exit | | | | | |

- Most likely exit path and rationale
- Exit-timeline modeling
- Expected-return analysis under each exit path

### 7. Worst-Case Scenario Analysis (Munger-style inversion)

> "Invert, always invert." — Munger

- How is this company most likely to **fail**? List 3 specific failure paths
- Probability assessment and triggers for each failure path
- In the worst case, how much can investors recover? (liquidation-value analysis)
- Why would smart people **not** invest in this company? (list at least 5 reasons)
- Historically, which companies with similar positioning/stage have failed? Why?
- What signal appearing would mean "the thesis is broken" and you should cut losses?
```

---

#### Task 5: Technical Capability and Intellectual-Property Analysis
- subject: `Analyze {company}'s tech stack, patent portfolio, and R&D capability`
- activeForm: `Analyzing {company}'s technical capability and intellectual property`
- description contains:

```
## Deep Analysis of Technical Capability and Intellectual Property

> For a tech company, the reality and durability of technical barriers directly determine whether the valuation is reasonable.

### 1. Tech-Stack Analysis
- Inferred core technical architecture (inferred from job postings, tech blogs, open-source projects, conference talks)
- Whether the tech-stack choices are reasonable (are the right tools solving the right problems?)
- Technical-debt signals:
  - Whether job postings show heavy hiring for "refactor/migration" roles
  - Whether a large-scale tech-stack switch is underway
  - Whether the user side has frequent bug/outage complaints

### 2. Patent-Portfolio Analysis
Search patent databases (Google Patents, CNIPA, USPTO):

| Patent Metric | Data | Source |
|---------|------|------|
| Total patents (granted) | | |
| Patents pending | | |
| New patents in the past 2 years | | |
| Distribution across core tech areas | | |
| Citation count of key patents | | |
| International patent footprint | | |

- Patent-quality assessment (not just count):
  - Any core/foundational patents?
  - Do the patents' tech areas align with the core business?
  - Any patent litigation (as defendant or as plaintiff)?
- Patent trend: is filing speed accelerating or slowing? Any shift in tech direction?
- Patent comparison with competitors

### 3. R&D-Capability Assessment
- **R&D investment**:
  - R&D headcount/share (estimated from hiring platforms, LinkedIn)
  - R&D-expense estimation (headcount × average salary + infrastructure)
  - R&D-expense ratio (vs. peers)
  - R&D-investment trend: increasing or cutting?
- **R&D output**:
  - Academic publications (search Google Scholar, arXiv)
  - Tech-conference talks (search top venues such as KDD, NeurIPS, SIGIR)
  - Open-source contributions (search the GitHub org account)
  - Tech blog / WeChat article output
- **R&D efficiency**:
  - Speed from tech R&D to product launch
  - Commercialization rate of technical achievements

### 4. Technical-Talent Assessment
- **Core technical leaders**: background and capability of the CTO/VP Eng/Chief Scientist
  | Name | Title | Education | Prior company | Technical influence |
  |------|------|------|--------|-----------|
- **Technical-talent density**:
  - Which companies/labs do they come from? (share from top institutions such as Google/Meta/MSRA/BAT)
  - Salary competitiveness of technical roles (estimated from job postings)
  - Attrition signals in the technical team (departure activity on LinkedIn)
- **Hiring signals**:
  - What technical roles are open now? (reflects technical strategy direction)
  - Hiring difficulty and fill speed for technical roles
  - Whether a new technical team/lab is being built?

### 5. Technical-Moat Assessment

| Technical-Barrier Dimension | Score (★1-5) | Evidence | Durability |
|-------------|-----------|------|--------|
| Algorithm/model barrier | | Any proprietary algorithm? Can it be copied? | |
| Data barrier | | Data scale, proprietary data, data-flywheel speed | |
| Engineering barrier | | System complexity, long-accumulated engineering capability | |
| Talent barrier | | Are core technical talents hard to replace? | |
| Ecosystem barrier | | Developer ecosystem, API/SDK coverage, technical standards | |

- Overall technical-moat rating: strong / medium / weak
- Assess the decay rate of the technical moat (in the AI era, the half-life of technical barriers may be very short)

### 6. AI/New-Technology Impact Assessment
- The company's AI capabilities and positioning
- Impact of AI on the company's core business (augmenting vs. threatening vs. neutral)
- Is the company a beneficiary of the AI transformation or one to be disrupted?
- Impact assessment of other emerging technologies (Web3/AR/VR/quantum computing, etc.)

### 7. Technology-Risk Checklist
| Risk | Specific Description | Probability | Impact |
|------|---------|------|------|
| Tech-route failure | The bet tech direction is falsified | | |
| Open-source substitution | Core technology replaced by an open-source solution | | |
| Platform dependency | Dependence on a specific cloud/chip/OS | | |
| Security vulnerability | Data breach / system attacked | | |
| Talent loss | Departure of core technical staff | | |
```

---

#### Task 6: Alternative-Data Signal Mining
- subject: `Mine {company}'s unconventional data signals and hidden clues`
- activeForm: `Mining {company}'s alternative-data signals`
- description contains:

```
## Alternative-Data Signal Mining

> Conventional information on private companies is limited; alternative data often provides more truthful operating signals than news coverage.
> The goal of this task is: beyond the conventional information sources, mine every possibly useful clue.

### 1. Hiring-Signal Analysis
Search job postings on LinkedIn, Boss Zhipin, Maimai, Indeed, Glassdoor:

**Hiring scale and trend**:
- Total open positions currently
- Hiring trend over the past 6 months (accelerating/stable/shrinking)
- Hiring-scale comparison with competitors

**Hiring-structure analysis**:
| Role Category | Count | Share | Signal Interpretation |
|---------|------|------|---------|
| R&D/Engineering | | | Tech direction |
| Product | | | Product strategy |
| Sales/BD | | | Commercialization stage |
| Marketing/Operations | | | Growth strategy |
| Data/AI | | | AI positioning |
| Internationalization | | | Overseas plans |
| Compliance/Legal | | | Regulatory response / IPO prep |
| Finance/IR | | | IPO-prep signal |

**Key-signal capture**:
- Hiring for IR (investor relations) = IPO signal
- Hiring for compliance/data security = regulatory pressure or IPO prep
- Hiring for overseas roles = internationalization move
- Salary range for senior roles = the company's financial strength and talent competitiveness
- Tech stacks / business directions mentioned in job descriptions = strategic direction

### 2. App/Product-Data Analysis
Search App Store, Google Play, Qimai Data, SimilarWeb:

| Metric | Data | Source | Trend |
|------|------|------|------|
| App Store ranking | | | 6-month trend |
| User rating | | | Direction of change |
| Number of ratings | | | Growth rate |
| Estimated downloads | | | |
| App update frequency | | | |
| Main features in the latest update | | | |

- High-frequency keywords and sentiment analysis in App Store reviews
- Main clusters of recent negative reviews (bugs? charges? worsening experience?)
- Web-traffic data (SimilarWeb): UV, PV, visit duration, bounce rate

### 3. Social-Media and Sentiment Signals
Search Weibo, Zhihu, Xiaohongshu, Twitter/X, Reddit:

- Interaction data of the company's official accounts (followers/reposts/comments trend)
- Heat and sentiment of spontaneous user discussion (positive/negative/neutral)
- Assessments of the company by industry KOLs / big Vs
- Sentiment hotspots in the past 3 months
- Checklist of negative sentiment and how the company responded
- Any leaks from insiders (former/current employees)

### 4. Business-Registration and Legal Signals
Search Tianyancha/Qichacha/Qixinbao:

**Business-registration information**:
- Registered capital and change history
- Paid-in capital
- Shareholder/equity-change records
- List of subsidiaries/affiliates (newly established = new business? deregistered = business contraction?)
- Changes in business scope (new scope = new business direction)

**Legal information**:
| Type | Count | Summary of important cases |
|------|------|-------------|
| Litigation as plaintiff | | |
| Litigation as defendant | | |
| IP disputes | | |
| Labor arbitration | | |
| Administrative penalties | | |
| Judgment-debtor records | | |

- Details and potential financial impact of major litigation/arbitration
- Administrative-penalty records (environmental/tax/labor/data-security, etc.)

### 5. Supply-Chain and Partner Signals
- List of known core suppliers/partners
- Are the suppliers listed? Do their financial reports mention cooperation data with this company?
- Tender/procurement information (government procurement sites, corporate bidding platforms)
- Partner assessments and depth of cooperation

### 6. Domain and Digital Footprint
Search domain/subdomain information:
- List of domains registered by the company (newly registered domains may hint at new business/products)
- Subdomain analysis (api.xx.com, pay.xx.com, etc. hint at business architecture)
- SSL-certificate information
- Trademark-registration status (newly registered trademarks = new brand/product line)

### 7. Industry-Conference and Exposure Signals
- Executives' conference talks / attendance records over the past 12 months
- Industry awards / media rankings (entered "unicorn lists," "most innovative," etc.?)
- Interaction with government/industry associations (policy consultation, standard-setting participation)
- Trend in media-exposure frequency and quality

### 8. Secondary-Market Trading Signals (if any)
- Whether an old-share trading market exists (SharesPost, EquityZen, WeChat groups, etc.)
- Implied valuation of old-share trades vs. latest-round funding valuation
- Supply-demand condition of buyers and sellers
- Whether many employees are selling options/RSUs

### 9. Consolidated Signal Scoring

| Signal Category | Direction (positive/negative/neutral) | Strength (strong/medium/weak) | Confidence | Core Findings |
|---------|----------------|---------------|--------|---------|
| Hiring signal | | | | |
| Product data | | | | |
| Sentiment signal | | | | |
| Legal signal | | | | |
| Supply-chain signal | | | | |
| Digital footprint | | | | |
| Industry exposure | | | | |
| Secondary trading | | | | |

**Combined-signal judgment**: do the signals point in the same direction? Any contradictory signals?

### 10. Anomalous-Signal Checklist (most important)
List all "unusual" findings — these are often the most valuable information:
- Signals inconsistent with the company's external narrative
- Data inconsistent with industry common sense
- Sudden changes (rapid hiring contraction/expansion, dense executive departures, etc.)
- Unexplainable phenomena
```

---

### Step 4: Launch 6 Parallel Agents

Use the Agent tool to launch 6 agents simultaneously (**they must be invoked in parallel within a single message**):

Each agent's configuration:
- `subagent_type`: `general-purpose`
- `run_in_background`: `true`

Prompt template for each agent:

```
You are the "{role name}" in the private-company research team for {company}.

You are researching a **private (unlisted) company**, which means:
- There are no standardized public financial statements; information must be pieced together from multiple sources
- Data may be incomplete or contradictory; confidence must be tagged
- More reasoning and reasonable estimation are needed, but the estimation process must be shown transparently
- Not finding information ≠ the information not existing; the information found may be biased

Please complete the following research task: {task subject}

Specific requirements:
{contents of the task description}

**Research method**:
1. Use WebSearch to search the latest public information; search each dimension at least 3-5 times with different keyword combinations
2. Search-keyword strategy:
   - Chinese: company name + revenue/valuation/funding/user count/MAU/IPO/prospectus/layoffs/rectification
   - English: Company Name + revenue/valuation/funding/users/IPO/filing
   - Specific person name + company name (search for management-related information)
   - Company name + specific competitor name (search for competitive dynamics)
3. Priority information sources:
   - High-confidence: prospectus, regulatory filings, related-party disclosures in listed-company annual reports
   - Medium-confidence: LatePost, The Information, 36Kr, Bloomberg, Reuters, TechCrunch
   - Supplementary verification: Zhihu, Maimai, Glassdoor, Tianyancha, Qichacha
4. Use WebFetch to obtain the full text of key articles (do not rely only on search snippets)
5. For important data, cross-verify with at least 2 different sources

**Data-tagging rules (strictly enforced)**:
- Tag the source of each key data point (down to the outlet name and article title)
- Tag the data time (accurate to year and month)
- Tag confidence: 🟢 high (prospectus/official disclosure) / 🟡 medium (credible media/research) / 🔴 low (estimate/rumor)
- When sources conflict, **list them all** and explain the difference and your judgment
- Distinguish "facts" from "reasoning": facts in normal font, reasoning/estimation in *italics* with the estimation method noted
- Explicitly tag information that cannot be obtained as "data missing"; do not fabricate

**Output requirements**:
- The report should be thorough, presenting key data in Markdown tables
- Each analysis dimension should have a clear conclusion and score
- The estimation process must be fully transparent (show the calculation logic and every assumption)
- At the end of the report, provide:
  1. Overall score for this dimension (★1-5) and core judgment
  2. Self-assessment of information completeness for this dimension (sufficient/moderate/insufficient/severely insufficient)
  3. The 3 most important findings
  4. The biggest information blind spot (which missing information most affects the judgment)
```

### Step 5: Receive Reports and Track Progress

- Show the user a live progress table (which agents are done, which are still researching)
- Each time a report arrives, update progress and present the report's core takeaways (3-5 points)
- Wait until all 6 reports have arrived

### Step 6: Cross-Verification and Information Jigsaw

**This is the most critical newly added step of the enhanced framework**. Before consolidating, the team-lead must:

1. **Data-conflict adjudication**:
   - Extract the key data from each agent's report
   - Identify whether the same data cited by different agents is consistent
   - Adjudicate conflicting data: list all sources, state which is trusted and why

2. **Signal-consistency check**:
   - Are the business-growth signals (business-decoder) vs. the hiring signals (signal-miner) consistent?
     (if the business is said to be growing fast but hiring is contracting, this needs explaining)
   - Do the tech-leadership narrative (tech-ip) vs. the patent/talent data (signal-miner) support each other?
   - Does the valuation level (financial-detective) vs. the competitive position (competitive-mapper) match?
   - Is management's public narrative (risk-governance) vs. the actual-action signals (signal-miner) consistent?

3. **Information-jigsaw reconstruction**:
   - Fit together the information fragments from the 6 reports and see whether a more complete picture can be reconstructed
   - Tag the information "white zone" (confirmed known), "gray zone" (clues but uncertain), "black zone" (entirely unknown)

4. **Anti-bias check**:
   - Check whether the report has a "detailed on positive information, brief on negative information" bias
   - Confirm each positive judgment has a corresponding counter-check

### Step 7: Consolidate the Final Report

Synthesize the 6 analysis reports and output a final report with the following structure:

---

#### 1. One-Sentence Conclusion
> In one paragraph (50-100 characters), summarize the **true-value judgment** of this private company: how much the business is worth, and why.

#### 2. Company-Profile Snapshot
| Item | Content | Confidence |
|------|------|--------|
| Company name | | |
| Founding year | | |
| Headquarters | | |
| Founder/CEO | | |
| Core business | | |
| Headcount | | |
| Latest valuation | | |
| Latest funding round | | |
| Estimated revenue scale | | |
| Estimated profit status | | |
| Estimated user scale | | |
| Main investors | | |
| VIE/red-chip structure | | |

#### 3. Six-Dimension Score Table
| Dimension | Analyst | Score (★1-5) | Core Judgment | Confidence | Information Completeness |
|------|--------|-----------|---------|--------|-----------|
| Business model & users | business-decoder | | | | |
| Financials & valuation | financial-detective | | | | |
| Industry & competition | competitive-mapper | | | | |
| Risk & governance | risk-governance-analyst | | | | |
| Technology & IP | tech-ip-analyst | | | | |
| Alternative-data signals | signal-miner | | | | |

Overall score: ★X / 5

#### 4. Key-Data Jigsaw (after cross-verification)
Integrate the data pieced together by each analyst, **keeping only cross-verified data**:

| Metric | Data | Number of Sources | Source Detail | Confidence | Notes |
|------|------|---------|---------|--------|------|

#### 5. Signal-Consistency Matrix
| Check Item | Signal A | Signal B | Consistency | Interpretation |
|--------|-------|-------|--------|------|
| Growth narrative vs. hiring trend | | | ✅/⚠️/❌ | |
| Tech-leadership narrative vs. patent data | | | | |
| Valuation level vs. competitive position | | | | |
| Management narrative vs. actual action | | | | |

#### 6. Per-Dimension Analysis Summary
For each dimension, extract the 3-5 most important findings (tag source and confidence)

#### 7. True-Value Assessment

**Business-essence judgment**:
- What kind of business is this? (one sentence)
- How high is the "certainty" of this business?
- Duan Yongping-style judgment: is this a "right business"?

**Moat Scorecard**:
| Moat Type | Score (★1-5) | Core Evidence | Trend | Durability |
|-----------|-----------|---------|------|--------|
| Network effect | | | widening/stable/narrowing | |
| Switching cost | | | | |
| Brand mindshare | | | | |
| Data barrier | | | | |
| Regulatory license | | | | |
| Economies of scale | | | | |
| Technical barrier | | | | |

**Valuation judgment**:
| Valuation Method | Valuation Range | Confidence | Notes |
|---------|---------|--------|------|
| Latest-funding valuation (adjusted) | | | |
| Comparable-company method | | | |
| DCF scenario analysis | | | |
| Endgame-market-cap back-solve | | | |
| Transaction-comparables method | | | |

**Consolidated true-value range**:
- Conservative valuation (margin-of-safety valuation): $XXB
- Fair valuation (base-case assumptions): $XXB
- Optimistic valuation (best-case scenario): $XXB
- Current market valuation: $XXB
- **Margin of safety**: current valuation vs. conservative valuation = XX%

#### 8. Investment Thesis (bull vs. bear)
- 🟢 Bull case (5-7 points, each with evidence source)
- 🔴 Bear case (5-7 points, each with evidence source)
- ⚖️ Which side's argument is more persuasive? Why?

#### 9. Risk Matrix
| Risk | Probability | Impact | Overall Severity | Hedgeable? | Monitoring Metric |
|------|------|------|-----------|-----------|---------|

Top 3 core risks and mitigation strategies

#### 10. Exit-Path Assessment
Most likely exit method, time window, expected return

#### 11. Investment-Decision Table

**One-page decision table**:
```
┌──────────────────────────────────────────────┐
│  Company: XXX    Latest valuation: $XXB      │
│  Stage: [seed/growth/mature/pre-IPO]         │
│  Info completeness: [sufficient/moderate/insufficient/severely insufficient] │
├──────────────────────────────────────────────┤
│  Core investment logic (in 3 sentences):     │
│  1. ________________________________________  │
│  2. ________________________________________  │
│  3. ________________________________________  │
├──────────────────────────────────────────────┤
│  True-value judgment:                        │
│  Fair valuation range: $XXB - $XXB           │
│  Current valuation vs. fair: rich/fair/cheap │
│  Margin of safety: ____%                     │
├──────────────────────────────────────────────┤
│  Key assumptions & validation method:        │
│  Assumption 1 → tracking metric → checkpoint → time │
│  Assumption 2 → tracking metric → checkpoint → time │
│  Assumption 3 → tracking metric → checkpoint → time │
├──────────────────────────────────────────────┤
│  Fatal risks & "thesis broken" signals:      │
│  Risk 1 → if X happens, conclusion flips → stop-loss strategy │
│  Risk 2 → if Y happens, conclusion flips → stop-loss strategy │
├──────────────────────────────────────────────┤
│  Conclusion: invest / wait-and-see / avoid   │
│  If wait-and-see: what triggers a re-evaluation? │
│  Expected exit: IPO / M&A / secondary transfer │
│  Expected return multiple: X - Y×            │
│  Expected time frame: X - Y years            │
│  Annualized return: X% - Y%                  │
└──────────────────────────────────────────────┘
```

**Tiered recommendations**:
| Investor Type | Recommendation | Rationale |
|-----------|------|------|
| PE/VC institution (lead) | | |
| PE/VC institution (follow) | | |
| Secondary-market transfer | | |
| Buy post-IPO | | |
| Not recommended to participate | | |

**Key catalysts**:
| Bull Catalyst | Expected Time | Bear Catalyst | Expected Time |
|-----------|---------|-----------|---------|
| | | | |

#### 12. Information-Blind-Spot Map
| Dimension | Known Information | Missing Information | Impact of Missing | Acquisition Suggestion |
|------|---------|---------|---------|---------|

Do these blind spots affect the reliability of the core conclusion? If so, state explicitly: "with X information missing, the confidence of the above conclusion is Y."

#### 13. Ongoing-Tracking Checklist
| Tracking Item | Frequency | Information Source | Metric to Watch | Alert Threshold |
|---------|------|---------|---------|---------|

#### 14. Closing Paragraph
A final summary of 150-250 characters, including:
- The essence of this business
- The true-value judgment
- The reasonableness of the current valuation
- The greatest certainty and uncertainty
- The final recommendation and core rationale

---

### Step 8: Save the Report

Write the complete final report to `reports/{company}/{company}-private-{YYYYMMDD}.md`.

### Step 9: Clean Up the Team

Use TeamDelete to clean up team resources.

---

## Important Notes

1. **The 6 agents must be launched in parallel** — invoke the Agent tool 6 times within a single message
2. **Data-confidence tagging** — private-company data sources vary widely in quality; every key data point must be tagged with source and confidence
3. **Estimation must be transparent** — all estimation processes must show the calculation logic; do not produce numbers out of thin air
4. **Cross-verification** — cross-verify key data with at least 2 sources; when sources conflict, list them all
5. **Signal-consistency check** — the consolidation stage must include a cross-dimension signal-consistency check
6. **Conclusions must be clear** — do not avoid giving an invest/wait-and-see/avoid recommendation, but also state the confidence of the conclusion
7. **Wait patiently** — the 6 agents' research takes several minutes; update the user on progress in real time
8. **Chinese and English search** — private-company information may be spread across Chinese and English media; search in both languages
9. **Anti-bias core principle** — scarce material ≠ bad company; short AI analysis ≠ low investment certainty. For companies with extremely scarce information, switch to "first-principles mode" focused on the core questions, without chasing formal report completeness
10. **Honest blanks** — clearly distinguish "evidence-based analysis" from "speculative filler" in the report; it is acceptable to state "this dimension has insufficient data to produce a meaningful conclusion"
11. **Alternative data is not noise** — hiring, patents, litigation, app data, and other alternative data may be closer to the true operating condition than news coverage
12. **True-value orientation** — the ultimate goal is to judge how much this business is worth, not to produce a good-looking report. If the information is insufficient for a reliable valuation judgment, simply say "insufficient information, cannot provide a reliable valuation"
