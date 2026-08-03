---
layout: default
title: Home
nav_order: 1
---
# clean-charts API Reference

> **Version:** 0.12.1 · **License:** MIT · **Python:** ≥ 3.8

`clean-charts` is a Python library for generating premium, publication-quality charts inspired by the clean aesthetics of **McKinsey**, **BCG**, and **The Economist**. Built on top of Matplotlib, it provides high-level functions that produce polished, presentation-ready visualizations with a single function call.

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

## Architecture Overview

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

## Chart Functions Reference

Explore the chart functions based on your analytical goal:

### Trends & Time
| Function | Use Case |
|----------|----------|
| [`plot_time_series()`](reference/time_series.md) | Multi-series line charts with annotations and splines |

### Distributions & Rankings
| Function | Use Case |
|----------|----------|
| [`plot_barh_chart()`](reference/bar_charts.md) | Horizontal bar chart for long labels and ranking |
| [`plot_barv_chart()`](reference/bar_charts.md) | Vertical bar chart for short labels or discrete time |
| [`plot_grouped_barh_chart()`](reference/grouped_barh.md) | Multi-series categorical comparison |
| [`plot_stacked_bar_chart()`](reference/stacked_bar.md) | Absolute or 100% normalized stack distribution |
| [`plot_dumbbell_chart()`](reference/dumbbell.md) | Connected dots showing 'Before vs After' deltas |

### Relationships
| Function | Use Case |
|----------|----------|
| [`plot_scatter_chart()`](reference/scatter_charts.md) | 2D scatter plot for two continuous variables |
| [`plot_grouped_scatter_chart()`](reference/scatter_charts.md) | Quadrant matrix mapping or categorical clusters |
| [`plot_bubble_scatter_chart()`](reference/scatter_charts.md) | 3-variable scatter (dot size encoding) |
| [`plot_bubble_matrix_chart()`](reference/bubble_matrix.md) | Size/color encoded grid for cross-tabulations |

### Part-to-Whole
| Function | Use Case |
|----------|----------|
| [`plot_donut_chart()`](reference/donut.md) | Part-of-whole ring with center label |
| [`plot_waffle_chart()`](reference/waffle.md) | 10×10 waffle grid for 'X out of 100' data |

### Layouts & Components
| Function | Use Case |
|----------|----------|
| [`plot_insight_card()`](reference/insight_card.md) | Bold text card for hero statistics |
| [`plot_table()`](reference/table.md) | Styled data table with conditional formatting |
| [`plot_geofacet()`](reference/geofacet.md) | Geographic small-multiples grid |
| [`plot_dashboard()`](reference/dashboard.md) | Composite mosaic combining multiple charts |

---

## Global Common Parameters

Most functions share these baseline arguments:

| Parameter       | Type           | Description |
|-----------------|----------------|-------------|
| `data`          | `pd.DataFrame` | Input data. Fallbacks to built-in sample if None. |
| `output_path`   | `str \| None`  | Save path. Displays inline if None. |
| `width`, `height`| `int \| None` | Explicit dimensions in pixels. |
| `aspect_ratio`  | `str \| None`  | `"square"`, `"landscape"`, `"vertical"`, `"1:1"`, `"2:1"`, `"1:2"`. |
| `title`         | `str \| None`  | Bold header text (auto-wrapped). |
| `subtitle`      | `str \| None`  | Secondary text below title. |
| `bg_color`      | `str \| None`  | Background hex color (defaults to `#f4f3f0`). |
| `scale_text`    | `bool`         | Scale fonts proportionally with image size. |
