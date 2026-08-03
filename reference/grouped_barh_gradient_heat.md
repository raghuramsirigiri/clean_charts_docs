---
layout: default
title: "Use Case: Gradient Heat Progression"
parent: "Grouped Bar"
---
# Use Case: Gradient Heat Progression


Map consecutive periods with `bar_padding=0` and a continuous gradient to create a localized heat map feeling per group.

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Category": ["A", "B"], "Yr1": [10, 20], "Yr2": [12, 22], "Yr3": [15, 25], "Yr4": [18, 28], "Yr5": [22, 35]})

cc.plot_grouped_barh_chart(
    data=df,
    title="5-Year Progression",
    subtitle="Consistent growth across categories",
    start_color="#cccccc",
    end_color="#cc0000",
    bar_padding=0
)
```
