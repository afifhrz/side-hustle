import math
import matplotlib.pyplot as mpl

def monthly_cost(principal, interest_rate, years):
    monthly_rate = interest_rate/12
    # interest rate is given in % so need to divide by 100
    r = monthly_rate/100
    n_payments = years * 12
    return principal * ((r * math.pow(1 + r, n_payments)) /
    (math.pow(1 + r, n_payments) - 1))
years = range(10,26)

# looping = 10
# while looping > i:
#     # code
#     i+=1

# range(11) -> = [0,1,2,3,4,5,6,7,8,9,10]

# for i in range(10):
    # code

mc = [monthly_cost(600000, 2.5, y) for y in years]

mc = []
for y in years:
    mc.append(monthly_cost(600000, 2.5, y))

# mc = [100]
# mc = [100,200]

mpl.plot(years, mc, ’g-’)
mc = [monthly_cost(600000, 3.5, y) for y in years]
mpl.plot(years, mc, ’b-’)
mc = [monthly_cost(600000, 4.5, y) for y in years]
mpl.plot(years, mc, ’r-’)
mpl.show()