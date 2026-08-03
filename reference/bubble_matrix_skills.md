---
layout: default
title: "Use Case: Skills Proficiency Grid"
parent: "Bubble Matrix Chart"
---
# Use Case: Skills Proficiency Grid


A dense resource allocation map to see who is trained in what at a glance.

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Employee": ["Alice", "Bob"], "Skill": ["Python", "SQL"], "Level": [3, 1]})

cc.plot_bubble_matrix_chart(
    data=df,
    title="Team Skills Inventory",
    subtitle="Larger bubbles = higher proficiency"
)
```
