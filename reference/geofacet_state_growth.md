---
layout: default
title: "Use Case: US State Growth Trajectories"
parent: "Geofacet Component"
---
# Use Case: US State Growth Trajectories


Map 50 state line charts to a geographic grid.

```python
import clean_charts as cc
import pandas as pd

df = pd.DataFrame(...) # State, Year, Value data

cc.plot_geofacet(
    data=df,
    title="Growth by State",
    subtitle="10-year trajectory"
)
```
