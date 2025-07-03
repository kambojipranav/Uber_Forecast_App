import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    url = "Uber-Jan-Feb-FOIL.csv"
    df = pd.read_csv(url)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df[['date', 'trips']].dropna()
    df = df.groupby('date').sum().resample('H').sum()
    df['trips'] = pd.to_numeric(df['trips'], errors='coerce').fillna(0)
    return df
