---
layout: default
title: "Use Case: Linear Trend Identifier"
parent: "Scatter Charts"
---
# Use Case: Linear Trend Identifier

In exceptionally dense datasets, plotting hundreds or thousands of scatter points can result in an unreadable cloud of visual noise. The 'Linear Trend Identifier' technique suppresses the opacity of individual data points, pushing them into the background. It then overlays a high-contrast regression line. This deliberate hierarchy tells the reader that while the variance exists, the only thing that matters is the overarching correlation trajectory, cutting through the noise to deliver a singular, actionable insight.

```python
import pandas as pd
import clean_charts as cc

df = cc.get_default_data()

cc.plot_scatter_chart(
    data=df,
    title="Correlation Analysis",
    subtitle="Variable X vs Y",
    show_trendline=True,
    trendline_color="#ff0000",
    alpha=0.5
)
```

![Use Case Preview](../images/docs/time_series_basic.png)
