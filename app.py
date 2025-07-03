import streamlit as st
from utils import set_custom_theme

st.set_page_config(page_title="🚖 Uber Forecast App", layout="wide")

st.sidebar.title("⚙️ App Settings")
theme_mode = st.sidebar.radio("Select Theme Mode", ["Light", "Dark"])
set_custom_theme(theme_mode.lower())

st.sidebar.markdown("---")
st.sidebar.info("Navigate pages via sidebar 👈")

st.markdown("""
    <h1 style='text-align:center;'>📊 Uber Forecasting App (Multi-Page)</h1>
    <p style='text-align:center;'>Navigate using the sidebar — Dashboard, Forecasting, About</p>
""", unsafe_allow_html=True)
