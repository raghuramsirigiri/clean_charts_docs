---
layout: default
title: Donut Chart
parent: Part-to-Whole
has_children: true
nav_order: 4
---
# `plot_donut_chart()`

Renders a donut (ring) chart with a hollow center for displaying summary text. Designed for part-of-whole compositions with up to ~8 segments. Each segment is rendered with a continuous color gradient from `start_color` to `end_color`.

![Donut — Basic](../images/docs/donut_basic.png)

---

## API Reference

```python
clean_charts.plot_donut_chart(
    data=None,
    output_path=None,
    width=None,
    height=None,
    aspect_ratio=None,
    title=None,
    subtitle=None,
    bg_color=None,
    color=None,
    end_color=None,
    center_label=None,
    show_percentages=False,
    value_suffix="",
    scale_text=True,
)
```

---

## Parameters

| Parameter          | Type             | Default     | Description |
|--------------------|------------------|-------------|-------------|
| `data`             | `pd.DataFrame`   | Built-in    | DataFrame with two columns: Column 0 (str) = segment labels, Column 1 (numeric) = values. Values are automatically normalized to percentages for display. |
| `output_path`      | `str \| None`    | `None`      | File path for the saved image. |
| `width`            | `int \| None`    | `600`       | Image width in pixels. |
| `height`           | `int \| None`    | Auto        | Auto-calculated based on width and segment count. |
| `aspect_ratio`     | `str \| None`    | `None`      | `"square"`, `"landscape"`, `"vertical"`, `"1:1"`, `"2:1"`, `"1:2"`. |
| `title`            | `str \| None`    | `None`      | Bold title (max 2 lines). |
| `subtitle`         | `str \| None`    | `None`      | Lighter subtitle (max 3 lines). |
| `bg_color`         | `str \| None`    | `"#f4f3f0"` | Background color. |
| `start_color`      | `str \| None`    | `"#000000"` | Gradient start color for the first (largest) segment. |
| `end_color`        | `str \| None`    | `"#2323FF"` | Gradient end color for the last (smallest) segment. |
| `center_label`     | `str \| None`    | `None`      | Text rendered inside the center of the donut ring. Supports `\n` for multiline. E.g., `"100%\nTotal"`, `"$42M"`. |
| `show_percentages` | `bool`           | `False`     | Append `" (XX.X%)"` to each legend label. |
| `value_suffix`     | `str`            | `""`        | String appended to numeric values in the legend. |
| `scale_text`       | `bool`           | `True`      | Scale fonts proportionally. |

---

## Examples

### Basic Donut Chart

```python
import pandas as pd
import clean_charts as cc

df_donut = pd.DataFrame({
    'Source': ['Solar', 'Wind', 'Nuclear', 'Natural Gas', 'Coal'],
    'TWh': [1200, 1500, 2500, 3000, 1800]
})

cc.plot_donut_chart(
    data=df_donut,
    title="Global Energy Mix",
    subtitle="Projected generation in 2030 (TWh)",
    center_label="10,000\nTWh"
)
```

![Donut — Basic](../images/docs/donut_basic.png)

### With Percentage Labels

Displays percentage values in the legend.

```python
cc.plot_donut_chart(
    data=df_donut,
    title="Global Energy Mix",
    subtitle="Percentage distribution of projected generation in 2030",
    center_label="100%",
    show_percentages=True
)
```

![Donut — Percentages](../images/docs/donut_percentages.png)

---

## Visual Behavior

- Data is **sorted by value descending** before rendering — the largest segment starts at the top (12 o'clock position).
- **Segments with value ≤ 0** are silently excluded.
- Segments are drawn clockwise starting from 90° (top of the ring).
- The **legend** is rendered as a structured list below the donut ring, with colored squares, category labels, and values.
- When `show_percentages=True`, each legend entry shows `"Label (XX.X%)"`.
- The **center label** is rendered in a medium-bold font at the exact center of the ring. Use `\n` for multi-line center labels (e.g., a number on top, a caption below).
- The donut width (ring thickness) is automatically calibrated relative to the overall size.
