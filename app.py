import streamlit as st
from dashboard import show_dashboard
from forecast import show_forecast
from about import show_about

# App Settings
st.set_page_config(page_title="🚖 Uber Forecasting App", layout="wide")

st.sidebar.title("⚙️ App Settings")
theme = st.sidebar.radio("Select Theme Mode", ["Light", "Dark"])

# Simulate theme switching
if theme == "Dark":
    st.markdown("<style>body { background-color: #0e1117; color: white; }</style>", unsafe_allow_html=True)

# Navigation Buttons
st.sidebar.title("🔍 Navigate Pages")
page = st.sidebar.radio("Go to", ["Dashboard", "Forecast", "About"])

# Route to corresponding page
if page == "Dashboard":
    show_dashboard()
elif page == "Forecast":
    show_forecast()
elif page == "About":
    show_about()

# Footer
st.markdown("---")
st.markdown("<center><sub>2025 © Pranav The King</sub></center>", unsafe_allow_html=True)
