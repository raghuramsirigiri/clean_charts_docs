---
layout: default
title: "Use Case: Square Tile KPI"
parent: "Bar Charts"
---
# Use Case: Square Tile KPI

Modern executive dashboards demand extreme spatial efficiency. The 'Square Tile' variation forces a strict 1:1 aspect ratio, condensing a standard vertical bar chart into a punchy, modular component. By scaling the text proportionally to fit the constrained bounding box, it ensures perfect legibility on high-resolution displays. This format is the gold standard for multi-metric 'cockpit' layouts, allowing you to tile multiple distributions side-by-side without visual friction.

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

![Use Case Preview](../images/docs/barv_basic.png)
