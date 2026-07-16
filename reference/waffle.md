---
layout: default
title: Waffle Chart
parent: Chart Reference
nav_order: 6
---
# `plot_waffle_chart()`

Renders a waffle chart — an array of small squares (typically 100 per group) where filled squares represent a percentage value. Inspired by the McKinsey/BCG style of presenting survey data, each group includes a heading, description, and a bold numeric callout.

This chart excels at communicating "X out of 100" or "X percent" in a visually intuitive way.

![Waffle — Basic](../images/docs/waffle_basic.png)

---

## Signature

```python
clean_charts.plot_waffle_chart(
    data=None,
    output_path=None,
    width=None,
    height=None,
    aspect_ratio=None,
    title=None,
    subtitle=None,
    bg_color=None,
    color=None,
    muted_color=None,
    value_suffix="%",
    scale_text=True,
)
```

---

## Parameters

| Parameter      | Type             | Default         | Description |
|----------------|------------------|-----------------|-------------|
| `data`         | `pd.DataFrame`   | Built-in sample | DataFrame with exactly **three columns**: Column 0 (`str`) = heading text for each waffle group (supports `\n` for multiline). Column 1 (`str`) = description text below the heading. Column 2 (`numeric`) = value (0–100, representing a percentage). |
| `output_path`  | `str \| None`    | `None`          | File path for the saved image. |
| `width`        | `int \| None`    | `600`           | Image width in pixels. |
| `height`       | `int \| None`    | Auto            | Auto-sized based on group count and layout. |
| `aspect_ratio` | `str \| None`    | `None`          | `"square"`, `"landscape"`, `"vertical"`. |
| `title`        | `str \| None`    | `None`          | Bold title text. |
| `subtitle`     | `str \| None`    | `None`          | Lighter subtitle text. |
| `bg_color`     | `str \| None`    | `"#f4f3f0"`     | Background color. |
| `color`        | `str \| None`    | `"#000000"`     | Hex color for filled squares. Defaults to `config.DEFAULT_COLOR`. |
| `muted_color`  | `str \| None`    | `"#94A3C0"`     | Hex color for unfilled (empty) squares. Defaults to `config.DEFAULT_COLOR_MUTED`. |
| `value_suffix` | `str`            | `"%"`           | String appended to the numeric callout label (e.g., `"%"`, `"pp"`). |
| `scale_text`   | `bool`           | `True`          | Scale fonts proportionally. |

---

## Example

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({
    "Heading": [
        "Growth\nFocus",
        "Volatility\nResponse",
        "Customer\nInput",
    ],
    "Description": [
        "report they focus 30%+ of their time on long-term growth",
        "increase resourcing for growth during volatility",
        "consistently incorporate customer input into decisions",
    ],
    "Value": [29, 30, 15],
})

cc.plot_waffle_chart(
    data=df,
    title="Leadership Priorities Survey",
    subtitle="% of executives who agree with each statement",
)
```

![Waffle — Basic](../images/docs/waffle_basic.png)

---

## Visual Behavior

- Each group is rendered as a **10×10 grid** of rounded-corner squares (100 total).
- The **filled count** = the value rounded to the nearest integer, filling **top-to-bottom, left-to-right**.
- Above the waffle grid:
  - **Big number** (e.g., `"29%"`) in large, bold text.
  - **Heading** (from column 0) in medium bold text. Supports line breaks with `\n`.
  - **Description** (from column 1) in smaller text below the heading. Auto-wrapped.
- Multiple groups are arranged **side-by-side** horizontally, each in its own column.
- The waffle squares use a slight corner radius for a polished, modern feel.
- A thin horizontal **separator line** is drawn below each group's heading area.

---

## Notes

- Values should be in the range **0–100**. Values outside this range are clamped.
- The chart is optimized for **2–4 groups**. More than 4 may produce small, hard-to-read squares.
- Use `\n` in heading text to create multi-line group headings (e.g., `"Growth\nFocus"`).
