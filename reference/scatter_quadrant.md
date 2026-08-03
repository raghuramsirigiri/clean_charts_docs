---
layout: default
title: "Use Case: Quadrant Strategy Matrix"
parent: "Scatter Charts"
---
# Use Case: Quadrant Strategy Matrix


Group by quadrant classification and only show labels for specific points (e.g. Leaders).

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Vendor": ["A", "B", "C"], "Vision": [8, 3, 9], "Execution": [9, 4, 2], "Group": ["Leader", "Niche", "Visionary"]})

cc.plot_grouped_scatter_chart(
    data=df,
    title="Vendor Strategy Matrix",
    subtitle="Vision vs Execution",
    show_labels=True
)
```
