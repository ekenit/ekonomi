# Main Application
import typer
from file_processing import *
from data_analysis import *
from visualization import *
from database_handler import *
from machine_learning import *
from utils import *

app = typer.Typer()

@app.command()
def show_most_common_expenses(number: int = typer.Option(500, help="Number of top expenses to show")):
    results = calculate_most_common_expenses(number)
    display_most_common_expenses(results)

@app.command()
def show_economic_trend():
    results = calculate_economic_trend()
    display_economic_trend(results)

@app.command()
def show_largest_transactions(type: str = typer.Argument(..., help="Specify 'income' or 'expenses'"), 
                              number: int = typer.Option(50, help="Number of transactions to show")):
    conn = create_database_connection()
    cursor = conn.cursor()
    
    if type == 'income':
        query = "SELECT * FROM transaktioner WHERE Belopp > 0 ORDER BY Belopp DESC LIMIT ?"
    elif type == 'expenses':
        query = "SELECT * FROM transaktioner WHERE Belopp < 0 ORDER BY Belopp ASC LIMIT ?"
    else:
        typer.echo("Invalid type. Specify either 'income' or 'expenses'.")
        raise typer.Exit()

    cursor.execute(query, (number,))
    results = cursor.fetchall()
    display_database_with_rich(f"Top {number} {type}", results)
    
    conn.close()

#@app.command()
def main():
    filepath = 'expenses'
    total_df = process_bank_files(filepath)

    total_df = consolidate_entries(total_df, expenses_mapping)
    handle_database(total_df, 'database.db')
    app()

    #aggregated_ammount = aggregate_by_month(total_df)
    #display_data_with_rich("Månadsvis Sammanställning", aggregated_ammount)

    #income, savings, expenses = segment_financial_data(total_df)

    #display_data_with_rich("Inkomster", income)
    #display_data_with_rich("Utgifter", expenses)
    #display_data_with_rich("Sparande", savings)

    #future_flows = extrapolate_future(total_df)
    #display_data_with_rich("Framtida flöden", future_flows)
    #regression_flows = linear_regression_forecast(total_df)

    pass


if __name__ == "__main__":
    main()
