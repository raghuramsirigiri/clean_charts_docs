---
layout: default
title: "Use Case: Linear Trend Identifier"
parent: "Scatter Charts"
---
# Use Case: Linear Trend Identifier


Find regressions in dense datasets by muting the scatter dots and blasting a bright red regression line.

```python
import pandas as pd
import clean_charts as cc

df = cc.get_default_data()

cc.plot_scatter_chart(
    data=df,
    title="Correlation Analysis",
    subtitle="Variable X vs Y",
    show_trendline=True,
    trendline_color="#ff0000",
    alpha=0.5
)
```
