import streamlit as st  # ✅ FIXED: Missing import
import xgboost as xgb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import numpy as np

@st.cache_resource
def train_xgboost_model(df):
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)
    df = df.resample("D").sum()

    df["target"] = df["trips"]
    df = df.dropna()

    df["dayofweek"] = df.index.dayofweek
    df["month"] = df.index.month
    df["day"] = df.index.day

    X = df[["dayofweek", "month", "day"]]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)

    model = xgb.XGBRegressor(n_estimators=100)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    error = mean_absolute_error(y_test, y_pred)

    return model, error

def forecast_future(model, periods):
    future_dates = pd.date_range(start=pd.Timestamp.today(), periods=periods)

    df_future = pd.DataFrame({
        "dayofweek": future_dates.dayofweek,
        "month": future_dates.month,
        "day": future_dates.day
    })

    forecast = model.predict(df_future)
    result = pd.DataFrame({"Date": future_dates, "Forecasted Trips": forecast})
    return result
