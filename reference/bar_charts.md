---
layout: default
title: Bar Charts
parent: Distributions & Rankings
nav_order: 1
has_children: true
---
# Bar Charts

**Overview**
Renders a bar chart with a single accent color, categorical labels, and numeric value labels. Designed for ranking, survey results, and categorical comparisons. Available in horizontal (`plot_barh_chart`) and vertical (`plot_barv_chart`) orientations.

![Horizontal Bar — Basic](../images/docs/barh_basic.png)

## Basic Usage

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({
    "Response": ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
    "Count": [42, 31, 18, 6, 3],
})

# Horizontal Bar
cc.plot_barh_chart(
    data=df,
    title="Customer Satisfaction Survey",
    subtitle="Horizontal orientation is best for long category names"
)

# Vertical Bar
cc.plot_barv_chart(
    data=df,
    title="Customer Satisfaction Survey",
    subtitle="Vertical orientation is best for short labels or time series"
)
```

## Data Requirements

The input `data` (a `pandas.DataFrame`) must adhere to the following constraints:
* **Dimensions**: Exactly two columns.
* **Column 0**: Category labels (strings).
* **Column 1**: Numeric values (float or int).
* **Ordering**: Rows are displayed in the exact order they appear in the DataFrame. Sort your DataFrame before plotting to achieve ranked charts.

## API Reference

```python
clean_charts.plot_barh_chart(
    data=None, output_path=None, width=None, height=None, aspect_ratio=None,
    title=None, subtitle=None, bg_color="#f4f3f0", color="#000000",
    bar_padding=0.35, value_suffix="", scale_text=True, show_percentages=False
)

clean_charts.plot_barv_chart(
    data=None, output_path=None, width=None, height=None, aspect_ratio=None,
    title=None, subtitle=None, bg_color="#f4f3f0", color="#000000",
    bar_padding=0.35, value_suffix="", scale_text=True, show_percentages=False
)
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `data` | `pd.DataFrame` | Built-in | 2-column DataFrame [Category, Value]. |
| `color` | `str` | `"#000000"` | Hex color for all bars. |
| `bar_padding` | `float` | `0.35` | Fraction of the bar slot left as gap between bars (0–1). Higher = thinner bars. |
| `value_suffix` | `str` | `""` | String appended to value labels and axis ticks (e.g., `%`, `M`). |
| `show_percentages`| `bool` | `False` | Show percentage labels (e.g., `"25.0%"`) instead of raw values. |

## Design Best Practices

* **Orientation**: Default to horizontal (`barh`) for most categorical data, as it allows long text labels to be read left-to-right easily. Reserve vertical (`barv`) for ordinal categories with short names (e.g., Q1, Q2, Q3) or discrete time periods.
* **Axis Labels**: Do not add explicit axis titles (like "Number of respondents"); instead, incorporate the unit into the `subtitle` or `value_suffix`.
