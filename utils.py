from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import pandas as pd
import numpy as np

def prepare_features(df):
    df = df.copy()
    df['dayofweek'] = df['Date'].dt.dayofweek
    df['day'] = df['Date'].dt.day
    df['month'] = df['Date'].dt.month
    df['year'] = df['Date'].dt.year
    return df

def train_xgboost_model(df):
    df = prepare_features(df)
    X = df[['dayofweek', 'day', 'month', 'year']]
    y = df['Trips']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = XGBRegressor(n_estimators=100)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return model, mae, r2, X_test, y_test, y_pred

def forecast_future(model, days, base_date):
    future_dates = pd.date_range(base_date + pd.Timedelta(days=1), periods=days)
    df_future = pd.DataFrame({
        'Date': future_dates,
        'dayofweek': future_dates.dayofweek,
        'day': future_dates.day,
        'month': future_dates.month,
        'year': future_dates.year
    })
    X_future = df_future[['dayofweek', 'day', 'month', 'year']]
    predictions = model.predict(X_future)
    df_future['Forecast'] = predictions.astype(int)
    return df_future
