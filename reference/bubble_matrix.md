---
layout: default
title: Bubble Matrix
parent: Chart Reference
nav_order: 9
---
# `plot_bubble_matrix_chart()`

Renders a bubble matrix chart — a grid of circles where each cell represents the intersection of a row category and a column header. Bubble **size** encodes the numeric value, and a continuous **color gradient** maps from the smallest to the largest value.

This chart is ideal for skill matrices, cross-tabulation heatmaps, and any two-dimensional categorical comparison where both magnitude and relative intensity matter.

![Bubble Matrix — Basic](../images/docs/bubble_matrix_basic.png)

---

## Signature

```python
clean_charts.plot_bubble_matrix_chart(
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
    show_values=True,
    value_suffix="",
    scale_text=True,
)
```

---

## Parameters

| Parameter        | Type             | Default         | Description |
|------------------|------------------|-----------------|-------------|
| `data`           | `pd.DataFrame`   | Built-in sample | DataFrame where Column 0 (str) = row category labels and every subsequent column (numeric) = values. Column headers become column labels. Values determine both bubble size and color intensity. |
| `output_path`    | `str \| None`    | `None`          | File path for the saved image. |
| `width`          | `int \| None`    | `1000`          | Image width in pixels. |
| `height`         | `int \| None`    | `700`           | Image height in pixels. |
| `aspect_ratio`   | `str \| None`    | `None`          | `"square"` / `"1:1"` (700×700), `"landscape"` / `"2:1"` (900×450), `"vertical"` / `"1:2"` (500×1000). |
| `title`          | `str \| None`    | `None`          | Bold title text (max 2 lines). |
| `subtitle`       | `str \| None`    | `None`          | Lighter subtitle text (max 3 lines). |
| `bg_color`       | `str \| None`    | `"#f4f3f0"`     | Background color. |
| `start_color`    | `str \| None`    | `"#000000"`     | Gradient start (lowest value). Note: the gradient is applied in reverse order (`end_color` → `start_color`). |
| `end_color`      | `str \| None`    | `"#2323FF"`     | Gradient end (highest value). |
| `show_values`    | `bool`           | `True`          | Display numeric values inside each bubble. |
| `value_suffix`   | `str`            | `""`            | String appended to value labels (e.g., `"%"`, `"x"`). |
| `scale_text`     | `bool`           | `True`          | Scale fonts proportionally. |

---

## Example

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({
    "Skill": ["Python", "JavaScript", "SQL", "Machine Learning", "Cloud"],
    "Junior": [65, 80, 45, 20, 15],
    "Mid-Level": [85, 75, 70, 55, 45],
    "Senior": [90, 60, 85, 80, 75],
    "Lead": [80, 45, 75, 90, 85],
})

cc.plot_bubble_matrix_chart(
    data=df,
    title="Engineering Skills Matrix",
    subtitle="Proficiency scores by seniority level",
    value_suffix="%",
)
```

![Bubble Matrix — Basic](../images/docs/bubble_matrix_basic.png)

---

## Visual Behavior

- **Bubble area** scales linearly from a minimum size (for the smallest value) to a maximum size (for the largest).
- The minimum bubble size is calibrated to be large enough to fit a value label inside.
- **Color** is assigned from a 256-step gradient ramp, interpolated between `start_color` and `end_color` based on each bubble's value relative to the global min/max.
- Values **≤ 0** or `NaN` are not plotted (no bubble drawn).
- **Column headers** are rendered above the grid, centered on each column, and auto-wrapped based on available column width.
- **Row labels** are rendered to the left of the grid, left-aligned flush with the title.
- All axes, ticks, and spines are hidden — the chart relies entirely on labels and bubbles.

---

## Notes

- This chart works best with **3–8 rows** and **2–6 columns**. Larger grids may produce small, hard-to-read bubbles.
- The bubble sizing is computed in data-unit space and converted to points² for `matplotlib.scatter`, ensuring consistent display across different figure sizes.
- When `show_values=False`, the chart becomes a pure size-and-color matrix — useful when you want the visual pattern to dominate.
