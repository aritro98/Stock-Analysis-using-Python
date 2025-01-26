# Stock Prediction

## Overview
This project focuses on analyzing and predicting stock prices using technical indicators such as Simple Moving Averages (SMA), Relative Strength Index (RSI), and other metrics. It also includes a user-friendly frontend for visualization and interaction. Historical stock data is fetched for 10 companies over a 5-year period and analyzed to identify trends and make predictions.

## Features
### Backend
- **Data Acquisition:** Fetches historical stock data for analysis.
- **Model Training:** Includes a Jupyter Notebook (`Model_Training.ipynb`) for training predictive models.
- **Prediction:** Uses `Stock_Prediction.ipynb` for generating stock predictions based on trained models.

### Frontend
- **Interactive User Interface:**
  - `Frontend.html`: Main entry point for the web interface.
  - `index.html`: Landing page.
  - `market.html`: Displays market trends and stock details.
  - `order.html`: Facilitates stock purchase simulations.
  - `portfolio.html`: Displays user's portfolio details.
  - `settings.html`: Allows configuration of application settings.
  - `Stock_Prediction.html`: Shows prediction outputs in a user-friendly format.

### Data
- **Dataset:** Historical stock data is stored in `data/stock_data_5_years.csv`, which contains stock information over five years.
- **Technical Indicators:**
  - Simple Moving Average (SMA): Smooths price data to identify trends.
  - Relative Strength Index (RSI): Identifies overbought or oversold conditions.

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
