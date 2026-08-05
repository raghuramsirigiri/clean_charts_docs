---
layout: chart
title: Horizontal Bar Chart
description: Build horizontal bar charts for ranking and categorical comparisons.
permalink: /docs/charts/barh/
---

# `plot_barh_chart()`

Plots a horizontal bar chart in the Economist style. Best for comparing 2–10 categories with long text labels. Horizontal orientation allows labels to be read naturally left-to-right.

## Quick Example

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({
    "Country": ["Finland", "Denmark", "Iceland", "Israel", "Netherlands", "Sweden"],
    "Happiness Score": [7.80, 7.58, 7.53, 7.47, 7.40, 7.39]
})

cc.plot_barh_chart(
    data=df,
    title="The World's Happiest Countries",
    subtitle="World Happiness Report 2024 (Top 6)",
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/barh_basic.png' | relative_url }}" alt="Barh" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Barh.</em>
</div>

## Data Requirements

The input `data` must be a `pandas.DataFrame` with exactly **two columns**:

- **Column 0** — Category labels (`str`)
- **Column 1** — Numeric values (`float` or `int`)

Rows are displayed in the exact order they appear. Sort your DataFrame before plotting to achieve ranked charts.

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
      <td>2-column DataFrame: [Category labels, Values].</td>
    </tr>
    <tr>
      <td><code>output_path</code></td>
      <td><code>str | None</code></td>
      <td><code>None</code></td>
      <td><span class="badge common">Common</span></td>
      <td>File path to save the chart. Displays inline if <code>None</code>.</td>
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
      <td>Bold header text (auto-wrapped).</td>
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
      <td>Scale fonts proportionally with image size.</td>
    </tr>
    <tr>
      <td><code>value_suffix</code></td>
      <td><code>str</code></td>
      <td><code>""</code></td>
      <td><span class="badge common">Common</span></td>
      <td>String appended to value labels (e.g., <code>"%"</code>, <code>"M"</code>).</td>
    </tr>
    <tr>
      <td><code>show_percentages</code></td>
      <td><code>bool</code></td>
      <td><code>False</code></td>
      <td><span class="badge common">Common</span></td>
      <td>Format values as percentages.</td>
    </tr>
    <tr>
      <td><code>color</code></td>
      <td><code>str</code></td>
      <td><code>"#000000"</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Hex color for all bars.</td>
    </tr>
    <tr>
      <td><code>bar_padding</code></td>
      <td><code>float</code></td>
      <td><code>0.35</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Fraction of bar slot left as gap between bars (0–1). Higher = thinner bars.</td>
    </tr>
  </tbody>
</table>

## Common Scenarios

### Minimalist Ranking

Ultra-thin bars for dense reports where the text hierarchy matters more than the bars:

```python
df = pd.DataFrame({
    "City": ["Vienna", "Copenhagen", "Zurich", "Melbourne", "Calgary", "Geneva"],
    "Index Score": [98.4, 98.0, 97.1, 97.0, 96.8, 96.8]
})
cc.plot_barh_chart(
    data=df,
    title="The World's Most Livable Cities",
    subtitle="Global Livability Index 2024",
    bar_padding=0.6,
    color="#000000",
    value_suffix=" pts",
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/barh_compact.png' | relative_url }}" alt="Barh" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Barh.</em>
</div>

### Percentage Labels

Show proportions instead of raw values:

```python
df = pd.DataFrame({"Region": ["North", "South", "East", "West"], "Share": [45, 25, 20, 10]})

cc.plot_barh_chart(
    data=df,
    title="A widening regional divide",
    subtitle="The North captures 45% of the market, more than the East and West combined",
    show_percentages=True,
    color="#D0006C"
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/barh_percentages.png' | relative_url }}" alt="Barh" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Barh.</em>
</div>
