# File: src/visualization/plot_utils.py
import matplotlib.pyplot as plt
import seaborn as sns

def set_plot_style():
    """
    Sets a consistent style for all plots.
    """
    plt.style.use('default')
    sns.set_palette("deep")
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10

def plot_histogram(data, column, bins=50, xlabel='', title='', kde=True, ax=None):
    """
    Creates a histogram for a specified column.

    Parameters:
    data (pandas.DataFrame): The DataFrame containing the data
    column (str): The name of the column to plot
    bins (int): Number of bins for the histogram
    xlabel (str): Label for the x-axis
    title (str): Title for the plot
    kde (bool): Whether to show kernel density estimate
    ax (matplotlib.axes.Axes): Axes object to plot on (for subplots)
    """
    if ax is None:
        plt.figure(figsize=(10, 6))
        ax = plt.gca()
    
    sns.histplot(data[column], bins=bins, kde=kde, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel('Frequency')
    
    if ax is None:
        plt.tight_layout()
        plt.show()

def plot_scatter(data, x_col, y_col, xlabel='', ylabel='', title='', alpha=0.6, ax=None):
    """
    Creates a scatter plot between two variables.

    Parameters:
    data (pandas.DataFrame): The DataFrame containing the data
    x_col (str): The name of the column for x-axis
    y_col (str): The name of the column for y-axis
    xlabel (str): Label for the x-axis
    ylabel (str): Label for the y-axis
    title (str): Title for the plot
    alpha (float): Transparency level for points
    ax (matplotlib.axes.Axes): Axes object to plot on (for subplots)
    """
    if ax is None:
        plt.figure(figsize=(10, 6))
        ax = plt.gca()
    
    sns.scatterplot(x=data[x_col], y=data[y_col], alpha=alpha, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    if ax is None:
        plt.tight_layout()
        plt.show()

def plot_correlation_matrix(data, columns=None, title='Correlation Matrix'):
    """
    Creates a heatmap of the correlation matrix.

    Parameters:
    data (pandas.DataFrame): The DataFrame containing the data
    columns (list): List of columns to include in correlation matrix
    title (str): Title for the plot
    """
    if columns is None:
        columns = data.select_dtypes(include=[np.number]).columns
    
    plt.figure(figsize=(12, 8))
    correlation_matrix = data[columns].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', 
                center=0, square=True)
    plt.title(title)
    plt.tight_layout()
    plt.show()

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
    plot_data = data.copy()
    if sample_size and len(data) > sample_size:
        plot_data = data.sample(n=sample_size, random_state=42)
    
    if columns is None:
        # Get numeric columns for the pairplot
        numeric_cols = plot_data.select_dtypes(include=[np.number]).columns.tolist()
        columns = numeric_cols[:5]  # Limit to first 5 numeric columns
    
    # Prepare the data for pairplot - include hue column if specified
    plot_columns = columns.copy()
    if hue and hue not in plot_columns:
        plot_columns.append(hue)
    
    # Create the pairplot
    plot = sns.pairplot(plot_data[plot_columns], hue=hue, diag_kind='hist')
    plot.fig.suptitle(title, y=1.02)
    plt.show()

# Example usage (will only run if script is executed directly)
if __name__ == "__main__":
    print("This is a utility module for plotting functions.")
    print("Import these functions in your notebook using:")
    print("from visualization.plot_utils import *")