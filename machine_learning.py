
import pandas as pd
import numpy as np
from visualization import plot_time_series
from sklearn.linear_model import LinearRegression

def linjar_regression_prognos(df):
    # Code for linear regression and predictive modeling...
    pass

def extrapolate_future(df, number_of_months=12):
    df['Månad'] = df['Transaktionsdatum'].dt.to_period('M')
    monthly_sum = df.groupby('Månad')['Belopp'].sum()

    average_change = monthly_sum.diff().mean()

    last_month = monthly_sum.index.max()
    future_months = pd.period_range(start=last_month, periods=number_of_months + 1, freq='M')[1:]
    forecasts = [monthly_sum[-1] + average_change * i for i in range(1, number_of_months + 1)]
    future_flow = pd.DataFrame({'Månad': future_months, 'Forecast': forecasts})

    historical_dates = monthly_sum.index.to_timestamp()
    forecast_dates = future_months.to_timestamp()
    plot_time_series(historical_dates, monthly_sum, forecast_dates, forecasts, 
                     'Historical Data and Future Economic Flows', 'Month', 'Amount')

    return future_flow


def linear_regression_forecast(df, number_of_months=12):
    df['Månad'] = df['Transaktionsdatum'].dt.to_period('M')
    df = df.groupby('Månad')['Belopp'].sum().reset_index()
    df['Månad'] = df['Månad'].dt.to_timestamp()

    X = np.array(range(len(df))).reshape(-1, 1)
    y = df['Belopp'].values

    model = LinearRegression().fit(X, y)
    future_months = pd.date_range(df['Månad'].max(), periods=number_of_months + 1, freq='M')[1:]
    X_future = np.array(range(len(df), len(df) + number_of_months)).reshape(-1, 1)
    forecasts = model.predict(X_future)

    # Display model details
    print(f"Model coefficient: {model.coef_[0]}")
    print(f"Intercept: {model.intercept_}")
    print(f"R² value: {model.score(X, y)}")

    # Call to the new visualization function
    historical_dates = df['Månad']
    forecast_dates = future_months
    plot_time_series(historical_dates, y, forecast_dates, forecasts,
                     'Linear Regression Forecast', 'Månad', 'Belopp')

    return pd.DataFrame({'Månad': future_months, 'Forecast': forecasts})