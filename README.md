# MACD Trading Strategy Simulation

## Overview 📈
This project implements a simple trading strategy based on the **Moving Average Convergence Divergence (MACD)** indicator. It reads financial data, calculates the MACD and Signal line, identifies buy and sell signals, and simulates trading performance over time.

## Features 🚀
- Reads financial data from a `.csv` file.
- Calculates **Exponential Moving Average (EMA)**.
- Computes the **MACD** and **Signal** line.
- Identifies **buy** and **sell** signals based on MACD crossover.
- Simulates trading decisions and tracks balance evolution.
- Plots relevant financial data and indicators.

## Requirements 🔧
- Python 3.x
- `matplotlib` (for plotting)

Install required dependencies using:
```sh
pip install matplotlib
```

## Usage ▶️
### 1. Prepare Data
Ensure you have a properly formatted data file with **tab-separated values** where:
- The **5th column** (index `4` in zero-based indexing) represents the closing price.
This is standard file format if you use data from **forexsb.com/historical-forex-data** which I used to get example data.

### 2. Run the Program
Execute the script using:
```sh
python script.py
```

### 3. Interpretation of Plots
- **Price Data**: Shows the closing price trend over time
- **MACD & Signal Line**: Identifies buy (green triangle) and sell (red triangle) signals.
- **Balance Evolution**: Displays the performance of simulated trading.

## Functions
### `read_data(filename)`
Reads financial data and extracts the closing prices.

### `EMA(n, data)`
Computes the Exponential Moving Average for a given period `n`.

### `MACD(close)`
Calculates the MACD values based on EMA(12) and EMA(26).

### `SIGNAL(macd)`
Computes the Signal line using EMA(9) of the MACD values.

### `get_intersections(macd, signal)`
Identifies buy and sell signals based on MACD crossover.

### `simulate(intersections, close, start_money=1000)`
Simulates trading based on the generated signals, tracking profit/loss.

### `draw_data(data, x0=0, x1=0)`
Plots the closing price data.

### `draw_MACD(macd, signal, x0=0, x1=0)`
Plots the MACD and Signal lines along with buy/sell signals.

### `draw_balance(balance, x0=0, x1=0)`
Visualizes the account balance changes over time.

### `draw_everything(close, macd, signal, x0=0, x1=0)`
Combines all visualizations into one comprehensive analysis.

## Example Output 
```python
Data used: ./data/GOLD-USD-1D.csv

Total transactions: 207
Profitable transactions: 78
Failed transactions: 129

Money before transactions: 1000.00
Money after transactions: 2080.92
Earnings: 1080.92
Profit [%]: 208.09
```

## Notes 📜
- The first **2N** days of EMA calculations may be unstable.
- The simulation assumes all-in trading without risk management strategies.
