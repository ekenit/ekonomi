# Database Module
import sqlite3


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

