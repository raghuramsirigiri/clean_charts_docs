---
layout: default
title: "Use Case: Hero Metric Focus"
parent: "Donut Chart"
---
# Use Case: Hero Metric Focus


Focus entirely on a single slice of dominance with a massive center label.

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Category": ["Market Leader", "Others"], "Share": [85, 15]})

cc.plot_donut_chart(
    data=df,
    title="Market Dominance",
    subtitle="Leader share vs competitors",
    center_label="85%"
)
```
