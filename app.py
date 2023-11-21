# Main Application
import typer
from file_processing import *
from data_analysis import *
from visualization import *
from database import *
from machine_learning import *
from utils import *

app = typer.Typer()

@app.command()
def main_command():
    filepath = 'expenses'
    total_df = process_bank_files(filepath)

    total_df = consolidate_entries(total_df, expenses_mapping)
    handle_database(total_df, 'database.db')

    pass


if __name__ == "__main__":
    app()
