import ccxt
import pandas as pd
import numpy as np

zigzag_len = 2 # ZigZag Length
show_zigzag = True # Show Zigzag
fib_factor = 0.33 # Fib Factor for breakout confirmation, 0 ~ 1

symbol = "ETH/BUSD"  # Binance
pos_size = 1
timeframe = "5m"

# API
account_binance = ccxt.binance({
    "apiKey": '',
    "secret": '',
    "enableRateLimit": True,
    'options': {
        'defaultType': 'spot'
    }
})
ohlcvLB = account_binance.fetch_ohlcv(symbol, timeframe)
dfLB = pd.DataFrame(ohlcvLB, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
dfLB.to_excel("data_ETHBUSD_5m.xlsx")