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
if len(ohlcvLB):
    dfLB['time'] = pd.to_datetime(dfLB['time'], unit='ms')
    # print(df)  # this is the dataframe

high_points_arr = np.zeros(5, dtype=float)
high_index_arr = np.zeros(5)
low_points_arr = np.zeros(5, dtype=float)
low_index_arr = np.zeros(5)
bu_ob_boxes = np.zeros((5, 4), dtype=float)
be_ob_boxes = np.zeros((5, 4), dtype=float)
# left top right bottom
zigzag_points = []

data = np.array(dfLB[['open', 'high', 'low', 'close']])
l0is = np.zeros(zigzag_len)
h0is = np.zeros(zigzag_len)
trend = 1
market = 1
last_up_idx = 0
last_down_idx = 0
last_l0 = 0
last_h0 = 0
bu_ob_index = 0
be_ob_index = 0

def f_get_high(ind):
    return [high_points_arr[np.size(high_points_arr) - 1 - ind], high_index_arr[np.size(high_index_arr) - 1 - ind]]

def f_get_low(ind):
    return [low_points_arr[np.size(low_points_arr) - 1 - ind], low_index_arr[np.size(low_index_arr) - 1 - ind]]

for i in range(zigzag_len-1, int(np.size(data) / 4)):
    open = data[i, 0]
    high = data[i, 1]
    low = data[i, 2]
    close = data[i, 3]
    highest = data[i-zigzag_len+1:i+1, 1].max()
    to_up = (high >= highest)
    lowest = data[i-zigzag_len+1:i+1, 2].min()
    to_down = (low <= lowest)
    
    trendchange = False
    if (trend == 1 and to_down):
        trend = -1
        trendchange = True
    elif (trend == -1 and to_up):
        trend = 1
        trendchange = True

    if last_up_idx + 2 >= i:
        low_val = data[i, 2]
        low_index = i
    else:
        u = data[last_up_idx + 2:i + 1, 2]
        low_val = u.min()
        low_index = np.argwhere(u==low_val)[-1][0] + last_up_idx+1
        
    if last_down_idx + 2 >= i:
        high_val = data[i, 1]
        high_index = i
    else:
        u = data[last_down_idx+2:i+1, 1]
        high_val = u.max()
        high_index = np.argwhere(u==high_val)[-1][0] + last_down_idx+1
        
    if trendchange:
        if trend == 1:
            zigzag_points.append([0, i, low_val])
            low_points_arr = np.append(low_points_arr, low_val)
            low_index_arr = np.append(low_index_arr, low_index)
        if trend == -1:
            zigzag_points.append([1, i, high_val])
            high_points_arr = np.append(high_points_arr, high_val)
            high_index_arr = np.append(high_index_arr, high_index)

    [h0, h0i] = f_get_high(0)
    [h1, h1i] = f_get_high(1)

    [l0, l0i] = f_get_low(0)
    [l1, l1i] = f_get_low(1)

    l0is = np.append(l0is, l0i)
    h0is = np.append(h0is, h0i)

    marketchange = False
    if (last_l0 != l0 and last_h0 != h0):
        if (market == 1 and l0 < l1 and l0 < (l1 - abs(h0 - l1) * fib_factor)):
            market = -1
            marketchange = True
        elif (market == -1 and h0 > h1 and h0 > (h1 + abs(h1 - l0) * fib_factor)):
            market = 1
            marketchange = True

    for j in range(int(h1i), int(l0is[np.size(l0is) - zigzag_len - 1] + 1)):
        if (data[j, 0] > data[j, 3]):
            bu_ob_index = j

    for j in range(int(l1i), int(h0is[np.size(h0is) - zigzag_len - 1] + 1)):
        if (data[j, 0] < data[j, 3]):
            be_ob_index = j

    # print(i, trend, market, last_h0, last_l0, h1, l1)

    if marketchange:
        last_h0 = h0
        last_l0 = l0
        if market == 1:
            print("Green Line: ", h1i, h1, h0i, h1)
            bu_ob_boxes = np.concatenate([bu_ob_boxes, np.array([[bu_ob_index, data[bu_ob_index, 1], i, data[bu_ob_index, 2]]])])
        elif market == -1:
            print("Red Line: ", l1i, l1, l0i, l1)
            be_ob_boxes = np.concatenate([be_ob_boxes, np.array([[be_ob_index, data[be_ob_index, 1], i, data[be_ob_index, 2]]])])
    
    j = 0
    while j < int(np.size(bu_ob_boxes) / 4):
        bull_ob = bu_ob_boxes[j]
        bull_bottom = bull_ob[3]
        if (close < bull_bottom):
            bu_ob_boxes = np.delete(bu_ob_boxes, j, 0)
        elif np.size(bu_ob_boxes) == 20:
            bu_ob_boxes = np.delete(bu_ob_boxes, 0, 0)
        else:
            bu_ob_boxes[j][2] = i
            j = j + 1
    
    j = 0
    while j < int(np.size(be_ob_boxes) / 4):
        bear_ob = be_ob_boxes[j]
        bear_top = bear_ob[1]
        if (close > bear_top):
            be_ob_boxes = np.delete(be_ob_boxes, j, 0)
        elif np.size(be_ob_boxes) == 20:
            be_ob_boxes = np.delete(be_ob_boxes, 0, 0)
        else:
            be_ob_boxes[j][2] = i
            j = j + 1

    if (to_up == True):
        last_up_idx = i
    if (to_down == True):
        last_down_idx = i

j = 0
while j < int(np.size(bu_ob_boxes) / 4):
    if bu_ob_boxes[j][1] == 0 and bu_ob_boxes[j][3] == 0:
        bu_ob_boxes = np.delete(bu_ob_boxes, j, 0)
    else:
        j = j + 1

j = 0
while j < int(np.size(be_ob_boxes) / 4):
    if be_ob_boxes[j][1] == 0 and be_ob_boxes[j][3] == 0:
        be_ob_boxes = np.delete(be_ob_boxes, j, 0)
    else:
        j = j + 1

for point in zigzag_points:
    if point[0] == 0:
        print("Low: ", point[1], point[2])
    else:
        print("High: ", point[1], point[2])

for bull_ob in bu_ob_boxes:
    print("Bull: ", bull_ob)

for bear_ob in be_ob_boxes:
    print("Bear: ", bear_ob)
