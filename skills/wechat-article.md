# WeChat Article: Author-Editor-Reader Three-Agent Collaboration

Conduct deep research on $ARGUMENTS and produce a publish-ready WeChat article. Three agents each play a distinct role: the author writes a deep first draft, the editor refines structure and expression, and the reader reviews it from the target audience's perspective.

**Supported input formats**: a topic description, for example: `Explaining large-model OPD technique`, `Reading the Qwen3 technical report`, `Why Buffett doesn't buy tech stocks`

---

## Design Philosophy

A good WeChat article must satisfy three dimensions at once:
1. **Depth** — worthy of the people who spend time reading it to the end (the author's responsibility)
2. **Readability** — clear structure, good pacing, doesn't drive readers away (the editor's responsibility)
3. **Actually understandable** — the target reader won't give up halfway (the reader's responsibility)

Solo writing easily turns into self-indulgence — the writer thinks it's clear, but the reader can't follow. The essence of three-agent collaboration is to **forcibly introduce an outside perspective**.

---

## Stage One: Research and Material Collection

### Step 1: Define the article's positioning

Before writing, confirm the following (proactively ask if the user hasn't specified):

| Dimension | To confirm | Default |
|------|---------|--------|
| **Target reader** | Level of technical background | Somewhat technical but not a domain expert |
| **Article depth** | Popular science / mid-depth / hardcore | Mid-depth (formulas allowed but must be clearly explained) |
| **Article length** | Word-count range | 3,000-4,000 words |
| **Whether to download original papers/materials** | Need PDFs/figures | Yes |
| **Writing style** | Formal / conversational / sharp | Conversational (like writing to a smart friend) |

### Step 2: Deep research

Use the Agent tool to launch 2-3 research agents **in parallel** and collect enough material:

**Research Agent A: Core content research**
- If it's a paper deep-read: download the paper PDF, extract core contributions, key figures, experimental results
- If it's a technical topic: search for the latest progress, key papers, technical details
- If it's a business/investment topic: search for the latest data, industry reports, competitive landscape

**Research Agent B: Industry context and applications**
- Search for how this technology/topic is being deployed in industry
- Which companies are using it? How well does it work?
- The latest development trends and milestone events

**Research Agent C (optional): Competitor/comparison research**
- Comparison with similar methods/products
- Historical development trajectory
- Future evolution direction

### Step 3: Organize the material framework

After all research agents finish, organize:
1. **Core thesis** (one sentence summarizing the core message the article aims to convey)
2. **Key data** (the 3-5 most impactful data points)
3. **Figure list** (which figures are needed and where they come from)
4. **Article outline** (titles and core content for 6-8 sections)

---

## Stage Two: The Author Agent Writes the First Draft

Use the Agent tool to launch the **Author Agent**, giving detailed writing instructions.

### Author Agent Prompt Template

```
You are a deep technical writer (Author Agent) tasked with writing a WeChat article.

## Target reader
{the reader profile confirmed in Step 1}

## Writing-style requirements
- Pure English expression, avoid mixing languages (when a technical term first appears, give the original term, then use plain language afterward)
- Write like technical popular science for a smart friend, not a translated academic paper
- Use analogies to aid understanding, but they must be apt, not clichéd
- Include key formulas/data, but explain each one in plain language
- No emoji
- Paragraphs no longer than 4 lines (WeChat reading environment)

## Core content
{the organized material, data, and thesis}

## Article-structure requirements
1. **Opening (first 3 paragraphs)**: must have a strong hook — open with the impact of data or a counterintuitive conclusion, not a gentle analogy
2. **Background**: why does this matter? What problem does it solve?
3. **Core content (2-3 sections)**: technical depth is shown here, but every technical point must have a "plain-language translation"
4. **Evidence/case studies**: let data and cases do the talking, no empty rhetoric
5. **Industry impact/outlook**: what this means for the industry
6. **Ending**: close with one shareable judgment, suitable to be screenshotted and forwarded

## Figure requirements
- Paper deep-read articles: you must extract the original figures from the paper PDF and insert them directly into the article with `![description](relative path)`, do not use [Figure X: description] placeholders
- Extraction method: use pdftoppm to render the PDF pages as high-resolution PNGs (at least 900 DPI), then use PIL to crop the target figure region
- Each image no smaller than 500KB, to ensure high definition
- Store images uniformly in the `assets/{topic short name}/` directory
- Non-paper articles: if figures are needed, search for and download suitable images and insert them directly as well

## Formula requirements
- All mathematical formulas use LaTeX format: inline with `$...$`, standalone formulas with `$$...$$`
- Plain-text formulas are forbidden (e.g. `> D_KL(P || Q) = ...`); they must use LaTeX rendering format
- Every formula must still be accompanied by a "plain-language translation"

Please write the complete first draft, about {target word count} words.
```

### After the Author Agent finishes

Check whether the draft file was generated, and read the full text to confirm content completeness.

---

## Stage Three: Editor Agent + Reader Agent Review in Parallel

Once the first draft is complete, use the Agent tool to launch the Editor Agent and the Reader Agent **in the same message**.

### Editor Agent Prompt Template

```
You are a senior WeChat editor (Editor Agent). Please review and refine the following article.

## Review criteria
1. **Title**: does it attract clicks in a feed? Will it get truncated (over 30 characters)?
2. **Opening**: can the first 3 paragraphs retain readers? Is the hook strong enough?
3. **Structure**: is the logical chain smooth? Any jumps or gaps?
4. **Depth-readability balance**: are the formula/technical parts genuinely accessible? Anywhere that "pretends to be accessible but doesn't actually explain"?
5. **Pacing**: any paragraphs that are too long? Is each section an appropriate length?
6. **Figures**: are images actually inserted (not placeholders)? Do they appear where readers most need visual aid?
7. **Ending**: is it shareable? Will readers want to forward it after finishing?

## Full article text
{the complete first draft}

## Output format
1. Overall assessment (3-5 sentences)
2. Title revision suggestions (give 2-3 alternatives)
3. Section-by-section revision suggestions (give specific "original → suggested revision" comparisons)
4. The 3 most critical improvement points
```

### Reader Agent Prompt Template

```
You are a {target reader profile} (Reader Agent). Please review the following article from a reader's perspective.

## Your background
{a concrete description of the target reader's knowledge level and reading habits}

## Full article text
{the complete first draft}

## Please answer the following questions
1. After reading the first 3 paragraphs, would you keep reading? Why?
2. Where do you "not understand" or "need to reread to understand"? Which sentence specifically?
3. Did you understand the technical/formula parts? Did the "plain-language translation" help you?
4. Is the article's core analogy apt? Is there a better one?
5. Too long or too short? Where would you lose patience?
6. After reading, can you summarize the article's core viewpoint in one sentence?
7. Would you forward this article? What would you say when forwarding it?
8. Is there anything you wanted to learn that the article didn't cover?
```

---

## Stage Four: Finalization

### Step 1: Synthesize the two agents' feedback

Focus on the following high-frequency issues:

| Issue type | Common editor feedback | Common reader feedback | How to handle |
|---------|------------|------------|---------|
| Weak opening | Hook not strong enough | No motivation to continue past first 3 paragraphs | Rewrite the opening with data/a counterintuitive conclusion |
| Technical section drives readers away | Formulas too dense | A section needs 3 rereads | Cut formulas or convert to images, add more intuitive analogies |
| Sluggish pacing | A section too long | Lost patience somewhere | Merge or trim (especially repeated technical explanations in the second half) |
| Weak ending | Lacks shareability | Won't forward | Rewrite as one screenshottable, shareable judgment |
| Conceptual jumps | Logical gaps | "Suddenly can't follow" somewhere | Add transition sentences or background explanation |

### Step 2: Execute the revisions

Rewrite the article based on the feedback. Core revision principles:

1. **Issues flagged by both editor and reader must be fixed**
2. **Issues flagged by only the editor should very likely be fixed** (the editor's professional judgment is usually accurate)
3. **Issues flagged by only the reader are fixed case by case** (reader feedback represents real experience, but not every item needs a response)
4. **When the two conflict, lean toward the reader** (the editor pursues perfection, but the reader's experience is the ultimate standard)

### Step 3: Extract figures

Paper deep-read articles must complete figure extraction before finalization:

1. **Render**: `pdftoppm -png -r 900 -f {page number} -l {page number} paper.pdf /tmp/page` (start at 900 DPI; if the image is under 500KB, raise to 1200 or 1500 DPI)
2. **Locate**: first render the full page at 150 DPI, visually confirm the pixel coordinates of each figure
3. **Crop**: crop by coordinates with PIL, save with `compress_level=1`, ensuring each is ≥ 500KB
4. **Store**: save to the `assets/{topic short name}/` directory, named `fig{index}-{description}.png`
5. **Insert**: reference in the article with `![description](../../assets/{topic short name}/fig{index}-{description}.png)`

### Step 4: Produce the final file

Save the finalized draft as an md file, appending the original paper/material links at the end of the file:

```markdown
**Original paper:**
- arXiv: {link}
```

---

## File Naming and Storage

| Type | Path | Naming format |
|------|------|---------|
| Technical topic | `reports/AI-Industry-Research/` | `wechat-{topic keyword}-{YYYYMMDD}.md` |
| Investment topic | `reports/{Company}/` | `{Company}-wechat-{YYYYMMDD}.md` |
| General topic | `reports/` | `wechat-{topic keyword}-{YYYYMMDD}.md` |

---

## Writing Red Lines

1. **No fabricated data**. Cited data must have a source; if it can't be found, label it "estimate"
2. **No AI tone**. Ban filler phrases like "let's take a look together", "it's worth noting", "one has to say"
3. **No overclaiming**. Technical articles don't say "disruptive" or "revolutionary" — let the data speak
4. **Every formula must have a plain-language explanation**. After each formula there must be a passage of "translated into human terms, this means..."
5. **Formulas must use LaTeX**. `$$...$$` format; plain-text formulas are forbidden
6. **Figures must be actually inserted**. Paper deep-reads extract high-definition original figures from the PDF (≥500KB); `[Figure X]` placeholders are forbidden
7. **Table parenthetical annotations must be precise**. When describing a concept, use an accurate definition, not a vague verb-object phrase (e.g. "text comes from the teacher" rather than "learn the teacher's text")
8. **Keep the analogy consistent throughout**. Use one throughline analogy across the whole article, don't switch to a new analogy in every section
9. **The ending must be shareable**. The last sentence should be worth screenshotting and forwarding on its own
