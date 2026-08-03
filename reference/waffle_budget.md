---
layout: default
title: "Use Case: Budget Allocation Block"
parent: "Waffle Chart"
---
# Use Case: Budget Allocation Block


Mapping distinct budget pools with a continuous gradient across 100 cells.

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Department": ["R&D", "Sales", "Ops", "G&A"], "Percent": [40, 30, 20, 10]})

cc.plot_waffle_chart(
    data=df,
    title="Budget Allocation",
    subtitle="Percent of total funding",
    start_color="#cccccc",
    end_color="#2323FF"
)
```
