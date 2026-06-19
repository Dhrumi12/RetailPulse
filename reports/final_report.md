# RetailPulse Retail Analytics Project

## Project Overview

RetailPulse is an end-to-end retail analytics solution developed using Python.

The project includes:

- Customer Segmentation
- Revenue Forecasting
- Churn Prediction
- Interactive Dashboard

---

## Dataset

Online Retail Dataset

Transactions:
- 500,000+ records
- Customers from multiple countries

---

## Customer Segmentation

RFM Analysis was used:

- Recency
- Frequency
- Monetary

K-Means clustering generated customer groups.

---

## Revenue Forecasting

Facebook Prophet model was trained on daily revenue.

Forecast Horizon:
- 30 Days

---

## Churn Prediction

A churn label was created using:

DaysSinceLastPurchase > 90

Model:
- Random Forest Classifier

Features:
- Recency
- Frequency
- Monetary

---

## Dashboard

Streamlit dashboard provides:

- Revenue KPIs
- Daily Revenue Trend
- Customer Segments
- Forecast Visualization

---

## Results

Total Revenue:
$8.27M

Average Daily Revenue:
$27.14K

Customers:
4372

---

## Technologies

- Python
- Pandas
- NumPy
- Scikit-Learn
- Prophet
- SHAP
- Streamlit