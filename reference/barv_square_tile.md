---
layout: default
title: "Use Case: Square Tile KPI"
parent: "Bar Charts"
---
# Use Case: Square Tile KPI


A compact, chunky 3-bar chart designed to act as an inset card in a larger dashboard layout.

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Metric": ["A", "B", "C"], "Value": [10, 20, 15]})

cc.plot_barv_chart(
    data=df,
    title="Key Metrics",
    subtitle="Current Quarter",
    aspect_ratio="1:1",
    width=400,
    scale_text=True
)
```
