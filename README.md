# Stock Prediction

## Overview
This project focuses on analyzing and predicting stock prices using technical indicators such as Simple Moving Averages (SMA), Relative Strength Index (RSI), and other metrics. The project utilizes the `pandas-ta` library for technical analysis and `yfinance` to fetch historical stock data for 10 companies over a 5-year period. The final dataset is prepared and stored in a CSV file for further analysis and visualization.

## Features
- Fetch historical stock data for 10 companies using the `yfinance` library.
- Perform technical analysis with indicators like SMA, RSI etc using `pandas-ta`.
- Visualize stock prices and technical indicators using `matplotlib`.
- Combine data into a single dataset and save it as a CSV file for future analysis.
- Analyze stock trends to aid in investment decisions.


## Installation

### Prerequisites
- Python 3.7 or higher
- Jupyter Notebook

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/aritro98/Stock-Analysis-using-Python.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Stock-Analysis-using-Python
   ```
3. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Open the Jupyter Notebook:
   ```bash
   jupyter notebook Stock_Prediction.ipynb
   ```
2. Run the notebook cells step-by-step to fetch data, calculate technical indicators, and visualize results.

## Technical Indicators
- Simple Moving Average (SMA): Smooths price data to identify trends.
- Relative Strength Index (RSI): Identifies overbought or oversold conditions.

## Additional Details
- Historical data is fetched for a 5-year period, covering multiple market conditions.
- The database includes company information and technical indicators to aid in comprehensive analysis.
