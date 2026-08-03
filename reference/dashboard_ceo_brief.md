---
layout: default
title: "Use Case: CEO Morning Brief"
parent: "Dashboard Component"
---
# Use Case: CEO Morning Brief


Combine a Table, a Time Series, and 2 Insight Cards in a 2x2 mosaic layout.

```python
import clean_charts as cc

cc.plot_dashboard(
    charts=[...], # Provide generated chart objects
    layout="2x2",
    title="Executive Daily Brief"
)
```
