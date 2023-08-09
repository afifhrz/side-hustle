import numpy as np
import math
from scipy import optimize, integrate

def F(x, mean=0, var=1):
    f = lambda x: 1 / np . sqrt (2* np .pi * var ) * np . exp ( -0.5 * ( np .array ( x ) - mean ) ** 2 / var )
    return integrate.quad(f, -np.inf, x)[0]

def inv_F(prob, mean=0, var=1):
    new_f = lambda x : prob -  1 / np.sqrt (2* np .pi * var ) * (np.sqrt(np.pi)*var*(math.erf((np.sqrt(2)*x-np.sqrt(2)*mean)/(2*var))+1))/np.sqrt(2)
    try:
        F_inv = optimize.bisect(new_f,-3+mean,3+mean)
    except ValueError:
        F_inv = np.nan
    return F_inv

print(inv_F(0.35))
print(F(inv_F(0.35)))
print(inv_F(0.35, 2, 1))
print(F (inv_F( 0.35 , 2 , 1), 2, 1))
print(inv_F(-0.5))