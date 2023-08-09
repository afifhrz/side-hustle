from builder_v2 import *
import numpy as np
import time
import matplotlib.pyplot as plt

def solve_PDE():
    
    # initial value
    L = 50 #in ft
    dx = 1 
    M = L//dx
    P_0 = 5000 * np.ones([M, 1]) # P init
    P_prev = P_0.copy()
    P_left = 4500
    dt = 0.0069
    perm = 10
    por = 0.10
    eta = 0.00633 * perm / por
    tol = 1e-6
    
    # Initialize x
    P_west_0, P_east_0 = create_P_west_east(P_0, P_left)
    alpha_0 = alpha(P_0, P_east_0, P_west_0, dx)
    beta_0 = beta(P_0, P_prev, dx, dt, eta)
    gamma_0 = gamma(P_0, P_east_0, P_west_0, dx)
    
    O_0 = create_O_n(P_0, alpha_0, beta_0, gamma_0)
    e_n = -1*O_0
    e_n[0,0] = e_n[0,0] - alpha_0[0,0]*P_left
    e_prev = e_n.copy()
    e_dot = -1*e_prev/dt
    
    w_n_T = np.random.rand(len(P_0), 1)
    # w_n_T shape (50,1)
    w_prev = w_n_T.copy()
    v_n = np.random.rand(len(P_0)*3, 1)
    # v_n shape (150,1)
    v_prev = v_n.copy()
    
    Fv = 1600
    Fw = 1500
    lamb = 300
    
    S = calc_s(e_dot, lamb, e_n)
    x = create_x(e_n,e_dot,np.zeros((len(P_0),1)))
    delta_p = w_n_T * rbf_sigmoid(v_n.T@x)
    max_iter = 200
    n = 0
    
    # to run GUI event loop
    plt.ion()
    x_ = np.linspace(0, L, M)
    
    # here we are creating sub plots
    figure, ax = plt.subplots(figsize=(10, 8))
    line1, = ax.plot(x_, P_0)
    
    # setting title
    # plt.title("Geeks For Geeks", fontsize=20)
    
    # setting x-axis label and y-axis label
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    while n < max_iter:
        print("Looping ke:",n)
        print(abs(max(e_n)))
        # print(P_0)
        
        if np.isnan(abs(max(e_n))):
            break
        
        if abs(max(e_n)) <= tol:    
            break
        
        DELT_v = delta_v(Fv,x,S,w_prev,v_prev)
        v_n = v_prev+DELT_v
        DELT_w = delta_w(Fw,v_prev,x,S)
        w_n_T = w_prev+DELT_w.T
        
        
        v_prev = v_n.copy()
        w_prev = w_n_T.copy()
        
        P_prev = P_0.copy()
        P_0 = P_0+delta_p
        
        P_west_0, P_east_0 = create_P_west_east(P_0, P_left)
        alpha_0 = alpha(P_0, P_east_0, P_west_0, dx)
        beta_0 = beta(P_0, P_prev, dx, dt, eta)
        gamma_0 = gamma(P_0, P_east_0, P_west_0, dx)
        
        O_0 = create_O_n(P_0, alpha_0, beta_0, gamma_0)
        e_n = -1*O_0
        e_n[0,0] = e_n[0,0] - alpha_0[0,0]*P_left
        e_dot = -1*e_prev/dt
        e_prev = e_n.copy()
        
        S = calc_s(e_dot, lamb, e_n)
        x = create_x(e_n,e_dot,np.zeros((len(P_0),1)))
        delta_p = w_n_T * rbf_sigmoid(v_n.T@x)
        
        # plotting
        # updating data values
        line1.set_xdata(x_)
        line1.set_ydata(P_0)
    
        # drawing updated values
        figure.canvas.draw()
    
        # This will run the GUI event
        # loop until all UI events
        # currently waiting have been processed
        figure.canvas.flush_events()
    
        time.sleep(1)
        
        n += 1
    
    
if __name__=="__main__":
    solve_PDE()