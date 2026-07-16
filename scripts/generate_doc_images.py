import sys
import os
import pandas as pd

# Add localforge to path to import clean_charts
current_dir = os.path.dirname(os.path.abspath(__file__))
localforge_dir = os.path.abspath(os.path.join(current_dir, "../../../localforge"))
sys.path.insert(0, localforge_dir)

from clean_charts import (
    plot_barh_chart,
    plot_time_series,
    plot_donut_chart,
    plot_grouped_barh_chart,
    plot_stacked_bar_chart
)

output_dir = os.path.abspath(os.path.join(current_dir, "../images/docs"))

def generate_bar_charts():
    print("Generating bar charts...")
    # 1. Survey Use Case (Custom Padding)
    df_survey = pd.DataFrame({
        'Question': ['I am proud to work here', 'I would recommend this company', 'My manager supports me', 'I have opportunities to grow'],
        'Score': [85, 82, 78, 65]
    }).sort_values('Score', ascending=True)
    
    plot_barh_chart(
        data=df_survey,
        title="Employee Engagement Survey",
        subtitle="% of employees agreeing with the statement",
        value_suffix="%",
        bar_padding=0.4,
        output_path=os.path.join(output_dir, "barh_survey.png")
    )

    # 2. Compact Aspect Ratio (1:1)
    df_health = pd.DataFrame({
        'Country': ['Japan', 'Switzerland', 'South Korea', 'Singapore', 'Spain'],
        'Life Expectancy': [84.6, 83.8, 83.6, 83.6, 83.3]
    })
    
    plot_barh_chart(
        data=df_health,
        title="Global Longevity Leaders",
        subtitle="Life expectancy at birth (years)",
        value_suffix=" yrs",
        aspect_ratio="1:1",
        output_path=os.path.join(output_dir, "barh_compact.png")
    )

def generate_time_series():
    print("Generating time series charts...")
    dates = pd.date_range(start='2023-01-01', periods=12, freq='ME')
    
    # 1. SaaS Metrics
    df_saas = pd.DataFrame({
        'date': dates,
        'Enterprise': [120, 135, 142, 150, 165, 178, 190, 205, 215, 230, 245, 260],
        'Mid-Market': [300, 310, 315, 325, 330, 345, 355, 360, 380, 395, 410, 420]
    })
    plot_time_series(
        data=df_saas,
        title="ARR Growth by Segment",
        subtitle="Monthly recurring revenue ($M)",
        output_path=os.path.join(output_dir, "ts_saas.png")
    )

    # 2. Macro Trends
    df_macro = pd.DataFrame({
        'date': dates,
        'Inflation': [6.5, 6.0, 5.0, 4.9, 4.0, 3.0, 3.2, 3.7, 3.7, 3.2, 3.1, 3.4],
        'Target Rate': [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
    })
    plot_time_series(
        data=df_macro,
        title="US Inflation vs Target",
        subtitle="CPI YoY % vs Federal Reserve Target",
        output_path=os.path.join(output_dir, "ts_macro.png")
    )

def generate_donut():
    print("Generating donut charts...")
    # 1. Energy Mix
    df_energy = pd.DataFrame({
        'Source': ['Solar', 'Wind', 'Nuclear', 'Natural Gas', 'Coal'],
        'TWh': [1200, 1500, 2500, 3000, 1800]
    })
    plot_donut_chart(
        data=df_energy,
        title="Global Energy Mix",
        subtitle="Projected generation in 2030 (TWh)",
        center_label="10,000\nTWh",
        output_path=os.path.join(output_dir, "donut_energy.png")
    )
    
    # 2. Portfolio
    df_portfolio = pd.DataFrame({
        'Asset': ['Equities', 'Fixed Income', 'Real Estate', 'Cash'],
        'Alloc': [60, 25, 10, 5]
    })
    plot_donut_chart(
        data=df_portfolio,
        title="Portfolio Allocation",
        subtitle="Balanced growth strategy",
        center_label="100%",
        value_suffix="%",
        output_path=os.path.join(output_dir, "donut_portfolio.png")
    )

def generate_grouped():
    print("Generating grouped bar charts...")
    df_fin = pd.DataFrame({
        'Region': ['North America', 'Europe', 'Asia Pacific'],
        'Q1': [12.5, 8.2, 15.4],
        'Q2': [14.0, 9.1, 16.8]
    })
    plot_grouped_barh_chart(
        data=df_fin,
        title="Quarterly Revenue by Region",
        subtitle="In millions of USD",
        value_suffix="M",
        output_path=os.path.join(output_dir, "grouped_finance.png")
    )

def generate_stacked():
    print("Generating stacked bar charts...")
    df_churn = pd.DataFrame({
        'Cohort': ['Q1 2023', 'Q2 2023', 'Q3 2023'],
        'Retained': [85, 88, 92],
        'Churned': [15, 12, 8]
    })
    plot_stacked_bar_chart(
        data=df_churn,
        title="Customer Retention by Cohort",
        subtitle="Percentage of retained vs churned users after 6 months",
        value_suffix="%",
        output_path=os.path.join(output_dir, "stacked_churn.png")
    )

if __name__ == "__main__":
    generate_bar_charts()
    generate_time_series()
    generate_donut()
    generate_grouped()
    generate_stacked()
    print("Done!")
