---
layout: default
title: "Use Case: Positive Delta Alert"
parent: "Insight Card Component"
---
# Use Case: Positive Delta Alert

Sometimes, a chart is overkill. When the entire goal of a presentation is to communicate a single, game-changing shift, the 'Insight Card' strips away all axes, legends, and data points. By employing massive typographic scale and using semantic color (such as a vivid green for positive growth), it elevates a raw number into a 'hero metric'. This uncompromising design choice guarantees that the most critical delta of the quarter is etched into the audience's memory.

```python
import clean_charts as cc

cc.plot_insight_card(
    value="+14%",
    title="Year over Year Growth",
    subtitle="Exceeding Q3 guidance",
    value_color="green"
)
```

![Use Case Preview](../images/docs/insight_card_basic.png)
