---
layout: chart
title: Vertical Bar Chart
description: Build vertical bar charts for ordinal data and short-label categories.
permalink: /docs/charts/barv/
---

# `plot_barv_chart()`

Plots a vertical bar chart in the Economist style. Best for comparing ordinal data or short-label categories like quarters, months, or single-letter codes.

## Quick Example

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Revenue": [12.5, 14.2, 11.8, 16.5]
})

cc.plot_barv_chart(
    data=df,
    title="Quarterly Revenue",
    subtitle="Vertical orientation is best for short labels or time series",
    value_suffix="M"
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/barv_basic.png' | relative_url }}" alt="Barv" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Barv.</em>
</div>


## Data Requirements

Identical to [`plot_barh_chart()`](../barh/) — a 2-column DataFrame with [Category labels, Values].

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
      <td>Scale fonts proportionally with image size.</td>
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
      <td>Fraction of bar slot left as gap (0–1).</td>
    </tr>
  </tbody>
</table>

## Common Scenarios

### Timeline Histogram

Visualize discrete time periods as a histogram-style chart:

```python
df = pd.DataFrame({
    "Salary Range": ["$30k-$50k", "$50k-$70k", "$70k-$90k", "$90k-$110k", "$110k-$130k", "$130k+"],
    "Employees": [45, 120, 210, 150, 60, 15]
})

cc.plot_barv_chart(
    data=df,
    aspect_ratio="2:1",
    title="Company Salary Distribution",
    subtitle="Number of employees per salary bracket",
    bar_padding=0,
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/barv_histogram.png' | relative_url }}" alt="Barv" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Barv.</em>
</div>

### Square Tile

Compact square aspect ratio for dashboard panels:

```python
df = pd.DataFrame({"Quarter": ["Q1", "Q2", "Q3", "Q4"], "Revenue": [12.5, 14.2, 11.8, 16.5]})

cc.plot_barv_chart(
    data=df,
    title="Quarterly Revenue",
    aspect_ratio="square",
    bar_padding=0.4
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/barv_square.png' | relative_url }}" alt="Barv" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Barv.</em>
</div>
