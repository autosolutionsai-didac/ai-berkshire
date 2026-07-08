# Three AI tracks: large models, autonomous driving, AI cloud

> "Understanding Baidu" series · Article 03
> Reading time: about 12 minutes

---

## The full picture of Baidu's AI

**Ernie's technology surpasses GPT-5, but its consumer-side MAU is only 1/72 of Doubao's. Apollo Go is #1 in global scale, yet has never disclosed a complete income statement. AI cloud is growing 34%, yet holds only a 6% market share.** This is the real state of Baidu's three AI tracks: the technology is strong enough, but none of the three has been fully validated.

Baidu is the only AI company in China that covers the full stack from "chips → framework → model → application." Here is its technology stack:

| Layer | Baidu product | Competing benchmark |
|------|---------|---------|
| AI chips | Kunlun (P800) | Huawei Ascend / Nvidia |
| Deep learning framework | PaddlePaddle | PyTorch / TensorFlow |
| Foundation large model | Ernie 5.0 / 5.1 | GPT-5 / DeepSeek / Qwen |
| AI cloud platform | Baidu AI Cloud Qianfan | Alibaba Cloud / Volcano Engine |
| Consumer-facing applications | Ernie Bot / AI-ified Baidu Search | Doubao / Yuanbao / DeepSeek |
| Autonomous driving | Apollo Go (Luobo Kuaipao) | Waymo / Tesla FSD |

**In China, no other company simultaneously does chips, frameworks, models, cloud, and autonomous driving.** Alibaba has cloud and models but no chip mass production or autonomous driving; ByteDance has models and cloud but no chips or framework; Huawei has chips but no consumer application ecosystem.

But is being "full-stack" an advantage or a burden? That depends on whether each track can stand on its own. Let's break them down one by one.

---

## Track one: Ernie large models — leading in technology, lagging in users

### Technical progress

The pace of Ernie's iteration has not been slow:

| Version | Release date | Key parameters | Highlights |
|------|---------|---------|------|
| Ernie Bot (3.5) | March 2023 | — | China's first conversational AI |
| Ernie 4.0 | April 2024 | — | Improved multimodal capability |
| Ernie 5.0 official release | January 2026 | **2.4 trillion parameters** | Native omni-modal, comprehensive benchmarks surpassing Gemini-2.5-Pro and GPT-5-High |
| Ernie 5.1 | May 2026 | — | Pretraining cost only **6%** of the industry norm, top domestic search capability, agent capability surpassing DeepSeek-V4-Pro |

> Data sources: Baidu official announcements, QbitAI, Guangming Online.

**Ernie 5.0's comprehensive capability surpasses Gemini-2.5-Pro and GPT-5-High across 40+ authoritative benchmarks** — this is a genuine technical breakthrough. Version 5.1 achieves comparable results at 6% of the pretraining cost, showing that Baidu has real capability in model-training efficiency.

### The consumer-side dilemma: why strong technology but so few users?

Yet leading technology has not translated into user scale. This is the most puzzling aspect of Baidu's AI story:

| AI app | MAU (March 2026) | Company behind it |
|--------|---------------------|---------|
| Doubao | **345 million** | ByteDance |
| Qwen | **~170 million** | Alibaba |
| DeepSeek | **127 million** | DeepSeek |
| Yuanbao | **~100 million+** | Tencent |
| **Ernie Bot** | **4.79 million** | **Baidu** |

> Data source: QuestMobile (March 2026).

**Baidu's consumer AI app ranks 11th, with an MAU only 1/72 of Doubao's.** This gap is not "a bit behind" — it is "not even in the same league."

What's the reason?

1. **Distribution gap**: ByteDance funnels traffic into Doubao via Douyin's 700 million daily active users, and Tencent funnels traffic into Yuanbao via Weixin — Baidu has no "super traffic entry point" from social or short video
2. **Flawed product strategy**: Baidu spread its AI capability across multiple entry points — the "Ernie Bot app," "AI-ified Baidu Search," "Ernie Assistant" — fragmenting user mindshare
3. **Fixed user perception**: Users equate Baidu with a search engine and don't proactively go to Baidu to "chat"

**Counterargument**: "Competition among consumer AI apps has only just begun, and MAU rankings will keep changing. Baidu's advantage is the combination of search plus AI — Ernie 5.1's search capability now ranks top domestically, and if Baidu Search can be turned into 'the best AI search,' its 679 million MAU will naturally convert without needing a standalone chat app."

**Rebuttal**: "The logic of 'search plus AI' sounds reasonable, but user behavior doesn't migrate automatically. Google has the world's strongest search AI (SGE), yet ChatGPT remains users' AI tool of choice. 'Search' and 'AI assistant' are two different user needs and cannot simply be equated."

---

## Track two: Apollo Go autonomous driving — the world's largest scale, an unclear profit picture

### Operating data

Apollo Go (Luobo Kuaipao) is the **most imaginative** part of Baidu's AI story:

| Metric | Data | Source |
|------|------|------|
| Cumulative rides | **20 million+** | Baidu annual report |
| Cumulative miles driven | **240 million km** | Baidu annual report |
| Weekly rides | **250,000** (matching Waymo) | Wall Street CN |
| Operating cities | Wuhan, Beijing, Shanghai, Chongqing, etc. | Baidu's official website |
| Internationalization | London (pilot in 1H26), Dubai, Hong Kong | Huarong Securities, Baidu announcements |
| Seventh-generation autonomous vehicle | 600km range, cost down 30% from the prior generation | Baidu Apollo's official website |
| RT6 cost | About **RMB 250,000** (Waymo's per-vehicle cost is > RMB 1 million) | Disclosed by Baidu |

> Data sources: Baidu annual report, Apollo's official website, Wall Street CN, Huarong Securities.

**#1 in global robotaxi scale, per-vehicle cost only 1/7th of Waymo's, and already matching Waymo's weekly ride volume.** These are all facts.

### The profit black box

But Baidu has never separately disclosed a complete income statement for Apollo Go. What we do know:

- Baidu claims that "per-city unit economics (UE) have already broken even"
- But this "breakeven" measure **excludes R&D amortization and headquarters overhead** — if these were included, it could still be running a substantial loss
- Apollo Go's revenue is folded into "non-online-marketing revenue," so it cannot be independently verified

**Counterargument**: "Autonomous driving is a business requiring massive upfront investment — looking at profit now is meaningless. Waymo doesn't make money either. The key is Baidu's cost advantage — RT6 at RMB 250,000 per vehicle vs. Waymo's 1 million+ — meaning Baidu is more likely to be first to profitability."

**Rebuttal**: "Low per-vehicle cost does not equal low total cost. Baidu still needs to fund perception-system R&D, HD map maintenance, operations teams, safety-driver salaries, government relations, and more, all at once. If 'per-city UE breakeven' excludes R&D, it isn't a true breakeven. Investors need to see a complete income statement, not selectively disclosed metrics."

### Internationalization: a genuine catalyst

Entering London in the first half of 2026 (in partnership with Uber), on top of its existing presence in Dubai and Hong Kong, is a critical step in upgrading Baidu's autonomous-driving story from a "China story" to a "global story."

If the London pilot succeeds, the impact on Baidu's valuation could be a step change — because the market currently prices in essentially none of Apollo Go's overseas potential.

But the risk is equally large: **internationalizing autonomous driving is not just a technology problem — it also involves local regulation, insurance, public acceptance, geopolitics, and many other uncertainties.**

---

## Track three: Baidu AI Cloud — small share, fast growth

### Market position

| Cloud vendor | China AI cloud market share (Omdia, 1H25) | Growth rate |
|--------|----------------------------------|------|
| Alibaba Cloud | **36%** | +20%+ |
| Huawei Cloud | **19%** | +30%+ |
| Tencent Cloud | **16%** | +15%+ |
| Volcano Engine (ByteDance) | **14.8%** | +60%+ |
| **Baidu AI Cloud** | **6.1%** | **+34%** |

> Data source: Omdia 1H25 report.

**Only 6.1% share, ranking fifth.** In a winner-take-most market like cloud, this position is not comfortable.

But Baidu AI Cloud has one differentiating advantage: **full-stack in-house development + large-model capability + industry depth**.

| Advantage | Specific evidence |
|------|---------|
| Large-model bid-winning | **#1 on both counts** for two consecutive years |
| Government/enterprise clients | Serves **65% of central SOEs** + all systemically important banks |
| AI compute subscriptions | Up **143%** year-over-year in 2025Q4 (accelerating) |
| Full-year AI cloud revenue | ~**RMB 20 billion** (+34% YoY) |

> Data sources: Baidu annual report, Wall Street CN.

### The profitability of AI cloud

This is the biggest unknown. Baidu has never separately disclosed the gross margin of AI cloud.

**Counterargument**: "AI cloud's high growth may be coming at the cost of losses. ByteDance's Volcano Engine, with 14.8% share and 60% growth, is closing in, and ByteDance also has internal businesses (Douyin recommendations, Doubao) that can absorb its compute capacity. Baidu's 6% share is fragile against Volcano Engine."

**Rebuttal**: "Baidu AI Cloud's client base skews toward government and enterprise customers — these clients are sticky, have strong paying power, and are unlikely to switch due to a price war. 65% central-SOE coverage plus every systemically important bank represent a security-review and trust barrier, not simple price competition."

---

## A hidden asset: Kunlun chips

Kunlun is not one of Baidu's AI "tracks" — it is a separate **value-unlocking event**.

| Metric | Data |
|------|------|
| Baidu's stake | **57.67%** (remains a subsidiary post-listing) |
| Latest valuation | **RMB 21 billion** (July 2025 funding round) |
| J.P. Morgan's 2026 valuation forecast | **RMB 80 billion** |
| Forecast 2026 revenue | **RMB 8.3 billion** (vs. RMB 1.3 billion in 2025) |
| Listing process | Confidential filing with the Hong Kong Stock Exchange (January 2026) + STAR Market IPO coaching (May 2026) |
| Market position | Third in China's GPU market (Nvidia 70% > Huawei Ascend 23% > Kunlun) |
| Flagship clients | China Mobile's billion-scale procurement, China Merchants Bank, China Southern Power Grid |

> Data sources: IT Home, 36Kr, Sina Finance, The Paper.

**At J.P. Morgan's RMB 80 billion valuation, Baidu's 57.67% stake would be worth about RMB 46.1 billion (about $6.3 billion) — roughly 13% of Baidu's current market cap.**

But note:

1. The RMB 80 billion valuation is based on a forecast 2026 revenue of RMB 8.3 billion — implying roughly 10x P/S, which is not cheap
2. Whether revenue can jump from RMB 1.3 billion to RMB 8.3 billion (a 6x increase) is highly dependent on the pace of domestic AI-chip substitution
3. The Kunlun IPO itself carries uncertainty — STAR Market review has been tightening, and the Hong Kong IPO subscription environment is lukewarm

**Kunlun is a confirmed "option" in Baidu's hand — its value is not zero, but it also should not be priced at the most optimistic scenario.**

---

## A composite assessment of the three AI tracks

| Track | 2025 revenue scale | Growth rate | Profitability | Competitive position | Rating |
|------|----------------|------|--------|---------|------|
| Ernie large models (consumer) | AI apps ~RMB 10 billion | +5% | Unknown | **11th place** (MAU) | ★★ |
| Apollo Go | Not separately disclosed | — | **Unknown** | **#1 globally** (scale) | ★★★ |
| Baidu AI Cloud | ~RMB 20 billion | +34% | **Unknown** | **5th place** (6.1% share) | ★★★ |
| Kunlun (IPO option) | RMB 1.3 billion (2025) | — | Unknown | **3rd place** (domestic GPUs) | ★★★ |

**A blunt fact: not one of Baidu's three AI tracks, plus Kunlun, has had its profitability fully validated.**

AI revenue of RMB 40 billion, growing 48% — these numbers look great. But if gross margin is very low (or even negative), the faster it grows, the larger the losses. Until Baidu discloses a complete income statement for its AI businesses, the conclusion that "the AI transformation has succeeded" cannot be reached.

**Counterargument**: "The very fact that Baidu doesn't disclose AI gross margin may be precisely because that margin doesn't look good. If AI cloud were profitable and Apollo were profitable, what reason would Baidu have not to tell investors loudly?"

**Rebuttal**: "Baidu's 2025 Non-GAAP net income was still RMB 18.9 billion — showing that even with heavy AI investment, the company overall remains profitable. Core net income in 2026Q1 was RMB 7.6 billion (+48%), and a profit recovery is already underway. The market's pessimism about Baidu has already been fully reflected in the share price."

---

## Summary of this article

| Track | Core judgment |
|------|---------|
| Ernie large models | Leading in technology but has already lost the consumer entry point; must break through via "AI-ified search" rather than a standalone app |
| Apollo Go | #1 in global scale plus a cost advantage, but profitability remains opaque; internationalization is the biggest catalyst |
| Baidu AI Cloud | Sticky government/enterprise clients, fast growth, but only 6% share and facing Volcano Engine's pursuit |
| Kunlun | A confirmed IPO option, but the valuation expectations may be overly optimistic |

**In one line: Baidu's new AI engines are indeed firing up, but not one track has yet "proven itself." Investing in Baidu is essentially a bet that at least one of these engines can reach escape velocity before the old engine runs out of fuel.**

---

## Coming up next

In the next article, we look at the **competitive landscape and core risks** Baidu faces.

Sharp questions to answer:

- Baidu Search is besieged on four sides by Douyin/Weixin/Xiaohongshu/DeepSeek — is there still a chance to turn things around?
- AI investment is massive but returns are uncertain — how big is the risk of "winning on technology, losing on the investment"?
- Is Robin Li's execution a real weakness? O2O burned RMB 20 billion, 91 Wireless lost $1.9 billion, Jidu Auto collapsed — will history repeat itself?

---

*This article is Article 03 in the "Understanding Baidu" series.*
*This series does not constitute investment advice.*
