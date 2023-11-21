# Visualization Module
import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table


def presentera_data_med_rich(title, data):
    # Code for presenting data with rich...
    pass

def plot_data(data):
    # Code for plotting data using matplotlib...
    pass

import matplotlib.pyplot as plt

def plot_time_series(historical_dates, historical_data, forecast_dates, forecast_data, title, xlabel, ylabel):
    """
    Plots time series data including historical data and forecasts.

    :param historical_dates: Dates for the historical data.
    :param historical_data: Historical data points.
    :param forecast_dates: Dates for the forecast data.
    :param forecast_data: Forecast data points.
    :param title: Title of the plot.
    :param xlabel: Label for the x-axis.
    :param ylabel: Label for the y-axis.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(historical_dates, historical_data, label='Historical Data')
    plt.plot(forecast_dates, forecast_data, label='Forecast', linestyle='--')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()



def display_data_with_rich(title, data):
    """
    Displays a pandas DataFrame using the rich library's table format.

    :param title: Title of the table.
    :param data: Pandas DataFrame to be displayed.
    """
    table = Table(title=title)
    for col in data.columns:
        table.add_column(col)
    for row in data.itertuples():
        row_data = [str(getattr(row, col, '')) for col in data.columns]
        table.add_row(*row_data)

    console = Console()
    console.print(table)


def display_database_with_rich(title, data):
    """
    Displays database data using the rich library's table format.

    :param title: Title of the table.
    :param data: List of tuples representing database rows.
    """
    table = Table(title=title)
    column_names = ["Date", "TransactionCode", "", "Amount"]

    for col in column_names:
        table.add_column(col)

    for row in data:
        cleaned_row = [str(row[i] or 'N/A') for i in range(len(column_names))]
        table.add_row(*cleaned_row)

    console = Console()
    console.print(table)