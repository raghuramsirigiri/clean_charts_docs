---
layout: chart
title: Insight Card
description: Bold text card for hero statistics and key takeaways.
permalink: /docs/charts/insight-card/
---

# `plot_insight_card()`

Plots a solid color card with large stylized text and an optional bottom image graphic. Best for hero statistics, key metric callouts, and executive summary highlights.

## Quick Example

```python
import clean_charts as cc

cc.plot_insight_card(
    text="Record-breaking $4.2B in Revenue",
    subtext="Driven by a massive 45% surge in Enterprise Cloud subscriptions across the APAC region.",
    image_path="3d.png",
    bg_color="#fff",
    text_color="#000",
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/insight_card_basic.png' | relative_url }}" alt="Insight Card" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Insight Card.</em>
  <br><a style="color: #666; font-size: 0.9em;" href="https://www.vecteezy.com/free-png/money">Money PNGs by Vecteezy</a>
</div>


## Parameters

<table class="param-table">
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Type</th>
      <th>Default</th>
      <th>Scope</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>output_path</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>File path to save.</td></tr>
    <tr><td><code>width</code></td><td><code>int | None</code></td><td>Auto</td><td><span class="badge common">Common</span></td><td>Image width in pixels.</td></tr>
    <tr><td><code>height</code></td><td><code>int | None</code></td><td>Auto</td><td><span class="badge common">Common</span></td><td>Image height in pixels.</td></tr>
    <tr><td><code>aspect_ratio</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td><code>"square"</code>, <code>"landscape"</code>, etc.</td></tr>
    <tr><td><code>title</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Bold header text.</td></tr>
    <tr><td><code>subtitle</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge common">Common</span></td><td>Secondary text.</td></tr>
    <tr><td><code>bg_color</code></td><td><code>str | None</code></td><td><code>"#f4f3f0"</code></td><td><span class="badge common">Common</span></td><td>Background hex color.</td></tr>
    <tr><td><code>scale_text</code></td><td><code>bool</code></td><td><code>True</code></td><td><span class="badge common">Common</span></td><td>Scale fonts proportionally.</td></tr>
    <tr><td><code>text</code></td><td><code>str</code></td><td><code>""</code></td><td><span class="badge unique">Unique</span></td><td>The main insight or summary text (large, bold).</td></tr>
    <tr><td><code>subtext</code></td><td><code>str</code></td><td><code>""</code></td><td><span class="badge unique">Unique</span></td><td>Secondary text displayed below the main text.</td></tr>
    <tr><td><code>image_path</code></td><td><code>str | None</code></td><td><code>None</code></td><td><span class="badge unique">Unique</span></td><td>Path to a raster image (PNG/JPG) rendered at the bottom of the card.</td></tr>
    <tr><td><code>text_color</code></td><td><code>str</code></td><td><code>"#000000"</code></td><td><span class="badge unique">Unique</span></td><td>Hex color for the text.</td></tr>
  </tbody>
</table>

## Common Scenarios

### Dark Theme Card

```python
cc.plot_insight_card(
    text="Record-breaking $4.2B in Revenue",
    subtext="Driven by a massive 45% surge in Enterprise Cloud subscriptions across the APAC region.",
    image_path="3d.png",
    bg_color="#000",
    text_color="#fff",
)
```

<div style="text-align: center; margin: 2rem 0;">
  <img src="{{ '/images/docs/insight_card_dark.png' | relative_url }}" alt="Insight Card" style="max-width: 100%; height: auto;" />
  <br>
  <em style="color: #666; font-size: 0.9em;">Example output for Insight Card.</em>
  <br><a style="color: #666; font-size: 0.9em;" href="https://www.vecteezy.com/free-png/money">Money PNGs by Vecteezy</a>
</div>

