# Market Data Analysis 📈

## Overview
This module focuses on the ingestion and exploratory analysis of financial time series. The goal is to establish a clean data pipeline for AAPL and EUR/USD to serve as the foundation for future backtesting.

## Key Technical Achievements
* **Automated Ingestion:** Developed scripts to pull historical data using the `yfinance` API.
* **Data Cleaning:** Implemented forward-filling (`ffill`) logic to handle missing timestamps in FX data.
* **Statistical Analysis:** Calculated Log Returns to ensure time-series additivity for future modeling.
* **Visualization:** Built technical overlays including 20-day and 50-day Simple Moving Averages (SMA).

## Insights
* Observed a bullish crossover on the AAPL 20/50 SMA during [Insert Date].
* Confirmed that log returns for EUR/USD exhibit "fat tails," deviating from a standard normal distribution—a key risk factor for Project 03 (Risk Management).
