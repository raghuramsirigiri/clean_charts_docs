---
layout: default
title: Global Parameters
permalink: /docs/global-parameters/
---

# Global Parameters

Almost all chart functions in `clean_charts` share a common set of parameters. These control output, dimensions, titles, and styling. Each individual chart page lists these alongside its unique parameters with a **Scope** badge to distinguish them.

---

## Output & Dimensions

<table class="param-table">
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Type</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>data</code></td>
      <td><code>pd.DataFrame</code></td>
      <td>Built-in sample</td>
      <td>Input tabular data. If <code>None</code>, uses a built-in sample dataset for demonstration.</td>
    </tr>
    <tr>
      <td><code>output_path</code></td>
      <td><code>str | None</code></td>
      <td><code>None</code></td>
      <td>File path to save the chart (<code>.png</code>, <code>.jpg</code>, <code>.pdf</code>, <code>.svg</code>). If <code>None</code>, displays inline.</td>
    </tr>
    <tr>
      <td><code>width</code></td>
      <td><code>int | None</code></td>
      <td>Auto</td>
      <td>Explicit image width in pixels.</td>
    </tr>
    <tr>
      <td><code>height</code></td>
      <td><code>int | None</code></td>
      <td>Auto</td>
      <td>Explicit image height in pixels.</td>
    </tr>
    <tr>
      <td><code>aspect_ratio</code></td>
      <td><code>str | None</code></td>
      <td><code>None</code></td>
      <td>Semantic sizing: <code>"square"</code>, <code>"landscape"</code>, <code>"vertical"</code>, <code>"1:1"</code>, <code>"2:1"</code>, <code>"1:2"</code>. Overrides <code>width</code> and <code>height</code>.</td>
    </tr>
  </tbody>
</table>

---

## Titles & Labels

<table class="param-table">
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Type</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>title</code></td>
      <td><code>str | None</code></td>
      <td><code>None</code></td>
      <td>Bold header text, flush-left aligned. Auto-wrapped to fit chart width.</td>
    </tr>
    <tr>
      <td><code>subtitle</code></td>
      <td><code>str | None</code></td>
      <td><code>None</code></td>
      <td>Lighter secondary text displayed below the title.</td>
    </tr>
  </tbody>
</table>

---

## Styling

<table class="param-table">
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Type</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>bg_color</code></td>
      <td><code>str | None</code></td>
      <td><code>"#f4f3f0"</code></td>
      <td>Background hex color. Defaults to Economist cream.</td>
    </tr>
    <tr>
      <td><code>scale_text</code></td>
      <td><code>bool</code></td>
      <td><code>True</code></td>
      <td>Scale fonts proportionally with image size.</td>
    </tr>
    <tr>
      <td><code>value_suffix</code></td>
      <td><code>str</code></td>
      <td><code>""</code></td>
      <td>String appended to data labels and axis ticks (e.g., <code>"%"</code>, <code>"M"</code>, <code>"x"</code>).</td>
    </tr>
    <tr>
      <td><code>show_percentages</code></td>
      <td><code>bool</code></td>
      <td><code>False</code></td>
      <td>Format numeric values as percentages (e.g., <code>0.25</code> → <code>"25.0%"</code>).</td>
    </tr>
  </tbody>
</table>

---

## Color Parameters

Many chart functions accept color parameters. The naming convention is:

- **`color`** — single hex color for all elements (bars, dots, lines)
- **`start_color`** / **`end_color`** — gradient boundary colors when multiple series or segments need differentiation
- **`colors`** — explicit list of hex colors when you want full control per series
