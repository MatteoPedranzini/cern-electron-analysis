# File: src/data/clean_data.py
import pandas as pd
import sys
import os

# Add the src directory to the path so we can import our config loader
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.config_loader import load_config, get_data_paths

def load_and_clean_data():
    """
    Loads the raw CERN electron collision data from a CSV, cleans it, and returns a DataFrame.
    Uses configuration from config.yaml for paths and cleaning parameters.

    Returns:
    pandas.DataFrame: The cleaned DataFrame ready for analysis.
    dict: Configuration dictionary
    """

    # Load configuration
    config = load_config()
    raw_data_path, processed_data_path, output_path = get_data_paths(config)
    
    # Load the dataset 
    df = pd.read_csv(raw_data_path)

    # Rename the 'px1 ' column to fix the error
    df = df.rename(columns={'px1 ': 'px1'})

    # Display initial info 
    print("Dataset loaded successfully.")
    print(f"Initial shape: {df.shape}")
    print(f"Data path: {raw_data_path}")

    # Check for missing values
    print("\nChecking for missing values:")
    missing_values = df.isnull().sum()
    print(missing_values)

    # Handle missing values based on config
    cleaning_config = config['data_cleaning']
    initial_count = len(df)
    
    if cleaning_config['missing_values'] == "drop":
        df = df.dropna()
        rows_dropped = initial_count - len(df)
        print(f"\nDropped {rows_dropped} rows with missing values.")
    elif cleaning_config['missing_values'] == "fill":
        # You could implement fill logic here if needed
        fill_value = cleaning_config.get('fill_value', 0)
        df = df.fillna(fill_value)
        print(f"\nFilled missing values with: {fill_value}")
    
    print(f"New shape: {df.shape}")

    # Check for duplicates
    duplicates = df.duplicated().sum()
    print(f"\nNumber of duplicate rows: {duplicates}")

    # Keep only specified columns from config
    columns_to_keep = cleaning_config['columns_to_keep']
    df = df[columns_to_keep]
    print(f"\nKeeping {len(columns_to_keep)} specified columns")
    print(f"Final shape: {df.shape}")

    # Display cleaned dataset info
    print("\nCleaned dataset info:")
    print(df.info())
    print("\nFirst 5 rows of cleaned data:")
    print(df.head())

    return df, config

# This block allows for testing the script directly
if __name__ == "__main__":
    # Test the function
    print("Testing clean_data.py with config...")
    cleaned_df, config = load_and_clean_data()
    print("\nTest completed successfully!")
    print(f"Used config: {config['data_cleaning']['missing_values']}")