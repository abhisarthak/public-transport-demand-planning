import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Multimodal Transport Decision Intelligence",
    page_icon="🚌",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🚌 Multimodal Transport Decision Intelligence Dashboard")

st.markdown("""
This dashboard integrates demand forecasting, fleet planning,
network resilience analysis, and Monte Carlo risk simulation
for the **Kharagpur–Kolkata transport corridor**.
""")


# --------------------------------------------------
# DATA PATH
# --------------------------------------------------

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "dashboard"


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data(filename):
    return pd.read_csv(DATA_PATH / filename)


forecast_df = load_data("forecast_performance.csv")
fleet_df = load_data("fleet_expansion.csv")
vulnerability_df = load_data("festival_vulnerability.csv")
marginal_df = load_data("marginal_bus_analysis.csv")
monte_carlo_df = load_data("monte_carlo_summary.csv")
resilience_df = load_data("resilience_matrix.csv")
recommendation_df = load_data("management_recommendation.csv")


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Select Analysis",
    [
        "Overview",
        "Demand Forecasting",
        "Fleet Optimization",
        "Festival Vulnerability",
        "Marginal Bus Analysis",
        "Network Resilience",
        "Monte Carlo Risk",
        "Management Recommendations"
    ]
)


# --------------------------------------------------
# OVERVIEW
# --------------------------------------------------

if section == "Overview":

    st.header("Decision Intelligence Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Forecast Records",
        len(forecast_df)
    )

    col2.metric(
        "Fleet Scenarios",
        len(fleet_df)
    )

    col3.metric(
        "Risk Simulations",
        len(monte_carlo_df)
    )

    st.subheader("Decision Intelligence Pipeline")

    st.markdown("""
    **Passenger Demand Data**  
    ↓  
    **Demand Forecasting**  
    ↓  
    **Capacity & Unmet Demand Analysis**  
    ↓  
    **Festival Vulnerability Identification**  
    ↓  
    **Fleet Expansion Optimization**  
    ↓  
    **Network Resilience Stress Testing**  
    ↓  
    **Monte Carlo Risk Analysis**  
    ↓  
    **Management Recommendations**
    """)

    st.info(
        "Use the navigation panel to explore each analytical component."
    )


# --------------------------------------------------
# DEMAND FORECASTING
# --------------------------------------------------

elif section == "Demand Forecasting":

    st.header("📈 Demand Forecasting Performance")

    st.dataframe(forecast_df, use_container_width=True)

    st.subheader("Forecast Performance")

    st.bar_chart(
        forecast_df.set_index(forecast_df.columns[0])
    )


# --------------------------------------------------
# FLEET OPTIMIZATION
# --------------------------------------------------

elif section == "Fleet Optimization":

    st.header("🚌 Fleet Expansion Optimization")

    st.dataframe(fleet_df, use_container_width=True)

    st.bar_chart(
        fleet_df.set_index(fleet_df.columns[0])
    )


# --------------------------------------------------
# FESTIVAL VULNERABILITY
# --------------------------------------------------

elif section == "Festival Vulnerability":

    st.header("⚠️ Festival Vulnerability Analysis")

    st.dataframe(vulnerability_df, use_container_width=True)


# --------------------------------------------------
# MARGINAL BUS ANALYSIS
# --------------------------------------------------

elif section == "Marginal Bus Analysis":

    st.header("📊 Marginal Bus Analysis")

    st.dataframe(marginal_df, use_container_width=True)


# --------------------------------------------------
# NETWORK RESILIENCE
# --------------------------------------------------

elif section == "Network Resilience":

    st.header("🌐 Network Resilience Analysis")

    st.dataframe(resilience_df, use_container_width=True)


# --------------------------------------------------
# MONTE CARLO RISK
# --------------------------------------------------

elif section == "Monte Carlo Risk":

    st.header("🎲 Monte Carlo Risk Analysis")

    st.dataframe(monte_carlo_df, use_container_width=True)


# --------------------------------------------------
# MANAGEMENT RECOMMENDATIONS
# --------------------------------------------------

elif section == "Management Recommendations":

    st.header("🎯 Management Recommendations")

    st.dataframe(recommendation_df, use_container_width=True)

    st.success(
        "The recommendations combine forecasting, optimization, "
        "resilience, and risk analysis into actionable decisions."
    )
