---
layout: default
title: "Use Case: Gradient Heat Progression"
parent: "Grouped Bar"
---
# Use Case: Gradient Heat Progression

Traditional grouped bar charts often suffer from the 'rainbow effect', using disparate, chaotic colors for each category that confuse the eye. The 'Gradient Heat' progression solves this by mapping consecutive periods (like years or quarters) to a smooth, two-anchor color gradient. Stripping away the bar padding fuses the periods together. This elegant technique allows the viewer's eye to intuitively follow the 'heat' of the gradient, instantly recognizing trends and momentum within a category without repeatedly checking a legend.

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Category": ["A", "B"], "Yr1": [10, 20], "Yr2": [12, 22], "Yr3": [15, 25], "Yr4": [18, 28], "Yr5": [22, 35]})

cc.plot_grouped_barh_chart(
    data=df,
    title="5-Year Progression",
    subtitle="Consistent growth across categories",
    end_bar_padding=0
)
```

![Use Case Preview](../images/docs/grouped_barh_basic.png)
