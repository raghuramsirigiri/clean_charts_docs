---
layout: default
title: "Use Case: Minimalist Ranking"
parent: "Bar Charts"
---
# Use Case: Minimalist Ranking


For pure rank orders (like 1st to 10th), reduce visual weight by using ultra-thin bars (`bar_padding=0.7`) and a black color.

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Rank": ["A", "B", "C"], "Score": [99, 85, 70]})

cc.plot_barh_chart(
    data=df,
    title="Top Performers",
    subtitle="Ranked by score",
    bar_padding=0.7,
    color="#000000",
    value_suffix=" pts"
)
```
