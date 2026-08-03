---
layout: default
title: Scatter Charts
parent: Relationships
has_children: true
nav_order: 14
---
# Scatter Charts

The `clean-charts` library provides three variants of scatter plots for visualizing relationships between continuous variables, grouped variables, and multi-dimensional data, all styled cleanly in the Economist aesthetic.

---

## `plot_scatter_chart()`

Plots a 2D scatter plot.

### API Reference

```python
clean_charts.plot_scatter_chart(
    data=None,
    output_path=None,
    width=None,
    height=None,
    aspect_ratio=None,
    title=None,
    subtitle=None,
    bg_color=None,
    color=None,
    dot_size=80,
    alpha=0.75,
    x_label=None,
    y_label=None,
    x_suffix="",
    y_suffix="",
    show_labels=False,
    show_trendline=False,
    trendline_color=None,
    axes_origin=None,
    show_grid=True,
    scale_text=True,
)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `data` | `pd.DataFrame \| None` | Built-in | DataFrame with 2 or 3 columns (Col 0: X, Col 1: Y or Col 0: Labels, Col 1: X, Col 2: Y). |
| `output_path` | `str \| None` | `None` | File path for the saved image. |
| `width` | `int \| None` | `700` | Target image width in pixels. |
| `height` | `int \| None` | `500` | Target image height in pixels. |
| `aspect_ratio` | `str \| None` | `None` | `"square"`, `"landscape"`, `"vertical"`, `"1:1"`, `"2:1"`, `"1:2"`. |
| `title` | `str \| None` | `None` | Header title (bold). |
| `subtitle` | `str \| None` | `None` | Subtitle text. |
| `bg_color` | `str \| None` | `None` | Hex background color. Defaults to Economist cream. |
| `color` | `str \| None` | `None` | Hex color for scatter dots. |
| `dot_size` | `float` | `80` | Marker size (area in points^2). |
| `alpha` | `float` | `0.75` | Transparency of scatter points (0.0 to 1.0). |
| `x_label`, `y_label` | `str \| None` | `None` | Labels for X and Y axes. |
| `x_suffix`, `y_suffix` | `str` | `""` | Suffix strings for axis annotations (e.g., "$", "%"). |
| `show_labels` | `bool` | `False` | Annotate scatter points with label strings. |
| `show_trendline` | `bool` | `False` | Plot a linear regression trend line. |
| `trendline_color` | `str \| None` | `None` | Hex color for the trend line. |

---

## `plot_grouped_scatter_chart()`

Plots a grouped or quadrant-mapped scatter plot.

### API Reference

```python
clean_charts.plot_grouped_scatter_chart(
    data=None,
    output_path=None,
    width=None,
    height=None,
    aspect_ratio=None,
    title=None,
    subtitle=None,
    bg_color=None,
    color=None,
    end_color=None,
    colors=None,
    dot_size=80,
    alpha=0.75,
    x_label=None,
    y_label=None,
    x_suffix="",
    y_suffix="",
    group_by=None,
    x_threshold=None,
    y_threshold=None,
    quadrant_labels=None,
    show_labels=False,
    show_threshold_lines=True,
    axes_origin=None,
    show_grid=True,
    scale_text=True,
)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `data` | `pd.DataFrame \| None` | Built-in | Categorical mode: 3-4 cols. Quadrant mode: 2-3 cols. |
| `group_by` | `str \| None` | `None` | `"category"` or `"quadrant"`. |
| `x_threshold`, `y_threshold` | `float \| None` | `None` | Threshold lines for quadrant division. Defaults to mean. |
| `quadrant_labels` | `list \| None` | `None` | Labels for Q1 (top-right), Q2 (top-left), Q3 (bottom-left), Q4 (bottom-right). |
| `start_color`, `end_color` | `str \| None` | `None` | Hex colors for group palette interpolation. |
| `colors` | `list \| None` | `None` | Explicit list of hex colors for categories/quadrants. |
| `show_threshold_lines` | `bool` | `True` | Plots x and y threshold lines in quadrant mode. |

*(Also shares standard output, dimensions, title, axis, and styling parameters with `plot_scatter_chart`)*

---

## `plot_bubble_scatter_chart()`

Plots a 3-variable bubble scatter plot where dot size encodes the third dimension.

### API Reference

```python
clean_charts.plot_bubble_scatter_chart(
    data=None,
    output_path=None,
    width=None,
    height=None,
    aspect_ratio=None,
    title=None,
    subtitle=None,
    bg_color=None,
    color=None,
    end_color=None,
    color=None,
    min_bubble_size=60,
    max_bubble_size=600,
    alpha=0.7,
    x_label=None,
    y_label=None,
    x_suffix="",
    y_suffix="",
    size_suffix="",
    show_values=False,
    show_labels=False,
    axes_origin=None,
    show_grid=True,
    scale_text=True,
)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `data` | `pd.DataFrame \| None` | Built-in | 3 columns: [X, Y, Size] or 4 columns: [Label, X, Y, Size]. |
| `min_bubble_size` | `float` | `60` | Minimum bubble marker area in points^2. |
| `max_bubble_size` | `float` | `600` | Maximum bubble marker area in points^2. |
| `size_suffix` | `str` | `""` | Suffix string for annotations (e.g., "M"). |
| `show_values` | `bool` | `False` | Annotate bubbles with their size values. |
| `start_color`, `end_color` | `str \| None` | `None` | Hex colors for bubble palette interpolation if `color` is None. |
| `color` | `str \| None` | `None` | Single color for all bubbles. |

*(Also shares standard output, dimensions, title, axis, and styling parameters with `plot_scatter_chart`)*
