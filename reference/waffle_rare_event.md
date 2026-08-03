---
layout: default
title: "Use Case: The 1-in-100 Storyteller"
parent: "Waffle Chart"
---
# Use Case: The 1-in-100 Storyteller


A 10x10 grid with exactly one red square, illustrating how rare an event is.

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Category": ["Defect", "Clean"], "Count": [1, 99]})

cc.plot_waffle_chart(
    data=df,
    title="Defect Rate",
    subtitle="1 out of every 100 units is defective",
    color="#ff0000"
)
```
