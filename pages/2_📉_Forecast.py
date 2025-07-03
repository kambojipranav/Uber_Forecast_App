import streamlit as st
from data_loader import load_data
from utils import train_xgboost_model, forecast_future
import plotly.graph_objects as go

st.set_page_config(page_title="🔮 Forecasting")

st.title("🔮 Forecast Future Uber Trips")

df = load_data()
model, mae, r2, X_test, y_test, y_pred = train_xgboost_model(df)

st.subheader("📈 Model Performance")
st.metric("Mean Absolute Error", f"{mae:.2f}")
st.metric("R² Score", f"{r2:.2f}")

# Forecasting
st.subheader("📆 Forecast into Future")
days = st.slider("Select days to forecast:", 1, 30, 7)
base_date = df['Date'].max()
forecast_df = forecast_future(model, days, base_date)

# Plotting
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Date'], y=df['Trips'], mode='lines', name='Actual'))
fig.add_trace(go.Scatter(x=forecast_df['Date'], y=forecast_df['Forecast'], mode='lines+markers', name='Forecast'))

fig.update_layout(title='Uber Trips Forecast', xaxis_title='Date', yaxis_title='Trips')
st.plotly_chart(fig, use_container_width=True)

st.dataframe(forecast_df, use_container_width=True)
