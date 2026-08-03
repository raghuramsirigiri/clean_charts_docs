---
layout: default
title: "Use Case: Skills Proficiency Grid"
parent: "Bubble Matrix Chart"
---
# Use Case: Skills Proficiency Grid

Mapping organizational capabilities across a wide array of resources is a notoriously difficult visualization challenge. The 'Skills Proficiency Grid' solves this by deploying a clean matrix where employees and skills form the axes, and bubble size encodes the depth of expertise. This creates an immediate visual footprint of a team's capabilities. Skill gaps appear as glaring white spaces, while concentrated expertise forms dense clusters, allowing leadership to instantly assess resource allocation.

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

![Use Case Preview](../images/docs/bubble_matrix_basic.png)
