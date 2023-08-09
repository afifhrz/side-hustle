from scipy import stats
import random
import pandas as pd
import numpy as np
import math

# s_0 = 147.383331
# ekspektasi_return = -0.004619266
# volatility = .08624000
# interest_rate = .225
partition_of_time = 0.08
# strike_price = 149.313339

# data_temp = []
# for i in range(10):
#     data_temp.append(stats.norm.ppf(random.random(), loc=ekspektasi_return , scale=volatility))

# data_result = pd.DataFrame(data_temp, columns=['return'])
# data_result['price'] = s_0 * (1+data_result['return'])
# data_result['simulated_call_c'] = data_result["price"].apply(lambda x: math.exp(-interest_rate*partition_of_time) * max(x-strike_price, 0))

# print(data_result.simulated_call_c.mean())

data = pd.read_csv('final_project/calculation/tsla.csv')
print(np.log(1+data.pct_change().fillna(0)))
data['return'] = np.log(1+data.pct_change().fillna(0))
data['variansi'] = (data['return']-data['return'].mean())**2
variansi =(data.variansi.sum())/(data.shape[0]-1)
volatility =(1/math.sqrt(partition_of_time)) * math.sqrt(variansi)
