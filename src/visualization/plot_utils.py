# File: src/visualization/plot_utils.py
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from utils.config_loader import load_config, get_visualization_config

# Load config once when module is imported
config = load_config()
viz_config = get_visualization_config(config)

def set_plot_style():
    """
    Sets a consistent style for all plots based on config.
    """
    # First, get the style name from the config and store it in a variable
    style_to_use = viz_config.get('style', 'seaborn-v0_8-deep')
    
    # Second, use that variable to set the style
    plt.style.use(style_to_use)
    
    # Set palette
    sns.set_palette(viz_config.get('palette_name', 'deep'))
    
    # Set rcParams from config
    rc_params = {
        'figure.figsize': viz_config.get('figure_size', [10, 6]),
        'font.size': viz_config.get('font_size', 12),
        'axes.labelsize': viz_config.get('label_size', 12),
        'axes.titlesize': viz_config.get('title_size', 14),
        'xtick.labelsize': viz_config.get('tick_size', 10),
        'ytick.labelsize': viz_config.get('tick_size', 10),
        'axes.grid': viz_config.get('grid_visible', True)
    }
    
    plt.rcParams.update(rc_params)
    
    # Finally, print the style name that was used. This is much more informative.
    print(f"Plot style set to: {style_to_use}")

def save_plot(name):
    """
    Save plot to file based on config settings.
    """
    # Use the path from your config
    figures_path = config['paths']['reports']['figures']
    
    # Create the directory if it doesn't exist
    os.makedirs(figures_path, exist_ok=True)
    
    format = viz_config.get('figure_format', 'png')
    dpi = viz_config.get('dpi', 300)
    
    # Create the full file path
    filename = os.path.join(figures_path, f"{name}.{format}")
    
    plt.savefig(filename, dpi=dpi, bbox_inches='tight', format=format)
    print(f"Plot saved to: {filename}")
    
    # Verify the file was actually created
    if os.path.exists(filename):
        print(f"✓ File successfully created: {os.path.basename(filename)}")
    else:
        print(f"✗ Error: File was not created at {filename}")

def _handle_standalone_plot(fig, title):
    """Internal helper to manage saving and showing standalone plots."""
    plt.tight_layout()
    if viz_config.get('save_figures', False):
        # Create a safe filename from the title
        filename = title.replace(' ', '_').lower().strip()
        save_plot(filename)
    if viz_config.get('show_figures', True):
        plt.show()
    else:
        plt.close(fig) # Close the figure to free memory if not showing

def save_subplot(name, fig=None):
    """
    Save the current active figure or a specific figure to file.
    
    Parameters:
    name (str): Name for the file
    fig (matplotlib.figure.Figure): Specific figure to save (optional)
    """
    if viz_config.get('save_figures', False):
        # Use the provided figure or get the current active figure
        if fig is None:
            fig = plt.gcf()  # Get current figure
        
        figures_path = "../reports/figures/"
        format = viz_config.get('figure_format', 'png')
        dpi = viz_config.get('dpi', 300)
        
        filename = f"{figures_path}{name}.{format}"
        fig.savefig(filename, dpi=dpi, bbox_inches='tight', format=format)
        print(f"Subplot saved to: {filename}")

def plot_histogram(data, column, bins=None, xlabel='', title='', kde=True, ax=None, **kwargs):
    """
    Creates a histogram for a specified column using config settings.
    """
    # Flag to check if we need to handle showing/saving the plot
    is_standalone = ax is None
    
    if is_standalone:
        fig, ax = plt.subplots(figsize=viz_config.get('figure_size', [10, 6]))
    else:
        fig = ax.get_figure()

    if bins is None:
        bins = viz_config.get('histogram_bins', 50)
    
    color = viz_config.get('colors', ['#1f77b4'])[0]
    
    sns.histplot(data[column], bins=bins, kde=kde, ax=ax, color=color, **kwargs)
    ax.set_title(title, fontsize=viz_config.get('title_size', 14))
    ax.set_xlabel(xlabel, fontsize=viz_config.get('label_size', 12))
    ax.set_ylabel('Frequency', fontsize=viz_config.get('label_size', 12))
    
    if is_standalone:
        _handle_standalone_plot(fig, title)

def plot_scatter(data, x_col, y_col, xlabel='', ylabel='', title='', alpha=0.6, ax=None, **kwargs):
    """
    Creates a scatter plot between two variables using config settings.
    """
    is_standalone = ax is None
    
    if is_standalone:
        fig, ax = plt.subplots(figsize=viz_config.get('figure_size', [10, 6]))
    else:
        fig = ax.get_figure()

    color = viz_config.get('colors', ['#1f77b4'])[0]
    
    sns.scatterplot(x=data[x_col], y=data[y_col], alpha=alpha, ax=ax, color=color, **kwargs)
    ax.set_title(title, fontsize=viz_config.get('title_size', 14))
    ax.set_xlabel(xlabel, fontsize=viz_config.get('label_size', 12))
    ax.set_ylabel(ylabel, fontsize=viz_config.get('label_size', 12))
    
    if is_standalone:
        _handle_standalone_plot(fig, title)

# --- Functions ported from the old code, adapted to the new style ---

def plot_correlation_matrix(data, columns=None, title='Correlation Matrix', **kwargs):
    """
    Creates a heatmap of the correlation matrix using config settings.
    """
    if columns is None:
        columns = data.select_dtypes(include=[np.number]).columns
        
    fig, ax = plt.subplots(figsize=viz_config.get('heatmap_size', [12, 8]))
    
    correlation_matrix = data[columns].corr()
    
    cmap = viz_config.get('cmap', 'coolwarm')
    
    sns.heatmap(correlation_matrix, annot=True, cmap=cmap, fmt='.2f', 
                center=0, square=True, ax=ax, **kwargs)
    ax.set_title(title, fontsize=viz_config.get('title_size', 14))
    
    _handle_standalone_plot(fig, title)

def plot_pairplot(data, columns=None, hue=None, title='Pairplot', sample_size=None):
    """
    Creates a pairplot for multiple variables.

    Parameters:
    data (pandas.DataFrame): The DataFrame containing the data
    columns (list): List of columns to include in pairplot
    hue (str): Column name for color encoding
    title (str): Title for the plot
    sample_size (int): Number of samples to use (for large datasets)
    """
    # Create a sample if requested (for large datasets)
    plot_data = data
    if sample_size and len(data) > sample_size:
        plot_data = data.sample(n=sample_size, random_state=42)
        print(f"Using sample of {sample_size} points for pairplot")
    
    if columns is None:
        # Get numeric columns for the pairplot
        numeric_cols = plot_data.select_dtypes(include=[np.number]).columns.tolist()
        columns = numeric_cols[:5]  # Limit to first 5 numeric columns
    
    # Prepare the data for pairplot - include hue column if specified
    plot_columns = columns.copy()
    if hue and hue not in plot_columns:
        plot_columns.append(hue)
    
    # Create the pairplot - NO sample_size parameter here!
    plot = sns.pairplot(plot_data[plot_columns], hue=hue, diag_kind='hist')
    plot.fig.suptitle(title, y=1.02)
    
    if viz_config.get('save_figures', False):
        save_plot(f"pairplot_{title.replace(' ', '_').lower()}")
    
    plt.show()

# Set the style automatically when module is imported for convenience
set_plot_style()