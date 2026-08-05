---
layout: default
title: Home
permalink: /
---

# clean_charts

> **Version:** 0.12.1 · **License:** MIT · **Python:** ≥ 3.8

`clean_charts` is a Python library for generating premium, publication-quality charts inspired by the clean aesthetics of **McKinsey**, **BCG**, and **The Economist**. Built on top of Matplotlib, it provides high-level functions that produce polished, presentation-ready visualizations with a single function call.

---

## Installation

```bash
pip install clean-charts
```

**Dependencies** (installed automatically):
`matplotlib ≥ 3.5.0`, `pandas ≥ 1.3.0`, `numpy ≥ 1.20.0`, `Pillow ≥ 8.0.0`, `scipy ≥ 1.7.0`, `geopandas ≥ 0.10.0`

---

## Quick Start

```python
import clean_charts as cc
import pandas as pd

# Plot with built-in sample data
cc.plot_time_series(title="Market Trends", subtitle="Monthly index")

# Plot with your own data
df = pd.DataFrame({"Category": ["A", "B", "C"], "Value": [42, 31, 18]})
cc.plot_barh_chart(data=df, title="My Chart", output_path="chart.png")
```

---

## Architecture

```
clean_charts/
├── __init__.py          # Public API re-exports
├── config.py            # Design tokens (colors, fonts, sizes)
├── data.py              # Default sample data & DataFrame conversion
├── _helpers.py          # Shared utilities (display, save, gradients)
├── fonts/               # Bundled Inter font files
└── plots/               # Core charting functions
    ├── time_series.py
    ├── barh.py, barv.py, grouped_barh.py, stacked_bar.py
    ├── scatter.py, grouped_scatter.py, bubble_scatter.py
    ├── donut.py, waffle.py, dumbbell.py
    ├── insight_card.py, bubble_matrix.py, table.py
    └── geofacet.py, dashboard.py
```

---

## Chart Gallery

Explore the full library of chart types:

### Bar Charts

| Function | Description |
|----------|-------------|
| [`plot_barh_chart()`](docs/charts/barh/) | Horizontal bars for long labels and rankings |
| [`plot_barv_chart()`](docs/charts/barv/) | Vertical bars for short labels or time periods |
| [`plot_grouped_barh_chart()`](docs/charts/grouped-barh/) | Multi-series categorical comparison |
| [`plot_stacked_bar_chart()`](docs/charts/stacked-bar/) | Part-to-whole distribution across categories |

### Time Series

| Function | Description |
|----------|-------------|
| [`plot_time_series()`](docs/charts/time-series/) | Multi-series line charts with annotations and splines |

### Scatter Plots

| Function | Description |
|----------|-------------|
| [`plot_scatter_chart()`](docs/charts/scatter/) | 2D scatter for two continuous variables |
| [`plot_grouped_scatter_chart()`](docs/charts/grouped-scatter/) | Quadrant matrix or categorical clusters |
| [`plot_bubble_scatter_chart()`](docs/charts/bubble-scatter/) | 3-variable scatter with dot size encoding |

### Matrix & Grid

| Function | Description |
|----------|-------------|
| [`plot_bubble_matrix_chart()`](docs/charts/bubble-matrix/) | Size/color encoded grid for cross-tabulations |
| [`plot_geofacet()`](docs/charts/geofacet/) | Geographic small-multiples grid |

### Proportions

| Function | Description |
|----------|-------------|
| [`plot_donut_chart()`](docs/charts/donut/) | Ring chart with center label |
| [`plot_waffle_chart()`](docs/charts/waffle/) | 10×10 waffle grid for "X out of 100" data |

### Comparisons

| Function | Description |
|----------|-------------|
| [`plot_dumbbell_chart()`](docs/charts/dumbbell/) | Connected dots showing before vs after deltas |

### Presentation

| Function | Description |
|----------|-------------|
| [`plot_insight_card()`](docs/charts/insight-card/) | Bold text card for hero statistics |
| [`plot_table()`](docs/charts/table/) | Styled data table with conditional formatting |
| [`plot_dashboard()`](docs/charts/dashboard/) | Composite mosaic combining multiple charts |
