import sys
import os
import pandas as pd

# Add localforge to path to import clean_charts
current_dir = os.path.dirname(os.path.abspath(__file__))
localforge_dir = os.path.abspath(os.path.join(current_dir, "../../localforge"))
sys.path.insert(0, localforge_dir)

from clean_charts import (
    plot_barh_chart,
    plot_barv_chart,
    plot_time_series,
    plot_donut_chart,
    plot_grouped_barh_chart,
    plot_stacked_bar_chart
)

output_dir = os.path.abspath(os.path.join(current_dir, "../images/docs"))
os.makedirs(output_dir, exist_ok=True)

def generate_bar_charts():
    print("Generating bar charts...")
    # Horizontal Bar
    df_h = pd.DataFrame({
        "Response": ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
        "Count": [420, 310, 180, 60, 30],
    })
    
    plot_barh_chart(
        data=df_h,
        title="Customer Satisfaction Survey",
        subtitle="Horizontal orientation is best for long category names",
        value_suffix=" resp",
        bar_padding=0.3,
        output_path=os.path.join(output_dir, "barh_basic.png")
    )
    
    # Vertical Bar
    df_v = pd.DataFrame({
        "Quarter": ["Q1", "Q2", "Q3", "Q4"],
        "Revenue": [12.5, 14.2, 11.8, 16.5]
    })
    
    plot_barv_chart(
        data=df_v,
        title="Quarterly Revenue",
        subtitle="Vertical orientation is best for short labels or time series",
        value_suffix="M",
        output_path=os.path.join(output_dir, "barv_basic.png")
    )

def generate_time_series():
    print("Generating time series charts...")
    df_ts = pd.DataFrame({
        "date": pd.date_range(start="2024-01-01", periods=12, freq="ME"),
        "Revenue": [120, 135, 142, 128, 155, 162, 175, 190, 185, 205, 215, 230],
        "Costs": [90, 95, 98, 105, 102, 110, 115, 120, 118, 125, 130, 135]
    })
    
    plot_time_series(
        data=df_ts,
        title="Quarterly Financials",
        subtitle="Revenue vs Costs in USD Thousands",
        label_frequency="quarter",
        line_labels="name",
        value_suffix="k",
        vlines={"date": "2024-06-30", "color": "#000000", "label": "Product Launch"},
        output_path=os.path.join(output_dir, "time_series_basic.png")
    )

def generate_donut():
    print("Generating donut charts...")
    df_donut = pd.DataFrame({
        'Source': ['Solar', 'Wind', 'Nuclear', 'Natural Gas', 'Coal'],
        'TWh': [1200, 1500, 2500, 3000, 1800]
    })
    
    plot_donut_chart(
        data=df_donut,
        title="Global Energy Mix",
        subtitle="Projected generation in 2030 (TWh)",
        center_label="10,000\nTWh",
        output_path=os.path.join(output_dir, "donut_basic.png")
    )
    
    plot_donut_chart(
        data=df_donut,
        title="Global Energy Mix",
        subtitle="Percentage distribution of projected generation in 2030",
        center_label="100%",
        show_percentages=True,
        output_path=os.path.join(output_dir, "donut_percentages.png")
    )

def generate_grouped():
    print("Generating grouped bar charts...")
    df_grouped = pd.DataFrame({
        'Region': ['North America', 'Europe', 'Asia Pacific'],
        '2023': [12.5, 8.2, 15.4],
        '2024': [14.0, 9.1, 16.8]
    })
    plot_grouped_barh_chart(
        data=df_grouped,
        title="Annual Revenue by Region",
        subtitle="In millions of USD",
        value_suffix="M",
        output_path=os.path.join(output_dir, "grouped_barh_basic.png")
    )

def generate_stacked():
    print("Generating stacked bar charts...")
    df_stacked = pd.DataFrame({
        'Cohort': ['Q1', 'Q2', 'Q3', 'Q4'],
        'Enterprise': [120, 135, 142, 150],
        'Mid-Market': [300, 310, 315, 325],
        'SMB': [500, 480, 460, 490]
    })
    plot_stacked_bar_chart(
        data=df_stacked,
        title="Customer Distribution by Segment",
        subtitle="Absolute number of active customers per cohort",
        output_path=os.path.join(output_dir, "stacked_bar_basic.png")
    )
    
    plot_stacked_bar_chart(
        data=df_stacked,
        title="Customer Distribution by Segment",
        subtitle="Percentage of active customers per cohort",
        show_percentages=True,
        output_path=os.path.join(output_dir, "stacked_bar_pct.png")
    )

if __name__ == "__main__":
    generate_bar_charts()
    generate_time_series()
    generate_donut()
    generate_grouped()
    generate_stacked()
    print("Done!")
