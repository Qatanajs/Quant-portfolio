import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load data with the correct lowercase 'date' column
df = pd.read_csv('../data/EURUSDX.csv')

# 2. Standardize column names to lowercase to avoid CaseErrors
df.columns = [col.lower() for col in df.columns]

# 3. Set index and sort
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df = df.sort_index(ascending=True)

# 4. Calculate Moving Averages
df['sma20'] = df['close'].rolling(window=20).mean()
df['sma50'] = df['close'].rolling(window=50).mean()

# 5. Generate Signals (1 = Buy, 0 = Hold/Sell)
df['signal'] = 0
# We use .iloc to avoid SettingWithCopy warnings
df.iloc[50:, df.columns.get_loc('signal')] = np.where(
    df['sma20'][50:] > df['sma50'][50:], 1, 0
)

# 6. Calculate Returns
df['market_returns'] = df['close'].pct_change()
df['strategy_returns'] = df['market_returns'] * df['signal'].shift(1)

# 7. Print Summary
print(f"--- Backtest Results: EUR/USD ---")
print(f"Total Data Points: {len(df)}")
print(f"Cumulative Market Return: {(1 + df['market_returns']).prod() - 1:.2%}")
print(f"Cumulative Strategy Return: {(1 + df['strategy_returns']).prod() - 1:.2%}")

# 8. Plotting the results
plt.figure(figsize=(12, 6))
plt.plot(df['close'], label='EUR/USD Price', alpha=0.5)
plt.plot(df['sma20'], label='20-day SMA', alpha=0.9)
plt.plot(df['sma50'], label='50-day SMA', alpha=0.9)

# Mark the Buy signals
plt.plot(df[df['signal'] == 1].index, 
         df['close'][df['signal'] == 1], 
         '^', markersize=10, color='g', label='Buy Signal')

plt.title('EUR/USD SMA Crossover Strategy')
plt.legend()
plt.grid()

# Save the plot as an image
plt.savefig('../results/equity_curve.png')
print("Chart saved as ../equity_curve.png")

