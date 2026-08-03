---
layout: default
title: "Use Case: Timeline Histogram"
parent: "Bar Charts"
---
# Use Case: Timeline Histogram


Map continuous-like time data (e.g. years) with `bar_padding=0.05` to mimic a continuous distribution or volume chart.

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Year": [2018, 2019, 2020, 2021, 2022], "Volume": [10, 15, 25, 40, 60]})

cc.plot_barv_chart(
    data=df,
    title="Trading Volume",
    subtitle="Annual volume (millions)",
    bar_padding=0.05,
    color="#cccccc",
    value_suffix="M"
)
```
