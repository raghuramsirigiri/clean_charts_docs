---
layout: default
title: "Use Case: Enterprise Risk Heatmap"
parent: "Bubble Matrix Chart"
---
# Use Case: Enterprise Risk Heatmap

Enterprise risk management demands absolute clarity regarding both probability and consequence. The 'Risk Heatmap' utilizes a rigorous cross-tabulation grid where Likelihood and Impact serve as the axes. By employing a fierce red gradient for the bubbles, the chart naturally draws the executive's eye to the top-right quadrant—the zone of catastrophic exposure. This layout strips away ambiguity, forcing a clear prioritization of mitigation efforts.

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Risk": ["Cyber", "Market"], "Likelihood": [10, 2], "Impact": [10, 10], "Cost": [100, 50]})

cc.plot_bubble_matrix_chart(
    data=df,
    title="Risk Assessment",
    subtitle="Size and color indicate financial exposure",
    end_)
```

![Use Case Preview](../images/docs/bubble_matrix_basic.png)
