---
layout: chart
title: Bubble Scatter Chart
description: 3-variable scatter plot with dot size encoding the third dimension.
permalink: /docs/charts/bubble-scatter/
---

# `plot_bubble_scatter_chart()`

Plots a 3-variable bubble scatter plot where dot size encodes a third numeric dimension. Best for market sizing, portfolio analysis, and multi-dimensional comparisons.

## Quick Example

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({
    "State": ["CA", "TX", "FL", "NY", "IL", "PA", "OH", "GA", "NC", "MI"],
    "Cost of Living Index": [138, 92, 101, 134, 94, 98, 91, 89, 96, 90],
    "Median Income": [84, 67, 61, 75, 72, 67, 61, 65, 60, 63],
    "Population (M)": [39.0, 30.0, 22.2, 19.5, 12.5, 12.9, 11.7, 10.9, 10.6, 10.0]
})

cc.plot_bubble_scatter_chart(
    data=df,
    title="Economic Reality by State",
    subtitle="Cost of living vs Median Income. Bubble size = Population.",
    x_label="Cost of Living Index",
    y_label="Median Income",
    y_suffix="k", 
    show_labels=True,
    alpha=0.6 
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/bubble_scatter_basic.png' | relative_url }}" alt="Bubble Scatter" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Bubble Scatter.</em>
</div>

## Data Requirements

- **3 columns** — [X, Y, Size]
- **4 columns** — [Label, X, Y, Size]

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
    <tr><td><code>data</code></td><td><code>pd.DataFrame</code></td><td>Built-in</td><td><span class="badge common">Common</span></td><td>3 or 4-column DataFrame.</td></tr>
    <tr><td><code>output_path</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>File path to save.</td></tr>
    <tr><td><code>width</code></td><td><code>int | None</code></td><td><code>700</code></td><td><span class="badge common">Common</span></td><td>Image width in pixels.</td></tr>
    <tr><td><code>height</code></td><td><code>int | None</code></td><td><code>500</code></td><td><span class="badge common">Common</span></td><td>Image height in pixels.</td></tr>
    <tr><td><code>aspect_ratio</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td><code>"square"</code>, <code>"landscape"</code>, etc.</td></tr>
    <tr><td><code>title</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Bold header text.</td></tr>
    <tr><td><code>subtitle</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Secondary text.</td></tr>
    <tr><td><code>bg_color</code></td><td><code>str | None</code></td><td><code>"#f4f3f0"</code></td><td><span class="badge common">Common</span></td><td>Background hex color.</td></tr>
    <tr><td><code>scale_text</code></td><td><code>bool</code></td><td><code>True</code></td><td><span class="badge common">Common</span></td><td>Scale fonts proportionally.</td></tr>
    <tr><td><code>min_bubble_size</code></td><td><code>float</code></td><td><code>60</code></td><td><span class="badge unique">Unique</span></td><td>Minimum bubble marker area in points².</td></tr>
    <tr><td><code>max_bubble_size</code></td><td><code>float</code></td><td><code>600</code></td><td><span class="badge unique">Unique</span></td><td>Maximum bubble marker area in points².</td></tr>
    <tr><td><code>start_color</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge unique">Unique</span></td><td>Gradient start color for bubbles.</td></tr>
    <tr><td><code>end_color</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge unique">Unique</span></td><td>Gradient end color for bubbles.</td></tr>
    <tr><td><code>color</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge unique">Unique</span></td><td>Single color for all bubbles.</td></tr>
    <tr><td><code>alpha</code></td><td><code>float</code></td><td><code>0.7</code></td><td><span class="badge unique">Unique</span></td><td>Transparency (0.0–1.0).</td></tr>
    <tr><td><code>show_values</code></td><td><code>bool</code></td><td><code>False</code></td><td><span class="badge unique">Unique</span></td><td>Annotate bubbles with their size values.</td></tr>
    <tr><td><code>show_labels</code></td><td><code>bool</code></td><td><code>False</code></td><td><span class="badge unique">Unique</span></td><td>Annotate bubbles with label strings.</td></tr>
    <tr><td><code>x_label</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge unique">Unique</span></td><td>X-axis label.</td></tr>
    <tr><td><code>y_label</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge unique">Unique</span></td><td>Y-axis label.</td></tr>
  </tbody>
</table>


