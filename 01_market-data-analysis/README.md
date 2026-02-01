# Project 01: Quantitative Market Analysis & Regime Detection

## Executive Summary
This project transitions from basic data visualization to a **Quantitative Research Framework**. It implements risk-adjusted performance metrics and a market-regime classification system to identify high-probability trading environments for EUR/USD and major equities.

## Advanced Features
### 1. Risk & Performance Analytics
* **Rolling Sharpe Ratio:** Annualized risk-adjusted returns using a 20-day lookback.
* **Maximum Drawdown (MDD):** "Underwater" analysis to quantify peak-to-trough risk.
* **Annualized Volatility:** Realized 20-day volatility to identify market stress.

### 2. Market Regime Framework
I developed a dual-factor regime model to categorize the market into four distinct states:
* **Trend Factor:** MA20/MA50 Crossover (Bullish vs. Bearish).
* **Volatility Factor:** Dynamic 50-day rolling median threshold (High vs. Low Vol).



## Key Insights
| Market State | Characteristics | Quantitative Finding |
| :--- | :--- | :--- |
| **Bullish / Low Vol** | Stable Growth | Highest Sharpe Ratio; ideal for trend-following strategies. |
| **Bearish / High Vol** | Panic/Crisis | High correlation across assets; maximum drawdown risk. |
| **Neutral / High Vol** | Mean Reversion | Choppy price action; high risk of "whipsaw" in trend signals. |

## Cross-Asset Dynamics
Using a **Correlation Heatmap**, I analyzed the relationships between EURUSD, USDJPY, AAPL, and MSFT.
* **Finding:** Diversification benefit is highest between FX and Equities during Low Vol regimes, but correlations "tend to 1" during market stress.



## Tech Stack
* **Analysis:** Python, Pandas, NumPy
* **Visualization:** Matplotlib (with custom "Underwater" and "Regime" overlays), Seaborn
* **Environment:** Termux (Mobile Linux) / Jupyter

## Interactive Report
View the full research notebook here: 
[Open Quant Report (HTML Preview)](https://htmlpreview.github.io/?https://github.com/Qatanajs/Quant-portfolio/blob/main/01_market-data-analysis/results/market_analysis.html)
