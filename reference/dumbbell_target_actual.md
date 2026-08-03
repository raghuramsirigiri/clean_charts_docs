---
layout: default
title: "Use Case: Target vs Actual Tracker"
parent: "Dumbbell Chart"
---
# Use Case: Target vs Actual Tracker


Map a target (gray dot) against actual performance (black dot). The line highlights the gap size.

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Metric": ["A", "B", "C"], "Target": [100, 100, 100], "Actual": [85, 105, 90]})

cc.plot_dumbbell_chart(
    data=df,
    title="Performance to Target",
    subtitle="Gray = Target, Black = Actual",
    start_color="#d3d3d3",
    end_color="#000000",
    dot_size=120
)
```
