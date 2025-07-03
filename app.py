import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="🚖 Uber Forecasting App (Multi-Page)", layout="wide")

# Theme toggle using session state
if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

st.sidebar.header("⚙️ App Settings")
st.sidebar.radio("Select Theme Mode", ["Light", "Dark"], key="theme")

# Display
st.markdown(
    f"""
    <div style="text-align: center; padding-top: 100px;">
        <h1 style="font-size: 3em;">📊 Uber Forecasting App (Multi-Page)</h1>
        <p style="font-size: 1.2em;">Navigate using the sidebar — <b>Dashboard</b>, <b>Forecasting</b>, <b>About</b></p>
    </div>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.markdown("---")
    st.info("Navigate pages via sidebar 👈")

st.markdown(
    "<div style='position: fixed; bottom: 20px; width: 100%; text-align: center;'>"
    "2025 © Pranav The King</div>",
    unsafe_allow_html=True
)
