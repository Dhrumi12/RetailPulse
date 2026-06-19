import streamlit as st
import pandas as pd
import plotly.express as px

st.title("RetailPulse Dashboard")

sales = pd.read_csv("sales_dashboard.csv")
forecast = pd.read_csv("forecast_dashboard.csv")
customers = pd.read_csv("customer_dashboard.csv")

st.header("Revenue Metrics")

st.metric(
    "Total Revenue",
    f"${sales['Revenue'].sum():,.2f}"
)

st.metric(
    "Average Daily Revenue",
    f"${sales['Revenue'].mean():,.2f}"
)

st.header("Daily Revenue")

fig = px.line(
    sales,
    x="InvoiceDate",
    y="Revenue",
    title="Daily Revenue"
)

st.plotly_chart(fig)

st.header("Customer Segments")

if "Cluster" in customers.columns:
    st.bar_chart(
        customers["Cluster"].value_counts()
    )