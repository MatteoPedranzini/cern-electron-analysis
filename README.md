# CERN Electron Analysis

# Analysis and Visualization of CERN Electron Collision Data



## Project Overview

This project analyzes electron collision data from CERN to identify patterns and distributions. It involves data cleaning, exploratory data analysis (EDA) in Python, visualization in Tableau, and optional regression modeling.



## Project Structure

```
cern-electron-analysis/
├── data/                 # Data management
│   ├── raw/              # Unprocessed datasets (original CSV files)
│   └── processed/        # Cleaned and transformed data
├── notebooks/            # Jupyter notebooks for analysis
│   ├── Cern_Initial_Analysis.ipynb          # Initial exploration
│   ├── Cern_Modular_Analysis.ipynb          # Modular approach implementation  
│   └── Cern_Modular_Analysis-with-config.ipynb  # Config system integration
├── src/                  # Source code
│   ├── data/             # Data processing modules
│   │   └── clean_data.py # Data cleaning and preparation
│   │   └── clean_data_legacy.py # Legacy version (for reference)
│   ├── utils/            # Utility functions
│   │   ├── config_loader.py     # Configuration management
│   │   ├── file_utils.py        # File I/O operations
│   │   ├── stats_utils.py       # Statistical functions
│   │   ├── validation_utils.py  # Data validation
│   │   └── logger.py            # Logging configuration
│   └── visualization/    # Visualization modules
│       ├── plot_utils.py        # Plotting functions
│       └── plot_utils_legacy.py # Legacy version (for reference)
├── tests/                # Unit tests (future development)
├── config/               # Configuration files
│   └── config.yaml       # Project settings and parameters
├── reports/              # Outputs and deliverables
│   ├── figures/          # Generated plots and visualizations
│   └── *.twb            # Tableau workbooks
├── .gitignore           # Git ignore rules
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

**Key Features:**
- **Modular Design**: Separated data, utils, and visualization code
- **Config-Driven**: Centralized configuration in config.yaml
- **Versioned**: Source code tracked in Git, data excluded
- **Reproducible**: requirements.txt ensures consistent environment
- **Documented**: Multiple notebook versions show evolution

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/MatteoPedranzini/cern-electron-analysis.git

2. Install required Python packages: `pip install -r requirements.txt`

3. Place the raw dataset `dielectron.csv` in the `data/raw/` directory.



## Usage

- Run the Jupyter Notebook in `notebooks/` for data cleaning and analysis.

- Open the Tableau workbook in `reports/` for interactive visualizations.

## Dataset
The project uses the "CERN Electron Collision Data" available on Kaggle, which contains 100,000 dielectron events in the invariant mass range of 2-110 GeV.

## Technologies Used
- Python (pandas, numpy, matplotlib, seaborn, scikit-learn)

- Jupyter Notebook

- Tableau

- Git & GitHub

## License
This project is for educational purposes as part of data science learning.



