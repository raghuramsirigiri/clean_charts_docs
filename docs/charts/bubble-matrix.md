---
layout: chart
title: Bubble Matrix Chart
description: Size and color encoded grid for cross-tabulations and heatmaps.
permalink: /docs/charts/bubble-matrix/
---

# `plot_bubble_matrix_chart()`

Plots a bubble matrix chart. Best for visualizing 3 dimensions of data (Row, Column, Size) in a grid format — useful for skill assessments, risk matrices, and performance heatmaps.

## Quick Example

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({
    "Generation": ["Gen Z", "Millennials", "Gen X", "Boomers"],
    "TikTok":    [95, 60, 20,  5],
    "Instagram": [85, 90, 55, 15],
    "X / Twitter":[45, 65, 40, 10],
    "LinkedIn":  [15, 75, 80, 30],
    "Facebook":  [10, 65, 85, 90]
})

cc.plot_bubble_matrix_chart(
    data=df,
    title="Social Media Demographics",
    subtitle="Estimated daily active users (in millions) by generation",
    value_suffix="m", 
)

```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/bubble_matrix_basic.png' | relative_url }}" alt="Bubble Matrix" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Bubble Matrix.</em>
</div>


## Data Requirements

- **Column 0** — Row category labels (`str`)
- **Columns 1…N** — Numeric values. Column headers become the column labels.

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
    <tr><td><code>data</code></td><td><code>pd.DataFrame</code></td><td>Built-in</td><td><span class="badge common">Common</span></td><td>First column: row labels. Remaining columns: numeric values.</td></tr>
    <tr><td><code>output_path</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>File path to save.</td></tr>
    <tr><td><code>width</code></td><td><code>int | None</code></td><td>Auto</td><td><span class="badge common">Common</span></td><td>Image width in pixels.</td></tr>
    <tr><td><code>height</code></td><td><code>int | None</code></td><td>Auto</td><td><span class="badge common">Common</span></td><td>Image height in pixels.</td></tr>
    <tr><td><code>aspect_ratio</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td><code>"square"</code>, <code>"landscape"</code>, etc.</td></tr>
    <tr><td><code>title</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Bold header text.</td></tr>
    <tr><td><code>subtitle</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Secondary text.</td></tr>
    <tr><td><code>bg_color</code></td><td><code>str | None</code></td><td><code>"#f4f3f0"</code></td><td><span class="badge common">Common</span></td><td>Background hex color.</td></tr>
    <tr><td><code>scale_text</code></td><td><code>bool</code></td><td><code>True</code></td><td><span class="badge common">Common</span></td><td>Scale fonts proportionally.</td></tr>
    <tr><td><code>start_color</code></td><td><code>str</code></td><td><code>"#000000"</code></td><td><span class="badge unique">Unique</span></td><td>Gradient color for lowest-value bubbles.</td></tr>
    <tr><td><code>end_color</code></td><td><code>str</code></td><td><code>"#2323FF"</code></td><td><span class="badge unique">Unique</span></td><td>Gradient color for highest-value bubbles.</td></tr>
    <tr><td><code>show_values</code></td><td><code>bool</code></td><td><code>False</code></td><td><span class="badge unique">Unique</span></td><td>Print numeric values inside each bubble.</td></tr>
  </tbody>
</table>

## Common Scenarios

### Risk Matrix

```python
df = pd.DataFrame({
    "Likelihood": ["Almost Certain", "Likely", "Possible", "Unlikely", "Rare"],
    "Negligible": [2, 5,  8, 12, 15],
    "Minor":      [1, 4, 10,  8,  5],
    "Moderate":   [0, 2,  6,  4,  2],
    "Major":      [0, 1,  2,  3,  1],
    "Severe":     [0, 0,  1,  1,  0]
})

cc.plot_bubble_matrix_chart(
    data=df,
    title="Enterprise Risk Assessment",
    subtitle="Volume of identified risks by Likelihood and Impact",
    show_values=True,
    end_color="#FFA896", 
    start_color="#9B1313"    
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/bubble_matrix_heatmap.png' | relative_url }}" alt="Bubble Matrix" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Bubble Matrix.</em>
</div>
