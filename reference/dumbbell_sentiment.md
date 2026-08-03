---
layout: default
title: "Use Case: Sentiment Shift"
parent: "Dumbbell Chart"
---
# Use Case: Sentiment Shift


Map 'Before' and 'After' sentiment scores, separating the questions clearly.

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({"Question": ["UX", "Speed", "Reliability"], "Before": [3.2, 2.5, 4.0], "After": [4.5, 4.2, 4.1]})

cc.plot_dumbbell_chart(
    data=df,
    title="Product Sentiment Shift",
    subtitle="Before vs After v2.0 Release (1-5 Scale)",
    bar_padding=0.5
)
```
