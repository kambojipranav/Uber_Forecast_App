import streamlit as st
from data_loader import load_data
from utils import train_xgboost_model, forecast_future
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="📉 Forecasting", layout="wide")
st.title("📉 Uber Trip Forecasting")

df = load_data()

if not df.empty:
    model, features, mape = train_xgboost_model(df)

    st.success(f"Model trained! MAPE: {mape:.2f}")

    forecast_days = st.slider("Select number of future days to forecast:", min_value=1, max_value=30, value=7)

    if st.button("Run Forecast"):
        last_date = df['date'].max()
        future_df = forecast_future(model, last_date, forecast_days, features)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['date'], y=df['trips'], mode='lines+markers', name='Actual Trips'))
        fig.add_trace(go.Scatter(x=future_df['date'], y=future_df['predicted_trips'], mode='lines+markers', name='Forecasted Trips'))
        fig.update_layout(title="Actual vs Forecasted Trips", xaxis_title="Date", yaxis_title="Trips")
        st.plotly_chart(fig, use_container_width=True)

        csv = future_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Forecast", csv, "forecast.csv", "text/csv", key='download-forecast')
