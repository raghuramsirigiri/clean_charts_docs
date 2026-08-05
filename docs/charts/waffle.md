---
layout: chart
title: Waffle Chart
description: 10×10 dot grid for precise "X out of 100" proportions.
permalink: /docs/charts/waffle/
---

# `plot_waffle_chart()`

Plots a multi-category waffle chart (10×10 dot grids) in the Economist style. Best for displaying precise grid proportions — "X out of 100" — in a visually striking format.

## Quick Example

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({
    "Heading": ["Growth Focus", "Resource Allocation", "Customer Centricity"],
    "Description": [
        "Organizations focusing 30% or more of their time on long-term growth initiatives",
        "Companies that actively increase resourcing during periods of market volatility",
        "Firms that consistently incorporate direct customer input into business decisions"
    ],
    "Value": [29, 30, 15]
})

cc.plot_waffle_chart(
    data=df,
    height=500,
    title="Key Strategic Priorities",
    subtitle="Percentage of surveyed organizations reporting on key focus areas",
    value_suffix="%"
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/waffle_basic.png' | relative_url }}" alt="Waffle" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Waffle.</em>
</div>


## Data Requirements

- **2 columns** — [Category, Percentage]
- **3 columns** — [Label (optional grouping), Category, Percentage]

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
    <tr><td><code>output_path</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>File path to save.</td></tr>
    <tr><td><code>width</code></td><td><code>int | None</code></td><td>Auto</td><td><span class="badge common">Common</span></td><td>Image width in pixels.</td></tr>
    <tr><td><code>height</code></td><td><code>int | None</code></td><td>Auto</td><td><span class="badge common">Common</span></td><td>Image height in pixels.</td></tr>
    <tr><td><code>aspect_ratio</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td><code>"square"</code>, <code>"landscape"</code>, etc.</td></tr>
    <tr><td><code>title</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Bold header text.</td></tr>
    <tr><td><code>subtitle</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Secondary text.</td></tr>
    <tr><td><code>bg_color</code></td><td><code>str | None</code></td><td><code>"#f4f3f0"</code></td><td><span class="badge common">Common</span></td><td>Background hex color.</td></tr>
    <tr><td><code>scale_text</code></td><td><code>bool</code></td><td><code>True</code></td><td><span class="badge common">Common</span></td><td>Scale fonts proportionally.</td></tr>
    <tr><td><code>color</code></td><td><code>str</code></td><td><code>"#000000"</code></td><td><span class="badge unique">Unique</span></td><td>Hex color for filled dots.</td></tr>
    <tr><td><code>inactive_color</code></td><td><code>str</code></td><td>Light gray</td><td><span class="badge unique">Unique</span></td><td>Hex color for unfilled dots.</td></tr>
  </tbody>
</table>

## Common Scenarios

### Budget Allocation

```python
df = pd.DataFrame({
    "Department": ["Manufacturing", "Engineering", "Operations", "Sales"],
    "Training Requirement": [
        "Heavy machinery and floor safety protocols",
        "Laboratory and electrical hazard compliance",
        "Logistics, warehouse, and lifting safety",
        "Standard office compliance and cybersecurity"
    ],
    "Completion (%)": [82, 94, 76, 98]
})

cc.plot_waffle_chart(
    data=df,
    title="Departmental Safety & Compliance Training",
    subtitle="Share of employees who have completed required annual certifications",
    value_suffix="%",
    color="#0066cc",          # Custom filled dot color (optional)
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/waffle_department.png' | relative_url }}" alt="Waffle" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Waffle.</em>
</div>
