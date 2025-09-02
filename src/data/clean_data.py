# File: src/data/clean_data.py
import pandas as pd

def load_and_clean_data(raw_data_path):
    """
    Loads the raw CERN electron collision data from a CSV, cleans it, and returns a DataFrame.
    Replicates the steps from the original Jupyter notebook.

    Parameters:
    raw_data_path (str): Path to the raw 'dielectron.csv' file.

    Returns:
    pandas.DataFrame: The cleaned DataFrame ready for analysis.
    """

    # Load the dataset 
    df = pd.read_csv(raw_data_path)

    # Display initial info 
    print("Dataset loaded successfully.")
    print(f"Initial shape: {df.shape}")
    print("\nInitial info:")
    print(df.info())
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nSummary statistics:")
    print(df.describe())

    # Check for missing values (Notebook Cell 4)
    print("\nChecking for missing values:")
    missing_values = df.isnull().sum()
    print(missing_values)

    # Handle missing values by dropping rows (Notebook Cell 5)
    initial_count = len(df)
    df = df.dropna()
    rows_dropped = initial_count - len(df)
    print(f"\nDropped {rows_dropped} rows with missing values.")
    print(f"New shape: {df.shape}")

    # Check for duplicates (Notebook Cell 6)
    duplicates = df.duplicated().sum()
    print(f"\nNumber of duplicate rows: {duplicates}")
    # Based on your notebook, no need to drop duplicates as count was 0

    # Display cleaned dataset info (Notebook Cell 7)
    print("\nCleaned dataset info:")
    print(df.info())
    print("\nFirst 5 rows of cleaned data:")
    print(df.head())

    return df

# This block allows for testing the script directly
if __name__ == "__main__":
    # Test the function
    print("Testing clean_data.py...")
    cleaned_df = load_and_clean_data('C:/Users/matte/Documents/Git folders/cern-electron-analysis/data/raw/dielectron.csv')
    print("\nTest completed successfully!")