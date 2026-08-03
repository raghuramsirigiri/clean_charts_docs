---
layout: default
title: "Use Case: Annotated Milestones"
parent: "Time Series"
---
# Use Case: Annotated Milestones


To create a large-format poster layout highlighting specific events, use `vlines` with paragraph dictionaries alongside `callouts`.

```python
import pandas as pd
import clean_charts as cc

df = cc.get_default_data()

cc.plot_time_series(
    data=df[["date", "Users"]],
    title="User Growth Over Time",
    subtitle="Key product milestones",
    scale_text=True,
    line_labels="both",
    vlines=[
        {
            "date": "2022-06-15", 
            "label": "Version 2.0", 
            "paragraph": "Major UI overhaul and new features released"
        }
    ],
    callouts=[
        {"date": "2023-01-01", "value": 1M, "text": "1M Users Reached"}
    ]
)
```
