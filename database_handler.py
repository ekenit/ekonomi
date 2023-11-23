# Database Module
import sqlite3
from visualization import display_db_with_rich

def handle_database(transactions_df, db_file_path):
    """
    Handles database operations for transaction data.

    :param transactions_df: DataFrame containing transaction data.
    :param db_file_path: Path to the database file.
    """
    if 'Månad' in transactions_df.columns:
        transactions_df['Månad'] = transactions_df['Månad'].astype(str)

    conn = sqlite3.connect(db_file_path)
    transactions_df.to_sql('transaktioner', conn, if_exists='replace', index=False)
    cursor = conn.cursor()
    rows = cursor.fetchall()
    conn.close()


def consolidate_entries(df, lookup_dict):
    """
    Consolidates entries in a DataFrame based on a lookup dictionary.

    :param df: Pandas DataFrame to be updated.
    :param lookup_dict: Dictionary where keys are existing names and values are new names.
    """
    for existing_name, new_name in lookup_dict.items():
        df.loc[df['Inköpsställe'] == existing_name, 'Inköpsställe'] = new_name
    return df


def create_database_connection():
    return sqlite3.connect('database.db')



def execute_sql_query(query, parameters=()):
    """
    Executes a SQL query and returns the results.

    :param query: The SQL query to execute.
    :param parameters: Optional parameters for the query.
    :return: Query results as a list of tuples.
    """
    conn = create_database_connection()  # Assuming this function is already defined
    cursor = conn.cursor()
    cursor.execute(query, parameters)
    results = cursor.fetchall()
    conn.close()
    return results

#def show_expense_analysis(purchase_place: str):
#    query = """
#    SELECT 
#        strftime('%w', Transaktionsdatum) AS Weekday, 
#        strftime('%H', Transaktionsdatum) AS Hour, 
#        COUNT(*) AS NumberOfTransactions
#    FROM 
#        transaktioner
#    WHERE 
#        Inköpsställe = ?
#    GROUP BY 
#        Weekday, Hour
#    ORDER BY 
#        NumberOfTransactions DESC
#    """
#    results = execute_sql_query(query, (purchase_place,))
#    return results
    
#def show_expense_analysis(purchase_place: str):
#    query = """
#    SELECT 
#        strftime('%w', Transaktionsdatum) AS Weekday, 
#        strftime('%m', Transaktionsdatum) AS Month,
#        strftime('%W', Transaktionsdatum) AS Week,
#        COUNT(*) AS NumberOfTransactions
#    FROM 
#        transaktioner
#    WHERE 
#        Inköpsställe = ?
#    GROUP BY 
#        Weekday, Month, Week
#    ORDER BY 
#        NumberOfTransactions DESC
#    """
#    results = execute_sql_query(query, (purchase_place,))
#    return results
    


def show_expense_analysis(purchase_place: str):
    # Analyze by Weekday
    weekday_query = """
    SELECT 
        strftime('%w', Transaktionsdatum) AS Weekday,
        COUNT(*) AS NumberOfTransactions,
        SUM(Belopp) AS TotalCost
    FROM 
        transaktioner
    WHERE 
        Inköpsställe = ?
    GROUP BY 
        Weekday
    ORDER BY 
        NumberOfTransactions DESC
    """
    weekday_results = execute_sql_query(weekday_query, (purchase_place,))
    weekday_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    formatted_weekday_results = [(weekday_names[int(row[0])], row[1], f"{row[2]:,.2f} kr") for row in weekday_results]
    display_db_with_rich(f"Most Common Weekdays for {purchase_place}", 
                         formatted_weekday_results, 
                         ["Weekday", "Number of Transactions", "Total Cost"])

    # Analyze by Week
    week_query = """
    SELECT 
        strftime('%W', Transaktionsdatum) AS Week,
        COUNT(*) AS NumberOfTransactions,
        SUM(Belopp) AS TotalCost
    FROM 
        transaktioner
    WHERE 
        Inköpsställe = ?
    GROUP BY 
        Week
    ORDER BY 
        NumberOfTransactions DESC
    """
    week_results = execute_sql_query(week_query, (purchase_place,))
    formatted_week_results = [("Week " + row[0], row[1], f"{row[2]:,.2f} kr") for row in week_results]
    display_db_with_rich(f"Most Common Weeks for {purchase_place}", 
                         formatted_week_results, 
                         ["Week", "Number of Transactions", "Total Cost"])

    # Analyze by Month
    month_query = """
    SELECT 
        strftime('%m', Transaktionsdatum) AS Month,
        COUNT(*) AS NumberOfTransactions,
        SUM(Belopp) AS TotalCost
    FROM 
        transaktioner
    WHERE 
        Inköpsställe = ?
    GROUP BY 
        Month
    ORDER BY 
        NumberOfTransactions DESC
    """
    month_results = execute_sql_query(month_query, (purchase_place,))
    formatted_month_results = [(row[0], row[1], f"{row[2]:,.2f} kr") for row in month_results]
    display_db_with_rich(f"Most Common Months for {purchase_place}", 
                         formatted_month_results, 
                         ["Month", "Number of Transactions", "Total Cost"])
