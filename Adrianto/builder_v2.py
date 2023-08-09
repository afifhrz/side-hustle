import numpy as np

# define P west and P east
def create_P_west_east(P_cell, P_left):
    P_west = np.zeros_like(P_cell)
    P_east = np.zeros_like(P_cell)

    for i in range(len(P_cell)):
        if i == 0:  # most-left grid
            P_west[i] = P_left
            P_east[i] = P_cell[i + 1]
        elif i == len(P_cell) - 1:  # most-right grid
            P_west[i] = P_cell[i - 1]
            P_east[i] = P_cell[i]
        else:
            P_west[i] = P_cell[i - 1]
            P_east[i] = P_cell[i + 1]
    return P_west, P_east

def alpha(P_cell, P_east, P_west, dx):
    a = ((P_west / (mu_gas(P_west) * z_factor(P_west))) +
         4 * (P_cell / (mu_gas(P_cell) * z_factor(P_cell))) -
         (P_east / (mu_gas(P_east) * z_factor(P_east)))) / (4 * dx**2)
    return a

def beta(P_cell, P_cell_prev, dx, dt, eta):
    b = (2 * (P_cell / (mu_gas(P_cell) * z_factor(P_cell))) / dx**2) + \
        ((1 / (eta * dt)) * ((1 / z_factor(P_cell)) - (P_cell_prev / (P_cell * z_factor(P_cell_prev)))))
    return b

def gamma(P_cell, P_east, P_west, dx):
    g = (-(P_west / (mu_gas(P_west) * z_factor(P_west))) +
         4 * (P_cell / (mu_gas(P_cell) * z_factor(P_cell))) +
         (P_east / (mu_gas(P_east) * z_factor(P_east)))) / (4 * dx**2)
    return g

def mu_gas(p):
    # Gas viscosity (Gonzalez, Bukacek and Lee, 1967)
    press = np.array([2000, 2500, 3000, 3500, 4000, 4500, 5000, 6000])
    visc = np.array([0.0164, 0.0174, 0.0186, 0.0197, 0.0209, 0.0220, 0.0233, 0.0257])
    fit = np.polyfit(press, visc, 1)
    mu = np.polyval(fit, p)
    return mu

def z_factor(p):
    # Papay correlation
    T = 679.7  # 220 F
    Pc = 673
    Tc = 344  # Critical properties of methane
    ppr = p / Pc
    tpr = T / Tc
    z_fact = 1 - ((3.53 * ppr) / (10**(0.9813 * tpr))) + ((0.274 * ppr**2) / (10**(0.815 * tpr)))
    return z_fact

# define On
def create_O_n(P_cell, alpha_n, beta_n, gamma_n):
    
    alpha_d = np.column_stack((np.diagflat(alpha_n[1:-1]),np.zeros((len(alpha_n)-2, 2))))
    beta_d = np.column_stack((np.diagflat(beta_n[1:-1],1)[:-1],np.zeros((len(beta_n)-2, 1))))
    gamma_d = np.diagflat(gamma_n[1:-1],2)[:-2]
    
    result = alpha_d + beta_d + gamma_d
    
    first_row = np.zeros((1,len(P_cell)))
    first_row[0,0] = -beta_n[0,0]
    first_row[0,1] = gamma_n[0,0]
    
    last_row = np.zeros((1,len(P_cell)))
    last_row[0,-2] = -alpha_n[0,-1]
    last_row[0,-1] = gamma_n[0,-1] - beta_n[0,-1]
    
    result = np.vstack((first_row, result))
    result = np.vstack((result,last_row))
    print(result)
    exit()
    result = result@P_cell
    return result

def create_x(e_n, e_dot, D_n):
    return np.hstack([e_n,e_dot,D_n]).reshape((-1,1))

def rbf_sigmoid(x):
    return 1 / (1 + np.e ** -np.abs(x))

def rbf_sigmoid_derivative(x):
    return rbf_sigmoid(x) * (1 - rbf_sigmoid(x))

def calc_s(e_dot, lamb, en):
    return e_dot+lamb*en

def delta_v(Fv, X, S, w_prev, v_prev):
    return Fv*X@S.T@w_prev*rbf_sigmoid_derivative(v_prev.T@X)

def delta_w(Fw, v_prev, x, S):
    print(Fw)
    print(v_prev)
    print(x)
    print(S)
    exit()
    return Fw*rbf_sigmoid(v_prev.T@x)@S.T