---
layout: chart
title: Dumbbell Chart
description: Connected dot chart showing before vs after deltas across categories.
permalink: /docs/charts/dumbbell/
---

# `plot_dumbbell_chart()`

Plots a horizontal dumbbell (range dot) chart. Best for comparing the same metric across two distinct time periods or groups — "before vs after", "target vs actual", "2022 vs 2023".

## Quick Example

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({
    "Country": ["US", "China", "Germany", "UK", "India", "France"],
    "2010": [14.99, 6.09, 3.42, 2.48, 1.68, 2.65],
    "2023": [25.46, 17.79, 4.46, 3.33, 3.73, 3.05]
})

cc.plot_dumbbell_chart(
    data=df,
    title="GDP Growth by Country",
    subtitle="2010 vs 2023 (USD Trillions)",
    value_suffix="T",
    show_values=True
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/dumbbell_basic.png' | relative_url }}" alt="Dumbbell" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Dumbbell.</em>
</div>


## Data Requirements

Exactly **3 columns**: [Category labels, Start values, End values].

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
    <tr><td><code>data</code></td><td><code>pd.DataFrame</code></td><td>Built-in</td><td><span class="badge common">Common</span></td><td>3-column DataFrame: [Category, Start, End].</td></tr>
    <tr><td><code>output_path</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>File path to save.</td></tr>
    <tr><td><code>width</code></td><td><code>int | None</code></td><td>Auto</td><td><span class="badge common">Common</span></td><td>Image width in pixels.</td></tr>
    <tr><td><code>height</code></td><td><code>int | None</code></td><td>Auto</td><td><span class="badge common">Common</span></td><td>Image height in pixels.</td></tr>
    <tr><td><code>aspect_ratio</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td><code>"square"</code>, <code>"landscape"</code>, etc.</td></tr>
    <tr><td><code>title</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Bold header text.</td></tr>
    <tr><td><code>subtitle</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Secondary text.</td></tr>
    <tr><td><code>bg_color</code></td><td><code>str | None</code></td><td><code>"#f4f3f0"</code></td><td><span class="badge common">Common</span></td><td>Background hex color.</td></tr>
    <tr><td><code>scale_text</code></td><td><code>bool</code></td><td><code>True</code></td><td><span class="badge common">Common</span></td><td>Scale fonts proportionally.</td></tr>
    <tr><td><code>value_suffix</code></td><td><code>str</code></td><td><code>""</code></td><td><span class="badge common">Common</span></td><td>String appended to value labels.</td></tr>
    <tr><td><code>start_color</code></td><td><code>str</code></td><td><code>"#000000"</code></td><td><span class="badge unique">Unique</span></td><td>Hex color for the first-series dots.</td></tr>
    <tr><td><code>end_color</code></td><td><code>str</code></td><td><code>"#2323FF"</code></td><td><span class="badge unique">Unique</span></td><td>Hex color for the second-series dots.</td></tr>
    <tr><td><code>connector_color</code></td><td><code>str</code></td><td>Auto</td><td><span class="badge unique">Unique</span></td><td>Hex color for the connecting line.</td></tr>
    <tr><td><code>dot_size</code></td><td><code>float</code></td><td>Auto</td><td><span class="badge unique">Unique</span></td><td>Marker size area in points².</td></tr>
    <tr><td><code>show_values</code></td><td><code>bool</code></td><td><code>False</code></td><td><span class="badge unique">Unique</span></td><td>Display numeric value labels next to each dot.</td></tr>
  </tbody>
</table>

## Common Scenarios

### Target vs Actual

```python
df = pd.DataFrame({
    "Product Line": ["Software Subscriptions", "Cloud Hosting", "Hardware Sales", "Consulting"],
    "Target": [150, 120, 85, 45],
    "Actual": [142, 135, 72, 48]
})

cc.plot_dumbbell_chart(
    data=df,
    title="Q4 Revenue Performance",
    subtitle="Target vs Actual revenue by product line (in Millions)",
    value_suffix="M",
    show_values=True,
    end_color="#FD8302",
    start_color="#0241FD",
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/dumbbell_dynamic.png' | relative_url }}" alt="Dumbbell" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Dumbbell.</em>
</div>

### Sentiment Shift

```python
df = pd.DataFrame({
    "Emotion": ["Joy", "Sadness", "Anger", "Fear", "Surprise"],
    "Previous": [12, 8, 5, 3, 6],
    "Current": [15, 6, 7, 2, 9]
})

cc.plot_dumbbell_chart(
    data=df,
    title="Brand Sentiment Shift",
    connector_color="#36404A"
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/dumbbell_no_labels.png' | relative_url }}" alt="Dumbbell" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Dumbbell.</em>
</div>
