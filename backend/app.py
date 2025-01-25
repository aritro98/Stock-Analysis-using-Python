from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import pandas as pd
import pandas_ta as ta  # Importing pandas_ta for technical analysis
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Load CSV file
file_path = 'C:/Users/KIIT/Documents/Project/template/stock_data_5_years.csv'
try:
    data = pd.read_csv(file_path)
    print(data.head())
except Exception as e:
    print(f"Error reading the file: {e}")
# Clean data: strip columns and handle missing values
data.columns = data.columns.str.strip()
data = data.ffill()  # Forward fill for missing values

@app.route('/example')
def example():
    return "CORS-enabled response"

@app.route('/Dashboard')
def dashboard():
    return render_template('index.html')  # Ensure the correct template name

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/orders")
def orders():
    return render_template("orders.html")

@app.route("/market")
def market():
    return render_template("market.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/stocks", methods=["GET"])
def fetch_stocks():
    ticker = request.args.get('ticker')
    if not ticker:
        return jsonify({"error": "Ticker symbol is required"}), 400

    data = get_stock_data(ticker)
    if data is None:
        return jsonify({"error": "Stock not found"}), 404

    return jsonify(data)

# Function to retrieve stock data and calculate indicators using pandas_ta
def get_stock_data(ticker):
    filtered_data = data[data['Ticker'].str.upper() == ticker.upper()]
    
    if filtered_data.empty:
        return None  # Return None if no data found

    # Ensure data is sorted for accurate indicator calculations
    filtered_data = filtered_data.sort_values('Date')

    # Calculate technical indicators using pandas_ta
    filtered_data['SMA_50'] = ta.sma(filtered_data['Close'], length=50)
    filtered_data['SMA_200'] = ta.sma(filtered_data['Close'], length=200)
    filtered_data['RSI'] = ta.rsi(filtered_data['Close'], length=14)

    # Drop rows with NaN values caused by indicator calculation
    filtered_data.dropna(inplace=True)

    result = {
        "dates": filtered_data["Date"].tolist(),
        "prices": filtered_data["Close"].tolist(),
        "sma_50": filtered_data["SMA_50"].tolist(),
        "sma_200": filtered_data["SMA_200"].tolist(),
        "rsi": filtered_data["RSI"].tolist()
    }
    return result

# Prepare the data for regression (price prediction)
def prepare_regression_data(data):
    data['Date'] = pd.to_datetime(data['Date'])
    data['Timestamp'] = data['Date'].map(pd.Timestamp.timestamp)
    X = data[['Timestamp']].values
    y = data['Close'].values
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Train regression model
def train_regression_model(data):
    X_train, X_test, y_train, y_test = prepare_regression_data(data)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Prepare data for classification (Buy/Sell/Hold)
def prepare_classification_data(data):
    data['Target'] = np.where(data['Close'].pct_change() > 0.02, 1,  # Buy
                              np.where(data['Close'].pct_change() < -0.02, -1, 0))  # Sell / Hold
    data.dropna(inplace=True)
    features = data[['Open', 'High', 'Low', 'Volume']].values
    labels = data['Target'].values
    scaler = StandardScaler()
    features = scaler.fit_transform(features)
    return train_test_split(features, labels, test_size=0.2, random_state=42)

# Train classification model
def train_classification_model(data):
    X_train, X_test, y_train, y_test = prepare_classification_data(data)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    return clf

# Integrate models into API
@app.route('/predict', methods=['GET'])
def predict():
    ticker = request.args.get('ticker')
    if not ticker:
        return jsonify({"error": "Ticker symbol is required"}), 400
    
    # Filter data for the given ticker
    stock_data = data[data['Ticker'].str.upper() == ticker.upper()]
    if stock_data.empty:
        return jsonify({"error": "Stock not found"}), 404

    # Train and predict with models
    regression_model = train_regression_model(stock_data)
    classification_model = train_classification_model(stock_data)

    # Get the latest stock data
    latest_stock = stock_data.iloc[-1:]
    future_price = regression_model.predict([[latest_stock['Timestamp'].values[0]]])[0]
    decision = classification_model.predict(latest_stock[['Open', 'High', 'Low', 'Volume']].values)[0]

    # Map decision to Buy/Sell/Hold
    decision_map = {-1: "Sell", 0: "Hold", 1: "Buy"}
    recommendation = decision_map.get(decision, "Hold")

    return jsonify({
        "future_price": round(future_price, 2),
        "recommendation": recommendation
    })

@app.route("/companies", methods=["GET"])
def get_companies():
    companies = data['Ticker'].unique().tolist()
    return jsonify(companies)

if __name__ == "__main__":
    app.run(debug=True)