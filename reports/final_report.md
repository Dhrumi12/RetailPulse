# RetailPulse AI Retail Analytics Platform

## Dataset

Online Retail Dataset

Total Transactions: 401,604

---

## Data Cleaning

- Removed missing CustomerID
- Removed missing Description
- Removed duplicate records
- Created Revenue column

---

## Exploratory Data Analysis

### Findings

- Revenue increases towards the end of the year
- Strong sales growth from September-November
- Some customers generate significantly higher revenue

---

## RFM Analysis

Features:

- Recency
- Frequency
- Monetary Value

Insights:

- Identified high-value customers
- Identified inactive customers

---

## Customer Segmentation

Algorithms Used:

- KMeans
- DBSCAN

Insights:

- Loyal customers
- Regular customers
- Low-value customers

---

## Time Series Analysis

Prepared daily sales data

Observed:

- Seasonal patterns
- Revenue growth trend

---

## Prophet Forecasting

Created baseline demand forecast

Findings:

- Revenue expected to continue growing
- Seasonal fluctuations observed

---

## LSTM Forecasting

Deep learning forecasting model built using PyTorch

Model Saved:

models/lstm_model.pth

---

## Conclusion

RetailPulse successfully performs:

- Data Cleaning
- Customer Segmentation
- Revenue Forecasting
- Business Analytics

Future Improvements:

- Real-time dashboard
- Inventory forecasting
- Recommendation engine