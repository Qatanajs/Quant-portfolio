01. Market Data Analysis
​Goal
​To develop a robust automated pipeline for collecting, cleaning, and visualizing historical FX and stock market data, forming the foundation for quantitative strategy development.
​Data
​Sources: Yahoo Finance API (yfinance)
​Assets:
​Forex: EUR/USD, USD/JPY
​Equities: AAPL, MSFT
​Features: Open, High, Low, Close, Adj Close, Volume
​Steps Completed (Week 1)
​Automated Ingestion: Developed download_data.py to fetch historical time-series data using Python and yfinance.
​Data Persistence: Implemented cleaning protocols to handle multi-index headers and saved finalized data as CSV files.
​Exploratory Data Analysis (EDA):
​Calculated Descriptive Statistics (mean, std dev, skewness).
​Audited for Missing Values and data gaps.
​Visualization:
​Time-series plots of Closing Prices.
​Histograms of Daily Returns to analyze distribution.
​Technical overlays: 20-day & 50-day Simple Moving Averages (SMA).
​Output: Successfully partitioned and saved processed data in the /data directory for downstream backtesting.
