---
layout: default
title: Dumbbell Chart
parent: Chart Reference
nav_order: 7
---
# `plot_dumbbell_chart()`

Renders a dumbbell chart (also called a Cleveland dot plot or lollipop chart) that visually encodes the difference between two values per category using connected dots. Ideal for "before vs. after", "actual vs. target", or "Period A vs. Period B" comparisons.

![Dumbbell — Basic](../images/docs/dumbbell_basic.png)

---

## Signature

```python
clean_charts.plot_dumbbell_chart(
    data=None,
    output_path=None,
    width=None,
    height=None,
    aspect_ratio=None,
    title=None,
    subtitle=None,
    bg_color=None,
    start_color=None,
    end_color=None,
    connector_color=None,
    value_suffix="",
    show_values=True,
    scale_text=True,
)
```

---

## Parameters

| Parameter          | Type             | Default     | Description |
|--------------------|------------------|-------------|-------------|
| `data`             | `pd.DataFrame`   | Built-in    | DataFrame with exactly **three columns**: Column 0 (str) = category labels. Column 1 (numeric) = left dot value (e.g., "before" or "2020"). Column 2 (numeric) = right dot value (e.g., "after" or "2023"). |
| `output_path`      | `str \| None`    | `None`      | File path for the saved image. |
| `width`            | `int \| None`    | `600`       | Image width in pixels. |
| `height`           | `int \| None`    | Auto        | Auto-sized: `max(300, 120 + n × 65)`. |
| `aspect_ratio`     | `str \| None`    | `None`      | `"square"`, `"landscape"`, `"vertical"`. |
| `title`            | `str \| None`    | `None`      | Bold title text. |
| `subtitle`         | `str \| None`    | `None`      | Lighter subtitle text. |
| `bg_color`         | `str \| None`    | `"#f4f3f0"` | Background color. |
| `start_color`      | `str \| None`    | `"#000000"` | Hex color for the **first** value column (Column 1) dots. |
| `end_color`        | `str \| None`    | `"#2323FF"` | Hex color for the **second** value column (Column 2) dots. |
| `connector_color`  | `str \| None`    | `"#94A3C0"` | Hex color for the horizontal line connecting the two dots. |
| `value_suffix`     | `str`            | `""`        | String appended to value annotations. |
| `show_values`      | `bool`           | `True`      | Display numeric values next to each dot. |
| `scale_text`       | `bool`           | `True`      | Scale fonts proportionally. |

---

## Example

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({
    "Country": ["United States", "China", "Germany",
                "United Kingdom", "India", "France"],
    "2010": [14.99, 6.09, 3.42, 2.48, 1.68, 2.65],
    "2023": [25.46, 17.79, 4.46, 3.33, 3.73, 3.05],
})

cc.plot_dumbbell_chart(
    data=df,
    title="GDP Growth by Country",
    subtitle="GDP in trillions USD, 2010 vs. 2023",
    value_suffix="T",
    show_values=True,
)
```

![Dumbbell — Basic](../images/docs/dumbbell_basic.png)

---

## Visual Behavior

- A **color legend** is automatically drawn between the subtitle and the chart, showing the two series names with colored dot indicators.
- Each category row displays:
  - A horizontal **connector line** in `connector_color` spanning the range between the two values.
  - Two **dots** (circles): one in `start_color` (Column 1) and one in `end_color` (Column 2).
  - When `show_values=True`, numeric values appear as small annotations near each dot.
- The X-axis ticks appear along the **top** of the chart.
- **Category labels** are left-aligned flush with the title and subtitle.
- **Gridlines** run vertically through the chart area.
- Data is displayed top-to-bottom in the order it appears in the DataFrame.

---

## Notes

- The chart expects exactly **three columns**: one label column and two value columns. Additional columns are ignored.
- The column names (e.g., `"2010"` and `"2023"`) automatically populate the legend.
- Dot sizes are proportional to `scale` for visual consistency.
