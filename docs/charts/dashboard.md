---
layout: chart
title: Dashboard
description: Composite mosaic combining multiple charts into a single image.
permalink: /docs/charts/dashboard/
---

# `plot_dashboard()`

Combines multiple clean-chart visualizations into a single composite mosaic image. Each sub-chart is rendered independently and composited onto a shared canvas using an ASCII layout string.

## Quick Example

```python
import pandas as pd
import clean_charts as cc

df_ts = cc.get_default_data()
df_barh = pd.DataFrame({
    "Response": ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
    "Count": [42, 31, 18, 6, 3],
})
df_donut = pd.DataFrame({
    "Source": ["Organic", "Direct", "Social", "Referral", "Email", "Paid"],
    "Share": [38.2, 24.5, 15.8, 10.3, 7.1, 4.1],
})
df_dumbbell = pd.DataFrame({
    "Country": ["US", "China", "Germany", "UK", "India", "France"],
    "2010": [14.99, 6.09, 3.42, 2.48, 1.68, 2.65],
    "2023": [25.46, 17.79, 4.46, 3.33, 3.73, 3.05],
})

cc.plot_dashboard(
    charts=[
        (cc.plot_time_series,    {"data": df_ts,       "title": "Market Trends"}),
        (cc.plot_barh_chart,     {"data": df_barh,     "title": "Survey Results"}),
        (cc.plot_donut_chart,    {"data": df_donut,    "title": "Traffic Sources", "center_label": "100%"}),
        (cc.plot_dumbbell_chart, {"data": df_dumbbell, "title": "GDP Comparison", "value_suffix": "T"}),
    ],
    layout="AB\nCD",
    title="Executive Summary Dashboard",
    subtitle="Key metrics and trends at a glance",
    output_path="dashboard.png",
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/dashboard_basic.png' | relative_url }}" alt="Dashboard" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Dashboard.</em>
</div>


## Layout Syntax

The `layout` parameter uses an ASCII string:

- Each **unique letter** maps to one chart (in order of first appearance)
- **Rows** separated by `\n`
- A letter **repeated horizontally** spans multiple columns
- A letter **repeated vertically** spans multiple rows
- A **period** (`.`) denotes an empty cell

| Layout String | Description |
|---------------|-------------|
| `"AB\nCD"` | 2×2 grid, 4 equal charts |
| `"AA\nBC"` | A spans full top row; B and C split the bottom |
| `"ABC"` | Single row, 3 equal-width charts |
| `"AB\nAC"` | A spans left column; B and C stack on the right |
| `"AAB\nCCC"` | A takes 2/3 of top, B takes 1/3; C spans full bottom |

When `layout=None`, an auto-generated grid is created based on chart count.

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
    <tr><td><code>output_path</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>File path to save.</td></tr>
    <tr><td><code>width</code></td><td><code>int</code></td><td><code>1400</code></td><td><span class="badge common">Common</span></td><td>Final image width in pixels.</td></tr>
    <tr><td><code>height</code></td><td><code>int | None</code></td><td>Auto</td><td><span class="badge common">Common</span></td><td>Final image height. Auto-derived from layout aspect ratio.</td></tr>
    <tr><td><code>title</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Dashboard-level title text.</td></tr>
    <tr><td><code>subtitle</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Dashboard-level subtitle.</td></tr>
    <tr><td><code>bg_color</code></td><td><code>str | None</code></td><td><code>"#f4f3f0"</code></td><td><span class="badge common">Common</span></td><td>Canvas background color.</td></tr>
    <tr><td><code>charts</code></td><td><code>list[tuple]</code></td><td><strong>Required</strong></td><td><span class="badge unique">Unique</span></td><td>List of <code>(plot_function, kwargs_dict)</code> tuples. Each specifies a chart and its params.</td></tr>
    <tr><td><code>layout</code></td><td><code>str | None</code></td><td>Auto</td><td><span class="badge unique">Unique</span></td><td>ASCII mosaic string defining spatial arrangement.</td></tr>
    <tr><td><code>padding</code></td><td><code>float</code></td><td><code>0.02</code></td><td><span class="badge unique">Unique</span></td><td>Fractional space between sub-charts (0–0.5).</td></tr>
  </tbody>
</table>

## Notes

- **Any chart function** can be used in a dashboard panel — including `plot_insight_card`, `plot_table`, and `plot_geofacet`.
- Do **not** include `output_path` in individual chart kwargs — it is managed internally.
- For best quality, use `width=1400` or higher for 4+ panel dashboards.
