---
layout: default
title: "Use Case: The 1-in-100 Storyteller"
parent: "Waffle Chart"
---
# Use Case: The 1-in-100 Storyteller

Humans struggle to conceptualize abstract probabilities, especially for rare events. The '1-in-100 Storyteller' bypasses this cognitive hurdle by plotting exactly one hundred distinct squares. By coloring 99 squares in a muted gray and highlighting a single square in alarming red, it provides a visceral, physical representation of a defect rate or rare occurrence. This technique is far more impactful than writing '1%', as it forces the brain to process the actual ratio visually.

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

![Use Case Preview](../images/docs/waffle_basic.png)
