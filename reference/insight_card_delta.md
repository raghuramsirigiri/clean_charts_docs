---
layout: default
title: "Use Case: Positive Delta Alert"
parent: "Insight Card Component"
---
# Use Case: Positive Delta Alert


A hero metric highlighting a positive YoY jump with a green color.

```python
import clean_charts as cc

cc.plot_insight_card(
    value="+14%",
    title="Year over Year Growth",
    subtitle="Exceeding Q3 guidance",
    value_color="green"
)
```
