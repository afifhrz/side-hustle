import math
import numpy as np
import matplotlib.pyplot as plt

def EulerODE(func, t0, tf, y0, n):

    # calculate step size
    h = (tf-t0)/n
    result = [y0]
    for i in range(n):
        slope = func(y0, t0)
        yn = y0 + h * slope
        result.append(yn)
        y0 = yn
        t0 = t0+h
    return result
  
ft = lambda y,t: y*(t**2) - 1.1*y
exact_solution = lambda t: math.exp(t**3/3 - 1.1*t)

t0 = 0
tf = 2.2
y0 = 1

n_exact = 100
y_exact_solution = []

for i in np.linspace(t0,tf,n_exact+1):
    y_exact_solution.append(exact_solution(i))

n = 10    
numerical_solution = EulerODE(ft, t0, tf, y0, n)

n_20 = 20    
numerical_solution_20 = EulerODE(ft, t0, tf, y0, n_20)

plt.plot(np.linspace(t0,tf,n_exact+1),y_exact_solution,  label='Exact Solution')
plt.plot(np.linspace(t0,tf,n+1),numerical_solution, label='Numerical Solution n=10')
plt.plot(np.linspace(t0,tf,n_20+1),numerical_solution_20, label='Numerical Solution n=20')
plt.title("Compare Exact Solution vs Euler N= 10 vs Euler N= 20")
plt.legend()
plt.show()

# Question B
ft = lambda y,t: (1+4*t)*math.sqrt(y)
exact_solution = lambda t: (t**2 + 0.5*t + 1)**2

t0 = 0
tf = 1.5
y0 = 1

n_exact = 100
y_exact_solution = []
for i in np.linspace(t0,tf,n_exact+1):
    y_exact_solution.append(exact_solution(i))

n = 10    
numerical_solution = EulerODE(ft, t0, tf, y0, n)

n_20 = 20    
numerical_solution_20 = EulerODE(ft, t0, tf, y0, n_20)

plt.plot(np.linspace(t0,tf,n_exact+1),y_exact_solution,  label='Exact Solution')
plt.plot(np.linspace(t0,tf,n+1),numerical_solution, label='Numerical Solution n=10')
plt.plot(np.linspace(t0,tf,n_20+1),numerical_solution_20, label='Numerical Solution n=20')
plt.title("Compare Exact Solution vs Euler N= 10 vs Euler N= 20")
plt.legend()
plt.show()

# Challenge
ft = lambda y,t: y*(t**2) - 1.1*y
exact_solution = lambda t: math.exp(t**3/3 - 1.1*t)

t0 = 0
tf = 2.2
y0 = 1

nlist = []
yapp = []
yex = exact_solution(2.2)
err = []

for m in range(2,11):
    n = 2**m
    nlist.append(n)
    numerical_solution = EulerODE(ft, t0, tf, y0, n)
    yapp.append(numerical_solution[-1])
    err.append(abs((yex-numerical_solution[-1])/yex)*100)

# plot the percent relative error vs. 𝑛 in a log-log plot
plt.figure()
plt.loglog(nlist, err,"*-")
plt.xlabel("n, number of intervals")
plt.ylabel("Percent relative error")
plt.grid()
plt.show()