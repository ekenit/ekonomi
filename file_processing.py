# File Processing Module
import os
import glob
import pandas as pd

def identify_bank(file_path):
    """Identifies the bank associated with an Excel file."""
    # Read only the first row (header) from the Excel file
    try:
        df = pd.read_excel(file_path, sheet_name=0, header=None, nrows=1)
    except Exception as e:
        print(f"Could not read the file: {file_path}. Error: {e}")
        return "Unknown"

    # Check the content in the first cell (A1)
    first_cell = df.iloc[0, 0]
    if isinstance(first_cell, str):
        if "Handelsbanken" in first_cell:
            return "Handelsbanken"
        elif "Export från internetbanken för privatpersoner" in first_cell:
            return "SEB"
    return "Unknown"


def read_seb_excel_file(file_path):
    """Reads and processes an SEB Excel file."""
    df = pd.read_excel(file_path, sheet_name=0)

    # Identify the starting point for the actual transaction data
    start_row = None
    for i, row in df.iterrows():
        if 'Bokförd' in row.values:  # 'Bokförd' means 'Booked' or 'Recorded'
            start_row = i
            break

    df = pd.read_excel(file_path, sheet_name=0, skiprows=start_row)
    df.columns = df.iloc[0]
    df = df[1:]
    df.reset_index(drop=True, inplace=True)

    # Check order and map column names
    df.rename(columns={
        'Valutadatum': 'Transaktionsdatum',
        'Text': 'Inköpsställe',
        'Belopp': 'Belopp',
        'Bokförd': 'Bokföringsdatum'
    }, inplace=True)

    # Add missing columns and remove unwanted ones
    missing_columns = ['Ort', 'Valuta', 'Valutakurs', 'Utl. belopp', 'Kortinnehavare']
    for column in missing_columns:
        df[column] = None
    df = df[['Transaktionsdatum', 'Inköpsställe', 'Belopp', 'Bokföringsdatum'] + missing_columns]
    df['Inköpsställe'] = df['Inköpsställe'].str.replace(r'/\d{2}-\d{2}-\d{2}', '', regex=True).str.strip()

    # Convert data types
    df['Transaktionsdatum'] = pd.to_datetime(df['Transaktionsdatum'], errors='coerce')
    df['Belopp'] = pd.to_numeric(df['Belopp'], errors='coerce')

    return df


def read_excel_file(file_path):
    """Reads and processes a single Excel file."""
    df = pd.read_excel(file_path, sheet_name=0)

    # Identify the starting point for the actual transaction data
    start_row = None
    for i, row in df.iterrows():
        if 'Transaktionsdatum' in row.values:  # 'Transaktionsdatum' means 'Transaction Date'
            start_row = i
            break

    df = pd.read_excel(file_path, sheet_name=0, skiprows=start_row)
    df.columns = df.iloc[0]  # Set the first row as column names
    df = df[1:]  # Remove the now redundant first row
    df.reset_index(drop=True, inplace=True)

    # Convert data types
    df['Belopp'] = pd.to_numeric(df['Belopp'], errors='coerce')
    df['Transaktionsdatum'] = pd.to_datetime(df['Transaktionsdatum'], errors='coerce')

    return df


def process_bank_files(folder_path):
    """Processes all bank files in a given folder."""
    combined_df = pd.DataFrame()
    file_list = glob.glob(os.path.join(folder_path, '*.xlsx'))
    for file in file_list:
        bank = identify_bank(file)
        if bank == "Handelsbanken":
            processed_df = read_excel_file(file)  # Your existing function for Handelsbanken
        elif bank == "SEB":
            processed_df = read_seb_excel_file(file)  # Your existing function for SEB
        else:
            print(f"Unknown bank for the file: {file}")
            continue
        combined_df = combined_df.append(processed_df, ignore_index=True)
    return combined_df



