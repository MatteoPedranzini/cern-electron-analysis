# src/utils/validation_utils.py
import pandas as pd

def validate_dataframe(df, expected_columns=None, min_rows=1):
    """Validate DataFrame structure and content."""
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    if len(df) < min_rows:
        raise ValueError(f"DataFrame must have at least {min_rows} rows")
    
    if expected_columns:
        missing_cols = set(expected_columns) - set(df.columns)
        if missing_cols:
            raise ValueError(f"Missing columns: {missing_cols}")
    
    return True

def check_missing_values(df, threshold=0.1):
    """Check for columns with excessive missing values."""
    missing_ratio = df.isnull().mean()
    problematic_cols = missing_ratio[missing_ratio > threshold]
    return problematic_cols