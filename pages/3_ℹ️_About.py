import streamlit as st

st.set_page_config(page_title="ℹ️ About", layout="centered")
st.title("ℹ️ About this App")

st.markdown("""
### 🚖 Uber Trip Forecasting App

This Streamlit app uses historical Uber trip data to forecast future trip volumes using XGBoost. 

**Key Features:**
- Dashboard with interactive visualizations
- XGBoost-based time series forecasting
- Downloadable forecast results
- Clean UI with multi-page navigation

Built with ❤️ using Python, Streamlit, and XGBoost.
""")
