---
layout: default
title: "Use Case: 3D Market Map"
parent: "Scatter Charts"
---
# Use Case: 3D Market Map


Use bubble sizing to add a third dimension of financial weight to a standard XY correlation.

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Company": ["A", "B", "C"], "Revenue": [10, 50, 100], "Growth": [0.5, 0.2, 0.1], "MarketCap": [100, 500, 1000]})

cc.plot_bubble_scatter_chart(
    data=df,
    title="Market Landscape",
    subtitle="Size = Market Cap",
    dot_size=200
)
```
