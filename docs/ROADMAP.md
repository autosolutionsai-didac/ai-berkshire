# ai-berkshire Roadmap

## P0: Near term (1-2 months)

### A-share data-source integration
- Integrate free data sources such as akshare and East Money.
- Cover A-share financials, quotes, and the "dragon-tiger" (top mover) list.
- No changes needed to existing skills; only the data layer is extended.

## P1: Mid term (3-6 months)

### HTML report output
- Add an HTML report format on top of Markdown.
- Support dark mode, a navigation bar, and chart visualization.
- Improve report shareability and reading experience.

### Multi-tier depth modes
- `lite`: 5-minute quick call, fast valuation range and core conclusion.
- `standard`: the current default mode, full multi-agent research.
- `deep`: more cross-validation and historical analogies, institution-grade depth.

### Multi-stock side-by-side comparison
- Support head-to-head comparison of 2-4 stocks on the same dimensions.
- Valuation benchmarking across peers in the same industry.
- Output a comparison matrix and a pick recommendation.

## P2: Long term (6 months+)

### Test coverage
- Add unit tests for core tools (financial_rigor.py, etc.).
- Add regression tests for skill output.
- Ensure iteration does not break existing functionality.

### Portfolio-level analysis
- Portfolio health assessment.
- Industry / geographic concentration analysis.
- Correlation-risk detection.
