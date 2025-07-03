import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error
import streamlit as st


@st.cache_resource
def train_xgboost_model(df, target_column='trips'):
    df = df.copy()
    df['day_of_week'] = df['date'].dt.dayofweek
    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year

    features = ['day', 'month', 'year', 'day_of_week', 'active_vehicles']
    X = df[features]
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = xgb.XGBRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mape = mean_absolute_percentage_error(y_test, preds)

    return model, features, mape

@st.cache_data
def forecast_future(model, last_date, periods, features):
    future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=periods)
    future_df = pd.DataFrame({
        'date': future_dates,
        'day': future_dates.day,
        'month': future_dates.month,
        'year': future_dates.year,
        'day_of_week': future_dates.dayofweek,
        'active_vehicles': [1000] * periods  # default/assumed input
    })

    future_X = future_df[features]
    predictions = model.predict(future_X)
    future_df['predicted_trips'] = predictions

    return future_df
