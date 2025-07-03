import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("Uber-Jan-Feb-FOIL.csv")
    df['Date/Time'] = pd.to_datetime(df['Date/Time'], errors='coerce')
    df = df.dropna(subset=['Date/Time'])
    df['Date'] = df['Date/Time'].dt.date
    daily_data = df.groupby('Date').size().reset_index(name='Trips')
    daily_data['Date'] = pd.to_datetime(daily_data['Date'])
    return daily_data
