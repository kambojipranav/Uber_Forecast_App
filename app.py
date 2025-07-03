import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="🚖 Uber Forecasting App", layout="wide")

# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# -----------------------------
# SIDEBAR SETTINGS
# -----------------------------
st.sidebar.markdown("## 🛠️ App Settings")
toggle = st.sidebar.checkbox("🌗 Dark Mode", value=st.session_state.theme == "dark")
st.session_state.theme = "dark" if toggle else "light"

# -----------------------------
# THEME-BASED BACKGROUND
# -----------------------------
dark_bg = """
    <style>
        body {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        }
    </style>
"""

light_bg = """
    <style>
        body {
            background: linear-gradient(135deg, #E0F7FA, #F1F8E9);
        }
    </style>
"""

st.markdown(dark_bg if st.session_state.theme == "dark" else light_bg, unsafe_allow_html=True)

# -----------------------------
# CENTERED TITLE AND TEXT
# -----------------------------
st.markdown("""
    <style>
        .centered {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-top: 10%;
            text-align: center;
        }
        .title {
            font-size: 3rem;
            font-weight: bold;
            background: -webkit-linear-gradient(45deg, #42A5F5, #AB47BC);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }
        .subtitle {
            font-size: 1.2rem;
            color: #ffffffcc;
        }
        .footer {
            position: fixed;
            bottom: 15px;
            width: 100%;
            text-align: center;
            font-size: 0.85rem;
            color: #cccccc;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# MAIN CONTENT
# -----------------------------
st.markdown('<div class="centered">', unsafe_allow_html=True)
st.markdown('<div class="title">🚖 Uber Forecasting App</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Navigate using the sidebar — Dashboard | Forecast | About</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown('<div class="footer">2025 © Pranav The King</div>', unsafe_allow_html=True)
