---
layout: default
title: Annotations & Separators
parent: Grouped Bar
nav_order: 1
---
# Grouped Bar: Annotations & Separators

The grouped bar chart can be transformed into an insightful scorecard by combining `group_comments` and `group_separators`. This is a highly effective way to present strategic metrics to executives.

## Use Case: Strategic Scorecard

By passing a list of dictionaries to `group_comments`, you can append custom insights to the right of the plot area. Setting `group_separators=True` draws horizontal lines between the groups, improving readability for dense charts.

```python
import pandas as pd
import clean_charts as cc

df_tech = pd.DataFrame({
    'Metric': ['Cloud Growth', 'Hardware Sales', 'Services Revenue'],
    'Q1': [12.4, 28.5, 15.2],
    'Q2': [18.2, 26.1, 16.5],
})

comments = [
    {
        "heading": "Cloud accelerating",
        "subtitle": "Q2 exceeded guidance",
        "big_number": "46%"
    },
    {
        "heading": "Hardware declining",
        "subtitle": "Supply chain constraints",
        "big_number": "-8%"
    },
    {
        "heading": "Services stable",
        "subtitle": "Consistent renewal rates",
        "big_number": "8%"
    }
]

cc.plot_grouped_barh_chart(
    data=df_tech,
    title="Segment Performance",
    subtitle="Q1 vs Q2 with YoY growth",
    value_suffix="B",
    group_comments=comments,
    group_separators=True
)
```

![Grouped Horizontal Bar — Complex](../images/docs/grouped_barh_complex.png)

## Comment Dictionary Structure

Each dictionary in the `group_comments` list maps directly to the corresponding category row in your DataFrame.

- `heading`: A bold, concise statement (e.g., "Cloud accelerating").
- `subtitle`: Lighter secondary text placed just below the heading.
- `big_number`: A prominent metric rendered on the far right (e.g., "46%").
