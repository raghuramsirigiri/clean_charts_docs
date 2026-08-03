---
layout: default
title: "Use Case: Hero Metric Focus"
parent: "Donut Chart"
---
# Use Case: Hero Metric Focus

When a single metric dictates the narrative—such as an overwhelming market dominance or a critical failure rate—a multi-slice pie chart dilutes the message. The 'Hero Metric' donut aggressively simplifies the data into two buckets: the dominant slice, and 'Everything Else'. By punching out the center and placing a massive, bold percentage label in the negative space, the design forces the reader to confront a single, undeniable fact. It is unapologetic, highly focused editorial design.

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

![Use Case Preview](../images/docs/donut_basic.png)
