---
layout: default
title: "Use Case: Strategic Scorecard"
parent: "Grouped Bar"
---
# Use Case: Strategic Scorecard


Spread groups far apart and use `group_comments` to append a massive delta metric to the right side of the visual.

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Division": ["North", "South"], "Target": [100, 100], "Actual": [110, 90]})

cc.plot_grouped_barh_chart(
    data=df,
    title="Division Performance",
    subtitle="Target vs Actual",
    group_separators=True,
    group_padding=0.8,
    bar_labels="none",
    group_comments=[
        {"heading": "North", "subtitle": "Exceeded", "big_number": "+10%"},
        {"heading": "South", "subtitle": "Missed", "big_number": "-10%"}
    ]
)
```
