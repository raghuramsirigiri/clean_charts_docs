---
layout: chart
title: Basic Scatter Chart
description: 2D scatter plot for visualizing relationships between two continuous variables.
permalink: /docs/charts/scatter/
---

# `plot_scatter_chart()`

Plots a 2D scatter plot in the Economist style. Best for visualizing relationships, correlations, and distributions between two continuous variables.

## Quick Example

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({
    "Company": ["AAPL", "MSFT", "GOOG", "AMZN", "META", "TSLA", "NVDA", "JPM"],
    "Revenue Growth (%)": [8, 12, 15, 11, 22, 19, 45, 6],
    "Profit Margin (%)": [26, 37, 25, 6, 28, 12, 55, 33]
})

cc.plot_scatter_chart(
    data=df,
    title="Tech Giants Performance",
    subtitle="Revenue Growth vs Profit Margin",
    x_label="Revenue Growth",
    y_label="Profit Margin",
    x_suffix="%",
    y_suffix="%",
    show_labels=True
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/scatter_basic.png' | relative_url }}" alt="Scatter" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Scatter.</em>
</div>

## Data Requirements

- **2 columns** — [X values, Y values]
- **3 columns** — [Labels, X values, Y values] (labels used when `show_labels=True`)

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
    <tr><td><code>data</code></td><td><code>pd.DataFrame</code></td><td>Built-in</td><td><span class="badge common">Common</span></td><td>2 or 3-column DataFrame.</td></tr>
    <tr><td><code>output_path</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>File path to save the chart.</td></tr>
    <tr><td><code>width</code></td><td><code>int | None</code></td><td><code>700</code></td><td><span class="badge common">Common</span></td><td>Image width in pixels.</td></tr>
    <tr><td><code>height</code></td><td><code>int | None</code></td><td><code>500</code></td><td><span class="badge common">Common</span></td><td>Image height in pixels.</td></tr>
    <tr><td><code>aspect_ratio</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td><code>"square"</code>, <code>"landscape"</code>, etc.</td></tr>
    <tr><td><code>title</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Bold header text.</td></tr>
    <tr><td><code>subtitle</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Secondary text below title.</td></tr>
    <tr><td><code>bg_color</code></td><td><code>str | None</code></td><td><code>"#f4f3f0"</code></td><td><span class="badge common">Common</span></td><td>Background hex color.</td></tr>
    <tr><td><code>scale_text</code></td><td><code>bool</code></td><td><code>True</code></td><td><span class="badge common">Common</span></td><td>Scale fonts proportionally.</td></tr>
    <tr><td><code>color</code></td><td><code>str | None</code></td><td>Auto</td><td><span class="badge unique">Unique</span></td><td>Hex color for scatter dots.</td></tr>
    <tr><td><code>dot_size</code></td><td><code>float</code></td><td><code>80</code></td><td><span class="badge unique">Unique</span></td><td>Marker size (area in points²).</td></tr>
    <tr><td><code>alpha</code></td><td><code>float</code></td><td><code>0.75</code></td><td><span class="badge unique">Unique</span></td><td>Transparency of scatter points (0.0–1.0).</td></tr>
    <tr><td><code>x_label</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge unique">Unique</span></td><td>X-axis label text.</td></tr>
    <tr><td><code>y_label</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge unique">Unique</span></td><td>Y-axis label text.</td></tr>
    <tr><td><code>x_suffix</code></td><td><code>str</code></td><td><code>""</code></td><td><span class="badge unique">Unique</span></td><td>Suffix for X-axis annotations.</td></tr>
    <tr><td><code>y_suffix</code></td><td><code>str</code></td><td><code>""</code></td><td><span class="badge unique">Unique</span></td><td>Suffix for Y-axis annotations.</td></tr>
    <tr><td><code>show_labels</code></td><td><code>bool</code></td><td><code>False</code></td><td><span class="badge unique">Unique</span></td><td>Annotate points with label strings.</td></tr>
    <tr><td><code>show_trendline</code></td><td><code>bool</code></td><td><code>False</code></td><td><span class="badge unique">Unique</span></td><td>Plot a linear regression trend line.</td></tr>
    <tr><td><code>trendline_color</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge unique">Unique</span></td><td>Hex color for the trend line.</td></tr>
  </tbody>
</table>

## Common Scenarios

### Labeled Scatter with Trend

```python
df = pd.DataFrame({
    "Company": ["AAPL", "MSFT", "GOOG", "AMZN", "META", "TSLA", "NVDA", "JPM"],
    "Revenue Growth (%)": [8, 12, 15, 11, 22, 19, 45, 6],
    "Profit Margin (%)": [26, 37, 25, 6, 28, 12, 55, 33]
})

cc.plot_scatter_chart(
    data=df,
    title="Growth vs Profitability",
    show_labels=True,
    show_trendline=True,
    trendline_color="#635bff"
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/scatter_trend.png' | relative_url }}" alt="Scatter" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Scatter.</em>
</div>

