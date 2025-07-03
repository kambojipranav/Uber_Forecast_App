import streamlit as st
from data_loader import load_data
from utils import train_xgboost_model, forecast_future
import plotly.graph_objects as go

st.set_page_config(page_title="📉 Forecast", layout="wide")

st.title("📉 Forecast Future Uber Trips")

# Load data
df = load_data()

# Show raw data toggle
with st.expander("🔍 Preview Raw Data"):
    st.dataframe(df.head())

# Display model training status
st.info("📊 Training XGBoost model on historical trip data...")

model, error = train_xgboost_model(df)

st.success(f"✅ Model trained successfully! MAE: {error:.2f} trips")

# User input for forecasting
n_days = st.slider("📆 Select number of future days to forecast:", min_value=1, max_value=30, value=7)

# Forecast future trips
forecast_df = forecast_future(model, n_days)

# Plot the forecast
fig = go.Figure()
fig.add_trace(go.Scatter(x=forecast_df["Date"], y=forecast_df["Forecasted Trips"],
                         mode='lines+markers', name='Forecasted Trips'))
fig.update_layout(title="📈 Forecasted Uber Trips", xaxis_title="Date", yaxis_title="Trips")

st.plotly_chart(fig, use_container_width=True)

# Show forecast table
with st.expander("📄 Forecast Data"):
    st.dataframe(forecast_df)

# Download forecast CSV
csv = forecast_df.to_csv(index=False).encode('utf-8')
st.download_button("📥 Download Forecast", data=csv, file_name='forecast.csv', mime='text/csv')
