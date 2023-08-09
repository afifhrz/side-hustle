import numpy as np
def T(limit, bound):
    x_for_y = np.linspace(0,limit,5000)
    y = (4*x_for_y**2-2)*np.exp(-(x_for_y**2))
    n = int(np.ceil(np.sqrt((limit**3)*max(abs(y[1:]))/(12*bound))))
    x = np.linspace(0,limit,n+1)
    h = limit/n
    sum_area = 0
    sum_area += 1/2*np.exp(-x[0]**2)
    sum_area += 1/2*np.exp(-x[-1]**2)
    sum_area += sum(np.exp(-x[1:-1]**2))
    
    total_area = h * sum_area
    
    return total_area

print(T(1,0.1))
print(T(1,0.01))
print(T(1,0.001))
print(T(1,0.0001))
print(T(2,0.1))
print(T(2,0.01))
print(T(2,0.001))
print(T(2,0.0001))