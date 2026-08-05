---
layout: chart
title: Stacked Bar Chart
description: Part-to-whole distribution across categories with stacked horizontal bars.
permalink: /docs/charts/stacked-bar/
---

# `plot_stacked_bar_chart()`

Plots a stacked horizontal bar chart. Best for showing part-to-whole relationships across categories, such as revenue composition by segment or survey response distributions.

## Quick Example

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({
    "Quarter": ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"],
    "Enterprise": [120, 135, 142, 160],
    "SMB": [80, 85, 95, 110],
    "Consumer": [45, 48, 52, 65]
})
cc.plot_stacked_bar_chart(
    data=df,
    title="Quarterly Revenue Growth",
    subtitle="Revenue breakdown by customer segment (in millions)",
    value_suffix="M",
    bar_labels="value"
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/stacked_bar_basic.png' | relative_url }}" alt="Stacked Bar" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Stacked Bar.</em>
</div>


## Data Requirements

- **Column 0** — Category labels (`str`)
- **Columns 1…N** — Numeric values for each stacked series. Column headers become legend labels.

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
    <tr>
      <td><code>data</code></td>
      <td><code>pd.DataFrame</code></td>
      <td>Built-in</td>
      <td><span class="badge common">Common</span></td>
      <td>First column: category labels. Subsequent columns: numeric series.</td>
    </tr>
    <tr>
      <td><code>output_path</code></td>
      <td><code>str | None</code></td>
      <td><code>None</code></td>
      <td><span class="badge common">Common</span></td>
      <td>File path to save the chart.</td>
    </tr>
    <tr>
      <td><code>width</code></td>
      <td><code>int | None</code></td>
      <td>Auto</td>
      <td><span class="badge common">Common</span></td>
      <td>Image width in pixels.</td>
    </tr>
    <tr>
      <td><code>height</code></td>
      <td><code>int | None</code></td>
      <td>Auto</td>
      <td><span class="badge common">Common</span></td>
      <td>Image height in pixels.</td>
    </tr>
    <tr>
      <td><code>aspect_ratio</code></td>
      <td><code>str | None</code></td>
      <td><code>None</code></td>
      <td><span class="badge common">Common</span></td>
      <td><code>"square"</code>, <code>"landscape"</code>, <code>"vertical"</code>, <code>"1:1"</code>, <code>"2:1"</code>, <code>"1:2"</code>.</td>
    </tr>
    <tr>
      <td><code>title</code></td>
      <td><code>str | None</code></td>
      <td><code>None</code></td>
      <td><span class="badge common">Common</span></td>
      <td>Bold header text.</td>
    </tr>
    <tr>
      <td><code>subtitle</code></td>
      <td><code>str | None</code></td>
      <td><code>None</code></td>
      <td><span class="badge common">Common</span></td>
      <td>Secondary text below title.</td>
    </tr>
    <tr>
      <td><code>bg_color</code></td>
      <td><code>str | None</code></td>
      <td><code>"#f4f3f0"</code></td>
      <td><span class="badge common">Common</span></td>
      <td>Background hex color.</td>
    </tr>
    <tr>
      <td><code>scale_text</code></td>
      <td><code>bool</code></td>
      <td><code>True</code></td>
      <td><span class="badge common">Common</span></td>
      <td>Scale fonts proportionally.</td>
    </tr>
    <tr>
      <td><code>value_suffix</code></td>
      <td><code>str</code></td>
      <td><code>""</code></td>
      <td><span class="badge common">Common</span></td>
      <td>String appended to value labels.</td>
    </tr>
    <tr>
      <td><code>show_percentages</code></td>
      <td><code>bool</code></td>
      <td><code>False</code></td>
      <td><span class="badge common">Common</span></td>
      <td>Format values as percentages.</td>
    </tr>
    <tr>
      <td><code>colors</code></td>
      <td><code>list[str]</code></td>
      <td>Auto</td>
      <td><span class="badge unique">Unique</span></td>
      <td>Explicit list of hex colors for the stacked series.</td>
    </tr>
    <tr>
      <td><code>start_color</code></td>
      <td><code>str</code></td>
      <td><code>"#000000"</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Gradient start color. Overrides <code>colors</code>.</td>
    </tr>
    <tr>
      <td><code>end_color</code></td>
      <td><code>str</code></td>
      <td><code>"#2323FF"</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Gradient end color. Overrides <code>colors</code>.</td>
    </tr>
    <tr>
      <td><code>bar_padding</code></td>
      <td><code>float</code></td>
      <td><code>0.35</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Fraction of bar slot left as whitespace (0–1).</td>
    </tr>
    <tr>
      <td><code>bar_labels</code></td>
      <td><code>str</code></td>
      <td><code>"none"</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Labels on each segment: <code>"none"</code>, <code>"value"</code>, <code>"name"</code>, <code>"both"</code>.</td>
    </tr>
  </tbody>
</table>

## Common Scenarios

### 100% Normalized Stack

Show proportional distribution with percentage labels:

```python
df = pd.DataFrame({
    "Country": ["France", "Sweden", "Germany", "USA", "China", "India"],
    "Fossil Fuels": [45, 12, 230, 2450, 5200, 1150],
    "Nuclear": [350, 55, 32, 780, 410, 45],
    "Renewables": [120, 115, 260, 950, 2400, 310]
})

cc.plot_stacked_bar_chart(
    data=df,
    title="The Global Energy Mix",
    subtitle="Share of total electricity generation by source",
    show_percentages=True, 
    bar_labels="value", 
    aspect_ratio="landscape"
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/stacked_bar_pct.png' | relative_url }}" alt="Stacked Bar" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Stacked Bar.</em>
</div>

### Custom Color Palette

Use brand colors for each segment:

```python
df = pd.DataFrame({
    "Year": ["2021", "2022", "2023", "2024"],
    "Our Brand": [15, 22, 35, 48],
    "Competitor A": [45, 40, 32, 25],
    "Competitor B": [40, 38, 33, 27]
})

cc.plot_stacked_bar_chart(
    data=df,
    title="Market Share Takeover",
    subtitle="Our brand vs top competitors",
    aspect_ratio="1:1",
    colors=["#E40078", "#4B5563", "#9CA3AF"], 
    show_percentages=True,
    bar_labels="value",
    bar_padding=0.5
)

```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/stacked_churn.png' | relative_url }}" alt="Stacked Bar" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Stacked Bar.</em>
</div>
