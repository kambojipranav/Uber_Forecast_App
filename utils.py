import streamlit as st
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_absolute_percentage_error, r2_score
from prophet import Prophet
from pmdarima import auto_arima

def set_custom_theme(theme="light"):
    if theme == "dark":
        bg_color = "#111"
        text_color = "#eaeaea"
        card_color = "#222"
        gradient = "linear-gradient(135deg, #1d2b64, #f8cdda)"
    else:
        bg_color = "#ffffff"
        text_color = "#222"
        card_color = "#ffffff"
        gradient = "linear-gradient(135deg, #f6d365, #fda085)"

    st.markdown(f"""
        <style>
        html, body, .stApp {{
            background: {gradient};
            color: {text_color};
        }}
        .main {{
            background-color: {card_color};
            border-radius: 12px;
            padding: 2rem;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
        }}
        footer {{ visibility: hidden; }}
        .footer-text {{
            position: fixed;
            bottom: 15px;
            left: 0;
            right: 0;
            text-align: center;
            font-size: 14px;
            color: {text_color};
            opacity: 0.7;
        }}
        </style>
        <div class="footer-text">2025 © Pranav The King</div>
    """, unsafe_allow_html=True)

def forecast_xgboost(series, window):
    X, y = [], []
    for i in range(len(series) - window):
        X.append(series[i:i + window])
        y.append(series[i + window])
    X, y = np.array(X), np.array(y)
    split = int(len(X) * 0.8)
    model = xgb.XGBRegressor(objective="reg:squarederror", n_estimators=150)
    model.fit(X[:split], y[:split])
    y_pred = model.predict(X[split:])
    return y[split:], y_pred, model

def forecast_arima(series):
    model = auto_arima(series, seasonal=True, suppress_warnings=True)
    n = int(len(series) * 0.2)
    forecast = model.predict(n_periods=n)
    return series[-n:], forecast, model

def forecast_prophet(df):
    df_p = df.reset_index().rename(columns={df.index.name or 'index': "ds", df.columns[0]: "y"})
    model = Prophet()
    model.fit(df_p)
    future = model.make_future_dataframe(periods=int(len(df)*0.2), freq="H")
    forecast = model.predict(future)
    y_true = df_p["y"].values[-int(len(df)*0.2):]
    y_pred = forecast["yhat"].values[-int(len(df)*0.2):]
    return y_true, y_pred, model

def evaluate(y_true, y_pred):
    return {
        "MAPE": mean_absolute_percentage_error(y_true, y_pred),
        "R2": r2_score(y_true, y_pred)
    }

def get_download_df(index, actual, predicted):
    return pd.DataFrame({"timestamp": index, "actual": actual, "predicted": predicted})
