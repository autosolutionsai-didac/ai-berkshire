# Management Deep-Dive: Buying a Stock Is Buying People

Conduct a management deep-dive research on $ARGUMENTS.

**Supported input formats**: `Company` or `Person Company`, e.g.: `Meituan`, `Wang Xing Meituan`, `Jensen Huang NVIDIA`

> "Buying a stock is buying people. Find people you trust, then hold for the long term." — Duan Yongping
>
> "To evaluate management, watch what they do when no one is looking." — Buffett

## Design Philosophy

Most investment analysis stops at the surface when evaluating management: résumés, ownership stakes, compensation. But Buffett spends a great deal of time **having meals and chatting with management**, Li Lu says **the essence of his investing is investing in people**, and Duan Yongping says **buying a stock is buying people**.

This skill is the **deepened version** of the fifth step (management evaluation) in `/investment-research`. When the management score in a standard investment study is uncertain (★★★ or below), or when management is the core investment logic, use this skill to conduct a deep-dive.

AI cannot have meals with management, but it can achieve the following through public information:
- **Track whether management's words and actions are consistent** (promises vs. delivery)
- **Analyze the return on every major capital-allocation decision**
- **Infer character from decisions made during hard times**
- **Cross-validate via feedback from employees / merchants / customers**

## Execution Flow

### Step 1: Identify Key Management and Launch Parallel Data Collection

Use WebSearch to confirm the following key figures:

| Role | Name | Tenure | Background | Ownership/Options |
|------|------|--------|------------|-------------------|
| CEO/Chairman | | | | |
| CFO | | | | |
| Founder (if not in office) | | | | |
| Actual controller (if different from CEO) | | | | |
| Other key executives | | | | |

**Note**: Distinguish between "who makes the decisions" and "whose name is on the title." At some companies the founder, though having stepped down, remains the guiding spirit (e.g., Colin Huang at Pinduoduo).

After confirming the key figures, use the Task tool to launch multiple background Agents to collect the following data **in parallel**:
1. Agent 1: CEO public statements and predictions (shareholder letters, earnings calls, interviews, social media)
2. Agent 2: Capital-allocation decision records (M&A, buybacks, dividends, new-business investments)
3. Agent 3: Governance structure and compensation (equity structure, related-party transactions, executive pay)
4. Agent 4: Cross-validation information (employee reviews, customer feedback, industry reputation)

### Step 2: CEO Circle-of-Competence Assessment

#### 2.1 Strategic Vision

Search the CEO's public statements over the past 5 years (shareholder letters, earnings calls, interviews, social media) and extract their judgments on the following questions:

| Time | CEO's judgment/prediction | Actual result | Accuracy |
|------|--------------------------|---------------|:--------:|
| | "We believe market X will..." | Market X actually... | ✅/❌ |
| | "Over the next 3 years our focus is..." | Actual execution... | ✅/❌ |

**Key questions**:
- Has the CEO ever made a correct judgment ahead of the market?
- Has the CEO stayed calm when everyone else was bullish?
- Is the CEO's understanding of industry trends following the market or independent thinking?

#### 2.2 Execution Ability

| Dimension | Assessment | Evidence |
|-----------|------------|----------|
| Strategy to execution | Did they do what they said? | |
| Organizational capability | Can they attract and retain talent? | |
| Crisis handling | How do they respond to difficulty? | |
| Iteration speed | How quickly do they correct mistakes? | |

### Step 3: Integrity Assessment (Most Important)

**Buffett**: "We look for three qualities: integrity, intelligence, and energy. And if you don't have the first, the other two will kill you."

#### 3.1 Promise-vs-Delivery Tracking

From the earnings calls, shareholder letters, and public interviews of the past 3 years, extract the **specific promises** management has made:

| # | Time | Promise | Where made | Delivery | Assessment |
|---|------|---------|------------|----------|------------|
| 1 | | "We will make business X profitable in 2025" | 2024 annual-report earnings call | | ✅/⚠️/❌ |
| 2 | | "We plan to buy back $X billion" | 2024 shareholder letter | | ✅/⚠️/❌ |

**Delivery-rate statistics**:

| Promise delivery rate | Assessment |
|:---------------------:|------------|
| >80% | Excellent — they do what they say |
| 60-80% | Acceptable — direction is right but execution deviates |
| 40-60% | Concerning — over-promises and under-delivers |
| <40% | Serious problem — not trustworthy |

#### 3.2 Performance During Hard Times

Search for major crises/difficulties in the company's history (stock crashes, earnings misses, regulatory shocks, intensifying competition) and analyze management's response:

| Crisis event | Time | Management's reaction | Assessment in hindsight |
|--------------|------|-----------------------|-------------------------|

**Focus on**:
- Did they communicate proactively or avoid?
- Did they attribute internally or shift blame externally?
- Did they seize the moment to do the hard-but-right thing, or choose to placate the market short-term?

#### 3.3 Attitude Toward Stakeholders

| Stakeholder | Management's attitude | Evidence | Assessment |
|-------------|-----------------------|----------|------------|
| Shareholders | Respect/ignore/exploit | | |
| Employees | Treat well/exploit/neglect | | |
| Customers/users | Customer-centric/short-term extraction | | |
| Merchants/suppliers | Fair cooperation/extreme price pressure | | |
| Regulators/society | Compliant/skirting the rules | | |

**Li Lu**: "A company's attitude toward its stakeholders determines its long-term vitality. Short-term squeezing can improve efficiency, but over the long run it damages the ecosystem."

### Step 4: Capital-Allocation Ability

This is the management ability Buffett values most — **for every dollar earned, how much can management turn it into?**

#### 4.1 Capital-Allocation Decision Records

Search the company's major capital-allocation decisions over the past 5 years and evaluate each one:

**M&A record**:

| Time | Acquisition target | Amount | Strategic rationale | Return in hindsight | Score (1-5) |
|------|--------------------|--------|---------------------|---------------------|:-----------:|

**Buyback record**:

Use `tools/financial_rigor.py verify-valuation` to verify PE and other valuation metrics at the time of the buyback and currently.

| Time | Buyback amount | Average buyback price | PE at the time | In hindsight | Score (1-5) |
|------|----------------|-----------------------|:--------------:|--------------|:-----------:|

**Dividend record**:

| Year | Dividend amount | Payout ratio | FCF same period | Sustainable? |
|------|-----------------|:------------:|-----------------|:------------:|

**New-business investments**:

| Time | Investment area | Cumulative outlay | Current status | Return assessment | Score (1-5) |
|------|-----------------|-------------------|----------------|-------------------|:-----------:|

#### 4.2 Capital-Allocation Score

| Dimension | Score (1-5) | Notes |
|-----------|:-----------:|-------|
| M&A discipline | | Acquiring at reasonable prices? How was post-deal integration? |
| Buyback timing | | Buying back when undervalued, stopping when overvalued? |
| Dividend reasonableness | | Does the payout ratio match FCF? |
| New-business investment | | What's the success rate? How disciplined are the stop-losses? |
| Cash management | | Are cash reserves reasonable? Hoarding too much? |
| **Overall score** | | |

**Buffett's standard**: The ideal management invests decisively when good opportunities exist, actively buys back / pays dividends when they don't, and never does an overpriced acquisition.

### Step 5: Governance Structure Assessment

#### 5.1 Equity Structure

| Item | Details | Risk assessment |
|------|---------|-----------------|
| Are there dual-class shares / super-voting rights? | | |
| Founder/actual-controller ownership stake? | | |
| Is there a VIE structure? | | |
| Are the independent directors genuinely independent? | | |
| Recent buy/sell records of major shareholders? | | |

#### 5.2 Compensation Reasonableness

| Executive | Total annual compensation | As % of company net profit | Vs. peers | Reasonable? |
|-----------|---------------------------|:--------------------------:|:---------:|:-----------:|

**Focus on**: Is the incentive structure aligned with long-term shareholder interests? Or does it encourage short-term behavior?

#### 5.3 Related-Party Transactions

| Related party | Transaction | Amount | Fair? | Risk assessment |
|---------------|-------------|--------|:-----:|-----------------|

### Step 6: Cross-Validation

AI cannot communicate with management face to face, but it can validate through publicly available secondary information. **Note**: the following information depends on what is publicly searchable and may be incomplete; annotate the information source and availability.

#### 6.1 Employee Perspective

Search **publicly searchable** employee reviews such as Glassdoor rating summaries and Zhihu discussions (for login-gated platforms like Maimai, mark "users may supplement on their own"):

| Dimension | Rating trend | Key feedback |
|-----------|--------------|--------------|
| Company culture | | |
| Management rating | | |
| Work intensity | | |
| Compensation satisfaction | | |
| Growth prospects | | |

#### 6.2 Customer/Merchant Perspective

Search App Store ratings, consumer complaints, and merchant forums:

| Dimension | Rating/trend | Key feedback |
|-----------|--------------|--------------|
| Product satisfaction | | |
| Customer service | | |
| Merchant/supplier relations | | |

#### 6.3 Industry Reputation

Search industry forums and social media to understand how peers and industry insiders view this management team.

### Step 7: Scenario Analysis for the CEO's Departure

**Buffett**: "A good company should be one even a fool can run — because sooner or later, a fool will run it."

| Question | Answer |
|----------|--------|
| If the CEO left tomorrow, could the company operate normally? | |
| How deep is the existing management team? Is there a clear successor? | |
| Does the company's competitive advantage depend on the CEO personally, or on the organization/systems? | |
| Were past management transitions smooth? | |

### Step 8: Output the Management Assessment Report

#### Report Structure

```
1. Key-figure snapshot (table)
2. Integrity assessment
   - Promise delivery rate
   - Performance during hard times
   - Attitude toward stakeholders
3. Ability assessment
   - Strategic vision (prediction accuracy)
   - Execution ability
   - Capital-allocation record
4. Governance structure
   - Equity-structure risks
   - Compensation reasonableness
   - Related-party transactions
5. Cross-validation
   - Employee perspective
   - Customer/merchant perspective
6. Overall score and conclusion
```

#### Overall Score

| Dimension | Weight | Score (1-5) | Weighted |
|-----------|:------:|:-----------:|:--------:|
| Integrity | 35% | | |
| Strategy & execution ability | 25% | | |
| Capital-allocation ability | 25% | | |
| Governance structure | 15% | | |
| **Overall score** | 100% | | |

#### Duan Yongping's "Buying People" Standard

> Answer the following three questions:
> 1. **Is this person honest?** (truthful, doesn't take advantage of shareholders)
> 2. **Is this person capable?** (strategic vision + execution + capital allocation)
> 3. **Would you be willing to hand your money to this person to manage for 10 years?**
>
> All three "yes" = ★★★★★ (5 points)
> First two "yes" = ★★★★ (4 points)
> Only the first "yes" = ★★★ (3 points)
> The first is not "yes" = ★ (1 point, don't invest)

### Step 9: Save the Report

Write the report to `reports/{Company}-management-{YYYYMMDD}.md`, e.g., `reports/Meituan-management-20260409.md`

---

## Key Principles

- **Integrity is a veto item** — insufficient ability can be learned, but flawed character cannot be repaired
- **Watch behavior, not words** — what management says doesn't matter; what they've done does
- **See the truth in hard times** — anyone is a good CEO with a tailwind; only a headwind reveals the real skill
- **Capital allocation is the ultimate exam** — making money is easy; allocating the money you've made well is hard
- **Don't fall in love with management** — stay objective; even people you admire can make big mistakes
