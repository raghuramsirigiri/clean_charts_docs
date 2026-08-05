---
layout: chart
title: Time Series Line Chart
description: Multi-series line charts with annotations, splines, and trend overlays.
permalink: /docs/charts/time-series/
---

# `plot_time_series()`

Plots a time-series line chart with smooth spline interpolation and inline series labels. Optimized for visualizing continuous data over time — financial metrics, user growth, performance trends.

## Quick Example

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({
    "Date": pd.date_range(start="2024-01-01", periods=12, freq="MS"),
    "Revenue": [120, 135, 142, 125, 155, 162, 175, 188, 185, 208, 215, 230],
    "Costs": [90, 95, 98, 105, 102, 108, 112, 118, 115, 125, 130, 135]
})

cc.plot_time_series(
    data=df,
    title="Quarterly Financials",
    subtitle="Revenue vs Costs in USD Thousands",
    label_frequency="quarter", 
    value_suffix="k",
    vlines=[
        {
            "date": "2024-07-01",
            "label": "Product Launch", 
            "color": "#000000"
        }
    ]
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/time_series_basic.png' | relative_url }}" alt="Time Series" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Time Series.</em>
</div>


## Data Requirements

- **Time Column** — must contain dates or timestamps. Auto-detected if named `"date"`, `"time"`, or `"timestamp"`, or if its dtype is datetime.
- **Value Columns** — all remaining numeric columns are plotted as independent series.
- **Frequency** — ideally regular intervals, though the spline interpolation handles irregular spacing.

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
      <td>DataFrame with a date column and one or more numeric series.</td>
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
      <td><code>int</code></td>
      <td><code>600</code></td>
      <td><span class="badge common">Common</span></td>
      <td>Image width in pixels.</td>
    </tr>
    <tr>
      <td><code>height</code></td>
      <td><code>int</code></td>
      <td><code>600</code></td>
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
      <td><code>False</code></td>
      <td><span class="badge common">Common</span></td>
      <td>Scale fonts proportionally.</td>
    </tr>
    <tr>
      <td><code>value_suffix</code></td>
      <td><code>str</code></td>
      <td><code>""</code></td>
      <td><span class="badge common">Common</span></td>
      <td>String appended to value labels.</td>
    </tr>
    <tr>
      <td><code>start_color</code></td>
      <td><code>str</code></td>
      <td><code>"#000000"</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Hex color for the first line series.</td>
    </tr>
    <tr>
      <td><code>end_color</code></td>
      <td><code>str</code></td>
      <td><code>"#2323FF"</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Hex color for the last line series.</td>
    </tr>
    <tr>
      <td><code>label_frequency</code></td>
      <td><code>str</code></td>
      <td><code>"year"</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>X-axis tick frequency: <code>"year"</code>, <code>"quarter"</code>, <code>"month"</code>, <code>"week"</code>, <code>"day"</code>.</td>
    </tr>
    <tr>
      <td><code>markers</code></td>
      <td><code>bool | str</code></td>
      <td><code>None</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Data-point markers on lines (e.g., <code>True</code>, <code>"o"</code>, <code>"s"</code>).</td>
    </tr>
    <tr>
      <td><code>line_labels</code></td>
      <td><code>str</code></td>
      <td><code>"name"</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Inline text near endpoints: <code>"name"</code>, <code>"value"</code>, <code>"both"</code>, <code>"none"</code>.</td>
    </tr>
    <tr>
      <td><code>smooth</code></td>
      <td><code>bool</code></td>
      <td><code>True</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Draw smooth PCHIP spline curves instead of straight segments.</td>
    </tr>
    <tr>
      <td><code>vlines</code></td>
      <td><code>list | dict</code></td>
      <td><code>None</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Vertical reference lines with optional labels. Accepts single dates, dicts, or lists of dicts.</td>
    </tr>
    <tr>
      <td><code>highlight_ranges</code></td>
      <td><code>list | dict</code></td>
      <td><code>None</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Shaded background regions between two dates.</td>
    </tr>
    <tr>
      <td><code>callouts</code></td>
      <td><code>list | dict</code></td>
      <td><code>None</code></td>
      <td><span class="badge unique">Unique</span></td>
      <td>Text callout boxes pointing to specific (date, value) coordinates. Keys: <code>date</code>, <code>text</code>, <code>series</code>, <code>color</code>.</td>
    </tr>
  </tbody>
</table>

## Common Scenarios

### Milestone Markers

Add vertical reference lines for key events:

```python
df = pd.DataFrame({
    "Date": pd.date_range(start="2024-01-01", periods=12, freq="MS"),
    "Revenue": [120, 135, 142, 125, 155, 162, 175, 188, 185, 208, 215, 230],
    "Costs": [90, 95, 98, 105, 102, 108, 112, 118, 115, 125, 130, 135]
})

cc.plot_time_series(
    data=df,
    title="Quarterly Financials",
    subtitle="Revenue vs Costs in USD Thousands",
    label_frequency="quarter", 
    value_suffix="k",
    vlines=[
        {
            "date": "2024-07-01",
            "label": "Product Launch", 
            "color": "#000000"
        }
    ]
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/time_series_markers.png' | relative_url }}" alt="Time Series" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Time Series.</em>
</div>

### Recession Bands

Shade time ranges to highlight periods of interest:

```python
df = pd.DataFrame({
    "Date": pd.date_range(start="2022-01-01", periods=24, freq="MS"),
    "Active Users": [
        1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 
        1.5, 1.4, 1.3, 1.2, 1.1, 1.2,
        1.3, 1.5, 1.8, 2.1, 2.4, 2.7, 
        2.9, 3.1, 3.2, 3.4, 3.5, 3.7
    ]
})

cc.plot_time_series(
    data=df,
    title="Platform Active Users",
    subtitle="Monthly active users in millions",
    label_frequency="quarter",
    value_suffix="m",
    highlight_ranges=[
        {
            "start": "2022-07-01", 
            "end": "2022-12-01",
            "color": "#e3120b",
            "alpha": 0.1,
            "label": "Service Outages",
            "paragraph": "A series of major infrastructure\nissues caused significant\nuser churn during this period."
        }
    ]
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/ts_macro.png' | relative_url }}" alt="Time Series" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Time Series.</em>
</div>

### Data Point Callouts

Annotate specific data points:

```python
df = pd.DataFrame({
    "Date": pd.date_range(start="2024-01-01", periods=6, freq="MS"),
    "Traffic": [210, 215, 225, 450, 280, 295]
})

cc.plot_time_series(
    data=df,
    title="Website Traffic",
    subtitle="Daily unique visitors (thousands)",
    label_frequency="month",
    value_suffix="k",
    callouts=[
        {
            "date": "2024-04-01",
            "series": "Traffic", 
            "text": "Featured on HackerNews\ndriving a massive spike",
            "text_y": 50, 
            "ha": "center",
            "color": "#0000CD"
        }
    ]
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/time_series_callouts.png' | relative_url }}" alt="Time Series" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Time Series.</em>
</div>
