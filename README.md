# 🚖 Uber Trips Forecasting with XGBoost

A stylish and interactive Streamlit-based web application for **time series forecasting** of Uber trip data using powerful **XGBoost** models with lag-based features. Whether you're analyzing ride demand, vehicle usage, or trip patterns, this app enables smart forecasting with ease and visual clarity.

---

## 🔍 Features

- 🎨 **Modern UI**: Responsive, theme-switchable interface with light/dark mode and gradient visuals.
- 📅 **Flexible Input**: Select your own date/time and trip count columns from uploaded datasets.
- ⏱️ **Lag Feature Tuning**: Adjust the lag window size to tune the model's memory of past values.
- 📈 **Live Forecasting**: Generate and visualize actual vs predicted trip volumes interactively.
- 📊 **Time Series Summary**: Quick overview of time trends using beautiful plots and charts.
- 🚀 **One-Click Forecast**: Just upload, select, and hit "Run Forecast" for instant results.

---

## 🧠 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend Model**: [XGBoost](https://xgboost.readthedocs.io/)
- **Visualization**: Plotly, Matplotlib
- **Data Handling**: Pandas, Numpy

---

## 📂 How to Use

```bash
# 1. Clone the repo
git clone https://github.com/kambojipranav/Uber_Forecast_App.git
cd Uber_Forecast_App

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py

## Output After Training for some time looks like :

