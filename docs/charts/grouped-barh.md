---
layout: chart
title: Grouped Horizontal Bar Chart
description: Multi-series categorical comparisons with grouped horizontal bars.
permalink: /docs/charts/grouped-barh/
---

# `plot_grouped_barh_chart()`

Plots a grouped horizontal bar chart. Best for comparing multiple subgroups across several primary categories — e.g., revenue by product line across regions.

## Quick Example

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({
    "Region": ["North America", "Europe", "Asia Pacific"],
    "2022": [45, 38, 52],
    "2023": [52, 42, 58]
})

cc.plot_grouped_barh_chart(
    data=df,
    title="Average Revenue by Region",
    subtitle="in millions of USD",
    value_suffix="M"
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/grouped_barh_basic.png' | relative_url }}" alt="Grouped Barh" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Grouped Barh.</em>
</div>


## Data Requirements

- **Column 0** — Category labels (`str`)
- **Columns 1…N** — Numeric values for each series. Column headers become the legend labels.

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
      <td><code>start_color</code></td>
      <td><code>str</code></td>
      <td><code>"#000000"</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Hex color for the first series (gradient start).</td>
    </tr>
    <tr>
      <td><code>end_color</code></td>
      <td><code>str</code></td>
      <td><code>"#2323FF"</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Hex color for the last series (gradient end).</td>
    </tr>
    <tr>
      <td><code>bar_padding</code></td>
      <td><code>float</code></td>
      <td><code>0.35</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Fraction of a single bar slot left as whitespace (0–1).</td>
    </tr>
    <tr>
      <td><code>group_padding</code></td>
      <td><code>float</code></td>
      <td>Auto</td>
      <td><span class="badge unique">Unique</span></td>
      <td>Fraction of the group height used as spacing between groups.</td>
    </tr>
    <tr>
      <td><code>bar_labels</code></td>
      <td><code>str</code></td>
      <td><code>"none"</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Controls labels drawn on each bar: <code>"none"</code>, <code>"value"</code>, <code>"name"</code>, <code>"both"</code>.</td>
    </tr>
    <tr>
      <td><code>group_comments</code></td>
      <td><code>list[dict]</code></td>
      <td><code>None</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Per-group annotations in the label region. Keys: <code>heading</code>, <code>subtitle</code>, <code>big_number</code>.</td>
    </tr>
    <tr>
      <td><code>group_separators</code></td>
      <td><code>bool</code></td>
      <td><code>False</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Draw thin horizontal lines between adjacent groups.</td>
    </tr>
  </tbody>
</table>

## Common Scenarios

### Scorecard with Group Comments

Add big-number annotations alongside each group:

```python
df = pd.DataFrame({
    "Sector": ["Cloud Infrastructure", "Digital Advertising", "Consumer Hardware", "Subscription Services"],
    "Q4,2023": [115, 205, 310, 85],
    "Q4,2024": [158, 235, 290, 112]
})

cc.plot_grouped_barh_chart(
    data=df,
    title="Tech Sector Revenue Shifts",
    subtitle="Global revenue comparison in billions (USD)",
    group_comments=[
        {
            "heading": "Cloud Infrastructure", 
            "subtitle": "AI workloads driving explosive growth", 
            "big_number": "+37%"
        },
        {
            "heading": "Digital Advertising", 
            "subtitle": "Ad spend rebounded strongly in Q4", 
            "big_number": "+15%"
        },
        {
            "heading": "Consumer Hardware", 
            "subtitle": "Impacted by global supply constraints", 
            "big_number": "-6%"
        },
        {
            "heading": "Subscription Services", 
            "subtitle": "High retention despite price hikes", 
            "big_number": "+32%"
        }
    ],
    group_separators=True,
    value_suffix="B",
    bar_labels="value"
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/grouped_barh_comments.png' | relative_url }}" alt="Grouped Barh" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Grouped Barh.</em>
</div>

### Gradient Heat

Use a gradient to encode series rank visually:

```python
df = pd.DataFrame({
    "Product": ["Enterprise Suite", "Pro Edition", "Basic Plan", "Free Tier"],
    "High Satisfaction": [72, 65, 45, 38],
    "Neutral": [20, 25, 35, 42],
    "Low Satisfaction": [8, 10, 20, 20]
})

cc.plot_grouped_barh_chart(
    data=df,
    title="Customer Satisfaction by Product Tier",
    subtitle="Gradient colors reinforce the sentiment hierarchy",
    start_color="#000044",
    end_color="#0044CD",
    group_padding=0.25,
    value_suffix="%",
    bar_labels="value"
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/grouped_finance.png' | relative_url }}" alt="Grouped Barh" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Grouped Barh.</em>
</div>
