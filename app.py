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
def show_most_common_expenses(number: int = typer.Option(10, help="Number of top expenses to show")):
    query = """
    SELECT 
        Inköpsställe, COUNT(*) as Antal_Transaktioner, SUM(Belopp) as Total_Belopp
    FROM 
        transaktioner 
    WHERE 
        Belopp < 0
    GROUP BY 
        Inköpsställe
    ORDER BY 
        Antal_Transaktioner DESC, Total_Belopp ASC
    LIMIT ?
    """
    results = execute_sql_query(query, (number,))
    display_db_with_rich("Most Common Expenses", results, ["Purchase Place", "Number of Transactions", "Total Amount"])


@app.command()
def show_economic_trend():
    query = """
    SELECT 
        strftime('%Y-%m', Transaktionsdatum) AS Månad, 
        SUM(CASE WHEN Belopp > 0 THEN Belopp ELSE 0 END) AS Total_Inkomst,
        SUM(CASE WHEN Belopp < 0 THEN Belopp ELSE 0 END) AS Total_Utgift,
        SUM(CASE WHEN Inköpsställe LIKE 'ISK%' OR Inköpsställe LIKE 'Buffert%' OR Inköpsställe LIKE 'spar%' THEN Belopp ELSE 0 END) AS Total_Sparande
    FROM 
        transaktioner 
    GROUP BY 
        Månad
    ORDER BY 
        Månad
    """
    results = execute_sql_query(query)
    display_db_with_rich("Economic Trend per Month", results, ["Month", "Total Income", "Total Expense", "Total Savings"])

@app.command()
def show_most_common_expenses(number: int = typer.Option(500, help="Number of top expenses to show")):
    results = calculate_most_common_expenses(number)
    display_most_common_expenses(results)

@app.command()
def show_economic_trend():
    results = calculate_economic_trend()
    display_economic_trend(results)


@app.command()
def show_future_flows():
    results = extrapolate_future(total_df)


@app.command()
def show_regression_flows():
    results = linear_regression_forecast(total_df)

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
