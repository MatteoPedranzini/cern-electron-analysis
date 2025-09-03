# src/utils/config_loader.py
import yaml
import os

def load_config(config_path=None):
    """
    Load configuration from YAML file.
    If no path provided, uses default relative to THIS file's location.
    """
    if config_path is None:
        # Get the directory of THIS file (config_loader.py)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Go from src/utils/ to config/ correctly
        config_path = os.path.join(current_dir, '..', '..', 'config', 'config.yaml')
        config_path = os.path.normpath(config_path)  # Clean up the path
    
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def get_data_paths(config):
    """
    Extract data paths from configuration.
    
    Parameters:
    config (dict): Configuration dictionary
    
    Returns:
    tuple: (raw_data_path, processed_data_path, output_path)
    """
    paths = config['paths']['data']
    return paths['raw'], paths['processed'], paths['output']

# Example usage
if __name__ == "__main__":
    config = load_config()
    print("Configuration loaded successfully!")
    print("Raw data path:", config['paths']['data']['raw'])