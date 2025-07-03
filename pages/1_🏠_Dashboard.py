import streamlit as st
from data_loader import load_data
import plotly.express as px

st.set_page_config(page_title="📈 Dashboard")

st.title("📊 Uber Daily Trips Overview")

df = load_data()

st.subheader("Daily Trip Count")
fig = px.line(df, x='Date', y='Trips', title='Uber Daily Trips - Jan & Feb')
st.plotly_chart(fig, use_container_width=True)

st.dataframe(df.tail(10), use_container_width=True)
