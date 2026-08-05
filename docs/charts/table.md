---
layout: chart
title: Data Table
description: Economist-style data table with conditional formatting and multi-index support.
permalink: /docs/charts/table/
---

# `plot_table()`

Plots an Economist-style data table using Matplotlib primitives. Supports multi-index DataFrames, column-level configuration, cell-level styling, and rule-based conditional highlighting.

## Quick Example

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({
    "Company": ["Apple", "Microsoft", "Google", "Amazon", "Meta"],
    "Revenue (B)": ["$394.3B", "$211.9B", "$307.4B", "$574.8B", "$134.9B"],
    "YoY Growth": ["+2.0%", "+15.8%", "+8.7%", "+11.8%", "+15.7%"],
    "Market Cap (T)": ["$3.44T", "$3.12T", "$2.17T", "$1.87T", "$1.27T"]
})

cc.plot_table(
    data=df,
    title="Big Tech financial Snapshot",
    subtitle="Fiscal year 2024 results",
    options={"rowLabelWidthPct": 0.25}
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/table_basic.png' | relative_url }}" alt="Table" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Table.</em>
</div>


## Data Requirements

- `pd.DataFrame` or `list` of rows. Supports `MultiIndex` for grouped row headers.

## Parameters

<table class="param-table">
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Type</th>
      <th>Default</th>
      <th>Scope</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>data</code></td><td><code>pd.DataFrame | list</code></td><td>Built-in</td><td><span class="badge common">Common</span></td><td>Tabular data to plot. Supports MultiIndex.</td></tr>
    <tr><td><code>output_path</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>File path to save.</td></tr>
    <tr><td><code>width</code></td><td><code>int | None</code></td><td>Auto</td><td><span class="badge common">Common</span></td><td>Image width in pixels.</td></tr>
    <tr><td><code>height</code></td><td><code>int | None</code></td><td>Auto</td><td><span class="badge common">Common</span></td><td>Image height in pixels.</td></tr>
    <tr><td><code>aspect_ratio</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td><code>"square"</code>, <code>"landscape"</code>, etc.</td></tr>
    <tr><td><code>title</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Bold header text.</td></tr>
    <tr><td><code>subtitle</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Secondary text.</td></tr>
    <tr><td><code>bg_color</code></td><td><code>str | None</code></td><td><code>"#f4f3f0"</code></td><td><span class="badge common">Common</span></td><td>Background hex color.</td></tr>
    <tr><td><code>scale_text</code></td><td><code>bool</code></td><td><code>True</code></td><td><span class="badge common">Common</span></td><td>Scale fonts proportionally.</td></tr>
    <tr><td><code>columns</code></td><td><code>list[dict]</code></td><td>Auto</td><td><span class="badge unique">Unique</span></td><td>Column-specific configs (width, alignment, format).</td></tr>
    <tr><td><code>cellStyles</code></td><td><code>dict</code></td><td><code>None</code></td><td><span class="badge unique">Unique</span></td><td>Per-cell styling by <code>(row_idx, col_idx)</code> key.</td></tr>
    <tr><td><code>highlightRules</code></td><td><code>list[dict]</code></td><td><code>None</code></td><td><span class="badge unique">Unique</span></td><td>Auto-highlight rules: ranges, callables, positive-negative coloring.</td></tr>
  </tbody>
</table>

## Common Scenarios

### Conditional Heatmap

Highlight cells based on value ranges:

```python
df = pd.DataFrame({
    "Region": ["North", "South", "East", "West"],
    "Revenue (B)": [45.2, 38.1, 52.7, 41.3],
    "Growth (%)": [12.3, -5.2, 18.1, 8.7],
    "Margin (%)": [1, 18.2, 31.0, 22.8]
})

cc.plot_table(
    data=df,
    title="Performance Matrix",
    options={"rowLabelWidthPct": 0.25},
    highlightRules=[
        {"col": 1, "condition": "positive-negative"},
        {"col": 2, "condition": "range", 
        "min_color": "#FF2C2C", "max_color": cc.config.BACKGROUND_COLOR, 
        "min": 18.2, "max": 31}
    ]
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/table_highlights.png' | relative_url }}" alt="Table" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Table.</em>
</div>

### Custom Column Widths

```python
df = pd.DataFrame({
    "Region": ["North", "South", "East", "West"],
    "Revenue (B)": [45.2, 38.1, 52.7, 41.3],
    "Growth (%)": [12.3, -5.2, 18.1, 8.7],
    "Margin (%)": [1, 18.2, 31.0, 22.8]
})

cc.plot_table(
    data=df,
    columns=[
        {"name": "Revenue", "width_pct": 0.25, "align": "right"},
        {"name": "Growth", "width_pct": 0.25, "align": "right"},
        {"name": "Margin", "width_pct": 0.25, "align": "right"}
    ]
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/table_widths.png' | relative_url }}" alt="Table" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Table.</em>
</div>
