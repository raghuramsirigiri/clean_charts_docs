---
layout: default
title: Quick Start Guide
permalink: /docs/quick-start/
---

# Quick Start Guide

Get your first chart rendered in under a minute.

---

## Step 1: Install

```bash
pip install clean-charts
```

---

## Step 2: Your First Chart

Every chart function works the same way — pass a DataFrame and optional styling parameters:

```python
import pandas as pd
import clean_charts as cc

df = pd.DataFrame({
    "Response": ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
    "Count": [420, 310, 180, 60, 30],
})

cc.plot_barh_chart(
    data=df,
    title="Customer Satisfaction Survey",
    subtitle="Q2 2024 Results",
    value_suffix=" resp"
)
```

This displays a publication-quality horizontal bar chart inline. No configuration files, no theme setup — it just works.

---

## Step 3: Save to File

Pass `output_path` to export as PNG, JPG, PDF, or SVG:

```python
cc.plot_barh_chart(
    data=df,
    title="Customer Satisfaction Survey",
    output_path="survey_results.png"
)
```

---

## Step 4: Use Built-in Sample Data

Every function ships with sample data. Call without `data=` to see a demo:

```python
cc.plot_time_series(title="Market Trends")
cc.plot_donut_chart(title="Revenue Breakdown")
cc.plot_dumbbell_chart(title="Year-over-Year Change")
```

---

## Step 5: Control Dimensions

Use `aspect_ratio` for semantic sizing, or `width`/`height` for pixel-exact control:

```python
# Semantic
cc.plot_barh_chart(data=df, aspect_ratio="landscape")

# Pixel-exact
cc.plot_barh_chart(data=df, width=1200, height=600)
```

Available ratios: `"square"`, `"landscape"`, `"vertical"`, `"1:1"`, `"2:1"`, `"1:2"`

---

## What's Next?

- **[Global Parameters](../global-parameters/)** — shared options available on every chart
- **[Horizontal Bar](../charts/barh/)** — deep dive into your first chart type
- **[Dashboard](../charts/dashboard/)** — combine multiple charts into a single image
