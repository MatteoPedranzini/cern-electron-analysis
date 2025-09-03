# CERN Electron Analysis

# Analysis and Visualization of CERN Electron Collision Data



## Project Overview

This project analyzes electron collision data from CERN to identify patterns and distributions. It involves data cleaning, exploratory data analysis (EDA) in Python, visualization in Tableau, and optional regression modeling.



## Project Structure

```
cern-electron-analysis/
├── data/
│   ├── raw/              # Unprocessed datasets
│   └── processed/        # Cleaned data
├── notebooks/            # Jupyter notebooks for exploration and analysis
├── src/
│   ├── data/             # Data handling and preprocessing
│   └── visualization/    # Visualization scripts
├── tests/                # Unit tests 
├── config/               # Configuration files   
├── reports/              # Contains Tableau workbook and final reports
├── .gitignore           # Tells Git which files to ignore
├── requirements.txt     # Python package dependencies
└── README.md            # This file
```

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



