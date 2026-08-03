---
layout: default
title: "Use Case: Quadrant Strategy Matrix"
parent: "Scatter Charts"
---
# Use Case: Quadrant Strategy Matrix

The 'Quadrant Matrix' is a staple of strategic consulting. By explicitly centering the axes to create four distinct zones (e.g., Leaders, Visionaries, Niche Players, Challengers), the chart categorizes continuous variables into discrete, understandable strategic buckets. To prevent overlapping chaos, labels are selectively applied only to the most critical data points. This format forces a decision framework onto raw data, making it the definitive choice for competitive landscape mapping.

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

![Use Case Preview](../images/docs/bubble_matrix_basic.png)
