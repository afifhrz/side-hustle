"""
z0 = y
z1 = dy/dt = dz0/dt
z2 = d^2 y/dt^2 = dz1/dt
dz2/dt = 1 - 5z0 - 3z1 - 10z2

z0 k+1 = z0 + z1 k * delta t
z1 k+1 = z1 + z2 k * delta t
z2 k+1 = z2 + (1 - 5z0 k - 3z1 k - 10z2 k) * delta t
"""
import numpy as np
import matplotlib.pyplot as plt

def solveDEQ(a0, a1, a2, a3, dt, tfinal):
    tspace = np.linspace(0, tfinal, int(tfinal/dt))
    # initial condition
    result = []
    z0 = 0
    z1 = 0
    z2 = 0
    result.append(z0)
    
    for i in tspace[1:]:
        z0 = z0 + z1*dt
        z1 = z1 + z2*dt
        z2 = z2 + (1 - a0*z0 - a1*z1 - a2*z2) * dt/a3
        result.append(z0)

    plt.plot(tspace, result,  label='Numerical Solution')
    plt.grid()
    plt.legend()
    plt.show()
    
a0 = 5
a1 = 3
a2 = 10
a3 = 1
dt = 0.01
tfinal = 20

solveDEQ(a0=a0, a1=a1, a2=a2, a3=a3, dt=dt, tfinal=tfinal)

def solveDEQ2(a, dt, tfinal, fn):
    ''' plots the solution to the differential of the form
        a3 d3y/dt3 + a2 d2y/dt2 + a1 dy/dt + a0 y = fn(t)
        with zero initial conditions for 0<t<tfinal
        inputs: a = a list of the equation constants = [a0, a1, a2, a3]
                dt = time step used in solving the equation,
                tfinal = final time of simulation
                fn = a function fn(t) that is the forcing function
        Outputs: t, y the solution to the DEQ for 0 <= t =< tfinal '''
    tspace = np.linspace(0, tfinal, int(tfinal/dt))
    
    # initial condition
    result = []
    z0 = 0
    z1 = 0
    z2 = 0
    result.append(z0)
    input_fnt = 0
    for i in tspace[1:]:
        z0 = z0 + z1*dt
        z1 = z1 + z2*dt
        z2 = z2 + (fn(input_fnt+i) - a[0]*z0 - a[1]*z1 - a[2]*z2) * dt/a[3]
        result.append(z0)

    plt.plot(tspace, result,  label='Numerical Solution')
    plt.grid()
    plt.legend()
    plt.show()
import math
a = [5,4,2,2] 
dt = 0.01
tfinal = 20
solveDEQ2(a, dt, tfinal, lambda t: math.cos(3*t))