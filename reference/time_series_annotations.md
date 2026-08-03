---
layout: default
title: Annotations & Callouts
parent: Time Series
nav_order: 1
---
# Time Series: Annotations & Callouts

In addition to basic plotting, `plot_time_series` supports advanced annotations that allow you to highlight specific date ranges, draw vertical reference lines for events, and point out exact data points with callout boxes.

## Adding Reference Lines and Ranges

Use the `vlines` and `highlight_ranges` parameters to provide contextual information about events that affected the data.

### Example Code

```python
import pandas as pd
import clean_charts as cc

df = cc.get_default_data()

cc.plot_time_series(
    data=df[["date", "Apples"]],
    title="Apple Price Index",
    subtitle="Impact of historical events",
    vlines=[
        {
            "date": "2021-09-01", 
            "label": "Harvest Shortage", 
            "color": "#e3120b"
        }
    ],
    highlight_ranges=[
        {
            "start": "2020-03-01", 
            "end": "2020-06-01", 
            "color": "#dcdbd7", 
            "alpha": 0.5
        }
    ],
    callouts=[
        {
            "date": "2023-01-01", 
            "value": 145, 
            "text": "Peak Price Reached"
        }
    ]
)
```

## Parameter Details

* **`vlines`**: Accepts a list of dictionaries. Each dict requires a `"date"` key, and optionally `"label"` (short text) and `"color"`.
* **`highlight_ranges`**: Accepts a list of dictionaries with `"start"` and `"end"` date strings. Useful for showing periods of recession or market outages.
* **`callouts`**: Places a text box with an arrow pointing to a specific `(date, value)` coordinate. Requires `"date"`, `"value"`, and `"text"`.

## Output Variation

Unlike a standard line chart, adding these annotations directs the reader's eye immediately to the key takeaways of the visualization, adhering to editorial design principles.
