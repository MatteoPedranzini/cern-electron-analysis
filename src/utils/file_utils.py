# src/utils/file_utils.py
import os
import pandas as pd

def get_project_root():
    """Get the absolute path to the project root directory."""
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def ensure_directory_exists(path):
    """Create directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)
    return path

def read_data(file_path, **kwargs):
    """Read data file with automatic format detection."""
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path, **kwargs)
    elif file_path.endswith('.parquet'):
        return pd.read_parquet(file_path, **kwargs)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")