# Data Analysis Module
import pandas as pd
import numpy as np
from database_handler import create_database_connection



def calculate_average_change(df):
    """ Calculates and returns the average change in amount over time. """
    # Create a new column for month and year
    df['Månad_År'] = df['Transaktionsdatum'].dt.to_period('M')

    # Group by month and year and sum the amounts
    monthly_sum = df.groupby('Månad_År')['Belopp'].sum()

    # Calculate monthly changes
    monthly_changes = monthly_sum.diff()

    # Calculate and return average change
    average_change = monthly_changes.mean()
    return average_change


def aggregate_by_month(df):
    df['Månad'] = df['Transaktionsdatum'].dt.to_period('M')
    monthly_sum = df.groupby('Månad')['Belopp'].sum().reset_index()
    return monthly_sum


def segment_data(df):
    # Define conditions for savings
    savings_conditions = (
        df['Inköpsställe'].str.startswith('ISK', na=False) |
        df['Inköpsställe'].str.startswith('Buffer', na=False) |
        df['Inköpsställe'].str.startswith('spar', na=False)
    )
    
    # Filter to get savings and expense data
    savings_df = df[savings_conditions]
    expenses_df = df[~savings_conditions & (df['Belopp'] < 0)]

    return expenses_df, savings_df


def segment_financial_data(df):
    income_criteria = ['LÖN', 'ELSTÖD', 'BARNBDR', 'ÅTERBET. IF']
    savings_criteria = ['ISK', 'Buffert', 'Spar']

    income_df = df[df['Inköpsställe'].str.contains('|'.join(income_criteria), na=False)]
    savings_df = df[df['Inköpsställe'].str.startswith(tuple(savings_criteria), na=False)]
    expenses_df = df[~df.index.isin(income_df.index) & ~df.index.isin(savings_df.index) & (df['Belopp'] < 0)]

    savings_df['Belopp'] = savings_df['Belopp'].abs()

    return income_df, savings_df, expenses_df

def aggregera_per_manad(df):
    # Code for aggregating data per month...
    pass

def segmentera_data(df):
    # Code for segmenting data into savings and expenses...
    pass


def calculate_economic_trend():
    conn = create_database_connection()
    cursor = conn.cursor()

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
    
    cursor.execute(query)
    results = cursor.fetchall()

    conn.close()
    return results

def calculate_most_common_expenses(number: int = 10):
    conn = create_database_connection()
    cursor = conn.cursor()

    query = """
    SELECT 
        Inköpsställe, COUNT(*) as Antal_Transaktioner, SUM(Belopp) as Totalt_Belopp
    FROM 
        transaktioner 
    WHERE 
        Belopp < 0
    GROUP BY 
        Inköpsställe
    ORDER BY 
        Antal_Transaktioner DESC, Totalt_Belopp ASC
    LIMIT ?
    """
    
    cursor.execute(query, (number,))
    results = cursor.fetchall()

    conn.close()
    return results