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
    column_names = ["Datum", "Transaktionskod", "", "Belopp"]

    for col in column_names:
        table.add_column(col)

    for row in data:
        cleaned_row = [str(row[i] or 'N/A') for i in range(len(column_names))]
        table.add_row(*cleaned_row)

    console = Console()
    console.print(table)


def display_db_with_rich(title, data, column_headers):
    """
    Displays database query results in a table format using the rich library.

    :param title: Title of the table.
    :param data: Data to be displayed (list of tuples).
    :param column_headers: List of column headers for the table.
    """
    table = Table(title=title)
    for header in column_headers:
        table.add_column(header, justify="center")

    for row in data:
        formatted_row = [str(item) for item in row]
        table.add_row(*formatted_row)

    console = Console()
    console.print(table)

def display_economic_trend(results):
    column_headers = ["Month", "Total Income", "Total Expense", "Total Savings"]
    display_db_with_rich("Economic Trend per Month", results, column_headers)


def display_most_common_expenses(results):
    column_headers = ["Purchase Place", "Number of Transactions", "Total Amount"]
    display_db_with_rich("Most Common Expenses", results, column_headers)
