# download_data.py
import yfinance as yf
import pandas as pd
import os

# Ensure data folder exists
if not os.path.exists('../data'):
    os.makedirs('../data')

# Define the tickers (Forex or stocks)
tickers = ['EURUSD=X', 'USDJPY=X', 'AAPL', 'MSFT']

# Define start and end dates
start_date = '2024-01-01'
end_date = '2026-01-01'

# Download data
for ticker in tickers:
    df = yf.download(ticker, start=start_date, end=end_date)
    df.to_csv(f'../data/{ticker.replace("=","")}.csv', index=True)
    print(f'Data saved for {ticker}')
