import os
import glob
import re

docs_dir = r"c:\Users\raghu\Documents\AG Projects\clean_chart_docs\docs\charts"
image_mapping = {
    "barh.md": ["barh_basic.png", "barh_compact.png", "barh_percentages.png"],
    "barv.md": ["barv_basic.png", "barv_basic.png", "barv_basic.png"],
    "grouped-barh.md": ["grouped_barh_basic.png", "grouped_barh_comments.png", "grouped_finance.png"],
    "stacked-bar.md": ["stacked_bar_basic.png", "stacked_bar_pct.png", "stacked_churn.png"],
    "time-series.md": ["time_series_basic.png", "time_series_markers.png", "ts_macro.png", "time_series_callouts.png"],
    "scatter.md": ["scatter_basic.png", "scatter_basic.png", "scatter_basic.png"],
    "grouped-scatter.md": ["grouped_scatter_basic.png", "grouped_scatter_basic.png", "grouped_scatter_basic.png"],
    "bubble-scatter.md": ["bubble_scatter_basic.png", "bubble_scatter_basic.png"],
    "bubble-matrix.md": ["bubble_matrix_basic.png", "bubble_matrix_basic.png"],
    "donut.md": ["donut_basic.png", "donut_percentages.png", "donut_portfolio.png"],
    "waffle.md": ["waffle_basic.png", "waffle_basic.png"],
    "dumbbell.md": ["dumbbell_basic.png", "dumbbell_dynamic.png", "dumbbell_no_labels.png"],
    "geofacet.md": ["geofacet_bar.png", "geofacet_donut.png", "geofacet_text.png"],
    "insight-card.md": ["insight_card_basic.png", "insight_card_dark.png", "insight_card_basic.png"],
    "table.md": ["table_basic.png", "table_highlights.png", "table_basic.png"],
    "dashboard.md": ["dashboard_basic.png", "dashboard_basic.png"]
}

for filepath in glob.glob(os.path.join(docs_dir, "*.md")):
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove "## Visual Output\n\n"
    content = re.sub(r'## Visual Output\n+', '', content)
    
    # Remove the div containers, we will insert images manually
    content = re.sub(r'<div class="chart-preview-card">.*?</div>\n+', '', content, flags=re.DOTALL)

    # Now, find all python code blocks and append an image
    # We will split the content by python blocks
    parts = re.split(r'(```python.*?```)', content, flags=re.DOTALL)
    
    new_content = ""
    images = image_mapping.get(filename, [])
    img_idx = 0
    
    for part in parts:
        new_content += part
        if part.startswith("```python"):
            # Insert image if we have one
            img_file = images[img_idx] if img_idx < len(images) else (images[-1] if images else None)
            if img_file:
                # Add image right after the code block
                title = filename.replace(".md", "").replace("-", " ").title()
                new_content += f"\n\n![{title}]({{{{ '/images/docs/{img_file}' | relative_url }}}})\n*Example output for {title}.*"
            img_idx += 1
            
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

print("Updated all charts files.")
