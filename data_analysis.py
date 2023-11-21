# Data Analysis Module
import pandas as pd
import numpy as np

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

# Other related functions...
