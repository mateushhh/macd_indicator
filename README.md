# MACD Trading Strategy Visualisation 📊

## Project Overview 🛠️
This project implements a trading strategy based on the **MACD (Moving Average Convergence Divergence)** indicator. The algorithm analyzes financial market data, identifies buy and sell signals, and simulates trading decisions, presenting results through visualizations.

## How Does MACD Work? 📈
MACD helps assess market trends by analyzing two exponential moving averages:
- **MACD Line**: The difference between the 12-period and 26-period EMA (Exponential Moving Average)
- **SIGNAL Line**: A 9-period EMA of the MACD values

The crossovers of these lines generate trading signals:
- 📈 **Buy** – when MACD crosses SIGNAL from below
- 📉 **Sell** – when MACD crosses SIGNAL from above

## Features 💸
- Reads market data from a `.csv` file
- Calculates **EMA, MACD, and SIGNAL**
- Detects buy and sell signals
- Simulates trading activity and tracks portfolio value
- Generates charts with transaction markers and performance analysis

## Requirements 🔧
- Python 3.x
- `matplotlib` (for data visualization)

Install dependencies:
```sh
pip install matplotlib
```

## Usage ▶️
1. **Prepare Data**
   - The `.csv` file should contain market data with closing prices in the **5th column** (index `4`).
   - Example data can be obtained from **forexsb.com/historical-forex-data**.

2. **Run the Script**
   ```sh
   python main.py
   ```

3. **Analyze Results**
   - **Price Chart** – shows asset value fluctuations
   - **MACD & SIGNAL** – displays buy and sell signals
   - **Portfolio Simulation** – visualizes how the portfolio value evolves

## Example Output 🏆
```python
Data file: ./data/GOLD-USD-1D.csv

Total transactions: 207
Profitable transactions: 78
Failed transactions: 129

Initial capital: $1000.00
Final capital: $2080.92
Net profit: $1080.92
Return on investment: 208.09%
```

## Important Notes 📜
- The first **2N** days of MACD and SIGNAL values may be unstable.
- The simulation does not account for transaction fees.
- The strategy works best in long-term market trends.

---

## Functions 🔍
```python
# Reads market data and extracts closing prices.
def read_data(filename)

# Computes the exponential moving average for a given period `n`.
def EMA(n, data)

# Calculates MACD values based on EMA(12) and EMA(26) of the closing prices.
def MACD(close)

# Computes the SIGNAL line using EMA(9) of the MACD values.
def SIGNAL(macd)

# Identifies buy and sell signals.
def get_intersections(macd, signal)

# Simulates investment decisions and calculates financial performance.
def simulate(intersections, close, start_money=1000):

# Generates a comprehensive visualization of all analytical data.
def draw_everything(close, macd, signal, balance):
```