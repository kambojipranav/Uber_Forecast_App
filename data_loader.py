import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("Uber-Jan-Feb-FOIL.csv")
    df.rename(columns=lambda x: x.strip().lower(), inplace=True)

    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df.dropna(subset=['date'], inplace=True)
    else:
        st.error("Missing 'date' column in uploaded data.")
        return pd.DataFrame()

    return df
