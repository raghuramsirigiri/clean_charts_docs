---
layout: default
title: "Use Case: Conditional Heatmap"
parent: "Data Table Component"
---
# Use Case: Conditional Heatmap


Using cell formatting thresholds to color-code a grid of numbers.

```python
import clean_charts as cc
import pandas as pd

df = pd.DataFrame({"A": [1, 10], "B": [5, 2]})

cc.plot_table(
    data=df,
    title="Risk Matrix",
    conditional_formatting=True
)
```
