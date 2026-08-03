---
layout: default
title: "Use Case: Recession Highlighter"
parent: "Time Series"
---
# Use Case: Recession Highlighter


By manipulating `smooth`, `markers`, and `highlight_ranges`, you can emphasize periods of market downturns while maintaining strict step-changes in the data line.

```python
import pandas as pd
import clean_charts as cc

df = cc.get_default_data()

cc.plot_time_series(
    data=df[["date", "Index_A"]],
    title="Market Activity",
    subtitle="Impact of the 2020 and 2022 slowdowns",
    smooth=False,
    markers=None,
    highlight_ranges=[
        {"start": "2020-02-01", "end": "2020-05-01", "color": "#dcdbd7", "alpha": 0.8},
        {"start": "2022-01-01", "end": "2022-09-01", "color": "#dcdbd7", "alpha": 0.8}
    ]
)
```
