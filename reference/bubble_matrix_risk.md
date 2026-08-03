---
layout: default
title: "Use Case: Enterprise Risk Heatmap"
parent: "Bubble Matrix Chart"
---
# Use Case: Enterprise Risk Heatmap


A classic grid where large, dark bubbles highlight catastrophic business risks.

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Risk": ["Cyber", "Market"], "Likelihood": ["High", "Low"], "Impact": ["High", "High"], "Cost": [100, 50]})

cc.plot_bubble_matrix_chart(
    data=df,
    title="Risk Assessment",
    subtitle="Size and color indicate financial exposure",
    start_color="#fee0d2",
    end_color="#de2d26"
)
```
