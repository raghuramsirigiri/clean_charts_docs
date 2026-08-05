---
layout: chart
title: Grouped Scatter Chart
description: Quadrant matrix or categorically grouped scatter plot.
permalink: /docs/charts/grouped-scatter/
---

# `plot_grouped_scatter_chart()`

Plots a grouped or quadrant-mapped scatter plot. Use `group_by="category"` for color-coded groups, or `group_by="quadrant"` for a 2×2 strategic matrix.

## Quick Example

```python
import pandas as pd
import numpy as np
import clean_charts as cc

np.random.seed(42)
n = 20

df = pd.concat([
    pd.DataFrame({
      "User": [f"P{i}" for i in range(n)], 
      "Time (mins)": np.random.normal(120, 15, n), 
      "Actions": np.random.normal(85, 10, n), 
      "Segment": "Power Users"}),
    pd.DataFrame({
      "User": [f"C{i}" for i in range(n)], 
      "Time (mins)": np.random.normal(30, 10, n), 
      "Actions": np.random.normal(15, 5, n), 
      "Segment": "Casual Browsers"}),
    pd.DataFrame({
      "User": [f"D{i}" for i in range(n)], 
      "Time (mins)": np.random.normal(110, 20, n), 
      "Actions": np.random.normal(20, 8, n), 
      "Segment": "Passive Scrollers"})
])

cc.plot_grouped_scatter_chart(
    data=df,
    title="User Behavior Segments",
    subtitle="Identifying distinct cohorts by in-app activity",
    show_labels=False,
    alpha=1,
    axes_origin=(60,60)
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/grouped_scatter_basic.png' | relative_url }}" alt="Grouped Scatter" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Grouped Scatter.</em>
</div>

## Data Requirements

- **Categorical mode** — 3–4 columns: [Label (opt), X, Y, Category]
- **Quadrant mode** — 2–3 columns: [Label (opt), X, Y]

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
    <tr><td><code>data</code></td><td><code>pd.DataFrame</code></td><td>Built-in</td><td><span class="badge common">Common</span></td><td>DataFrame with X, Y, and optional label/category columns.</td></tr>
    <tr><td><code>output_path</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>File path to save the chart.</td></tr>
    <tr><td><code>width</code></td><td><code>int | None</code></td><td><code>700</code></td><td><span class="badge common">Common</span></td><td>Image width in pixels.</td></tr>
    <tr><td><code>height</code></td><td><code>int | None</code></td><td><code>500</code></td><td><span class="badge common">Common</span></td><td>Image height in pixels.</td></tr>
    <tr><td><code>aspect_ratio</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td><code>"square"</code>, <code>"landscape"</code>, etc.</td></tr>
    <tr><td><code>title</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Bold header text.</td></tr>
    <tr><td><code>subtitle</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Secondary text below title.</td></tr>
    <tr><td><code>bg_color</code></td><td><code>str | None</code></td><td><code>"#f4f3f0"</code></td><td><span class="badge common">Common</span></td><td>Background hex color.</td></tr>
    <tr><td><code>scale_text</code></td><td><code>bool</code></td><td><code>True</code></td><td><span class="badge common">Common</span></td><td>Scale fonts proportionally.</td></tr>
    <tr><td><code>group_by</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge unique">Unique</span></td><td><code>"category"</code> or <code>"quadrant"</code>.</td></tr>
    <tr><td><code>x_threshold</code></td><td><code>float | None</code></td><td>Mean</td><td><span class="badge unique">Unique</span></td><td>Threshold line for quadrant X division.</td></tr>
    <tr><td><code>y_threshold</code></td><td><code>float | None</code></td><td>Mean</td><td><span class="badge unique">Unique</span></td><td>Threshold line for quadrant Y division.</td></tr>
    <tr><td><code>quadrant_labels</code></td><td><code>list[str]</code></td><td><code>None</code></td><td><span class="badge unique">Unique</span></td><td>Labels for [top-right, top-left, bottom-left, bottom-right].</td></tr>
    <tr><td><code>show_threshold_lines</code></td><td><code>bool</code></td><td><code>True</code></td><td><span class="badge unique">Unique</span></td><td>Plot the x and y threshold lines.</td></tr>
    <tr><td><code>colors</code></td><td><code>list[str]</code></td><td>Auto</td><td><span class="badge unique">Unique</span></td><td>Explicit hex colors for categories/quadrants.</td></tr>
    <tr><td><code>start_color</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge unique">Unique</span></td><td>Gradient start color for groups.</td></tr>
    <tr><td><code>end_color</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge unique">Unique</span></td><td>Gradient end color for groups.</td></tr>
    <tr><td><code>dot_size</code></td><td><code>float</code></td><td><code>80</code></td><td><span class="badge unique">Unique</span></td><td>Marker size (area in points²).</td></tr>
    <tr><td><code>alpha</code></td><td><code>float</code></td><td><code>0.75</code></td><td><span class="badge unique">Unique</span></td><td>Transparency of points.</td></tr>
    <tr><td><code>x_label</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge unique">Unique</span></td><td>X-axis label.</td></tr>
    <tr><td><code>y_label</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge unique">Unique</span></td><td>Y-axis label.</td></tr>
    <tr><td><code>show_labels</code></td><td><code>bool</code></td><td><code>False</code></td><td><span class="badge unique">Unique</span></td><td>Annotate points with labels.</td></tr>
  </tbody>
</table>

