# Technical Path — MoE Architecture, the Open-Source Strategy, and the Training-Efficiency Breakthrough

> Understanding DeepSeek series · Part 02
> Reading time: approximately 10 minutes

---

## Why start with the technology?

A 270-person team trained a globally frontier large model for $5.6 million. If this were purely luck, it wouldn't be worth researching; if it is structural, it changes the competitive logic of the entire AI industry.

There is only one way to judge this: understand the technical path. This article will do its best to explain the four core innovations in non-technical language.

---

## Innovation One: MoE Architecture — Doing the Same Order of Computation on 1/10 the Electricity Bill

### What is MoE?

Traditional large models (such as early GPT-4) are "dense models" — every inference call engages **all parameters**. A model with one trillion parameters uses the full trillion parameters for every single question.

MoE (Mixture of Experts) takes a completely different approach: split the model into **multiple "expert modules,"** and activate only a small subset of them on each inference call.

An analogy: a law firm with 500 lawyers doesn't send all 500 to meet a client — it dispatches only the 5 most relevant experts based on the type of case.

DeepSeek V3's numbers:

| Metric | Value |
|------|------|
| Total parameters | **671 billion** (671B) |
| Parameters activated per call | **37 billion** (37B) |
| Activation ratio | Approximately **5.5%** |

V4-Pro goes further:

| Metric | Value |
|------|------|
| Total parameters | **1.6 trillion** (1.6T) |
| Parameters activated per call | **49 billion** (49B) |
| Activation ratio | Approximately **3%** |

(Source: DeepSeek technical papers, Hugging Face model pages)

**What does this mean?** V4-Pro has a "knowledge capacity" of 1.6 trillion parameters, but each computation only consumes the compute cost of 49 billion parameters. It gets both breadth of knowledge and efficiency of inference.

**Counterargument**: MoE is not DeepSeek's invention — Google's Switch Transformer (2021) and Mixtral (2024) both use MoE. DeepSeek's contribution is **pushing MoE to engineering extremes at ultra-large scale**, but that doesn't mean other companies can't replicate it. In fact, within weeks of V4's release, multiple labs were already researching similar architectures.

### MoE's key advantages

| Advantage | Description |
|------|------|
| Low training cost | V3 was trained for only **$5.6 million**, whereas a dense model of comparable performance would require hundreds of millions of dollars |
| Low inference cost | Only 3-5% of parameters are activated per call, sharply lowering the electricity cost per inference |
| Good scalability | More "experts" can keep being added without a proportional increase in inference cost |

---

## Innovation Two: The MLA Attention Mechanism — Solving the Memory Bottleneck for Long Text

Large models hit a technical bottleneck when processing long text: the **KV-cache** (key-value cache) grows linearly with context length, consuming enormous amounts of GPU memory.

DeepSeek's **MLA (Multi-head Latent Attention)** performs low-rank compression on the attention heads, sharply reducing the memory footprint of the KV-cache.

Building on this, V4 further introduces a hybrid mechanism of **CSA (Compressed Sparse Attention)** and **HCA (Heavily Compressed Attention)**:

| Metric | Compared to V3 |
|------|--------|
| Compute per token of inference | Only **27%** of V3's |
| KV-cache footprint | Only **10%** of V3's |
| Context window | Expanded from 128K to **1 million tokens** |

(Source: DeepSeek V4 technical paper)

**Why does this matter?** A 1 million token context window means being able to read an entire book or an entire codebase in one pass. And the compression of the KV-cache means the hardware cost of this capability is sharply reduced — not by piling on more expensive GPUs, but through smarter algorithms.

---

## Innovation Three: FP8 Mixed-Precision Training and R1-Zero

### FP8 training

Traditional large models are trained using FP16 (16-bit floating point) or BF16. DeepSeek V3 is **the first open-source large model to successfully complete full training using FP8 (8-bit floating point)**.

Halving the bit width has direct effects:

- Memory footprint cut in half
- Compute throughput nearly doubled
- Total training cost further reduced

(Source: DeepSeek V3 arXiv paper)

**Counterargument**: FP8 training has been discussed in academia for years, and NVIDIA's H100/H200 already support FP8 compute natively. DeepSeek's contribution is **being the first to run a complete FP8 training pipeline at ultra-large scale**, but this technique will quickly be adopted across the industry.

### R1-Zero: a milestone in pure reinforcement learning

In January 2025, DeepSeek R1 was released along with a research result — **R1-Zero**.

Traditionally, training a large model's reasoning ability requires first using human-annotated "chain of thought" data for supervised fine-tuning (SFT), then applying reinforcement learning (RL). This process relies on a large amount of human annotation.

R1-Zero's breakthrough is: **skipping supervised fine-tuning entirely, using only reinforcement learning, and having the model spontaneously develop chains of reasoning on its own.**

The academic community views this as a landmark event — it hints that **reasoning ability may not need to be taught to an AI step by step by humans; AI can learn to "think" through self-play.**

**Counterargument**: R1-Zero's actual performance falls short of R1, which went through the full SFT+RL pipeline. Its academic significance outweighs its engineering significance. But it validates a theoretical path, and the long-term impact of that path may far exceed its short-term benchmark scores.

---

## Innovation Four: Full MIT Open Source — Moat or Self-Inflicted Wound?

All of DeepSeek's core models — V3, R1, V4 — are open-sourced entirely under the **MIT license**. This is one of the most permissive open-source licenses, which means:

- Anyone can download the model weights for free
- They can be used for commercial purposes
- Modified versions are not required to also be open-sourced
- Training code and tools are also all made public

**38% of new AI papers in Q1 2025 cited DeepSeek's tools or datasets** (Source: DemandSage statistics). On Hugging Face, DeepSeek models are downloaded more than **800,000 times** per month.

### Pros and cons of the open-source strategy

| Dimension | Bull case (the "moat" argument) | Bear case (the "self-destruction" argument) |
|------|-----------------|---------------|
| Ecosystem | Once a developer ecosystem is built, it's extremely hard to migrate away from | Others can take the code and train their own competing models |
| Talent attraction | Top researchers worldwide are willing to contribute to open-source projects | Core intellectual property is given away for free |
| Brand | "The Linux of AI" — enormous influence | The Linux Foundation doesn't make money |
| Commercial | Low-priced API + open source = capturing the developer market | Competitors use your model to build competing products |
| Security | Transparent code leads to more thorough security audits | Malicious users can strip out the safety guardrails |

**One fact that can't be ignored**: as of May 2026, DeepSeek ranks **first in the world** in open-source large models, with its GitHub repositories accumulating more than **70,000 stars** in total (Source: GitHub). On the "open-source AI" track, DeepSeek has built a significant first-mover advantage.

**But another fact is equally impossible to ignore**: Anthropic (Claude) and OpenAI have taken the completely opposite closed-source path, and both are far ahead of DeepSeek commercially. Whether open-source influence can be converted into a sustainable competitive advantage remains an open question.

---

## V4's Adaptation to Huawei Ascend: A Key Turning Point

On April 24, 2026, when DeepSeek V4 was released, one easily overlooked detail was included: **it simultaneously announced full support for Huawei's Ascend 950 chip.**

This means:

| Change | Before | After |
|------|------|------|
| Training dependency | Primarily reliant on NVIDIA H800 | Beginning to adapt to Huawei Ascend |
| Inference deployment | CUDA ecosystem (NVIDIA) | CANN framework (Huawei) |
| Supply chain risk | Extremely high (U.S. chip ban) | Has a backup path |

Huawei's Ascend 950 super node achieved single-card decoding throughput of **4,700 TPS** and a first-token latency of about **20ms** on V4-Pro (Source: Huawei Computing, Sciencenet).

**This is the first time a world-class open-source large model has achieved full-stack deployment — from training to inference — on domestic chips**, without relying on any NVIDIA hardware.

**Counterargument**: the Ascend chip still lags NVIDIA's latest H200/B100 in performance. Huawei's own capacity ramp-up needs time — V4-Pro's high-end inference service is currently constrained by compute, and pricing is not expected to drop substantially until the Ascend 950 reaches mass production in the second half of 2026. "De-Americanization" is the direction, but it is far from complete.

---

## How Long Can the Technical Lead Last?

This is the hardest question to answer. Here are the arguments on both sides, directly:

### Reasons to be bullish

1. **The organizational capability behind algorithmic innovation**: a 270-person team has continuously produced three generations of breakthrough results — V3, R1, V4 — indicating extremely high "research density" within the team
2. **The cost advantage has a compounding effect**: lower training cost leads to faster iteration leads to further lower cost
3. **The open-source ecosystem moat**: cited by 38% of new papers globally; once a developer ecosystem locks in, it's very hard to migrate away
4. **Early domestic-chip adaptation**: the experience on Ascend will become a benchmark for later domestic substitution efforts

### Reasons to be bearish

1. **The MoE architecture is not a secret**: the technical papers are fully public, and competitors can quickly catch up
2. **Talent attrition is already happening**: from late 2025 through early 2026, multiple core members departed to join Xiaomi, Tencent, and ByteDance (Source: 36Kr)
3. **No equity incentives**: the 270-person elite team has none of the equity lock-up mechanisms of a listed company
4. **The chip gap**: the Ascend adaptation lowers supply-chain risk, but the efficiency of training frontier models may still be constrained

**A relatively cautious judgment is**: the technical lead will most likely be maintained for **1-2 years**. A lead of 3 years or more depends on team stability, chip supply, and how fast competitors catch up — all of which carry significant uncertainty.

---

## Coming Up Next

Technology is only the starting point. In the next article, we'll answer a sharper question — **where does this lab's money come from? How far can it go?**

Questions to unpack:

- What exactly is High-Flyer Quant? How long can its profits sustain DeepSeek?
- What does the 50 billion yuan first funding round mean? Is the "idealism" still there?
- Where does DeepSeek stand in its competition with OpenAI, Anthropic, and Google?
- Is "not commercializing" a strategy, or a lack of choice?

---

*This article is Part 02 of the "Understanding DeepSeek" series.*
*This series does not constitute investment advice. All data sources are cited in the text; corrections are welcome if errors are found.*
