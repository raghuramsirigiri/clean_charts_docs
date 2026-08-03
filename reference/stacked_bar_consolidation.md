---
layout: default
title: "Use Case: 100% Market Consolidation"
parent: "Stacked Bar Chart"
---
# Use Case: 100% Market Consolidation


Normalize a time series so every bar is the same length, visually emphasizing market share shifts.

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Year": [2020, 2021, 2022], "Incumbent": [80, 60, 40], "Challenger": [20, 40, 60]})

cc.plot_stacked_bar_chart(
    data=df,
    title="Market Share Shift",
    subtitle="Challenger eating incumbent share",
    show_percentages=True,
    bar_labels="none"
)
```
