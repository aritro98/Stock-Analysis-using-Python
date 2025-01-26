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

## Technologies Used
### Backend
- **Python Libraries:**
  - `pandas`: Data manipulation
  - `numpy`: Numerical computations
  - `matplotlib`: Data visualization
  - `scikit-learn`: Model training and evaluation
  - `yfinance`: Fetching stock data
  - `pandas-ta`: Technical analysis
  - `flask`: Backend framework for handling requests
  - `flask-CORS`: Enabling Cross-Origin Resource Sharing

### Frontend
- **Languages and Frameworks:**
  - HTML: Structure of web pages
  - CSS: Styling the user interface
  - JavaScript: Enhancing interactivity

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
### Backend
1. Run the backend application:
   ```bash
   python backend/app.py
   ```
2. Use the Jupyter Notebooks for training and prediction:
   - Open `Model_Training.ipynb` to train models.
   - Open `Stock_Prediction.ipynb` to generate predictions.

### Frontend
1. Open `Frontend.html` in a web browser.
2. Navigate through different pages to explore features like:
   - Market trends
   - Portfolio management
   - Stock predictions

## Additional Details
- Historical data is fetched for a 5-year period, covering multiple market conditions.
- The database includes company information and technical indicators to aid in comprehensive analysis.
- Includes functionality for real-time data fetching to provide up-to-date predictions.
- Implements cross-origin resource sharing (CORS) to enable smooth communication between backend and frontend.
- Designed with modularity, allowing easy updates and addition of new features or technical indicators.
- Offers robust error handling to manage data inconsistencies and API limitations effectively.
