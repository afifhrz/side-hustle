# S_t: the spot price of the underlying asset at time t
# r: the risk-free interest rate
# sigma: the volatility of returns of the underlying asset
# K: the strike price or exercise price of the option
# C0: the price of a European call option at time t = 0
# t: current time in years
# T: expiry or maturity date
# N: number of realizations for Monte Carlo simulation

# lognormal distribution of the price
import numpy as np
import matplotlib.pyplot as plt


S0 = 100  
r = 0.05  
sigma = 0.25  
K = 105
T = 1.0  
N = 10000
Z = np.random.normal(size=N)

ST = S0*np.exp((r-0.5*sigma**2)*T+sigma*np.sqrt(T)*Z)  
# plt.hist(ST, bins='auto')  
# plt.xlabel('price')
# plt.ylabel('ferquency')
# plt.show()

# Monte Carlo simulation
weeks = 52  
dt = T/weeks  
S = np.zeros((weeks+1, N))  
S[0] = S0  
for t in range(1, weeks+1):
    Z = np.random.normal(size=N)
    S[t] = S[t-1]*np.exp((r-0.5*sigma**2)*dt+sigma*np.sqrt(dt)*Z)
    
for i in range(0, N):
    plt.plot(range(1,weeks+2), S[:,i])

plt.show()