# The Real Level of GLM's Large Models

> *Understanding Zhipu AI* series · Part 02 · Technology and products
> Reading time: ~10 minutes

---

## GLM-5.1: has it truly caught up with the global frontier?

Is topping the benchmark leaderboards something you can game, or a genuine reflection of technical strength? That is the key question for understanding Zhipu.

On April 8, 2026, Zhipu released GLM-5.1, just two months after its predecessor GLM-5. The official claim is that it is "fully on par with Claude Opus 4.6" — how much is that claim really worth?

### Laying out the hard numbers

| Benchmark | GLM-5.1 result | Comparison | Assessment |
|---------|------------|---------|------|
| SWE-bench Pro | **World's best** | Surpasses Claude Opus 4.6 | Genuinely top-tier engineering capability |
| SWE-bench Verified | **77.8** | Highest score among open-source models | Strong practical engineering ability |
| Terminal-Bench 2.0 | **56.2** | Highest score among open-source models | Leading terminal-operation capability |
| Artificial Analysis v4.0 Index | **50 points** | First time an open-weight model has reached this score | A new benchmark for overall capability |

(Source: Zhipu technical report, Artificial Analysis, official SWE-bench leaderboard)

This data points to one thing: **on the coding and engineering dimension, GLM-5.1 genuinely stands among the global elite**.

**But two caveats need to be kept clearly in view**:

First, benchmark performance is not the same as real-world usage experience. SWE-bench tests "given a GitHub issue, can the model automatically generate a correct code patch" — a core AI-coding scenario, but not a proxy for general intelligence. On dimensions like creative writing, complex reasoning, and multi-turn conversation, there is no authoritative third-party evaluation yet of the gap between GLM-5.1 and Claude or GPT-5.

Second, the window of generational advantage in models is extremely short. GLM-5.1 launched on April 8, but Anthropic, OpenAI, and Google are all iterating rapidly on new models too. In the large-model field, **the half-life of a technical lead is roughly 3-6 months**.

### Breaking down the technical architecture

Several key technical choices behind GLM-5:

| Technical dimension | GLM-5/5.1 approach | Meaning |
|---------|-------------|------|
| Parameter count | **744 billion** (up from 355 billion in the prior generation) | Parameter count has doubled |
| Architecture | Sparse MoE (mixture of experts) | Only about **40 billion parameters** are activated per inference |
| Pretraining data | **28.5 trillion tokens** (up from 23 trillion) | Data volume up 24% |
| Context window | **200K tokens** | Strong long-context processing capability |
| Reinforcement learning | Proprietary "Slime" asynchronous RL framework | Supports more complex RL training |
| Attention mechanism | Incorporates DeepSeek Sparse Attention | Reduces deployment cost |
| Domestic-chip support | Huawei Ascend, Moore Threads, Cambricon | A "self-sufficient and controllable" narrative |

(Source: GLM-5 technical report, Zhipu official documentation)

A few points worth noting:

The **MoE architecture** is a smart choice. A 744-billion-parameter model that activates only about 40 billion per inference means inference cost is far lower than a dense model of the same parameter scale. This is consistent with DeepSeek's technical approach — trading architectural innovation for cost-efficiency.

**Incorporating DeepSeek's sparse attention** shows that Zhipu is pragmatic enough on the technical front not to shy away from adopting a competitor's superior approach.

**Domestic-chip support** is a policy plus given the backdrop of US-China tech rivalry, since running on Huawei Ascend is a point in Zhipu's favor — but it also means hardware performance may be constrained by the gap between domestic chips and Nvidia's.

**Counterpoint**: training a 744-billion-parameter MoE model is extremely expensive, and Zhipu's annual R&D spend of **RMB 3.18 billion** is only middling-to-low among global AI companies. Anthropic raised **$8 billion** in 2025, and OpenAI's figures run into the tens of billions. Over the long run, it's a big open question whether Zhipu has enough ammunition for the compute arms race.

---

## The product lineup: one bright spot, one weak point, two potential winners

### Zhipu Qingyan: ceding the consumer market

| Metric | Zhipu Qingyan | Doubao (ByteDance) | DeepSeek | Tongyi Qianwen (Alibaba) |
|------|---------|------------|----------|---------------|
| MAU (mid-2025) | **~8.38 million** | **227 million** | Growing rapidly | Growing rapidly |
| Registered users | 25 million | — | — | — |
| Traffic entry point | None | Douyin ecosystem | Word of mouth | Taobao/DingTalk ecosystem |

(Source: Sensor Tower, Quantum Bit (QbitAI), each company's public data)

The data is brutal enough that it needs no further analysis: **Zhipu Qingyan has already fallen a full order of magnitude behind the tech giants on the consumer side**.

The core reason isn't that the model is bad — it's that Zhipu **has no traffic entry point**.

- ByteDance has Douyin (700 million+ daily active users), so Doubao can be embedded across short video, search, e-commerce, and every other scenario
- Alibaba has Taobao and DingTalk, so Tongyi Qianwen can directly serve hundreds of millions of users
- Baidu has its search engine, so Ernie Bot naturally captures search traffic
- What does Zhipu have? **Nothing**. It is a pure AI technology company with no consumer-facing traffic pool of its own

DeepSeek likewise has no traffic entry point, but it achieved viral spread through "extreme cost-efficiency plus open-source community word of mouth." Zhipu hasn't managed that either — its spread relies mainly on the technical community and enterprise clients, lacking mass-market buzz.

**Counterpoint**: the consumer market may simply not be the battle Zhipu should be fighting. Anthropic also doesn't build consumer products (Claude is aimed more at developers and enterprises), yet Anthropic is valued at over $60 billion. Zhipu's correct path may be to abandon consumer and go all-in on on-premise enterprise plus API.

### MaaS/API platform: the real growth engine

This is Zhipu's brightest business line:

| Metric | Data | Source |
|------|------|------|
| Registered platform users | **4 million+** | Zhipu 2025 annual report |
| Paying users | **220,000** | Prospectus |
| Enterprise clients | **12,000** | Prospectus |
| Countries covered | **218** | Zhipu annual report |
| MaaS ARR | **~RMB 1.7 billion (about $250 million)** | Securities Times |
| ARR year-over-year growth | **60x** | Securities Times |
| Q1 2026 API call-volume growth | **400%** | Zhipu earnings call |
| Q1 2026 API pricing increase | **83%** | Zhipu earnings call |

(Source: Zhipu annual report, prospectus, Securities Times reporting)

**Rising volume alongside rising price** is a very good signal — it indicates demand isn't being "bought" through discounting, but reflects genuine market pull.

CEO Zhang Peng summed up the 2026 strategy in his earnings call with a single phrase: "**token volume**." This mirrors Anthropic's thinking closely — grow the developer ecosystem through the API first, then achieve profitability through economies of scale.

**Counterpoint**: an ARR of RMB 1.7 billion sounds impressive, but actual recognized revenue was only RMB 190 million (the cloud portion). ARR is an annualized figure that includes a large amount of contract value not yet booked. And the API market is in the midst of a brutal price war — DeepSeek's API pricing is an order of magnitude lower than Zhipu's. Whether Zhipu's 83% price increase can hold if DeepSeek keeps cutting prices is a big open question.

### AutoGLM: an opening move in AI agents

AutoGLM is Zhipu's push into AI agents, positioned as "an AI that can operate your phone":

- The **world's first** AI agent framework with "phone use" capability
- Can autonomously operate **50+ high-frequency apps**, including WeChat, Taobao, Douyin, and Meituan
- Can complete complex, multi-step tasks such as ordering food delivery or booking flights, in **dozens of steps**
- Launched in December 2025

(Source: Zhipu's official website, Electronic Engineering Album/EEPW)

AI agents are seen as one of the most commercially promising directions for large models to land in. If AutoGLM can become a "universal AI assistant" on mobile, its commercial value could far exceed that of API calls.

**But the real-world challenges are significant**: Ant Group's Lingguang, ByteDance's Doubao, and Apple's Apple Intelligence are all pursuing similar goals. Zhipu has no hardware entry point on mobile and must rely on partnerships with manufacturers like Samsung and Honor for pre-installation — leaving its distribution channel in others' hands.

### CogVideoX: AI video generation

- A paper accepted at ICLR 2025 (academic recognition)
- A 3D causal VAE architecture
- Can generate 10-second videos at 768x1360 resolution
- Competes with Sora, Kling (Kuaishou), and Vidu (Shengshu Technology)

(Source: ICLR 2025, Zhipu technical report)

Video generation is a track that hasn't yet produced a clear business model. CogVideoX has solid academic standing, but it still has a way to go before large-scale commercialization.

---

## Open-source strategy: smart, but not without cost

Zhipu has adopted **fully open source under the MIT license** — the most permissive open-source license, meaning anyone can freely use, modify, and commercialize Zhipu's models.

| Open-source strategy comparison | Zhipu | DeepSeek | Meta (Llama) | Alibaba's Qwen |
|------------|------|----------|-------------|---------|
| License | MIT (fully open) | MIT | Llama License (restricted) | Apache 2.0 |
| Open-source scope | Full model + code | Full model + code | Model weights | Full model + code |
| Commercial restrictions | None | None | Authorization required above 700 million monthly active users | None |

(Source: each model's official GitHub repository)

The benefits of an open-source strategy are obvious: it quickly builds a developer ecosystem, boosts brand influence, and draws enterprise clients in through free trials before conversion to paying customers.

**But the cost is equally clear**: you're giving your most core technology away for free to everyone — including your competitors. DeepSeek and Qwen are likewise fully open source, and the technical gap among the three is being rapidly narrowed.

The endgame of open-source competition isn't "whose model is best" — it's **who can build the strongest commercial ecosystem around the open-source model** (API platform, enterprise services, application integration). On this front, Zhipu currently trails both DeepSeek and Qwen.

---

## Summary of this piece: top-tier technology, an uneven product lineup

| Dimension | Assessment | Risk factor |
|------|------|--------|
| Model technology | GLM-5.1 is genuinely top-tier | The window of generational advantage is short (3-6 months) |
| Consumer product | Already left 27x behind by big tech | No traffic entry point, no short-term fix |
| API/MaaS | Extremely fast growth, rising volume and price | Large gap between ARR and recognized revenue; price-war threat |
| AI agents | First-mover advantage, but distribution is in others' hands | Every giant is pursuing this too |
| Video generation | Academically leading, commercialization unproven | The track itself is immature |
| Open-source ecosystem | Fully open under MIT, developer-friendly | Rivals are equally open source, eroding differentiation |

In one line: **Zhipu's technology genuinely delivers, but there is still a long road between "strong technology" and "making money."**

---

## Coming up next

In the next piece, we widen the lens to the entire Chinese large-model race —

- Who is Zhipu's real rival? What are the respective strategies of DeepSeek, Baidu's Ernie, MiniMax, and Moonshot AI?
- Is the "big five" lineup among startups stable? Who might fall behind?
- Big tech (ByteDance, Alibaba, Tencent) versus startups — how does this fight play out?
- What exactly is Zhipu's competitive niche?

---

*This is Part 02 of the "Understanding Zhipu AI" series. Two more installments will follow.*
*This series is written based on public information and does not constitute investment advice. The AI industry moves extremely fast — figures in this article are current as of May 2026; please refer to the latest disclosures.*
