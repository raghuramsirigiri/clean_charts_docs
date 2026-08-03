---
layout: default
title: "Use Case: Revenue Layer Cake"
parent: "Stacked Bar Chart"
---
# Use Case: Revenue Layer Cake


A towering vertical stacked bar distinguishing multiple product tiers via a gradient.

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Year": [2020, 2021, 2022], "Tier 1": [10, 15, 20], "Tier 2": [20, 25, 30], "Tier 3": [30, 35, 40]})

cc.plot_stacked_bar_chart(
    data=df,
    title="Revenue by Tier",
    subtitle="Absolute values in millions",
    show_percentages=False,
    bar_labels="both",
    aspect_ratio="vertical",
    start_color="#e0e0ff",
    end_color="#000080"
)
```
