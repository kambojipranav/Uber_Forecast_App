import streamlit as st
import os

st.set_page_config(page_title="🚖 Uber Forecasting App", layout="wide")

# Add theme toggle
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

theme_option = st.selectbox("Choose Theme", ['light', 'dark'], index=0 if st.session_state.theme == 'light' else 1)

# Save selected theme to config file
if theme_option != st.session_state.theme:
    st.session_state.theme = theme_option
    theme_content = f"""
[theme]
base="{theme_option}"
primaryColor="#1E90FF"
backgroundColor="{ '#FFFFFF' if theme_option == 'light' else '#0E1117' }"
secondaryBackgroundColor="{ '#F5F5F5' if theme_option == 'light' else '#262730' }"
textColor="{ '#000000' if theme_option == 'light' else '#FAFAFA' }"
font="sans serif"
"""
    os.makedirs(".streamlit", exist_ok=True)
    with open(".streamlit/config.toml", "w") as f:
        f.write(theme_content)

    st.experimental_rerun()

st.title("🚖 Uber Forecasting App")
st.markdown("Navigate using the sidebar — Dashboard, Forecasting, About.")
