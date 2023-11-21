# Main Application
import typer
from file_processing import *
from data_analysis import *
from visualization import *
from database import *
from machine_learning import *
from utils import *

#app = typer.Typer()

#@app.command()
def main():
    filepath = 'expenses'
    total_df = process_bank_files(filepath)

    total_df = consolidate_entries(total_df, expenses_mapping)
    handle_database(total_df, 'database.db')


    #aggregated_ammount = aggregate_by_month(total_df)
    #display_data_with_rich("Månadsvis Sammanställning", aggregated_ammount)

    #income, savings, expenses = segment_financial_data(total_df)

    #display_data_with_rich("Inkomster", income)
    #display_data_with_rich("Utgifter", expenses)
    #display_data_with_rich("Sparande", savings)

    #future_flows = extrapolate_future(total_df)
    #display_data_with_rich("Framtida flöden", future_flows)
    regression_flows = linear_regression_forecast(total_df)
    pass


if __name__ == "__main__":
    main()
