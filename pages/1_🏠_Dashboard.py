import streamlit as st
from data_loader import load_data
import plotly.express as px

st.set_page_config(page_title="📊 Dashboard", layout="wide")
st.title("📊 Uber Trip Dashboard")

df = load_data()

if not df.empty:
    st.subheader("Trips over Time")
    fig = px.line(df, x='date', y='trips', title='Trips Over Time')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Active Vehicles vs Trips")
    fig2 = px.scatter(df, x='active_vehicles', y='trips', color='dispatching_base_number', title='Active Vehicles vs Trips')
    st.plotly_chart(fig2, use_container_width=True)
