---
layout: chart
title: Geofacet Map
description: Geographic small-multiples grid approximating a physical map layout.
permalink: /docs/charts/geofacet/
---

# `plot_geofacet()`

Visualize geographic data using a grid that roughly approximates the physical map. Each state or region is rendered as a cell with text, donut, or bar indicators.

## Quick Example

```python
import pandas as pd
import clean_charts as cc

states = [
    "AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI",
    "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN",
    "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH",
    "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA",
    "WI", "WV", "WY"
]
values = [
    42.0, 15.5, 22.0, 68.2, 98.5, 85.0, 88.4, 92.1, 74.0, 55.5, 45.0, 95.2,
    32.0, 28.5, 70.1, 35.4, 40.0, 24.5, 18.0, 94.6, 82.2, 60.0, 65.5, 58.8,
    38.0, 12.5, 20.0, 50.4, 15.0, 25.5, 72.0, 86.6, 44.4, 62.2, 96.0, 48.8,
    26.5, 90.0, 66.0, 80.5, 34.0, 22.5, 42.0, 78.5, 54.0, 76.2, 84.4, 97.5,
    52.0, 10.5, 14.0
]
df = pd.DataFrame({
    "State": states,
    "EV Adoption": values
})

cc.plot_geofacet(
    data=df,
    layout="us",
    display_type="bar",
    title="Electric Vehicle Adoption",
    subtitle="Percentage of total vehicle sales in %",
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/geofacet_bar.png' | relative_url }}" alt="Geofacet" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Geofacet.</em>
</div>


## Data Requirements

- DataFrame with a column of state/region abbreviations and a column of numeric values.

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
    <tr><td><code>data</code></td><td><code>pd.DataFrame</code></td><td>Built-in</td><td><span class="badge common">Common</span></td><td>DataFrame with state abbreviations and values.</td></tr>
    <tr><td><code>output_path</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>File path to save.</td></tr>
    <tr><td><code>width</code></td><td><code>int | None</code></td><td>Auto</td><td><span class="badge common">Common</span></td><td>Image width in pixels.</td></tr>
    <tr><td><code>height</code></td><td><code>int | None</code></td><td>Auto</td><td><span class="badge common">Common</span></td><td>Image height in pixels.</td></tr>
    <tr><td><code>aspect_ratio</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td><code>"square"</code>, <code>"landscape"</code>, etc.</td></tr>
    <tr><td><code>title</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Bold header text.</td></tr>
    <tr><td><code>subtitle</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Secondary text.</td></tr>
    <tr><td><code>bg_color</code></td><td><code>str | None</code></td><td><code>"#f4f3f0"</code></td><td><span class="badge common">Common</span></td><td>Background hex color.</td></tr>
    <tr><td><code>scale_text</code></td><td><code>bool</code></td><td><code>True</code></td><td><span class="badge common">Common</span></td><td>Scale fonts proportionally.</td></tr>
    <tr><td><code>state_col</code></td><td><code>str</code></td><td>Auto</td><td><span class="badge unique">Unique</span></td><td>Column name containing location abbreviations.</td></tr>
    <tr><td><code>value_col</code></td><td><code>str</code></td><td>Auto</td><td><span class="badge unique">Unique</span></td><td>Column name containing numeric values.</td></tr>
    <tr><td><code>layout</code></td><td><code>str</code></td><td><code>"us"</code></td><td><span class="badge unique">Unique</span></td><td>Grid layout: <code>"us"</code>, <code>"uk"</code>.</td></tr>
    <tr><td><code>display_type</code></td><td><code>str</code></td><td><code>"text"</code></td><td><span class="badge unique">Unique</span></td><td>Cell render style: <code>"text"</code>, <code>"donut"</code>, <code>"bar"</code>.</td></tr>
    <tr><td><code>max_value</code></td><td><code>float</code></td><td>Auto</td><td><span class="badge unique">Unique</span></td><td>Maximum value for scaling progress rings and bars.</td></tr>
    <tr><td><code>missing_color</code></td><td><code>str</code></td><td>Light gray</td><td><span class="badge unique">Unique</span></td><td>Color for states with no data.</td></tr>
    <tr><td><code>start_color</code></td><td><code>str</code></td><td><code>"#000000"</code></td><td><span class="badge unique">Unique</span></td><td>Heatmap gradient start color.</td></tr>
    <tr><td><code>end_color</code></td><td><code>str</code></td><td><code>"#2323FF"</code></td><td><span class="badge unique">Unique</span></td><td>Heatmap gradient end color.</td></tr>
  </tbody>
</table>

## Common Scenarios

### Donut-Style State Cells

```python
df = pd.DataFrame({
    "State": ["CA", "TX", "NY", "FL", "IL", "PA", "OH", "GA", "NC", "MI"],
    "Goal Completion": [85, 45, 92, 38, 67, 55, 42, 60, 58, 48]
})

cc.plot_geofacet(
    data=df,
    layout="us",
    display_type="donut",
    max_value=100.0,
    title="Q3 Sales Goal Progress",
    subtitle="Percent to quota for top 10 regional markets",
    value_suffix="%",
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/geofacet_donut.png' | relative_url }}" alt="Geofacet" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Geofacet.</em>
</div>

### Heatmap Bar View

```python
states = [
    "AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI",
    "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN",
    "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH",
    "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA",
    "WI", "WV", "WY"
]
values = [
    42.0, 15.5, 22.0, 68.2, 98.5, 85.0, 88.4, 92.1, 74.0, 55.5, 45.0, 95.2,
    32.0, 28.5, 70.1, 35.4, 40.0, 24.5, 18.0, 94.6, 82.2, 60.0, 65.5, 58.8,
    38.0, 12.5, 20.0, 50.4, 15.0, 25.5, 72.0, 86.6, 44.4, 62.2, 96.0, 48.8,
    26.5, 90.0, 66.0, 80.5, 34.0, 22.5, 42.0, 78.5, 54.0, 76.2, 84.4, 97.5,
    52.0, 10.5, 14.0
]
df = pd.DataFrame({
    "State": states,
    "EV Adoption": values
})

cc.plot_geofacet(
    data=df,
    layout="us",
    display_type="text",
    title="Electric Vehicle Adoption",
    subtitle="Percentage of total vehicle sales in %",
    end_color="#2B0057",
    start_color="#d3a9fc"
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/geofacet_text.png' | relative_url }}" alt="Geofacet" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Geofacet.</em>
</div>
