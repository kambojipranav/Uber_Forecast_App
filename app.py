import streamlit as st

st.set_page_config(
    page_title="🚖 Uber Forecasting App (Multi-Page)",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Theme toggle
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

with st.sidebar:
    st.title("🚖 Uber Forecasting App")
    st.markdown("Navigate using the sidebar — Dashboard, Forecasting, About")

    toggle = st.checkbox("🌗 Dark Mode", value=st.session_state.dark_mode)
    if toggle != st.session_state.dark_mode:
        st.session_state.dark_mode = toggle
        st.rerun()  # ✅ FIXED: Previously st.experimental_rerun()

# Optional: apply custom dark/light theme here using markdown CSS (optional improvement)
