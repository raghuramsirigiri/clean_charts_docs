---
layout: default
title: "Use Case: Budget Allocation Block"
parent: "Waffle Chart"
---
# Use Case: Budget Allocation Block

While donut charts are excellent for high-level part-to-whole relationships, they fail when comparing segments of similar size due to our poor ability to judge angles. The 'Budget Allocation Block' waffle chart converts percentages into a strict, countable 10x10 grid. Using a continuous, monochromatic gradient across the segments allows the reader to visually estimate area far more accurately than radial slices. It provides a structured, rigid, and highly professional breakdown of resource distribution.

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Department": ["R&D", "Sales", "Ops", "G&A"], "Percent": [40, 30, 20, 10]})

cc.plot_waffle_chart(
    data=df,
    title="Budget Allocation",
    subtitle="Percent of total funding",
    start_color="#cccccc",
    end_color="#2323FF"
)
```

![Use Case Preview](../images/docs/waffle_basic.png)
