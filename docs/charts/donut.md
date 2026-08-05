---
layout: chart
title: Donut Chart
description: Ring chart with center label for part-to-whole compositions.
permalink: /docs/charts/donut/
---

# `plot_donut_chart()`

Renders a donut (ring) chart with a hollow center for displaying summary text. Designed for part-of-whole compositions with up to ~8 segments. Each segment is colored with a continuous gradient.

## Quick Example

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({
    "Source": ["Solar", "Wind", "Nuclear", "Natural Gas", "Coal"],
    "TWh": [1200, 1500, 2500, 3000, 1800]
})

cc.plot_donut_chart(
    data=df,
    title="Global Energy Mix",
    subtitle="Projected generation in 2030 (TWh)",
    center_label="10,000\nTWh"
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/donut_basic.png' | relative_url }}" alt="Donut" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Donut.</em>
</div>


## Data Requirements

- **Column 0** — Segment labels (`str`)
- **Column 1** — Numeric values (auto-normalized to percentages)

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
    <tr><td><code>data</code></td><td><code>pd.DataFrame</code></td><td>Built-in</td><td><span class="badge common">Common</span></td><td>2-column DataFrame: [Labels, Values].</td></tr>
    <tr><td><code>output_path</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>File path to save.</td></tr>
    <tr><td><code>width</code></td><td><code>int | None</code></td><td><code>600</code></td><td><span class="badge common">Common</span></td><td>Image width in pixels.</td></tr>
    <tr><td><code>height</code></td><td><code>int | None</code></td><td>Auto</td><td><span class="badge common">Common</span></td><td>Image height in pixels.</td></tr>
    <tr><td><code>aspect_ratio</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td><code>"square"</code>, <code>"landscape"</code>, etc.</td></tr>
    <tr><td><code>title</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Bold header text.</td></tr>
    <tr><td><code>subtitle</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Secondary text.</td></tr>
    <tr><td><code>bg_color</code></td><td><code>str | None</code></td><td><code>"#f4f3f0"</code></td><td><span class="badge common">Common</span></td><td>Background hex color.</td></tr>
    <tr><td><code>scale_text</code></td><td><code>bool</code></td><td><code>True</code></td><td><span class="badge common">Common</span></td><td>Scale fonts proportionally.</td></tr>
    <tr><td><code>value_suffix</code></td><td><code>str</code></td><td><code>""</code></td><td><span class="badge common">Common</span></td><td>String appended to legend values.</td></tr>
    <tr><td><code>show_percentages</code></td><td><code>bool</code></td><td><code>False</code></td><td><span class="badge common">Common</span></td><td>Append percentage to legend labels.</td></tr>
    <tr><td><code>start_color</code></td><td><code>str</code></td><td><code>"#000000"</code></td><td><span class="badge unique">Unique</span></td><td>Gradient start color for the first segment.</td></tr>
    <tr><td><code>end_color</code></td><td><code>str</code></td><td><code>"#2323FF"</code></td><td><span class="badge unique">Unique</span></td><td>Gradient end color for the last segment.</td></tr>
    <tr><td><code>center_label</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge unique">Unique</span></td><td>Bold text inside the ring center. Use <code>\n</code> for multiline (e.g., <code>"$42M\nTotal"</code>).</td></tr>
    <tr><td><code>hole_radius</code></td><td><code>float</code></td><td>Auto</td><td><span class="badge unique">Unique</span></td><td>Inner hole as fraction of outer radius (0–1).</td></tr>
    <tr><td><code>start_angle</code></td><td><code>float</code></td><td><code>90</code></td><td><span class="badge unique">Unique</span></td><td>Angle (degrees) to start drawing the first wedge.</td></tr>
    <tr><td><code>donut_radius</code></td><td><code>float</code></td><td>Auto</td><td><span class="badge unique">Unique</span></td><td>Outer radius as fraction of available chart height.</td></tr>
  </tbody>
</table>

## Common Scenarios

### Hero Metric Donut

```python
df = pd.DataFrame({
    "Source": ["Solar", "Wind", "Nuclear", "Natural Gas", "Coal"],
    "TWh": [1200, 1500, 2500, 3000, 1800]
})

cc.plot_donut_chart(
    data=df,
    title="Revenue Breakdown",
    center_label="$42M\nTotal Revenue",
    show_percentages=True
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/donut_percentages.png' | relative_url }}" alt="Donut" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Donut.</em>
</div>

### Custom Gradient

```python
df = pd.DataFrame({
    "Source": ["Solar", "Wind", "Nuclear", "Natural Gas", "Coal"],
    "TWh": [1200, 1500, 2500, 3000, 1800]
})

cc.plot_donut_chart(
    data=df,
    title="Revenue Breakdown",
    center_label="$42M\nTotal Revenue",
    show_percentages=True,
    start_color="#0A1F13",
    end_color="#FFED29"
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/donut_energy.png' | relative_url }}" alt="Donut" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Donut.</em>
</div>
